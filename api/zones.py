"""Build node zones (repeat, simulation, closure, for-each) from decorated functions.

A zone's body is an ordinary Python function. Its parameters become the zone's
items and its return values feed the zone output, in the same order::

    @repeat_zone
    def grow(geometry: Geometry, size: float, iteration: int):
        ...
        return new_geometry, size * 2.0

    # Inside a @tree:
    result = grow(geometry, 1.0, iterations=4)
    result.geometry, result.size
"""

from __future__ import annotations

import functools
import inspect
from collections import namedtuple
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any

import bpy

from .items import (
    clear_items,
    data_sockets,
    item_type,
    new_sockets,
    socket_identifiers,
    socket_item_type,
)
from .naming import class_name, humanize, identifier, unique_name
from .runtime import BuildContext, ItemOutputs, Socket, current_build_context
from .socket_types import resolve_builder_annotations
from .tree import tree_output_values


@dataclass(frozen=True)
class _ZoneKind:
    input_node: str
    output_node: str
    items: str
    # Optional body parameter bound to a built-in zone input output, such as
    # the repeat iteration index, and the socket name it reads from.
    special_parameter: str | None
    special_output: str | None
    # Fixed sockets that precede the items on each node.
    input_node_controls: int
    output_node_controls: int


_REPEAT = _ZoneKind(
    "GeometryNodeRepeatInput", "GeometryNodeRepeatOutput", "repeat_items",
    "iteration", "Iteration", 1, 0,
)
_SIMULATION = _ZoneKind(
    "GeometryNodeSimulationInput", "GeometryNodeSimulationOutput", "state_items",
    "delta_time", "Delta Time", 0, 1,
)


def _active_context(builder: Callable[..., Any]) -> BuildContext:
    context = current_build_context()
    if context is None:
        raise RuntimeError(
            f"Zone {builder.__name__!r} must be called while building a tree."
        )
    return context


def _new_zone(
    context: BuildContext, input_node: str, output_node: str, *item_collections: str
) -> tuple[bpy.types.Node, bpy.types.Node]:
    """Add a paired zone input and output, with the output's item lists emptied."""
    zone_input = context.new_node(input_node)
    zone_output = context.new_node(output_node)
    zone_input.pair_with_output(zone_output)
    for collection in item_collections:
        clear_items(getattr(zone_output, collection))
    return zone_input, zone_output


def _parameter_item_types(
    builder: Callable[..., Any],
    parameters: Sequence[inspect.Parameter],
    values: Mapping[str, Any],
) -> list[str]:
    """Item socket types for body parameters, from annotations, else their values."""
    annotations = resolve_builder_annotations(builder)
    return [
        item_type(
            annotations.get(parameter.name, inspect.Parameter.empty),
            values[parameter.name],
            parameter.name,
        )
        for parameter in parameters
    ]


def _value_item_type(value: Any, name: str) -> str:
    return item_type(inspect.Parameter.empty, value, name)


def _ordered_results(result: Any, names: list[str], zone_name: str) -> list[Any]:
    """Match a zone body's return value to its items by name or position."""
    if isinstance(result, Mapping):
        missing = [name for name in names if name not in result]
        if missing:
            raise ValueError(f"Zone {zone_name!r} did not return {missing!r}.")
        return [result[name] for name in names]
    values = [value for _, value in tree_output_values(result)]
    if len(values) != len(names):
        raise ValueError(
            f"Zone {zone_name!r} returned {len(values)} value(s) but has "
            f"{len(names)} item(s): {names!r}."
        )
    return values


def _wrap_outputs(
    name: str, names: list[str], sockets: list[bpy.types.NodeSocket], context: BuildContext
) -> Any:
    values = [context.wrap(socket) for socket in sockets]
    if len(values) == 1:
        return values[0]
    return namedtuple(f"{class_name(name, 'Zone')}Outputs", names)(*values)


def _stateful_zone(kind: _ZoneKind, control_name: str, control_socket: int, control_default: Any):
    """Make a decorator for zones whose items flow from input to output."""

    def decorate(builder: Callable[..., Any]) -> Callable[..., Any]:
        signature = inspect.signature(builder)
        item_parameters = [
            parameter
            for parameter in signature.parameters.values()
            if parameter.name != kind.special_parameter
        ]
        item_signature = signature.replace(parameters=item_parameters)
        item_names = [parameter.name for parameter in item_parameters]

        @functools.wraps(builder)
        def build(*args: Any, **kwargs: Any) -> Any:
            context = _active_context(builder)
            control_value = kwargs.pop(control_name, control_default)
            bound = item_signature.bind(*args, **kwargs)
            bound.apply_defaults()

            zone_input, zone_output = _new_zone(
                context, kind.input_node, kind.output_node, kind.items
            )
            items = getattr(zone_output, kind.items)
            for parameter, socket_type in zip(
                item_parameters,
                _parameter_item_types(builder, item_parameters, bound.arguments),
                strict=True,
            ):
                items.new(socket_type, humanize(parameter.name))

            control_target = (
                zone_input.inputs if control_socket == 0 else zone_output.inputs
            )
            context.set_input(data_sockets(control_target)[0], control_value)

            initial_inputs = data_sockets(zone_input.inputs)[kind.input_node_controls:]
            for parameter, socket in zip(item_parameters, initial_inputs, strict=True):
                context.set_input(socket, bound.arguments[parameter.name])

            body_sockets = data_sockets(zone_input.outputs)
            item_sockets = body_sockets[len(body_sockets) - len(item_parameters):]
            body_arguments = {
                parameter.name: context.wrap(socket)
                for parameter, socket in zip(item_parameters, item_sockets, strict=True)
            }
            if kind.special_parameter in signature.parameters:
                body_arguments[kind.special_parameter] = context.wrap(
                    zone_input.outputs[kind.special_output]
                )

            results = _ordered_results(builder(**body_arguments), item_names, builder.__name__)
            next_inputs = data_sockets(zone_output.inputs)[kind.output_node_controls:]
            for value, socket in zip(results, next_inputs, strict=True):
                context.set_input(socket, value)

            return _wrap_outputs(
                builder.__name__, item_names, data_sockets(zone_output.outputs), context
            )

        build.builder = builder  # type: ignore[attr-defined]
        return build

    return decorate


repeat_zone = _stateful_zone(_REPEAT, "iterations", 0, 1)
repeat_zone.__doc__ = """Build a Repeat zone. Call it with the initial item values and
``iterations=``. A body parameter named ``iteration`` receives the iteration index."""

simulation_zone = _stateful_zone(_SIMULATION, "skip", 1, False)
simulation_zone.__doc__ = """Build a Simulation zone. Call it with the initial state and
optionally ``skip=``. A body parameter named ``delta_time`` receives the frame step."""


def closure_zone(builder: Callable[..., Any]) -> Callable[..., Any]:
    """Build a Closure zone; calling it while building a tree returns the Closure socket.

    The body's parameters become the closure's inputs and its return values
    become the closure's outputs. Use ``f.evaluate(closure, ...)`` to add an
    Evaluate Closure node with matching items.
    """
    signature = inspect.signature(builder)
    parameters = list(signature.parameters.values())

    def item_types() -> list[tuple[str, str]]:
        defaults = {parameter.name: parameter.default for parameter in parameters}
        socket_types = _parameter_item_types(builder, parameters, defaults)
        return [
            (socket_type, humanize(parameter.name))
            for parameter, socket_type in zip(parameters, socket_types, strict=True)
        ]

    output_items: list[tuple[str, str]] = []

    @functools.wraps(builder)
    def build() -> Socket[Any]:
        context = _active_context(builder)
        zone_input, zone_output = _new_zone(
            context, "NodeClosureInput", "NodeClosureOutput", "input_items", "output_items"
        )
        for socket_type, name in item_types():
            zone_output.input_items.new(socket_type, name)

        body_arguments = {
            parameter.name: context.wrap(socket)
            for parameter, socket in zip(
                parameters, data_sockets(zone_input.outputs), strict=True
            )
        }
        results = tree_output_values(builder(**body_arguments))
        output_items.clear()
        for name, value in results:
            socket_type = _value_item_type(value, name)
            output_items.append((socket_type, name))
            zone_output.output_items.new(socket_type, name)
        for (_, value), socket in zip(
            results, data_sockets(zone_output.inputs), strict=True
        ):
            context.set_input(socket, value)
        return Socket(zone_output.outputs[0], context)

    def evaluate(closure: Socket[Any], *args: Any, **kwargs: Any) -> Any:
        """Evaluate a closure with this zone's signature."""
        context = _active_context(builder)
        if not output_items:
            raise RuntimeError(
                f"Build closure {builder.__name__!r} before evaluating it."
            )
        bound = signature.bind(*args, **kwargs)
        bound.apply_defaults()
        node = context.new_node("NodeEvaluateClosure")
        clear_items(node.input_items)
        clear_items(node.output_items)
        for socket_type, name in item_types():
            node.input_items.new(socket_type, name)
        for socket_type, name in output_items:
            node.output_items.new(socket_type, name)
        inputs = data_sockets(node.inputs)
        context.set_input(inputs[0], closure)
        for parameter, socket in zip(parameters, inputs[1:], strict=True):
            context.set_input(socket, bound.arguments[parameter.name])
        return _wrap_outputs(
            builder.__name__,
            [identifier(name).lower() or "result" for _, name in output_items],
            data_sockets(node.outputs),
            context,
        )

    build.evaluate = evaluate  # type: ignore[attr-defined]
    build.builder = builder  # type: ignore[attr-defined]
    return build


@dataclass(frozen=True)
class ForEachResult:
    """What a ``@for_each_element`` body produces for each element.

    ``main`` values are stored per element as attributes on the input
    geometry. Each ``generated`` group starts with a geometry, followed by
    attributes for it; every element's generated geometry is joined.
    """

    main: Mapping[str, Any] = field(default_factory=dict)
    generated: Sequence[Mapping[str, Any]] = ()


class ForEachOutputs:
    """Outputs of a For Each Element zone, split like ``ForEachResult``."""

    __slots__ = ("main", "generated")

    def __init__(self, main: ItemOutputs, generated: ItemOutputs) -> None:
        self.main = main
        self.generated = generated

    def __repr__(self) -> str:
        return f"ForEachOutputs(main={self.main!r}, generated={self.generated!r})"


_FOR_EACH_SPECIAL = {"index": "Index", "element": "Element"}


def for_each_element(
    builder: Callable[..., Any] | None = None, *, domain: str = "POINT"
) -> Any:
    """Build a For Each Geometry Element zone.

    Body parameters named ``index`` and ``element`` receive the element's index
    and geometry; other parameters are per-element inputs, given as fields when
    calling. The body returns a ``ForEachResult`` (or a mapping of main values)::

        @for_each_element(domain="POINT")
        def scatter(index: int, radius: float):
            ball = uv_sphere(radius=radius).mesh
            return ForEachResult(main={"scale": radius * 2.0},
                                 generated=[{"geometry": ball, "id": index}])

        out = scatter(points, selection=selected, radius=radius_field)
        out.main.geometry, out.main.scale, out.generated.geometry
    """

    def decorate(builder: Callable[..., Any]) -> Callable[..., ForEachOutputs]:
        signature = inspect.signature(builder)
        item_parameters = [
            parameter
            for parameter in signature.parameters.values()
            if parameter.name not in _FOR_EACH_SPECIAL
        ]
        item_signature = signature.replace(parameters=item_parameters)

        @functools.wraps(builder)
        def build(
            geometry: Any, *args: Any, selection: Any = True, **kwargs: Any
        ) -> ForEachOutputs:
            context = _active_context(builder)
            bound = item_signature.bind(*args, **kwargs)
            bound.apply_defaults()

            zone_input, zone_output = _new_zone(
                context,
                "GeometryNodeForeachGeometryElementInput",
                "GeometryNodeForeachGeometryElementOutput",
                "input_items",
                "main_items",
                "generation_items",
            )
            zone_output.domain = domain

            before = socket_identifiers(zone_input.inputs)
            for parameter, socket_type in zip(
                item_parameters,
                _parameter_item_types(builder, item_parameters, bound.arguments),
                strict=True,
            ):
                zone_output.input_items.new(socket_type, parameter.name)
            fixed_inputs = data_sockets(zone_input.inputs)
            context.set_input(fixed_inputs[0], geometry)
            context.set_input(fixed_inputs[1], selection)
            body_sockets = new_sockets(zone_input.outputs, {"Index", "Element"})
            for parameter, socket in zip(
                item_parameters, new_sockets(zone_input.inputs, before), strict=True
            ):
                context.set_input(socket, bound.arguments[parameter.name])

            body_arguments = {
                parameter.name: context.wrap(socket)
                for parameter, socket in zip(item_parameters, body_sockets, strict=True)
            }
            for name, socket_name in _FOR_EACH_SPECIAL.items():
                if name in signature.parameters:
                    body_arguments[name] = context.wrap(zone_input.outputs[socket_name])

            result = builder(**body_arguments)
            if not isinstance(result, ForEachResult):
                result = ForEachResult(main=result if result is not None else {})

            main = _add_result_items(
                context, zone_output, "main_items", list(result.main.items())
            )
            generated_values: list[tuple[str, Any]] = []
            for group in result.generated:
                group_items = list(group.items())
                if not group_items or not _is_geometry(group_items[0][1]):
                    raise TypeError(
                        f"Each generated group of {builder.__name__!r} must start "
                        "with a geometry."
                    )
                generated_values.extend(group_items)
            generated = _add_result_items(
                context, zone_output, "generation_items", generated_values
            )

            main_geometry = context.wrap(zone_output.outputs["Geometry"])
            return ForEachOutputs(
                ItemOutputs({"geometry": main_geometry, **main}),
                ItemOutputs(generated),
            )

        build.builder = builder  # type: ignore[attr-defined]
        return build

    if builder is not None:
        return decorate(builder)
    return decorate


def _is_geometry(value: Any) -> bool:
    return isinstance(value, Socket) and socket_item_type(value) == "GEOMETRY"


def _add_result_items(
    context: BuildContext,
    zone_output: bpy.types.Node,
    identifier: str,
    values: list[tuple[str, Any]],
) -> dict[str, Socket[Any]]:
    """Add one item per value, link it, and return its outputs by unique name."""
    inputs_before = socket_identifiers(zone_output.inputs)
    outputs_before = socket_identifiers(zone_output.outputs)
    items = getattr(zone_output, identifier)
    for name, value in values:
        items.new(_value_item_type(value, name), name)
    for (_, value), socket in zip(
        values, new_sockets(zone_output.inputs, inputs_before), strict=True
    ):
        context.set_input(socket, value)

    used: set[str] = set()
    return {
        unique_name(name, used): context.wrap(socket)
        for (name, _), socket in zip(
            values, new_sockets(zone_output.outputs, outputs_before), strict=True
        )
    }
