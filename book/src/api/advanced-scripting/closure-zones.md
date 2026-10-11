# Closure Zones

A *Closure* zone packages a block of nodes as a value. The closure can be passed around, through node groups or bundles, and evaluated later with an *Evaluate Closure* node.

Use the `@closure_zone` decorator. The function's parameters become the closure's inputs, and its return values become the closure's outputs.

```python
@closure_zone
def scale(x: float, factor: float = 2.0):
    return x * factor

@tree("Closure")
def closure_tree(value: float):
    closure = scale()                          # A Closure socket
    return scale.evaluate(closure, value, 3.0) # Evaluate it
```

Calling the decorated function inside a tree creates the zone and returns its *Closure* socket. `scale.evaluate(closure, ...)` adds an *Evaluate Closure* node with the same inputs and outputs as `scale`, and passes the remaining arguments to its inputs.

The closure must be created before it is evaluated, so the zone's outputs are known.

A tree can take a closure as an input with the `Closure` annotation:

```python
@tree("Apply")
def apply(value: float, operation: Closure):
    return scale.evaluate(operation, value, 2.0)
```
