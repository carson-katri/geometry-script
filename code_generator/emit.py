"""Render node signatures as the Python source of the generated node functions."""

from __future__ import annotations

import collections
import math
import typing
from dataclasses import replace

from .signatures import (
    NO_DEFAULT,
    ItemCollection,
    NodeMetatype,
    NodeSignature,
    snake_case,
    unique_name,
    unique_names,
)


_NULLABLE_SOCKET_TYPES = {
    "Object",
    "Image",
    "Collection",
    "Material",
    "Texture",
    "Shader",
    "Bundle",
    "Closure",
    "Font",
    "Scene",
    "Sound",
    "Text",
    "Mask",
}

# Generated functions are star-exported, so they must not hide Python names
# that scripts commonly use (e.g. the Math node and the `math` module).
_RESERVED_FUNCTION_NAMES = {
    "abs", "all", "any", "bool", "dict", "float", "format", "hash", "id",
    "input", "int", "len", "list", "map", "math", "max", "min", "next",
    "object", "pow", "random", "range", "round", "set", "slice", "sorted",
    "str", "string", "sum", "tuple", "type", "zip",
}

_DYNAMIC_STRUCTURE_SOCKET_TYPES = {
    "bool",
    "int",
    "float",
    "str",
    "Color",
    "Vector",
    "Vector2",
    "Vector4",
    "IntVector2",
    "IntVector3",
    "Rotation",
    "Matrix",
}

_ITEM_DOCS = {
    "values": "Items to add, by name; each socket type is inferred from its value.",
    "named": "Items to add, mapping each name to its input value.",
    "sequence": "Item input values, in order.",
    "types": "Items to add, mapping each name to its type (float, Vector, Geometry, ...).",
}


def emit_module(
    signatures: typing.Iterable[NodeSignature],
    *,
    tree_type: str,
    blender_version_string: str,
    blender_version: tuple[int, ...],
) -> str:
    """Return the source of a module with one function per node signature."""
    signatures = _disambiguate_function_names(list(signatures))
    signatures.sort(key=lambda signature: (signature.function_name, signature.output_type_name))

    lines = [
        f"# Generated from Blender {blender_version_string} ({tree_type}).",
        "# Do not edit: run code_generator/node_functions_generator.py instead.",
        "",
        "from __future__ import annotations",
        "",
        "import typing",
        "",
        "import bpy",
        "",
        "from .runtime import ItemOutputs, Socket, node_function as _node_function",
        "from .types import *",
        "",
        f"BLENDER_VERSION = {blender_version!r}",
        "",
        "__all__ = [",
        *(f"    {signature.function_name!r}," for signature in signatures),
        "]",
        "",
    ]
    for signature in signatures:
        lines.extend(_emit_signature(signature))
    return "\n".join(lines).rstrip() + "\n"


def _disambiguate_function_names(signatures: list[NodeSignature]) -> list[NodeSignature]:
    counts = collections.Counter(signature.function_name for signature in signatures)
    result: list[NodeSignature] = []
    used: set[str] = set()
    for signature in signatures:
        name = signature.function_name
        if name in _RESERVED_FUNCTION_NAMES:
            name += "_"
        if counts[signature.function_name] > 1:
            output_name = signature.output_type_name.removesuffix("Outputs")
            name = f"{name}_{snake_case(output_name, fallback='node')}"
        result.append(replace(signature, function_name=unique_name(name, used)))
    return result


def _python_literal(value: object) -> str:
    if value is NO_DEFAULT:
        raise ValueError("A missing socket default cannot be rendered as a literal")
    if isinstance(value, float):
        if math.isnan(value):
            return "float('nan')"
        if math.isinf(value):
            return "float('inf')" if value > 0 else "float('-inf')"
    if isinstance(value, tuple):
        contents = ", ".join(_python_literal(item) for item in value)
        if len(value) == 1:
            contents += ","
        return f"({contents})"
    if isinstance(value, (set, frozenset)):
        contents = ", ".join(
            _python_literal(item) for item in sorted(value, key=repr)
        )
        if isinstance(value, frozenset):
            return f"frozenset({{{contents}}})"
        return "{" + contents + "}" if value else "set()"
    return repr(value)


def _socket_structure_kind(socket: NodeMetatype) -> str | None:
    """Return the value structure represented by a socket, when explicit."""
    if socket.display_shape == "VOLUME_GRID" or socket.structure_type == "GRID":
        return "GRID"
    if socket.display_shape == "LIST" or socket.structure_type == "LIST":
        return "LIST"
    return None


def _output_structure_type(socket: NodeMetatype) -> str:
    """The structure the runtime gives an output socket; AUTO asks Blender."""
    if socket.structure_type in {"FIELD", "GRID", "LIST"}:
        return socket.structure_type
    return {
        "DIAMOND": "FIELD",
        "DIAMOND_DOT": "FIELD",
        "VOLUME_GRID": "GRID",
        "LIST": "LIST",
    }.get(socket.display_shape, "AUTO")


def _socket_value_type(socket: NodeMetatype, *, is_output: bool) -> str:
    members = socket.type.split(" | ")
    if len(members) == 1:
        return _single_socket_value_type(socket, is_output=is_output)
    # A type property can switch this socket between types; each member keeps
    # its own structure rules (e.g. Geometry is never a field).
    variants: list[str] = []
    nullable = False
    for member in members:
        member_type = _single_socket_value_type(
            replace(socket, type=member), is_output=is_output
        )
        if member_type.endswith(" | None"):
            nullable = True
            member_type = member_type.removesuffix(" | None")
        variants.extend(member_type.split(" | "))
    result = " | ".join(dict.fromkeys(variants))
    return f"{result} | None" if nullable else result


def _single_socket_value_type(socket: NodeMetatype, *, is_output: bool) -> str:
    base_type = socket.type
    structure_kind = _socket_structure_kind(socket)
    # Grid and List inputs have no usable scalar default; None means the DSL
    # leaves them unlinked.
    optional_structure = not is_output and not socket.is_multi_input

    if socket.enum_values:
        # Blender's menu identifiers are strings accepted by the socket's
        # default_value property, so a Literal can pass through unchanged.
        values = ", ".join(repr(value) for value in socket.enum_values)
        return f"typing.Literal[{values}]"
    if socket.is_menu:
        # The menu domain can depend on links and may not exist at generation
        # time. Keep the public Menu name; it is an annotated str.
        return "Menu"
    if structure_kind == "GRID":
        # A scalar RNA default on a grid socket is only the base socket's
        # storage default; it does not describe a grid (which also needs a
        # topology and transform).
        return f"Grid[{base_type}] | None" if optional_structure else f"Grid[{base_type}]"
    if structure_kind == "LIST":
        return f"List[{base_type}] | None" if optional_structure else f"List[{base_type}]"
    if (
        socket.structure_type == "DYNAMIC"
        or (socket.display_shape == "CIRCLE" and socket.supports_geometry_structures)
    ) and base_type in _DYNAMIC_STRUCTURE_SOCKET_TYPES:
        return " | ".join(
            (base_type, f"Field[{base_type}]", f"Grid[{base_type}]", f"List[{base_type}]")
        )
    if socket.structure_type == "FIELD" or (
        socket.supports_geometry_structures and socket.supports_field
    ):
        # A field socket can also take a single constant, which Blender
        # broadcasts over the field's domain.
        if is_output and socket.display_shape != "DIAMOND_DOT":
            return f"Field[{base_type}]"
        return f"{base_type} | Field[{base_type}]"
    if (
        not is_output
        and socket.default_value is None
        and base_type in _NULLABLE_SOCKET_TYPES
    ):
        return f"{base_type} | None"
    return base_type


def _argument_type(socket: NodeMetatype, *, is_output: bool) -> str:
    value_type = _socket_value_type(socket, is_output=is_output)
    if is_output:
        return f"Socket[{value_type}]"

    nullable = value_type.endswith(" | None")
    if nullable:
        value_type = value_type.removesuffix(" | None")
    socket_type = f"{value_type} | Socket[{value_type}]"
    if nullable:
        socket_type += " | None"
    if socket.is_multi_input:
        return f"typing.Sequence[{socket_type}]"
    return socket_type


def _input_default(socket: NodeMetatype) -> object:
    """The DSL default for an input; None leaves the socket unlinked."""
    if socket.is_multi_input:
        # Multi-input sockets collect links; an empty sequence means no links.
        return ()
    if _socket_structure_kind(socket) is not None:
        # Blender may expose the scalar backing property's default even though
        # a Grid/List input cannot be supplied by that scalar.
        return None
    if socket.default_value is NO_DEFAULT:
        # Sockets without an RNA default (Geometry, Matrix, ...) are valid
        # when unlinked.
        return None
    return socket.default_value


class _Parameters(typing.NamedTuple):
    """The Python parameter name of every input, property and item collection."""

    inputs: list[str]
    properties: list[str]
    items: list[tuple[str, ItemCollection]]


def _parameter_names(signature: NodeSignature) -> _Parameters:
    input_names = unique_names(snake_case(socket.name) for socket in signature.inputs)
    used = set(input_names)
    property_names: list[str] = []
    for prop in signature.properties:
        base_name = snake_case(prop.identifier)
        if base_name in used:
            base_name = f"{base_name}_property"
        property_names.append(unique_name(base_name, used))

    item_names: list[tuple[str, ItemCollection]] = []
    for collection in signature.item_collections:
        if _is_kwargs(collection, signature):
            base = "items"
        elif collection.mode == "values":
            base = collection.identifier
        elif collection.mode == "types" and "items" in used:
            base = "outputs"
        else:
            base = "items"
        item_names.append((unique_name(base, used), collection))
    return _Parameters(input_names, property_names, item_names)


def _is_kwargs(collection: ItemCollection, signature: NodeSignature) -> bool:
    """The first value-mode collection takes the function's keyword arguments."""
    first_values = next(
        (c for c in signature.item_collections if c.mode == "values"), None
    )
    return collection is first_values


def _signature_parameters(signature: NodeSignature, names: _Parameters) -> str:
    parameters: list[str] = []
    for name, socket in zip(names.inputs, signature.inputs, strict=True):
        annotation = _argument_type(socket, is_output=False)
        default_value = _input_default(socket)
        if default_value is None and not annotation.endswith(" | None"):
            annotation += " | None"
        parameters.append(f"{name}: {annotation} = {_python_literal(default_value)}")

    for name, prop in zip(names.properties, signature.properties, strict=True):
        if prop.identifier in signature.type_properties:
            # None asks the runtime to infer the type from the linked inputs.
            parameters.append(f"{name}: {prop.type} | None = None")
            continue
        parameter = f"{name}: {prop.type}"
        if prop.default_value is not NO_DEFAULT:
            parameter += f" = {_python_literal(prop.default_value)}"
        parameters.append(parameter)

    kwargs: str | None = None
    for name, collection in names.items:
        if _is_kwargs(collection, signature):
            kwargs = f"**{name}: typing.Any"
        elif collection.mode == "sequence":
            parameters.append(f"{name}: typing.Sequence[typing.Any] = ()")
        else:
            parameters.append(f"{name}: typing.Mapping[str, typing.Any] | None = None")

    # Socket order changes between Blender releases, so every parameter is
    # keyword-only.
    result = f"*, {', '.join(parameters)}" if parameters else ""
    if kwargs is not None:
        result = f"{result}, {kwargs}" if result else kwargs
    return result


def _function_docstring(
    signature: NodeSignature, names: _Parameters, output_names: list[str]
) -> str:
    sections: list[str] = []
    if signature.description:
        sections.append(signature.description)

    arguments = [
        (name, socket.description)
        for name, socket in zip(names.inputs, signature.inputs, strict=True)
        if socket.description
    ]
    arguments.extend(
        (
            name,
            f"{prop.description} Inferred from the linked inputs when None."
            if prop.identifier in signature.type_properties
            else prop.description,
        )
        for name, prop in zip(names.properties, signature.properties, strict=True)
        if prop.description or prop.identifier in signature.type_properties
    )
    arguments.extend(
        (
            name,
            _ITEM_DOCS[collection.mode]
            + (" Their outputs are available by name on the result." if collection.creates_outputs else ""),
        )
        for name, collection in names.items
    )
    if arguments:
        sections.append("Args:\n" + _doc_entries(arguments))

    returns = [
        (name, socket.description)
        for name, socket in zip(output_names, signature.outputs, strict=True)
        if socket.description
    ]
    if returns:
        sections.append("Returns:\n" + _doc_entries(returns))
    return "\n\n".join(sections)


def _doc_entries(entries: list[tuple[str, str]]) -> str:
    return "\n".join(f"    {name}: {description}" for name, description in entries)


def _emit_signature(signature: NodeSignature) -> list[str]:
    output_names = unique_names(snake_case(socket.name) for socket in signature.outputs)
    names = _parameter_names(signature)
    has_outputs = bool(signature.outputs) or signature.has_item_outputs
    return_type = signature.output_type_name if has_outputs else "None"

    lines: list[str] = []
    if has_outputs:
        lines.extend(_emit_output_class(signature, output_names))
    lines.append(
        f"def {signature.function_name}({_signature_parameters(signature, names)}) -> {return_type}:"
    )
    docstring = _function_docstring(signature, names, output_names)
    if docstring:
        lines.append(f"    {_python_literal(docstring)}")
    lines.extend(_emit_node_call(signature, names, output_names, return_type))
    return lines


def _emit_output_class(signature: NodeSignature, output_names: list[str]) -> list[str]:
    base = "ItemOutputs" if signature.has_item_outputs else "typing.NamedTuple"
    lines = [f"class {signature.output_type_name}({base}):"]
    if signature.description:
        description = f"Outputs from {signature.name}: {signature.description}"
        lines.append(f"    {_python_literal(description)}")
    for name, socket in zip(output_names, signature.outputs, strict=True):
        lines.append(f"    {name}: {_argument_type(socket, is_output=True)}")
    if not signature.outputs and not signature.description:
        lines.append("    pass")
    lines.append("")
    return lines


def _emit_node_call(
    signature: NodeSignature,
    names: _Parameters,
    output_names: list[str],
    output_type: str,
) -> list[str]:
    """The ``_node_function(...)`` call that creates the node in the active tree."""
    indent = " " * 12
    input_values = [f"{indent}{name!r}: {name}," for name in names.inputs]
    input_sockets = [
        f"{indent}{name!r}: "
        f"{_python_literal((socket.socket_identifier, socket.name, socket.socket_index, _input_default(socket)))},"
        for name, socket in zip(names.inputs, signature.inputs, strict=True)
    ]
    properties = [
        f"{indent}{prop.identifier!r}: {name},"
        for name, prop in zip(names.properties, signature.properties, strict=True)
    ]
    output_sockets = [
        f"{indent}{name!r}: "
        f"{_python_literal((socket.socket_identifier, socket.name, socket.socket_index, _output_structure_type(socket)))},"
        for name, socket in zip(output_names, signature.outputs, strict=True)
    ]

    lines = [
        "    return _node_function(",
        f"        {signature.node_type_id!r},",
        "        inputs={",
        *input_values,
        "        },",
        "        input_sockets={",
        *input_sockets,
        "        },",
        "        properties={",
        *properties,
        "        },",
        "        output_sockets={",
        *output_sockets,
        "        },",
        f"        output_type={output_type},",
    ]
    if names.items:
        lines.append("        item_collections=(")
        lines.extend(
            f"{indent}({collection.identifier!r}, {collection.mode!r}, {name}),"
            for name, collection in names.items
        )
        lines.append("        ),")
    # Type properties are keyed by input parameter name rather than socket index.
    type_kinds = {
        identifier: {
            value: {names.inputs[index]: kind for index, kind in kinds.items()}
            for value, kinds in by_value.items()
        }
        for identifier, by_value in signature.type_properties.items()
    }
    if type_kinds:
        lines.append(f"        type_properties={_python_literal(type_kinds)},")
    lines.extend(["    )", ""])
    return lines
