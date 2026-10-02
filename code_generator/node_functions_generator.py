"""Print typed function signatures for the node types exposed by Blender."""

from __future__ import annotations

import argparse
import keyword
import math
import re
import sys
import typing
from dataclasses import dataclass

import bpy


NO_DEFAULT = object()


@dataclass(frozen=True, slots=True)
class NodeMetatype:
    """A socket as it appears in a generated function signature."""

    name: str
    type: str
    default_value: object = NO_DEFAULT
    description: str = ""
    display_shape: str = ""
    structure_type: str = ""
    enum_values: tuple[str, ...] = ()
    is_menu: bool = False
    supports_field: bool = False
    supports_geometry_structures: bool = False
    is_multi_input: bool = False
    is_variadic: bool = False


@dataclass(frozen=True, slots=True)
class NodeProperty:
    """A settable node property exposed as a function parameter."""

    identifier: str
    type: str
    default_value: object = NO_DEFAULT
    description: str = ""


@dataclass(frozen=True, slots=True)
class NodeSignature:
    name: str
    function_name: str
    output_type_name: str
    description: str
    inputs: tuple[NodeMetatype, ...]
    outputs: tuple[NodeMetatype, ...]
    properties: tuple[NodeProperty, ...] = ()


_SOCKET_ENUM_TYPES: dict[str, str] = {
    "BOOLEAN": "bool",
    "VALUE": "float",
    "INT": "int",
    # NodeInternalSocketTemplate only reports the broad integer-vector enum,
    # while instantiated sockets expose their precise 2D/3D class.
    "INT_VECTOR": "IntVector2 | IntVector3",
    "VECTOR": "Vector",
    "RGBA": "Color",
    "STRING": "str",
    "GEOMETRY": "Geometry",
    "SHADER": "Shader",
    "OBJECT": "Object",
    "IMAGE": "Image",
    "COLLECTION": "Collection",
    "MATERIAL": "Material",
    "TEXTURE": "Texture",
    "ROTATION": "Rotation",
    "MATRIX": "Matrix",
    "BUNDLE": "Bundle",
    "CLOSURE": "Closure",
    # NodeSocketMenu.default_value is a string enum identifier. Socket
    # instances narrow it to their current enum items when those are known.
    "MENU": "Menu",
    "FONT": "Font",
    "SCENE": "Scene",
    "SOUND": "Sound",
    "TEXT": "Text",
    "MASK": "Mask",
}

_SOCKET_ID_TYPES: dict[str, str] = {
    "NodeSocketBool": "bool",
    "NodeSocketColor": "Color",
    "NodeSocketGeometry": "Geometry",
    "NodeSocketMatrix": "Matrix",
    "NodeSocketObject": "Object",
    "NodeSocketImage": "Image",
    "NodeSocketCollection": "Collection",
    "NodeSocketMaterial": "Material",
    "NodeSocketTexture": "Texture",
    "NodeSocketRotation": "Rotation",
    "NodeSocketShader": "Shader",
    "NodeSocketBundle": "Bundle",
    "NodeSocketClosure": "Closure",
    "NodeSocketMenu": "Menu",
    "NodeSocketFont": "Font",
    "NodeSocketScene": "Scene",
    "NodeSocketSound": "Sound",
    "NodeSocketText": "Text",
    "NodeSocketMask": "Mask",
    "NodeSocketString": "str",
    "NodeSocketStringFilePath": "str",
}
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

_NODE_TREE_TYPES: tuple[str, ...] = (
    "GeometryNodeTree",
    "ShaderNodeTree",
    "CompositorNodeTree",
    "TextureNodeTree",
)

_NODE_FAMILY_TREE_TYPES: dict[str, tuple[str, ...]] = {
    "GeometryNode": ("GeometryNodeTree",),
    # Blender's FunctionNode family is used by function-style nodes in geometry trees.
    "FunctionNode": ("GeometryNodeTree",),
    "ShaderNode": ("ShaderNodeTree",),
    "CompositorNode": ("CompositorNodeTree",),
    "TextureNode": ("TextureNodeTree",),
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

_GENERIC_NODE_BASE_NAMES = {
    "Node",
    "NodeInternal",
    "GeometryNode",
    "FunctionNode",
    "ShaderNode",
    "CompositorNode",
    "TextureNode",
}

_INTERNAL_NODE_PROPERTY_IDENTIFIERS = {
    # These properties select rows in Blender's node-editor panels. They do
    # not configure the values processed by the node.
    "active_index",
    "active_item",
    "inspection_index",
    "ui_shortcut",
}


def _safe_getattr(value: object, attribute: str, default: typing.Any = None) -> typing.Any:
    try:
        return getattr(value, attribute)
    except Exception:
        return default


def _socket_structure_kind(display_shape: str, structure_type: str) -> str | None:
    """Return the value structure represented by a socket, when explicit."""
    if display_shape == "VOLUME_GRID" or structure_type == "GRID":
        return "GRID"
    if display_shape == "LIST" or structure_type == "LIST":
        return "LIST"
    return None


def _is_virtual_socket(socket: object) -> bool:
    """Return whether a socket is Blender's editor-only dynamic socket slot."""
    socket_id = _safe_getattr(socket, "bl_idname", "")
    if socket_id == "NodeSocketVirtual":
        return True
    if socket_id:
        return False

    # Some RNA proxies do not expose bl_idname consistently, so use the RNA
    # identifier and concrete Python proxy type as conservative fallbacks.
    rna = _safe_getattr(socket, "bl_rna")
    rna_id = _safe_getattr(rna, "identifier", "")
    return (
        rna_id == "NodeSocketVirtual"
        or type(socket).__name__ == "NodeSocketVirtual"
    )


def _virtual_socket_argument(node_type_id: str) -> NodeMetatype | None:
    """Map supported dynamic socket slots to their initial DSL argument."""
    if node_type_id == "GeometryNodeBake":
        # Bake's extra items are currently treated as additional geometry
        # values. Their names and individual data types can be modeled later.
        return NodeMetatype(name="value", type="Geometry", is_variadic=True)
    return None


def _is_internal_node_property(prop: object) -> bool:
    """Exclude node-editor selection and inspection state from DSL arguments."""
    identifier = _safe_getattr(prop, "identifier", "")
    if not isinstance(identifier, str):
        identifier = ""
    if identifier in _INTERNAL_NODE_PROPERTY_IDENTIFIERS:
        return True

    # Nodes with several item lists often expose a separate active_*_index for
    # each list. These indices are UI row selection state as well.
    if re.fullmatch(r"active(?:_[a-z0-9]+)*_index", identifier):
        return True

    description = _safe_getattr(prop, "description", "")
    if not isinstance(description, str):
        return False
    description = description.casefold()
    return "inspection features" in description or "ui shortcut" in description


def _initialize_documented_node_defaults(node: object) -> None:
    """Expose the Bake node's documented default Geometry pass-through."""
    if _safe_getattr(node, "bl_idname", "") != "GeometryNodeBake":
        return

    # Bake sockets are dynamically declared from bake_items. A bare nodes.new()
    # probe has no items, even though the node manual documents Geometry as its
    # standard input/output. Seed that documented default for signature reading.
    items = _safe_getattr(node, "bake_items")
    if items is None:
        return
    try:
        if len(items) == 0:
            items.new("GEOMETRY", "Geometry")
    except Exception:
        # Keep generation usable for Blender versions where the collection or
        # its socket enum differs; virtual sockets are still filtered below.
        return


def _snake_case(value: str, *, fallback: str = "socket") -> str:
    """Convert a UI label or RNA name into a valid, readable Python identifier."""
    value = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^0-9a-zA-Z_]+", "_", value).strip("_").lower()
    value = re.sub(r"_+", "_", value)
    if not value:
        value = fallback
    if value[0].isdigit():
        value = f"{fallback}_{value}"
    if keyword.iskeyword(value):
        value += "_"
    return value


def _unique_names(names: typing.Iterable[str]) -> list[str]:
    used: set[str] = set()
    result: list[str] = []
    for name in names:
        candidate = name
        suffix = 2
        while candidate in used:
            candidate = f"{name}_{suffix}"
            suffix += 1
        used.add(candidate)
        result.append(candidate)
    return result


def _socket_type_name(socket_id: str, socket_type: str) -> str:
    """Map Blender's socket classes to the public types used by the library."""
    if socket_id in _SOCKET_ID_TYPES:
        return _SOCKET_ID_TYPES[socket_id]

    if socket_id.startswith("NodeSocketIntVector"):
        if socket_id.endswith("2D"):
            return "IntVector2"
        if socket_id.endswith("3D"):
            return "IntVector3"
        return "typing.Any"

    # All Blender float and integer socket subtypes (angle, distance, factor,
    # percentage, and so on) still carry the corresponding Python scalar.
    if socket_id.startswith("NodeSocketFloat"):
        return "float"
    if socket_id.startswith("NodeSocketInt"):
        return "int"

    if socket_id.startswith("NodeSocketVector"):
        if socket_id.endswith("2D"):
            return "Vector2"
        if socket_id.endswith("4D"):
            return "Vector4"
        return "Vector"

    if socket_id.startswith("NodeSocketString"):
        return "str"

    return _SOCKET_ENUM_TYPES.get(socket_type, "typing.Any")


def _literal_value(value: object) -> object:
    """Copy simple RNA values into ordinary Python literals for source output."""
    if value is None or isinstance(value, (bool, int, str, bytes)):
        return value
    if isinstance(value, float):
        return value
    if isinstance(value, (set, frozenset)):
        items = tuple(_literal_value(item) for item in sorted(value, key=repr))
        if any(item is NO_DEFAULT for item in items):
            return NO_DEFAULT
        return type(value)(items)
    if isinstance(value, dict):
        return NO_DEFAULT

    # RNA arrays and mathutils vectors/colors expose iteration but are not
    # directly representable in generated Python source.
    try:
        items = tuple(_literal_value(item) for item in value)  # type: ignore[union-attr]
        if any(item is NO_DEFAULT for item in items):
            return NO_DEFAULT
        return items
    except Exception:
        return NO_DEFAULT


def _socket_meta(
    socket: object,
    index: int,
    *,
    is_input: bool,
    supports_geometry_structures: bool = False,
) -> NodeMetatype:
    socket_name = _safe_getattr(socket, "name", "")
    if not isinstance(socket_name, str) or not socket_name:
        socket_name = _safe_getattr(socket, "identifier", "")
    if not isinstance(socket_name, str) or not socket_name:
        socket_name = f"Socket {index + 1}"

    socket_id = _safe_getattr(socket, "bl_idname", "")
    if not isinstance(socket_id, str):
        socket_id = ""
    if not socket_id:
        socket_id = type(socket).__name__

    socket_type = _safe_getattr(socket, "type", "")
    if not isinstance(socket_type, str):
        socket_type = ""

    display_shape = _safe_getattr(socket, "display_shape", "")
    if not isinstance(display_shape, str):
        display_shape = ""
    structure_type = _safe_getattr(socket, "inferred_structure_type", "")
    if not isinstance(structure_type, str):
        structure_type = ""

    is_menu = socket_id == "NodeSocketMenu" or socket_type == "MENU"
    enum_values: tuple[str, ...] = ()
    if is_menu:
        enum_values = _socket_menu_values(socket)

    default_value: object = NO_DEFAULT
    if is_input:
        try:
            default_value = _literal_value(getattr(socket, "default_value"))
        except Exception:
            pass

    description = _safe_getattr(socket, "description", "")
    if not isinstance(description, str):
        description = ""

    return NodeMetatype(
        name=socket_name,
        type=_socket_type_name(socket_id, socket_type),
        default_value=default_value,
        description=description,
        display_shape=display_shape,
        structure_type=structure_type,
        enum_values=enum_values,
        is_menu=is_menu,
        # DIAMOND_DOT is retained in RNA for older node definitions.
        supports_field=display_shape in {"DIAMOND", "DIAMOND_DOT"},
        supports_geometry_structures=supports_geometry_structures,
        is_multi_input=bool(_safe_getattr(socket, "is_multi_input", False)),
    )


def _template_meta(template: object, index: int) -> NodeMetatype:
    """Read a static NodeInternal socket template when no instance is usable."""
    name = _safe_getattr(template, "name", "")
    if not isinstance(name, str) or not name:
        name = _safe_getattr(template, "identifier", "")
    if not isinstance(name, str) or not name:
        name = f"Socket {index + 1}"
    socket_type = _safe_getattr(template, "type", "")
    if not isinstance(socket_type, str):
        socket_type = ""
    return NodeMetatype(
        name=name,
        type=_socket_type_name("", socket_type),
        is_menu=socket_type == "MENU",
    )


def _registered_node_types(node_type: type) -> list[type]:
    result: list[type] = []
    for name in dir(bpy.types):
        try:
            candidate = getattr(bpy.types, name)
            if (
                isinstance(candidate, type)
                and candidate is not node_type
                and issubclass(candidate, node_type)
            ):
                is_registered = getattr(candidate, "is_registered_node_type", None)
                if callable(is_registered) and not is_registered():
                    continue
                if not _safe_getattr(candidate, "bl_idname", candidate.__name__):
                    continue
                result.append(candidate)
        except Exception:
            # bpy.types can include lazily registered or partially defined RNA
            # classes. A single broken registration must not stop generation.
            continue
    return result


def _tree_types_for(node_type: type, selected_base: type) -> tuple[str, ...]:
    """Choose likely tree contexts, with all standard trees as a fallback."""
    family_names = tuple(_NODE_FAMILY_TREE_TYPES)
    mro_names = {base.__name__ for base in getattr(node_type, "__mro__", ())}
    for family_name in family_names:
        if family_name in mro_names:
            return _NODE_FAMILY_TREE_TYPES[family_name]

    selected_mro_names = {base.__name__ for base in getattr(selected_base, "__mro__", ())}
    for family_name in family_names:
        if family_name in selected_mro_names:
            return _NODE_FAMILY_TREE_TYPES[family_name]
    return _NODE_TREE_TYPES


def _node_socket_templates(node_type: type, method_name: str) -> tuple[NodeMetatype, ...]:
    method = getattr(node_type, method_name, None)
    if not callable(method):
        return ()

    sockets: list[NodeMetatype] = []
    for index in range(512):
        try:
            template = method(index)
        except Exception:
            break
        if template is None:
            break
        sockets.append(_template_meta(template, index))
    return tuple(sockets)


def _enum_values(prop: object) -> tuple[str, ...]:
    """Return stable enum identifiers without depending on a UI context."""
    for collection_name in ("enum_items_static", "enum_items"):
        items = _safe_getattr(prop, collection_name)
        if items is None:
            continue
        try:
            values = tuple(
                identifier
                for item in items
                if isinstance((identifier := _safe_getattr(item, "identifier")), str)
                and identifier
            )
        except Exception:
            continue
        if values:
            return values
    return ()


def _socket_menu_values(socket: object) -> tuple[str, ...]:
    """Read a menu socket's current RNA enum, with a node-item fallback."""
    socket_rna = _safe_getattr(socket, "bl_rna")
    properties = _safe_getattr(socket_rna, "properties")
    property_get = _safe_getattr(properties, "get")
    if callable(property_get):
        values = _enum_values(property_get("default_value"))
        if values:
            return values

    # Menu Switch owns its item definition on the node, while the socket's
    # RNA enum callback can be unavailable when the socket is inspected
    # outside a UI context. NodeEnumItem.name is the RNA enum identifier.
    node = _safe_getattr(socket, "node")
    items = _safe_getattr(node, "enum_items")
    if items is None:
        return ()
    values: list[str] = []
    seen: set[str] = set()
    try:
        for item in items:
            name = _safe_getattr(item, "name")
            if isinstance(name, str) and name and name not in seen:
                values.append(name)
                seen.add(name)
    except Exception:
        return ()
    return tuple(values)


def _property_type(prop: object) -> str:
    property_type = _safe_getattr(prop, "type", "")
    if not isinstance(property_type, str):
        property_type = ""

    if property_type == "ENUM":
        values = _enum_values(prop)
        literal_type = (
            f"typing.Literal[{', '.join(repr(value) for value in values)}]"
            if values
            else "str"
        )
        if _safe_getattr(prop, "is_enum_flag", False):
            return f"set[{literal_type}]" if values else "set[str]"
        return literal_type

    if property_type == "POINTER":
        fixed_type = _safe_getattr(prop, "fixed_type")
        type_name = _safe_getattr(fixed_type, "identifier", "")
        if not isinstance(type_name, str) or not type_name.isidentifier():
            type_name = "typing.Any"
        if type_name != "typing.Any" and not _safe_getattr(prop, "is_never_none", False):
            type_name = f"{type_name} | None"
        return type_name

    scalar_types = {
        "BOOLEAN": "bool",
        "INT": "int",
        "FLOAT": "float",
        "STRING": "str",
    }
    scalar_type = scalar_types.get(property_type, "typing.Any")
    if not _safe_getattr(prop, "is_array", False):
        return scalar_type

    array_length = _safe_getattr(prop, "array_length", 0)
    if not isinstance(array_length, int) or array_length <= 0:
        return f"tuple[{scalar_type}, ...]"

    subtype = _safe_getattr(prop, "subtype", "")
    if property_type == "FLOAT":
        if subtype == "COLOR":
            return "Color"
        if subtype == "MATRIX":
            return "Matrix"
        if array_length == 2:
            return "Vector2"
        if array_length == 3:
            return "Vector"
        if array_length == 4:
            return "Vector4"
    if property_type == "INT":
        if array_length == 2:
            return "IntVector2"
        if array_length == 3:
            return "IntVector3"

    return f"tuple[{scalar_type}, ...]"


def _property_default(prop: object, node: object | None) -> object:
    identifier = _safe_getattr(prop, "identifier", "")
    if node is not None and isinstance(identifier, str) and identifier:
        try:
            return _literal_value(getattr(node, identifier))
        except Exception:
            pass

    if _safe_getattr(prop, "type", "") == "ENUM" and _safe_getattr(
        prop, "is_enum_flag", False
    ):
        value = _safe_getattr(prop, "default_flag", NO_DEFAULT)
    else:
        value = _safe_getattr(prop, "default", NO_DEFAULT)
        if value is NO_DEFAULT:
            value = _safe_getattr(prop, "default_array", NO_DEFAULT)
    return _literal_value(value) if value is not NO_DEFAULT else NO_DEFAULT


def _node_properties(node_type: type, node: object | None) -> tuple[NodeProperty, ...]:
    """Collect writable properties declared by this node, excluding Node base API."""
    inherited_identifiers: set[str] = set()
    for base in getattr(node_type, "__mro__", ())[1:]:
        if base.__name__ not in _GENERIC_NODE_BASE_NAMES:
            continue
        base_rna = _safe_getattr(base, "bl_rna")
        try:
            for prop in _safe_getattr(base_rna, "properties", ()):
                identifier = _safe_getattr(prop, "identifier", "")
                if isinstance(identifier, str):
                    inherited_identifiers.add(identifier)
        except Exception:
            continue

    rna = _safe_getattr(node_type, "bl_rna")
    properties: list[NodeProperty] = []
    try:
        rna_properties = tuple(_safe_getattr(rna, "properties", ()))
    except Exception:
        return ()
    for prop in rna_properties:
        try:
            identifier = _safe_getattr(prop, "identifier", "")
            if not isinstance(identifier, str) or not identifier:
                continue
            if _is_internal_node_property(prop):
                continue
            if identifier in inherited_identifiers:
                continue
            if _safe_getattr(prop, "is_readonly", True):
                continue
            if _safe_getattr(prop, "is_deprecated", False):
                continue
            if _safe_getattr(prop, "is_output", False):
                continue
            if _safe_getattr(prop, "type", "") == "COLLECTION":
                # RNA collections are edited through add/remove operations and
                # cannot be assigned as a normal function argument.
                continue

            description = _safe_getattr(prop, "description", "")
            properties.append(
                NodeProperty(
                    identifier=identifier,
                    type=_property_type(prop),
                    default_value=_property_default(prop, node),
                    description=description if isinstance(description, str) else "",
                )
            )
        except Exception:
            continue
    return tuple(properties)


def _node_type_name(node_type: type) -> str:
    rna = _safe_getattr(node_type, "bl_rna")
    name = _safe_getattr(rna, "name", "")
    if isinstance(name, str) and name:
        return name
    label = _safe_getattr(node_type, "bl_label", "")
    if isinstance(label, str) and label:
        return label
    return node_type.__name__


def _node_description(node_type: type) -> str:
    description = _safe_getattr(node_type, "bl_description", "")
    if not isinstance(description, str) or not description:
        description = _safe_getattr(node_type, "__doc__", "")
    return description.strip() if isinstance(description, str) else ""


def _build_signature(
    node_type: type,
    selected_base: type,
    probe_trees: dict[str, object],
) -> NodeSignature:
    inputs: tuple[NodeMetatype, ...] = ()
    outputs: tuple[NodeMetatype, ...] = ()
    properties: tuple[NodeProperty, ...] = ()
    node = None
    tree = None
    socket_tree_type = ""
    node_type_id = _safe_getattr(node_type, "bl_idname", node_type.__name__)

    for tree_type in _tree_types_for(node_type, selected_base):
        try:
            tree = probe_trees.get(tree_type)
            if tree is None:
                tree = bpy.data.node_groups.new(
                    name=f"_geometry_script_codegen_{tree_type}", type=tree_type
                )
                probe_trees[tree_type] = tree
            node = tree.nodes.new(type=node_type_id)
            if node is not None:
                socket_tree_type = tree_type
                break
        except Exception:
            node = None
            tree = None
            continue

    if node is not None and tree is not None:
        try:
            _initialize_documented_node_defaults(node)
            virtual_input_enabled = any(
                _safe_getattr(socket, "enabled", True)
                and _is_virtual_socket(socket)
                for socket in node.inputs
            )
            inputs = tuple(
                _socket_meta(
                    socket,
                    index,
                    is_input=True,
                    supports_geometry_structures=socket_tree_type == "GeometryNodeTree",
                )
                for index, socket in enumerate(node.inputs)
                if _safe_getattr(socket, "enabled", True)
                and not _is_virtual_socket(socket)
            )
            if virtual_input_enabled:
                variadic_argument = _virtual_socket_argument(node_type_id)
                if variadic_argument is not None:
                    inputs = (*inputs, variadic_argument)
            outputs = tuple(
                _socket_meta(
                    socket,
                    index,
                    is_input=False,
                    supports_geometry_structures=socket_tree_type == "GeometryNodeTree",
                )
                for index, socket in enumerate(node.outputs)
                if _safe_getattr(socket, "enabled", True)
                and not _is_virtual_socket(socket)
            )
        except Exception as error:
            print(
                f"Could not read sockets for {node_type.__name__}: {error}",
                file=sys.stderr,
            )
        try:
            properties = _node_properties(node_type, node)
        except Exception as error:
            print(
                f"Could not read properties for {node_type.__name__}: {error}",
                file=sys.stderr,
            )
        finally:
            try:
                tree.nodes.remove(node)
            except Exception:
                pass

    # NodeInternal exposes class-level socket templates. They provide a useful
    # fallback for nodes that cannot be instantiated in a generic node tree.
    if not inputs:
        inputs = _node_socket_templates(node_type, "input_template")
    if not outputs:
        outputs = _node_socket_templates(node_type, "output_template")
    if not properties:
        properties = _node_properties(node_type, None)

    node_name = _node_type_name(node_type)
    return NodeSignature(
        name=node_name,
        function_name=_snake_case(node_name, fallback="node"),
        output_type_name=f"{node_type.__name__}Outputs",
        description=_node_description(node_type),
        inputs=inputs,
        outputs=outputs,
        properties=properties,
    )


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
    if isinstance(value, set):
        if not value:
            return "set()"
        return "{" + ", ".join(
            _python_literal(item) for item in sorted(value, key=repr)
        ) + "}"
    if isinstance(value, frozenset):
        contents = ", ".join(
            _python_literal(item) for item in sorted(value, key=repr)
        )
        return f"frozenset({{{contents}}})"
    return repr(value)


def _argument_type(socket: NodeMetatype, *, is_output: bool) -> str:
    base_type = socket.type
    structure_kind = _socket_structure_kind(
        socket.display_shape, socket.structure_type
    )

    if socket.enum_values:
        # Blender's menu identifiers are strings accepted by the socket's
        # default_value property, so a Literal can pass through unchanged.
        values = ", ".join(repr(value) for value in socket.enum_values)
        base_type = f"typing.Literal[{values}]"
    elif socket.is_menu:
        # The menu domain can depend on links and may not exist at generation
        # time. Keep the public Menu name; builtins aliases it to str.
        base_type = "Menu"
    elif structure_kind == "GRID":
        base_type = f"Grid[{base_type}]"
        # A scalar RNA default on a grid socket is only the base socket's
        # storage default; it does not describe a grid (which also needs a
        # topology and transform). None means the DSL leaves it unlinked.
        if not is_output and not socket.is_multi_input:
            base_type = f"{base_type} | None"
    elif structure_kind == "LIST":
        base_type = f"List[{base_type}]"
        if not is_output and not socket.is_multi_input:
            base_type = f"{base_type} | None"
    elif (
        (
            socket.structure_type == "DYNAMIC"
            or (
                socket.display_shape == "CIRCLE"
                and socket.supports_geometry_structures
            )
        )
        and socket.type in _DYNAMIC_STRUCTURE_SOCKET_TYPES
    ):
        variants = (
            base_type,
            f"Field[{base_type}]",
            f"Grid[{base_type}]",
            f"List[{base_type}]",
        )
        base_type = " | ".join(variants)
    elif socket.structure_type == "FIELD" or (
        socket.supports_geometry_structures and socket.supports_field
    ):
        # A field socket can also take a single constant, which Blender
        # broadcasts over the field's domain.
        if is_output and socket.display_shape == "DIAMOND_DOT":
            base_type = f"{base_type} | Field[{base_type}]"
        elif is_output:
            base_type = f"Field[{base_type}]"
        else:
            base_type = f"{base_type} | Field[{base_type}]"
    elif (
        not is_output
        and socket.default_value is None
        and base_type in _NULLABLE_SOCKET_TYPES
    ):
        base_type = f"{base_type} | None"

    if socket.is_multi_input and not is_output:
        return f"typing.Sequence[{base_type}]"
    return base_type


def _parameter_names(
    inputs: tuple[NodeMetatype, ...], properties: tuple[NodeProperty, ...]
) -> tuple[list[str], list[str]]:
    input_names = _unique_names(_snake_case(socket.name) for socket in inputs)
    used = set(input_names)
    property_names: list[str] = []
    for prop in properties:
        base_name = _snake_case(prop.identifier)
        if base_name in used:
            base_name = f"{base_name}_property"
        name = base_name
        suffix = 2
        while name in used:
            name = f"{base_name}_{suffix}"
            suffix += 1
        used.add(name)
        property_names.append(name)
    return input_names, property_names


def _signature_parameters_with_properties(
    inputs: tuple[NodeMetatype, ...], properties: tuple[NodeProperty, ...]
) -> str:
    input_names, property_names = _parameter_names(inputs, properties)
    parameters: list[str] = []
    defaults_seen = False
    required_after_default = False
    variadic_seen = False
    for name, socket in zip(input_names, inputs, strict=True):
        if socket.is_variadic:
            parameters.append(
                f"*{name}: {_argument_type(socket, is_output=False)}"
            )
            variadic_seen = True
            continue

        structure_kind = _socket_structure_kind(
            socket.display_shape, socket.structure_type
        )
        if socket.is_multi_input:
            # Multi-input sockets collect links; an empty sequence means no
            # links. Their inherited scalar default, if any, is irrelevant.
            has_default = True
            default_value: object = ()
        elif structure_kind is not None:
            # Blender may expose the scalar backing property's default even
            # though a Grid/List input cannot be supplied by that scalar.
            # None is the DSL-level spelling for leaving such an input open.
            has_default = True
            default_value = None
        else:
            default_value = socket.default_value
            has_default = default_value is not NO_DEFAULT
        if has_default:
            defaults_seen = True
        elif defaults_seen:
            required_after_default = True
        annotation = _argument_type(socket, is_output=False)
        parameter = f"{name}: {annotation}"
        if has_default:
            parameter += f" = {_python_literal(default_value)}"
        parameters.append(parameter)

    for name, prop in zip(property_names, properties, strict=True):
        has_default = prop.default_value is not NO_DEFAULT
        if has_default:
            defaults_seen = True
        elif defaults_seen:
            required_after_default = True
        parameter = f"{name}: {prop.type}"
        if has_default:
            parameter += f" = {_python_literal(prop.default_value)}"
        parameters.append(parameter)

    if required_after_default and parameters and not variadic_seen:
        return "*, " + ", ".join(parameters)
    return ", ".join(parameters)


def _function_docstring(
    signature: NodeSignature,
    input_names: list[str],
    property_names: list[str],
) -> str:
    sections: list[str] = []
    if signature.description:
        sections.append(signature.description)

    documented_inputs = [
        (name, socket.description)
        for name, socket in zip(input_names, signature.inputs, strict=True)
        if socket.description
    ]
    if documented_inputs:
        input_docs = "\n".join(
            f"    {name}: {description}" for name, description in documented_inputs
        )
        sections.append("Args:\n" + input_docs)

    documented_properties = [
        (name, prop.description)
        for name, prop in zip(property_names, signature.properties, strict=True)
        if prop.description
    ]
    if documented_properties:
        property_docs = "\n".join(
            f"    {name}: {description}" for name, description in documented_properties
        )
        if sections and sections[-1].startswith("Args:\n"):
            sections[-1] += "\n" + property_docs
        else:
            sections.append("Args:\n" + property_docs)

    output_names = _unique_names(_snake_case(socket.name) for socket in signature.outputs)
    documented_outputs = [
        (name, socket.description)
        for name, socket in zip(output_names, signature.outputs, strict=True)
        if socket.description
    ]
    if documented_outputs:
        output_docs = "\n".join(
            f"    {name}: {description}"
            for name, description in documented_outputs
        )
        sections.append("Returns:\n" + output_docs)
    return "\n\n".join(sections)


def _emit_signature(signature: NodeSignature) -> list[str]:
    lines: list[str] = []
    output_names = _unique_names(_snake_case(socket.name) for socket in signature.outputs)
    if signature.outputs:
        lines.append(f"class {signature.output_type_name}(typing.NamedTuple):")
        if signature.description:
            description = (
                f"Outputs from {signature.name}: {signature.description}"
            )
            lines.append(f"    {_python_literal(description)}")
        for name, socket in zip(output_names, signature.outputs, strict=True):
            lines.append(f"    {name}: {_argument_type(socket, is_output=True)}")
        lines.append("")

    parameter_names, property_names = _parameter_names(
        signature.inputs, signature.properties
    )
    parameters = _signature_parameters_with_properties(
        signature.inputs, signature.properties
    )
    if signature.outputs:
        return_type = signature.output_type_name
    else:
        return_type = "None"
    lines.append(
        f"def {signature.function_name}({parameters}) -> {return_type}:"
    )
    docstring = _function_docstring(signature, parameter_names, property_names)
    if docstring:
        lines.append(f"    {_python_literal(docstring)}")
    lines.append("    ...")
    lines.append("")
    return lines


def _disambiguate_function_names(signatures: list[NodeSignature]) -> list[NodeSignature]:
    counts: dict[str, int] = {}
    for signature in signatures:
        counts[signature.function_name] = counts.get(signature.function_name, 0) + 1

    result: list[NodeSignature] = []
    used: set[str] = set()
    for signature in signatures:
        name = signature.function_name
        if counts[name] > 1:
            output_name = signature.output_type_name.removesuffix("Outputs")
            name = f"{name}_{_snake_case(output_name, fallback='node')}"
        unique_name = name
        suffix = 2
        while unique_name in used:
            unique_name = f"{name}_{suffix}"
            suffix += 1
        used.add(unique_name)
        result.append(
            NodeSignature(
                name=signature.name,
                function_name=unique_name,
                output_type_name=signature.output_type_name,
                description=signature.description,
                inputs=signature.inputs,
                outputs=signature.outputs,
                properties=signature.properties,
            )
        )
    return result

def _load_builtins() -> str:
    """
    Gets all of the code in the builtins/ folder and concatenates them into a single string for the generated code output.
    """
    import os

    builtins_dir = os.path.join(os.path.dirname(__file__), "builtins")
    builtins_code = ""
    for filename in os.listdir(builtins_dir):
        if filename.endswith(".py"):
            with open(os.path.join(builtins_dir, filename), "r", encoding="utf-8") as f:
                builtins_code += f.read() + "\n"
    return builtins_code

def generate_code(node_type: type) -> str:
    if not isinstance(node_type, type) or not issubclass(node_type, bpy.types.Node):
        raise TypeError(f"{node_type!r} is not a bpy.types.Node subclass")

    probe_trees: dict[str, object] = {}
    signatures: list[NodeSignature] = []
    try:
        for registered_type in _registered_node_types(node_type):
            try:
                signatures.append(
                    _build_signature(registered_type, node_type, probe_trees)
                )
            except Exception as error:
                print(
                    f"Skipping {registered_type.__name__}: {error}",
                    file=sys.stderr,
                )
    finally:
        for tree in probe_trees.values():
            try:
                bpy.data.node_groups.remove(tree)
            except Exception as error:
                print(f"Could not remove temporary node tree: {error}", file=sys.stderr)

    signatures = _disambiguate_function_names(signatures)
    signatures.sort(key=lambda signature: (signature.function_name, signature.output_type_name))

    builtins = _load_builtins()

    lines = [
        "from __future__ import annotations",
        "",
        "import bpy",
        "",
        "import typing",
        "",
        builtins,
        "",
    ]
    for signature in signatures:
        lines.extend(_emit_signature(signature))
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv
        if "--" in argv:
            argv = argv[argv.index("--") + 1 :]
        else:
            argv = []

    parser = argparse.ArgumentParser(description="Generate typed node functions")
    parser.add_argument(
        "--node-type",
        required=True,
        help="A bpy.types node base class, such as GeometryNode or FunctionNode",
    )
    args = parser.parse_args(argv)

    node_type = getattr(bpy.types, args.node_type, None)
    if not isinstance(node_type, type) or not issubclass(node_type, bpy.types.Node):
        parser.error(f"bpy.types.{args.node_type} is not a node type")

    try:
        sys.stdout.write(generate_code(node_type))
    except Exception as error:
        print(f"Could not generate node functions: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
