import bpy
import re
from inspect import getfullargspec
try:
    import node_arrange as node_arrange
except:
    pass
from .state import State
from .types import Type
from .node_mapper import *

def _as_iterable(input):
    try:
        return iter(input)
    except TypeError:
        return {input}

def tree(name):
    tree_name = name
    def build_tree(builder):
        # Locate or create the node group
        node_group = None
        if tree_name in bpy.data.node_groups:
            node_group = bpy.data.node_groups[tree_name]
        else:
            node_group = bpy.data.node_groups.new(tree_name, 'GeometryNodeTree')
        # Clear the node group before building
        for node in node_group.nodes:
            node_group.nodes.remove(node)
        for group_input in node_group.inputs:
            node_group.inputs.remove(group_input)
        for group_output in node_group.outputs:
            node_group.outputs.remove(group_output)
        
        # Setup the group inputs
        group_input_node = node_group.nodes.new('NodeGroupInput')
        group_output_node = node_group.nodes.new('NodeGroupOutput')

        # Collect the inputs
        argspec = getfullargspec(builder)
        inputs = {}
        for arg in argspec.args:
            if not arg in argspec.annotations:
                raise Exception(f"Tree input '{arg}' has no type specified. Please specify a valid NodeInput subclass.")
            type_annotation = argspec.annotations[arg]
            if not issubclass(type_annotation, Type):
                raise Exception(f"Type of tree input '{arg}' is not a valid 'Type' subclass.")
            inputs[arg] = type_annotation

        # Create the input sockets and collect input values.
        builder_inputs = []
        for i, arg in enumerate(inputs.items()):
            node_group.inputs.new(arg[1].socket_type, re.sub('([A-Z])', r' \1', arg[0]).title())
            builder_inputs.append(arg[1](group_input_node.outputs[i]))

        # Run the builder function
        State.current_node_tree = node_group
        outputs = builder(*builder_inputs)

        # Create the output sockets
        for i, result in enumerate(_as_iterable(outputs)):
            if not issubclass(type(result), Type):
                result = Type(value=result)
                # raise Exception(f"Return value '{result}' is not a valid 'Type' subclass.")
            node_group.outputs.new(result.socket_type, 'Result')
            link = node_group.links.new(result._socket, group_output_node.inputs[i])
        
        # Attempt to run the "Node Arrange" add-on on the tree.
        try:
            for area in bpy.context.screen.areas:
                for space in area.spaces:
                    if space.type == 'NODE_EDITOR':
                        space.node_tree = node_group
                        with bpy.context.temp_override(area=area, space=space, space_data=space):
                            ntree = node_group
                            ntree.nodes[0].select = True
                            ntree.nodes.active = ntree.nodes[0]
                            n_groups = []
                            for i in ntree.nodes:
                                if i.type == 'GROUP':
                                    n_groups.append(i)

                            while n_groups:
                                j = n_groups.pop(0)
                                node_arrange.nodes_iterate(j.node_tree)
                                for i in j.node_tree.nodes:
                                    if i.type == 'GROUP':
                                        n_groups.append(i)

                            node_arrange.nodes_iterate(ntree)

                            # arrange nodes + this center nodes together
                            if bpy.context.scene.node_center:
                                node_arrange.nodes_center(ntree)
        except:
            pass

        # Return a function that creates a NodeGroup node in the tree.
        # This lets @trees be used in other @trees via simple function calls.
        def group_reference(*args, **kwargs):
            return group(node_tree=node_group, *args, **kwargs)
        return group_reference
    if isinstance(name, str):
        return build_tree
    else:
        tree_name = name.__name__
        return build_tree(name)