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
from .static.sample_mode import *
from .static.simulation import *
from .arrange import _arrange

def _as_iterable(x):
    if isinstance(x, Type):
        return [x,]
    try:
        return iter(x)
    except TypeError:
        return [x,]

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
        # Clear the node group before building
        for node in node_group.nodes:
            node_group.nodes.remove(node)
        while len(node_group.inputs) > sum(map(lambda p: len(p.annotation.__annotations__) if issubclass(p.annotation, InputGroup) else 1, list(signature.parameters.values()))):
            node_group.inputs.remove(node_group.inputs[-1])
        for group_output in node_group.outputs:
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
        for i, node_input in enumerate(node_group.inputs):
            if node_input.bl_socket_idname != list(inputs.values())[i][0].socket_type:
                for ni in node_group.inputs:
                    node_group.inputs.remove(ni)
                break
        builder_inputs = {}
        for i, arg in enumerate(inputs.items()):
            input_name = arg[0].replace('_', ' ').title()
            if len(node_group.inputs) > i:
                node_group.inputs[i].name = input_name
                node_input = node_group.inputs[i]
            else:
                node_input = node_group.inputs.new(arg[1][0].socket_type, input_name)
            if arg[1][1] != inspect.Parameter.empty:
                node_input.default_value = arg[1][1]
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
        for i, result in enumerate(_as_iterable(outputs)):
            if not issubclass(type(result), Type):
                result = Type(value=result)
                # raise Exception(f"Return value '{result}' is not a valid 'Type' subclass.")
            node_group.outputs.new(result.socket_type, 'Result')
            link = node_group.links.new(result._socket, group_output_node.inputs[i])
        
        _arrange(node_group)

        # Return a function that creates a NodeGroup node in the tree.
        # This lets @trees be used in other @trees via simple function calls.
        def group_reference(*args, **kwargs):
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