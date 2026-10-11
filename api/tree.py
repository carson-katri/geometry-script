"""Build Blender node groups from ordinary Python functions."""

from __future__ import annotations

import contextlib
import functools
import inspect
from collections import namedtuple
from collections.abc import Callable, Iterator, Mapping
from typing import Any

import bpy

from .naming import attribute_names, class_name, humanize
from .runtime import (
    BuildContext,
    ItemOutputs,
    MissingOutput,
    Socket,
    activate_build_context,
    current_build_context,
    reset_build_context,
    resolve_socket,
    with_output_hints,
)
from .socket_types import (
    INTERFACE_VECTOR_DIMENSIONS,
    interface_socket_spec,
    literal_socket_type,
    resolve_builder_annotations,
)


# Names of the trees built since this list was last cleared, in build order.
built_tree_names: list[str] = []


def tree_output_values(value: Any) -> list[tuple[str, Any]]:
    """Name the values a builder returned, in order."""
    if value is None:
        return []
    if isinstance(value, Mapping):
        return [(str(name), item) for name, item in value.items()]
    if isinstance(value, ItemOutputs):
        return list(value._asdict().items())
    if isinstance(value, tuple) and hasattr(type(value), "_fields"):
        return list(zip(type(value)._fields, value, strict=True))
    if isinstance(value, (tuple, list)):
        return [
            ("Result" if index == 0 else f"Result {index + 1}", item)
            for index, item in enumerate(value)
        ]
    if inspect.isgenerator(value):
        return tree_output_values(tuple(value))
    return [("Result", value)]


def _create_or_reuse_tree(name: str) -> bpy.types.GeometryNodeTree:
    node_tree = bpy.data.node_groups.get(name)
    if node_tree is not None and node_tree.bl_idname != "GeometryNodeTree":
        bpy.data.node_groups.remove(node_tree, do_unlink=True)
        node_tree = None
    if node_tree is None:
        node_tree = bpy.data.node_groups.new(name, "GeometryNodeTree")
    else:
        for node in tuple(node_tree.nodes):
            node_tree.nodes.remove(node)
        node_tree.interface.clear()
    node_tree.is_modifier = True
    return node_tree


_MODIFIER_INPUT_FIELDS = ("value", "type", "attribute_name")


def _modifier_input_values(node_tree: bpy.types.NodeTree) -> list[tuple[Any, dict[str, dict[str, Any]]]]:
    """The input values of each modifier using ``node_tree``, by input name.

    Rebuilding gives the interface new socket identifiers, which modifiers use
    to store their values, so they are carried over by name instead.
    """
    saved = []
    inputs = [
        item for item in node_tree.interface.items_tree
        if item.item_type == "SOCKET" and item.in_out == "INPUT"
    ]
    for owner in bpy.data.objects:
        for modifier in owner.modifiers:
            if modifier.type != "NODES" or modifier.node_group != node_tree:
                continue
            values = {}
            for item in inputs:
                stored = getattr(modifier.properties.inputs, item.identifier, None)
                if stored is not None:
                    values[item.name] = {
                        field: getattr(stored, field)
                        for field in _MODIFIER_INPUT_FIELDS
                        if hasattr(stored, field)
                    }
            saved.append((modifier, values))
    return saved


def _restore_modifier_input_values(
    node_tree: bpy.types.NodeTree, saved: list[tuple[Any, dict[str, dict[str, Any]]]]
) -> None:
    inputs = [
        item for item in node_tree.interface.items_tree
        if item.item_type == "SOCKET" and item.in_out == "INPUT"
    ]
    for modifier, values in saved:
        if modifier.node_group != node_tree:
            continue
        for item in inputs:
            stored = getattr(modifier.properties.inputs, item.identifier, None)
            if stored is None:
                continue
            if item.name in values:
                fields = values[item.name]
            elif hasattr(item, "default_value"):
                fields = {"value": item.default_value}
            else:
                continue
            for field, value in fields.items():
                try:
                    setattr(stored, field, value)
                except (AttributeError, TypeError, ValueError, RuntimeError):
                    pass  # The input's type changed; keep its new default.


@contextlib.contextmanager
def _rebuild_transaction(name: str) -> Iterator[bpy.types.GeometryNodeTree]:
    """Yield the cleared tree ``name``; if the build fails, restore what was there.

    Modifiers using the tree keep their input values either way.
    """
    existing = bpy.data.node_groups.get(name)
    backup = existing.copy() if existing is not None else None
    saved = _modifier_input_values(existing) if existing is not None else []
    node_tree = _create_or_reuse_tree(name)
    try:
        yield node_tree
    except BaseException:
        if node_tree is existing and backup is not None:
            node_tree.user_remap(backup)
        bpy.data.node_groups.remove(node_tree)
        if backup is not None:
            backup.name = name
            _restore_modifier_input_values(backup, saved)
        raise
    if backup is not None:
        bpy.data.node_groups.remove(backup)
    _restore_modifier_input_values(node_tree, saved)


def _socket_reference(interface_socket: Any, index: int) -> tuple[str, str, int]:
    return (interface_socket.identifier, interface_socket.name, index)


def _socket_output_reference(interface_socket: Any, index: int) -> tuple[str, str, int, str]:
    structure_type = getattr(interface_socket, "structure_type", "AUTO")
    if structure_type not in {"FIELD", "GRID", "LIST"}:
        structure_type = "AUTO"
    return (*_socket_reference(interface_socket, index), structure_type)


def _check_parameters(parameters: list[inspect.Parameter]) -> None:
    unsupported = {
        inspect.Parameter.VAR_POSITIONAL,
        inspect.Parameter.VAR_KEYWORD,
        inspect.Parameter.POSITIONAL_ONLY,
    }
    if any(parameter.kind in unsupported for parameter in parameters):
        raise TypeError("@tree functions must use named positional or keyword-only parameters.")


def _new_interface_socket(
    node_tree: bpy.types.GeometryNodeTree, name: str, in_out: str, socket_type: str
) -> Any:
    dimensions = INTERFACE_VECTOR_DIMENSIONS.get(socket_type)
    try:
        interface_socket = node_tree.interface.new_socket(
            name=name,
            in_out=in_out,
            socket_type="NodeSocketVector" if dimensions else socket_type,
        )
    except TypeError:
        kind = "input" if in_out == "INPUT" else "output"
        raise TypeError(
            f"Geometry node groups cannot have {socket_type.removeprefix('NodeSocket')} "
            f"{kind}s ({name!r})."
        ) from None
    if dimensions is not None:
        # Changing the dimensions replaces the item with a differently typed one.
        identifier = interface_socket.identifier
        interface_socket.dimensions = dimensions
        interface_socket = next(
            item
            for item in node_tree.interface.items_tree
            if item.item_type == "SOCKET" and item.identifier == identifier
        )
    return interface_socket


def _add_interface_input(
    node_tree: bpy.types.GeometryNodeTree,
    parameter: inspect.Parameter,
    annotation: Any,
) -> tuple[Any, str]:
    """Add the group input for a builder parameter; returns it and its structure type."""
    socket_type, structure_type = interface_socket_spec(
        annotation,
        default=parameter.default,
        parameter_name=parameter.name,
    )
    interface_socket = _new_interface_socket(
        node_tree, humanize(parameter.name), "INPUT", socket_type
    )
    if structure_type != "AUTO":
        try:
            interface_socket.structure_type = structure_type
        except (AttributeError, TypeError, ValueError, RuntimeError) as error:
            raise TypeError(
                f"The {structure_type} structure is not supported by "
                f"{socket_type} for tree input {parameter.name!r}."
            ) from error
    # A menu input has no items until it is linked to a menu, so its default waits.
    if socket_type != "NodeSocketMenu":
        _set_interface_default(interface_socket, parameter)
    return interface_socket, structure_type


def _set_interface_default(interface_socket: Any, parameter: inspect.Parameter) -> None:
    if parameter.default is inspect.Parameter.empty:
        return
    try:
        interface_socket.default_value = parameter.default
    except (AttributeError, TypeError, ValueError, RuntimeError) as error:
        if parameter.default is not None:
            raise TypeError(
                f"Default value {parameter.default!r} is invalid for tree input "
                f"{parameter.name!r}."
            ) from error


def _add_interface_outputs(context: BuildContext, result: Any) -> None:
    """Add a group output for each value the builder returned, and link it."""
    node_tree = context.node_tree
    interface_outputs = []
    sources = []
    for output_name, output_value in tree_output_values(result):
        if isinstance(output_value, MissingOutput):
            raise output_value.error()
        if isinstance(output_value, Socket):
            if output_value.context is not context:
                raise ValueError("A tree output cannot use a socket from another node tree.")
            socket_type = output_value.socket_type
            structure_type = output_value.structure_type
            source = output_value
        else:
            socket_type = literal_socket_type(output_value)
            structure_type = "AUTO"
            source = context.constant_socket(output_value, socket_type)

        interface_socket = _new_interface_socket(
            node_tree, output_name, "OUTPUT", socket_type
        )
        if structure_type != "AUTO":
            interface_socket.structure_type = structure_type
        interface_outputs.append(interface_socket)
        sources.append(source)

    group_output = node_tree.nodes.new("NodeGroupOutput")
    group_output.is_active_output = True
    for index, (interface_socket, source) in enumerate(
        zip(interface_outputs, sources, strict=True)
    ):
        output_input = resolve_socket(
            group_output.inputs, _socket_reference(interface_socket, index)
        )
        context.link(source, output_input)


def _fill_tree(
    node_tree: bpy.types.GeometryNodeTree,
    builder: Callable[..., Any],
    parameters: list[inspect.Parameter],
) -> dict[str, tuple[Any, str]]:
    """Add the interface and nodes for ``builder``; returns its inputs by parameter."""
    context = BuildContext(node_tree)
    annotations = resolve_builder_annotations(builder)
    interface_inputs = {
        parameter.name: _add_interface_input(
            node_tree,
            parameter,
            annotations.get(parameter.name, parameter.annotation),
        )
        for parameter in parameters
    }

    group_input = node_tree.nodes.new("NodeGroupInput")
    builder_values = {
        parameter_name: Socket(
            resolve_socket(group_input.outputs, _socket_reference(interface_socket, index)),
            context,
            structure_type=structure_type,
        )
        for index, (parameter_name, (interface_socket, structure_type)) in enumerate(
            interface_inputs.items()
        )
    }

    token = activate_build_context(context)
    try:
        _add_interface_outputs(context, builder(**builder_values))
    finally:
        reset_build_context(token)
    context.validate_links()
    for parameter in parameters:
        interface_socket, _ = interface_inputs[parameter.name]
        if interface_socket.bl_socket_idname == "NodeSocketMenu":
            _set_interface_default(interface_socket, parameter)
    return interface_inputs


def _build_tree(
    name: str, builder: Callable[..., Any]
) -> tuple[bpy.types.GeometryNodeTree, inspect.Signature, dict[str, Any]]:
    """Build the node group; returns it, the builder signature and its inputs by parameter."""
    signature = inspect.signature(builder)
    parameters = list(signature.parameters.values())
    _check_parameters(parameters)

    with _rebuild_transaction(name) as node_tree:
        interface_inputs = _fill_tree(node_tree, builder, parameters)
    built_tree_names.append(node_tree.name)

    interface_sockets = {
        parameter_name: interface_socket
        for parameter_name, (interface_socket, _) in interface_inputs.items()
    }
    return node_tree, signature, interface_sockets


def _tree_function(name: str, builder: Callable[..., Any]) -> Callable[..., Any]:
    node_tree, signature, interface_inputs = _build_tree(name, builder)
    input_specs = {
        parameter_name: _socket_reference(interface_socket, index)
        for index, (parameter_name, interface_socket) in enumerate(interface_inputs.items())
    }
    interface_outputs = [
        item
        for item in node_tree.interface.items_tree
        if item.item_type == "SOCKET" and item.in_out == "OUTPUT"
    ]
    output_names = attribute_names(socket.name for socket in interface_outputs)
    output_specs = {
        output_name: _socket_output_reference(interface_socket, index)
        for index, (output_name, interface_socket) in enumerate(
            zip(output_names, interface_outputs, strict=True)
        )
    }
    output_type_name = f"{class_name(builder.__name__, 'Tree')}Outputs"
    output_type = with_output_hints(namedtuple(output_type_name, output_names))

    @functools.wraps(builder)
    def group_reference(*args: Any, **kwargs: Any) -> Any:
        context = current_build_context()
        if context is None:
            return node_tree

        bound = signature.bind(*args, **kwargs)
        bound.apply_defaults()
        outputs = context.create_node(
            "GeometryNodeGroup",
            inputs={name: bound.arguments[name] for name in input_specs},
            input_sockets=input_specs,
            properties={"node_tree": node_tree},
            output_sockets=output_specs,
            output_type=None,
        )
        if not outputs:
            return None
        if len(outputs) == 1:
            return outputs[0]
        return output_type(*outputs)

    group_reference.__signature__ = signature  # type: ignore[attr-defined]
    group_reference.node_tree = node_tree  # type: ignore[attr-defined]
    group_reference.builder = builder  # type: ignore[attr-defined]
    return group_reference


def tree(
    name_or_builder: str | Callable[..., Any] | None = None,
) -> Callable[..., Any]:
    """Build or rebuild a Geometry Nodes group from a decorated function.

    A bare ``@tree`` uses the function name. ``@tree("Name")`` uses the given
    group name. Calling the decorated function inside another active ``@tree``
    creates a node-group instance; calling it outside a build returns its tree.
    """

    def decorate(builder: Callable[..., Any], name: str | None = None) -> Callable[..., Any]:
        return _tree_function(name or builder.__name__, builder)

    if isinstance(name_or_builder, str):
        return lambda builder: decorate(builder, name_or_builder)
    if callable(name_or_builder):
        return decorate(name_or_builder)
    if name_or_builder is None:
        return lambda builder: decorate(builder)
    raise TypeError("@tree expects a function, a tree name, or no argument.")
