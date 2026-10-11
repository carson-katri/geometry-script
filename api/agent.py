"""Short, plain-text reports for agents driving Geometry Script.

Everything here prints a few lines instead of tracebacks or screenshots:

    from geometry_script import agent
    agent.run("/path/to/script.py", object="Scatter")  # build, attach, evaluate
    agent.describe("set_position")                     # a node's signature
    agent.search("points on faces")                    # find a node
    agent.describe_tree("Scatter")                     # read an existing tree back
"""

from __future__ import annotations

import linecache
import os
import re
import time
import traceback as traceback_module
from collections.abc import Iterable
from typing import Any

import bpy

from . import tree as tree_module
from .describe import describe, node_for_bl_idname, search

__all__ = ["describe", "describe_tree", "run", "search", "status"]

# The latest run's source, report, success and time, for status().
_last_run: dict[str, Any] | None = None


def run(
    source: str,
    *,
    filename: str | None = None,
    echo: bool = True,
    object: str | bpy.types.Object | None = None,
    tree: str | None = None,
    traceback: bool = False,
) -> dict[str, Any]:
    """Run a Geometry Script file or code string and print a short report.

    Reports each tree built, then the evaluated geometry and node warnings of
    every object using one of them. ``object`` names an object to evaluate,
    created if needed, that gets a modifier for ``tree`` (default: the last
    tree built). Errors print as one line plus the failing line of the script;
    pass ``traceback=True`` for the full traceback. ``filename`` names a code
    string in reports.

    Prints the report unless ``echo=False``, and returns ``{"ok": bool,
    "report": str}``, so ``result = agent.run(..., echo=False)`` hands it to an
    MCP tool that returns ``result`` instead of printed output.
    """
    is_path = "\n" not in source and (source.endswith(".py") or os.path.isfile(source))
    if is_path:
        filename = os.path.abspath(os.path.expanduser(source))
        with open(filename, encoding="utf-8") as file:
            code = file.read()
    else:
        filename, code = filename or "<geometry script>", source
        linecache.cache[filename] = (len(code), None, code.splitlines(True), filename)

    tree_module.built_tree_names.clear()
    namespace = {"__name__": "__main__", "__file__": filename}
    lines: list[str] = []
    ok = True
    try:
        exec(compile(code, filename, "exec"), namespace)
    except Exception as error:
        ok = False
        lines.append(_error_report(error, filename, traceback))

    built = list(dict.fromkeys(tree_module.built_tree_names))
    for name in built:
        node_tree = bpy.data.node_groups.get(name)
        if node_tree is not None:
            lines.append(f"built {_tree_summary(node_tree)}")
    if not built and ok:
        lines.append("no trees built")

    objects: list[bpy.types.Object] = []
    if object is not None and ok:
        target_name = tree or (built[-1] if built else None)
        if target_name is None:
            lines.append("no tree to attach: pass tree= or build one")
        else:
            objects.append(_attach(object, target_name))
    for name in built:
        objects.extend(
            candidate for candidate in _objects_using(name) if candidate not in objects
        )
    if objects:
        depsgraph = bpy.context.evaluated_depsgraph_get()
        depsgraph.update()
        for candidate in objects[:5]:
            lines.append(_object_report(candidate, depsgraph))
        if len(objects) > 5:
            lines.append(f"... and {len(objects) - 5} more objects")

    report = "\n".join(lines)
    global _last_run
    _last_run = {"source": filename, "report": report, "ok": ok, "time": time.time()}
    if echo:
        print(report)
    return {"ok": ok, "report": report}


def status() -> None:
    """Print the report of the latest run, including live-edit reruns."""
    if _last_run is None:
        print("nothing run yet")
        return
    seconds = time.time() - _last_run["time"]
    print(f"last run: {_last_run['source']} ({seconds:.0f}s ago)\n{_last_run['report']}")


def _error_report(error: BaseException, filename: str, full: bool) -> str:
    message = f"ERROR {type(error).__name__}: {error}"
    if full:
        return message + "\n" + "".join(traceback_module.format_exception(error))
    frames = [
        frame for frame in traceback_module.extract_tb(error.__traceback__)
        if frame.filename == filename
    ]
    if frames:
        frame = frames[-1]
        where = f" in {frame.name}" if frame.name != "<module>" else ""
        message += f"\n  at line {frame.lineno}{where}: {(frame.line or '').strip()}"
    return message


def _socket_summary(item: Any) -> str:
    socket_type = item.bl_socket_idname.removeprefix("NodeSocket")
    text = f"{item.name}: {socket_type}"
    structure = getattr(item, "structure_type", "AUTO")
    if structure not in {"AUTO", "SINGLE", "DYNAMIC"}:
        text += f" {structure.lower()}"
    default = getattr(item, "default_value", None)
    if item.in_out == "INPUT" and isinstance(default, (int, float, bool, str)):
        text += f" = {_short(default)}"
    return text


def _tree_summary(node_tree: bpy.types.NodeTree) -> str:
    sockets = [item for item in node_tree.interface.items_tree if item.item_type == "SOCKET"]
    inputs = ", ".join(_socket_summary(s) for s in sockets if s.in_out == "INPUT")
    outputs = ", ".join(_socket_summary(s) for s in sockets if s.in_out == "OUTPUT")
    return f"{node_tree.name!r}: {len(node_tree.nodes)} nodes; in ({inputs}) -> out ({outputs})"


def _objects_using(tree_name: str) -> Iterable[bpy.types.Object]:
    for candidate in bpy.data.objects:
        for modifier in candidate.modifiers:
            if modifier.type == "NODES" and modifier.node_group and modifier.node_group.name == tree_name:
                yield candidate
                break


def _attach(target: str | bpy.types.Object, tree_name: str) -> bpy.types.Object:
    """Give ``target`` a modifier using ``tree_name``, creating the object if needed."""
    if isinstance(target, str):
        found = bpy.data.objects.get(target)
        if found is None:
            found = bpy.data.objects.new(target, bpy.data.meshes.new(target))
            bpy.context.scene.collection.objects.link(found)
        target = found
    node_tree = bpy.data.node_groups[tree_name]
    modifier = next(
        (m for m in target.modifiers if m.type == "NODES" and m.node_group == node_tree),
        None,
    ) or next((m for m in target.modifiers if m.type == "NODES" and m.node_group is None), None)
    if modifier is None:
        modifier = target.modifiers.new(tree_name, "NODES")
    modifier.node_group = node_tree
    return target


def _object_report(target: bpy.types.Object, depsgraph: Any) -> str:
    evaluated = target.evaluated_get(depsgraph)
    parts = []
    instance_positions: list[tuple[float, ...]] = []
    try:
        geometry = evaluated.evaluated_geometry()
    except (AttributeError, RuntimeError):
        geometry = None
    if geometry is not None:
        mesh = geometry.mesh
        if mesh is not None and len(mesh.vertices):
            parts.append(
                f"mesh {len(mesh.vertices)}v {len(mesh.edges)}e {len(mesh.polygons)}f"
            )
        if geometry.pointcloud is not None:
            parts.append(f"points {len(geometry.pointcloud.points)}")
        if geometry.curves is not None:
            curves = geometry.curves
            parts.append(f"curves {len(curves.curves)} ({len(curves.points)} points)")
        instance_positions = _instance_positions(target, depsgraph)
        if instance_positions:
            parts.append(f"instances {len(instance_positions)}")
        if geometry.volume is not None:
            parts.append(f"volume {len(geometry.volume.grids)} grids")
        if geometry.grease_pencil is not None:
            parts.append(f"grease pencil {len(geometry.grease_pencil.layers)} layers")
    if parts:
        corners = [tuple(corner) for corner in evaluated.bound_box]
        low = tuple(min(c[i] for c in corners) for i in range(3))
        high = tuple(max(c[i] for c in corners) for i in range(3))
        if low != high:
            parts.append(f"bounds {_short(low)}..{_short(high)}")
        elif instance_positions:
            # Instances alone give no bounding box; report where they are.
            low = tuple(min(p[i] for p in instance_positions) for i in range(3))
            high = tuple(max(p[i] for p in instance_positions) for i in range(3))
            parts.append(f"instance positions {_short(low)}..{_short(high)}")
    report = f"object {target.name!r}: " + ("; ".join(parts) or "empty geometry")
    warnings = []
    for modifier in target.modifiers:
        for warning in getattr(modifier, "node_warnings", ()):
            text = f"  {warning.type} ({modifier.name}): {warning.message}"
            if text not in warnings:
                warnings.append(text)
    return "\n".join([report, *warnings])


def _instance_positions(target: bpy.types.Object, depsgraph: Any) -> list[tuple[float, ...]]:
    """World positions of the instances ``target``'s geometry creates."""
    positions = []
    for instance in depsgraph.object_instances:
        if instance.is_instance and instance.parent and instance.parent.original == target:
            positions.append(tuple(instance.matrix_world.translation))
    return positions


def _short(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:.4g}"
    if isinstance(value, (tuple, list)) or hasattr(value, "__len__") and not isinstance(value, str):
        try:
            return "(" + ", ".join(_short(item) for item in value) + ")"
        except TypeError:
            pass
    return repr(value)


def describe_tree(name: str) -> None:
    """Print a node tree as Geometry Script-like calls, leaving out default values."""
    node_tree = bpy.data.node_groups.get(name)
    if node_tree is None:
        print(f"No node tree {name!r}.")
        return
    print(_describe_tree_text(node_tree))


def _python_name(text: str) -> str:
    return re.sub(r"\W+", "_", text.strip().lower()).strip("_") or "value"


def _describe_tree_text(node_tree: bpy.types.NodeTree) -> str:
    lines = [f"# {_tree_summary(node_tree)}"]
    variables: dict[str, str] = {}
    counts: dict[str, int] = {}
    defaults_tree = bpy.data.node_groups.new("__describe_defaults__", node_tree.bl_idname)
    defaults: dict[str, bpy.types.Node] = {}
    try:
        for node in _ordered_nodes(node_tree):
            if node.bl_idname == "NodeGroupInput":
                continue
            if node.bl_idname == "NodeGroupOutput":
                lines.append("return " + _group_output_text(node, variables))
                continue
            info = node_for_bl_idname(node.bl_idname)
            function = info.function_name if info else (
                node.node_tree.name if node.bl_idname == "GeometryNodeGroup" and node.node_tree
                else node.bl_idname
            )
            if node.bl_idname not in defaults:
                try:
                    defaults[node.bl_idname] = defaults_tree.nodes.new(node.bl_idname)
                except RuntimeError:
                    defaults[node.bl_idname] = None  # type: ignore[assignment]
            reference = defaults[node.bl_idname]
            arguments = []
            for prop in node.bl_rna.properties:
                if prop.is_readonly or prop.identifier in _SKIPPED_PROPERTIES:
                    continue
                if prop.type not in {"ENUM", "BOOLEAN", "INT", "FLOAT"} or getattr(prop, "is_array", False):
                    continue
                value = getattr(node, prop.identifier)
                if reference is not None and value == getattr(reference, prop.identifier):
                    continue
                arguments.append(f"{prop.identifier}={value!r}")
            for index, socket in enumerate(node.inputs):
                if not socket.enabled or socket.bl_idname == "NodeSocketVirtual":
                    continue
                argument = (
                    info.input_names.get(socket.identifier) or info.input_names.get(socket.name)
                    if info else None
                ) or _python_name(socket.name)
                sources = [_source_text(link, variables) for link in socket.links if link.is_valid]
                if sources:
                    arguments.append(
                        f"{argument}={sources[0] if len(sources) == 1 else '[' + ', '.join(sources) + ']'}"
                    )
                    continue
                if not hasattr(socket, "default_value") or socket.hide_value:
                    continue
                value = socket.default_value
                default = None
                if reference is not None and index < len(reference.inputs):
                    default = getattr(reference.inputs[index], "default_value", None)
                if default is not None and _short(value) == _short(default):
                    continue
                arguments.append(f"{argument}={_short(value)}")
            stem = _python_name(function)
            counts[stem] = counts.get(stem, 0) + 1
            variable = f"{stem}_{counts[stem]}"
            variables[node.name] = variable
            lines.append(f"{variable} = {function}({', '.join(arguments)})")
    finally:
        bpy.data.node_groups.remove(defaults_tree)
    return "\n".join(lines)


_SKIPPED_PROPERTIES = {
    "name", "label", "location", "width", "height", "select", "show_options",
    "show_preview", "hide", "mute", "show_texture", "use_custom_color", "color",
    "bl_idname", "bl_label", "bl_description", "bl_icon", "bl_static_type",
    "bl_width_default", "bl_width_min", "bl_width_max", "bl_height_default",
    "bl_height_min", "bl_height_max", "location_absolute", "warning_propagation",
    "color_tag",
}


def _source_text(link: Any, variables: dict[str, str]) -> str:
    source_node, socket = link.from_node, link.from_socket
    while source_node.bl_idname == "NodeReroute":
        if not source_node.inputs[0].links:
            return "unlinked"
        upstream = source_node.inputs[0].links[0]
        source_node, socket = upstream.from_node, upstream.from_socket
    variable = variables.get(source_node.name, _python_name(source_node.name))
    if source_node.bl_idname == "NodeGroupInput":
        return _python_name(socket.name)
    info = node_for_bl_idname(source_node.bl_idname)
    output = (
        info.output_names.get(socket.identifier) or info.output_names.get(socket.name)
        if info else None
    ) or _python_name(socket.name)
    return f"{variable}.{output}"


def _group_output_text(node: bpy.types.Node, variables: dict[str, str]) -> str:
    parts = []
    for socket in node.inputs:
        if socket.bl_idname == "NodeSocketVirtual":
            continue
        sources = [_source_text(link, variables) for link in socket.links if link.is_valid]
        parts.append(f"{socket.name!r}: {sources[0] if sources else 'None'}")
    return "{" + ", ".join(parts) + "}"


def _ordered_nodes(node_tree: bpy.types.NodeTree) -> list[bpy.types.Node]:
    """Nodes with every node after the nodes it reads from; frames and reroutes left out."""
    ordered: list[bpy.types.Node] = []
    seen: set[str] = set()

    def visit(node: bpy.types.Node) -> None:
        if node.name in seen:
            return
        seen.add(node.name)
        for socket in node.inputs:
            for link in socket.links:
                visit(link.from_node)
        # Zone outputs come after their inputs' bodies; pair them explicitly.
        paired = getattr(node, "paired_output", None)
        if paired is not None:
            ordered.append(node)
            visit(paired)
            return
        ordered.append(node)

    for node in sorted(node_tree.nodes, key=lambda n: n.bl_idname == "NodeGroupOutput"):
        if node.bl_idname not in {"NodeFrame", "NodeReroute"}:
            visit(node)
    return [node for node in ordered if node.bl_idname not in {"NodeFrame", "NodeReroute"}]
