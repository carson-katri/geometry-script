# Generators

Python has support for [generators](https://wiki.python.org/moin/Generators) using the `yield` keyword.

Tree functions can be written as generators. Each yielded value becomes a separate output, just like returning a tuple:

```python
@tree("Primitive Shapes")
def primitive_shapes():
    yield cube().mesh        # Result
    yield uv_sphere().mesh   # Result 2
    yield 5                  # Result 3
```

This is handy when the outputs are computed in several steps, since each one can be yielded as soon as it's ready.

## Joining Geometry

Yielded geometry is *not* joined automatically. To output several geometries as one, pass a list to *Join Geometry*:

```python
@tree("Primitive Shapes")
def primitive_shapes():
    return join_geometry(geometry=[
        cube().mesh,
        uv_sphere().mesh,
        cylinder().mesh,
    ]).geometry
```

Multi-input sockets, such as the *Geometry* input of *Join Geometry* or the *Mesh* input of *Mesh Boolean*, accept a list of sockets.

> The first output is always displayed when using a *Geometry Nodes* modifier. Ensure it is a `Geometry` socket, unless you are using the function as a node group.
