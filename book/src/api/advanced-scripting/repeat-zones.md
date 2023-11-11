# Repeat Zones

Blender 4.0 introduced repeat zones.

Using a *Repeat Input* and *Repeat Output* node, you can loop a block of nodes for a specific number of iterations.

You must use the `@repeat_zone` decorator to create these special linked nodes.

```python
from geometry_script import *

@tree
def test_loop(geometry: Geometry):
    @repeat_zone
    def doubler(value: Float):
        return value * 2
    return points(count=doubler(5, 1)) # double the input value 5 times.
```

The function should modify the input values and return them in the same order.

When calling the repeat zone, pass the *Iterations* argument first, then any other arguments the function accepts.

For example:

```python
def doubler(value: Float) -> Float
```

would be called as:

```python
doubler(iteration_count, value)
```

When a repeat zone has multiple arguments, return a tuple from the zone.

```python
@repeat_zone
def multi_doubler(value1: Float, value2: Float):
    return (value1 * 2, value2 * 2)
```