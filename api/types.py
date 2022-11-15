import bpy
from bpy.types import NodeSocketStandard
import nodeitems_utils
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
        math_node = State.current_node_tree.nodes.new('ShaderNodeVectorMath' if self._socket.type == 'VECTOR' else 'ShaderNodeMath')
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
        return self._math(other, 'MULTIPLY')
    
    def __truediv__(self, other):
        return self._math(other, 'DIVIDE')
    
    def __mod__(self, other):
        return self._math(other, 'MODULO')
    
    def _compare(self, other, operation):
        compare_node = State.current_node_tree.nodes.new('FunctionNodeCompare')
        compare_node.data_type = 'FLOAT' if self._socket.type == 'VALUE' else self._socket.type
        compare_node.operation = operation
        a = None
        b = None
        for node_input in compare_node.inputs:
            if not node_input.enabled:
                continue
            elif a is None:
                a = node_input
            else:
                b = node_input
        State.current_node_tree.links.new(self._socket, a)
        if issubclass(type(other), Type):
            State.current_node_tree.links.new(other._socket, b)
        else:
            b.default_value = other
        return Type(compare_node.outputs[0])
    
    def __eq__(self, other):
        return self._compare(other, 'EQUAL')
    
    def __ne__(self, other):
        return self._compare(other, 'NOT_EQUAL')
    
    def __lt__(self, other):
        return self._compare(other, 'LESS_THAN')
    
    def __le__(self, other):
        return self._compare(other, 'LESS_EQUAL')
    
    def __gt__(self, other):
        return self._compare(other, 'GREATER_THAN')
    
    def __ge__(self, other):
        return self._compare(other, 'GREATER_EQUAL')
    
    def _get_xyz_component(self, component):
        if self._socket.type != 'VECTOR':
            raise Exception("`x`, `y`, `z` properties are not available on non-Vector types.")
        separate_node = State.current_node_tree.nodes.new('ShaderNodeSeparateXYZ')
        State.current_node_tree.links.new(self._socket, separate_node.inputs[0])
        return Type(separate_node.outputs[component])
    @property
    def x(self):
        return self._get_xyz_component(0)
    @property
    def y(self):
        return self._get_xyz_component(1)
    @property
    def z(self):
        return self._get_xyz_component(2)

for standard_socket in list(filter(lambda x: 'NodeSocket' in x, dir(bpy.types))):
    name = standard_socket.replace('NodeSocket', '')
    if len(name) < 1:
        continue
    globals()[name] = type(name, (Type,), { 'socket_type': standard_socket, '__module__': Type.__module__ })
    if name == 'Int':
        class IntIterator:
            def __init__(self, integer):
                self.integer = integer
                self.points = State.current_node_tree.nodes.new('GeometryNodePoints')
                State.current_node_tree.links.new(self.integer._socket, self.points.inputs[0])
                self.index = State.current_node_tree.nodes.new('GeometryNodeInputIndex')
                self._did_iterate = False
            def __next__(self):
                if not self._did_iterate:
                    self._did_iterate = True
                    return Type(self.index.outputs[0]), Type(self.points.outputs[0])
                else:
                    raise StopIteration()
        globals()[name].__iter__ = lambda self: IntIterator(self)