"""Lay out a built node tree in columns that flow left to right.

Blender only measures nodes when it draws them, so builds in background mode
or before the editor opens have no sizes to work with. Heights are estimated
from each node's visible sockets and settings instead.
"""

from __future__ import annotations

from collections import defaultdict
from statistics import mean

import bpy

HEADER_HEIGHT = 30.0
ROW_HEIGHT = 22.0
COLUMN_GAP = 80.0
NODE_GAP = 40.0

# Unlinked inputs that show their value as a column of fields: one row per component.
_EXPANDED_INPUT_ROWS = {"VECTOR": 4, "ROTATION": 4, "MATRIX": 1}


def _visible(sockets: bpy.types.bpy_prop_collection) -> list[bpy.types.NodeSocket]:
    return [socket for socket in sockets if socket.enabled and not socket.hide]


def _input_rows(socket: bpy.types.NodeSocket) -> int:
    if socket.is_linked or socket.hide_value:
        return 1
    return _EXPANDED_INPUT_ROWS.get(socket.type, 1)


def _base_properties(node: bpy.types.Node) -> set[str]:
    return {
        prop.identifier
        for base in type(node).__mro__[1:]
        if hasattr(base, "bl_rna")
        for prop in base.bl_rna.properties
    }


def _setting_rows(node: bpy.types.Node) -> int:
    """Roughly how many rows the node's own settings take above its inputs."""
    inherited = _base_properties(node)
    return sum(
        1
        for prop in node.bl_rna.properties
        if prop.identifier not in inherited
        and not prop.is_readonly
        and prop.type in {"ENUM", "BOOLEAN", "POINTER", "INT", "FLOAT", "STRING"}
    )


class _Measure:
    """Estimated sizes and socket offsets (downward from the node's top) of one node."""

    def __init__(self, node: bpy.types.Node) -> None:
        outputs = _visible(node.outputs)
        inputs = _visible(node.inputs)
        self.width = node.width
        if node.hide:
            self.height = HEADER_HEIGHT
            self.output_offsets = {socket: HEADER_HEIGHT / 2 for socket in outputs}
            self.input_offsets = {socket: HEADER_HEIGHT / 2 for socket in inputs}
            return
        y = HEADER_HEIGHT
        self.output_offsets = {}
        for socket in outputs:
            self.output_offsets[socket] = y + ROW_HEIGHT / 2
            y += ROW_HEIGHT
        y += _setting_rows(node) * ROW_HEIGHT
        self.input_offsets = {}
        for socket in inputs:
            self.input_offsets[socket] = y + ROW_HEIGHT / 2
            y += _input_rows(socket) * ROW_HEIGHT
        self.height = y + ROW_HEIGHT / 2


def _consumers(node_tree: bpy.types.NodeTree) -> dict[bpy.types.Node, list[tuple[bpy.types.Node, bpy.types.NodeLink]]]:
    """Each node's downstream nodes, with the link to each (``None`` for a zone pairing)."""
    consumers = defaultdict(list)
    for link in node_tree.links:
        if link.from_node != link.to_node:
            consumers[link.from_node].append((link.to_node, link))
    for node in node_tree.nodes:
        # Keep a zone's input to the left of its output even when nothing links them.
        paired = getattr(node, "paired_output", None)
        if paired is not None:
            consumers[node].append((paired, None))
    return consumers


def _columns(
    nodes: list[bpy.types.Node], consumers: dict[bpy.types.Node, list]
) -> list[list[bpy.types.Node]]:
    """Group nodes by their longest path to a node nothing reads, rightmost column first."""
    column: dict[bpy.types.Node, int] = {}
    visiting: set[bpy.types.Node] = set()

    def place(start: bpy.types.Node) -> None:
        stack = [(start, False)]
        while stack:
            node, expanded = stack.pop()
            if node in column or (not expanded and node in visiting):
                continue
            downstream = [
                target for target, _ in consumers[node] if target not in visiting
            ]
            if not expanded:
                visiting.add(node)
                stack.append((node, True))
                stack.extend((target, False) for target in downstream if target not in column)
                continue
            visiting.discard(node)
            column[node] = max((column[target] + 1 for target in downstream if target in column), default=0)

    for node in nodes:
        place(node)
    columns: list[list[bpy.types.Node]] = [[] for _ in range(max(column.values(), default=-1) + 1)]
    for node in nodes:
        columns[column[node]].append(node)
    return columns


def arrange(node_tree: bpy.types.NodeTree) -> None:
    """Position the nodes of ``node_tree`` so links flow left to right without overlapping."""
    nodes = [node for node in node_tree.nodes if node.bl_idname != "NodeFrame"]
    if not nodes:
        return
    consumers = _consumers(node_tree)
    measures = {node: _Measure(node) for node in nodes}
    top: dict[bpy.types.Node, float] = {}

    x = 0.0
    for column in _columns(nodes, consumers):
        x -= max(measures[node].width for node in column)

        # Line each node's first linked output up with the inputs it feeds.
        desired = {}
        for node in column:
            targets = [
                top[target] - measures[target].input_offsets.get(link.to_socket, 0.0)
                + measures[node].output_offsets.get(link.from_socket, 0.0)
                for target, link in consumers[node]
                if link is not None and target in top
            ]
            desired[node] = mean(targets) if targets else None

        # Unlinked nodes keep build order, after the linked ones.
        order = sorted(
            range(len(column)),
            key=lambda index: (desired[column[index]] is None, -(desired[column[index]] or 0.0), index),
        )
        y = None
        offsets = []
        for index in order:
            node = column[index]
            wanted = desired[node] if desired[node] is not None else (y if y is not None else 0.0)
            placed = wanted if y is None else min(wanted, y)
            top[node] = placed
            offsets.append(wanted - placed)
            y = placed - measures[node].height - NODE_GAP
        # Pushing nodes down to avoid overlaps moves them off their links; split the difference.
        shift = mean(offsets)
        for node in column:
            top[node] += shift
            node.location = (x, top[node])
        x -= COLUMN_GAP

    # Start the tree at the origin.
    left = min(node.location.x for node in nodes)
    for node in nodes:
        node.location.x -= left
