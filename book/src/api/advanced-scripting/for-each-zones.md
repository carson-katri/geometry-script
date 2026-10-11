# For Each Element Zones

A *For Each Geometry Element* zone runs a block of nodes once for each element of a geometry, such as each point or each face.

Use the `@for_each_element` decorator, and choose the domain with `domain=`:

```python
@for_each_element(domain="POINT")
def ball_per_point(index: int, radius: float):
    ball = uv_sphere(radius=radius).mesh
    return ForEachResult(
        main={"scale": radius * 2.0},
        generated=[{"geometry": ball, "id": index}],
    )

@tree("Balls")
def balls(geometry: Geometry):
    points = mesh_to_points(mesh=geometry).points
    radius = random_value(min=0.05, max=0.2).value
    result = ball_per_point(points, radius=radius)
    return result.generated.geometry
```

When calling the zone, pass the geometry first. Every other parameter is an input of the zone, evaluated as a field on the geometry, so each element receives its own value. You can also pass `selection=` to only run the zone for some elements.

Two parameter names are special and are not inputs:

* `index` receives the index of the current element.
* `element` receives the current element as its own geometry.

## Results

The zone function returns a `ForEachResult`:

* `main` values are stored as attributes on the input geometry, one value per element.
* `generated` is a list of groups. Each group starts with a geometry, followed by attributes stored on it. The geometry from every element is joined.

The zone's outputs are split the same way. `result.main.geometry` is the input geometry with the `main` attributes, readable as `result.main.scale`. `result.generated.geometry` is the joined generated geometry.

If you only need `main` values, return a dictionary instead of a `ForEachResult`.
