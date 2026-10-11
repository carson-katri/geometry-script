"""Build the extension package for one Blender version.

    python tools/build.py --blender /path/to/blender [--output-dir dist]

The tracked sources are staged in a temporary directory, the node modules
(api/nodes.py, api/shader_nodes.py, api/compositor_nodes.py) are regenerated
with the given Blender, the manifest is limited to that Blender
series, the smoke test runs against the staged copy, and Blender's extension
builder writes ``geometry_script-<version>-blender-<major>.<minor>.zip``.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def blender_version(blender: str) -> tuple[int, int, int]:
    output = subprocess.run(
        [blender, "--factory-startup", "--version"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    match = re.search(r"^Blender (\d+)\.(\d+)\.(\d+)", output, re.MULTILINE)
    if match is None:
        raise SystemExit(f"Could not read the Blender version from:\n{output}")
    major, minor, patch = (int(part) for part in match.groups())
    return major, minor, patch


def stage_sources(staging: Path) -> None:
    files = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.split("\0")
    for name in filter(None, files):
        source = ROOT / name
        if not source.is_file():
            # Tracked but deleted in the working tree.
            continue
        target = staging / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def limit_manifest(manifest: Path, major: int, minor: int) -> str:
    text = manifest.read_text(encoding="utf-8")
    minimum = f'blender_version_min = "{major}.{minor}.0"'
    maximum = f'blender_version_max = "{major}.{minor + 1}.0"'
    text, count = re.subn(r"^blender_version_min\s*=.*$", minimum, text, flags=re.MULTILINE)
    if count != 1:
        raise SystemExit("blender_manifest.toml must set blender_version_min once")
    text = re.sub(r"^blender_version_max\s*=.*\n", "", text, flags=re.MULTILINE)
    text = text.replace(minimum, f"{minimum}\n{maximum}")
    manifest.write_text(text, encoding="utf-8")
    return re.search(r'^version\s*=\s*"([^"]+)"', text, re.MULTILINE).group(1)


def run_blender(blender: str, *args: str, cwd: Path) -> None:
    subprocess.run(
        [blender, "-b", "--factory-startup", "--python-exit-code", "1", *args],
        cwd=cwd,
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--blender", default="blender", help="Blender executable")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    parser.add_argument("--skip-tests", action="store_true")
    args = parser.parse_args()

    major, minor, patch = blender_version(args.blender)
    print(f"Building for Blender {major}.{minor}.{patch}")

    with tempfile.TemporaryDirectory() as temp:
        staging = Path(temp) / "geometry_script"
        stage_sources(staging)

        run_blender(
            args.blender,
            "--python", "code_generator/node_functions_generator.py",
            cwd=staging,
        )
        version = limit_manifest(staging / "blender_manifest.toml", major, minor)

        if not args.skip_tests:
            run_blender(args.blender, "--python", "tests/smoke_test.py", cwd=staging)

        args.output_dir.mkdir(parents=True, exist_ok=True)
        output = args.output_dir.resolve() / f"geometry_script-{version}-blender-{major}.{minor}.zip"
        subprocess.run(
            [
                args.blender, "--factory-startup", "--command", "extension", "build",
                "--source-dir", str(staging),
                "--output-filepath", str(output),
            ],
            check=True,
        )
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
