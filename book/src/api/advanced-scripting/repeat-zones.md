# Repeat Zones

Using a *Repeat Input* and *Repeat Output* node, you can loop a block of nodes for a specific number of iterations.

Use the `@repeat_zone` decorator to create these linked nodes. The function's parameters become the zone's items, and the function returns their new values in the same order.

```python
@repeat_zone
def doubler(value: float):
    return value * 2

@tree("Test Loop")
def test_loop():
    # Double the input value 5 times.
    return points(count=doubler(1.0, iterations=5)).points
```

When calling the repeat zone, pass the initial value of each item, then the number of iterations as `iterations=`.

A zone can also be defined inside the tree function that uses it.

## Multiple Items

When a repeat zone has multiple items, return a tuple from the zone. Calling it returns a named tuple with a field per item:

```python
@repeat_zone
def multi_doubler(value1: float, value2: float):
    return value1 * 2, value2 * 2

@tree("Multi Doubler")
def multi_doubler_tree():
    result = multi_doubler(1.0, 2.0, iterations=3)
    return result.value1, result.value2
```

You can also return a dictionary from the zone, keyed by parameter name.

## Iteration Index

A parameter named `iteration` is not an item. It receives the *Iteration* output of the zone, which counts from 0.

```python
@repeat_zone
def stack(geometry: Geometry, iteration: int):
    layer = transform_geometry(geometry=cube().mesh, translation=(0.0, 0.0, iteration * 1.5)).geometry
    return join_geometry(geometry=[geometry, layer]).geometry

@tree("Tower")
def tower(floors: int = 5):
    return stack(cube().mesh, iterations=floors)
```
