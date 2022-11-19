# Attributes

An important concept in Geometry Nodes is attributes. Many trees transfer attributes between geometry, using a combination of *Capture Attribute* and *Transfer Attribute*.

Unfortunately, it takes quite a bit of code to use this common pattern.

```python
@tree("Skin")
def skin():
    # Create a cube
    c = cube()
    # Capture the position
    cube_position_attribute = c.capture_attribute(
        data_type=CaptureAttribute.DataType.FLOAT_VECTOR,
        value=position()
    )
    # Create a sphere
    sphere = uv_sphere()
    # Transfer the position to the sphere
    transferred_position = cube_position_attribute.geometry.transfer_attribute(
        data_type=TransferAttribute.DataType.FLOAT_VECTOR,
        attribute=cube_position_attribute.attribute
    )
    # Make the sphere conform to the shape of the cube
    return sphere.set_position(position=transferred_position)
```

Thankfully, a convenient `capture(...)` method is available on `Geometry`, which simplifies this function quite a bit.

```python
@tree("Skin")
def skin():
    # Create a cube
    c = cube()
    # Capture the position
    cube_position = c.capture(position())
    # Create a sphere
    sphere = uv_sphere()
    # Make the sphere conform to the shape of the cube
    return sphere.set_position(position=cube_position())
```

## How it Works

Internally, `capture(...)` works just like the more manual approach.

1. Capture the attribute from the source

In the example above, we capture the `position()` from the cube.
The data type is automatically inferred from the input. If you want to customize other options, simply pass them as keyword arguments to `capture(...)`.

```python
cube_position = c.capture(position())
cube_position = c.capture(position(), domain=CaptureAttribute.Domain.FACE) # Optionally pass other arguments available on `capture_attribute`.
```

2. Transfer the attribute to the target

`capture(...)` returns another function that calls `transfer_attribute` with the correct arguments passed automatically.
Call this returned function (which we store in the variable `cube_position`) to transfer the attribute.
In this example we also set the transferred cube position back onto the sphere.

```python
sphere.set_position(position=cube_position())
sphere.set_position(position=cube_position(mapping=TransferAttribute.Mapping.NEAREST)) # Optionally pass other arguments available on `transfer_attribute`.
```