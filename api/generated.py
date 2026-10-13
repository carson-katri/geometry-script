"""Generate the node modules when running from a source checkout.

Built packages ship api/nodes.py, api/shader_nodes.py and api/compositor_nodes.py
for their Blender series. A checkout doesn't track them, so they are generated
with the running Blender the first time the add-on loads, and again when it is
loaded by a different Blender series.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import bpy

API = Path(__file__).resolve().parent
ROOT = API.parent
GENERATOR = ROOT / "code_generator" / "node_functions_generator.py"
MODULES = ("nodes.py", "shader_nodes.py", "compositor_nodes.py")


def _generated_series(module: Path) -> tuple[int, int] | None:
    try:
        text = module.read_text(encoding="utf-8")
    except OSError:
        return None
    match = re.search(r"^BLENDER_VERSION = \((\d+), (\d+),", text, re.MULTILINE)
    return (int(match[1]), int(match[2])) if match else None


def ensure_node_modules() -> None:
    series = tuple(bpy.app.version[:2])
    if all(_generated_series(API / name) == series for name in MODULES):
        return
    if not GENERATOR.is_file():
        raise ImportError(
            f"Geometry Script's node modules are missing or not for Blender "
            f"{series[0]}.{series[1]}. Install the package built for this Blender version."
        )
    # Add-ons load while bpy.data is restricted, and the generator needs to create
    # node trees, so it runs in a background Blender instead.
    print(f"Geometry Script: generating node modules for Blender {bpy.app.version_string}")
    result = subprocess.run(
        [
            bpy.app.binary_path, "-b", "--factory-startup", "--python-exit-code", "1",
            "--python", str(GENERATOR),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise ImportError(
            "Could not generate Geometry Script's node modules:\n"
            + (result.stderr or result.stdout)[-2000:]
        )
