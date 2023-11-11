import bpy
import inspect
import typing

def repeat_zone(block: typing.Callable):
    """
    Create a repeat input/output block.

    > Only available in Blender 4.0+.
    """
    def wrapped(*args, **kwargs):
        from geometry_script.api.node_mapper import OutputsList, set_or_create_link
        from geometry_script.api.state import State
        from geometry_script.api.types import Type, socket_class_to_data_type

        signature = inspect.signature(block)
        
        # setup zone
        repeat_in = State.current_node_tree.nodes.new(bpy.types.GeometryNodeRepeatInput.__name__)
        repeat_out = State.current_node_tree.nodes.new(bpy.types.GeometryNodeRepeatOutput.__name__)
        repeat_in.pair_with_output(repeat_out)

        # clear state items
        for item in repeat_out.repeat_items:
            repeat_out.repeat_items.remove(item)

        # link the iteration count
        set_or_create_link(args[0], repeat_in.inputs[0])

        # create state items from block signature
        repeat_items = {}
        for param in signature.parameters.values():
            repeat_items[param.name] = (param.annotation, param.default, None, None)
        for i, arg in enumerate(repeat_items.items()):
            repeat_out.repeat_items.new(socket_class_to_data_type(arg[1][0].socket_type), arg[0].replace('_', ' ').title())
            # skip the first index, which is reserved for the iteration count
            i = i + 1
            set_or_create_link(kwargs[arg[0]] if arg[0] in kwargs else args[i], repeat_in.inputs[i])
        
        step = block(*[Type(o) for o in repeat_in.outputs[:-1]])

        if isinstance(step, Type):
            step = (step,)
        for i, result in enumerate(step):
            set_or_create_link(result, repeat_out.inputs[i])

        if len(repeat_out.outputs[:-1]) == 1:
            return Type(repeat_out.outputs[0])
        else:
            return OutputsList({o.name.lower().replace(' ', '_'): Type(o) for o in repeat_out.outputs[:-1]})
    return wrapped