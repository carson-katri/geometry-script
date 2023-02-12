import bpy
from bpy.types import NodeSocketStandard
import nodeitems_utils
import enum
from .state import State
from .static.sample_mode import SampleMode
import geometry_script

def map_case_name(i):
    return ('_' if not i.identifier[0].isalpha() else '') + i.identifier.replace(' ', '_').upper()

def socket_type_to_data_type(socket_type):
    match socket_type:
        case 'VALUE':
            return 'FLOAT'
        case 'VECTOR':
            return 'FLOAT_VECTOR'
        case 'COLOR':
            return 'FLOAT_COLOR'
        case _:
            return socket_type

# The base class all exposed socket types conform to.
class _TypeMeta(type):
    def __getitem__(self, args):
        for s in filter(lambda x: isinstance(x, slice), args):
            if (isinstance(s.start, float) or isinstance(s.start, int)) and (isinstance(s.stop, float) or isinstance(s.stop, int)):
                print(f"minmax: ({s.start}, {s.stop})")
            elif isinstance(s.start, str):
                print(f"{s.start} = {s.stop}")
        return self

class Type(metaclass=_TypeMeta):
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
            if type(value) == int:
                print("Making an integer node?")
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
    
    def _math(self, other, operation, reverse=False):
        if self._socket.type == 'VECTOR':
            return geometry_script.vector_math(operation=operation, vector=(other, self) if reverse else (self, other))
        else:
            return geometry_script.math(operation=operation, value=(other, self) if reverse else (self, other))

    def __add__(self, other):
        return self._math(other, 'ADD')
    
    def __radd__(self, other):
        return self._math(other, 'ADD', True)
    
    def __sub__(self, other):
        return self._math(other, 'SUBTRACT')
    
    def __rsub__(self, other):
        return self._math(other, 'SUBTRACT', True)
    
    def __mul__(self, other):
        return self._math(other, 'MULTIPLY')
    
    def __rmul__(self, other):
        return self._math(other, 'MULTIPLY', True)
    
    def __truediv__(self, other):
        return self._math(other, 'DIVIDE')
    
    def __rtruediv__(self, other):
        return self._math(other, 'DIVIDE', True)
    
    def __mod__(self, other):
        return self._math(other, 'MODULO')
    
    def __rmod__(self, other):
        return self._math(other, 'MODULO', True)
    
    def _compare(self, other, operation):
        return geometry_script.compare(operation=operation, a=self, b=other)
    
    def __eq__(self, other):
        if self._socket.type == 'BOOLEAN':
            return self._boolean_math(other, 'XNOR')
        else:
            return self._compare(other, 'EQUAL')
    
    def __ne__(self, other):
        if self._socket.type == 'BOOLEAN':
            return self._boolean_math(other, 'XOR')
        else:
            return self._compare(other, 'NOT_EQUAL')
    
    def __lt__(self, other):
        return self._compare(other, 'LESS_THAN')
    
    def __le__(self, other):
        return self._compare(other, 'LESS_EQUAL')
    
    def __gt__(self, other):
        return self._compare(other, 'GREATER_THAN')
    
    def __ge__(self, other):
        return self._compare(other, 'GREATER_EQUAL')
    
    def _boolean_math(self, other, operation, reverse=False):
        boolean_math_node = State.current_node_tree.nodes.new('FunctionNodeBooleanMath')
        boolean_math_node.operation = operation
        a = None
        b = None
        for node_input in boolean_math_node.inputs:
            if not node_input.enabled:
                continue
            elif a is None:
                a = node_input
            else:
                b = node_input
        State.current_node_tree.links.new(self._socket, a)
        if other is not None:
            if issubclass(type(other), Type):
                State.current_node_tree.links.new(other._socket, b)
            else:
                b.default_value = other
        return Type(boolean_math_node.outputs[0])
    
    def __and__(self, other):
        return self._boolean_math(other, 'AND')

    def __rand__(self, other):
        return self._boolean_math(other, 'AND', reverse=True)
    
    def __or__(self, other):
        return self._boolean_math(other, 'OR')
    
    def __ror__(self, other):
        return self._boolean_math(other, 'OR', reverse=True)
    
    def __invert__(self):
        if self._socket.type == 'BOOLEAN':
            return self._boolean_math(None, 'NOT')
        else:
            return self._math((-1, -1, -1) if self._socket.type == 'VECTOR' else -1, 'MULTIPLY')
    
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
    
    def capture(self, value, **kwargs):
        data_type = socket_type_to_data_type(value._socket.type)
        res = self.capture_attribute(data_type=data_type, value=value, **kwargs)
        return res.geometry, res.attribute
    def transfer(self, attribute, **kwargs):
        data_type = socket_type_to_data_type(attribute._socket.type)
        return self.transfer_attribute(data_type=data_type, attribute=attribute, **kwargs)
    
    def __getitem__(self, subscript):
        if isinstance(subscript, tuple):
            accessor = subscript[0]
            args = subscript[1:]
        else:
            accessor = subscript
            args = []
        sample_mode = SampleMode.INDEX if len(args) < 1 else args[0]
        domain = 'POINT' if len(args) < 2 else (args[1].value if isinstance(args[1], enum.Enum) else args[1])
        sample_position = None
        sampling_index = None
        if isinstance(accessor, slice):
            data_type = socket_type_to_data_type(accessor.start._socket.type)
            value = accessor.start
            match sample_mode:
                case SampleMode.INDEX:
                    sampling_index = accessor.stop
                case SampleMode.NEAREST_SURFACE:
                    sample_position = accessor.stop
                case SampleMode.NEAREST:
                    sample_position = accessor.stop
            if accessor.step is not None:
                domain = accessor.step.value if isinstance(accessor.step, enum.Enum) else accessor.step
        else:
            data_type = socket_type_to_data_type(accessor._socket.type)
            value = accessor
        match sample_mode:
            case SampleMode.INDEX:
                return self.sample_index(
                    data_type=data_type,
                    domain=domain,
                    value=value,
                    index=sampling_index or geometry_script.index()
                )
            case SampleMode.NEAREST_SURFACE:
                return self.sample_nearest_surface(
                    data_type=data_type,
                    value=value,
                    sample_position=sample_position or geometry_script.position()
                )
            case SampleMode.NEAREST:
                return self.sample_index(
                    data_type=data_type,
                    value=value,
                    index=self.sample_nearest(domain=domain, sample_position=sample_position or geometry_script.position())
                )

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