"""Generate typed Python functions for the nodes available in a Blender node tree.

    blender -b --factory-startup --python code_generator/node_functions_generator.py -- --output api/nodes.py
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
        default="GeometryNodeTree",
        help="The node tree type whose nodes are generated",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path of the Python module to write (Blender also prints to stdout)",
    )
    args = parser.parse_args(argv)

    try:
        code = generate_code(args.tree_type)
    except Exception as error:
        print(f"Could not generate node functions: {error}", file=sys.stderr)
        return 1
    with open(args.output, "w", encoding="utf-8", newline="\n") as file:
        file.write(code)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
