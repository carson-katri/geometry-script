# Attributes

An important concept in Geometry Nodes is attributes. Many trees capture attributes or transfer them from one domain to another.

## Capturing Attributes

*Capture Attribute* evaluates fields on a geometry and keeps the values for later. Pass each value to capture as a keyword argument; its output has the same name.

```python
@tree("Twist")
def twist(geometry: Geometry, amount: float = 1.0):
    captured = capture_attribute(
        geometry=geometry,
        height=separate_xyz(vector=position().position).z,
    )
    # captured.height still refers to the height before the geometry was moved
    moved = set_position(geometry=captured.geometry, offset=(0.0, 0.0, 1.0)).geometry
    return set_position(geometry=moved, offset=(captured.height * amount, 0.0, 0.0)).geometry
```

> Use the `Geometry` returned from `capture_attribute(...)`, not the original, for the captured values to be available.

You can capture several values at once, and choose the domain:

```python
captured = capture_attribute(geometry=mesh, domain="FACE", normal=normal().normal, index=index().index)
captured.normal, captured.index
```

## Named Attributes

Store an attribute by name with *Store Named Attribute*, and read it back with *Named Attribute*. The data type is inferred when storing; set it when reading.

```python
@tree("Named Attributes")
def named_attributes(geometry: Geometry):
    # Store a value
    geometry = store_named_attribute(
        geometry=geometry,
        name="my_custom_attribute",
        value=0.5,
        domain="POINT",
    ).geometry
    # Read it back
    value = named_attribute(name="my_custom_attribute", data_type="FLOAT").attribute
    return set_position(geometry=geometry, offset=(0.0, 0.0, value)).geometry
```

A helper function can keep the name and type in one place:

```python
def height_attribute():
    return named_attribute(name="height", data_type="FLOAT").attribute
```

## Attribute Sampling
To read values from another geometry, use the sampling nodes: *Sample Index*, *Sample Nearest*, *Sample Nearest Surface*, *Geometry Proximity*, and so on.

```python
# The position of the next point
next_position = sample_index(geometry=points, value=position().position, index=index().index + 1).value

# The color of the nearest point on another geometry
nearest = sample_nearest(geometry=other, sample_position=position().position).index
color = sample_index(geometry=other, value=named_attribute(name="color", data_type="FLOAT_COLOR").attribute, index=nearest).value

# Snap a sphere to the surface of a cube
snapped = geometry_proximity(geometry=cube().mesh, sample_position=position().position).position
set_position(geometry=uv_sphere().mesh, position=snapped).geometry
```
