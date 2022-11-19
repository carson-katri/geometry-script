# Input Groups

Some geometry node trees need a lot of arguments.

```python
@tree("Terrain Generator")
def terrain_generator(
    width: Float
    height: Float
    resolution: Int
    scale: Float
    w: Float
):
    ...
```

There are a couple of problems with this. Firstly, the function signature is getting long. This can make it harder to visually parse the script. And, if we want to use the same arguments in another tree and pass them through to `terrain`, we need to make sure to keep everything up to date.

This is where input groups come in. An input group is class that contains properties annotated with valid socket types.

To create an input group, declare a new class that derives from `InputGroup`.

```python
class TerrainInputs(InputGroup):
    width: Float
    height: Float
    resolution: Int
    scale: Float
    w: Float
```

Then annotate an argument in your tree function with this class.

```python
@tree("Terrain Generator")
def terrain_generator(
    inputs: TerrainInputs
):
    ...
```

This will create a node tree with the exact same structure as the original implementation. The inputs can be accessed with dot notation.

```python
size = combine_xyz(x=input.width, y=input.height)
```

And now passing the inputs through from another function is much simpler.

```python
def point_terrain(
    terrain_inputs: TerrainInputs,
    radius: Float
):
    return terrain_generator(
        inputs=terrain_inputs
    ).mesh_to_points(radius=radius)
```

## Instantiating Input Groups

If you nest calls to tree functions, you can instantiate the `InputGroup` subclass to pass the correct inputs.

```python
def point_terrain():
    return terrain_generator(
        inputs=TerrainInputs(
            width=5,
            height=5,
            resolution=10,
            scale=1,
            w=0
        )
    ).mesh_to_points()
```

## Input Group Prefix

If you use the same `InputGroup` multiple times, you need to provide a prefix. Otherwise, inputs with duplicate names will be created on your tree.

To do this, use square brackets next to the annotation with a string for the prefix.

```python
def mountain_or_canyon(
    mountain_inputs: TerrainInputs["Mountain"], # Prefixed with 'Mountain'
    canyon_inputs: TerrainInputs["Canyon"], # Prefixed with 'Canyon'
    is_mountain: Bool
):
    return terrain_generator(
        inputs=switch(switch=is_mountain, true=mountain_inputs, false=canyon_inputs)
    )
```