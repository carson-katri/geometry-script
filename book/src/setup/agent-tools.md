# Command-Line and Agent Tools

Geometry Script includes a few tools that report on a script in a few lines of plain text, instead of tracebacks or screenshots. They are useful when running scripts outside of Blender's UI, and for AI coding agents that build node trees.

## Running a Script

`agent.run` builds the trees in a script, optionally attaches the last one to an object, evaluates it, and prints a short report:

```python
from geometry_script import agent
agent.run("/path/to/Repeat Grid.py", object="Cube")
```

```
built 'Repeat Grid': 14 nodes; in (Geometry: Geometry, Columns: Int = 3, Rows: Int = 3, Spacing X: Float = 0, Spacing Y: Float = 0) -> out (Result: Geometry)
object 'Cube': instances 9; instance positions (-2, -2, 0)..(2, 2, 0)
```

`object=` names the object to add a *Geometry Nodes* modifier to, creating the object if it doesn't exist. `tree=` picks which tree to attach, instead of the last one built. If the script fails, the report shows the error and the line of your script that caused it. Pass `traceback=True` for the full traceback.

`agent.status()` prints the report of the latest run, including runs triggered by [Live Edit](./external-editing.md#linking-with-blender).

To run a script in background Blender from a terminal, use `tools/run.py` from the repository. It loads Geometry Script from the checkout, so the extension doesn't need to be installed:

```sh
python3 tools/run.py "examples/Repeat Grid.py" --object Cube
python3 tools/run.py "examples/City Builder.py" --object Roads --blend city.blend
```

## Looking Up Nodes

```sh
python3 tools/describe.py --search "points on faces"   # find a node
python3 tools/describe.py set_position mesh_to_points  # print their signatures
```

Inside Blender, the same is available as `agent.search(...)` and `agent.describe(...)`.

## Reading an Existing Tree

`agent.describe_tree("Tree Name")` prints any geometry node tree, including ones made by hand, as Geometry Script calls. Inputs left at their default values are omitted.

## Agent Skill

The repository includes a skill for AI coding agents in `skills/geometry-script/SKILL.md`. It explains the API and the run-and-fix loop above, including how to use these tools through Blender's MCP server.
