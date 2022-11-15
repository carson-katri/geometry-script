# Introduction

**Geometry Script** is a scripting API for Blender's Geometry Nodes.
It makes complicated node trees more managable and easy to share.

* [Full coverage of nodes](./api/basics/using-nodes.md) available in your Blender version
* Clean, easy to use [Python API](./api/basics.md)
* External [IDE integration](./setup/external-editing.md) for better completions and hot reload

Here's a simple example of what's possible with a short script:

### Geometry Script

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

### Generated Node Tree

![Generated node tree](images/example_generated_tree.png)