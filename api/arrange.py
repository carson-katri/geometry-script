import bpy
import typing

def _arrange(node_tree, padding: typing.Tuple[float, float] = (50, 25)):
    # Organize the nodes into columns based on their links.
    columns: typing.List[typing.List[typing.Any]] = []
    def contains_link(node, column):
        return any(
            any(
                any(link.from_node == node for link in input.links)
                for input in n.inputs
            )
            for n in column
        )
    for node in reversed(node_tree.nodes):
        if (x := next(
            filter(
                lambda x: contains_link(node, x[1]),
                enumerate(columns)
            ),
            None
        )) is not None:
            if x[0] > 0:
                columns[x[0] - 1].append(node)
            else:
                columns.insert(x[0], [node])
        else:
            if len(columns) == 0:
                columns.append([node])
            else:
                columns[len(columns) - 1].append(node)
    
    # Arrange the columns, computing the size of the node manually so arrangement can be done without UI being visible.
    UI_SCALE = bpy.context.preferences.view.ui_scale
    NODE_HEADER_HEIGHT = 20
    NODE_LINK_HEIGHT = 28
    NODE_PROPERTY_HEIGHT = 28
    NODE_VECTOR_HEIGHT = 84
    x = 0
    for col in columns:
        largest_width = 0
        y = 0
        for node in col:
            node.update()
            input_count = len(list(filter(lambda i: i.enabled, node.inputs)))
            output_count = len(list(filter(lambda i: i.enabled, node.outputs)))
            parent_props = [prop.identifier for base in type(node).__bases__ for prop in base.bl_rna.properties]
            properties_count = len([prop for prop in node.bl_rna.properties if prop.identifier not in parent_props])
            unset_vector_count = len(list(filter(lambda i: i.enabled and i.type == 'VECTOR' and len(i.links) == 0, node.inputs)))
            node_height = (
                NODE_HEADER_HEIGHT \
                + (output_count * NODE_LINK_HEIGHT) \
                + (properties_count * NODE_PROPERTY_HEIGHT) \
                + (input_count * NODE_LINK_HEIGHT) \
                + (unset_vector_count * NODE_VECTOR_HEIGHT)
            ) * UI_SCALE
            if node.width > largest_width:
                largest_width = node.width
            node.location = (x, y)
            y -= node_height + padding[1]
        x += largest_width + padding[0]