"""Read node signatures from the node types registered in the running Blender."""

from __future__ import annotations

import re
import sys
import typing
from dataclasses import replace

import bpy

from .signatures import (
    NO_DEFAULT,
    ItemCollection,
    NodeMetatype,
    NodeProperty,
    NodeSignature,
    snake_case,
)


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

_EXCLUDED_NODE_TYPES = {
    # Editor layout nodes carry no data.
    "NodeFrame",
    "NodeReroute",
    "NodeImplicitConversion",
    # Group interfaces and group instances are built by @tree.
    "NodeGroupInput",
    "NodeGroupOutput",
    "GeometryNodeGroup",
    # Zone nodes only work as linked input/output pairs, so they are built
    # by the zone decorators in api/zones.py instead.
    "GeometryNodeRepeatInput",
    "GeometryNodeRepeatOutput",
    "GeometryNodeSimulationInput",
    "GeometryNodeSimulationOutput",
    "GeometryNodeForeachGeometryElementInput",
    "GeometryNodeForeachGeometryElementOutput",
    "NodeClosureInput",
    "NodeClosureOutput",
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

# Probing every pair of enum values is enough to find the sockets of nested
# settings (e.g. Compare's vector modes); this caps runaway combinations.
_MAX_PROBED_CONFIGURATIONS = 256

_SocketKey = tuple[str, int]


class _Configuration(typing.NamedTuple):
    """The node's sockets with some enum properties set away from their defaults."""

    assignment: dict[str, str]
    inputs: dict[_SocketKey, NodeMetatype]
    outputs: dict[_SocketKey, NodeMetatype]


def read_signatures(tree_type: str) -> list[NodeSignature]:
    """Read the signature of every node that can be added to a ``tree_type`` tree."""
    tree = bpy.data.node_groups.new(name="_geometry_script_codegen", type=tree_type)
    signatures: list[NodeSignature] = []
    try:
        for node_type in _node_types_for_tree(tree):
            try:
                signatures.append(_build_signature(node_type, tree))
            except Exception as error:
                print(f"Skipping {node_type.__name__}: {error}", file=sys.stderr)
    finally:
        bpy.data.node_groups.remove(tree)
    return signatures


def _safe_getattr(value: object, attribute: str, default: typing.Any = None) -> typing.Any:
    try:
        return getattr(value, attribute)
    except Exception:
        return default


def _safe_str(value: object, attribute: str) -> str:
    """Read a string attribute, or "" when it is missing or not a string."""
    result = _safe_getattr(value, attribute, "")
    return result if isinstance(result, str) else ""


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


def _is_internal_node_property(prop: object) -> bool:
    """Exclude node-editor selection and inspection state from DSL arguments."""
    identifier = _safe_str(prop, "identifier")
    if identifier in _INTERNAL_NODE_PROPERTY_IDENTIFIERS:
        return True

    # Nodes with several item lists often expose a separate active_*_index for
    # each list. These indices are UI row selection state as well.
    if re.fullmatch(r"active(?:_[a-z0-9]+)*_index", identifier):
        return True

    description = _safe_str(prop, "description").casefold()
    return "inspection features" in description or "ui shortcut" in description


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
    if value is None or isinstance(value, (bool, int, float, str, bytes)):
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


def _socket_name(socket: object, index: int) -> str:
    return (
        _safe_str(socket, "name")
        or _safe_str(socket, "identifier")
        or f"Socket {index + 1}"
    )


def _socket_meta(
    socket: object,
    index: int,
    *,
    is_input: bool,
    supports_geometry_structures: bool = False,
) -> NodeMetatype:
    socket_id = _safe_str(socket, "bl_idname") or type(socket).__name__
    socket_type = _safe_str(socket, "type")
    display_shape = _safe_str(socket, "display_shape")

    is_menu = socket_id == "NodeSocketMenu" or socket_type == "MENU"

    default_value: object = NO_DEFAULT
    if is_input:
        try:
            default_value = _literal_value(getattr(socket, "default_value"))
        except Exception:
            pass

    return NodeMetatype(
        name=_socket_name(socket, index),
        type=_socket_type_name(socket_id, socket_type),
        default_value=default_value,
        description=_safe_str(socket, "description"),
        display_shape=display_shape,
        structure_type=_safe_str(socket, "inferred_structure_type"),
        enum_values=_socket_menu_values(socket) if is_menu else (),
        is_menu=is_menu,
        # DIAMOND_DOT is retained in RNA for older node definitions.
        supports_field=display_shape in {"DIAMOND", "DIAMOND_DOT"},
        supports_geometry_structures=supports_geometry_structures,
        is_multi_input=bool(_safe_getattr(socket, "is_multi_input", False)),
        socket_identifier=str(_safe_getattr(socket, "identifier", "") or ""),
        socket_index=index,
        kind=socket_type,
    )


def _template_meta(template: object, index: int) -> NodeMetatype:
    """Read a static NodeInternal socket template when no instance is usable."""
    socket_type = _safe_str(template, "type")
    return NodeMetatype(
        name=_socket_name(template, index),
        type=_socket_type_name("", socket_type),
        is_menu=socket_type == "MENU",
        socket_identifier=str(_safe_getattr(template, "identifier", "") or ""),
        socket_index=index,
    )


def _node_types_for_tree(tree: object) -> list[type]:
    """Return every registered node class that can be added to ``tree``.

    Class-level ``poll()`` is unreliable for built-in nodes (it reports False
    for Function and Shader nodes that geometry trees accept), so each node
    type is probed by instantiating it.
    """
    result: list[type] = []
    for name in dir(bpy.types):
        candidate = getattr(bpy.types, name, None)
        if (
            not isinstance(candidate, type)
            or candidate is bpy.types.Node
            or not issubclass(candidate, bpy.types.Node)
        ):
            continue
        node_type_id = _safe_getattr(candidate, "bl_idname", "") or candidate.__name__
        if node_type_id in _EXCLUDED_NODE_TYPES:
            continue
        try:
            node = tree.nodes.new(type=node_type_id)  # type: ignore[attr-defined]
        except Exception:
            continue
        tree.nodes.remove(node)  # type: ignore[attr-defined]
        result.append(candidate)
    return result


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
                if (identifier := _safe_str(item, "identifier"))
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
    try:
        names = [name for item in items if (name := _safe_str(item, "name"))]
    except Exception:
        return ()
    return tuple(dict.fromkeys(names))


def _property_type(prop: object) -> str:
    property_type = _safe_str(prop, "type")

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
        type_name = _safe_str(_safe_getattr(prop, "fixed_type"), "identifier")
        if not type_name.isidentifier():
            return "typing.Any"
        if _safe_getattr(prop, "is_never_none", False):
            return f"bpy.types.{type_name}"
        return f"bpy.types.{type_name} | None"

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
        vector_type = {2: "Vector2", 3: "Vector", 4: "Vector4"}.get(array_length)
        if vector_type is not None:
            return vector_type
    if property_type == "INT":
        vector_type = {2: "IntVector2", 3: "IntVector3"}.get(array_length)
        if vector_type is not None:
            return vector_type

    return f"tuple[{scalar_type}, ...]"


def _property_default(prop: object, node: object | None) -> object:
    identifier = _safe_str(prop, "identifier")
    if node is not None and identifier:
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


def _inherited_property_identifiers(node_type: type) -> set[str]:
    """Identifiers of the properties every node of a family shares (name, location, ...)."""
    identifiers: set[str] = set()
    for base in getattr(node_type, "__mro__", ())[1:]:
        if base.__name__ not in _GENERIC_NODE_BASE_NAMES:
            continue
        base_rna = _safe_getattr(base, "bl_rna")
        try:
            for prop in _safe_getattr(base_rna, "properties", ()):
                identifiers.add(_safe_str(prop, "identifier"))
        except Exception:
            continue
    return identifiers


def _is_node_argument(prop: object, inherited_identifiers: set[str]) -> bool:
    identifier = _safe_str(prop, "identifier")
    return not (
        not identifier
        or _is_internal_node_property(prop)
        or identifier in inherited_identifiers
        or _safe_getattr(prop, "is_readonly", True)
        or _safe_getattr(prop, "is_deprecated", False)
        or _safe_getattr(prop, "is_output", False)
        # RNA collections are edited through add/remove operations and
        # cannot be assigned as a normal function argument.
        or _safe_getattr(prop, "type", "") == "COLLECTION"
    )


def _node_properties(node_type: type, node: object | None) -> tuple[NodeProperty, ...]:
    """Collect writable properties declared by this node, excluding Node base API."""
    inherited_identifiers = _inherited_property_identifiers(node_type)
    rna = _safe_getattr(node_type, "bl_rna")
    try:
        rna_properties = tuple(_safe_getattr(rna, "properties", ()))
    except Exception:
        return ()

    properties: list[NodeProperty] = []
    for prop in rna_properties:
        try:
            if not _is_node_argument(prop, inherited_identifiers):
                continue
            properties.append(
                NodeProperty(
                    identifier=_safe_str(prop, "identifier"),
                    type=_property_type(prop),
                    default_value=_property_default(prop, node),
                    description=_safe_str(prop, "description"),
                )
            )
        except Exception:
            continue
    return tuple(properties)


def _node_type_name(node_type: type) -> str:
    return (
        _safe_str(_safe_getattr(node_type, "bl_rna"), "name")
        or _safe_str(node_type, "bl_label")
        or node_type.__name__
    )


def _node_description(node_type: type) -> str:
    description = (
        _safe_str(node_type, "bl_description")
        or _safe_str(_safe_getattr(node_type, "bl_rna"), "description")
        or _safe_str(node_type, "__doc__")
    )
    return description.strip()


def _read_sockets(
    node: typing.Any, supports_geometry_structures: bool
) -> tuple[list[NodeMetatype], list[NodeMetatype]]:
    def read(sockets: typing.Any, is_input: bool) -> list[NodeMetatype]:
        return [
            _socket_meta(
                socket,
                index,
                is_input=is_input,
                supports_geometry_structures=supports_geometry_structures,
            )
            for index, socket in enumerate(sockets)
            if _safe_getattr(socket, "enabled", True) and not _is_virtual_socket(socket)
        ]

    return read(node.inputs, True), read(node.outputs, False)


def _keyed(sockets: list[NodeMetatype]) -> dict[_SocketKey, NodeMetatype]:
    """Key sockets by name and occurrence, so Math's three "Value" inputs stay apart."""
    seen: dict[str, int] = {}
    result: dict[_SocketKey, NodeMetatype] = {}
    for socket in sockets:
        occurrence = seen.get(socket.name, 0)
        seen[socket.name] = occurrence + 1
        result[(socket.name, occurrence)] = socket
    return result


def _enum_property_values(node: typing.Any, identifier: str) -> tuple[str, ...]:
    prop = node.bl_rna.properties.get(identifier)
    return _enum_values(prop) if prop is not None else ()


def _try_set(node: typing.Any, identifier: str, value: typing.Any) -> bool:
    try:
        setattr(node, identifier, value)
    except Exception:
        return False
    return True


def _probe_configurations(
    node: typing.Any,
    properties: tuple[NodeProperty, ...],
    supports_geometry_structures: bool,
) -> list[_Configuration]:
    """Read the node's sockets under each enum value, and each pair of values."""
    enum_ids = [
        prop.identifier for prop in properties if prop.type.startswith("typing.Literal[")
    ]
    originals = {identifier: getattr(node, identifier) for identifier in enum_ids}

    def read(assignment: dict[str, str]) -> _Configuration:
        inputs, outputs = _read_sockets(node, supports_geometry_structures)
        return _Configuration(assignment, _keyed(inputs), _keyed(outputs))

    configurations = [read({identifier: str(value) for identifier, value in originals.items()})]
    try:
        for identifier in enum_ids:
            for value in _enum_property_values(node, identifier):
                if value == originals[identifier] or not _try_set(node, identifier, value):
                    continue
                configurations.append(read({identifier: value}))
                for other in enum_ids:
                    if other == identifier:
                        continue
                    for other_value in _enum_property_values(node, other):
                        if (
                            other_value == originals[other]
                            or len(configurations) >= _MAX_PROBED_CONFIGURATIONS
                        ):
                            continue
                        if _try_set(node, other, other_value):
                            configurations.append(
                                read({identifier: value, other: other_value})
                            )
                    # Reset ``other``, then set ``identifier`` again so the next
                    # pairs are probed with it still at ``value``.
                    _restore(node, originals)
                    if not _try_set(node, identifier, value):
                        break
            _restore(node, originals)
    finally:
        _restore(node, originals)
    return configurations


def _restore(node: typing.Any, originals: dict[str, typing.Any]) -> None:
    """Reset enum properties; valid values can depend on each other, so retry."""
    for _ in range(len(originals) + 1):
        failed = False
        for identifier, value in originals.items():
            try:
                if getattr(node, identifier) != value:
                    setattr(node, identifier, value)
            except Exception:
                failed = True
        if not failed:
            return


def _merge_sockets(
    variants: list[dict[_SocketKey, NodeMetatype]],
) -> tuple[list[_SocketKey], tuple[NodeMetatype, ...]]:
    """Union sockets over every configuration, widening types that change."""
    order: list[_SocketKey] = []
    for variant in variants:
        order.extend(key for key in variant if key not in order)
    merged: list[NodeMetatype] = []
    for key in order:
        found = [variant[key] for variant in variants if key in variant]
        types = list(dict.fromkeys(socket.type for socket in found))
        enum_values = tuple(
            dict.fromkeys(value for socket in found for value in socket.enum_values)
        )
        merged.append(
            replace(
                found[0],
                type=" | ".join(types),
                enum_values=enum_values,
                is_conditional=len(found) < len(variants),
            )
        )
    return order, tuple(merged)


def _type_properties(
    configurations: list[_Configuration],
    input_order: list[_SocketKey],
    value_orders: dict[str, tuple[str, ...]],
) -> dict[str, dict[str, dict[int, str]]]:
    """Find enum properties whose values change the kind of an input socket."""
    defaults, default_inputs, default_outputs = configurations[0]
    single: dict[str, dict[str, dict[_SocketKey, NodeMetatype]]] = {}
    changes_outputs: set[str] = set()
    for assignment, inputs, outputs in configurations[1:]:
        if len(assignment) != 1:
            continue
        ((identifier, value),) = assignment.items()
        single.setdefault(identifier, {})[value] = inputs
        if any(
            key in default_outputs and default_outputs[key].kind != socket.kind
            for key, socket in outputs.items()
        ):
            changes_outputs.add(identifier)

    result: dict[str, dict[str, dict[int, str]]] = {}
    for identifier, by_value in single.items():
        changed = {
            key
            for inputs in by_value.values()
            for key, socket in inputs.items()
            if key in default_inputs and default_inputs[key].kind != socket.kind
        }
        if not changed and identifier not in changes_outputs:
            continue
        by_value = {defaults[identifier]: default_inputs, **by_value}
        changed_order = sorted(changed, key=input_order.index)
        kinds: dict[str, dict[int, str]] = {}
        for value in value_orders[identifier]:
            if value in by_value:
                kinds[value] = {
                    input_order.index(key): by_value[value][key].kind
                    for key in changed_order
                    if key in by_value[value]
                }
        result[identifier] = kinds
    return result


def _clear_items(items: typing.Any) -> None:
    try:
        items.clear()
    except Exception:
        while len(items):
            items.remove(items[len(items) - 1])


def _item_collections(node: typing.Any) -> tuple[ItemCollection, ...]:
    """Find and empty the node's item lists, classifying each by a test item.

    The node is left without items, so its remaining sockets are the fixed ones.
    """
    found: list[tuple[str, list[str]]] = []
    for prop in node.bl_rna.properties:
        identifier = prop.identifier
        if prop.type != "COLLECTION" or not identifier.endswith("_items"):
            continue
        items = getattr(node, identifier, None)
        new = _safe_getattr(_safe_getattr(items, "bl_rna"), "functions", {}).get("new")
        if new is None:
            continue
        _clear_items(items)
        found.append((identifier, [p.identifier for p in new.parameters if not p.is_output]))

    test_arguments = {"socket_type": "FLOAT", "name": "Item"}
    result: list[ItemCollection] = []
    for identifier, parameters in found:
        items = getattr(node, identifier)
        inputs_before = {socket.identifier for socket in node.inputs}
        outputs_before = {socket.identifier for socket in node.outputs}
        try:
            items.new(**{name: test_arguments[name] for name in parameters})
        except Exception:
            continue
        creates_inputs = any(
            socket.identifier not in inputs_before and not _is_virtual_socket(socket)
            for socket in node.inputs
        )
        creates_outputs = any(
            socket.identifier not in outputs_before and not _is_virtual_socket(socket)
            for socket in node.outputs
        )
        _clear_items(items)
        if creates_inputs:
            if "socket_type" in parameters:
                mode = "values"
            elif "name" in parameters:
                mode = "named"
            else:
                mode = "sequence"
        elif creates_outputs:
            mode = "types"
        else:
            continue
        result.append(ItemCollection(identifier, mode, creates_outputs))
    return tuple(result)


def _build_signature(node_type: type, tree: typing.Any) -> NodeSignature:
    inputs: tuple[NodeMetatype, ...] = ()
    outputs: tuple[NodeMetatype, ...] = ()
    properties: tuple[NodeProperty, ...] = ()
    type_properties: dict[str, dict[str, dict[int, str]]] = {}
    item_collections: tuple[ItemCollection, ...] = ()
    node_type_id = _safe_getattr(node_type, "bl_idname", node_type.__name__)
    supports_geometry_structures = tree.bl_idname == "GeometryNodeTree"
    try:
        node = tree.nodes.new(type=node_type_id)
    except Exception:
        node = None

    if node is not None:
        try:
            item_collections = _item_collections(node)
            properties = _node_properties(node_type, node)
            configurations = _probe_configurations(
                node, properties, supports_geometry_structures
            )
            input_order, inputs = _merge_sockets([c.inputs for c in configurations])
            _, outputs = _merge_sockets([c.outputs for c in configurations])
            value_orders = {
                prop.identifier: _enum_property_values(node, prop.identifier)
                for prop in properties
            }
            type_properties = _type_properties(configurations, input_order, value_orders)
        except Exception as error:
            print(f"Could not read {node_type.__name__}: {error}", file=sys.stderr)
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
        function_name=snake_case(node_name, fallback="node"),
        node_type_id=str(node_type_id),
        output_type_name=f"{node_type.__name__}Outputs",
        description=_node_description(node_type),
        inputs=inputs,
        outputs=outputs,
        properties=properties,
        type_properties=type_properties,
        item_collections=item_collections,
    )
