import bpy
from .state import State
from .types import Type

class OutputsList(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def build_node(node_type):
    def build(_primary_arg=None, **kwargs):
        node = State.current_node_tree.nodes.new(node_type.__name__)
        if _primary_arg is not None:
            State.current_node_tree.links.new(_primary_arg._socket, node.inputs[0])
        for prop in node.bl_rna.properties:
            argname = prop.name.lower().replace(' ', '_')
            if argname in kwargs:
                setattr(node, prop.identifier, kwargs[argname])
        for node_input in (node.inputs[1:] if _primary_arg is not None else node.inputs):
            argname = node_input.name.lower().replace(' ', '_')
            if argname in kwargs:
                if node_input.is_multi_input and hasattr(kwargs[argname], '__iter__') and len(kwargs[argname]) > 0 and issubclass(type(next(iter(kwargs[argname]))), Type):
                    for x in kwargs[argname]:
                        State.current_node_tree.links.new(x._socket, node_input)
                elif issubclass(type(kwargs[argname]), Type):
                    State.current_node_tree.links.new(kwargs[argname]._socket, node_input)
                else:
                    try:
                        node_input.default_value = kwargs[argname]
                    except:
                        constant = Type(value=kwargs[argname])
                        State.current_node_tree.links.new(constant._socket, node_input)
        outputs = {}
        for node_output in node.outputs:
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
    globals()[snake_case_name] = build_node(node_type)
    globals()[snake_case_name].bl_category_path = category_path
    globals()[snake_case_name].bl_node_type = node_type
    documentation[snake_case_name] = globals()[snake_case_name]
    def build_node_method(node_type):
        def build(self, *args, **kwargs):
            return build_node(node_type)(self, *args, **kwargs)
        return build
    setattr(Type, snake_case_name, build_node_method(node_type))
    registered_nodes.add(node_type)
for category_name in list(filter(lambda x: x.startswith('NODE_MT_category_GEO_'), dir(bpy.types))):
    category = getattr(bpy.types, category_name)
    category_path = category.category.name.lower().replace(' ', '_')
    for node in category.category.items(None):
        node_type = getattr(bpy.types, node.nodetype)
        register_node(node_type, category_path)
for node_type in bpy.types.GeometryNode.__subclasses__():
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
    for func in sorted(documentation.keys()):
        method = documentation[func]
        link = f"https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/{method.bl_category_path}/{func}.html"
        image = f"https://docs.blender.org/manual/en/latest/_images/node-types_{method.bl_node_type.__name__}"
        node_instance = temp_node_group.nodes.new(method.bl_node_type.__name__)
        props_inputs = {}
        symbol_inputs = {}
        parent_props = [prop.identifier for base in method.bl_node_type.__bases__ for prop in base.bl_rna.properties]
        for prop in method.bl_node_type.bl_rna.properties:
            if not prop.identifier in parent_props:
                if prop.type == 'ENUM':
                    enum_items = 'Literal[' + ', '.join(map(lambda i: f"'{i.identifier}'", prop.enum_items)) + ']'
                    props_inputs[prop.identifier] = f"<span style=\"color: {color_mappings['STRING']};\">{enum_items}</span>"
                    symbol_inputs[prop.identifier] = enum_items
                else:
                    props_inputs[prop.identifier] = f"<span style=\"color: {color_mappings.get(prop.type, default_color)};\">{prop.type.title()}</span>"
                    symbol_inputs[prop.identifier] = prop.type.title()
        primary_arg = None
        for node_input in node_instance.inputs:
            name = node_input.name.lower().replace(' ', '_')
            typename = type(node_input).__name__.replace('NodeSocket', '')
            if node_input.is_multi_input:
                typename = f"List[{typename}]"
            type_str = f"<span style=\"color: {color_mappings.get(node_input.type, default_color)};\">{typename}</span>"
            if name in props_inputs:
                props_inputs[name] = props_inputs[name] + f' | {type_str}'
                symbol_inputs[name] = symbol_inputs[name] + f' | {typename}'
            else:
                props_inputs[name] = type_str
                symbol_inputs[name] = typename
            if primary_arg is None:
                primary_arg = (name, props_inputs[name])
        arg_docs = []
        symbol_args = []
        for name, value in props_inputs.items():
            arg_docs.append(f"{name}: {value}")
            symbol_args.append(f"{name}: {symbol_inputs[name]}")
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
        output_symbol_separator = '\n  '
        symbol_return_type = f"_{func}_result"
        if len(output_symbols) > 1:
            symbols.append(f"""class {symbol_return_type}:
  {output_symbol_separator.join(output_symbols)}""")
        symbols.append(f"""def {func}({', '.join(symbol_args)}) -> {list(symbol_outputs.values())[0] if len(output_symbols) == 1 else symbol_return_type}: pass""")
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
    with open('documentation.html', 'w') as f:
        f.write(html)
    with open('geometry_script.py', 'w') as f:
        newline = '\n'
        def type_symbol(t):
            return f"class {t.__name__}: pass"
        f.write(f"""from typing import *
{newline.join(map(type_symbol, Type.__subclasses__()))}
{newline.join(symbols)}""")

def create_docs():
    create_documentation()
bpy.app.timers.register(create_docs)