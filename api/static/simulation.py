import bpy
import inspect
import typing

def simulation_zone(block: typing.Callable):
    """
    Create a simulation input/output block.

    > Only available in Blender 3.6+.
    """
    def wrapped(*args, **kwargs):
        from geometry_script.api.node_mapper import OutputsList, set_or_create_link
        from geometry_script.api.state import State
        from geometry_script.api.types import Type, socket_class_to_data_type

        signature = inspect.signature(block)
        
        # setup zone
        simulation_in = State.current_node_tree.nodes.new(bpy.types.GeometryNodeSimulationInput.__name__)
        simulation_out = State.current_node_tree.nodes.new(bpy.types.GeometryNodeSimulationOutput.__name__)
        simulation_in.pair_with_output(simulation_out)

        # clear state items
        for item in simulation_out.state_items:
            simulation_out.state_items.remove(item)

        # create state items from block signature
        state_items = {}
        for param in [*signature.parameters.values()][1:]:
            state_items[param.name] = (param.annotation, param.default, None, None)
        for i, arg in enumerate(state_items.items()):
            simulation_out.state_items.new(socket_class_to_data_type(arg[1][0].socket_type), arg[0].replace('_', ' ').title())
            set_or_create_link(kwargs[arg[0]] if arg[0] in kwargs else args[i], simulation_in.inputs[i])
        
        step = block(*[Type(o) for o in simulation_in.outputs[:-1]])

        if isinstance(step, Type):
            step = (step,)
        for i, result in enumerate(step):
            State.current_node_tree.links.new(result._socket, simulation_out.inputs[i])

        if len(simulation_out.outputs[:-1]) == 1:
            return Type(simulation_out.outputs[0])
        else:
            return OutputsList({o.name.lower().replace(' ', '_'): Type(o) for o in simulation_out.outputs[:-1]})
    return wrapped