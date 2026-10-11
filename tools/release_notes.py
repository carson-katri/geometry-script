"""Print the release notes for a build with a drag and drop link per Blender series.

    python tools/release_notes.py dist/index.json --base-url https://github.com/<repo>/releases/download/<tag>/

``index.json`` is the extension repository listing written by Blender's
``extension server-generate`` next to the ZIP files. Dropping one of the links
into Blender offers to add that repository and install the matching build.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
from pathlib import Path


def drop_url(base_url: str, package: dict[str, str]) -> str:
    query = {"repository": "./index.json", "blender_version_min": package["blender_version_min"]}
    if "blender_version_max" in package:
        query["blender_version_max"] = package["blender_version_max"]
    archive = package["archive_url"].removeprefix("./")
    return f"{base_url.rstrip('/')}/{archive}?{urllib.parse.urlencode(query, safe='/')}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("index", type=Path, help="Repository listing (index.json)")
    parser.add_argument("--base-url", required=True, help="URL the ZIP files and index.json are served from")
    parser.add_argument("--commit", default="", help="Commit the packages were built from")
    args = parser.parse_args()

    packages = json.loads(args.index.read_text(encoding="utf-8"))["data"]
    packages.sort(key=lambda package: tuple(int(part) for part in package["blender_version_min"].split(".")))

    lines = []
    if args.commit:
        lines += [f"Built from {args.commit}.", ""]
    lines += [
        "Drag the link for your Blender version into Blender to install it:",
        "",
    ]
    for package in packages:
        series = ".".join(package["blender_version_min"].split(".")[:2])
        lines.append(f"- [Geometry Script for Blender {series}]({drop_url(args.base_url, package)})")
    lines += [
        "",
        "Or download the ZIP matching your Blender version and install it from "
        "Preferences > Get Extensions > Install from Disk.",
    ]
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
