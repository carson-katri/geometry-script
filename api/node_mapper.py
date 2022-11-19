import bpy
import bl_ui
import itertools
import enum
import re
from .state import State
from .types import *
from .static.input_group import InputGroup
from ..absolute_path import absolute_path

class OutputsList(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def build_node(node_type):
    def build(_primary_arg=None, **kwargs):
        for k, v in kwargs.items():
            if isinstance(v, InputGroup):
                kwargs = { **kwargs, **v.__dict__ }
                del kwargs[k]
        node = State.current_node_tree.nodes.new(node_type.__name__)
        if _primary_arg is not None:
            State.current_node_tree.links.new(_primary_arg._socket, node.inputs[0])
        for prop in node.bl_rna.properties:
            argname = prop.identifier.lower().replace(' ', '_')
            if argname in kwargs:
                value = kwargs[argname]
                if isinstance(value, enum.Enum):
                    value = value.value
                setattr(node, prop.identifier, value)
        for node_input in (node.inputs[1:] if _primary_arg is not None else node.inputs):
            argname = node_input.name.lower().replace(' ', '_')
            all_with_name = []
            for node_input2 in (node.inputs[1:] if _primary_arg is not None else node.inputs):
                if node_input2.name.lower().replace(' ', '_') == argname and node_input2.type == node_input.type:
                    all_with_name.append(node_input2)
            if argname in kwargs:
                def set_or_create_link(x, node_input):
                    if issubclass(type(x), Type):
                        State.current_node_tree.links.new(x._socket, node_input)
                    else:
                        try:
                            node_input.default_value = x
                        except:
                            constant = Type(value=x)
                            State.current_node_tree.links.new(constant._socket, node_input)
                value = kwargs[argname]
                if isinstance(value, enum.Enum):
                    value = value.value
                if node_input.is_multi_input and hasattr(value, '__iter__') and len(value) > 0 and issubclass(type(next(iter(value))), Type):
                    for x in value:
                        for node_input in all_with_name:
                            State.current_node_tree.links.new(x._socket, node_input)
                elif len(all_with_name) > 1 and issubclass(type(value), tuple) and len(value) > 0:
                    for i, x in enumerate(value):
                        set_or_create_link(x, all_with_name[i])
                else:
                    for node_input in all_with_name:
                        set_or_create_link(value, node_input)
        outputs = {}
        for node_output in node.outputs:
            if not node_output.enabled:
                continue
            outputs[node_output.name.lower().replace(' ', '_')] = Type(node_output)
        if len(outputs) == 1:
            return list(outputs.values())[0]
        else:
            return OutputsList(outputs)
    return build

documentation = {}
registered_nodes = set()
def register_node(node_type, category_path=None):
    if node_type in registered_nodes:
        return
    snake_case_name = node_type.bl_rna.name.lower().replace(' ', '_')
    node_namespace_name = snake_case_name.replace('_', ' ').title().replace(' ', '')
    globals()[snake_case_name] = build_node(node_type)
    globals()[snake_case_name].bl_category_path = category_path
    globals()[snake_case_name].bl_node_type = node_type
    documentation[snake_case_name] = globals()[snake_case_name]
    def build_node_method(node_type):
        def build(self, *args, **kwargs):
            return build_node(node_type)(self, *args, **kwargs)
        return build
    setattr(Type, snake_case_name, build_node_method(node_type))
    parent_props = [prop.identifier for base in node_type.__bases__ for prop in base.bl_rna.properties]
    for prop in node_type.bl_rna.properties:
        if not prop.identifier in parent_props and prop.type == 'ENUM':
            if node_namespace_name not in globals():
                class NodeNamespace: pass
                NodeNamespace.__name__ = node_namespace_name
                globals()[node_namespace_name] = NodeNamespace
            enum_type_name = prop.identifier.replace('_', ' ').title().replace(' ', '')
            enum_type = enum.Enum(enum_type_name, { map_case_name(i): i.identifier for i in prop.enum_items })
            setattr(globals()[node_namespace_name], enum_type_name, enum_type)
    registered_nodes.add(node_type)
for category_name in list(filter(lambda x: x.startswith('NODE_MT_category_GEO_'), dir(bpy.types))):
    category = getattr(bpy.types, category_name)
    if not hasattr(category, 'category'):
        category_path = category.bl_label.lower().replace(' ', '_')
        add_node_type = bl_ui.node_add_menu.add_node_type
        draw_node_group_add_menu = bl_ui.node_add_menu.draw_node_group_add_menu
        draw_assets_for_catalog = bl_ui.node_add_menu.draw_assets_for_catalog
        bl_ui.node_add_menu.add_node_type = lambda _layout, node_type_name: register_node(getattr(bpy.types, node_type_name), category_path)
        bl_ui.node_add_menu.draw_node_group_add_menu = lambda _context, _layout: None
        bl_ui.node_add_menu.draw_assets_for_catalog = lambda _context, _layout: None
        class CategoryStub:
            bl_label = ""
            def __init__(self):
                self.layout = Layout()
        class Layout:
            def separator(self): pass
        category.draw(CategoryStub(), None)
        bl_ui.node_add_menu.add_node_type = add_node_type
        bl_ui.node_add_menu.draw_node_group_add_menu = draw_node_group_add_menu
        bl_ui.node_add_menu.draw_assets_for_catalog = draw_assets_for_catalog
    else:
        category_path = category.category.name.lower().replace(' ', '_')
        for node in category.category.items(None):
            node_type = getattr(bpy.types, node.nodetype)
            register_node(node_type, category_path)
for node_type_name in list(filter(lambda x: 'GeometryNode' in x, dir(bpy.types))):
    node_type = getattr(bpy.types, node_type_name)
    if issubclass(node_type, bpy.types.GeometryNode):
        register_node(node_type)

def create_documentation():
    temp_node_group = bpy.data.node_groups.new('temp_node_group', 'GeometryNodeTree')
    color_mappings = {
        'INT': '#598C5C',
        'FLOAT': '#A1A1A1',
        'BOOLEAN': '#CCA6D6',
        'GEOMETRY': '#00D6A3',
        'VALUE': '#A1A1A1',
        'VECTOR': '#6363C7',
        'MATERIAL': '#EB7582',
        'TEXTURE': '#9E4FA3',
        'COLLECTION': '#F5F5F5',
        'OBJECT': '#ED9E5C',
        'STRING': '#70B2FF',
        'RGBA': '#C7C729',
    }
    default_color = '#A1A1A1'
    docstrings = []
    symbols = []
    enums = {}
    for func in sorted(documentation.keys()):
        try:
            method = documentation[func]
            link = f"https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/{method.bl_category_path}/{func}.html"
            image = f"https://docs.blender.org/manual/en/latest/_images/node-types_{method.bl_node_type.__name__}"
            node_instance = temp_node_group.nodes.new(method.bl_node_type.__name__)
            props_inputs = {}
            symbol_inputs = {}
            parent_props = [prop.identifier for base in method.bl_node_type.__bases__ for prop in base.bl_rna.properties]
            node_namespace_name = func.replace('_', ' ').title().replace(' ', '')
            for prop in method.bl_node_type.bl_rna.properties:
                if not prop.identifier in parent_props:
                    if prop.type == 'ENUM':
                        enum_name = prop.identifier.replace('_', ' ').title().replace(' ', '')
                        enum_cases = '\n    '.join(map(lambda i: f"{map_case_name(i)} = '{i.identifier}'", prop.enum_items))
                        if node_namespace_name not in enums:
                            enums[node_namespace_name] = []
                        enums[node_namespace_name].append(f"""  class {enum_name}(enum.Enum):
    {enum_cases}""")
                        props_inputs[prop.identifier] = {f"<span style=\"color: {color_mappings['STRING']};\">{node_namespace_name}.{enum_name}</span>":1}
                        symbol_inputs[prop.identifier] = {f"{node_namespace_name}.{enum_name}": 1}
                    else:
                        props_inputs[prop.identifier] = {f"<span style=\"color: {color_mappings.get(prop.type, default_color)};\">{prop.type.title()}</span>":1}
                        symbol_inputs[prop.identifier] = {prop.type.title(): 1}
            primary_arg = None
            for node_input in node_instance.inputs:
                name = node_input.name.lower().replace(' ', '_')
                typename = type(node_input).__name__.replace('NodeSocket', '')
                if node_input.is_multi_input:
                    typename = f"List[{typename}]"
                type_str = f"<span style=\"color: {color_mappings.get(node_input.type, default_color)};\">{typename}</span>"
                if name in props_inputs:
                    if type_str in props_inputs[name]:
                        props_inputs[name][type_str] += 1
                        symbol_inputs[name][typename] += 1
                    else:
                        props_inputs[name][type_str] = 1
                        symbol_inputs[name][typename] = 1
                else:
                    props_inputs[name] = {type_str: 1}
                    symbol_inputs[name] = {typename: 1}
                if primary_arg is None:
                    primary_arg = (name, list(props_inputs[name].keys())[0])
            def collapse_inputs(inputs):
                for k, v in inputs.items():
                    values = []
                    for t, c in v.items():
                        for c in range(1, c + 1):
                            value = ""
                            if c > 1:
                                value += "Tuple["
                            value += ', '.join(itertools.repeat(t, c))
                            if c > 1:
                                value += "]"
                            values.append(value)
                    inputs[k] = ' | '.join(values)
            collapse_inputs(props_inputs)
            collapse_inputs(symbol_inputs)
            arg_docs = []
            symbol_args = []
            for name, value in props_inputs.items():
                arg_docs.append(f"{name}: {value}")
                symbol_args.append(f"{name}: {symbol_inputs[name]} | None = None")
            outputs = {}
            symbol_outputs = {}
            for node_output in node_instance.outputs:
                output_name = node_output.name.lower().replace(' ', '_')
                output_type = type(node_output).__name__.replace('NodeSocket', '')
                outputs[output_name] = f"<span style=\"color: {color_mappings.get(node_output.type, default_color)};\">{output_type}</span>"
                symbol_outputs[output_name] = output_type
            output_docs = []
            output_symbols = []
            for name, value in outputs.items():
                output_docs.append(f"{name}: {value}")
                output_symbols.append(f"{name}: {symbol_outputs[name]}")
            outputs_doc = f"{{ {', '.join(output_docs)} }}" if len(output_docs) > 1 else ''.join(output_docs)
            arg_separator = ',\n  '
            def primary_arg_docs():
                return f"""
                <h4>Chain Syntax</h4>
                <pre><code>{primary_arg[0]}: {primary_arg[1]} = ...
{primary_arg[0]}.{func}(...)</code></pre>
                """
            docstrings.append(f"""
            <details style="margin: 10px 0;">
                <summary><code>{func}</code> - <a href="{link}">{method.bl_node_type.bl_rna.name}</a></summary>
                <div style="margin-top: 5px;">
                    <img src="{image}.webp" onerror="if (this.src != '{image}.png') this.src = '{image}.png'" />
                    <h4>Signature</h4>
                    <pre><code>{func}(
  {arg_separator.join(arg_docs)}
)</code></pre>
                    <h4>Result</h4>
                    <pre><code>{outputs_doc}</code></pre>
                    {primary_arg_docs() if primary_arg is not None else ""}
                </div>
            </details>
            """)
            output_symbol_separator = '\n    '
            if len(output_symbols) > 1:
                if node_namespace_name not in enums:
                    enums[node_namespace_name] = []
                enums[node_namespace_name].append(f"""  class Result:
    {output_symbol_separator.join(output_symbols)}""")
            return_type_hint = list(symbol_outputs.values())[0] if len(output_symbols) == 1 else f"{node_namespace_name}.Result"
            symbols.append(f"""def {func}({', '.join(symbol_args)}) -> {return_type_hint}: \"\"\"![]({image}.webp)\"\"\"""")
        except Exception as e:
            import os, sys
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            continue
    bpy.data.node_groups.remove(temp_node_group)
    html = f"""
    <html>
    <head>
    <style>
        html {{
            background-color: #1D1D1D;
            color: #FFFFFF;
        }}
        a {{
            color: #4772B3;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
            max-width: 60em;
            margin: 0 auto;
        }}
        pre {{
            overflow: scroll;
            padding: 16px;
            background-color: #303030;
            border-radius: 5px;
        }}
    </style>
    </head>
    <body>
    <h1>Geometry Script</h1>
    <h3>Nodes</h3>
    {''.join(docstrings)}
    </body>
    </html>
    """
    with open(absolute_path('docs/documentation.html'), 'w') as f:
        f.write(html)
    with open(absolute_path('typeshed/geometry_script.pyi'), 'w') as fpyi, open(absolute_path('typeshed/geometry_script.py'), 'w') as fpy:
        newline = '\n'
        def type_symbol(t):
            return f"class {t.__name__}(Type): pass"
        def enum_namespace(k):
            return f"""class {k}:
{newline.join(enums[k])}"""
        def add_self_arg(x):
            return re.sub('\(', '(self, ', x, 1)
        contents = f"""from typing import *
import enum
def tree(builder):
  \"\"\"
  Marks a function as a node tree.
  \"\"\"
  pass
class Type:
  def __add__(self, other) -> Type: return self
  def __radd__(self, other) -> Type: return self
  def __sub__(self, other) -> Type: return self
  def __rsub__(self, other) -> Type: return self
  def __mul__(self, other) -> Type: return self
  def __rmul__(self, other) -> Type: return self
  def __truediv__(self, other) -> Type: return self
  def __rtruediv__(self, other) -> Type: return self
  def __mod__(self, other) -> Type: return self
  def __rmod__(self, other) -> Type: return self
  def __eq__(self, other) -> Type: return self
  def __ne__(self, other) -> Type: return self
  def __lt__(self, other) -> Type: return self
  def __le__(self, other) -> Type: return self
  def __gt__(self, other) -> Type: return self
  def __ge__(self, other) -> Type: return self
  x = Type()
  y = Type()
  z = Type()
  def capture(self, attribute: Type, **kwargs) -> Callable[[], Type]: return transfer_attribute
  {(newline + '  ').join(map(add_self_arg, filter(lambda x: x.startswith('def'), symbols)))}
  
{newline.join(map(type_symbol, Type.__subclasses__()))}
{newline.join(map(enum_namespace, enums.keys()))}
{newline.join(symbols)}"""

        static_path = absolute_path('api/static')
        for path in os.listdir(static_path):
            if os.path.splitext(path)[-1] != '.py':
                continue
            with open(os.path.join(static_path, path), 'r') as static_api:
                contents += f"\n\n# {path}\n{static_api.read()}"

        fpyi.write(contents)
        fpy.write(contents)

def create_docs():
    create_documentation()
bpy.app.timers.register(create_docs)