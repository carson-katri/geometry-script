"""Create user-defined node items (zone items, capture items, bundle items, ...)."""

from __future__ import annotations

import inspect
from collections.abc import Sequence
from typing import Any

import bpy

from .runtime import BuildContext, Socket, literal_kind
from .socket_types import interface_socket_spec, literal_socket_type


# Socket.type values that differ from the item socket_type enum.
_SOCKET_KIND_ITEM_TYPES = {"VALUE": "FLOAT", "CUSTOM": "GEOMETRY"}
_SOCKET_ID_ITEM_TYPES = {
    "NodeSocketFloat": "FLOAT",
    "NodeSocketInt": "INT",
    "NodeSocketBool": "BOOLEAN",
    "NodeSocketVector": "VECTOR",
    "NodeSocketVector2D": "VECTOR",
    "NodeSocketVector4D": "VECTOR",
    "NodeSocketColor": "RGBA",
    "NodeSocketIntVector2D": "INT_VECTOR",
    "NodeSocketIntVector3D": "INT_VECTOR",
}


def _socket_id_item_type(socket_id: str) -> str:
    return _SOCKET_ID_ITEM_TYPES.get(
        socket_id, socket_id.removeprefix("NodeSocket").upper()
    )


def socket_item_type(socket: Socket[Any]) -> str:
    kind = socket.node_socket.type
    return _SOCKET_KIND_ITEM_TYPES.get(kind, kind)


def literal_item_type(value: Any) -> str | None:
    """The item type a literal clearly asks for (see ``literal_kind``)."""
    kind = literal_kind(value)
    return _SOCKET_KIND_ITEM_TYPES.get(kind, kind) if kind is not None else None


def item_type(annotation: Any, value: Any, name: str) -> str:
    """Choose an item socket_type from an annotation, else from the value."""
    if annotation is inspect.Parameter.empty:
        if isinstance(value, Socket):
            return socket_item_type(value)
        try:
            return _socket_id_item_type(literal_socket_type(value))
        except TypeError:
            raise TypeError(
                f"Cannot infer a socket type for item {name!r} from {value!r}; "
                "pass a socket or annotate it."
            ) from None
    socket_id, _ = interface_socket_spec(
        annotation, default=value, parameter_name=name
    )
    return _socket_id_item_type(socket_id)


def marker_item_type(marker: Any, name: str) -> str:
    """Item socket_type for a type marker such as ``float``, ``Vector`` or ``"FLOAT"``."""
    if isinstance(marker, str) and marker.isupper():
        return marker
    return item_type(marker, inspect.Parameter.empty, name)


def data_sockets(sockets: Any) -> list[bpy.types.NodeSocket]:
    return [
        socket
        for socket in sockets
        if socket.enabled and socket.bl_idname != "NodeSocketVirtual"
    ]


def socket_identifiers(sockets: Any) -> set[str]:
    return {socket.identifier for socket in sockets}


def new_sockets(sockets: Any, before: set[str]) -> list[bpy.types.NodeSocket]:
    """The data sockets whose identifiers are not in ``before``."""
    return [socket for socket in data_sockets(sockets) if socket.identifier not in before]


def clear_items(items: Any) -> None:
    try:
        items.clear()
    except (AttributeError, RuntimeError):
        while len(items):
            items.remove(items[len(items) - 1])


def add_items(
    context: BuildContext,
    node: bpy.types.Node,
    collections: Sequence[tuple[str, str, Any]],
) -> list[bpy.types.NodeSocket]:
    """Replace each given item collection and link the item values.

    Returns the output sockets the new items created, in order.
    """
    item_outputs: list[bpy.types.NodeSocket] = []
    for identifier, mode, values in collections:
        if not values:
            continue
        items = getattr(node, identifier)
        clear_items(items)
        inputs_before = socket_identifiers(node.inputs)
        outputs_before = socket_identifiers(node.outputs)

        def new_item(*arguments: Any) -> None:
            try:
                items.new(*arguments)
            except RuntimeError as error:
                raise TypeError(
                    f"{node.name!r} cannot add item {arguments!r}: {error}"
                ) from None

        linked: list[Any] = []
        if mode == "values":
            for name, value in values.items():
                new_item(item_type(inspect.Parameter.empty, value, name), name)
                linked.append(value)
        elif mode == "named":
            for name, value in values.items():
                new_item(name)
                linked.append(value)
        elif mode == "sequence":
            for value in values:
                new_item()
                linked.append(value)
        elif mode == "types":
            for name, marker in values.items():
                new_item(marker_item_type(marker, name), name)
        else:
            raise ValueError(f"Unknown item mode {mode!r}.")

        for value, socket in zip(linked, new_sockets(node.inputs, inputs_before), strict=True):
            context.set_input(socket, value)
        item_outputs.extend(new_sockets(node.outputs, outputs_before))
    return item_outputs
