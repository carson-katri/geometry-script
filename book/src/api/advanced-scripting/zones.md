# Zones

A zone is a region of a node tree between a pair of input and output nodes, such as *Repeat Input* and *Repeat Output*. The nodes inside the zone are evaluated differently from the rest of the tree: repeated, run once per frame, run once per element, or packaged up to be evaluated later.

Geometry Script has a decorator for each kind of zone:

| Zone | Decorator | Runs its nodes | Works in |
|---|---|---|---|
| [Repeat](./repeat-zones.md) | `@repeat_zone` | A set number of times, feeding each result into the next iteration | Geometry Nodes, shaders |
| [Simulation](./simulation-zones.md) | `@simulation_zone` | Once per frame, starting from the previous frame's result | Geometry Nodes |
| [For Each Element](./for-each-zones.md) | `@for_each_element(domain=...)` | Once for each point, face, or other element of a geometry | Geometry Nodes |
| [Closure](./closure-zones.md) | `@closure_zone` | Whenever the closure is evaluated | Geometry Nodes, shaders |

## Writing a Zone

The decorated function is the body of the zone. Its parameters become the zone's items, and the values it returns are connected to the zone's output node:

```python
@repeat_zone
def grow(geometry: Geometry, size: float):
    bigger = transform_geometry(geometry=geometry, scale=(1.1, 1.1, 1.1)).geometry
    return bigger, size * 1.1
```

* Each parameter's annotation sets the item's socket type, just like the inputs of a [tree function](../basics/tree-functions.md#group-input). Without an annotation, the type is inferred from the value passed in.
* Return one value per item, in the same order as the parameters. You can also return a dictionary keyed by parameter name.
* Some parameter names are special, and receive a value from the zone instead of being an item: `iteration` in a repeat zone, `delta_time` in a simulation zone, and `index` and `element` in a for-each zone.

## Using a Zone

Call the decorated function inside a tree function to add the zone to the tree. Pass the initial value of each item, positionally or by name, along with any settings of the zone itself, such as `iterations=` or `skip=`:

```python
@tree("Growing Cube")
def growing_cube(steps: int = 4):
    result = grow(cube().mesh, 1.0, iterations=steps)
    return result.geometry, result.size
```

A zone with a single item returns that socket directly. A zone with several items returns a named tuple with a field per item. For-each and closure zones return their own kinds of results, described on their pages.

Each call adds a new zone, so the same decorated function can be used several times, in one tree or in many. Zones can only be called while a tree is being built.

A zone can also be defined inside the tree function that uses it, which lets its body use the tree's inputs directly:

```python
@tree("Spiral")
def spiral(count: int = 12, turn: float = 0.5):
    @repeat_zone
    def step(geometry: Geometry, iteration: int):
        point = points(position=(math_(operation="COSINE", value=iteration * turn).value,
                                 math_(operation="SINE", value=iteration * turn).value,
                                 iteration * 0.1)).points
        return join_geometry(geometry=[geometry, point]).geometry

    return step(points(count=0).points, iterations=count)
```

The next pages cover each kind of zone in detail.
