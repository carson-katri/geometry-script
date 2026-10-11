"""Build representative trees with the generated API in the running Blender.

    blender -b --factory-startup --python-exit-code 1 --python tests/smoke_test.py
"""

import importlib.util
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "geometry_script", root / "__init__.py", submodule_search_locations=[str(root)]
)
assert spec is not None and spec.loader is not None
geometry_script = importlib.util.module_from_spec(spec)
sys.modules["geometry_script"] = geometry_script
spec.loader.exec_module(geometry_script)

import bpy

from geometry_script import *


@tree("Repeat Grid")
def repeat_grid(geometry: Geometry, columns: int = 3, rows: int = 3):
    mesh = grid(vertices_x=columns, vertices_y=rows).mesh
    points = mesh_to_points(mesh=mesh).points
    return instance_on_points(points=points, instance=geometry).instances


@tree("Nested")
def nested(geometry: Geometry):
    return repeat_grid(repeat_grid(geometry))


@repeat_zone
def climb(geometry: Geometry, step: float, iteration: int):
    moved = set_position(geometry=geometry, offset=(0.0, 0.0, 1.0)).geometry
    return moved, step * 2.0


@tree("Climb")
def climb_tree(geometry: Geometry):
    return climb(geometry, 1.0, iterations=4).geometry


@simulation_zone
def fall(geometry: Geometry, delta_time: float):
    return set_position(geometry=geometry, offset=(0.0, 0.0, -1.0)).geometry


@tree("Fall")
def fall_tree(geometry: Geometry):
    return fall(geometry)


@closure_zone
def scale(x: float, factor: float = 2.0):
    return x * factor


@tree("Closure")
def closure_tree(value: float):
    return scale.evaluate(scale(), value, 3.0)


def node_setting(tree_name: str, node_type_id: str, identifier: str) -> str:
    node = next(
        node
        for node in bpy.data.node_groups[tree_name].nodes
        if node.bl_idname == node_type_id
    )
    return getattr(node, identifier)


@tree("Inferred Switch")
def inferred_switch(a: Geometry, b: Geometry, condition: bool):
    return switch(switch=condition, false=a, true=b).output


assert node_setting("Inferred Switch", "GeometryNodeSwitch", "input_type") == "GEOMETRY"


@tree("Inferred Types")
def inferred_types(geometry: Geometry):
    position_field = position().position
    is_above = compare(a=position_field, b=(0.0, 0.0, 1.0), operation="GREATER_THAN").result
    stored = store_named_attribute(geometry=geometry, name="offset", value=position_field)
    jitter = random_value(min=(-1.0, -1.0, -1.0), max=(1.0, 1.0, 1.0)).value
    moved = set_position(geometry=stored.geometry, selection=is_above, offset=jitter)
    return moved.geometry


assert node_setting("Inferred Types", "FunctionNodeCompare", "data_type") == "VECTOR"
assert node_setting("Inferred Types", "GeometryNodeStoreNamedAttribute", "data_type") == "FLOAT_VECTOR"
assert node_setting("Inferred Types", "FunctionNodeRandomValue", "data_type") == "FLOAT_VECTOR"


@tree("Explicit Type")
def explicit_type(seed: int):
    return random_value(seed=seed, probability=0.25, data_type="BOOLEAN").value


assert node_setting("Explicit Type", "FunctionNodeRandomValue", "data_type") == "BOOLEAN"

@tree("Items")
def items_tree(a: Geometry, b: Geometry, choice: int, label: str):
    captured = capture_attribute(
        geometry=a, domain="POINT", normal=normal().normal, height=position().position
    )
    picked = index_switch(index=choice, items=[captured.geometry, b]).output
    menu = menu_switch(menu="High", items={"Low": a, "High": picked}).output
    bundle = combine_bundle(height=captured.height, mesh=menu).bundle
    unpacked = separate_bundle(bundle=bundle, items={"height": Vector, "mesh": Geometry})
    text = format_string(format="{name}: {count}", name=label, count=choice).string
    moved = set_position(geometry=unpacked.mesh, offset=unpacked.height)
    return {"Geometry": moved.geometry, "Text": text, "Normal": captured.normal}


assert node_setting("Items", "GeometryNodeIndexSwitch", "data_type") == "GEOMETRY"
assert node_setting("Items", "GeometryNodeMenuSwitch", "data_type") == "GEOMETRY"
items_nodes = {node.bl_idname: node for node in bpy.data.node_groups["Items"].nodes}
assert [item.name for item in items_nodes["GeometryNodeCaptureAttribute"].capture_items] == ["normal", "height"]
assert [item.name for item in items_nodes["GeometryNodeMenuSwitch"].enum_items] == ["Low", "High"]
assert [item.socket_type for item in items_nodes["NodeSeparateBundle"].bundle_items] == ["VECTOR", "GEOMETRY"]


@for_each_element(domain="POINT")
def scatter(index: int, radius: float):
    ball = uv_sphere(radius=radius).mesh
    return ForEachResult(
        main={"scale": radius * 2.0},
        generated=[{"geometry": ball, "id": index}],
    )


@tree("For Each")
def for_each_tree(geometry: Geometry):
    points = mesh_to_points(mesh=grid(vertices_x=2, vertices_y=2).mesh).points
    out = scatter(points, radius=0.25)
    return {"Balls": out.generated.geometry, "Points": out.main.geometry, "Scale": out.main.scale}


@tree("Type Markers")
def type_markers(
    a: Geometry,
    b: Geometry,
    offset: Vector = (0.0, 0.0, 1.0),
    tint: Color = (1.0, 0.0, 0.0, 1.0),
    uv: Field[Vector2] = (0.5, 0.5),
    density: Grid[float] = 0.0,
    mode: Menu = "High",
):
    picked = menu_switch(menu=mode, items={"Low": a, "High": b}).output
    moved = set_position(geometry=picked, offset=offset).geometry
    return {"Geometry": moved, "Tint": tint, "UV": uv, "Density": density, "Pair": (1.0, 2.0)}


marker_sockets = {
    (item.in_out, item.name): item
    for item in bpy.data.node_groups["Type Markers"].interface.items_tree
}
assert [
    (marker_sockets["INPUT", name].bl_socket_idname, marker_sockets["INPUT", name].structure_type)
    for name in ("Offset", "Tint", "Uv", "Density", "Mode")
] == [
    ("NodeSocketVector", "AUTO"),
    ("NodeSocketColor", "AUTO"),
    ("NodeSocketVector2D", "FIELD"),
    ("NodeSocketFloat", "GRID"),
    ("NodeSocketMenu", "AUTO"),
]
assert tuple(marker_sockets["INPUT", "Uv"].default_value) == (0.5, 0.5)
assert marker_sockets["INPUT", "Mode"].default_value == "High"
assert marker_sockets["OUTPUT", "Pair"].bl_socket_idname == "NodeSocketVector2D"


@repeat_zone
def drift(position: Vector, iteration: int):
    return position + (1.0, 0.0, 0.0)


@tree("Vector Zone")
def vector_zone(geometry: Geometry):
    return set_position(geometry=geometry, offset=drift((0.0, 0.0, 0.0), iterations=2)).geometry


try:
    @tree("Bad Socket Type")
    def bad_socket_type(shader: Shader):
        return shader
except TypeError as error:
    assert "cannot have Shader inputs" in str(error), error
else:
    raise AssertionError("Shader inputs should be rejected.")

bpy.ops.mesh.primitive_cube_add()
balls =bpy.context.active_object
balls.modifiers.new("Geometry Script", "NODES").node_group = bpy.data.node_groups["For Each"]
balls_mesh = balls.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
# 4 points, one UV sphere (32 x 16 segments: 482 vertices) each.
assert len(balls_mesh.vertices) == 4 * 482, len(balls_mesh.vertices)

try:
    @tree("Bad Link")
    def bad_link(a: Geometry, b: float):
        return set_position(geometry=b, offset=a).geometry
except TypeError:
    pass
else:
    raise AssertionError("Linking Geometry into a Vector input should fail.")

bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object
modifier = cube.modifiers.new("Geometry Script", "NODES")
modifier.node_group = bpy.data.node_groups["Climb"]
evaluated = cube.evaluated_get(bpy.context.evaluated_depsgraph_get())
heights = [vertex.co.z for vertex in evaluated.data.vertices]
assert (min(heights), max(heights)) == (3.0, 5.0), heights

# Outputs a node lacks with its settings raise when used instead of linking nothing.
try:
    @tree("Missing Output")
    def missing_output(geometry: Geometry, a: Vector):
        dot = vector_math(operation="DOT_PRODUCT", vector=a, vector_2=a)
        return set_position(geometry=geometry, offset=dot.vector).geometry
except TypeError as error:
    assert "no 'vector' output" in str(error) and "'value'" in str(error), error
else:
    raise AssertionError("Using a missing output should fail.")
assert "Missing Output" not in bpy.data.node_groups, "A failed build left a tree behind."

try:
    @tree("Unknown Output")
    def unknown_output(geometry: Geometry):
        return mesh_to_points(mesh=geometry).geometry
except AttributeError as error:
    assert "available: ['points']" in str(error), error
else:
    raise AssertionError("Unknown outputs should fail.")

try:
    @tree("Bad Enum")
    def bad_enum(geometry: Geometry):
        return mesh_to_points(mesh=geometry, mode="VERTEX").points
except TypeError as error:
    assert "Did you mean 'VERTICES'?" in str(error), error
else:
    raise AssertionError("Unknown enum values should fail.")

@tree("Socket Tuple")
def socket_tuple(geometry: Geometry, height: float = 2.0):
    return set_position(geometry=geometry, offset=(0.0, 0.0, height)).geometry

assert "ShaderNodeCombineXYZ" in {
    node.bl_idname for node in bpy.data.node_groups["Socket Tuple"].nodes
}

# A failed rebuild keeps the previous tree, and modifiers keep their input values.
height_modifier = cube.modifiers.new("Socket Tuple", "NODES")
height_modifier.node_group = bpy.data.node_groups["Socket Tuple"]


def height_value() -> float:
    node_tree = height_modifier.node_group
    identifier = node_tree.interface.items_tree["Height"].identifier
    return getattr(height_modifier.properties.inputs, identifier).value


getattr(
    height_modifier.properties.inputs,
    height_modifier.node_group.interface.items_tree["Height"].identifier,
).value = 5.0
try:
    @tree("Socket Tuple")
    def socket_tuple(geometry: Geometry, height: float = 2.0):
        return mesh_to_points(mesh=geometry).geometry
except AttributeError:
    pass
assert height_modifier.node_group.name == "Socket Tuple"
assert "ShaderNodeCombineXYZ" in {node.bl_idname for node in height_modifier.node_group.nodes}
assert height_value() == 5.0, height_value()

@tree("Socket Tuple")
def socket_tuple(geometry: Geometry, height: float = 2.0):
    return set_position(geometry=geometry, offset=(0.0, 0.0, height)).geometry

assert height_value() == 5.0, height_value()

@tree("Math Alias")
def math_alias(value: float):
    return math(value=value, value_2=math.pi, operation="MULTIPLY").value

print("Smoke test passed.")
