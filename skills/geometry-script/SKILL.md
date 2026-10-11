---
name: geometry-script
description: Build and edit Blender node trees in Python with the Geometry Script add-on (`from geometry_script import *`, `@tree`; `geometry_script.shader` for `@shader`/`@material`/`@world`; `geometry_script.compositor` for `@compositor`). Use when asked to create, change, debug or inspect a geometry node tree, shader node group, material, world or compositor node group, procedurally generate geometry in Blender, or when a script uses geometry_script — whether through Blender's official MCP server (execute_blender_code) or headless Blender.
---

# Geometry Script

Geometry Script turns a decorated Python function into a Geometry Nodes group.
Every Blender node is a generated, typed function. The add-on checks your
input names, output names, enum values and link types, and its errors say what
to change. **Guess, run and fix from the error.** That is cheaper than reading
up front.

The repo root is two directories above this file. `tools/` and `api/` paths
below are relative to it.

## The loop

1. Write the script to a `.py` file, not an inline string, so later edits are small diffs.
2. Run it and read the short report. Always go through `agent.run`: raw `exec` of
   the same script returns a traceback about 10x longer.
   - **Blender MCP, running Blender:** `execute_blender_code` with
     `from geometry_script import agent; agent.run("/abs/path/script.py", object="Name")`.
     The report comes back as `stdout`.
   - **Blender MCP, no window:** `execute_blender_code_for_cli` with a `blend_file` and
     `from geometry_script import agent; result = agent.run("/abs/path/script.py", object="Name", echo=False)`.
     This tool returns only `result`, not printed output.
   - **No MCP:** `python3 tools/run.py script.py --object Name`
     (add `--blend file.blend` to start from a file).
3. Fix the single error it prints, then run again.
4. Check the result with the report's geometry stats (vertex/face/point/instance
   counts, bounds) and node warnings. Take a viewport screenshot only when what
   it *looks like* matters.

**Live edit:** if the user has the script open in Blender's Text Editor with
Live Edit and the add-on's auto-resolve on, saving the file reruns it. Then
just edit the file and call `agent.status()`, which prints the latest run's report.

`agent.run` prints a few lines and returns them as `{"ok": bool, "report": str}`: each tree built (nodes, inputs, outputs), then the
evaluated geometry and node warnings for every object using those trees.
`object=` attaches the last tree built, or `tree=` if given, to that object,
creating the object if needed. Errors print as `ERROR Type: message` plus the
failing line of your script. Pass `traceback=True` only when that isn't enough.

## Saving context

| Need | Cheap way | Avoid |
|---|---|---|
| Find a node | `python3 tools/describe.py --search "points on faces"` or `agent.search(...)` | grepping `api/nodes.py` (9k+ lines) |
| A node's sockets | `python3 tools/describe.py set_position mesh_to_points` or `agent.describe(...)` | reading the generated function source |
| Shader / compositor nodes | `tools/describe.py --tree shader ...`, `agent.describe(..., tree="compositor")` | grepping `api/shader_nodes.py` / `api/compositor_nodes.py` |
| Check a build | `agent.run(...)` / `tools/run.py` report, or `agent.status()` after a live-edit save | raw `exec` with full tracebacks; screenshots |
| Understand an existing tree | `agent.describe_tree("Name")` (node group, material or world): prints it as Geometry Script calls, without default values | dumping `node_tree.nodes` / links |
| Know the API | this file | the book in `book/` (longer) |
| See the result | report stats first; then MCP `get_screenshot_of_area_as_image(area_ui_type="VIEW_3D", size_limit_in_bytes=200000)` | `get_screenshot_of_window_as_image` (the whole window) |
| A `bpy` (not node) question | MCP `search_api_docs` / `get_python_api_docs` | guessing, or long `dir()` dumps |

Describe only the nodes you're unsure of, and several in one call. Most names
are the node's UI name in snake_case, and the error will tell you if you're wrong.

## Writing trees

```python
from geometry_script import *

@tree("Scatter Cubes")                       # group name; rebuilt in place if it exists
def scatter_cubes(geometry: Geometry, count: int = 4, size: float = 0.3):
    mesh = grid(size_x=4.0, size_y=4.0, vertices_x=count, vertices_y=count).mesh
    points = mesh_to_points(mesh=mesh).points
    cube_mesh = cube(size=(size, size, size)).mesh     # socket tuples -> Combine XYZ
    lifted = set_position(geometry=points, offset=(0.0, 0.0, size * 2)).geometry
    return instance_on_points(points=lifted, instance=cube_mesh).instances
```

- **Inputs:** parameter annotations and defaults become group inputs: `Geometry`, `float`,
  `int`, `bool`, `str`, `Vector`, `Color`, `Rotation`, `Matrix`, `Menu`, `Object`,
  `Material`, `Collection`, `Image`, plus `Field[T]`, `Grid[T]`, `Vector2`. Return one
  value, a tuple, or a dict `{"Output Name": value}` for named outputs.
- **Node functions take keyword arguments only** and return a namedtuple of outputs:
  `mesh_to_points(mesh=m).points`. Enum settings are strings: `mode="FACES"`.
  Type settings (`data_type`, `input_type`) are inferred from what you link, so
  set them only to override.
- **Arithmetic** (`+ - * / % **`, unary `-`) on float, int and vector sockets
  adds Math / Vector Math nodes. Comparisons (`< <= > >= == !=`) add a
  Compare node and give a boolean socket: `z > 0.5`, `index().index % 2 == 0`.
  Combine them with `boolean_math`, not `and`/`or`/`not` or `0 < x < 1`.
  Fields such as `position().position` and `index().index` are plain sockets.
- **Calling a `@tree` function inside another `@tree`** adds a group node. Those
  take positional arguments: `repeat_grid(geometry)`.
- **Builds are all-or-nothing:** if a build raises, the previous tree (and its
  modifier input values) is left untouched. Modifiers keep their input values
  across rebuilds.
- **Names that would shadow Python builtins get a trailing underscore:** `math_`
  (`math(...)` also works, and `math.pi` is still the math module), `id_`,
  `object_`, `string_`.

### Zones

```python
@repeat_zone
def climb(geometry: Geometry, step: float, iteration: int):   # `iteration` is the index
    return set_position(geometry=geometry, offset=(0.0, 0.0, step)).geometry, step * 2.0

@simulation_zone
def fall(geometry: Geometry, delta_time: float):
    return set_position(geometry=geometry, offset=(0.0, 0.0, -1.0)).geometry

@for_each_element(domain="POINT")
def per_point(index: int, radius: float):
    return ForEachResult(main={"scale": radius * 2.0},
                         generated=[{"geometry": uv_sphere(radius=radius).mesh}])

@closure_zone
def scale(x: float, factor: float = 2.0):
    return x * factor

@tree("Zones")
def zones(geometry: Geometry):
    climbed = climb(geometry, 1.0, iterations=4).geometry
    out = per_point(mesh_to_points(mesh=climbed).points, radius=0.25)
    value = scale.evaluate(scale(), 1.0, 3.0)
    return {"Geometry": fall(out.generated.geometry), "Value": value}
```

### Shaders, materials, worlds and the compositor

Each tree type has its own module of node functions; names like `normal`, `mix`
or `object_info` mean different nodes in each. A node used in the wrong tree
raises an error naming the module it belongs to.

```python
from geometry_script import *            # geometry nodes, @tree / @geometry
from geometry_script import shader as sh # @sh.shader, @sh.material, @sh.world
from geometry_script import compositor as comp

@sh.shader("Stripes")                    # shader node group: works like @tree
def stripes(color: Color = (0.9, 0.3, 0.1, 1.0), scale: float = 6.0):
    wave = sh.wave_texture(scale=scale)
    return sh.mix(data_type="RGBA", factor=wave.factor, a=color, b=(0, 0, 0, 1)).result

@sh.material("Striped")                  # no parameters; return the surface shader,
def striped():                           # or {"surface": ..., "displacement": ...}
    return sh.principled_bsdf(base_color=stripes(scale=10.0)).bsdf

@sh.world("Studio", scene=True)          # scene=True makes it the scene's world
def studio():
    return sh.background(color=(0.05, 0.06, 0.08, 1.0)).background

@comp.compositor("Glow", scene=True)     # scene=True makes it the scene's compositor
def glow(strength: float = 0.3):
    image = comp.render_layers().image
    blurred = comp.blur(image=image, size=(20, 20)).image
    return comp.mix(data_type="RGBA", blend_type="SCREEN", factor=strength, a=image, b=blurred).result

@tree("Striped Cube")                    # calling a @material returns the Material
def striped_cube():
    return set_material(geometry=cube().mesh, material=striped()).geometry
```

`@repeat_zone` and `@closure_zone` also work in shader trees. `agent.run` reports
shader groups, materials and worlds, but `object=` only attaches geometry trees.

### Item nodes

Capture Attribute, Index/Menu Switch, Bundles and Format String take their
items as keyword arguments, `items=[...]` or `items={...}`, and expose them by
name: `capture_attribute(geometry=g, height=position().position).height`.

## Errors and what they mean

| Error | Fix |
|---|---|
| `unexpected keyword argument 'offest'. Did you mean 'offset'?` | Rename it. |
| `...Outputs has no output 'geometry'; available: ['points']` | Use a listed name. |
| `has no 'vector' output with its current settings {'operation': 'DOT_PRODUCT'}; available: ['value']` | That mode outputs something else; use a listed output or change the setting. |
| `Cannot set ...mode to 'VERTEX'. Expected one of [...]. Did you mean 'VERTICES'?` | Use a listed value. |
| `has no 'x' input with its current settings {...}` | That input only exists in another mode or type. |
| `Invalid links ... cannot take ... Set the node's type, one of: ...` | Wrong socket type, or set `data_type=`/`input_type=`. |
| `takes 0 positional arguments` | Node functions are keyword-only. |
| `NameError: name 'foo' is not defined` | Wrong node name: run `tools/describe.py --search foo`. |

Watch out: Blender silently converts some types (float → vector, bool → float),
so a link of the wrong kind can still build. Check the result stats.

## Blender 5.x scene snippets

- Attach by hand: `mod = obj.modifiers.new("GS", "NODES"); mod.node_group = bpy.data.node_groups["Name"]`
  (`agent.run(..., object=...)` does this for you).
- Modifier input values: `getattr(mod.properties.inputs, socket.identifier).value = 5.0`,
  where `socket = mod.node_group.interface.items_tree["Height"]`. The old
  `mod["Socket_1"]` form no longer works in Blender 5.
