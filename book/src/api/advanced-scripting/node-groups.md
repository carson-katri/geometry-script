# Node Groups

A Geometry Script can have more than one tree function. Each tree function is a node group, and tree functions can be used in other tree functions to create *Node Group* nodes.

```python
@tree("Instance Grid")
def instance_grid(instance: Geometry):
    """ Instance the input geometry on a grid """
    return grid().mesh_to_points().instance_on_points(instance=instance)

@tree("Cube Grid")
def cube_grid():
    """ Create a grid of cubes """
    return instance_grid(instance=cube(size=0.2))
```

The *Cube Grid* tree uses the *Instance Grid* node group by calling the `instance_grid` function:

![](./cube_grid.png)

The *Instance Grid* node group uses the passed in `instance` argument to create a grid of instances:

![](./instance_grid.png)

This concept can scale to complex interconnected node trees, while keeping everything neatly organized in separate functions.

## Functions vs Node Groups

You do not have to mark a function with `@tree(...)`. If you don't, function calls are treated as normal in Python. No checks are made against the arguments. Any nodes created in the callee will be placed in the caller's tree.

```python
def instance_grid(instance: Geometry): # Not marked with `@tree(...)`
    return grid().mesh_to_points().instance_on_points(instance=instance)

@tree("Cube Grid")
def cube_grid(): # Marked with `@tree(...)`
    return instance_grid(instance=cube(size=0.2))
```

The above example would place the *Grid*, *Mesh to Points*, and *Instance on Points* nodes in the main "Cube Grid" tree. It could be rewritten as:

```python
@tree("Cube Grid")
def cube_grid():
    return grid().mesh_to_points().instance_on_points(instance=cube(size=0.2))
```