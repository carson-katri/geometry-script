# Boolean Math

The *Boolean Math* node gives access to common boolean operations, such as `AND`, `NOT`, `XOR`, etc. Use it together with the *Compare* node to build conditions.

```python
@tree("Select Top")
def select_top(geometry: Geometry, threshold: float = 0.5):
    z = separate_xyz(vector=position().position).z
    above = compare(a=z, b=threshold, operation="GREATER_THAN").result
    is_even = compare(a=index().index % 2, b=0, operation="EQUAL", data_type="INT").result
    selection = boolean_math(boolean=above, boolean_2=is_even, operation="AND").boolean
    return delete_geometry(geometry=geometry, selection=selection).geometry
```

`NOT` only uses the first input:

```python
boolean_math(boolean=above, operation="NOT").boolean
```

> You *cannot* use the Python keywords `and`, `or`, and `not`, or the comparison operators `<`, `==`, etc. on sockets. The script only builds the node tree, so it never sees the values that would decide the result. Use *Compare* and *Boolean Math* nodes instead.

If a condition gets long, a small helper function keeps it readable:

```python
def all_of(*conditions):
    result = conditions[0]
    for condition in conditions[1:]:
        result = boolean_math(boolean=result, boolean_2=condition, operation="AND").boolean
    return result
```
