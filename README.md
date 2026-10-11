![Geometry Script wordmark](book/src/images/wordmark.png)

A scripting API for Blender's Geometry Nodes:

<table>
<tbody>
<tr>

<td>

```python
from geometry_script import *

@tree("Repeat Grid")
def repeat_grid(geometry: Geometry, width: int = 3, height: int = 3):
    mesh = grid(
        size_x=width, size_y=height,
        vertices_x=width, vertices_y=height,
    ).mesh
    points = mesh_to_points(mesh=mesh).points
    return instance_on_points(points=points, instance=geometry).instances
```

</td>
<td>

![Generated node tree](book/src/images/example_generated_tree.png)

</td>
</tr>
</tbody>
</table>

## Installation
Geometry Script is a Blender extension and requires Blender 5.2 or newer.

1. Download the ZIP matching your Blender version from the [`nightly` release](https://github.com/carson-katri/geometry-script/releases/tag/nightly), e.g. `geometry_script-1.0.0-blender-5.2.zip`
2. Open *Blender* > *Preferences* > *Get Extensions*
3. Open the dropdown at the top right, choose *Install from Disk...* and select the downloaded ZIP file

## What is Geometry Script?
*Geometry Script* is a robust yet easy to use Python API for creating Geometry Nodes with code.

At a certain point, Geometry Node trees become unmanagably large. Creating node trees in Python enables quicker editing and reorganization of large, complex trees.

*Geometry Script* has all of the performance and capabilities of Geometry Nodes, but in a more managable format. The scripts are converted directly to Geometry Node trees making them easy to tweak for others unfamiliar with scripting.

Every node in your Blender version is available as a typed Python function, generated from Blender itself, so your editor can complete node names, inputs, outputs and enum values.

## [Documentation](https://carson-katri.github.io/geometry-script/)
Read the documentation for more information on installation, syntax, and tutorials.

## Contributing
Use [`uv`](https://docs.astral.sh/uv/) to get `fake-bpy-module` and some pyright settings.

```sh
uv sync
```

To build an installable package for a specific Blender version, which regenerates `api/nodes.py` with that Blender and runs the smoke test:

```sh
python tools/build.py --blender /path/to/blender  # writes dist/geometry_script-<version>-blender-<major>.<minor>.zip
```

Then you can [follow Blender's steps](https://developer.blender.org/docs/handbook/extensions/addon_dev_setup/#setting-up-project) to setup a symlink for a local repository.