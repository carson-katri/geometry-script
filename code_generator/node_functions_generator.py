"""Generate typed Python functions for the nodes available in each kind of node tree.

    blender -b --factory-startup --python code_generator/node_functions_generator.py

writes api/nodes.py (Geometry Nodes), api/shader_nodes.py and
api/compositor_nodes.py. Pass ``--tree-type`` and ``--output`` to generate one.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import bpy

# Blender runs this file as a script, so make its package importable.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from code_generator.emit import emit_module
from code_generator.introspect import read_signatures

ROOT = Path(__file__).resolve().parent.parent

# The module generated for each tree type, relative to the add-on root.
MODULES = {
    "GeometryNodeTree": "api/nodes.py",
    "ShaderNodeTree": "api/shader_nodes.py",
    "CompositorNodeTree": "api/compositor_nodes.py",
}


def generate_code(tree_type: str = "GeometryNodeTree") -> str:
    return emit_module(
        read_signatures(tree_type),
        tree_type=tree_type,
        blender_version_string=bpy.app.version_string,
        blender_version=tuple(bpy.app.version),
    )


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv
        if "--" in argv:
            argv = argv[argv.index("--") + 1 :]
        else:
            argv = []

    parser = argparse.ArgumentParser(description="Generate typed node functions")
    parser.add_argument(
        "--tree-type",
        choices=sorted(MODULES),
        help="Generate only this tree type's nodes (default: every tree type)",
    )
    parser.add_argument(
        "--output",
        help="Path of the module to write with --tree-type (default: its module in api/)",
    )
    args = parser.parse_args(argv)
    if args.output and not args.tree_type:
        parser.error("--output needs --tree-type")

    if args.tree_type:
        targets = {args.tree_type: Path(args.output or ROOT / MODULES[args.tree_type])}
    else:
        targets = {tree_type: ROOT / path for tree_type, path in MODULES.items()}
    for tree_type, output in targets.items():
        try:
            code = generate_code(tree_type)
        except Exception as error:
            print(f"Could not generate {tree_type} node functions: {error}", file=sys.stderr)
            return 1
        with open(output, "w", encoding="utf-8", newline="\n") as file:
            file.write(code)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
