"""Print the Blender builds to test against as a GitHub Actions matrix.

    python tools/blender_versions.py

Every Linux x64 series on builder.blender.org at or above the manifest's
``blender_version_min`` is included. Released series use the newest official
release from download.blender.org; alpha and beta series use the daily build
and are marked ``experimental``.
"""

from __future__ import annotations

import json
import re
import tomllib
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DAILY_URL = "https://builder.blender.org/download/daily/?format=json&v=1"
RELEASE_URL = "https://download.blender.org/release/Blender{series}/"


def fetch(url: str) -> str:
    # download.blender.org rejects urllib's default User-Agent.
    request = urllib.request.Request(url, headers={"User-Agent": "geometry-script-ci"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode()


def parse_version(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def latest_release(series: str) -> str | None:
    try:
        listing = fetch(RELEASE_URL.format(series=series))
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise
    pattern = rf'blender-({re.escape(series)}\.\d+)-linux-x64\.tar\.xz"'
    versions = re.findall(pattern, listing)
    return max(versions, key=parse_version) if versions else None


def matrix() -> list[dict[str, object]]:
    manifest = tomllib.loads((ROOT / "blender_manifest.toml").read_text(encoding="utf-8"))
    minimum = parse_version(manifest["blender_version_min"])[:2]

    builds = {}
    for build in json.loads(fetch(DAILY_URL)):
        if (build["platform"], build["architecture"], build["file_extension"]) != ("linux", "x86_64", "xz"):
            continue
        series = ".".join(build["version"].split(".")[:2])
        if parse_version(series) >= minimum:
            builds[series] = build

    entries = []
    for series, build in sorted(builds.items(), key=lambda item: parse_version(item[0])):
        release = latest_release(series) if build["risk_id"] in ("stable", "candidate") else None
        if release is not None:
            url = f"{RELEASE_URL.format(series=series)}blender-{release}-linux-x64.tar.xz"
            entries.append({"series": series, "version": release, "url": url, "experimental": False})
        else:
            version = f"{build['version']}-{build['risk_id']}"
            entries.append({"series": series, "version": version, "url": build["url"], "experimental": True})
    return entries


if __name__ == "__main__":
    print(json.dumps(matrix()))
