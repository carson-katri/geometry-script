# Boolean Math

The *Boolean Math* node gives access to common boolean operations, such as `AND`, `NOT`, `XOR`, etc. Use it together with comparisons (which create *Compare* nodes) to build conditions.

```python
@tree("Select Top")
def select_top(geometry: Geometry, threshold: float = 0.5):
    z = separate_xyz(vector=position().position).z
    above = z > threshold
    is_even = index().index % 2 == 0
    selection = boolean_math(boolean=above, boolean_2=is_even, operation="AND").boolean
    return delete_geometry(geometry=geometry, selection=selection).geometry
```

`NOT` only uses the first input:

```python
boolean_math(boolean=above, operation="NOT").boolean
```

> You *cannot* use the Python keywords `and`, `or`, and `not` on sockets. The script only builds the node tree, so it never sees the values that would decide the result. Use *Boolean Math* nodes instead.

If a condition gets long, a small helper function keeps it readable:

```python
def all_of(*conditions):
    result = conditions[0]
    for condition in conditions[1:]:
        result = boolean_math(boolean=result, boolean_2=condition, operation="AND").boolean
    return result
```
