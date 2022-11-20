def scripted_expression(scripted_expression: str) -> 'Type':
    from geometry_script import Type, State
    value_node = State.current_node_tree.nodes.new('ShaderNodeValue')
    fcurve = value_node.outputs[0].driver_add("default_value")
    fcurve.driver.expression = scripted_expression
    return Type(value_node.outputs[0])