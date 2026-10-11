# Simulation Zones

Using a *Simulation Input* and *Simulation Output* node, you can create effects that change over time.

The `@simulation_zone` decorator creates these linked nodes. Like a repeat zone, its parameters are the simulation's state items, and the function returns their new values in the same order.

```python
@simulation_zone
def fall(geometry: Geometry, speed: float, delta_time: float):
    moved = set_position(geometry=geometry, offset=(0.0, 0.0, -speed * delta_time)).geometry
    return moved, speed + 9.8 * delta_time

@tree("Falling")
def falling(geometry: Geometry):
    return fall(geometry, 0.0).geometry
```

A parameter named `delta_time` is not a state item. It receives the time since the previous frame, in seconds.

Each frame, the result from the previous frame is passed into the zone's inputs. The initial call to `fall` in `falling` provides the initial values for the simulation.

## Skipping Steps

Pass `skip=` to set the *Skip* input of the *Simulation Output* node. When it is true, the simulation keeps its previous state for that frame.

```python
paused = compare(a=scene_time().frame, b=50.0, operation="GREATER_THAN").result
fall(geometry, 0.0, skip=paused)
```

## Animation without a Simulation

If a value only depends on the current frame, not on the previous state, you don't need a simulation zone. Use the *Scene Time* node:

```python
frame = scene_time().frame
seconds = scene_time().seconds
```
