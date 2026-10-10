"""Runtime socket values and node creation helpers used by generated code."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from contextvars import ContextVar, Token
from typing import Any, Generic, TypeVar

import bpy


T = TypeVar("T")


class Socket(Generic[T]):
    """A node-tree socket that can be linked or used to build an expression."""

    __slots__ = ("node_socket", "context", "structure_type")

    def __init__(
        self,
        node_socket: bpy.types.NodeSocket,
        context: BuildContext,
        structure_type: str = "AUTO",
    ) -> None:
        self.node_socket = node_socket
        self.context = context
        self.structure_type = structure_type

    @property
    def name(self) -> str:
        return self.node_socket.name

    @property
    def socket_type(self) -> str:
        return self.node_socket.bl_idname

    def _binary(self, other: Any, operation: str, *, reverse: bool = False) -> Socket[Any]:
        if self.context is not current_build_context():
            raise RuntimeError("Socket expressions can only be built in their active @tree.")

        left, right = (other, self) if reverse else (self, other)
        socket_kind = self.node_socket.type
        if socket_kind == "VECTOR":
            node_type_id = "ShaderNodeVectorMath"
            input_names = (("Vector", 0), ("Vector_001", 1))
            output_name = "Vector"
        elif socket_kind in {"VALUE", "INT"}:
            node_type_id = "ShaderNodeMath"
            input_names = (("Value", 0), ("Value_001", 1))
            output_name = "Value"
        else:
            raise TypeError(f"Arithmetic is not supported for {self.node_socket.bl_idname}.")

        outputs = self.context.create_node(
            node_type_id,
            inputs={"left": left, "right": right},
            input_sockets={
                "left": ("", input_names[0][0], input_names[0][1]),
                "right": ("", input_names[1][0], input_names[1][1]),
            },
            properties={"operation": operation},
            output_sockets={
                "result": ("", output_name, 0, "FIELD"),
            },
            output_type=None,
        )
        return outputs[0]

    def __add__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "ADD")

    def __radd__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "ADD", reverse=True)

    def __sub__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "SUBTRACT")

    def __rsub__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "SUBTRACT", reverse=True)

    def __mul__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "MULTIPLY")

    def __rmul__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "MULTIPLY", reverse=True)

    def __truediv__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "DIVIDE")

    def __rtruediv__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "DIVIDE", reverse=True)

    def __mod__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "MODULO")

    def __rmod__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "MODULO", reverse=True)

    def __pow__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "POWER")

    def __rpow__(self, other: Any) -> Socket[Any]:
        return self._binary(other, "POWER", reverse=True)

    def __neg__(self) -> Socket[Any]:
        if self.node_socket.type == "VECTOR":
            outputs = self.context.create_node(
                "ShaderNodeVectorMath",
                inputs={"vector": self, "scale": -1.0},
                input_sockets={
                    "vector": ("", "Vector", 0),
                    "scale": ("", "Scale", 1),
                },
                properties={"operation": "SCALE"},
                output_sockets={"result": ("", "Vector", 0, "FIELD")},
                output_type=None,
            )
            return outputs[0]
        return self._binary(-1.0, "MULTIPLY")

    def __repr__(self) -> str:
        return f"Socket({self.node_socket.node.name}.{self.node_socket.name})"


class ItemOutputs:
    """Outputs of a node with user-defined items.

    Fixed outputs are attributes; item outputs are reachable by their item
    name, as an attribute or with ``outputs["Item Name"]``. Iterating yields
    every output in node order.
    """

    __slots__ = ("_values",)

    def __init__(self, values: Mapping[str, Socket[Any] | None]) -> None:
        object.__setattr__(self, "_values", dict(values))

    def __getattr__(self, name: str) -> Socket[Any]:
        try:
            return self._values[name]  # type: ignore[return-value]
        except KeyError:
            raise AttributeError(
                f"{type(self).__name__} has no output {name!r}; "
                f"available: {list(self._values)!r}."
            ) from None

    def __getitem__(self, key: str | int) -> Socket[Any]:
        if isinstance(key, int):
            return list(self._values.values())[key]  # type: ignore[return-value]
        return self._values[key]  # type: ignore[return-value]

    def __iter__(self) -> Any:
        return iter(self._values.values())

    def __len__(self) -> int:
        return len(self._values)

    def _asdict(self) -> dict[str, Socket[Any] | None]:
        return dict(self._values)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({', '.join(self._values)})"


class BuildContext:
    """Build nodes and links in one Blender node tree."""

    def __init__(self, node_tree: bpy.types.NodeTree) -> None:
        self.node_tree = node_tree

    def create_node(
        self,
        node_type_id: str,
        *,
        inputs: Mapping[str, Any],
        input_sockets: Mapping[str, tuple[Any, ...]],
        properties: Mapping[str, Any],
        output_sockets: Mapping[str, tuple[str, str, int, str]],
        output_type: type | None,
        type_properties: Mapping[str, Mapping[str, Mapping[str, str]]] | None = None,
        item_collections: Sequence[tuple[str, str, Any]] = (),
    ) -> Any:
        from .items import add_items

        node = self.node_tree.nodes.new(node_type_id)

        # Inputs left at their generated default keep Blender's own default,
        # which also holds after a type property changes the socket's type.
        given = {
            name: value
            for name, value in inputs.items()
            if not _is_default(value, input_sockets[name])
        }
        properties = _with_inferred_types(
            properties, type_properties or {}, given, item_collections
        )
        self._set_properties(node, properties)
        item_outputs = add_items(self, node, item_collections)
        self._set_inputs(node, given, input_sockets, properties)

        if output_type is None and not output_sockets:
            return None
        outputs = self._outputs(node, output_sockets)
        if output_type is None:
            return tuple(outputs.values())
        if issubclass(output_type, ItemOutputs):
            for socket in item_outputs:
                outputs[socket.name] = self.wrap(socket)
            return output_type(outputs)
        return output_type(*outputs.values())

    def _set_properties(self, node: bpy.types.Node, properties: Mapping[str, Any]) -> None:
        for identifier, value in properties.items():
            if value is None:
                continue
            try:
                setattr(node, identifier, value)
            except Exception as error:
                node_type_id = node.bl_idname
                self.node_tree.nodes.remove(node)
                raise TypeError(
                    f"Cannot set {node_type_id}.{identifier} to {value!r}."
                ) from error

    def _set_inputs(
        self,
        node: bpy.types.Node,
        given: Mapping[str, Any],
        input_sockets: Mapping[str, tuple[Any, ...]],
        properties: Mapping[str, Any],
    ) -> None:
        for name, value in given.items():
            try:
                input_socket = resolve_socket(node.inputs, input_sockets[name][:3])
            except LookupError:
                settings = {
                    identifier: getattr(node, identifier) for identifier in properties
                }
                raise TypeError(
                    f"{node.name!r} has no {name!r} input with its current "
                    f"settings {settings!r}."
                ) from None
            self.set_input(input_socket, value)

    def _outputs(
        self,
        node: bpy.types.Node,
        output_sockets: Mapping[str, tuple[str, str, int, str]],
    ) -> dict[str, Socket[Any] | None]:
        outputs: dict[str, Socket[Any] | None] = {}
        for field_name, reference in output_sockets.items():
            try:
                output_socket = resolve_socket(node.outputs, reference[:3])
            except LookupError:
                # This output does not exist with the node's current settings.
                outputs[field_name] = None
                continue
            outputs[field_name] = self.wrap(output_socket, reference[3])
        return outputs

    def wrap(self, socket: bpy.types.NodeSocket, structure_type: str = "AUTO") -> Socket[Any]:
        """A Socket for a node socket in this tree; AUTO asks Blender for the structure."""
        if structure_type == "AUTO":
            structure_type = inferred_structure_type(socket)
        return Socket(socket, self, structure_type=structure_type)

    def validate_links(self) -> None:
        """Raise if Blender rejected any link, e.g. Geometry into a Float input."""
        problems = []
        for link in self.node_tree.links:
            if link.is_valid:
                continue
            source, target = link.from_socket, link.to_socket
            problem = (
                f"{link.to_node.name!r} input {target.name!r} ({target.bl_idname}) "
                f"cannot take {link.from_node.name!r} output {source.name!r} "
                f"({source.bl_idname})."
            )
            hints = _type_property_hints(link.to_node)
            if hints:
                problem += f" Set the node's type, one of: {hints}."
            problems.append(problem)
        if problems:
            raise TypeError(
                f"Invalid links in {self.node_tree.name!r}:\n  " + "\n  ".join(problems)
            )

    def set_input(self, node_input: bpy.types.NodeSocket, value: Any) -> None:
        """Link a Socket into ``node_input``, or store a literal as its value."""
        if isinstance(value, Socket):
            self.link(value, node_input)
            return

        if value is None:
            try:
                node_input.default_value = None
            except (AttributeError, TypeError, ValueError, RuntimeError):
                pass
            return

        if node_input.is_multi_input:
            if self._is_multi_input_sequence(value, node_input.bl_idname):
                values = value
            else:
                values = (value,)
            for item in values:
                if isinstance(item, Socket):
                    self.link(item, node_input)
                elif item is not None:
                    self.link(
                        self.constant_socket(item, node_input.bl_idname), node_input
                    )
            return

        try:
            node_input.default_value = value
        except (AttributeError, TypeError, ValueError, RuntimeError):
            self.link(self.constant_socket(value, node_input.bl_idname), node_input)

    def link(self, source: Socket | bpy.types.NodeSocket, target: bpy.types.NodeSocket) -> None:
        if isinstance(source, Socket):
            if source.context is not self:
                raise ValueError("Cannot connect sockets from different node trees.")
            source_socket = source.node_socket
        else:
            source_socket = source
        self.node_tree.links.new(source_socket, target)

    def constant_socket(self, value: Any, socket_id: str) -> bpy.types.NodeSocket:
        """Add an input node holding ``value`` for a ``socket_id`` socket."""
        vector_dimensions: int | None = None
        if isinstance(value, bool):
            node_type_id, property_name = "FunctionNodeInputBool", "boolean"
        elif isinstance(value, int):
            node_type_id, property_name = "FunctionNodeInputInt", "integer"
        elif isinstance(value, float):
            node_type_id, property_name = "ShaderNodeValue", "default_value"
        elif isinstance(value, str):
            node_type_id, property_name = "FunctionNodeInputString", "string"
        elif isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
            if "Color" in socket_id:
                node_type_id, property_name = "FunctionNodeInputColor", "value"
            elif "IntVector" in socket_id:
                node_type_id, property_name = "FunctionNodeInputIntVector", "vector"
                vector_dimensions = len(value)
            elif "Vector" in socket_id:
                node_type_id, property_name = "FunctionNodeInputVector", "vector"
                vector_dimensions = len(value)
            else:
                raise TypeError(f"Cannot make a constant node for {socket_id}.")
        else:
            raise TypeError(
                f"A literal of type {type(value).__name__} cannot be linked to {socket_id}."
            )

        node = self.node_tree.nodes.new(node_type_id)
        if property_name == "default_value":
            node.outputs[0].default_value = value
        else:
            if vector_dimensions is not None:
                node.vector_dimensions = vector_dimensions
            setattr(node, property_name, value)
        return node.outputs[0]

    @staticmethod
    def _is_multi_input_sequence(value: Any, socket_id: str) -> bool:
        if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
            return False
        if "Vector" not in socket_id and "Color" not in socket_id:
            return True
        if not value:
            return True
        if "Color" in socket_id or "Vector4" in socket_id:
            dimensions = 4
        elif "Vector2" in socket_id:
            dimensions = 2
        else:
            dimensions = 3
        return not (
            len(value) == dimensions
            and all(isinstance(component, (int, float)) for component in value)
        )


_NO_DEFAULT = object()


def _is_default(value: Any, reference: tuple[Any, ...]) -> bool:
    default = reference[3] if len(reference) > 3 else _NO_DEFAULT
    if default is _NO_DEFAULT or isinstance(value, Socket):
        return False
    if isinstance(default, tuple) and isinstance(value, (tuple, list)):
        return len(value) == len(default) and all(
            type(item) is type(expected) and item == expected
            for item, expected in zip(value, default)
        )
    return type(value) is type(default) and value == default


def literal_kind(value: Any) -> str | None:
    """The socket kind a Python literal clearly asks for, if any.

    Integers are left out on purpose: ``1`` is as likely meant as a float.
    """
    if isinstance(value, bool):
        return "BOOLEAN"
    if isinstance(value, float):
        return "VALUE"
    if isinstance(value, str):
        return "STRING"
    if isinstance(value, (tuple, list)) and all(
        isinstance(item, (int, float)) and not isinstance(item, bool) for item in value
    ):
        return {3: "VECTOR", 4: "RGBA"}.get(len(value))
    return None


def _with_inferred_types(
    properties: Mapping[str, Any],
    type_properties: Mapping[str, Mapping[str, Mapping[str, str]]],
    given: Mapping[str, Any],
    item_collections: Sequence[tuple[str, str, Any]],
) -> dict[str, Any]:
    """Fill type properties left as None from the inputs and item values."""
    # Items typed by the node itself (Index/Menu Switch) decide its type.
    item_values = [
        value
        for _, mode, values in item_collections
        if values and mode in {"named", "sequence"}
        for value in (values.values() if mode == "named" else values)
    ]
    properties = dict(properties)
    for identifier, kinds in type_properties.items():
        if properties.get(identifier) is None:
            properties[identifier] = _infer_type_property(kinds, given, item_values)
    return properties


def _infer_type_property(
    kinds: Mapping[str, Mapping[str, str]],
    given: Mapping[str, Any],
    item_values: Sequence[Any] = (),
) -> str | None:
    """Pick the first property value whose sockets match the given inputs.

    Linked sockets decide first, then literals; None keeps Blender's default.
    Item values (Index/Menu Switch) match properties whose values are item
    socket types, such as ``input_type='GEOMETRY'``.
    """

    def sockets_in(value: Any) -> list[Socket[Any]]:
        if isinstance(value, Socket):
            return [value]
        if isinstance(value, (list, tuple)):
            return [item for item in value if isinstance(item, Socket)]
        return []

    for find_kind in (
        lambda value: next((s.node_socket.type for s in sockets_in(value)), None),
        literal_kind,
    ):
        for name, value in given.items():
            kind = find_kind(value)
            if kind is None:
                continue
            for property_value, socket_kinds in kinds.items():
                if socket_kinds.get(name) == kind:
                    return property_value

    from .items import literal_item_type, socket_item_type

    for find_type in (
        lambda value: socket_item_type(value) if isinstance(value, Socket) else None,
        literal_item_type,
    ):
        for value in item_values:
            item_type = find_type(value)
            if item_type in kinds:
                return item_type
    return None


def _type_property_hints(node: bpy.types.Node) -> str:
    """Describe enum properties that choose a node's socket types."""
    hints = []
    for prop in node.bl_rna.properties:
        if (
            prop.type == "ENUM"
            and not prop.is_readonly
            and prop.identifier.endswith(("data_type", "input_type"))
        ):
            values = ", ".join(repr(item.identifier) for item in prop.enum_items)
            hints.append(f"{prop.identifier}=({values})")
    return "; ".join(hints)


_BUILD_CONTEXT: ContextVar[BuildContext | None] = ContextVar(
    "geometry_script_build_context", default=None
)


def current_build_context() -> BuildContext | None:
    """Return the tree currently being built, if a @tree decorator is active."""
    return _BUILD_CONTEXT.get()


def activate_build_context(context: BuildContext) -> Token[BuildContext | None]:
    return _BUILD_CONTEXT.set(context)


def reset_build_context(token: Token[BuildContext | None]) -> None:
    _BUILD_CONTEXT.reset(token)


def node_function(
    node_type_id: str,
    *,
    inputs: Mapping[str, Any],
    input_sockets: Mapping[str, tuple[Any, ...]],
    properties: Mapping[str, Any],
    output_sockets: Mapping[str, tuple[str, str, int, str]],
    output_type: type | None,
    type_properties: Mapping[str, Mapping[str, Mapping[str, str]]] | None = None,
    item_collections: Sequence[tuple[str, str, Any]] = (),
) -> Any:
    """Add a node to the active @tree. Called by the generated node functions."""
    context = current_build_context()
    if context is None:
        raise RuntimeError("Node functions must be called while building a @tree.")
    return context.create_node(
        node_type_id,
        inputs=inputs,
        input_sockets=input_sockets,
        properties=properties,
        output_sockets=output_sockets,
        output_type=output_type,
        type_properties=type_properties,
        item_collections=item_collections,
    )


def resolve_socket(
    sockets: Sequence[bpy.types.NodeSocket],
    reference: tuple[str, str, int],
) -> bpy.types.NodeSocket:
    identifier, name, index = reference
    available = [
        socket
        for socket in sockets
        if socket.enabled and socket.bl_idname != "NodeSocketVirtual"
    ]

    if identifier:
        for socket in available:
            if socket.identifier == identifier:
                return socket

    same_name = [socket for socket in available if socket.name == name]
    if len(same_name) == 1:
        return same_name[0]
    if 0 <= index < len(sockets):
        indexed = sockets[index]
        if indexed in available:
            return indexed
    if same_name:
        return same_name[0]
    raise LookupError(
        f"Could not find Blender socket {name!r} ({identifier!r}) among "
        f"{[socket.name for socket in available]!r}."
    )


def inferred_structure_type(socket: bpy.types.NodeSocket) -> str:
    inferred = getattr(socket, "inferred_structure_type", "AUTO")
    if inferred in {"FIELD", "GRID", "LIST"}:
        return inferred
    if socket.display_shape in {"DIAMOND", "DIAMOND_DOT"}:
        return "FIELD"
    if socket.display_shape == "VOLUME_GRID":
        return "GRID"
    if socket.display_shape == "LIST":
        return "LIST"
    return "AUTO"
