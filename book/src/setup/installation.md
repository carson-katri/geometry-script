# Installation

Geometry Script is a Blender extension and requires **Blender 5.2** or newer.

Each build of the extension is generated for one Blender version, so its node functions match the nodes in that version exactly. Download the build that matches the version of Blender you use.

## From GitHub
1. Download the ZIP matching your Blender version from the [`nightly` release](https://github.com/carson-katri/geometry-script/releases/tag/nightly), e.g. `geometry_script-1.0.0-blender-5.2.zip`
2. Open *Blender* > *Preferences* > *Get Extensions*
3. Open the dropdown at the top right, choose *Install from Disk...* and select the downloaded ZIP file

## From Blender Market
1. After [purchasing the add-on](https://www.blendermarket.com/), download the ZIP file
2. Open *Blender* > *Preferences* > *Get Extensions*
3. Open the dropdown at the top right, choose *Install from Disk...* and select the downloaded ZIP file

## Building it yourself
To build the extension for a Blender version that has no published ZIP, clone the repository and run:

```sh
python tools/build.py --blender /path/to/blender
```

This regenerates the node functions with that Blender, runs a smoke test, and writes `dist/geometry_script-<version>-blender-<major>.<minor>.zip`.
