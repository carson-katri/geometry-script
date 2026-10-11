"""Print compact node function signatures without starting Blender.

    python3 tools/describe.py set_position mesh_to_points
    python3 tools/describe.py --search "points on faces"
"""

import importlib.util
import sys
from pathlib import Path

# Load api/describe.py by path: putting api/ on sys.path would let api/types.py
# hide the standard library's types module.
path = Path(__file__).resolve().parent.parent / "api" / "describe.py"
spec = importlib.util.spec_from_file_location("geometry_script_describe", path)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

raise SystemExit(module.main(sys.argv[1:]))
