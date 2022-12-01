# Simulation

> This API is subject to change as future builds of Blender with simulation nodes are released.

The `geometry-nodes-simulation` branch of Blender 3.5 includes support for "simulation nodes".

Using a *Simulation Input* and *Simulation Output* node, you can create effects that change over time.

As a convenience, the `@simulation` decorator is provided to make simulation node blocks easier to create.

```python
@simulation
def move_over_time(
    geometry: Geometry, # the first input must be `Geometry`
    speed: Float,
    dt: SimulationInput.DeltaTime, # Automatically passes the delta time on any argument annotated with `SimulationInput.DeltaTime`.
    elapsed: SimulationInput.ElapsedTime, # Automatically passes the elapsed time
) -> Geometry:
    return geometry.set_position(
        offset=combine_xyz(x=speed)
    )
```

Every frame the argument `geometry` will be set to the geometry from the previous frame. This allows the offset to accumulate over time.

The `SimulationInput.DeltaTime`/`SimulationInput.ElapsedTime` types mark arguments that should be given the outputs from the *Simulation Input* node.