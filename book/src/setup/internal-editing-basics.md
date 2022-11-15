# Internal Editing Basics

The fastest way to get up and running is with Blender's built-in *Text Editor*.
You can edit and execute your scripts right inside of Blender:

1. Open a *Text Editor* space.

![A screenshot of the available spaces, with the Text Editor space highlighted](../images/text_editor_space.png)

2. Create a new text data-block with the *New* button.

![A screenshot of the Text Editor space with the new button](../images/text_editor_new.png)

3. Start writing a Geometry Script. As an example, you can paste in the script below. More detailed instructions on writing scripts are in later chapters.

```python
from geometry_script import *

@tree("Repeat Grid")
def repeat_grid(geometry: Geometry, width: Int, height: Int):
    g = grid(
        size_x=width, size_y=height,
        vertices_x=width, vertices_y=height
    ).mesh_to_points()
    return g.instance_on_points(instance=geometry)
```

4. Click the run button to execute the script. This will create a Geometry Nodes tree named *Repeat Grid*.

![A screenshot of the Text Editor space with the Run Script button](../images/text_editor_run_script.png)

5. Create a *Geometry Nodes* modifier on any object in your scene and select the *Repeat Grid* tree.

![A screenshot of the Blender window with a 3x3 grid of cubes on the left and a Geometry Nodes modifier with the Repeat Grid tree selected on the right](../images/geometry_nodes_modifier.png)