"""Build materials and worlds, whose shader trees end in an output node instead of a group."""

from __future__ import annotations

import contextlib
import functools
import inspect
from collections.abc import Callable, Iterator, Mapping
from dataclasses import dataclass
from typing import Any

import bpy

from .runtime import (
    BuildContext,
    MissingOutput,
    activate_build_context,
    reset_build_context,
)
from .tree import built_trees, named_decorator, tree_output_values


@dataclass(frozen=True)
class _OutputKind:
    decorator: str
    collection: str
    output_node: str


_MATERIAL = _OutputKind("@material", "materials", "ShaderNodeOutputMaterial")
_WORLD = _OutputKind("@world", "worlds", "ShaderNodeOutputWorld")


@contextlib.contextmanager
def _rebuild_transaction(name: str, kind: _OutputKind) -> Iterator[Any]:
    """Yield the material or world ``name`` with its nodes cleared.

    It is rebuilt in place, so objects and nodes using it keep it. If the build
    fails, what was there is restored.
    """
    collection = getattr(bpy.data, kind.collection)
    existing = collection.get(name)
    backup = existing.copy() if existing is not None else None
    block = existing if existing is not None else collection.new(name)
    try:
        if block.node_tree is None:
            block.use_nodes = True
        node_tree = block.node_tree
        for node in tuple(node_tree.nodes):
            node_tree.nodes.remove(node)
        yield block
    except BaseException:
        if backup is not None:
            block.user_remap(backup)
            collection.remove(block)
            backup.name = name
        else:
            collection.remove(block)
        raise
    if backup is not None:
        collection.remove(backup)


def _link_outputs(context: BuildContext, kind: _OutputKind, name: str, result: Any) -> None:
    """Link what the builder returned into a new output node.

    A single value is the surface; a mapping (or named tuple) names the output
    inputs, such as ``{"surface": ..., "volume": ...}``. ``None`` adds no output
    node, for builders that add their own.
    """
    if result is None:
        return
    if isinstance(result, Mapping):
        values = [(str(key), value) for key, value in result.items()]
    else:
        values = tree_output_values(result)
        if len(values) == 1:
            values = [("surface", values[0][1])]

    output = context.new_node(kind.output_node)
    output.is_active_output = True
    inputs = {socket.name.lower(): socket for socket in output.inputs if socket.enabled}
    for key, value in values:
        target = inputs.get(key.lower())
        if target is None:
            raise TypeError(
                f"{kind.decorator} {name!r} returned {key!r}; return a shader, or a "
                f"mapping with any of {list(inputs)!r}."
            )
        if isinstance(value, MissingOutput):
            raise value.error()
        context.set_input(target, value)


def _build(builder: Callable[..., Any], name: str, kind: _OutputKind) -> Any:
    if inspect.signature(builder).parameters:
        raise TypeError(
            f"{kind.decorator} functions take no parameters, since a "
            f"{kind.collection[:-1]} has no inputs. Build a @shader group for "
            "reusable inputs and use it here."
        )
    with _rebuild_transaction(name, kind) as block:
        context = BuildContext(block.node_tree)
        token = activate_build_context(context)
        try:
            _link_outputs(context, kind, name, builder())
        finally:
            reset_build_context(token)
        context.validate_links()
    built_trees.append((kind.collection, block.name))
    return block


def _reference(builder: Callable[..., Any], block: Any) -> Callable[[], Any]:
    @functools.wraps(builder)
    def reference() -> Any:
        return block

    reference.node_tree = block.node_tree  # type: ignore[attr-defined]
    reference.builder = builder  # type: ignore[attr-defined]
    return reference


def material(
    name_or_builder: str | Callable[..., Any] | None = None,
) -> Callable[..., Any]:
    """Build or rebuild a material from a decorated function using shader nodes.

    The function takes no parameters and returns the surface shader, or a
    mapping such as ``{"surface": ..., "volume": ..., "displacement": ...}``.
    Calling the decorated function returns the material, e.g. for
    ``set_material(material=gold())`` in a ``@tree``.
    """

    def build(builder: Callable[..., Any], name: str) -> Callable[[], bpy.types.Material]:
        reference = _reference(builder, _build(builder, name, _MATERIAL))
        reference.material = reference()  # type: ignore[attr-defined]
        return reference

    return named_decorator("@material", name_or_builder, build)


def world(
    name_or_builder: str | Callable[..., Any] | None = None,
    *,
    scene: bool | bpy.types.Scene = False,
) -> Callable[..., Any]:
    """Build or rebuild a world from a decorated function using shader nodes.

    The function takes no parameters and returns the surface shader (usually a
    ``background``), or a mapping with ``surface`` and ``volume``. ``scene=True``
    makes it the active scene's world (pass a Scene to choose another).
    Calling the decorated function returns the world.
    """

    def build(builder: Callable[..., Any], name: str) -> Callable[[], bpy.types.World]:
        block = _build(builder, name, _WORLD)
        if scene is not False:
            target = bpy.context.scene if scene is True else scene
            target.world = block
        reference = _reference(builder, block)
        reference.world = block  # type: ignore[attr-defined]
        return reference

    return named_decorator("@world", name_or_builder, build)
