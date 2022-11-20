# Attributes

An important concept in Geometry Nodes is attributes. Many trees capture attributes or transfer them from one geometry to another.

When using these methods, the `data_type` argument must be correctly specified for the transfer to work as intended.

```python
@tree("Skin")
def skin():
    # Create a cube
    c = cube()
    # Create a sphere
    sphere = uv_sphere()
    # Transfer the position to the sphere
    transferred_position = c.transfer_attribute(
        data_type=TransferAttribute.DataType.FLOAT_VECTOR,
        attribute=position()
    )
    # Make the sphere conform to the shape of the cube
    return sphere.set_position(position=transferred_position)
```

To improve the usability of these nodes, `capture(...)` and `transfer(...)` methods are provided on `Geometry` that simply take the attribute and any other optional arguments.

```python
@tree("Skin")
def skin():
    # Create a cube
    c = cube()
    # Create a sphere
    sphere = uv_sphere()
    # Make the sphere conform to the shape of the cube
    return sphere.set_position(position=c.transfer(position()))
```

The same is available for `capture(...)`.

```python
geometry_with_attribute, attribute = c.capture(position())
```

> You must use the `Geometry` returned from `capture(...)` for the anonymous attribute it creates to be usable.

Any additional keyword arguments can be passed as normal.

```python
c.transfer(position(), mapping=TransferAttribute.Mapping.INDEX)
```