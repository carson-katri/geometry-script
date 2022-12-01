# Attributes

An important concept in Geometry Nodes is attributes. Many trees capture attributes or transfer them from one domain to another.

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

## Named Attributes

Custom attributes can be created by name.
The safest way to use named attributes is with the `Attribute` class.

Create a named attribute with a data type and optional domain, then use the `store(...)`, `exists()`, and `__call__(...)` methods to use it.

```python
# Create the attribute
my_custom_attribute = Attribute(
    "my_custom_attribute",
    NamedAttribute.DataType.FLOAT, # declare the data type once
    StoreNamedAttribute.Domain.INSTANCE # optional
)
# Store a value
geometry = my_custom_attribute.store(geometry, 0.5)
# Use the value by calling the attribute
geometry = geometry.set_position(offset=my_custom_attribute())
```

## Attribute Sampling
In Blender 3.4+, transfer attribute was replaced with a few separate nodes: *Sample Index*, *Sample Nearest*, and *Sample Nearest Surface*.

To avoid inputting data types and geometry manually, you can use the custom `Geometry` subscript.

The structure for these subscripts is:

```python
geometry[value : index or sample position : domain, mode, domain]
```

Only the value argument is required. Other arguments can be supplied as needed.

```python
geometry[value]
geometry[value : sample_position, SampleMode.NEAREST]
geometry[value : index() + 1 : SampleIndex.Domain.EDGE]
```

Try passing different arguments and see how the resulting nodes are created.