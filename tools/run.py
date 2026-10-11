"""Run a Geometry Script file in background Blender and print agent.run's short report.

    python3 tools/run.py script.py [--object NAME] [--tree NAME] [--traceback]
                         [--blend FILE] [--blender PATH]

Loads Geometry Script from this checkout, so it needs no installed add-on.
Exits 1 if the script failed. Blender's own startup output is left out.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEGIN, END = "<<<geometry-script-report>>>", "<<<end-geometry-script-report>>>"

BOOTSTRAP = """
import importlib.util, json, sys
root, script, options = {root!r}, {script!r}, json.loads({options!r})
spec = importlib.util.spec_from_file_location(
    "geometry_script", root + "/__init__.py", submodule_search_locations=[root]
)
module = importlib.util.module_from_spec(spec)
sys.modules["geometry_script"] = module
spec.loader.exec_module(module)
print({begin!r})
ok = module.agent.run(script, **options)["ok"]
print({end!r})
sys.exit(0 if ok else 1)
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").strip().splitlines()[0])
    parser.add_argument("script", type=Path)
    parser.add_argument("--object", help="Object to attach the tree to and evaluate")
    parser.add_argument("--tree", help="Tree to attach to --object (default: last built)")
    parser.add_argument("--traceback", action="store_true", help="Print full tracebacks")
    parser.add_argument("--blend", type=Path, help="Open this .blend file first")
    parser.add_argument("--blender", default="blender", help="Blender executable")
    args = parser.parse_args()

    options = {"traceback": args.traceback}
    if args.object:
        options["object"] = args.object
    if args.tree:
        options["tree"] = args.tree
    code = BOOTSTRAP.format(
        root=str(ROOT),
        script=str(args.script.resolve()),
        options=json.dumps(options),
        begin=BEGIN,
        end=END,
    )
    command = [args.blender, "-b", "--factory-startup"]
    if args.blend:
        command.append(str(args.blend))
    command += ["--python-exit-code", "1", "--python-expr", code]
    result = subprocess.run(command, capture_output=True, text=True)

    output = result.stdout
    if BEGIN in output:
        report = output.split(BEGIN, 1)[1].split(END, 1)[0].strip("\n")
        print(report)
    else:
        # Geometry Script itself failed to load; show what Blender said.
        print((result.stdout + result.stderr).strip()[-3000:])
    return 0 if result.returncode == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
