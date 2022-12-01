import inspect
import typing

class SimulationInput:
    class DeltaTime: pass
    class ElapsedTime: pass

def simulation(block: typing.Callable[typing.Any, 'Geometry']):
    """
    Create a simulation input/output block.

    > Only available in the `geometry-node-simulation` branch of Blender 3.5.
    """
    def wrapped(geometry: 'Geometry', *args, **kwargs):
        from geometry_script import simulation_input, simulation_output
        simulation_in = simulation_input(geometry=geometry)
        signature = inspect.signature(block)
        for key, value in signature.parameters.items():
            match value.annotation:
                case SimulationInput.DeltaTime:
                    kwargs[key] = simulation_in.delta_time
                case SimulationInput.ElapsedTime:
                    kwargs[key] = simulation_in.elapsed_time
        return simulation_output(geometry=block(simulation_in.geometry, *args, **kwargs)).geometry
    return wrapped