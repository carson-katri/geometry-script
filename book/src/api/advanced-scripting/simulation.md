# Simulation

Blender 3.6 includes simulation nodes.

Using a *Simulation Input* and *Simulation Output* node, you can create effects that change over time.

As a convenience, the `@simulation_zone` decorator is provided to make simulation node blocks easier to create.

```python
from geometry_script import *

@tree
def test_sim(geometry: Geometry):
    @simulation_zone
    def my_sim(delta_time, geometry: Geometry, value: Float):
        return (geometry, value)
    return my_sim(geometry, 0.26).value
```

The first argument should always be `delta_time`. Any other arguments must also be returned as a tuple with their modified values.
Each frame, the result from the previous frame is passed into the zone's inputs.
The initial call to `my_sim` in `test_sim` provides the initial values for the simulation.