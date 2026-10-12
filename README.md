![Geometry Script wordmark](book/src/images/wordmark.png)

A scripting API for Blender's Geometry Nodes, shaders and compositor:

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

Drag the box for your Blender version into Blender to install it:

<p>
<a href="https://github.com/carson-katri/geometry-script/releases/download/nightly/geometry_script-1.0.0-blender-5.2.zip?repository=./index.json&amp;blender_version_min=5.2.0&amp;blender_version_max=5.3.0"><picture><source media="(prefers-color-scheme: dark)" srcset="book/src/images/install/blender-5.2-dark.svg"><img alt="Geometry Script for Blender 5.2" src="book/src/images/install/blender-5.2-light.svg" width="200" height="72"></picture></a>
<a href="https://github.com/carson-katri/geometry-script/releases/download/nightly/geometry_script-1.0.0-blender-5.3.zip?repository=./index.json&amp;blender_version_min=5.3.0&amp;blender_version_max=5.4.0"><picture><source media="(prefers-color-scheme: dark)" srcset="book/src/images/install/blender-5.3-dark.svg"><img alt="Geometry Script for Blender 5.3" src="book/src/images/install/blender-5.3-light.svg" width="200" height="72"></picture></a>
<a href="https://github.com/carson-katri/geometry-script/releases/download/nightly/geometry_script-1.0.0-blender-5.4.zip?repository=./index.json&amp;blender_version_min=5.4.0&amp;blender_version_max=5.5.0"><picture><source media="(prefers-color-scheme: dark)" srcset="book/src/images/install/blender-5.4-dark.svg"><img alt="Geometry Script for Blender 5.4" src="book/src/images/install/blender-5.4-light.svg" width="200" height="72"></picture></a>
</p>

Blender asks to allow online access if it's off, then to add the Geometry Script repository, then confirms the install. The [`nightly` release](https://github.com/carson-katri/geometry-script/releases/tag/nightly) always lists the links for every Blender version with a build.

To install manually instead:

1. Download the ZIP matching your Blender version from the [`nightly` release](https://github.com/carson-katri/geometry-script/releases/tag/nightly), e.g. `geometry_script-1.0.0-blender-5.2.zip`
2. Open *Blender* > *Preferences* > *Get Extensions*
3. Open the dropdown at the top right, choose *Install from Disk...* and select the downloaded ZIP file

### Claude Code skill
The repository is also a [Claude Code](https://claude.com/claude-code) plugin marketplace with a skill for building node trees with Geometry Script. Install it with:

```
/plugin install geometry-script --marketplace carson-katri/geometry-script
```

On Claude Code versions before 2.1.275, add the marketplace first:

```
/plugin marketplace add carson-katri/geometry-script
/plugin install geometry-script@geometry-script
```

The skill runs scripts through Blender's MCP server when it's connected, or in background Blender otherwise. Run `/plugin marketplace update geometry-script` to get the latest version, or turn on auto-update for the marketplace in `/plugin`.

## What is Geometry Script?
*Geometry Script* is a robust yet easy to use Python API for creating Geometry Nodes with code.

At a certain point, Geometry Node trees become unmanagably large. Creating node trees in Python enables quicker editing and reorganization of large, complex trees.

*Geometry Script* has all of the performance and capabilities of Geometry Nodes, but in a more managable format. The scripts are converted directly to Geometry Node trees making them easy to tweak for others unfamiliar with scripting.

Every node in your Blender version is available as a typed Python function, generated from Blender itself, so your editor can complete node names, inputs, outputs and enum values.

Shader node groups, materials, worlds and compositor node groups can be scripted the same way, with `geometry_script.shader` and `geometry_script.compositor`:

```python
from geometry_script.shader import *

@material("Gold")
def gold():
    return principled_bsdf(base_color=(1.0, 0.77, 0.34, 1.0), metallic=1.0, roughness=0.2).bsdf
```

## [Documentation](https://carson-katri.github.io/geometry-script/)
Read the documentation for more information on installation, syntax, and tutorials.

## Contributing
Use [`uv`](https://docs.astral.sh/uv/) to get `fake-bpy-module` and some pyright settings.

```sh
uv sync
```

The node modules (`api/nodes.py`, `api/shader_nodes.py` and `api/compositor_nodes.py`) are generated from Blender and aren't checked in. Loading the add-on from a checkout generates them with that Blender, or you can generate them yourself, e.g. for editor completions:

```sh
blender -b --factory-startup --python code_generator/node_functions_generator.py
```

To build an installable package for a specific Blender version, which generates the node modules with that Blender and runs the smoke test:

```sh
python tools/build.py --blender /path/to/blender  # writes dist/geometry_script-<version>-blender-<major>.<minor>.zip
```

Then you can [follow Blender's steps](https://developer.blender.org/docs/handbook/extensions/addon_dev_setup/#setting-up-project) to setup a symlink for a local repository.