import bpy
import mathutils
import collections.abc

class _Assignment:
    name: str
    node: bpy.types.Node
    props: dict
    arguments: dict
    argument_dot_access: dict

    def __init__(self, name, node, props):
        self.name = name
        self.node = node
        self.props = props
        self.arguments = {}
        self.argument_dot_access = {}
    
    def _flattened_arguments(self):
        for a in self.arguments.values():
            if isinstance(a, _Assignment):
                yield a
            elif isinstance(a, list):
                yield from a
    def flattened_arguments(self):
        return [*self._flattened_arguments()]

    def convert_argument(self, k, v, delimiter='=', index=None):
        if isinstance(v, list):
            v = ', '.join([self.convert_argument("", sv, delimiter="", index=i) for i, sv in enumerate(v)])
            return f"{k}{delimiter}[{v}]"
        if not isinstance(v, _Assignment):
            if isinstance(v, str):
                v = f'"{v}"'
            else:
                v = str(v)
            return f"{k}{delimiter}{v}"
        if v.node.type == 'GROUP_INPUT':
            return f"{k}{delimiter}{self.argument_dot_access[k] if index is None else self.argument_dot_access[k][index]}"
        else:
            return f"{k}{delimiter}{v.name}{'.' + self.argument_dot_access[k] if len(list(o for o in v.node.outputs if o.enabled)) > 1 else ''}"

    def to_script(self):
        snake_case_name = self.node.bl_rna.name.lower().replace(' ', '_')
        args = ', '.join([
            self.convert_argument(k, v)

            for k, v in (list(self.props.items()) + list(self.arguments.items()))
        ])
        return f"{self.name} = {snake_case_name}({args})"

class ConvertTree(bpy.types.Operator):
    bl_idname = "geometry_script.convert_tree"
    bl_label = "Convert to Geometry Script"

    def execute(self, context):
        tree = context.space_data.node_tree

        assignments = []

        def convert_default_value(v):
            if isinstance(v, mathutils.Vector):
                return (v[0], v[1], v[2])
            elif isinstance(v, mathutils.Euler):
                return (v[0], v[1], v[2])
            elif isinstance(v, collections.abc.Iterable):
                return tuple(v)
            else:
                return v

        node_type_counter = {}
        for node in tree.nodes:
            count = node_type_counter.get(node.type[0], 0)
            props = {i.name.lower().replace(' ', '_'): convert_default_value(i.default_value) for i in node.inputs if i.enabled and hasattr(i, 'default_value') and not i.hide_value}
            props.update({k: getattr(node, k) for k in set(p.identifier for p in node.bl_rna.properties) - set(p.identifier for p in node.bl_rna.base.bl_rna.properties)})
            assignments.append(_Assignment(f"{node.type[0].lower()}{count + 1}", node, props))
            node_type_counter[node.type[0]] = count + 1

        sorted_assignments = assignments.copy()
        for link in tree.links:
            to_node = next(a for a in assignments if a.node == link.to_node)
            from_node = next(a for a in assignments if a.node == link.from_node)
            argument_name = link.to_socket.name.lower().replace(' ', '_')
            output_name = link.from_socket.name.lower().replace(' ', '_')
            if argument_name in to_node.props:
                del to_node.props[argument_name]
            if argument_name in to_node.arguments:
                if isinstance(to_node.arguments[argument_name], list):
                    index = len(to_node.arguments[argument_name])
                    to_node.arguments[argument_name].append(from_node)
                    to_node.argument_dot_access[argument_name][index] = output_name
                else:
                    to_node.arguments[argument_name] = [to_node.arguments[argument_name], from_node]
                    to_node.argument_dot_access[argument_name] = {
                        0: to_node.argument_dot_access[argument_name],
                        1: output_name
                    }
            else:
                to_node.arguments[argument_name] = from_node
                to_node.argument_dot_access[argument_name] = output_name

        def topological_sort(root):
            seen = set()
            stack = []
            order = []
            q = [root]
            while q:
                v = q.pop()
                if v not in seen:
                    seen.add(v)
                    q.extend(v.flattened_arguments())

                    while stack and v not in stack[-1].flattened_arguments():
                        order.append(stack.pop())
                    stack.append(v)

            return order[::-1] + stack[::-1]
        
        group_output = next(a for a in assignments if a.node.type == 'GROUP_OUTPUT')
        sorted_assignments = [a for a in topological_sort(group_output) if a.node.type != 'GROUP_OUTPUT' and a.node.type != 'GROUP_INPUT']
        
        body = '\n    '.join([a.to_script() for a in sorted_assignments])

        group_input = next((n for n in tree.nodes if n.type == 'GROUP_INPUT'), None)
        tree_arguments = []
        if group_input is not None:
            for output in group_input.outputs:
                if output.type == 'CUSTOM':
                    continue
                output_name = output.name.lower().replace(' ', '_')
                output_type = output.bl_rna.identifier.replace('NodeSocket', '')
                tree_arguments.append(f"{output_name}: {output_type}")
        tree_arguments = ', '.join(tree_arguments)

        tree_returns = []
        for k, v in group_output.arguments.items():
            tree_returns.append(group_output.convert_argument(f'"{k}"', v, ': '))
        tree_returns = ', '.join(tree_returns)

        script = f"""from geometry_script import *

@tree("{tree.name}")
def {tree.name.lower().replace(' ', '_')}({tree_arguments}):
    {body}
    return {{ {tree_returns} }}"""
        script_datablock = bpy.data.texts.new(tree.name + '.py')
        script_datablock.write(script)
        return {'FINISHED'}