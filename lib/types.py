import bpy
from .state import State

# The base class all exposed socket types conform to.
class Type:
    socket_type: str

    def __init__(self, socket: bpy.types.NodeSocket = None, value = None):
        if value is not None:
            input_nodes = {
                int: ('FunctionNodeInputInt', 'integer'),
                bool: ('FunctionNodeInputBool', 'boolean'),
                str: ('FunctionNodeInputString', 'string'),
                tuple: ('FunctionNodeInputVector', 'vector'),
                float: ('ShaderNodeValue', None),
            }
            if not type(value) in input_nodes:
                raise Exception(f"'{value}' cannot be expressed as a node.")
            input_node_info = input_nodes[type(value)]
            value_node = State.current_node_tree.nodes.new(input_node_info[0])
            if input_node_info[1] is None:
                value_node.outputs[0].default_value = value
            else:
                setattr(value_node, input_node_info[1], value)
            socket = value_node.outputs[0]
        self._socket = socket
        self.socket_type = type(socket).__name__
    
    def _math(self, other, operation):
        math_node = State.current_node_tree.nodes.new('ShaderNodeVectorMath' if self._socket.type else 'ShaderNodeMath')
        math_node.operation = operation
        State.current_node_tree.links.new(self._socket, math_node.inputs[0])
        if issubclass(type(other), Type):
            State.current_node_tree.links.new(other._socket, math_node.inputs[1])
        else:
            math_node.inputs[1].default_value = other
        return Type(math_node.outputs[0])

    def __add__(self, other):
        return self._math(other, 'ADD')
    
    def __sub__(self, other):
        return self._math(other, 'SUBTRACT')
    
    def __mul__(self, other):
        return self._math(other, 'SUBTRACT')
    
    def __truediv__(self, other):
        return self._math(other, 'DIVIDE')

for standard_socket in bpy.types.NodeSocketStandard.__subclasses__():
    name = standard_socket.__name__.replace('NodeSocket', '')
    globals()[name] = type(name, (Type,), { 'socket_type': standard_socket.__name__ })