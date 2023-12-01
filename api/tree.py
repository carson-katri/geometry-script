import bpy
import inspect
try:
    import node_arrange as node_arrange
except:
    pass
from .state import State
from .types import *
from .node_mapper import *
from .static.attribute import *
from .static.curve import *
from .static.expression import *
from .static.input_group import *
from .static.repeat import *
from .static.sample_mode import *
from .static.simulation import *
from .arrange import _arrange

IS_BLENDER_4 = bpy.app.version[0] >= 4

def _as_iterable(x):
    if isinstance(x, Type):
        return [x,]
    try:
        return iter(x)
    except TypeError:
        return [x,]

def get_node_inputs(x):
    if IS_BLENDER_4:
        return [i for i in x.interface.items_tree if i.item_type == 'SOCKET' and i.in_out == 'INPUT']
    else:
        return x.inputs
def get_node_outputs(x):
    if IS_BLENDER_4:
        return [i for i in x.interface.items_tree if i.item_type == 'SOCKET' and i.in_out == 'OUTPUT']
    else:
        return x.outputs

def tree(name):
    tree_name = name
    def build_tree(builder):
        signature = inspect.signature(builder)

        # Locate or create the node group
        node_group = None
        if tree_name in bpy.data.node_groups:
            node_group = bpy.data.node_groups[tree_name]
        else:
            node_group = bpy.data.node_groups.new(tree_name, 'GeometryNodeTree')

        if IS_BLENDER_4:
            node_group.is_modifier = True

        # Clear the node group before building
        for node in node_group.nodes:
            node_group.nodes.remove(node)

        node_inputs = get_node_inputs(node_group)
        input_count = sum(map(lambda p: len(p.annotation.__annotations__) if issubclass(p.annotation, InputGroup) else 1, list(signature.parameters.values())))
        for node_input in node_inputs[input_count:]:
            if IS_BLENDER_4:
                node_group.interface.remove(node_input)
            else:
                node_group.inputs.remove(node_input)

        for group_output in get_node_outputs(node_group):
            if IS_BLENDER_4:
                node_group.interface.remove(group_output)
            else:
                node_group.outputs.remove(group_output)
        
        # Setup the group inputs
        group_input_node = node_group.nodes.new('NodeGroupInput')
        group_output_node = node_group.nodes.new('NodeGroupOutput')

        # Collect the inputs
        inputs = {}
        def validate_param(param):
            if param.annotation == inspect.Parameter.empty:
                raise Exception(f"Tree input '{param.name}' has no type specified. Please annotate with a valid node input type.")
            if not issubclass(param.annotation, Type):
                raise Exception(f"Type of tree input '{param.name}' is not a valid 'Type' subclass.")
        for param in signature.parameters.values():
            if issubclass(param.annotation, InputGroup):
                instance = param.annotation()
                prefix = (param.annotation.prefix + "_") if hasattr(param.annotation, "prefix") else ""
                for group_param, annotation in param.annotation.__annotations__.items():
                    default = getattr(instance, group_param, None)
                    inputs[prefix + group_param] = (annotation, inspect.Parameter.empty if default is None else default, param.name, prefix)
            else:
                validate_param(param)
                inputs[param.name] = (param.annotation, param.default, None, None)

        # Create the input sockets and collect input values.
        node_inputs = get_node_inputs(node_group)
        for i, node_input in enumerate(node_inputs):
            if node_input.bl_socket_idname != list(inputs.values())[i][0].socket_type:
                for ni in node_inputs:
                    if IS_BLENDER_4:
                        node_group.interface.remove(ni)
                    else:
                        node_group.inputs.remove(ni)
                break
        builder_inputs = {}

        node_inputs = get_node_inputs(node_group)
        for i, arg in enumerate(inputs.items()):
            input_name = arg[0].replace('_', ' ').title()
            if len(node_inputs) > i:
                node_inputs[i].name = input_name
                node_input = node_inputs[i]
            else:
                if IS_BLENDER_4:
                    node_input = node_group.interface.new_socket(socket_type=arg[1][0].socket_type, name=input_name, in_out='INPUT')
                else:
                    node_input = node_group.inputs.new(arg[1][0].socket_type, input_name)
            if arg[1][1] != inspect.Parameter.empty:
                node_input.default_value = arg[1][1]
            if hasattr(arg[1][0], 'min_value'):
                node_input.min_value = arg[1][0].min_value
            if hasattr(arg[1][0], 'max_value'):
                node_input.max_value = arg[1][0].max_value
            if arg[1][2] is not None:
                if arg[1][2] not in builder_inputs:
                    builder_inputs[arg[1][2]] = signature.parameters[arg[1][2]].annotation()
                setattr(builder_inputs[arg[1][2]], arg[0].replace(arg[1][3], ''), arg[1][0](group_input_node.outputs[i]))
            else:
                builder_inputs[arg[0]] = arg[1][0](group_input_node.outputs[i])

        # Run the builder function
        State.current_node_tree = node_group
        if inspect.isgeneratorfunction(builder):
            generated_outputs = [*builder(**builder_inputs)]
            if all(map(lambda x: issubclass(type(x), Type) and x._socket.type == 'GEOMETRY', generated_outputs)):
                outputs = join_geometry(geometry=generated_outputs)
            else:
                outputs = generated_outputs
        else:
            outputs = builder(**builder_inputs)

        # Create the output sockets
        if isinstance(outputs, dict):
            # Use a dict to name each return value
            for i, (k, v) in enumerate(outputs.items()):
                if not issubclass(type(v), Type):
                    v = Type(value=v)
                if IS_BLENDER_4:
                    node_group.interface.new_socket(socket_type=v.socket_type, name=k, in_out='OUTPUT')
                else:
                    node_group.outputs.new(v.socket_type, k)
                node_group.links.new(v._socket, group_output_node.inputs[i])
        else: 
            for i, result in enumerate(_as_iterable(outputs)):
                if not issubclass(type(result), Type):
                    result = Type(value=result)
                    # raise Exception(f"Return value '{result}' is not a valid 'Type' subclass.")
                if IS_BLENDER_4:
                    node_group.interface.new_socket(socket_type=result.socket_type, name='Result', in_out='OUTPUT')
                else:
                    node_group.outputs.new(result.socket_type, 'Result')
                node_group.links.new(result._socket, group_output_node.inputs[i])
        
        _arrange(node_group)

        # Return a function that creates a NodeGroup node in the tree.
        # This lets @trees be used in other @trees via simple function calls.
        def group_reference(*args, **kwargs):
            if IS_BLENDER_4:
                result = geometrynodegroup(node_tree=node_group, *args, **kwargs)
            else:
                result = group(node_tree=node_group, *args, **kwargs)
            group_outputs = []
            for group_output in result._socket.node.outputs:
                group_outputs.append(Type(group_output))
            if len(group_outputs) == 1:
                return group_outputs[0]
            else:
                return tuple(group_outputs)
        return group_reference
    if isinstance(name, str):
        return build_tree
    else:
        tree_name = name.__name__
        return build_tree(name)