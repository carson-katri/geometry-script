# Item Nodes

Some nodes have a list of items you add yourself, instead of a fixed set of sockets. In Geometry Script, the items are passed to the node function and their outputs are available by name.

## Capture Attribute and Format String

Pass each item as a keyword argument. The item's socket type is inferred from its value.

```python
captured = capture_attribute(geometry=mesh, height=separate_xyz(vector=position().position).z)
captured.height

label = format_string(format="Point {index}", index=index().index).string
```

## Index Switch

Pass the items as a list, in order:

```python
shape = index_switch(index=choice, items=[cube().mesh, uv_sphere().mesh, cylinder().mesh]).output
```

## Menu Switch

Pass the items as a dictionary from each menu entry's name to its value. Connecting a tree's `Menu` input to the switch gives the modifier a dropdown with those entries:

```python
@tree("Shape Picker")
def shape_picker(shape: Menu = "Cube"):
    return menu_switch(menu=shape, items={
        "Cube": cube().mesh,
        "Sphere": uv_sphere().mesh,
    }).output
```

## Bundles

*Combine Bundle* takes its items as keyword arguments. *Separate Bundle* takes a dictionary from each item's name to its type, since the values come from the bundle:

```python
bundle = combine_bundle(size=2.0, mesh=cube().mesh).bundle

parts = separate_bundle(bundle=bundle, items={"size": float, "mesh": Geometry})
parts.size, parts.mesh
```

Item outputs can also be read with square brackets, e.g. `parts["size"]`, which is useful for names that aren't valid Python identifiers.
