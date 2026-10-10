# Generated from Blender 5.2.0 LTS (GeometryNodeTree).
# Do not edit: run code_generator/node_functions_generator.py instead.

from __future__ import annotations

import typing

import bpy

from .runtime import ItemOutputs, Socket, node_function as _node_function
from .types import *

BLENDER_VERSION = (5, 2, 0)

__all__ = [
    'accumulate_field',
    'active_camera',
    'active_element',
    'advect_grid',
    'align_euler_to_vector',
    'align_rotation_to_vector',
    'arc',
    'attribute_statistic',
    'axes_to_rotation',
    'axis_angle_to_rotation',
    'b_zier_segment',
    'bake',
    'bit_math',
    'blackbody',
    'blur_attribute',
    'bone_info',
    'boolean',
    'boolean_math',
    'bounding_box',
    'brick_texture',
    'camera_info',
    'capture_attribute',
    'checker_texture',
    'clamp',
    'clip_grid',
    'closure_to_list',
    'cluster_by_connected',
    'cluster_by_distance',
    'collection',
    'collection_children',
    'collection_info',
    'color',
    'color_ramp',
    'combine_bundle',
    'combine_color',
    'combine_matrix',
    'combine_transform',
    'combine_xyz',
    'compare',
    'cone',
    'convex_hull',
    'corners_of_edge',
    'corners_of_face',
    'corners_of_vertex',
    'cube',
    'cube_grid_topology',
    'curve_circle',
    'curve_handle_positions',
    'curve_length',
    'curve_line',
    'curve_of_point',
    'curve_tangent',
    'curve_tilt',
    'curve_to_mesh',
    'curve_to_points',
    'curves_to_grease_pencil',
    'cylinder',
    'deform_curves_on_surface',
    'delete_geometry',
    'dial_gizmo',
    'distribute_points_in_grid',
    'distribute_points_in_volume',
    'distribute_points_on_faces',
    'domain_size',
    'dual_mesh',
    'duplicate_elements',
    'edge_angle',
    'edge_neighbors',
    'edge_paths_to_curves',
    'edge_paths_to_selection',
    'edge_vertices',
    'edges_of_corner',
    'edges_of_vertex',
    'edges_to_face_groups',
    'enable_output',
    'endpoint_selection',
    'euler_to_rotation',
    'evaluate_at_index',
    'evaluate_closure',
    'evaluate_on_domain',
    'extrude_mesh',
    'face_area',
    'face_group_boundaries',
    'face_neighbors',
    'face_of_corner',
    'face_set',
    'field_average',
    'field_min_max',
    'field_to_grid',
    'field_to_list',
    'field_variance',
    'fill_curve',
    'fillet_curve',
    'filter_list',
    'find_in_string',
    'flip_faces',
    'float_curve',
    'float_to_integer',
    'font',
    'format_string',
    'gabor_texture',
    'gamma',
    'geometry_proximity',
    'geometry_to_instance',
    'get_attribute_names',
    'get_bundle_item',
    'get_geometry_bundle',
    'get_geometry_component',
    'get_list_item',
    'get_named_grid',
    'get_nested_bundle_paths',
    'gradient_texture',
    'grease_pencil_to_curves',
    'grid',
    'grid_curl',
    'grid_dilate_erode',
    'grid_divergence',
    'grid_gradient',
    'grid_info',
    'grid_laplacian',
    'grid_mean',
    'grid_median',
    'grid_to_mesh',
    'grid_to_points',
    'handle_type_selection',
    'hash_value',
    'ico_sphere',
    'id_',
    'image',
    'image_info',
    'image_texture',
    'import_csv',
    'import_obj',
    'import_ply',
    'import_stl',
    'import_text',
    'import_vdb',
    'index',
    'index_of_nearest',
    'index_switch',
    'instance_bounds',
    'instance_on_points',
    'instance_reference',
    'instance_rotation',
    'instance_scale',
    'instance_transform',
    'instances_to_points',
    'integer',
    'integer_math',
    'integer_vector',
    'interpolate_curves',
    'invert_matrix',
    'invert_rotation',
    'is_edge_smooth',
    'is_face_planar',
    'is_face_smooth',
    'is_spline_cyclic',
    'is_viewport',
    'join_bundle',
    'join_geometry',
    'join_strings',
    'linear_gizmo',
    'list_length',
    'magic_texture',
    'map_range',
    'match_string',
    'material',
    'material_index',
    'material_selection',
    'math_',
    'matrix_determinant',
    'matrix_svd',
    'menu',
    'menu_switch',
    'merge_by_distance',
    'merge_layers',
    'merge_points',
    'mesh_bevel',
    'mesh_boolean',
    'mesh_circle',
    'mesh_island',
    'mesh_line',
    'mesh_to_curve',
    'mesh_to_density_grid',
    'mesh_to_points',
    'mesh_to_sdf_grid',
    'mesh_to_volume',
    'mix',
    'mix_legacy',
    'mouse_position',
    'multiply_matrices',
    'named_attribute',
    'named_layer_selection',
    'node_3_d_cursor',
    'noise_texture',
    'normal',
    'object_',
    'object_info',
    'offset_corner_in_face',
    'offset_point_in_curve',
    'pack_uv_islands',
    'points',
    'points_of_curve',
    'points_to_curves',
    'points_to_sdf_grid',
    'points_to_vertices',
    'points_to_volume',
    'position',
    'project_point',
    'prune_grid',
    'quadratic_b_zier',
    'quadrilateral',
    'quaternion_to_rotation',
    'radial_tiling',
    'radius',
    'random_value',
    'raycast',
    'realize_instances',
    'remove_named_attribute',
    'rename_attribute',
    'replace_material',
    'replace_string',
    'resample_curve',
    'reverse_curve',
    'reverse_string',
    'rgb_curves',
    'rotate_euler',
    'rotate_instances',
    'rotate_rotation',
    'rotate_vector',
    'rotation',
    'rotation_to_axis_angle',
    'rotation_to_euler',
    'rotation_to_quaternion',
    'sample_curve',
    'sample_grid',
    'sample_grid_index',
    'sample_index',
    'sample_nearest',
    'sample_nearest_surface',
    'sample_sound_frequencies',
    'sample_uv_surface',
    'scale_elements',
    'scale_instances',
    'scene_time',
    'sdf_grid_boolean',
    'sdf_grid_fillet',
    'sdf_grid_laplacian',
    'sdf_grid_mean',
    'sdf_grid_mean_curvature',
    'sdf_grid_median',
    'sdf_grid_offset',
    'selection',
    'self_object',
    'separate_bundle',
    'separate_color',
    'separate_components',
    'separate_geometry',
    'separate_matrix',
    'separate_transform',
    'separate_xyz',
    'set_curve_normal',
    'set_curve_radius',
    'set_curve_tilt',
    'set_face_set',
    'set_geometry_bundle',
    'set_geometry_name',
    'set_grease_pencil_color',
    'set_grease_pencil_depth',
    'set_grease_pencil_softness',
    'set_grid_background',
    'set_grid_transform',
    'set_handle_positions',
    'set_handle_type',
    'set_id',
    'set_instance_transform',
    'set_material',
    'set_material_index',
    'set_mesh_normal',
    'set_nurbs_order',
    'set_nurbs_weight',
    'set_point_radius',
    'set_position',
    'set_selection',
    'set_shade_smooth',
    'set_spline_cyclic',
    'set_spline_resolution',
    'set_spline_type',
    'set_string_case',
    'shortest_edge_paths',
    'slice_string',
    'sort_elements',
    'sort_list',
    'special_characters',
    'spiral',
    'spline_length',
    'spline_parameter',
    'spline_resolution',
    'split_edges',
    'split_string',
    'split_to_instances',
    'star',
    'store_bundle_item',
    'store_named_attribute',
    'store_named_grid',
    'string_',
    'string_length',
    'string_to_curves',
    'string_to_value',
    'subdivide_curve',
    'subdivide_mesh',
    'subdivision_surface',
    'switch',
    'tag_filter',
    'transfer_attributes',
    'transform_direction',
    'transform_geometry',
    'transform_gizmo',
    'transform_point',
    'translate_instances',
    'transpose_matrix',
    'triangulate',
    'trim_curve',
    'trim_string',
    'uv_sphere',
    'uv_tangent',
    'uv_unwrap',
    'value',
    'value_to_string',
    'vector',
    'vector_curves',
    'vector_math',
    'vector_rotate',
    'vertex_neighbors',
    'vertex_of_corner',
    'viewer',
    'viewport_transform',
    'volume_cube',
    'volume_to_mesh',
    'voronoi_texture',
    'voxel_index',
    'voxelize_grid',
    'warning',
    'wave_texture',
    'white_noise_texture',
    'xpbd_solver',
]

class GeometryNodeAccumulateFieldOutputs(typing.NamedTuple):
    leading: Socket[Field[float] | Field[int] | Field[Vector] | Field[Matrix]]
    trailing: Socket[Field[float] | Field[int] | Field[Vector] | Field[Matrix]]
    total: Socket[Field[float] | Field[int] | Field[Vector] | Field[Matrix]]

def accumulate_field(*, value: float | Field[float] | int | Field[int] | Vector | Field[Vector] | Matrix | Field[Matrix] | Socket[float | Field[float] | int | Field[int] | Vector | Field[Vector] | Matrix | Field[Matrix]] = 1.0, group_id: int | Field[int] | Socket[int | Field[int]] = 0, data_type: typing.Literal['FLOAT', 'INT', 'FLOAT_VECTOR', 'TRANSFORM'] | None = None, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT') -> GeometryNodeAccumulateFieldOutputs:
    'Args:\n    data_type: Type of data that is accumulated Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeAccumulateField',
        inputs={
            'value': value,
            'group_id': group_id,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 1.0),
            'group_id': ('Group Index', 'Group ID', 1, 0),
        },
        properties={
            'data_type': data_type,
            'domain': domain,
        },
        output_sockets={
            'leading': ('Leading', 'Leading', 0, 'FIELD'),
            'trailing': ('Trailing', 'Trailing', 1, 'FIELD'),
            'total': ('Total', 'Total', 2, 'FIELD'),
        },
        output_type=GeometryNodeAccumulateFieldOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}, 'TRANSFORM': {'value': 'MATRIX'}}},
    )

class GeometryNodeInputActiveCameraOutputs(typing.NamedTuple):
    active_camera: Socket[Object]

def active_camera() -> GeometryNodeInputActiveCameraOutputs:
    return _node_function(
        'GeometryNodeInputActiveCamera',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'active_camera': ('Active Camera', 'Active Camera', 0, 'AUTO'),
        },
        output_type=GeometryNodeInputActiveCameraOutputs,
    )

class GeometryNodeToolActiveElementOutputs(typing.NamedTuple):
    index: Socket[int]
    exists: Socket[bool]

def active_element(*, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'LAYER'] = 'POINT') -> GeometryNodeToolActiveElementOutputs:
    return _node_function(
        'GeometryNodeToolActiveElement',
        inputs={
        },
        input_sockets={
        },
        properties={
            'domain': domain,
        },
        output_sockets={
            'index': ('Index', 'Index', 0, 'AUTO'),
            'exists': ('Exists', 'Exists', 1, 'AUTO'),
        },
        output_type=GeometryNodeToolActiveElementOutputs,
    )

class GeometryNodeGridAdvectOutputs(typing.NamedTuple):
    grid: Socket[Grid[float] | Grid[int] | Grid[Vector]]

def advect_grid(*, grid: Grid[float] | Grid[int] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[Vector]] | None = None, velocity: Grid[Vector] | Socket[Grid[Vector]] | None = None, time_step: float | Socket[float] = 1.0, integration_scheme: Menu | Socket[Menu] = 'Runge-Kutta 3', limiter: Menu | Socket[Menu] = 'Clamp', data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeGridAdvectOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeGridAdvect',
        inputs={
            'grid': grid,
            'velocity': velocity,
            'time_step': time_step,
            'integration_scheme': integration_scheme,
            'limiter': limiter,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'velocity': ('Velocity', 'Velocity', 1, None),
            'time_step': ('Time Step', 'Time Step', 2, 1.0),
            'integration_scheme': ('Integration Scheme', 'Integration Scheme', 3, 'Runge-Kutta 3'),
            'limiter': ('Limiter', 'Limiter', 4, 'Clamp'),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeGridAdvectOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class FunctionNodeAlignEulerToVectorOutputs(typing.NamedTuple):
    rotation: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def align_euler_to_vector(*, rotation: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), factor: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 1.0), axis: typing.Literal['X', 'Y', 'Z'] = 'X', pivot_axis: typing.Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO') -> FunctionNodeAlignEulerToVectorOutputs:
    'Args:\n    axis: Axis to align to the vector\n    pivot_axis: Axis to rotate around'
    return _node_function(
        'FunctionNodeAlignEulerToVector',
        inputs={
            'rotation': rotation,
            'factor': factor,
            'vector': vector,
        },
        input_sockets={
            'rotation': ('Rotation', 'Rotation', 0, (0.0, 0.0, 0.0)),
            'factor': ('Factor', 'Factor', 1, 1.0),
            'vector': ('Vector', 'Vector', 2, (0.0, 0.0, 1.0)),
        },
        properties={
            'axis': axis,
            'pivot_axis': pivot_axis,
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'AUTO'),
        },
        output_type=FunctionNodeAlignEulerToVectorOutputs,
    )

class FunctionNodeAlignRotationToVectorOutputs(typing.NamedTuple):
    rotation: Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]]

def align_rotation_to_vector(*, rotation: Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = (0.0, 0.0, 0.0), factor: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 1.0), axis: typing.Literal['X', 'Y', 'Z'] = 'Z', pivot_axis: typing.Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO') -> FunctionNodeAlignRotationToVectorOutputs:
    'Args:\n    axis: Axis to align to the vector\n    pivot_axis: Axis to rotate around'
    return _node_function(
        'FunctionNodeAlignRotationToVector',
        inputs={
            'rotation': rotation,
            'factor': factor,
            'vector': vector,
        },
        input_sockets={
            'rotation': ('Rotation', 'Rotation', 0, (0.0, 0.0, 0.0)),
            'factor': ('Factor', 'Factor', 1, 1.0),
            'vector': ('Vector', 'Vector', 2, (0.0, 0.0, 1.0)),
        },
        properties={
            'axis': axis,
            'pivot_axis': pivot_axis,
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'AUTO'),
        },
        output_type=FunctionNodeAlignRotationToVectorOutputs,
    )

class GeometryNodeCurveArcOutputs(typing.NamedTuple):
    curve: Socket[Geometry]
    center: Socket[Vector]
    normal: Socket[Vector]
    radius: Socket[float]

def arc(*, resolution: int | Socket[int] = 16, radius: float | Socket[float] = 1.0, start_angle: float | Socket[float] = 0.0, sweep_angle: float | Socket[float] = 5.497786998748779, connect_center: bool | Socket[bool] = False, invert_arc: bool | Socket[bool] = False, start: Vector | Socket[Vector] = (-1.0, 0.0, 0.0), middle: Vector | Socket[Vector] = (0.0, 2.0, 0.0), end: Vector | Socket[Vector] = (1.0, 0.0, 0.0), offset_angle: float | Socket[float] = 0.0, mode: typing.Literal['POINTS', 'RADIUS'] = 'RADIUS') -> GeometryNodeCurveArcOutputs:
    'Args:\n    mode: Method used to determine radius and placement'
    return _node_function(
        'GeometryNodeCurveArc',
        inputs={
            'resolution': resolution,
            'radius': radius,
            'start_angle': start_angle,
            'sweep_angle': sweep_angle,
            'connect_center': connect_center,
            'invert_arc': invert_arc,
            'start': start,
            'middle': middle,
            'end': end,
            'offset_angle': offset_angle,
        },
        input_sockets={
            'resolution': ('Resolution', 'Resolution', 0, 16),
            'radius': ('Radius', 'Radius', 4, 1.0),
            'start_angle': ('Start Angle', 'Start Angle', 5, 0.0),
            'sweep_angle': ('Sweep Angle', 'Sweep Angle', 6, 5.497786998748779),
            'connect_center': ('Connect Center', 'Connect Center', 8, False),
            'invert_arc': ('Invert Arc', 'Invert Arc', 9, False),
            'start': ('Start', 'Start', 1, (-1.0, 0.0, 0.0)),
            'middle': ('Middle', 'Middle', 2, (0.0, 2.0, 0.0)),
            'end': ('End', 'End', 3, (1.0, 0.0, 0.0)),
            'offset_angle': ('Offset Angle', 'Offset Angle', 7, 0.0),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
            'center': ('Center', 'Center', 1, 'AUTO'),
            'normal': ('Normal', 'Normal', 2, 'AUTO'),
            'radius': ('Radius', 'Radius', 3, 'AUTO'),
        },
        output_type=GeometryNodeCurveArcOutputs,
    )

class GeometryNodeAttributeStatisticOutputs(typing.NamedTuple):
    mean: Socket[float | Vector]
    median: Socket[float | Vector]
    sum: Socket[float | Vector]
    min: Socket[float | Vector]
    max: Socket[float | Vector]
    range: Socket[float | Vector]
    standard_deviation: Socket[float | Vector]
    variance: Socket[float | Vector]

def attribute_statistic(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, attribute: float | Field[float] | Vector | Field[Vector] | Socket[float | Field[float] | Vector | Field[Vector]] = 0.0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT') -> GeometryNodeAttributeStatisticOutputs:
    'Args:\n    data_type: The data type the attribute is converted to before calculating the results Inferred from the linked inputs when None.\n    domain: Which domain to read the data from'
    return _node_function(
        'GeometryNodeAttributeStatistic',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'attribute': attribute,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'attribute': ('Attribute', 'Attribute', 2, 0.0),
        },
        properties={
            'data_type': data_type,
            'domain': domain,
        },
        output_sockets={
            'mean': ('Mean', 'Mean', 0, 'AUTO'),
            'median': ('Median', 'Median', 1, 'AUTO'),
            'sum': ('Sum', 'Sum', 2, 'AUTO'),
            'min': ('Min', 'Min', 3, 'AUTO'),
            'max': ('Max', 'Max', 4, 'AUTO'),
            'range': ('Range', 'Range', 5, 'AUTO'),
            'standard_deviation': ('Standard Deviation', 'Standard Deviation', 6, 'AUTO'),
            'variance': ('Variance', 'Variance', 7, 'AUTO'),
        },
        output_type=GeometryNodeAttributeStatisticOutputs,
        type_properties={'data_type': {'FLOAT': {'attribute': 'VALUE'}, 'FLOAT_VECTOR': {'attribute': 'VECTOR'}}},
    )

class FunctionNodeAxesToRotationOutputs(typing.NamedTuple):
    rotation: Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]]

def axes_to_rotation(*, primary_axis: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 1.0), secondary_axis: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (1.0, 0.0, 0.0), primary_axis_property: typing.Literal['X', 'Y', 'Z'] = 'Z', secondary_axis_property: typing.Literal['X', 'Y', 'Z'] = 'X') -> FunctionNodeAxesToRotationOutputs:
    'Args:\n    primary_axis_property: Axis that is aligned exactly to the provided primary direction\n    secondary_axis_property: Axis that is aligned as well as possible given the alignment of the primary axis'
    return _node_function(
        'FunctionNodeAxesToRotation',
        inputs={
            'primary_axis': primary_axis,
            'secondary_axis': secondary_axis,
        },
        input_sockets={
            'primary_axis': ('Primary Axis', 'Primary Axis', 0, (0.0, 0.0, 1.0)),
            'secondary_axis': ('Secondary Axis', 'Secondary Axis', 1, (1.0, 0.0, 0.0)),
        },
        properties={
            'primary_axis': primary_axis_property,
            'secondary_axis': secondary_axis_property,
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'AUTO'),
        },
        output_type=FunctionNodeAxesToRotationOutputs,
    )

class FunctionNodeAxisAngleToRotationOutputs(typing.NamedTuple):
    rotation: Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]]

def axis_angle_to_rotation(*, axis: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 1.0), angle: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0) -> FunctionNodeAxisAngleToRotationOutputs:
    return _node_function(
        'FunctionNodeAxisAngleToRotation',
        inputs={
            'axis': axis,
            'angle': angle,
        },
        input_sockets={
            'axis': ('Axis', 'Axis', 0, (0.0, 0.0, 1.0)),
            'angle': ('Angle', 'Angle', 1, 0.0),
        },
        properties={
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'AUTO'),
        },
        output_type=FunctionNodeAxisAngleToRotationOutputs,
    )

class GeometryNodeCurvePrimitiveBezierSegmentOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def b_zier_segment(*, resolution: int | Socket[int] = 16, start: Vector | Socket[Vector] = (-1.0, 0.0, 0.0), start_handle: Vector | Socket[Vector] = (-0.5, 0.5, 0.0), end_handle: Vector | Socket[Vector] = (0.0, 0.0, 0.0), end: Vector | Socket[Vector] = (1.0, 0.0, 0.0), mode: typing.Literal['POSITION', 'OFFSET'] = 'POSITION') -> GeometryNodeCurvePrimitiveBezierSegmentOutputs:
    'Args:\n    mode: Method used to determine control handles'
    return _node_function(
        'GeometryNodeCurvePrimitiveBezierSegment',
        inputs={
            'resolution': resolution,
            'start': start,
            'start_handle': start_handle,
            'end_handle': end_handle,
            'end': end,
        },
        input_sockets={
            'resolution': ('Resolution', 'Resolution', 0, 16),
            'start': ('Start', 'Start', 1, (-1.0, 0.0, 0.0)),
            'start_handle': ('Start Handle', 'Start Handle', 2, (-0.5, 0.5, 0.0)),
            'end_handle': ('End Handle', 'End Handle', 3, (0.0, 0.0, 0.0)),
            'end': ('End', 'End', 4, (1.0, 0.0, 0.0)),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeCurvePrimitiveBezierSegmentOutputs,
    )

class GeometryNodeBakeOutputs(ItemOutputs):
    pass

def bake(**items: typing.Any) -> GeometryNodeBakeOutputs:
    'Args:\n    items: Items to add, by name; each socket type is inferred from its value. Their outputs are available by name on the result.'
    return _node_function(
        'GeometryNodeBake',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
        },
        output_type=GeometryNodeBakeOutputs,
        item_collections=(
            ('bake_items', 'values', items),
        ),
    )

class FunctionNodeBitMathOutputs(typing.NamedTuple):
    value: Socket[int | Field[int] | Grid[int] | List[int]]

def bit_math(*, a: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, b: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, shift: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, operation: typing.Literal['AND', 'OR', 'XOR', 'NOT', 'SHIFT', 'ROTATE'] = 'AND') -> FunctionNodeBitMathOutputs:
    return _node_function(
        'FunctionNodeBitMath',
        inputs={
            'a': a,
            'b': b,
            'shift': shift,
        },
        input_sockets={
            'a': ('A', 'A', 0, 0),
            'b': ('B', 'B', 1, 0),
            'shift': ('Shift', 'Shift', 2, 0),
        },
        properties={
            'operation': operation,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=FunctionNodeBitMathOutputs,
    )

class ShaderNodeBlackbodyOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]

def blackbody(*, temperature: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 6500.0) -> ShaderNodeBlackbodyOutputs:
    return _node_function(
        'ShaderNodeBlackbody',
        inputs={
            'temperature': temperature,
        },
        input_sockets={
            'temperature': ('Temperature', 'Temperature', 0, 6500.0),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeBlackbodyOutputs,
    )

class GeometryNodeBlurAttributeOutputs(typing.NamedTuple):
    value: Socket[Field[float] | Field[int] | Field[Vector] | Field[Color]]

def blur_attribute(*, value: float | Field[float] | int | Field[int] | Vector | Field[Vector] | Color | Field[Color] | Socket[float | Field[float] | int | Field[int] | Vector | Field[Vector] | Color | Field[Color]] = 0.0, iterations: int | Socket[int] = 1, weight: float | Field[float] | Socket[float | Field[float]] = 1.0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None) -> GeometryNodeBlurAttributeOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeBlurAttribute',
        inputs={
            'value': value,
            'iterations': iterations,
            'weight': weight,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0.0),
            'iterations': ('Iterations', 'Iterations', 1, 1),
            'weight': ('Weight', 'Weight', 2, 1.0),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'FIELD'),
        },
        output_type=GeometryNodeBlurAttributeOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}, 'FLOAT_COLOR': {'value': 'RGBA'}}},
    )

class GeometryNodeBoneInfoOutputs(typing.NamedTuple):
    pose: Socket[Matrix]
    local_pose: Socket[Matrix]
    transform_pose: Socket[Matrix]
    rest_pose: Socket[Matrix]
    rest_length: Socket[float]
    exists: Socket[bool]

def bone_info(*, armature: Object | Socket[Object] | None = None, bone_name: str | Socket[str] = '', transform_space: typing.Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL') -> GeometryNodeBoneInfoOutputs:
    'Args:\n    transform_space: The transformation of the vector and geometry outputs'
    return _node_function(
        'GeometryNodeBoneInfo',
        inputs={
            'armature': armature,
            'bone_name': bone_name,
        },
        input_sockets={
            'armature': ('Armature', 'Armature', 0, None),
            'bone_name': ('Bone Name', 'Bone Name', 1, ''),
        },
        properties={
            'transform_space': transform_space,
        },
        output_sockets={
            'pose': ('Pose', 'Pose', 0, 'AUTO'),
            'local_pose': ('Local Pose', 'Local Pose', 1, 'AUTO'),
            'transform_pose': ('Transform Pose', 'Transform Pose', 2, 'AUTO'),
            'rest_pose': ('Rest Pose', 'Rest Pose', 3, 'AUTO'),
            'rest_length': ('Rest Length', 'Rest Length', 4, 'AUTO'),
            'exists': ('Exists', 'Exists', 5, 'AUTO'),
        },
        output_type=GeometryNodeBoneInfoOutputs,
    )

class FunctionNodeInputBoolOutputs(typing.NamedTuple):
    boolean: Socket[bool]

def boolean(*, boolean: bool = False) -> FunctionNodeInputBoolOutputs:
    'Args:\n    boolean: Input value used for unconnected socket'
    return _node_function(
        'FunctionNodeInputBool',
        inputs={
        },
        input_sockets={
        },
        properties={
            'boolean': boolean,
        },
        output_sockets={
            'boolean': ('Boolean', 'Boolean', 0, 'AUTO'),
        },
        output_type=FunctionNodeInputBoolOutputs,
    )

class FunctionNodeBooleanMathOutputs(typing.NamedTuple):
    boolean: Socket[bool | Field[bool] | Grid[bool] | List[bool]]

def boolean_math(*, boolean: bool | Field[bool] | Grid[bool] | List[bool] | Socket[bool | Field[bool] | Grid[bool] | List[bool]] = False, boolean_2: bool | Field[bool] | Grid[bool] | List[bool] | Socket[bool | Field[bool] | Grid[bool] | List[bool]] = False, operation: typing.Literal['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY'] = 'AND') -> FunctionNodeBooleanMathOutputs:
    return _node_function(
        'FunctionNodeBooleanMath',
        inputs={
            'boolean': boolean,
            'boolean_2': boolean_2,
        },
        input_sockets={
            'boolean': ('Boolean', 'Boolean', 0, False),
            'boolean_2': ('Boolean_001', 'Boolean', 1, False),
        },
        properties={
            'operation': operation,
        },
        output_sockets={
            'boolean': ('Boolean', 'Boolean', 0, 'AUTO'),
        },
        output_type=FunctionNodeBooleanMathOutputs,
    )

class GeometryNodeBoundBoxOutputs(typing.NamedTuple):
    bounding_box: Socket[Geometry]
    min: Socket[Vector]
    max: Socket[Vector]

def bounding_box(*, geometry: Geometry | Socket[Geometry] | None = None, use_radius: bool | Socket[bool] = True) -> GeometryNodeBoundBoxOutputs:
    return _node_function(
        'GeometryNodeBoundBox',
        inputs={
            'geometry': geometry,
            'use_radius': use_radius,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'use_radius': ('Use Radius', 'Use Radius', 1, True),
        },
        properties={
        },
        output_sockets={
            'bounding_box': ('Bounding Box', 'Bounding Box', 0, 'AUTO'),
            'min': ('Min', 'Min', 1, 'AUTO'),
            'max': ('Max', 'Max', 2, 'AUTO'),
        },
        output_type=GeometryNodeBoundBoxOutputs,
    )

class ShaderNodeTexBrickOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]
    factor: Socket[float | Field[float] | Grid[float] | List[float]]

def brick_texture(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), color1: Color | Field[Color] | Grid[Color] | List[Color] | Socket[Color | Field[Color] | Grid[Color] | List[Color]] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), color2: Color | Field[Color] | Grid[Color] | List[Color] | Socket[Color | Field[Color] | Grid[Color] | List[Color]] = (0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0), mortar: Color | Field[Color] | Grid[Color] | List[Color] | Socket[Color | Field[Color] | Grid[Color] | List[Color]] = (0.0, 0.0, 0.0, 1.0), scale: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 5.0, mortar_size: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.019999999552965164, mortar_smooth: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.10000000149011612, bias: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, brick_width: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5, row_height: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.25, offset_frequency: int = 2, squash_frequency: int = 2, offset: float = 0.5, squash: float = 1.0) -> ShaderNodeTexBrickOutputs:
    'Args:\n    offset_frequency: How often rows are offset. A value of 2 gives an even/uneven pattern of rows.\n    squash_frequency: How often rows consist of "squished" bricks\n    offset: Determines the brick offset of the various rows\n    squash: Factor to adjust the brick\'s width for particular rows determined by the Offset Frequency'
    return _node_function(
        'ShaderNodeTexBrick',
        inputs={
            'vector': vector,
            'color1': color1,
            'color2': color2,
            'mortar': mortar,
            'scale': scale,
            'mortar_size': mortar_size,
            'mortar_smooth': mortar_smooth,
            'bias': bias,
            'brick_width': brick_width,
            'row_height': row_height,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'color1': ('Color1', 'Color1', 1, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'color2': ('Color2', 'Color2', 2, (0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0)),
            'mortar': ('Mortar', 'Mortar', 3, (0.0, 0.0, 0.0, 1.0)),
            'scale': ('Scale', 'Scale', 4, 5.0),
            'mortar_size': ('Mortar Size', 'Mortar Size', 5, 0.019999999552965164),
            'mortar_smooth': ('Mortar Smooth', 'Mortar Smooth', 6, 0.10000000149011612),
            'bias': ('Bias', 'Bias', 7, 0.0),
            'brick_width': ('Brick Width', 'Brick Width', 8, 0.5),
            'row_height': ('Row Height', 'Row Height', 9, 0.25),
        },
        properties={
            'offset_frequency': offset_frequency,
            'squash_frequency': squash_frequency,
            'offset': offset,
            'squash': squash,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'FIELD'),
            'factor': ('Fac', 'Factor', 1, 'FIELD'),
        },
        output_type=ShaderNodeTexBrickOutputs,
    )

class GeometryNodeCameraInfoOutputs(typing.NamedTuple):
    projection_matrix: Socket[Matrix]
    focal_length: Socket[float]
    sensor: Socket[Vector2]
    shift: Socket[Vector2]
    clip_start: Socket[float]
    clip_end: Socket[float]
    focus_distance: Socket[float]
    is_orthographic: Socket[bool]
    orthographic_scale: Socket[float]

def camera_info(*, camera: Object | Socket[Object] | None = None) -> GeometryNodeCameraInfoOutputs:
    return _node_function(
        'GeometryNodeCameraInfo',
        inputs={
            'camera': camera,
        },
        input_sockets={
            'camera': ('Camera', 'Camera', 0, None),
        },
        properties={
        },
        output_sockets={
            'projection_matrix': ('Projection Matrix', 'Projection Matrix', 0, 'AUTO'),
            'focal_length': ('Focal Length', 'Focal Length', 1, 'AUTO'),
            'sensor': ('Sensor', 'Sensor', 2, 'AUTO'),
            'shift': ('Shift', 'Shift', 3, 'AUTO'),
            'clip_start': ('Clip Start', 'Clip Start', 4, 'AUTO'),
            'clip_end': ('Clip End', 'Clip End', 5, 'AUTO'),
            'focus_distance': ('Focus Distance', 'Focus Distance', 6, 'AUTO'),
            'is_orthographic': ('Is Orthographic', 'Is Orthographic', 7, 'AUTO'),
            'orthographic_scale': ('Orthographic Scale', 'Orthographic Scale', 8, 'AUTO'),
        },
        output_type=GeometryNodeCameraInfoOutputs,
    )

class GeometryNodeCaptureAttributeOutputs(ItemOutputs):
    geometry: Socket[Geometry]
    selection: Socket[Field[bool]]

def capture_attribute(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT', **items: typing.Any) -> GeometryNodeCaptureAttributeOutputs:
    'Args:\n    domain: Which domain to store the data in\n    items: Items to add, by name; each socket type is inferred from its value. Their outputs are available by name on the result.'
    return _node_function(
        'GeometryNodeCaptureAttribute',
        inputs={
            'geometry': geometry,
            'selection': selection,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
            'domain': domain,
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
            'selection': ('Selection', 'Selection', 1, 'FIELD'),
        },
        output_type=GeometryNodeCaptureAttributeOutputs,
        item_collections=(
            ('capture_items', 'values', items),
        ),
    )

class ShaderNodeTexCheckerOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]
    factor: Socket[float | Field[float] | Grid[float] | List[float]]

def checker_texture(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), color1: Color | Field[Color] | Grid[Color] | List[Color] | Socket[Color | Field[Color] | Grid[Color] | List[Color]] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), color2: Color | Field[Color] | Grid[Color] | List[Color] | Socket[Color | Field[Color] | Grid[Color] | List[Color]] = (0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0), scale: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 5.0) -> ShaderNodeTexCheckerOutputs:
    return _node_function(
        'ShaderNodeTexChecker',
        inputs={
            'vector': vector,
            'color1': color1,
            'color2': color2,
            'scale': scale,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'color1': ('Color1', 'Color1', 1, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'color2': ('Color2', 'Color2', 2, (0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0)),
            'scale': ('Scale', 'Scale', 3, 5.0),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'FIELD'),
            'factor': ('Fac', 'Factor', 1, 'FIELD'),
        },
        output_type=ShaderNodeTexCheckerOutputs,
    )

class ShaderNodeClampOutputs(typing.NamedTuple):
    result: Socket[float | Field[float] | Grid[float] | List[float]]

def clamp(*, value: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, min: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, max: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, clamp_type: typing.Literal['MINMAX', 'RANGE'] = 'MINMAX') -> ShaderNodeClampOutputs:
    return _node_function(
        'ShaderNodeClamp',
        inputs={
            'value': value,
            'min': min,
            'max': max,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 1.0),
            'min': ('Min', 'Min', 1, 0.0),
            'max': ('Max', 'Max', 2, 1.0),
        },
        properties={
            'clamp_type': clamp_type,
        },
        output_sockets={
            'result': ('Result', 'Result', 0, 'AUTO'),
        },
        output_type=ShaderNodeClampOutputs,
    )

class GeometryNodeGridClipOutputs(typing.NamedTuple):
    grid: Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]]

def clip_grid(*, grid: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, min_x: int | Socket[int] = 0, min_y: int | Socket[int] = 0, min_z: int | Socket[int] = 0, max_x: int | Socket[int] = 32, max_y: int | Socket[int] = 32, max_z: int | Socket[int] = 32, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeGridClipOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeGridClip',
        inputs={
            'grid': grid,
            'min_x': min_x,
            'min_y': min_y,
            'min_z': min_z,
            'max_x': max_x,
            'max_y': max_y,
            'max_z': max_z,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'min_x': ('Min X', 'Min X', 1, 0),
            'min_y': ('Min Y', 'Min Y', 2, 0),
            'min_z': ('Min Z', 'Min Z', 3, 0),
            'max_x': ('Max X', 'Max X', 4, 32),
            'max_y': ('Max Y', 'Max Y', 5, 32),
            'max_z': ('Max Z', 'Max Z', 6, 32),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeGridClipOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'BOOLEAN': {'grid': 'BOOLEAN'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class GeometryNodeClosureToListOutputs(ItemOutputs):
    pass

def closure_to_list(*, count: int | Socket[int] = 1, closure: Closure | Socket[Closure] | None = None, items: typing.Mapping[str, typing.Any] | None = None) -> GeometryNodeClosureToListOutputs:
    'Args:\n    items: Items to add, mapping each name to its type (float, Vector, Geometry, ...). Their outputs are available by name on the result.'
    return _node_function(
        'GeometryNodeClosureToList',
        inputs={
            'count': count,
            'closure': closure,
        },
        input_sockets={
            'count': ('Count', 'Count', 0, 1),
            'closure': ('Closure', 'Closure', 1, None),
        },
        properties={
        },
        output_sockets={
        },
        output_type=GeometryNodeClosureToListOutputs,
        item_collections=(
            ('list_items', 'types', items),
        ),
    )

class GeometryNodeClusterByConnectedOutputs(typing.NamedTuple):
    cluster_id: Socket[Field[int]]

def cluster_by_connected(*, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, position: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), distance: float | Socket[float] = 0.0010000000474974513) -> GeometryNodeClusterByConnectedOutputs:
    return _node_function(
        'GeometryNodeClusterByConnected',
        inputs={
            'selection': selection,
            'position': position,
            'distance': distance,
        },
        input_sockets={
            'selection': ('Selection', 'Selection', 0, True),
            'position': ('Position', 'Position', 1, (0.0, 0.0, 0.0)),
            'distance': ('Distance', 'Distance', 2, 0.0010000000474974513),
        },
        properties={
        },
        output_sockets={
            'cluster_id': ('Cluster ID', 'Cluster ID', 0, 'FIELD'),
        },
        output_type=GeometryNodeClusterByConnectedOutputs,
    )

class GeometryNodeClusterByDistanceOutputs(typing.NamedTuple):
    cluster_id: Socket[Field[int]]

def cluster_by_distance(*, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, group_id: int | Field[int] | Socket[int | Field[int]] = 0, position: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), distance: float | Socket[float] = 0.0010000000474974513) -> GeometryNodeClusterByDistanceOutputs:
    return _node_function(
        'GeometryNodeClusterByDistance',
        inputs={
            'selection': selection,
            'group_id': group_id,
            'position': position,
            'distance': distance,
        },
        input_sockets={
            'selection': ('Selection', 'Selection', 0, True),
            'group_id': ('Group ID', 'Group ID', 1, 0),
            'position': ('Position', 'Position', 2, (0.0, 0.0, 0.0)),
            'distance': ('Distance', 'Distance', 3, 0.0010000000474974513),
        },
        properties={
        },
        output_sockets={
            'cluster_id': ('Cluster ID', 'Cluster ID', 0, 'FIELD'),
        },
        output_type=GeometryNodeClusterByDistanceOutputs,
    )

class GeometryNodeInputCollectionOutputs(typing.NamedTuple):
    collection: Socket[Collection]

def collection(*, collection: bpy.types.Collection | None = None) -> GeometryNodeInputCollectionOutputs:
    return _node_function(
        'GeometryNodeInputCollection',
        inputs={
        },
        input_sockets={
        },
        properties={
            'collection': collection,
        },
        output_sockets={
            'collection': ('Collection', 'Collection', 0, 'AUTO'),
        },
        output_type=GeometryNodeInputCollectionOutputs,
    )

class GeometryNodeCollectionChildrenOutputs(typing.NamedTuple):
    collections: Socket[List[Collection]]
    objects: Socket[List[Object]]

def collection_children(*, collection: Collection | Socket[Collection] | None = None, recursive: bool | Socket[bool] = False) -> GeometryNodeCollectionChildrenOutputs:
    return _node_function(
        'GeometryNodeCollectionChildren',
        inputs={
            'collection': collection,
            'recursive': recursive,
        },
        input_sockets={
            'collection': ('Collection', 'Collection', 0, None),
            'recursive': ('Recursive', 'Recursive', 1, False),
        },
        properties={
        },
        output_sockets={
            'collections': ('Collections', 'Collections', 0, 'LIST'),
            'objects': ('Objects', 'Objects', 1, 'LIST'),
        },
        output_type=GeometryNodeCollectionChildrenOutputs,
    )

class GeometryNodeCollectionInfoOutputs(typing.NamedTuple):
    instances: Socket[Geometry]

def collection_info(*, collection: Collection | Socket[Collection] | None = None, separate_children: bool | Socket[bool] = False, reset_children: bool | Socket[bool] = False, transform_space: typing.Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL') -> GeometryNodeCollectionInfoOutputs:
    'Args:\n    transform_space: The transformation of the instances output. Does not affect the internal geometry'
    return _node_function(
        'GeometryNodeCollectionInfo',
        inputs={
            'collection': collection,
            'separate_children': separate_children,
            'reset_children': reset_children,
        },
        input_sockets={
            'collection': ('Collection', 'Collection', 0, None),
            'separate_children': ('Separate Children', 'Separate Children', 1, False),
            'reset_children': ('Reset Children', 'Reset Children', 2, False),
        },
        properties={
            'transform_space': transform_space,
        },
        output_sockets={
            'instances': ('Instances', 'Instances', 0, 'AUTO'),
        },
        output_type=GeometryNodeCollectionInfoOutputs,
    )

class FunctionNodeInputColorOutputs(typing.NamedTuple):
    color: Socket[Color]

def color(*, value: Color = (0.5, 0.5, 0.5, 1.0)) -> FunctionNodeInputColorOutputs:
    return _node_function(
        'FunctionNodeInputColor',
        inputs={
        },
        input_sockets={
        },
        properties={
            'value': value,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=FunctionNodeInputColorOutputs,
    )

class ShaderNodeValToRGBOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]
    alpha: Socket[float | Field[float] | Grid[float] | List[float]]

def color_ramp(*, factor: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5) -> ShaderNodeValToRGBOutputs:
    return _node_function(
        'ShaderNodeValToRGB',
        inputs={
            'factor': factor,
        },
        input_sockets={
            'factor': ('Fac', 'Factor', 0, 0.5),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 1, 'AUTO'),
        },
        output_type=ShaderNodeValToRGBOutputs,
    )

class NodeCombineBundleOutputs(typing.NamedTuple):
    bundle: Socket[Bundle]

def combine_bundle(*, define_signature: bool = False, **items: typing.Any) -> NodeCombineBundleOutputs:
    'Args:\n    define_signature: This node defines a bundle signature that should be used by other nodes\n    items: Items to add, by name; each socket type is inferred from its value.'
    return _node_function(
        'NodeCombineBundle',
        inputs={
        },
        input_sockets={
        },
        properties={
            'define_signature': define_signature,
        },
        output_sockets={
            'bundle': ('Bundle', 'Bundle', 0, 'AUTO'),
        },
        output_type=NodeCombineBundleOutputs,
        item_collections=(
            ('bundle_items', 'values', items),
        ),
    )

class FunctionNodeCombineColorOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]

def combine_color(*, red: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, green: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, blue: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, alpha: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, mode: typing.Literal['RGB', 'HSV', 'HSL'] = 'RGB') -> FunctionNodeCombineColorOutputs:
    'Args:\n    mode: Mode of color processing'
    return _node_function(
        'FunctionNodeCombineColor',
        inputs={
            'red': red,
            'green': green,
            'blue': blue,
            'alpha': alpha,
        },
        input_sockets={
            'red': ('Red', 'Red', 0, 0.0),
            'green': ('Green', 'Green', 1, 0.0),
            'blue': ('Blue', 'Blue', 2, 0.0),
            'alpha': ('Alpha', 'Alpha', 3, 1.0),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=FunctionNodeCombineColorOutputs,
    )

class FunctionNodeCombineMatrixOutputs(typing.NamedTuple):
    matrix: Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]

def combine_matrix(*, column_1_row_1: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, column_1_row_2: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_1_row_3: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_1_row_4: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_2_row_1: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_2_row_2: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, column_2_row_3: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_2_row_4: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_3_row_1: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_3_row_2: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_3_row_3: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, column_3_row_4: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_4_row_1: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_4_row_2: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_4_row_3: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, column_4_row_4: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0) -> FunctionNodeCombineMatrixOutputs:
    return _node_function(
        'FunctionNodeCombineMatrix',
        inputs={
            'column_1_row_1': column_1_row_1,
            'column_1_row_2': column_1_row_2,
            'column_1_row_3': column_1_row_3,
            'column_1_row_4': column_1_row_4,
            'column_2_row_1': column_2_row_1,
            'column_2_row_2': column_2_row_2,
            'column_2_row_3': column_2_row_3,
            'column_2_row_4': column_2_row_4,
            'column_3_row_1': column_3_row_1,
            'column_3_row_2': column_3_row_2,
            'column_3_row_3': column_3_row_3,
            'column_3_row_4': column_3_row_4,
            'column_4_row_1': column_4_row_1,
            'column_4_row_2': column_4_row_2,
            'column_4_row_3': column_4_row_3,
            'column_4_row_4': column_4_row_4,
        },
        input_sockets={
            'column_1_row_1': ('Column 1 Row 1', 'Column 1 Row 1', 0, 1.0),
            'column_1_row_2': ('Column 1 Row 2', 'Column 1 Row 2', 1, 0.0),
            'column_1_row_3': ('Column 1 Row 3', 'Column 1 Row 3', 2, 0.0),
            'column_1_row_4': ('Column 1 Row 4', 'Column 1 Row 4', 3, 0.0),
            'column_2_row_1': ('Column 2 Row 1', 'Column 2 Row 1', 4, 0.0),
            'column_2_row_2': ('Column 2 Row 2', 'Column 2 Row 2', 5, 1.0),
            'column_2_row_3': ('Column 2 Row 3', 'Column 2 Row 3', 6, 0.0),
            'column_2_row_4': ('Column 2 Row 4', 'Column 2 Row 4', 7, 0.0),
            'column_3_row_1': ('Column 3 Row 1', 'Column 3 Row 1', 8, 0.0),
            'column_3_row_2': ('Column 3 Row 2', 'Column 3 Row 2', 9, 0.0),
            'column_3_row_3': ('Column 3 Row 3', 'Column 3 Row 3', 10, 1.0),
            'column_3_row_4': ('Column 3 Row 4', 'Column 3 Row 4', 11, 0.0),
            'column_4_row_1': ('Column 4 Row 1', 'Column 4 Row 1', 12, 0.0),
            'column_4_row_2': ('Column 4 Row 2', 'Column 4 Row 2', 13, 0.0),
            'column_4_row_3': ('Column 4 Row 3', 'Column 4 Row 3', 14, 0.0),
            'column_4_row_4': ('Column 4 Row 4', 'Column 4 Row 4', 15, 1.0),
        },
        properties={
        },
        output_sockets={
            'matrix': ('Matrix', 'Matrix', 0, 'AUTO'),
        },
        output_type=FunctionNodeCombineMatrixOutputs,
    )

class FunctionNodeCombineTransformOutputs(typing.NamedTuple):
    transform: Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]

def combine_transform(*, translation: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), rotation: Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = (0.0, 0.0, 0.0), scale: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (1.0, 1.0, 1.0)) -> FunctionNodeCombineTransformOutputs:
    return _node_function(
        'FunctionNodeCombineTransform',
        inputs={
            'translation': translation,
            'rotation': rotation,
            'scale': scale,
        },
        input_sockets={
            'translation': ('Translation', 'Translation', 0, (0.0, 0.0, 0.0)),
            'rotation': ('Rotation', 'Rotation', 1, (0.0, 0.0, 0.0)),
            'scale': ('Scale', 'Scale', 2, (1.0, 1.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'transform': ('Transform', 'Transform', 0, 'AUTO'),
        },
        output_type=FunctionNodeCombineTransformOutputs,
    )

class ShaderNodeCombineXYZOutputs(typing.NamedTuple):
    vector: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def combine_xyz(*, x: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, y: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, z: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0) -> ShaderNodeCombineXYZOutputs:
    return _node_function(
        'ShaderNodeCombineXYZ',
        inputs={
            'x': x,
            'y': y,
            'z': z,
        },
        input_sockets={
            'x': ('X', 'X', 0, 0.0),
            'y': ('Y', 'Y', 1, 0.0),
            'z': ('Z', 'Z', 2, 0.0),
        },
        properties={
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
        },
        output_type=ShaderNodeCombineXYZOutputs,
    )

class FunctionNodeCompareOutputs(typing.NamedTuple):
    result: Socket[bool | Field[bool] | Grid[bool] | List[bool]]

def compare(*, a: float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | str | Field[str] | Grid[str] | List[str] | Object | Image | Collection | Material | Font | Sound | Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | str | Field[str] | Grid[str] | List[str] | Object | Image | Collection | Material | Font | Sound] = 0.0, b: float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | str | Field[str] | Grid[str] | List[str] | Object | Image | Collection | Material | Font | Sound | Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | str | Field[str] | Grid[str] | List[str] | Object | Image | Collection | Material | Font | Sound] = 0.0, epsilon: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0010000000474974513, c: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.8999999761581421, angle: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.08726649731397629, operation: typing.Literal['LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL', 'BRIGHTER', 'DARKER'] = 'GREATER_THAN', data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None, mode: typing.Literal['ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION'] = 'ELEMENT') -> FunctionNodeCompareOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'FunctionNodeCompare',
        inputs={
            'a': a,
            'b': b,
            'epsilon': epsilon,
            'c': c,
            'angle': angle,
        },
        input_sockets={
            'a': ('A', 'A', 0, 0.0),
            'b': ('B', 'B', 1, 0.0),
            'epsilon': ('Epsilon', 'Epsilon', 2, 0.0010000000474974513),
            'c': ('C', 'C', 2, 0.8999999761581421),
            'angle': ('Angle', 'Angle', 2, 0.08726649731397629),
        },
        properties={
            'operation': operation,
            'data_type': data_type,
            'mode': mode,
        },
        output_sockets={
            'result': ('Result', 'Result', 0, 'AUTO'),
        },
        output_type=FunctionNodeCompareOutputs,
        type_properties={'data_type': {'FLOAT': {'a': 'VALUE', 'b': 'VALUE'}, 'INT': {'a': 'INT', 'b': 'INT'}, 'VECTOR': {'a': 'VECTOR', 'b': 'VECTOR'}, 'RGBA': {'a': 'RGBA', 'b': 'RGBA'}, 'STRING': {'a': 'STRING', 'b': 'STRING'}, 'OBJECT': {'a': 'OBJECT', 'b': 'OBJECT'}, 'IMAGE': {'a': 'IMAGE', 'b': 'IMAGE'}, 'COLLECTION': {'a': 'COLLECTION', 'b': 'COLLECTION'}, 'MATERIAL': {'a': 'MATERIAL', 'b': 'MATERIAL'}, 'FONT': {'a': 'FONT', 'b': 'FONT'}, 'SOUND': {'a': 'SOUND', 'b': 'SOUND'}}},
    )

class GeometryNodeMeshConeOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]
    top: Socket[Field[bool]]
    bottom: Socket[Field[bool]]
    side: Socket[Field[bool]]
    uv_map: Socket[Field[Vector]]

def cone(*, vertices: int | Socket[int] = 32, side_segments: int | Socket[int] = 1, fill_segments: int | Socket[int] = 1, radius_top: float | Socket[float] = 0.0, radius_bottom: float | Socket[float] = 1.0, depth: float | Socket[float] = 2.0, fill_type: typing.Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON') -> GeometryNodeMeshConeOutputs:
    return _node_function(
        'GeometryNodeMeshCone',
        inputs={
            'vertices': vertices,
            'side_segments': side_segments,
            'fill_segments': fill_segments,
            'radius_top': radius_top,
            'radius_bottom': radius_bottom,
            'depth': depth,
        },
        input_sockets={
            'vertices': ('Vertices', 'Vertices', 0, 32),
            'side_segments': ('Side Segments', 'Side Segments', 1, 1),
            'fill_segments': ('Fill Segments', 'Fill Segments', 2, 1),
            'radius_top': ('Radius Top', 'Radius Top', 3, 0.0),
            'radius_bottom': ('Radius Bottom', 'Radius Bottom', 4, 1.0),
            'depth': ('Depth', 'Depth', 5, 2.0),
        },
        properties={
            'fill_type': fill_type,
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
            'top': ('Top', 'Top', 1, 'FIELD'),
            'bottom': ('Bottom', 'Bottom', 2, 'FIELD'),
            'side': ('Side', 'Side', 3, 'FIELD'),
            'uv_map': ('UV Map', 'UV Map', 4, 'FIELD'),
        },
        output_type=GeometryNodeMeshConeOutputs,
    )

class GeometryNodeConvexHullOutputs(typing.NamedTuple):
    convex_hull: Socket[Geometry]

def convex_hull(*, geometry: Geometry | Socket[Geometry] | None = None) -> GeometryNodeConvexHullOutputs:
    return _node_function(
        'GeometryNodeConvexHull',
        inputs={
            'geometry': geometry,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
        },
        properties={
        },
        output_sockets={
            'convex_hull': ('Convex Hull', 'Convex Hull', 0, 'AUTO'),
        },
        output_type=GeometryNodeConvexHullOutputs,
    )

class GeometryNodeCornersOfEdgeOutputs(typing.NamedTuple):
    corner_index: Socket[Field[int]]
    total: Socket[Field[int]]

def corners_of_edge(*, edge_index: int | Field[int] | Socket[int | Field[int]] = 0, weights: float | Field[float] | Socket[float | Field[float]] = 0.0, sort_index: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeCornersOfEdgeOutputs:
    return _node_function(
        'GeometryNodeCornersOfEdge',
        inputs={
            'edge_index': edge_index,
            'weights': weights,
            'sort_index': sort_index,
        },
        input_sockets={
            'edge_index': ('Edge Index', 'Edge Index', 0, 0),
            'weights': ('Weights', 'Weights', 1, 0.0),
            'sort_index': ('Sort Index', 'Sort Index', 2, 0),
        },
        properties={
        },
        output_sockets={
            'corner_index': ('Corner Index', 'Corner Index', 0, 'FIELD'),
            'total': ('Total', 'Total', 1, 'FIELD'),
        },
        output_type=GeometryNodeCornersOfEdgeOutputs,
    )

class GeometryNodeCornersOfFaceOutputs(typing.NamedTuple):
    corner_index: Socket[Field[int]]
    total: Socket[Field[int]]

def corners_of_face(*, face_index: int | Field[int] | Socket[int | Field[int]] = 0, weights: float | Field[float] | Socket[float | Field[float]] = 0.0, sort_index: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeCornersOfFaceOutputs:
    return _node_function(
        'GeometryNodeCornersOfFace',
        inputs={
            'face_index': face_index,
            'weights': weights,
            'sort_index': sort_index,
        },
        input_sockets={
            'face_index': ('Face Index', 'Face Index', 0, 0),
            'weights': ('Weights', 'Weights', 1, 0.0),
            'sort_index': ('Sort Index', 'Sort Index', 2, 0),
        },
        properties={
        },
        output_sockets={
            'corner_index': ('Corner Index', 'Corner Index', 0, 'FIELD'),
            'total': ('Total', 'Total', 1, 'FIELD'),
        },
        output_type=GeometryNodeCornersOfFaceOutputs,
    )

class GeometryNodeCornersOfVertexOutputs(typing.NamedTuple):
    corner_index: Socket[Field[int]]
    total: Socket[Field[int]]

def corners_of_vertex(*, vertex_index: int | Field[int] | Socket[int | Field[int]] = 0, weights: float | Field[float] | Socket[float | Field[float]] = 0.0, sort_index: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeCornersOfVertexOutputs:
    return _node_function(
        'GeometryNodeCornersOfVertex',
        inputs={
            'vertex_index': vertex_index,
            'weights': weights,
            'sort_index': sort_index,
        },
        input_sockets={
            'vertex_index': ('Vertex Index', 'Vertex Index', 0, 0),
            'weights': ('Weights', 'Weights', 1, 0.0),
            'sort_index': ('Sort Index', 'Sort Index', 2, 0),
        },
        properties={
        },
        output_sockets={
            'corner_index': ('Corner Index', 'Corner Index', 0, 'FIELD'),
            'total': ('Total', 'Total', 1, 'FIELD'),
        },
        output_type=GeometryNodeCornersOfVertexOutputs,
    )

class GeometryNodeMeshCubeOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]
    uv_map: Socket[Field[Vector]]

def cube(*, size: Vector | Socket[Vector] = (1.0, 1.0, 1.0), vertices_x: int | Socket[int] = 2, vertices_y: int | Socket[int] = 2, vertices_z: int | Socket[int] = 2) -> GeometryNodeMeshCubeOutputs:
    return _node_function(
        'GeometryNodeMeshCube',
        inputs={
            'size': size,
            'vertices_x': vertices_x,
            'vertices_y': vertices_y,
            'vertices_z': vertices_z,
        },
        input_sockets={
            'size': ('Size', 'Size', 0, (1.0, 1.0, 1.0)),
            'vertices_x': ('Vertices X', 'Vertices X', 1, 2),
            'vertices_y': ('Vertices Y', 'Vertices Y', 2, 2),
            'vertices_z': ('Vertices Z', 'Vertices Z', 3, 2),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
            'uv_map': ('UV Map', 'UV Map', 1, 'FIELD'),
        },
        output_type=GeometryNodeMeshCubeOutputs,
    )

class GeometryNodeCubeGridTopologyOutputs(typing.NamedTuple):
    topology: Socket[Grid[bool]]

def cube_grid_topology(*, bounds_min: Vector | Socket[Vector] = (-1.0, -1.0, -1.0), bounds_max: Vector | Socket[Vector] = (1.0, 1.0, 1.0), resolution_x: int | Socket[int] = 32, resolution_y: int | Socket[int] = 32, resolution_z: int | Socket[int] = 32, min_x: int | Socket[int] = 0, min_y: int | Socket[int] = 0, min_z: int | Socket[int] = 0) -> GeometryNodeCubeGridTopologyOutputs:
    return _node_function(
        'GeometryNodeCubeGridTopology',
        inputs={
            'bounds_min': bounds_min,
            'bounds_max': bounds_max,
            'resolution_x': resolution_x,
            'resolution_y': resolution_y,
            'resolution_z': resolution_z,
            'min_x': min_x,
            'min_y': min_y,
            'min_z': min_z,
        },
        input_sockets={
            'bounds_min': ('Bounds Min', 'Bounds Min', 0, (-1.0, -1.0, -1.0)),
            'bounds_max': ('Bounds Max', 'Bounds Max', 1, (1.0, 1.0, 1.0)),
            'resolution_x': ('Resolution X', 'Resolution X', 2, 32),
            'resolution_y': ('Resolution Y', 'Resolution Y', 3, 32),
            'resolution_z': ('Resolution Z', 'Resolution Z', 4, 32),
            'min_x': ('Min X', 'Min X', 5, 0),
            'min_y': ('Min Y', 'Min Y', 6, 0),
            'min_z': ('Min Z', 'Min Z', 7, 0),
        },
        properties={
        },
        output_sockets={
            'topology': ('Topology', 'Topology', 0, 'GRID'),
        },
        output_type=GeometryNodeCubeGridTopologyOutputs,
    )

class GeometryNodeCurvePrimitiveCircleOutputs(typing.NamedTuple):
    curve: Socket[Geometry]
    center: Socket[Vector]

def curve_circle(*, resolution: int | Socket[int] = 32, radius: float | Socket[float] = 1.0, point_1: Vector | Socket[Vector] = (-1.0, 0.0, 0.0), point_2: Vector | Socket[Vector] = (0.0, 1.0, 0.0), point_3: Vector | Socket[Vector] = (1.0, 0.0, 0.0), mode: typing.Literal['POINTS', 'RADIUS'] = 'RADIUS') -> GeometryNodeCurvePrimitiveCircleOutputs:
    'Args:\n    mode: Method used to determine radius and placement'
    return _node_function(
        'GeometryNodeCurvePrimitiveCircle',
        inputs={
            'resolution': resolution,
            'radius': radius,
            'point_1': point_1,
            'point_2': point_2,
            'point_3': point_3,
        },
        input_sockets={
            'resolution': ('Resolution', 'Resolution', 0, 32),
            'radius': ('Radius', 'Radius', 4, 1.0),
            'point_1': ('Point 1', 'Point 1', 1, (-1.0, 0.0, 0.0)),
            'point_2': ('Point 2', 'Point 2', 2, (0.0, 1.0, 0.0)),
            'point_3': ('Point 3', 'Point 3', 3, (1.0, 0.0, 0.0)),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
            'center': ('Center', 'Center', 1, 'AUTO'),
        },
        output_type=GeometryNodeCurvePrimitiveCircleOutputs,
    )

class GeometryNodeInputCurveHandlePositionsOutputs(typing.NamedTuple):
    left: Socket[Field[Vector]]
    right: Socket[Field[Vector]]

def curve_handle_positions(*, relative: bool | Field[bool] | Socket[bool | Field[bool]] = False) -> GeometryNodeInputCurveHandlePositionsOutputs:
    return _node_function(
        'GeometryNodeInputCurveHandlePositions',
        inputs={
            'relative': relative,
        },
        input_sockets={
            'relative': ('Relative', 'Relative', 0, False),
        },
        properties={
        },
        output_sockets={
            'left': ('Left', 'Left', 0, 'FIELD'),
            'right': ('Right', 'Right', 1, 'FIELD'),
        },
        output_type=GeometryNodeInputCurveHandlePositionsOutputs,
    )

class GeometryNodeCurveLengthOutputs(typing.NamedTuple):
    length: Socket[float]

def curve_length(*, curve: Geometry | Socket[Geometry] | None = None) -> GeometryNodeCurveLengthOutputs:
    return _node_function(
        'GeometryNodeCurveLength',
        inputs={
            'curve': curve,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
        },
        properties={
        },
        output_sockets={
            'length': ('Length', 'Length', 0, 'AUTO'),
        },
        output_type=GeometryNodeCurveLengthOutputs,
    )

class GeometryNodeCurvePrimitiveLineOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def curve_line(*, start: Vector | Socket[Vector] = (0.0, 0.0, 0.0), end: Vector | Socket[Vector] = (0.0, 0.0, 1.0), direction: Vector | Socket[Vector] = (0.0, 0.0, 1.0), length: float | Socket[float] = 1.0, mode: typing.Literal['POINTS', 'DIRECTION'] = 'POINTS') -> GeometryNodeCurvePrimitiveLineOutputs:
    'Args:\n    mode: Method used to determine radius and placement'
    return _node_function(
        'GeometryNodeCurvePrimitiveLine',
        inputs={
            'start': start,
            'end': end,
            'direction': direction,
            'length': length,
        },
        input_sockets={
            'start': ('Start', 'Start', 0, (0.0, 0.0, 0.0)),
            'end': ('End', 'End', 1, (0.0, 0.0, 1.0)),
            'direction': ('Direction', 'Direction', 2, (0.0, 0.0, 1.0)),
            'length': ('Length', 'Length', 3, 1.0),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeCurvePrimitiveLineOutputs,
    )

class GeometryNodeCurveOfPointOutputs(typing.NamedTuple):
    curve_index: Socket[Field[int]]
    index_in_curve: Socket[Field[int]]

def curve_of_point(*, point_index: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeCurveOfPointOutputs:
    return _node_function(
        'GeometryNodeCurveOfPoint',
        inputs={
            'point_index': point_index,
        },
        input_sockets={
            'point_index': ('Point Index', 'Point Index', 0, 0),
        },
        properties={
        },
        output_sockets={
            'curve_index': ('Curve Index', 'Curve Index', 0, 'FIELD'),
            'index_in_curve': ('Index in Curve', 'Index in Curve', 1, 'FIELD'),
        },
        output_type=GeometryNodeCurveOfPointOutputs,
    )

class GeometryNodeInputTangentOutputs(typing.NamedTuple):
    tangent: Socket[Field[Vector]]

def curve_tangent() -> GeometryNodeInputTangentOutputs:
    return _node_function(
        'GeometryNodeInputTangent',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'tangent': ('Tangent', 'Tangent', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputTangentOutputs,
    )

class GeometryNodeInputCurveTiltOutputs(typing.NamedTuple):
    tilt: Socket[Field[float]]

def curve_tilt() -> GeometryNodeInputCurveTiltOutputs:
    return _node_function(
        'GeometryNodeInputCurveTilt',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'tilt': ('Tilt', 'Tilt', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputCurveTiltOutputs,
    )

class GeometryNodeCurveToMeshOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def curve_to_mesh(*, curve: Geometry | Socket[Geometry] | None = None, profile_curve: Geometry | Socket[Geometry] | None = None, scale: float | Field[float] | Socket[float | Field[float]] = 1.0, fill_caps: bool | Socket[bool] = False) -> GeometryNodeCurveToMeshOutputs:
    return _node_function(
        'GeometryNodeCurveToMesh',
        inputs={
            'curve': curve,
            'profile_curve': profile_curve,
            'scale': scale,
            'fill_caps': fill_caps,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'profile_curve': ('Profile Curve', 'Profile Curve', 1, None),
            'scale': ('Scale', 'Scale', 2, 1.0),
            'fill_caps': ('Fill Caps', 'Fill Caps', 3, False),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeCurveToMeshOutputs,
    )

class GeometryNodeCurveToPointsOutputs(typing.NamedTuple):
    points: Socket[Geometry]
    tangent: Socket[Field[Vector]]
    normal: Socket[Field[Vector]]
    rotation: Socket[Field[Rotation]]

def curve_to_points(*, curve: Geometry | Socket[Geometry] | None = None, count: int | Field[int] | Socket[int | Field[int]] = 10, length: float | Field[float] | Socket[float | Field[float]] = 0.10000000149011612, mode: typing.Literal['EVALUATED', 'COUNT', 'LENGTH'] = 'COUNT') -> GeometryNodeCurveToPointsOutputs:
    'Args:\n    mode: How to generate points from the input curve'
    return _node_function(
        'GeometryNodeCurveToPoints',
        inputs={
            'curve': curve,
            'count': count,
            'length': length,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'count': ('Count', 'Count', 1, 10),
            'length': ('Length', 'Length', 2, 0.10000000149011612),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'points': ('Points', 'Points', 0, 'AUTO'),
            'tangent': ('Tangent', 'Tangent', 1, 'FIELD'),
            'normal': ('Normal', 'Normal', 2, 'FIELD'),
            'rotation': ('Rotation', 'Rotation', 3, 'FIELD'),
        },
        output_type=GeometryNodeCurveToPointsOutputs,
    )

class GeometryNodeCurvesToGreasePencilOutputs(typing.NamedTuple):
    grease_pencil: Socket[Geometry]

def curves_to_grease_pencil(*, curves: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, instances_as_layers: bool | Socket[bool] = True) -> GeometryNodeCurvesToGreasePencilOutputs:
    return _node_function(
        'GeometryNodeCurvesToGreasePencil',
        inputs={
            'curves': curves,
            'selection': selection,
            'instances_as_layers': instances_as_layers,
        },
        input_sockets={
            'curves': ('Curves', 'Curves', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'instances_as_layers': ('Instances as Layers', 'Instances as Layers', 2, True),
        },
        properties={
        },
        output_sockets={
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 0, 'AUTO'),
        },
        output_type=GeometryNodeCurvesToGreasePencilOutputs,
    )

class GeometryNodeMeshCylinderOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]
    top: Socket[Field[bool]]
    side: Socket[Field[bool]]
    bottom: Socket[Field[bool]]
    uv_map: Socket[Field[Vector]]

def cylinder(*, vertices: int | Socket[int] = 32, side_segments: int | Socket[int] = 1, fill_segments: int | Socket[int] = 1, radius: float | Socket[float] = 1.0, depth: float | Socket[float] = 2.0, fill_type: typing.Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NGON') -> GeometryNodeMeshCylinderOutputs:
    return _node_function(
        'GeometryNodeMeshCylinder',
        inputs={
            'vertices': vertices,
            'side_segments': side_segments,
            'fill_segments': fill_segments,
            'radius': radius,
            'depth': depth,
        },
        input_sockets={
            'vertices': ('Vertices', 'Vertices', 0, 32),
            'side_segments': ('Side Segments', 'Side Segments', 1, 1),
            'fill_segments': ('Fill Segments', 'Fill Segments', 2, 1),
            'radius': ('Radius', 'Radius', 3, 1.0),
            'depth': ('Depth', 'Depth', 4, 2.0),
        },
        properties={
            'fill_type': fill_type,
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
            'top': ('Top', 'Top', 1, 'FIELD'),
            'side': ('Side', 'Side', 2, 'FIELD'),
            'bottom': ('Bottom', 'Bottom', 3, 'FIELD'),
            'uv_map': ('UV Map', 'UV Map', 4, 'FIELD'),
        },
        output_type=GeometryNodeMeshCylinderOutputs,
    )

class GeometryNodeDeformCurvesOnSurfaceOutputs(typing.NamedTuple):
    curves: Socket[Geometry]

def deform_curves_on_surface(*, curves: Geometry | Socket[Geometry] | None = None) -> GeometryNodeDeformCurvesOnSurfaceOutputs:
    return _node_function(
        'GeometryNodeDeformCurvesOnSurface',
        inputs={
            'curves': curves,
        },
        input_sockets={
            'curves': ('Curves', 'Curves', 0, None),
        },
        properties={
        },
        output_sockets={
            'curves': ('Curves', 'Curves', 0, 'AUTO'),
        },
        output_type=GeometryNodeDeformCurvesOnSurfaceOutputs,
    )

class GeometryNodeDeleteGeometryOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def delete_geometry(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, mode: typing.Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL', domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT') -> GeometryNodeDeleteGeometryOutputs:
    'Args:\n    mode: Which parts of the mesh component to delete\n    domain: Which domain to delete in'
    return _node_function(
        'GeometryNodeDeleteGeometry',
        inputs={
            'geometry': geometry,
            'selection': selection,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
            'mode': mode,
            'domain': domain,
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeDeleteGeometryOutputs,
    )

class GeometryNodeGizmoDialOutputs(typing.NamedTuple):
    transform: Socket[Geometry]

def dial_gizmo(*, value: typing.Sequence[float | Socket[float]] = (), position: Vector | Socket[Vector] = (0.0, 0.0, 0.0), up: Vector | Socket[Vector] = (0.0, 0.0, 1.0), screen_space: bool | Socket[bool] = True, radius: float | Socket[float] = 1.0, color_id: typing.Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY') -> GeometryNodeGizmoDialOutputs:
    return _node_function(
        'GeometryNodeGizmoDial',
        inputs={
            'value': value,
            'position': position,
            'up': up,
            'screen_space': screen_space,
            'radius': radius,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, ()),
            'position': ('Position', 'Position', 1, (0.0, 0.0, 0.0)),
            'up': ('Up', 'Up', 2, (0.0, 0.0, 1.0)),
            'screen_space': ('Screen Space', 'Screen Space', 3, True),
            'radius': ('Radius', 'Radius', 4, 1.0),
        },
        properties={
            'color_id': color_id,
        },
        output_sockets={
            'transform': ('Transform', 'Transform', 0, 'AUTO'),
        },
        output_type=GeometryNodeGizmoDialOutputs,
    )

class GeometryNodeDistributePointsInGridOutputs(typing.NamedTuple):
    points: Socket[Geometry]

def distribute_points_in_grid(*, grid: Grid[float] | Socket[Grid[float]] | None = None, density: float | Socket[float] = 1.0, seed: int | Socket[int] = 0, spacing: Vector | Socket[Vector] = (0.30000001192092896, 0.30000001192092896, 0.30000001192092896), threshold: float | Socket[float] = 0.10000000149011612, mode: typing.Literal['DENSITY_RANDOM', 'DENSITY_GRID'] = 'DENSITY_RANDOM') -> GeometryNodeDistributePointsInGridOutputs:
    'Args:\n    mode: Method to use for scattering points'
    return _node_function(
        'GeometryNodeDistributePointsInGrid',
        inputs={
            'grid': grid,
            'density': density,
            'seed': seed,
            'spacing': spacing,
            'threshold': threshold,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'density': ('Density', 'Density', 1, 1.0),
            'seed': ('Seed', 'Seed', 2, 0),
            'spacing': ('Spacing', 'Spacing', 3, (0.30000001192092896, 0.30000001192092896, 0.30000001192092896)),
            'threshold': ('Threshold', 'Threshold', 4, 0.10000000149011612),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'points': ('Points', 'Points', 0, 'AUTO'),
        },
        output_type=GeometryNodeDistributePointsInGridOutputs,
    )

class GeometryNodeDistributePointsInVolumeOutputs(typing.NamedTuple):
    points: Socket[Geometry]

def distribute_points_in_volume(*, volume: Geometry | Socket[Geometry] | None = None, mode: Menu | Socket[Menu] = 'Random', density: float | Socket[float] = 1.0, seed: int | Socket[int] = 0, spacing: Vector | Socket[Vector] = (0.30000001192092896, 0.30000001192092896, 0.30000001192092896), threshold: float | Socket[float] = 0.10000000149011612) -> GeometryNodeDistributePointsInVolumeOutputs:
    return _node_function(
        'GeometryNodeDistributePointsInVolume',
        inputs={
            'volume': volume,
            'mode': mode,
            'density': density,
            'seed': seed,
            'spacing': spacing,
            'threshold': threshold,
        },
        input_sockets={
            'volume': ('Volume', 'Volume', 0, None),
            'mode': ('Mode', 'Mode', 1, 'Random'),
            'density': ('Density', 'Density', 2, 1.0),
            'seed': ('Seed', 'Seed', 3, 0),
            'spacing': ('Spacing', 'Spacing', 4, (0.30000001192092896, 0.30000001192092896, 0.30000001192092896)),
            'threshold': ('Threshold', 'Threshold', 5, 0.10000000149011612),
        },
        properties={
        },
        output_sockets={
            'points': ('Points', 'Points', 0, 'AUTO'),
        },
        output_type=GeometryNodeDistributePointsInVolumeOutputs,
    )

class GeometryNodeDistributePointsOnFacesOutputs(typing.NamedTuple):
    points: Socket[Geometry]
    normal: Socket[Field[Vector]]
    rotation: Socket[Field[Rotation]]

def distribute_points_on_faces(*, mesh: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, density: float | Field[float] | Socket[float | Field[float]] = 10.0, seed: int | Socket[int] = 0, distance_min: float | Socket[float] = 0.0, density_max: float | Socket[float] = 10.0, density_factor: float | Field[float] | Socket[float | Field[float]] = 1.0, distribute_method: typing.Literal['RANDOM', 'POISSON'] = 'RANDOM', use_legacy_normal: bool = False) -> GeometryNodeDistributePointsOnFacesOutputs:
    'Args:\n    distribute_method: Method to use for scattering points\n    use_legacy_normal: Output the normal and rotation values that have been output before the node started taking smooth normals into account'
    return _node_function(
        'GeometryNodeDistributePointsOnFaces',
        inputs={
            'mesh': mesh,
            'selection': selection,
            'density': density,
            'seed': seed,
            'distance_min': distance_min,
            'density_max': density_max,
            'density_factor': density_factor,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'density': ('Density', 'Density', 4, 10.0),
            'seed': ('Seed', 'Seed', 6, 0),
            'distance_min': ('Distance Min', 'Distance Min', 2, 0.0),
            'density_max': ('Density Max', 'Density Max', 3, 10.0),
            'density_factor': ('Density Factor', 'Density Factor', 5, 1.0),
        },
        properties={
            'distribute_method': distribute_method,
            'use_legacy_normal': use_legacy_normal,
        },
        output_sockets={
            'points': ('Points', 'Points', 0, 'AUTO'),
            'normal': ('Normal', 'Normal', 1, 'FIELD'),
            'rotation': ('Rotation', 'Rotation', 2, 'FIELD'),
        },
        output_type=GeometryNodeDistributePointsOnFacesOutputs,
    )

class GeometryNodeAttributeDomainSizeOutputs(typing.NamedTuple):
    point_count: Socket[int]
    edge_count: Socket[int]
    face_count: Socket[int]
    face_corner_count: Socket[int]
    spline_count: Socket[int]
    instance_count: Socket[int]
    layer_count: Socket[int]

def domain_size(*, geometry: Geometry | Socket[Geometry] | None = None, component: typing.Literal['MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES', 'GREASEPENCIL', 'VOLUME'] = 'MESH') -> GeometryNodeAttributeDomainSizeOutputs:
    return _node_function(
        'GeometryNodeAttributeDomainSize',
        inputs={
            'geometry': geometry,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
        },
        properties={
            'component': component,
        },
        output_sockets={
            'point_count': ('Point Count', 'Point Count', 0, 'AUTO'),
            'edge_count': ('Edge Count', 'Edge Count', 1, 'AUTO'),
            'face_count': ('Face Count', 'Face Count', 2, 'AUTO'),
            'face_corner_count': ('Face Corner Count', 'Face Corner Count', 3, 'AUTO'),
            'spline_count': ('Spline Count', 'Spline Count', 4, 'AUTO'),
            'instance_count': ('Instance Count', 'Instance Count', 5, 'AUTO'),
            'layer_count': ('Layer Count', 'Layer Count', 6, 'AUTO'),
        },
        output_type=GeometryNodeAttributeDomainSizeOutputs,
    )

class GeometryNodeDualMeshOutputs(typing.NamedTuple):
    dual_mesh: Socket[Geometry]

def dual_mesh(*, mesh: Geometry | Socket[Geometry] | None = None, keep_boundaries: bool | Socket[bool] = False) -> GeometryNodeDualMeshOutputs:
    return _node_function(
        'GeometryNodeDualMesh',
        inputs={
            'mesh': mesh,
            'keep_boundaries': keep_boundaries,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'keep_boundaries': ('Keep Boundaries', 'Keep Boundaries', 1, False),
        },
        properties={
        },
        output_sockets={
            'dual_mesh': ('Dual Mesh', 'Dual Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeDualMeshOutputs,
    )

class GeometryNodeDuplicateElementsOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]
    duplicate_index: Socket[Field[int]]

def duplicate_elements(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, amount: int | Field[int] | Socket[int | Field[int]] = 1, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'SPLINE', 'LAYER', 'INSTANCE'] = 'POINT') -> GeometryNodeDuplicateElementsOutputs:
    'Args:\n    domain: Which domain to duplicate'
    return _node_function(
        'GeometryNodeDuplicateElements',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'amount': amount,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'amount': ('Amount', 'Amount', 2, 1),
        },
        properties={
            'domain': domain,
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
            'duplicate_index': ('Duplicate Index', 'Duplicate Index', 1, 'FIELD'),
        },
        output_type=GeometryNodeDuplicateElementsOutputs,
    )

class GeometryNodeInputMeshEdgeAngleOutputs(typing.NamedTuple):
    unsigned_angle: Socket[Field[float]]
    signed_angle: Socket[Field[float]]

def edge_angle() -> GeometryNodeInputMeshEdgeAngleOutputs:
    return _node_function(
        'GeometryNodeInputMeshEdgeAngle',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'unsigned_angle': ('Unsigned Angle', 'Unsigned Angle', 0, 'FIELD'),
            'signed_angle': ('Signed Angle', 'Signed Angle', 1, 'FIELD'),
        },
        output_type=GeometryNodeInputMeshEdgeAngleOutputs,
    )

class GeometryNodeInputMeshEdgeNeighborsOutputs(typing.NamedTuple):
    face_count: Socket[Field[int]]

def edge_neighbors() -> GeometryNodeInputMeshEdgeNeighborsOutputs:
    return _node_function(
        'GeometryNodeInputMeshEdgeNeighbors',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'face_count': ('Face Count', 'Face Count', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputMeshEdgeNeighborsOutputs,
    )

class GeometryNodeEdgePathsToCurvesOutputs(typing.NamedTuple):
    curves: Socket[Geometry]

def edge_paths_to_curves(*, mesh: Geometry | Socket[Geometry] | None = None, start_vertices: bool | Field[bool] | Socket[bool | Field[bool]] = True, next_vertex_index: int | Field[int] | Socket[int | Field[int]] = -1) -> GeometryNodeEdgePathsToCurvesOutputs:
    return _node_function(
        'GeometryNodeEdgePathsToCurves',
        inputs={
            'mesh': mesh,
            'start_vertices': start_vertices,
            'next_vertex_index': next_vertex_index,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'start_vertices': ('Start Vertices', 'Start Vertices', 1, True),
            'next_vertex_index': ('Next Vertex Index', 'Next Vertex Index', 2, -1),
        },
        properties={
        },
        output_sockets={
            'curves': ('Curves', 'Curves', 0, 'AUTO'),
        },
        output_type=GeometryNodeEdgePathsToCurvesOutputs,
    )

class GeometryNodeEdgePathsToSelectionOutputs(typing.NamedTuple):
    selection: Socket[Field[bool]]

def edge_paths_to_selection(*, start_vertices: bool | Field[bool] | Socket[bool | Field[bool]] = True, next_vertex_index: int | Field[int] | Socket[int | Field[int]] = -1) -> GeometryNodeEdgePathsToSelectionOutputs:
    return _node_function(
        'GeometryNodeEdgePathsToSelection',
        inputs={
            'start_vertices': start_vertices,
            'next_vertex_index': next_vertex_index,
        },
        input_sockets={
            'start_vertices': ('Start Vertices', 'Start Vertices', 0, True),
            'next_vertex_index': ('Next Vertex Index', 'Next Vertex Index', 1, -1),
        },
        properties={
        },
        output_sockets={
            'selection': ('Selection', 'Selection', 0, 'FIELD'),
        },
        output_type=GeometryNodeEdgePathsToSelectionOutputs,
    )

class GeometryNodeInputMeshEdgeVerticesOutputs(typing.NamedTuple):
    vertex_index_1: Socket[Field[int]]
    vertex_index_2: Socket[Field[int]]
    position_1: Socket[Field[Vector]]
    position_2: Socket[Field[Vector]]

def edge_vertices() -> GeometryNodeInputMeshEdgeVerticesOutputs:
    return _node_function(
        'GeometryNodeInputMeshEdgeVertices',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'vertex_index_1': ('Vertex Index 1', 'Vertex Index 1', 0, 'FIELD'),
            'vertex_index_2': ('Vertex Index 2', 'Vertex Index 2', 1, 'FIELD'),
            'position_1': ('Position 1', 'Position 1', 2, 'FIELD'),
            'position_2': ('Position 2', 'Position 2', 3, 'FIELD'),
        },
        output_type=GeometryNodeInputMeshEdgeVerticesOutputs,
    )

class GeometryNodeEdgesOfCornerOutputs(typing.NamedTuple):
    next_edge_index: Socket[Field[int]]
    previous_edge_index: Socket[Field[int]]

def edges_of_corner(*, corner_index: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeEdgesOfCornerOutputs:
    return _node_function(
        'GeometryNodeEdgesOfCorner',
        inputs={
            'corner_index': corner_index,
        },
        input_sockets={
            'corner_index': ('Corner Index', 'Corner Index', 0, 0),
        },
        properties={
        },
        output_sockets={
            'next_edge_index': ('Next Edge Index', 'Next Edge Index', 0, 'FIELD'),
            'previous_edge_index': ('Previous Edge Index', 'Previous Edge Index', 1, 'FIELD'),
        },
        output_type=GeometryNodeEdgesOfCornerOutputs,
    )

class GeometryNodeEdgesOfVertexOutputs(typing.NamedTuple):
    edge_index: Socket[Field[int]]
    total: Socket[Field[int]]

def edges_of_vertex(*, vertex_index: int | Field[int] | Socket[int | Field[int]] = 0, weights: float | Field[float] | Socket[float | Field[float]] = 0.0, sort_index: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeEdgesOfVertexOutputs:
    return _node_function(
        'GeometryNodeEdgesOfVertex',
        inputs={
            'vertex_index': vertex_index,
            'weights': weights,
            'sort_index': sort_index,
        },
        input_sockets={
            'vertex_index': ('Vertex Index', 'Vertex Index', 0, 0),
            'weights': ('Weights', 'Weights', 1, 0.0),
            'sort_index': ('Sort Index', 'Sort Index', 2, 0),
        },
        properties={
        },
        output_sockets={
            'edge_index': ('Edge Index', 'Edge Index', 0, 'FIELD'),
            'total': ('Total', 'Total', 1, 'FIELD'),
        },
        output_type=GeometryNodeEdgesOfVertexOutputs,
    )

class GeometryNodeEdgesToFaceGroupsOutputs(typing.NamedTuple):
    face_group_id: Socket[Field[int]]

def edges_to_face_groups(*, boundary_edges: bool | Field[bool] | Socket[bool | Field[bool]] = True) -> GeometryNodeEdgesToFaceGroupsOutputs:
    return _node_function(
        'GeometryNodeEdgesToFaceGroups',
        inputs={
            'boundary_edges': boundary_edges,
        },
        input_sockets={
            'boundary_edges': ('Boundary Edges', 'Boundary Edges', 0, True),
        },
        properties={
        },
        output_sockets={
            'face_group_id': ('Face Group ID', 'Face Group ID', 0, 'FIELD'),
        },
        output_type=GeometryNodeEdgesToFaceGroupsOutputs,
    )

class NodeEnableOutputOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound]

def enable_output(*, enable: bool | Socket[bool] = False, value: float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound | Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound] = 0.0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> NodeEnableOutputOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'NodeEnableOutput',
        inputs={
            'enable': enable,
            'value': value,
        },
        input_sockets={
            'enable': ('Enable', 'Enable', 0, False),
            'value': ('Value', 'Value', 1, 0.0),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=NodeEnableOutputOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'BOOLEAN': {'value': 'BOOLEAN'}, 'VECTOR': {'value': 'VECTOR'}, 'RGBA': {'value': 'RGBA'}, 'ROTATION': {'value': 'ROTATION'}, 'MATRIX': {'value': 'MATRIX'}, 'STRING': {'value': 'STRING'}, 'MENU': {'value': 'MENU'}, 'OBJECT': {'value': 'OBJECT'}, 'IMAGE': {'value': 'IMAGE'}, 'GEOMETRY': {'value': 'GEOMETRY'}, 'COLLECTION': {'value': 'COLLECTION'}, 'MATERIAL': {'value': 'MATERIAL'}, 'BUNDLE': {'value': 'BUNDLE'}, 'CLOSURE': {'value': 'CLOSURE'}, 'FONT': {'value': 'FONT'}, 'SOUND': {'value': 'SOUND'}}},
    )

class GeometryNodeCurveEndpointSelectionOutputs(typing.NamedTuple):
    selection: Socket[Field[bool]]

def endpoint_selection(*, start_size: int | Field[int] | Socket[int | Field[int]] = 1, end_size: int | Field[int] | Socket[int | Field[int]] = 1) -> GeometryNodeCurveEndpointSelectionOutputs:
    return _node_function(
        'GeometryNodeCurveEndpointSelection',
        inputs={
            'start_size': start_size,
            'end_size': end_size,
        },
        input_sockets={
            'start_size': ('Start Size', 'Start Size', 0, 1),
            'end_size': ('End Size', 'End Size', 1, 1),
        },
        properties={
        },
        output_sockets={
            'selection': ('Selection', 'Selection', 0, 'FIELD'),
        },
        output_type=GeometryNodeCurveEndpointSelectionOutputs,
    )

class FunctionNodeEulerToRotationOutputs(typing.NamedTuple):
    rotation: Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]]

def euler_to_rotation(*, euler: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0)) -> FunctionNodeEulerToRotationOutputs:
    return _node_function(
        'FunctionNodeEulerToRotation',
        inputs={
            'euler': euler,
        },
        input_sockets={
            'euler': ('Euler', 'Euler', 0, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'AUTO'),
        },
        output_type=FunctionNodeEulerToRotationOutputs,
    )

class GeometryNodeFieldAtIndexOutputs(typing.NamedTuple):
    value: Socket[Field[float] | Field[int] | Field[bool] | Field[Vector] | Field[Color] | Field[Rotation] | Field[Matrix]]

def evaluate_at_index(*, value: float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix] | Socket[float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix]] = 0.0, index: int | Field[int] | Socket[int | Field[int]] = 0, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT', data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None) -> GeometryNodeFieldAtIndexOutputs:
    'Args:\n    domain: Domain the field is evaluated in\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeFieldAtIndex',
        inputs={
            'value': value,
            'index': index,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0.0),
            'index': ('Index', 'Index', 1, 0),
        },
        properties={
            'domain': domain,
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'FIELD'),
        },
        output_type=GeometryNodeFieldAtIndexOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'BOOLEAN': {'value': 'BOOLEAN'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}, 'FLOAT_COLOR': {'value': 'RGBA'}, 'QUATERNION': {'value': 'ROTATION'}, 'FLOAT4X4': {'value': 'MATRIX'}}},
    )

class NodeEvaluateClosureOutputs(ItemOutputs):
    pass

def evaluate_closure(*, closure: Closure | Socket[Closure] | None = None, define_signature: bool = False, outputs: typing.Mapping[str, typing.Any] | None = None, **items: typing.Any) -> NodeEvaluateClosureOutputs:
    'Args:\n    define_signature: This node defines a closure signature that should be used by other nodes\n    items: Items to add, by name; each socket type is inferred from its value.\n    outputs: Items to add, mapping each name to its type (float, Vector, Geometry, ...). Their outputs are available by name on the result.'
    return _node_function(
        'NodeEvaluateClosure',
        inputs={
            'closure': closure,
        },
        input_sockets={
            'closure': ('Closure', 'Closure', 0, None),
        },
        properties={
            'define_signature': define_signature,
        },
        output_sockets={
        },
        output_type=NodeEvaluateClosureOutputs,
        item_collections=(
            ('input_items', 'values', items),
            ('output_items', 'types', outputs),
        ),
    )

class GeometryNodeFieldOnDomainOutputs(typing.NamedTuple):
    value: Socket[Field[float] | Field[int] | Field[bool] | Field[Vector] | Field[Color] | Field[Rotation] | Field[Matrix]]

def evaluate_on_domain(*, value: float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix] | Socket[float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix]] = 0.0, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT', data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None) -> GeometryNodeFieldOnDomainOutputs:
    'Args:\n    domain: Domain the field is evaluated in\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeFieldOnDomain',
        inputs={
            'value': value,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0.0),
        },
        properties={
            'domain': domain,
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'FIELD'),
        },
        output_type=GeometryNodeFieldOnDomainOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'BOOLEAN': {'value': 'BOOLEAN'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}, 'FLOAT_COLOR': {'value': 'RGBA'}, 'QUATERNION': {'value': 'ROTATION'}, 'FLOAT4X4': {'value': 'MATRIX'}}},
    )

class GeometryNodeExtrudeMeshOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]
    top: Socket[Field[bool]]
    side: Socket[Field[bool]]

def extrude_mesh(*, mesh: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, offset: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), offset_scale: float | Field[float] | Socket[float | Field[float]] = 1.0, individual: bool | Socket[bool] = True, mode: typing.Literal['VERTICES', 'EDGES', 'FACES'] = 'FACES') -> GeometryNodeExtrudeMeshOutputs:
    return _node_function(
        'GeometryNodeExtrudeMesh',
        inputs={
            'mesh': mesh,
            'selection': selection,
            'offset': offset,
            'offset_scale': offset_scale,
            'individual': individual,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'offset': ('Offset', 'Offset', 2, (0.0, 0.0, 0.0)),
            'offset_scale': ('Offset Scale', 'Offset Scale', 3, 1.0),
            'individual': ('Individual', 'Individual', 4, True),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
            'top': ('Top', 'Top', 1, 'FIELD'),
            'side': ('Side', 'Side', 2, 'FIELD'),
        },
        output_type=GeometryNodeExtrudeMeshOutputs,
    )

class GeometryNodeInputMeshFaceAreaOutputs(typing.NamedTuple):
    area: Socket[Field[float]]

def face_area() -> GeometryNodeInputMeshFaceAreaOutputs:
    return _node_function(
        'GeometryNodeInputMeshFaceArea',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'area': ('Area', 'Area', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputMeshFaceAreaOutputs,
    )

class GeometryNodeMeshFaceSetBoundariesOutputs(typing.NamedTuple):
    boundary_edges: Socket[Field[bool]]

def face_group_boundaries(*, face_group_id: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeMeshFaceSetBoundariesOutputs:
    return _node_function(
        'GeometryNodeMeshFaceSetBoundaries',
        inputs={
            'face_group_id': face_group_id,
        },
        input_sockets={
            'face_group_id': ('Face Set', 'Face Group ID', 0, 0),
        },
        properties={
        },
        output_sockets={
            'boundary_edges': ('Boundary Edges', 'Boundary Edges', 0, 'FIELD'),
        },
        output_type=GeometryNodeMeshFaceSetBoundariesOutputs,
    )

class GeometryNodeInputMeshFaceNeighborsOutputs(typing.NamedTuple):
    vertex_count: Socket[Field[int]]
    face_count: Socket[Field[int]]

def face_neighbors() -> GeometryNodeInputMeshFaceNeighborsOutputs:
    return _node_function(
        'GeometryNodeInputMeshFaceNeighbors',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'vertex_count': ('Vertex Count', 'Vertex Count', 0, 'FIELD'),
            'face_count': ('Face Count', 'Face Count', 1, 'FIELD'),
        },
        output_type=GeometryNodeInputMeshFaceNeighborsOutputs,
    )

class GeometryNodeFaceOfCornerOutputs(typing.NamedTuple):
    face_index: Socket[Field[int]]
    index_in_face: Socket[Field[int]]

def face_of_corner(*, corner_index: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeFaceOfCornerOutputs:
    return _node_function(
        'GeometryNodeFaceOfCorner',
        inputs={
            'corner_index': corner_index,
        },
        input_sockets={
            'corner_index': ('Corner Index', 'Corner Index', 0, 0),
        },
        properties={
        },
        output_sockets={
            'face_index': ('Face Index', 'Face Index', 0, 'FIELD'),
            'index_in_face': ('Index in Face', 'Index in Face', 1, 'FIELD'),
        },
        output_type=GeometryNodeFaceOfCornerOutputs,
    )

class GeometryNodeToolFaceSetOutputs(typing.NamedTuple):
    face_set: Socket[Field[int]]
    exists: Socket[Field[bool]]

def face_set() -> GeometryNodeToolFaceSetOutputs:
    return _node_function(
        'GeometryNodeToolFaceSet',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'face_set': ('Face Set', 'Face Set', 0, 'FIELD'),
            'exists': ('Exists', 'Exists', 1, 'FIELD'),
        },
        output_type=GeometryNodeToolFaceSetOutputs,
    )

class GeometryNodeFieldAverageOutputs(typing.NamedTuple):
    mean: Socket[Field[float] | Field[Vector]]
    median: Socket[Field[float] | Field[Vector]]

def field_average(*, value: float | Field[float] | Vector | Field[Vector] | Socket[float | Field[float] | Vector | Field[Vector]] = 0.0, group_id: int | Field[int] | Socket[int | Field[int]] = 0, data_type: typing.Literal['FLOAT', 'FLOAT_VECTOR'] | None = None, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT') -> GeometryNodeFieldAverageOutputs:
    'Args:\n    data_type: Type of data the outputs are calculated from Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeFieldAverage',
        inputs={
            'value': value,
            'group_id': group_id,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0.0),
            'group_id': ('Group Index', 'Group ID', 1, 0),
        },
        properties={
            'data_type': data_type,
            'domain': domain,
        },
        output_sockets={
            'mean': ('Mean', 'Mean', 0, 'FIELD'),
            'median': ('Median', 'Median', 1, 'FIELD'),
        },
        output_type=GeometryNodeFieldAverageOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}}},
    )

class GeometryNodeFieldMinAndMaxOutputs(typing.NamedTuple):
    min: Socket[Field[float] | Field[int] | Field[Vector]]
    max: Socket[Field[float] | Field[int] | Field[Vector]]

def field_min_max(*, value: float | Field[float] | int | Field[int] | Vector | Field[Vector] | Socket[float | Field[float] | int | Field[int] | Vector | Field[Vector]] = 0.0, group_id: int | Field[int] | Socket[int | Field[int]] = 0, data_type: typing.Literal['FLOAT', 'INT', 'FLOAT_VECTOR'] | None = None, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT') -> GeometryNodeFieldMinAndMaxOutputs:
    'Args:\n    data_type: Type of data the outputs are calculated from Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeFieldMinAndMax',
        inputs={
            'value': value,
            'group_id': group_id,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0.0),
            'group_id': ('Group Index', 'Group ID', 1, 0),
        },
        properties={
            'data_type': data_type,
            'domain': domain,
        },
        output_sockets={
            'min': ('Min', 'Min', 0, 'FIELD'),
            'max': ('Max', 'Max', 1, 'FIELD'),
        },
        output_type=GeometryNodeFieldMinAndMaxOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}}},
    )

class GeometryNodeFieldToGridOutputs(ItemOutputs):
    pass

def field_to_grid(*, topology: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None, **items: typing.Any) -> GeometryNodeFieldToGridOutputs:
    'Args:\n    data_type: Data type for topology grid Inferred from the linked inputs when None.\n    items: Items to add, by name; each socket type is inferred from its value. Their outputs are available by name on the result.'
    return _node_function(
        'GeometryNodeFieldToGrid',
        inputs={
            'topology': topology,
        },
        input_sockets={
            'topology': ('Topology', 'Topology', 0, None),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
        },
        output_type=GeometryNodeFieldToGridOutputs,
        item_collections=(
            ('grid_items', 'values', items),
        ),
        type_properties={'data_type': {'FLOAT': {'topology': 'VALUE'}, 'INT': {'topology': 'INT'}, 'BOOLEAN': {'topology': 'BOOLEAN'}, 'VECTOR': {'topology': 'VECTOR'}}},
    )

class GeometryNodeFieldToListOutputs(ItemOutputs):
    pass

def field_to_list(*, count: int | Socket[int] = 1, **items: typing.Any) -> GeometryNodeFieldToListOutputs:
    'Args:\n    items: Items to add, by name; each socket type is inferred from its value. Their outputs are available by name on the result.'
    return _node_function(
        'GeometryNodeFieldToList',
        inputs={
            'count': count,
        },
        input_sockets={
            'count': ('Count', 'Count', 0, 1),
        },
        properties={
        },
        output_sockets={
        },
        output_type=GeometryNodeFieldToListOutputs,
        item_collections=(
            ('list_items', 'values', items),
        ),
    )

class GeometryNodeFieldVarianceOutputs(typing.NamedTuple):
    standard_deviation: Socket[Field[float] | Field[Vector]]
    variance: Socket[Field[float] | Field[Vector]]

def field_variance(*, value: float | Field[float] | Vector | Field[Vector] | Socket[float | Field[float] | Vector | Field[Vector]] = 0.0, group_id: int | Field[int] | Socket[int | Field[int]] = 0, data_type: typing.Literal['FLOAT', 'FLOAT_VECTOR'] | None = None, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT') -> GeometryNodeFieldVarianceOutputs:
    'Args:\n    data_type: Type of data the outputs are calculated from Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeFieldVariance',
        inputs={
            'value': value,
            'group_id': group_id,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0.0),
            'group_id': ('Group Index', 'Group ID', 1, 0),
        },
        properties={
            'data_type': data_type,
            'domain': domain,
        },
        output_sockets={
            'standard_deviation': ('Standard Deviation', 'Standard Deviation', 0, 'FIELD'),
            'variance': ('Variance', 'Variance', 1, 'FIELD'),
        },
        output_type=GeometryNodeFieldVarianceOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}}},
    )

class GeometryNodeFillCurveOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def fill_curve(*, curve: Geometry | Socket[Geometry] | None = None, group_id: int | Field[int] | Socket[int | Field[int]] = 0, mode: Menu | Socket[Menu] = 'Triangles', fill_rule: Menu | Socket[Menu] = 'Even-Odd') -> GeometryNodeFillCurveOutputs:
    return _node_function(
        'GeometryNodeFillCurve',
        inputs={
            'curve': curve,
            'group_id': group_id,
            'mode': mode,
            'fill_rule': fill_rule,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'group_id': ('Group ID', 'Group ID', 1, 0),
            'mode': ('Mode', 'Mode', 2, 'Triangles'),
            'fill_rule': ('Fill Rule', 'Fill Rule', 3, 'Even-Odd'),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeFillCurveOutputs,
    )

class GeometryNodeFilletCurveOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def fillet_curve(*, curve: Geometry | Socket[Geometry] | None = None, radius: float | Field[float] | Socket[float | Field[float]] = 0.25, limit_radius: bool | Socket[bool] = False, mode: Menu | Socket[Menu] = 'Bézier', count: int | Field[int] | Socket[int | Field[int]] = 1) -> GeometryNodeFilletCurveOutputs:
    return _node_function(
        'GeometryNodeFilletCurve',
        inputs={
            'curve': curve,
            'radius': radius,
            'limit_radius': limit_radius,
            'mode': mode,
            'count': count,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'radius': ('Radius', 'Radius', 1, 0.25),
            'limit_radius': ('Limit Radius', 'Limit Radius', 2, False),
            'mode': ('Mode', 'Mode', 3, 'Bézier'),
            'count': ('Count', 'Count', 4, 1),
        },
        properties={
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeFilletCurveOutputs,
    )

class GeometryNodeFilterListOutputs(typing.NamedTuple):
    selection: Socket[List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound]]
    inverted: Socket[List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound]]

def filter_list(*, list: List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound] | Socket[List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound]] | None = None, selection: bool | Field[bool] | Grid[bool] | List[bool] | Socket[bool | Field[bool] | Grid[bool] | List[bool]] = True, socket_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeFilterListOutputs:
    'Args:\n    socket_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeFilterList',
        inputs={
            'list': list,
            'selection': selection,
        },
        input_sockets={
            'list': ('List', 'List', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
            'socket_type': socket_type,
        },
        output_sockets={
            'selection': ('Selection', 'Selection', 0, 'LIST'),
            'inverted': ('Inverted', 'Inverted', 1, 'LIST'),
        },
        output_type=GeometryNodeFilterListOutputs,
        type_properties={'socket_type': {'FLOAT': {'list': 'VALUE'}, 'INT': {'list': 'INT'}, 'BOOLEAN': {'list': 'BOOLEAN'}, 'VECTOR': {'list': 'VECTOR'}, 'RGBA': {'list': 'RGBA'}, 'ROTATION': {'list': 'ROTATION'}, 'MATRIX': {'list': 'MATRIX'}, 'STRING': {'list': 'STRING'}, 'MENU': {'list': 'MENU'}, 'OBJECT': {'list': 'OBJECT'}, 'IMAGE': {'list': 'IMAGE'}, 'GEOMETRY': {'list': 'GEOMETRY'}, 'COLLECTION': {'list': 'COLLECTION'}, 'MATERIAL': {'list': 'MATERIAL'}, 'BUNDLE': {'list': 'BUNDLE'}, 'CLOSURE': {'list': 'CLOSURE'}, 'FONT': {'list': 'FONT'}, 'SOUND': {'list': 'SOUND'}}},
    )

class FunctionNodeFindInStringOutputs(typing.NamedTuple):
    first_found: Socket[int | Field[int] | Grid[int] | List[int]]
    count: Socket[int | Field[int] | Grid[int] | List[int]]

def find_in_string(*, string: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', search: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', mode: Menu | Socket[Menu] = 'From Start') -> FunctionNodeFindInStringOutputs:
    return _node_function(
        'FunctionNodeFindInString',
        inputs={
            'string': string,
            'search': search,
            'mode': mode,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
            'search': ('Search', 'Search', 1, ''),
            'mode': ('Mode', 'Mode', 2, 'From Start'),
        },
        properties={
        },
        output_sockets={
            'first_found': ('First Found', 'First Found', 0, 'AUTO'),
            'count': ('Count', 'Count', 1, 'AUTO'),
        },
        output_type=FunctionNodeFindInStringOutputs,
    )

class GeometryNodeFlipFacesOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def flip_faces(*, mesh: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True) -> GeometryNodeFlipFacesOutputs:
    return _node_function(
        'GeometryNodeFlipFaces',
        inputs={
            'mesh': mesh,
            'selection': selection,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeFlipFacesOutputs,
    )

class ShaderNodeFloatCurveOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float]]

def float_curve(*, factor: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, value: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0) -> ShaderNodeFloatCurveOutputs:
    return _node_function(
        'ShaderNodeFloatCurve',
        inputs={
            'factor': factor,
            'value': value,
        },
        input_sockets={
            'factor': ('Factor', 'Factor', 0, 1.0),
            'value': ('Value', 'Value', 1, 1.0),
        },
        properties={
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=ShaderNodeFloatCurveOutputs,
    )

class FunctionNodeFloatToIntOutputs(typing.NamedTuple):
    integer: Socket[int | Field[int] | Grid[int] | List[int]]

def float_to_integer(*, float: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, rounding_mode: typing.Literal['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE'] = 'ROUND') -> FunctionNodeFloatToIntOutputs:
    'Args:\n    rounding_mode: Method used to convert the float to an integer'
    return _node_function(
        'FunctionNodeFloatToInt',
        inputs={
            'float': float,
        },
        input_sockets={
            'float': ('Float', 'Float', 0, 0.0),
        },
        properties={
            'rounding_mode': rounding_mode,
        },
        output_sockets={
            'integer': ('Integer', 'Integer', 0, 'AUTO'),
        },
        output_type=FunctionNodeFloatToIntOutputs,
    )

class GeometryNodeInputFontOutputs(typing.NamedTuple):
    font: Socket[Font]

def font(*, font: bpy.types.VectorFont | None) -> GeometryNodeInputFontOutputs:
    return _node_function(
        'GeometryNodeInputFont',
        inputs={
        },
        input_sockets={
        },
        properties={
            'font': font,
        },
        output_sockets={
            'font': ('Font', 'Font', 0, 'AUTO'),
        },
        output_type=GeometryNodeInputFontOutputs,
    )

class FunctionNodeFormatStringOutputs(typing.NamedTuple):
    string: Socket[str | Field[str] | Grid[str] | List[str]]

def format_string(*, format: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', **items: typing.Any) -> FunctionNodeFormatStringOutputs:
    'Args:\n    items: Items to add, by name; each socket type is inferred from its value.'
    return _node_function(
        'FunctionNodeFormatString',
        inputs={
            'format': format,
        },
        input_sockets={
            'format': ('Format', 'Format', 0, ''),
        },
        properties={
        },
        output_sockets={
            'string': ('String', 'String', 0, 'AUTO'),
        },
        output_type=FunctionNodeFormatStringOutputs,
        item_collections=(
            ('format_items', 'values', items),
        ),
    )

class ShaderNodeTexGaborOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float]]
    phase: Socket[float | Field[float] | Grid[float] | List[float]]
    intensity: Socket[float | Field[float] | Grid[float] | List[float]]

def gabor_texture(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), scale: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 5.0, frequency: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 2.0, anisotropy: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, orientation: float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector]] = 0.7853981852531433, gabor_type: typing.Literal['2D', '3D'] | None = None) -> ShaderNodeTexGaborOutputs:
    'Args:\n    gabor_type: The type of Gabor noise to evaluate Inferred from the linked inputs when None.'
    return _node_function(
        'ShaderNodeTexGabor',
        inputs={
            'vector': vector,
            'scale': scale,
            'frequency': frequency,
            'anisotropy': anisotropy,
            'orientation': orientation,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'scale': ('Scale', 'Scale', 1, 5.0),
            'frequency': ('Frequency', 'Frequency', 2, 2.0),
            'anisotropy': ('Anisotropy', 'Anisotropy', 3, 1.0),
            'orientation': ('Orientation 2D', 'Orientation', 4, 0.7853981852531433),
        },
        properties={
            'gabor_type': gabor_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'FIELD'),
            'phase': ('Phase', 'Phase', 1, 'FIELD'),
            'intensity': ('Intensity', 'Intensity', 2, 'FIELD'),
        },
        output_type=ShaderNodeTexGaborOutputs,
        type_properties={'gabor_type': {'2D': {'orientation': 'VALUE'}, '3D': {'orientation': 'VECTOR'}}},
    )

class ShaderNodeGammaOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]

def gamma(*, color: Color | Field[Color] | Grid[Color] | List[Color] | Socket[Color | Field[Color] | Grid[Color] | List[Color]] = (1.0, 1.0, 1.0, 1.0), gamma: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0) -> ShaderNodeGammaOutputs:
    return _node_function(
        'ShaderNodeGamma',
        inputs={
            'color': color,
            'gamma': gamma,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 1.0, 1.0, 1.0)),
            'gamma': ('Gamma', 'Gamma', 1, 1.0),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeGammaOutputs,
    )

class GeometryNodeProximityOutputs(typing.NamedTuple):
    position: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    distance: Socket[float | Field[float] | Grid[float] | List[float]]
    is_valid: Socket[bool | Field[bool] | Grid[bool] | List[bool]]

def geometry_proximity(*, geometry: Geometry | Socket[Geometry] | None = None, group_id: int | Field[int] | Socket[int | Field[int]] = 0, sample_position: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), sample_group_id: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, target_element: typing.Literal['POINTS', 'EDGES', 'FACES'] = 'FACES') -> GeometryNodeProximityOutputs:
    'Args:\n    target_element: Element of the target geometry to calculate the distance from'
    return _node_function(
        'GeometryNodeProximity',
        inputs={
            'geometry': geometry,
            'group_id': group_id,
            'sample_position': sample_position,
            'sample_group_id': sample_group_id,
        },
        input_sockets={
            'geometry': ('Target', 'Geometry', 0, None),
            'group_id': ('Group ID', 'Group ID', 1, 0),
            'sample_position': ('Source Position', 'Sample Position', 2, (0.0, 0.0, 0.0)),
            'sample_group_id': ('Sample Group ID', 'Sample Group ID', 3, 0),
        },
        properties={
            'target_element': target_element,
        },
        output_sockets={
            'position': ('Position', 'Position', 0, 'FIELD'),
            'distance': ('Distance', 'Distance', 1, 'FIELD'),
            'is_valid': ('Is Valid', 'Is Valid', 2, 'FIELD'),
        },
        output_type=GeometryNodeProximityOutputs,
    )

class GeometryNodeGeometryToInstanceOutputs(typing.NamedTuple):
    instances: Socket[Geometry]

def geometry_to_instance(*, geometry: typing.Sequence[Geometry | Socket[Geometry]] = ()) -> GeometryNodeGeometryToInstanceOutputs:
    return _node_function(
        'GeometryNodeGeometryToInstance',
        inputs={
            'geometry': geometry,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, ()),
        },
        properties={
        },
        output_sockets={
            'instances': ('Instances', 'Instances', 0, 'AUTO'),
        },
        output_type=GeometryNodeGeometryToInstanceOutputs,
    )

class GeometryNodeGetAttributeNamesOutputs(typing.NamedTuple):
    names: Socket[List[str]]

def get_attribute_names(*, geometry: Geometry | Socket[Geometry] | None = None, filter_data_type: bool | Socket[bool] = False, data_type: Menu | Socket[Menu] = 'Float', filter_domain: bool | Socket[bool] = False, domain: Menu | Socket[Menu] = 'Point') -> GeometryNodeGetAttributeNamesOutputs:
    return _node_function(
        'GeometryNodeGetAttributeNames',
        inputs={
            'geometry': geometry,
            'filter_data_type': filter_data_type,
            'data_type': data_type,
            'filter_domain': filter_domain,
            'domain': domain,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'filter_data_type': ('Filter Data Type', 'Filter Data Type', 1, False),
            'data_type': ('Data Type', 'Data Type', 2, 'Float'),
            'filter_domain': ('Filter Domain', 'Filter Domain', 3, False),
            'domain': ('Domain', 'Domain', 4, 'Point'),
        },
        properties={
        },
        output_sockets={
            'names': ('Names', 'Names', 0, 'LIST'),
        },
        output_type=GeometryNodeGetAttributeNamesOutputs,
    )

class NodeGetBundleItemOutputs(typing.NamedTuple):
    bundle: Socket[Bundle]
    item: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound]
    exists: Socket[bool]

def get_bundle_item(*, bundle: Bundle | Socket[Bundle] | None = None, path: str | Socket[str] = '', remove: bool | Socket[bool] = False, socket_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None, structure_type: typing.Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO') -> NodeGetBundleItemOutputs:
    'Args:\n    socket_type: Value may be implicitly converted if the type does not match Inferred from the linked inputs when None.\n    structure_type: What kind of higher order types are expected to flow through this socket'
    return _node_function(
        'NodeGetBundleItem',
        inputs={
            'bundle': bundle,
            'path': path,
            'remove': remove,
        },
        input_sockets={
            'bundle': ('Bundle', 'Bundle', 0, None),
            'path': ('Path', 'Path', 1, ''),
            'remove': ('Remove', 'Remove', 2, False),
        },
        properties={
            'socket_type': socket_type,
            'structure_type': structure_type,
        },
        output_sockets={
            'bundle': ('Bundle', 'Bundle', 0, 'AUTO'),
            'item': ('Item', 'Item', 1, 'AUTO'),
            'exists': ('Exists', 'Exists', 2, 'AUTO'),
        },
        output_type=NodeGetBundleItemOutputs,
        type_properties={'socket_type': {'FLOAT': {}, 'INT': {}, 'BOOLEAN': {}, 'VECTOR': {}, 'RGBA': {}, 'ROTATION': {}, 'MATRIX': {}, 'STRING': {}, 'MENU': {}, 'OBJECT': {}, 'IMAGE': {}, 'GEOMETRY': {}, 'COLLECTION': {}, 'MATERIAL': {}, 'BUNDLE': {}, 'CLOSURE': {}, 'FONT': {}, 'SOUND': {}}},
    )

class GeometryNodeGetGeometryBundleOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]
    bundle: Socket[Bundle]

def get_geometry_bundle(*, geometry: Geometry | Socket[Geometry] | None = None, remove: bool | Socket[bool] = False) -> GeometryNodeGetGeometryBundleOutputs:
    return _node_function(
        'GeometryNodeGetGeometryBundle',
        inputs={
            'geometry': geometry,
            'remove': remove,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'remove': ('Remove', 'Remove', 1, False),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
            'bundle': ('Bundle', 'Bundle', 1, 'AUTO'),
        },
        output_type=GeometryNodeGetGeometryBundleOutputs,
    )

class GeometryNodeGetGeometryComponentOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]
    component: Socket[Geometry]
    exists: Socket[bool]

def get_geometry_component(*, geometry: Geometry | Socket[Geometry] | None = None, type: Menu | Socket[Menu] = 'Mesh', remove: bool | Socket[bool] = True) -> GeometryNodeGetGeometryComponentOutputs:
    return _node_function(
        'GeometryNodeGetGeometryComponent',
        inputs={
            'geometry': geometry,
            'type': type,
            'remove': remove,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'type': ('Type', 'Type', 1, 'Mesh'),
            'remove': ('Remove', 'Remove', 2, True),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
            'component': ('Component', 'Component', 1, 'AUTO'),
            'exists': ('Exists', 'Exists', 2, 'AUTO'),
        },
        output_type=GeometryNodeGetGeometryComponentOutputs,
    )

class GeometryNodeListGetItemOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound]

def get_list_item(*, list: List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound] | Socket[List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound]] | None = None, index: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, socket_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None, structure_type: typing.Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO') -> GeometryNodeListGetItemOutputs:
    'Args:\n    socket_type: Value may be implicitly converted if the type does not match Inferred from the linked inputs when None.\n    structure_type: What kind of higher order types are expected to flow through this socket'
    return _node_function(
        'GeometryNodeListGetItem',
        inputs={
            'list': list,
            'index': index,
        },
        input_sockets={
            'list': ('List', 'List', 0, None),
            'index': ('Index', 'Index', 1, 0),
        },
        properties={
            'socket_type': socket_type,
            'structure_type': structure_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=GeometryNodeListGetItemOutputs,
        type_properties={'socket_type': {'FLOAT': {'list': 'VALUE'}, 'INT': {'list': 'INT'}, 'BOOLEAN': {'list': 'BOOLEAN'}, 'VECTOR': {'list': 'VECTOR'}, 'RGBA': {'list': 'RGBA'}, 'ROTATION': {'list': 'ROTATION'}, 'MATRIX': {'list': 'MATRIX'}, 'STRING': {'list': 'STRING'}, 'MENU': {'list': 'MENU'}, 'OBJECT': {'list': 'OBJECT'}, 'IMAGE': {'list': 'IMAGE'}, 'GEOMETRY': {'list': 'GEOMETRY'}, 'COLLECTION': {'list': 'COLLECTION'}, 'MATERIAL': {'list': 'MATERIAL'}, 'BUNDLE': {'list': 'BUNDLE'}, 'CLOSURE': {'list': 'CLOSURE'}, 'FONT': {'list': 'FONT'}, 'SOUND': {'list': 'SOUND'}}},
    )

class GeometryNodeGetNamedGridOutputs(typing.NamedTuple):
    volume: Socket[Geometry]
    grid: Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]]

def get_named_grid(*, volume: Geometry | Socket[Geometry] | None = None, name: str | Socket[str] = '', remove: bool | Socket[bool] = True, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeGetNamedGridOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeGetNamedGrid',
        inputs={
            'volume': volume,
            'name': name,
            'remove': remove,
        },
        input_sockets={
            'volume': ('Volume', 'Volume', 0, None),
            'name': ('Name', 'Name', 1, ''),
            'remove': ('Remove', 'Remove', 2, True),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'volume': ('Volume', 'Volume', 0, 'AUTO'),
            'grid': ('Grid', 'Grid', 1, 'GRID'),
        },
        output_type=GeometryNodeGetNamedGridOutputs,
        type_properties={'data_type': {'FLOAT': {}, 'INT': {}, 'BOOLEAN': {}, 'VECTOR': {}}},
    )

class NodeGetNestedBundlePathsOutputs(typing.NamedTuple):
    paths: Socket[List[str]]

def get_nested_bundle_paths(*, bundle: Bundle | Socket[Bundle] | None = None, mode: Menu | Socket[Menu] = 'All', pattern_mode: Menu | Socket[Menu] = 'Exact', bundle_type: str | Socket[str] = '', data_type: Menu | Socket[Menu] = 'Float') -> NodeGetNestedBundlePathsOutputs:
    return _node_function(
        'NodeGetNestedBundlePaths',
        inputs={
            'bundle': bundle,
            'mode': mode,
            'pattern_mode': pattern_mode,
            'bundle_type': bundle_type,
            'data_type': data_type,
        },
        input_sockets={
            'bundle': ('Bundle', 'Bundle', 0, None),
            'mode': ('Mode', 'Mode', 1, 'All'),
            'pattern_mode': ('Pattern Mode', 'Pattern Mode', 2, 'Exact'),
            'bundle_type': ('Bundle Type', 'Bundle Type', 3, ''),
            'data_type': ('Data Type', 'Data Type', 4, 'Float'),
        },
        properties={
        },
        output_sockets={
            'paths': ('Paths', 'Paths', 0, 'LIST'),
        },
        output_type=NodeGetNestedBundlePathsOutputs,
    )

class ShaderNodeTexGradientOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]
    factor: Socket[float | Field[float] | Grid[float] | List[float]]

def gradient_texture(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), gradient_type: typing.Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR') -> ShaderNodeTexGradientOutputs:
    'Args:\n    gradient_type: Style of the color blending'
    return _node_function(
        'ShaderNodeTexGradient',
        inputs={
            'vector': vector,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
        },
        properties={
            'gradient_type': gradient_type,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'FIELD'),
            'factor': ('Fac', 'Factor', 1, 'FIELD'),
        },
        output_type=ShaderNodeTexGradientOutputs,
    )

class GeometryNodeGreasePencilToCurvesOutputs(typing.NamedTuple):
    curves: Socket[Geometry]

def grease_pencil_to_curves(*, grease_pencil: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, layers_as_instances: bool | Socket[bool] = True) -> GeometryNodeGreasePencilToCurvesOutputs:
    return _node_function(
        'GeometryNodeGreasePencilToCurves',
        inputs={
            'grease_pencil': grease_pencil,
            'selection': selection,
            'layers_as_instances': layers_as_instances,
        },
        input_sockets={
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'layers_as_instances': ('Layers as Instances', 'Layers as Instances', 2, True),
        },
        properties={
        },
        output_sockets={
            'curves': ('Curves', 'Curves', 0, 'AUTO'),
        },
        output_type=GeometryNodeGreasePencilToCurvesOutputs,
    )

class GeometryNodeMeshGridOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]
    uv_map: Socket[Field[Vector]]

def grid(*, size_x: float | Socket[float] = 1.0, size_y: float | Socket[float] = 1.0, vertices_x: int | Socket[int] = 3, vertices_y: int | Socket[int] = 3) -> GeometryNodeMeshGridOutputs:
    return _node_function(
        'GeometryNodeMeshGrid',
        inputs={
            'size_x': size_x,
            'size_y': size_y,
            'vertices_x': vertices_x,
            'vertices_y': vertices_y,
        },
        input_sockets={
            'size_x': ('Size X', 'Size X', 0, 1.0),
            'size_y': ('Size Y', 'Size Y', 1, 1.0),
            'vertices_x': ('Vertices X', 'Vertices X', 2, 3),
            'vertices_y': ('Vertices Y', 'Vertices Y', 3, 3),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
            'uv_map': ('UV Map', 'UV Map', 1, 'FIELD'),
        },
        output_type=GeometryNodeMeshGridOutputs,
    )

class GeometryNodeGridCurlOutputs(typing.NamedTuple):
    curl: Socket[Grid[Vector]]

def grid_curl(*, grid: Grid[Vector] | Socket[Grid[Vector]] | None = None) -> GeometryNodeGridCurlOutputs:
    return _node_function(
        'GeometryNodeGridCurl',
        inputs={
            'grid': grid,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
        },
        properties={
        },
        output_sockets={
            'curl': ('Curl', 'Curl', 0, 'GRID'),
        },
        output_type=GeometryNodeGridCurlOutputs,
    )

class GeometryNodeGridDilateAndErodeOutputs(typing.NamedTuple):
    grid: Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]]

def grid_dilate_erode(*, grid: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, connectivity: Menu | Socket[Menu] = 'Face', tiles: Menu | Socket[Menu] = 'Preserve', steps: int | Socket[int] = 1, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeGridDilateAndErodeOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeGridDilateAndErode',
        inputs={
            'grid': grid,
            'connectivity': connectivity,
            'tiles': tiles,
            'steps': steps,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'connectivity': ('Connectivity', 'Connectivity', 1, 'Face'),
            'tiles': ('Tiles', 'Tiles', 2, 'Preserve'),
            'steps': ('Steps', 'Steps', 3, 1),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeGridDilateAndErodeOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'BOOLEAN': {'grid': 'BOOLEAN'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class GeometryNodeGridDivergenceOutputs(typing.NamedTuple):
    divergence: Socket[Grid[float]]

def grid_divergence(*, grid: Grid[Vector] | Socket[Grid[Vector]] | None = None) -> GeometryNodeGridDivergenceOutputs:
    return _node_function(
        'GeometryNodeGridDivergence',
        inputs={
            'grid': grid,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
        },
        properties={
        },
        output_sockets={
            'divergence': ('Divergence', 'Divergence', 0, 'GRID'),
        },
        output_type=GeometryNodeGridDivergenceOutputs,
    )

class GeometryNodeGridGradientOutputs(typing.NamedTuple):
    gradient: Socket[Grid[Vector]]

def grid_gradient(*, grid: Grid[float] | Socket[Grid[float]] | None = None) -> GeometryNodeGridGradientOutputs:
    return _node_function(
        'GeometryNodeGridGradient',
        inputs={
            'grid': grid,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
        },
        properties={
        },
        output_sockets={
            'gradient': ('Gradient', 'Gradient', 0, 'GRID'),
        },
        output_type=GeometryNodeGridGradientOutputs,
    )

class GeometryNodeGridInfoOutputs(typing.NamedTuple):
    transform: Socket[Matrix]
    background_value: Socket[float | int | bool | Vector]

def grid_info(*, grid: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeGridInfoOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeGridInfo',
        inputs={
            'grid': grid,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'transform': ('Transform', 'Transform', 0, 'AUTO'),
            'background_value': ('Background Value', 'Background Value', 1, 'AUTO'),
        },
        output_type=GeometryNodeGridInfoOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'BOOLEAN': {'grid': 'BOOLEAN'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class GeometryNodeGridLaplacianOutputs(typing.NamedTuple):
    laplacian: Socket[Grid[float]]

def grid_laplacian(*, grid: Grid[float] | Socket[Grid[float]] | None = None) -> GeometryNodeGridLaplacianOutputs:
    return _node_function(
        'GeometryNodeGridLaplacian',
        inputs={
            'grid': grid,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
        },
        properties={
        },
        output_sockets={
            'laplacian': ('Laplacian', 'Laplacian', 0, 'GRID'),
        },
        output_type=GeometryNodeGridLaplacianOutputs,
    )

class GeometryNodeGridMeanOutputs(typing.NamedTuple):
    grid: Socket[Grid[float] | Grid[int] | Grid[Vector]]

def grid_mean(*, grid: Grid[float] | Grid[int] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[Vector]] | None = None, width: int | Socket[int] = 1, iterations: int | Socket[int] = 1, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeGridMeanOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeGridMean',
        inputs={
            'grid': grid,
            'width': width,
            'iterations': iterations,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'width': ('Width', 'Width', 1, 1),
            'iterations': ('Iterations', 'Iterations', 2, 1),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeGridMeanOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class GeometryNodeGridMedianOutputs(typing.NamedTuple):
    grid: Socket[Grid[float] | Grid[int] | Grid[Vector]]

def grid_median(*, grid: Grid[float] | Grid[int] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[Vector]] | None = None, width: int | Socket[int] = 1, iterations: int | Socket[int] = 1, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeGridMedianOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeGridMedian',
        inputs={
            'grid': grid,
            'width': width,
            'iterations': iterations,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'width': ('Width', 'Width', 1, 1),
            'iterations': ('Iterations', 'Iterations', 2, 1),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeGridMedianOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class GeometryNodeGridToMeshOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def grid_to_mesh(*, grid: Grid[float] | Socket[Grid[float]] | None = None, threshold: float | Socket[float] = 0.10000000149011612, adaptivity: float | Socket[float] = 0.0) -> GeometryNodeGridToMeshOutputs:
    return _node_function(
        'GeometryNodeGridToMesh',
        inputs={
            'grid': grid,
            'threshold': threshold,
            'adaptivity': adaptivity,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'threshold': ('Threshold', 'Threshold', 1, 0.10000000149011612),
            'adaptivity': ('Adaptivity', 'Adaptivity', 2, 0.0),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeGridToMeshOutputs,
    )

class GeometryNodeGridToPointsOutputs(typing.NamedTuple):
    points: Socket[Geometry]
    value: Socket[Field[float] | Field[int] | Field[bool] | Field[Vector]]
    x: Socket[Field[int]]
    y: Socket[Field[int]]
    z: Socket[Field[int]]
    is_tile: Socket[Field[bool]]
    extent: Socket[Field[int]]

def grid_to_points(*, grid: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeGridToPointsOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeGridToPoints',
        inputs={
            'grid': grid,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'points': ('Points', 'Points', 0, 'AUTO'),
            'value': ('Value', 'Value', 1, 'FIELD'),
            'x': ('X', 'X', 2, 'FIELD'),
            'y': ('Y', 'Y', 3, 'FIELD'),
            'z': ('Z', 'Z', 4, 'FIELD'),
            'is_tile': ('Is Tile', 'Is Tile', 5, 'FIELD'),
            'extent': ('Extent', 'Extent', 6, 'FIELD'),
        },
        output_type=GeometryNodeGridToPointsOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'BOOLEAN': {'grid': 'BOOLEAN'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class GeometryNodeCurveHandleTypeSelectionOutputs(typing.NamedTuple):
    selection: Socket[Field[bool]]

def handle_type_selection(*, handle_type: typing.Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO', mode: set[typing.Literal['LEFT', 'RIGHT']] = {'LEFT', 'RIGHT'}) -> GeometryNodeCurveHandleTypeSelectionOutputs:
    'Args:\n    mode: Whether to check the type of left and right handles'
    return _node_function(
        'GeometryNodeCurveHandleTypeSelection',
        inputs={
        },
        input_sockets={
        },
        properties={
            'handle_type': handle_type,
            'mode': mode,
        },
        output_sockets={
            'selection': ('Selection', 'Selection', 0, 'FIELD'),
        },
        output_type=GeometryNodeCurveHandleTypeSelectionOutputs,
    )

class FunctionNodeHashValueOutputs(typing.NamedTuple):
    hash: Socket[int | Field[int] | Grid[int] | List[int]]

def hash_value(*, value: int | Field[int] | Grid[int] | List[int] | float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Socket[int | Field[int] | Grid[int] | List[int] | float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str]] = 0, seed: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> FunctionNodeHashValueOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'FunctionNodeHashValue',
        inputs={
            'value': value,
            'seed': seed,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0),
            'seed': ('Seed', 'Seed', 1, 0),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'hash': ('Hash', 'Hash', 0, 'AUTO'),
        },
        output_type=FunctionNodeHashValueOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'VECTOR': {'value': 'VECTOR'}, 'RGBA': {'value': 'RGBA'}, 'ROTATION': {'value': 'ROTATION'}, 'MATRIX': {'value': 'MATRIX'}, 'STRING': {'value': 'STRING'}}},
    )

class GeometryNodeMeshIcoSphereOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]
    uv_map: Socket[Field[Vector]]

def ico_sphere(*, radius: float | Socket[float] = 1.0, subdivisions: int | Socket[int] = 1) -> GeometryNodeMeshIcoSphereOutputs:
    return _node_function(
        'GeometryNodeMeshIcoSphere',
        inputs={
            'radius': radius,
            'subdivisions': subdivisions,
        },
        input_sockets={
            'radius': ('Radius', 'Radius', 0, 1.0),
            'subdivisions': ('Subdivisions', 'Subdivisions', 1, 1),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
            'uv_map': ('UV Map', 'UV Map', 1, 'FIELD'),
        },
        output_type=GeometryNodeMeshIcoSphereOutputs,
    )

class GeometryNodeInputIDOutputs(typing.NamedTuple):
    id: Socket[Field[int]]

def id_() -> GeometryNodeInputIDOutputs:
    return _node_function(
        'GeometryNodeInputID',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'id': ('ID', 'ID', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputIDOutputs,
    )

class GeometryNodeInputImageOutputs(typing.NamedTuple):
    image: Socket[Image]

def image(*, image: bpy.types.Image | None = None) -> GeometryNodeInputImageOutputs:
    return _node_function(
        'GeometryNodeInputImage',
        inputs={
        },
        input_sockets={
        },
        properties={
            'image': image,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=GeometryNodeInputImageOutputs,
    )

class GeometryNodeImageInfoOutputs(typing.NamedTuple):
    width: Socket[int]
    height: Socket[int]
    has_alpha: Socket[bool]
    frame_count: Socket[int]
    fps: Socket[float]

def image_info(*, image: Image | Socket[Image] | None = None, frame: int | Socket[int] = 0) -> GeometryNodeImageInfoOutputs:
    return _node_function(
        'GeometryNodeImageInfo',
        inputs={
            'image': image,
            'frame': frame,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, None),
            'frame': ('Frame', 'Frame', 1, 0),
        },
        properties={
        },
        output_sockets={
            'width': ('Width', 'Width', 0, 'AUTO'),
            'height': ('Height', 'Height', 1, 'AUTO'),
            'has_alpha': ('Has Alpha', 'Has Alpha', 2, 'AUTO'),
            'frame_count': ('Frame Count', 'Frame Count', 3, 'AUTO'),
            'fps': ('FPS', 'FPS', 4, 'AUTO'),
        },
        output_type=GeometryNodeImageInfoOutputs,
    )

class GeometryNodeImageTextureOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]
    alpha: Socket[float | Field[float] | Grid[float] | List[float]]

def image_texture(*, image: Image | Socket[Image] | None = None, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), frame: int | Socket[int] = 0, interpolation: typing.Literal['Linear', 'Closest', 'Cubic'] = 'Linear', extension: typing.Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR'] = 'REPEAT') -> GeometryNodeImageTextureOutputs:
    'Args:\n    interpolation: Method for smoothing values between pixels\n    extension: How the image is extrapolated past its original bounds'
    return _node_function(
        'GeometryNodeImageTexture',
        inputs={
            'image': image,
            'vector': vector,
            'frame': frame,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, None),
            'vector': ('Vector', 'Vector', 1, (0.0, 0.0, 0.0)),
            'frame': ('Frame', 'Frame', 2, 0),
        },
        properties={
            'interpolation': interpolation,
            'extension': extension,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'FIELD'),
            'alpha': ('Alpha', 'Alpha', 1, 'FIELD'),
        },
        output_type=GeometryNodeImageTextureOutputs,
    )

class GeometryNodeImportCSVOutputs(typing.NamedTuple):
    point_cloud: Socket[Geometry]

def import_csv(*, path: str | Socket[str] = '', delimiter: str | Socket[str] = ',') -> GeometryNodeImportCSVOutputs:
    return _node_function(
        'GeometryNodeImportCSV',
        inputs={
            'path': path,
            'delimiter': delimiter,
        },
        input_sockets={
            'path': ('Path', 'Path', 0, ''),
            'delimiter': ('Delimiter', 'Delimiter', 1, ','),
        },
        properties={
        },
        output_sockets={
            'point_cloud': ('Point Cloud', 'Point Cloud', 0, 'AUTO'),
        },
        output_type=GeometryNodeImportCSVOutputs,
    )

class GeometryNodeImportOBJOutputs(typing.NamedTuple):
    instances: Socket[Geometry]

def import_obj(*, path: str | Socket[str] = '') -> GeometryNodeImportOBJOutputs:
    return _node_function(
        'GeometryNodeImportOBJ',
        inputs={
            'path': path,
        },
        input_sockets={
            'path': ('Path', 'Path', 0, ''),
        },
        properties={
        },
        output_sockets={
            'instances': ('Instances', 'Instances', 0, 'AUTO'),
        },
        output_type=GeometryNodeImportOBJOutputs,
    )

class GeometryNodeImportPLYOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def import_ply(*, path: str | Socket[str] = '') -> GeometryNodeImportPLYOutputs:
    return _node_function(
        'GeometryNodeImportPLY',
        inputs={
            'path': path,
        },
        input_sockets={
            'path': ('Path', 'Path', 0, ''),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeImportPLYOutputs,
    )

class GeometryNodeImportSTLOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def import_stl(*, path: str | Socket[str] = '') -> GeometryNodeImportSTLOutputs:
    return _node_function(
        'GeometryNodeImportSTL',
        inputs={
            'path': path,
        },
        input_sockets={
            'path': ('Path', 'Path', 0, ''),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeImportSTLOutputs,
    )

class GeometryNodeImportTextOutputs(typing.NamedTuple):
    string: Socket[str]

def import_text(*, path: str | Socket[str] = '') -> GeometryNodeImportTextOutputs:
    return _node_function(
        'GeometryNodeImportText',
        inputs={
            'path': path,
        },
        input_sockets={
            'path': ('Path', 'Path', 0, ''),
        },
        properties={
        },
        output_sockets={
            'string': ('String', 'String', 0, 'AUTO'),
        },
        output_type=GeometryNodeImportTextOutputs,
    )

class GeometryNodeImportVDBOutputs(typing.NamedTuple):
    volume: Socket[Geometry]

def import_vdb(*, path: str | Socket[str] = '') -> GeometryNodeImportVDBOutputs:
    return _node_function(
        'GeometryNodeImportVDB',
        inputs={
            'path': path,
        },
        input_sockets={
            'path': ('Path', 'Path', 0, ''),
        },
        properties={
        },
        output_sockets={
            'volume': ('Volume', 'Volume', 0, 'AUTO'),
        },
        output_type=GeometryNodeImportVDBOutputs,
    )

class GeometryNodeInputIndexOutputs(typing.NamedTuple):
    index: Socket[Field[int]]

def index() -> GeometryNodeInputIndexOutputs:
    return _node_function(
        'GeometryNodeInputIndex',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'index': ('Index', 'Index', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputIndexOutputs,
    )

class GeometryNodeIndexOfNearestOutputs(typing.NamedTuple):
    index: Socket[Field[int]]
    has_neighbor: Socket[Field[bool]]

def index_of_nearest(*, position: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), group_id: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeIndexOfNearestOutputs:
    return _node_function(
        'GeometryNodeIndexOfNearest',
        inputs={
            'position': position,
            'group_id': group_id,
        },
        input_sockets={
            'position': ('Position', 'Position', 0, (0.0, 0.0, 0.0)),
            'group_id': ('Group ID', 'Group ID', 1, 0),
        },
        properties={
        },
        output_sockets={
            'index': ('Index', 'Index', 0, 'FIELD'),
            'has_neighbor': ('Has Neighbor', 'Has Neighbor', 1, 'FIELD'),
        },
        output_type=GeometryNodeIndexOfNearestOutputs,
    )

class GeometryNodeIndexSwitchOutputs(typing.NamedTuple):
    output: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound]

def index_switch(*, index: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None, items: typing.Sequence[typing.Any] = ()) -> GeometryNodeIndexSwitchOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.\n    items: Item input values, in order.'
    return _node_function(
        'GeometryNodeIndexSwitch',
        inputs={
            'index': index,
        },
        input_sockets={
            'index': ('Index', 'Index', 0, 0),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'output': ('Output', 'Output', 0, 'AUTO'),
        },
        output_type=GeometryNodeIndexSwitchOutputs,
        item_collections=(
            ('index_switch_items', 'sequence', items),
        ),
        type_properties={'data_type': {'FLOAT': {}, 'INT': {}, 'BOOLEAN': {}, 'VECTOR': {}, 'RGBA': {}, 'ROTATION': {}, 'MATRIX': {}, 'STRING': {}, 'MENU': {}, 'OBJECT': {}, 'IMAGE': {}, 'GEOMETRY': {}, 'COLLECTION': {}, 'MATERIAL': {}, 'BUNDLE': {}, 'CLOSURE': {}, 'FONT': {}, 'SOUND': {}}},
    )

class GeometryNodeInputInstanceBoundsOutputs(typing.NamedTuple):
    min: Socket[Field[Vector]]
    max: Socket[Field[Vector]]

def instance_bounds(*, use_radius: bool | Socket[bool] = True) -> GeometryNodeInputInstanceBoundsOutputs:
    return _node_function(
        'GeometryNodeInputInstanceBounds',
        inputs={
            'use_radius': use_radius,
        },
        input_sockets={
            'use_radius': ('Use Radius', 'Use Radius', 0, True),
        },
        properties={
        },
        output_sockets={
            'min': ('Min', 'Min', 0, 'FIELD'),
            'max': ('Max', 'Max', 1, 'FIELD'),
        },
        output_type=GeometryNodeInputInstanceBoundsOutputs,
    )

class GeometryNodeInstanceOnPointsOutputs(typing.NamedTuple):
    instances: Socket[Geometry]

def instance_on_points(*, points: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, instance: Geometry | Socket[Geometry] | None = None, pick_instance: bool | Field[bool] | Socket[bool | Field[bool]] = False, instance_index: int | Field[int] | Socket[int | Field[int]] = 0, rotation: Rotation | Field[Rotation] | Socket[Rotation | Field[Rotation]] = (0.0, 0.0, 0.0), scale: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (1.0, 1.0, 1.0)) -> GeometryNodeInstanceOnPointsOutputs:
    return _node_function(
        'GeometryNodeInstanceOnPoints',
        inputs={
            'points': points,
            'selection': selection,
            'instance': instance,
            'pick_instance': pick_instance,
            'instance_index': instance_index,
            'rotation': rotation,
            'scale': scale,
        },
        input_sockets={
            'points': ('Points', 'Points', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'instance': ('Instance', 'Instance', 2, None),
            'pick_instance': ('Pick Instance', 'Pick Instance', 3, False),
            'instance_index': ('Instance Index', 'Instance Index', 4, 0),
            'rotation': ('Rotation', 'Rotation', 5, (0.0, 0.0, 0.0)),
            'scale': ('Scale', 'Scale', 6, (1.0, 1.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'instances': ('Instances', 'Instances', 0, 'AUTO'),
        },
        output_type=GeometryNodeInstanceOnPointsOutputs,
    )

class GeometryNodeInputInstanceReferenceOutputs(typing.NamedTuple):
    reference_index: Socket[Field[int]]

def instance_reference() -> GeometryNodeInputInstanceReferenceOutputs:
    return _node_function(
        'GeometryNodeInputInstanceReference',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'reference_index': ('Reference Index', 'Reference Index', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputInstanceReferenceOutputs,
    )

class GeometryNodeInputInstanceRotationOutputs(typing.NamedTuple):
    rotation: Socket[Field[Rotation]]

def instance_rotation() -> GeometryNodeInputInstanceRotationOutputs:
    return _node_function(
        'GeometryNodeInputInstanceRotation',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputInstanceRotationOutputs,
    )

class GeometryNodeInputInstanceScaleOutputs(typing.NamedTuple):
    scale: Socket[Field[Vector]]

def instance_scale() -> GeometryNodeInputInstanceScaleOutputs:
    return _node_function(
        'GeometryNodeInputInstanceScale',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'scale': ('Scale', 'Scale', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputInstanceScaleOutputs,
    )

class GeometryNodeInstanceTransformOutputs(typing.NamedTuple):
    transform: Socket[Field[Matrix]]

def instance_transform() -> GeometryNodeInstanceTransformOutputs:
    return _node_function(
        'GeometryNodeInstanceTransform',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'transform': ('Transform', 'Transform', 0, 'FIELD'),
        },
        output_type=GeometryNodeInstanceTransformOutputs,
    )

class GeometryNodeInstancesToPointsOutputs(typing.NamedTuple):
    points: Socket[Geometry]

def instances_to_points(*, instances: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, position: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), radius: float | Field[float] | Socket[float | Field[float]] = 0.05000000074505806) -> GeometryNodeInstancesToPointsOutputs:
    return _node_function(
        'GeometryNodeInstancesToPoints',
        inputs={
            'instances': instances,
            'selection': selection,
            'position': position,
            'radius': radius,
        },
        input_sockets={
            'instances': ('Instances', 'Instances', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'position': ('Position', 'Position', 2, (0.0, 0.0, 0.0)),
            'radius': ('Radius', 'Radius', 3, 0.05000000074505806),
        },
        properties={
        },
        output_sockets={
            'points': ('Points', 'Points', 0, 'AUTO'),
        },
        output_type=GeometryNodeInstancesToPointsOutputs,
    )

class FunctionNodeInputIntOutputs(typing.NamedTuple):
    integer: Socket[int]

def integer(*, integer: int = 0) -> FunctionNodeInputIntOutputs:
    'Args:\n    integer: Input value used for unconnected socket'
    return _node_function(
        'FunctionNodeInputInt',
        inputs={
        },
        input_sockets={
        },
        properties={
            'integer': integer,
        },
        output_sockets={
            'integer': ('Integer', 'Integer', 0, 'AUTO'),
        },
        output_type=FunctionNodeInputIntOutputs,
    )

class FunctionNodeIntegerMathOutputs(typing.NamedTuple):
    value: Socket[int | Field[int] | Grid[int] | List[int]]

def integer_math(*, value: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, value_2: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, value_3: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, operation: typing.Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'ABSOLUTE', 'NEGATE', 'POWER', 'MINIMUM', 'MAXIMUM', 'SIGN', 'DIVIDE_ROUND', 'DIVIDE_FLOOR', 'DIVIDE_CEIL', 'FLOORED_MODULO', 'MODULO', 'GCD', 'LCM'] = 'ADD') -> FunctionNodeIntegerMathOutputs:
    return _node_function(
        'FunctionNodeIntegerMath',
        inputs={
            'value': value,
            'value_2': value_2,
            'value_3': value_3,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0),
            'value_2': ('Value_001', 'Value', 1, 0),
            'value_3': ('Value_002', 'Value', 2, 0),
        },
        properties={
            'operation': operation,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=FunctionNodeIntegerMathOutputs,
    )

class FunctionNodeInputIntVectorOutputs(typing.NamedTuple):
    vector: Socket[IntVector3]

def integer_vector(*, vector: IntVector3 = (0, 0, 0), vector_dimensions: int = 3) -> FunctionNodeInputIntVectorOutputs:
    'Args:\n    vector_dimensions: Dimensions of the vector socket'
    return _node_function(
        'FunctionNodeInputIntVector',
        inputs={
        },
        input_sockets={
        },
        properties={
            'vector': vector,
            'vector_dimensions': vector_dimensions,
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
        },
        output_type=FunctionNodeInputIntVectorOutputs,
    )

class GeometryNodeInterpolateCurvesOutputs(typing.NamedTuple):
    curves: Socket[Geometry]
    closest_index: Socket[Field[int]]
    closest_weight: Socket[Field[float]]

def interpolate_curves(*, guide_curves: Geometry | Socket[Geometry] | None = None, guide_up: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), guide_group_id: int | Field[int] | Socket[int | Field[int]] = 0, points: Geometry | Socket[Geometry] | None = None, point_up: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), point_group_id: int | Field[int] | Socket[int | Field[int]] = 0, max_neighbors: int | Socket[int] = 4) -> GeometryNodeInterpolateCurvesOutputs:
    return _node_function(
        'GeometryNodeInterpolateCurves',
        inputs={
            'guide_curves': guide_curves,
            'guide_up': guide_up,
            'guide_group_id': guide_group_id,
            'points': points,
            'point_up': point_up,
            'point_group_id': point_group_id,
            'max_neighbors': max_neighbors,
        },
        input_sockets={
            'guide_curves': ('Guide Curves', 'Guide Curves', 0, None),
            'guide_up': ('Guide Up', 'Guide Up', 1, (0.0, 0.0, 0.0)),
            'guide_group_id': ('Guide Group ID', 'Guide Group ID', 2, 0),
            'points': ('Points', 'Points', 3, None),
            'point_up': ('Point Up', 'Point Up', 4, (0.0, 0.0, 0.0)),
            'point_group_id': ('Point Group ID', 'Point Group ID', 5, 0),
            'max_neighbors': ('Max Neighbors', 'Max Neighbors', 6, 4),
        },
        properties={
        },
        output_sockets={
            'curves': ('Curves', 'Curves', 0, 'AUTO'),
            'closest_index': ('Closest Index', 'Closest Index', 1, 'FIELD'),
            'closest_weight': ('Closest Weight', 'Closest Weight', 2, 'FIELD'),
        },
        output_type=GeometryNodeInterpolateCurvesOutputs,
    )

class FunctionNodeInvertMatrixOutputs(typing.NamedTuple):
    matrix: Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]
    invertible: Socket[bool | Field[bool] | Grid[bool] | List[bool]]

def invert_matrix(*, matrix: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None) -> FunctionNodeInvertMatrixOutputs:
    return _node_function(
        'FunctionNodeInvertMatrix',
        inputs={
            'matrix': matrix,
        },
        input_sockets={
            'matrix': ('Matrix', 'Matrix', 0, None),
        },
        properties={
        },
        output_sockets={
            'matrix': ('Matrix', 'Matrix', 0, 'AUTO'),
            'invertible': ('Invertible', 'Invertible', 1, 'AUTO'),
        },
        output_type=FunctionNodeInvertMatrixOutputs,
    )

class FunctionNodeInvertRotationOutputs(typing.NamedTuple):
    rotation: Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]]

def invert_rotation(*, rotation: Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = (0.0, 0.0, 0.0)) -> FunctionNodeInvertRotationOutputs:
    return _node_function(
        'FunctionNodeInvertRotation',
        inputs={
            'rotation': rotation,
        },
        input_sockets={
            'rotation': ('Rotation', 'Rotation', 0, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'AUTO'),
        },
        output_type=FunctionNodeInvertRotationOutputs,
    )

class GeometryNodeInputEdgeSmoothOutputs(typing.NamedTuple):
    smooth: Socket[Field[bool]]

def is_edge_smooth() -> GeometryNodeInputEdgeSmoothOutputs:
    return _node_function(
        'GeometryNodeInputEdgeSmooth',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'smooth': ('Smooth', 'Smooth', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputEdgeSmoothOutputs,
    )

class GeometryNodeInputMeshFaceIsPlanarOutputs(typing.NamedTuple):
    planar: Socket[Field[bool]]

def is_face_planar(*, threshold: float | Field[float] | Socket[float | Field[float]] = 0.009999999776482582) -> GeometryNodeInputMeshFaceIsPlanarOutputs:
    return _node_function(
        'GeometryNodeInputMeshFaceIsPlanar',
        inputs={
            'threshold': threshold,
        },
        input_sockets={
            'threshold': ('Threshold', 'Threshold', 0, 0.009999999776482582),
        },
        properties={
        },
        output_sockets={
            'planar': ('Planar', 'Planar', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputMeshFaceIsPlanarOutputs,
    )

class GeometryNodeInputShadeSmoothOutputs(typing.NamedTuple):
    smooth: Socket[Field[bool]]

def is_face_smooth() -> GeometryNodeInputShadeSmoothOutputs:
    return _node_function(
        'GeometryNodeInputShadeSmooth',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'smooth': ('Smooth', 'Smooth', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputShadeSmoothOutputs,
    )

class GeometryNodeInputSplineCyclicOutputs(typing.NamedTuple):
    cyclic: Socket[Field[bool]]

def is_spline_cyclic() -> GeometryNodeInputSplineCyclicOutputs:
    return _node_function(
        'GeometryNodeInputSplineCyclic',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'cyclic': ('Cyclic', 'Cyclic', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputSplineCyclicOutputs,
    )

class GeometryNodeIsViewportOutputs(typing.NamedTuple):
    is_viewport: Socket[bool]

def is_viewport() -> GeometryNodeIsViewportOutputs:
    return _node_function(
        'GeometryNodeIsViewport',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'is_viewport': ('Is Viewport', 'Is Viewport', 0, 'AUTO'),
        },
        output_type=GeometryNodeIsViewportOutputs,
    )

class NodeJoinBundleOutputs(typing.NamedTuple):
    bundle: Socket[Bundle]

def join_bundle(*, bundle: typing.Sequence[Bundle | Socket[Bundle]] = ()) -> NodeJoinBundleOutputs:
    return _node_function(
        'NodeJoinBundle',
        inputs={
            'bundle': bundle,
        },
        input_sockets={
            'bundle': ('Bundle', 'Bundle', 0, ()),
        },
        properties={
        },
        output_sockets={
            'bundle': ('Bundle', 'Bundle', 0, 'AUTO'),
        },
        output_type=NodeJoinBundleOutputs,
    )

class GeometryNodeJoinGeometryOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def join_geometry(*, geometry: typing.Sequence[Geometry | Socket[Geometry]] = ()) -> GeometryNodeJoinGeometryOutputs:
    return _node_function(
        'GeometryNodeJoinGeometry',
        inputs={
            'geometry': geometry,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, ()),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeJoinGeometryOutputs,
    )

class GeometryNodeStringJoinOutputs(typing.NamedTuple):
    string: Socket[str]

def join_strings(*, delimiter: str | Socket[str] = '', strings: typing.Sequence[str | Socket[str]] = ()) -> GeometryNodeStringJoinOutputs:
    return _node_function(
        'GeometryNodeStringJoin',
        inputs={
            'delimiter': delimiter,
            'strings': strings,
        },
        input_sockets={
            'delimiter': ('Delimiter', 'Delimiter', 0, ''),
            'strings': ('Strings', 'Strings', 1, ()),
        },
        properties={
        },
        output_sockets={
            'string': ('String', 'String', 0, 'AUTO'),
        },
        output_type=GeometryNodeStringJoinOutputs,
    )

class GeometryNodeGizmoLinearOutputs(typing.NamedTuple):
    transform: Socket[Geometry]

def linear_gizmo(*, value: typing.Sequence[float | Socket[float]] = (), position: Vector | Socket[Vector] = (0.0, 0.0, 0.0), direction: Vector | Socket[Vector] = (0.0, 0.0, 1.0), color_id: typing.Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z'] = 'PRIMARY', draw_style: typing.Literal['ARROW', 'CROSS', 'BOX'] = 'ARROW') -> GeometryNodeGizmoLinearOutputs:
    return _node_function(
        'GeometryNodeGizmoLinear',
        inputs={
            'value': value,
            'position': position,
            'direction': direction,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, ()),
            'position': ('Position', 'Position', 1, (0.0, 0.0, 0.0)),
            'direction': ('Direction', 'Direction', 2, (0.0, 0.0, 1.0)),
        },
        properties={
            'color_id': color_id,
            'draw_style': draw_style,
        },
        output_sockets={
            'transform': ('Transform', 'Transform', 0, 'AUTO'),
        },
        output_type=GeometryNodeGizmoLinearOutputs,
    )

class GeometryNodeListLengthOutputs(typing.NamedTuple):
    length: Socket[int]

def list_length(*, list: List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound] | Socket[List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound]] | None = None, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeListLengthOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeListLength',
        inputs={
            'list': list,
        },
        input_sockets={
            'list': ('List', 'List', 0, None),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'length': ('Length', 'Length', 0, 'AUTO'),
        },
        output_type=GeometryNodeListLengthOutputs,
        type_properties={'data_type': {'FLOAT': {'list': 'VALUE'}, 'INT': {'list': 'INT'}, 'BOOLEAN': {'list': 'BOOLEAN'}, 'VECTOR': {'list': 'VECTOR'}, 'RGBA': {'list': 'RGBA'}, 'ROTATION': {'list': 'ROTATION'}, 'MATRIX': {'list': 'MATRIX'}, 'STRING': {'list': 'STRING'}, 'MENU': {'list': 'MENU'}, 'OBJECT': {'list': 'OBJECT'}, 'IMAGE': {'list': 'IMAGE'}, 'GEOMETRY': {'list': 'GEOMETRY'}, 'COLLECTION': {'list': 'COLLECTION'}, 'MATERIAL': {'list': 'MATERIAL'}, 'BUNDLE': {'list': 'BUNDLE'}, 'CLOSURE': {'list': 'CLOSURE'}, 'FONT': {'list': 'FONT'}, 'SOUND': {'list': 'SOUND'}}},
    )

class ShaderNodeTexMagicOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]
    factor: Socket[float | Field[float] | Grid[float] | List[float]]

def magic_texture(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), scale: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 5.0, distortion: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, turbulence_depth: int = 2) -> ShaderNodeTexMagicOutputs:
    'Args:\n    turbulence_depth: Level of detail in the added turbulent noise'
    return _node_function(
        'ShaderNodeTexMagic',
        inputs={
            'vector': vector,
            'scale': scale,
            'distortion': distortion,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'scale': ('Scale', 'Scale', 1, 5.0),
            'distortion': ('Distortion', 'Distortion', 2, 1.0),
        },
        properties={
            'turbulence_depth': turbulence_depth,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'FIELD'),
            'factor': ('Fac', 'Factor', 1, 'FIELD'),
        },
        output_type=ShaderNodeTexMagicOutputs,
    )

class ShaderNodeMapRangeOutputs(typing.NamedTuple):
    result: Socket[float | Field[float] | Grid[float] | List[float]]
    vector: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def map_range(*, value: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, from_min: float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector]] = 0.0, from_max: float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector]] = 1.0, to_min: float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector]] = 0.0, to_max: float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector]] = 1.0, steps: float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector]] = 4.0, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), clamp: bool = True, interpolation_type: typing.Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR', data_type: typing.Literal['FLOAT', 'FLOAT_VECTOR'] | None = None) -> ShaderNodeMapRangeOutputs:
    'Args:\n    clamp: Clamp the result to the target range [To Min, To Max]\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'ShaderNodeMapRange',
        inputs={
            'value': value,
            'from_min': from_min,
            'from_max': from_max,
            'to_min': to_min,
            'to_max': to_max,
            'steps': steps,
            'vector': vector,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 1.0),
            'from_min': ('From Min', 'From Min', 1, 0.0),
            'from_max': ('From Max', 'From Max', 2, 1.0),
            'to_min': ('To Min', 'To Min', 3, 0.0),
            'to_max': ('To Max', 'To Max', 4, 1.0),
            'steps': ('Steps', 'Steps', 5, 4.0),
            'vector': ('Vector', 'Vector', 6, (0.0, 0.0, 0.0)),
        },
        properties={
            'clamp': clamp,
            'interpolation_type': interpolation_type,
            'data_type': data_type,
        },
        output_sockets={
            'result': ('Result', 'Result', 0, 'AUTO'),
            'vector': ('Vector', 'Vector', 1, 'AUTO'),
        },
        output_type=ShaderNodeMapRangeOutputs,
        type_properties={'data_type': {'FLOAT': {'from_min': 'VALUE', 'from_max': 'VALUE', 'to_min': 'VALUE', 'to_max': 'VALUE'}, 'FLOAT_VECTOR': {'from_min': 'VECTOR', 'from_max': 'VECTOR', 'to_min': 'VECTOR', 'to_max': 'VECTOR'}}},
    )

class FunctionNodeMatchStringOutputs(typing.NamedTuple):
    result: Socket[bool | Field[bool] | Grid[bool] | List[bool]]

def match_string(*, string: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', operation: Menu | Socket[Menu] = 'Starts With', key: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '') -> FunctionNodeMatchStringOutputs:
    return _node_function(
        'FunctionNodeMatchString',
        inputs={
            'string': string,
            'operation': operation,
            'key': key,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
            'operation': ('Operation', 'Operation', 1, 'Starts With'),
            'key': ('Key', 'Key', 2, ''),
        },
        properties={
        },
        output_sockets={
            'result': ('Result', 'Result', 0, 'AUTO'),
        },
        output_type=FunctionNodeMatchStringOutputs,
    )

class GeometryNodeInputMaterialOutputs(typing.NamedTuple):
    material: Socket[Material]

def material(*, material: bpy.types.Material | None = None) -> GeometryNodeInputMaterialOutputs:
    return _node_function(
        'GeometryNodeInputMaterial',
        inputs={
        },
        input_sockets={
        },
        properties={
            'material': material,
        },
        output_sockets={
            'material': ('Material', 'Material', 0, 'AUTO'),
        },
        output_type=GeometryNodeInputMaterialOutputs,
    )

class GeometryNodeInputMaterialIndexOutputs(typing.NamedTuple):
    material_index: Socket[Field[int]]

def material_index() -> GeometryNodeInputMaterialIndexOutputs:
    return _node_function(
        'GeometryNodeInputMaterialIndex',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'material_index': ('Material Index', 'Material Index', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputMaterialIndexOutputs,
    )

class GeometryNodeMaterialSelectionOutputs(typing.NamedTuple):
    selection: Socket[Field[bool]]

def material_selection(*, material: Material | Socket[Material] | None = None) -> GeometryNodeMaterialSelectionOutputs:
    return _node_function(
        'GeometryNodeMaterialSelection',
        inputs={
            'material': material,
        },
        input_sockets={
            'material': ('Material', 'Material', 0, None),
        },
        properties={
        },
        output_sockets={
            'selection': ('Selection', 'Selection', 0, 'FIELD'),
        },
        output_type=GeometryNodeMaterialSelectionOutputs,
    )

class ShaderNodeMathOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float]]

def math_(*, value: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5, value_2: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5, value_3: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5, operation: typing.Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'] = 'ADD', use_clamp: bool = False) -> ShaderNodeMathOutputs:
    'Args:\n    use_clamp: Clamp result of the node to 0.0 to 1.0 range'
    return _node_function(
        'ShaderNodeMath',
        inputs={
            'value': value,
            'value_2': value_2,
            'value_3': value_3,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0.5),
            'value_2': ('Value_001', 'Value', 1, 0.5),
            'value_3': ('Value_002', 'Value', 2, 0.5),
        },
        properties={
            'operation': operation,
            'use_clamp': use_clamp,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=ShaderNodeMathOutputs,
    )

class FunctionNodeMatrixDeterminantOutputs(typing.NamedTuple):
    determinant: Socket[float | Field[float] | Grid[float] | List[float]]

def matrix_determinant(*, matrix: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None) -> FunctionNodeMatrixDeterminantOutputs:
    return _node_function(
        'FunctionNodeMatrixDeterminant',
        inputs={
            'matrix': matrix,
        },
        input_sockets={
            'matrix': ('Matrix', 'Matrix', 0, None),
        },
        properties={
        },
        output_sockets={
            'determinant': ('Determinant', 'Determinant', 0, 'AUTO'),
        },
        output_type=FunctionNodeMatrixDeterminantOutputs,
    )

class FunctionNodeMatrixSVDOutputs(typing.NamedTuple):
    u: Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]
    s: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    v: Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]

def matrix_svd(*, matrix: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None) -> FunctionNodeMatrixSVDOutputs:
    return _node_function(
        'FunctionNodeMatrixSVD',
        inputs={
            'matrix': matrix,
        },
        input_sockets={
            'matrix': ('Matrix', 'Matrix', 0, None),
        },
        properties={
        },
        output_sockets={
            'u': ('U', 'U', 0, 'AUTO'),
            's': ('S', 'S', 1, 'AUTO'),
            'v': ('V', 'V', 2, 'AUTO'),
        },
        output_type=FunctionNodeMatrixSVDOutputs,
    )

class FunctionNodeInputMenuOutputs(typing.NamedTuple):
    menu: Socket[Menu]

def menu(*, value: str = '') -> FunctionNodeInputMenuOutputs:
    'Args:\n    value: Value of the output socket'
    return _node_function(
        'FunctionNodeInputMenu',
        inputs={
        },
        input_sockets={
        },
        properties={
            'value': value,
        },
        output_sockets={
            'menu': ('Menu', 'Menu', 0, 'AUTO'),
        },
        output_type=FunctionNodeInputMenuOutputs,
    )

class GeometryNodeMenuSwitchOutputs(ItemOutputs):
    output: Socket[Geometry | float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Collection | Material | Bundle | Closure | Font | Sound]

def menu_switch(*, menu: Menu | Socket[Menu] = '', data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None, items: typing.Mapping[str, typing.Any] | None = None) -> GeometryNodeMenuSwitchOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.\n    items: Items to add, mapping each name to its input value. Their outputs are available by name on the result.'
    return _node_function(
        'GeometryNodeMenuSwitch',
        inputs={
            'menu': menu,
        },
        input_sockets={
            'menu': ('Menu', 'Menu', 0, ''),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'output': ('Output', 'Output', 0, 'AUTO'),
        },
        output_type=GeometryNodeMenuSwitchOutputs,
        item_collections=(
            ('enum_items', 'named', items),
        ),
        type_properties={'data_type': {'FLOAT': {}, 'INT': {}, 'BOOLEAN': {}, 'VECTOR': {}, 'RGBA': {}, 'ROTATION': {}, 'MATRIX': {}, 'STRING': {}, 'MENU': {}, 'OBJECT': {}, 'IMAGE': {}, 'GEOMETRY': {}, 'COLLECTION': {}, 'MATERIAL': {}, 'BUNDLE': {}, 'CLOSURE': {}, 'FONT': {}, 'SOUND': {}}},
    )

class GeometryNodeMergeByDistanceOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def merge_by_distance(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, mode: Menu | Socket[Menu] = 'All', distance: float | Socket[float] = 0.0010000000474974513) -> GeometryNodeMergeByDistanceOutputs:
    return _node_function(
        'GeometryNodeMergeByDistance',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'mode': mode,
            'distance': distance,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'mode': ('Mode', 'Mode', 2, 'All'),
            'distance': ('Distance', 'Distance', 3, 0.0010000000474974513),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeMergeByDistanceOutputs,
    )

class GeometryNodeMergeLayersOutputs(typing.NamedTuple):
    grease_pencil: Socket[Geometry]

def merge_layers(*, grease_pencil: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, group_id: int | Field[int] | Socket[int | Field[int]] = 0, mode: typing.Literal['MERGE_BY_NAME', 'MERGE_BY_ID'] = 'MERGE_BY_NAME') -> GeometryNodeMergeLayersOutputs:
    'Args:\n    mode: Determines how to choose which layers are merged'
    return _node_function(
        'GeometryNodeMergeLayers',
        inputs={
            'grease_pencil': grease_pencil,
            'selection': selection,
            'group_id': group_id,
        },
        input_sockets={
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'group_id': ('Group ID', 'Group ID', 2, 0),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 0, 'AUTO'),
        },
        output_type=GeometryNodeMergeLayersOutputs,
    )

class GeometryNodeMergePointsOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def merge_points(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, merge_id: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeMergePointsOutputs:
    return _node_function(
        'GeometryNodeMergePoints',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'merge_id': merge_id,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'merge_id': ('Merge ID', 'Merge ID', 2, 0),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeMergePointsOutputs,
    )

class GeometryNodeMeshBevelOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]
    vertex_face: Socket[Field[bool]]
    edge_face: Socket[Field[bool]]
    outer_edge: Socket[Field[bool]]
    mid_edge: Socket[Field[bool]]

def mesh_bevel(*, mesh: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, affect_kind: Menu | Socket[Menu] = 'Edges', start_left_offset: float | Field[float] | Socket[float | Field[float]] = 0.10000000149011612, start_right_offset: float | Field[float] | Socket[float | Field[float]] = 0.10000000149011612, end_left_offset: float | Field[float] | Socket[float | Field[float]] = 0.10000000149011612, end_right_offset: float | Field[float] | Socket[float | Field[float]] = 0.10000000149011612, offset: float | Field[float] | Socket[float | Field[float]] = 0.10000000149011612, miter: bool | Field[bool] | Socket[bool | Field[bool]] = False, spread: float | Field[float] | Socket[float | Field[float]] = 0.10000000149011612, segments: int | Socket[int] = 1, shape: float | Socket[float] = 0.5, profile: Geometry | Socket[Geometry] | None = None) -> GeometryNodeMeshBevelOutputs:
    return _node_function(
        'GeometryNodeMeshBevel',
        inputs={
            'mesh': mesh,
            'selection': selection,
            'affect_kind': affect_kind,
            'start_left_offset': start_left_offset,
            'start_right_offset': start_right_offset,
            'end_left_offset': end_left_offset,
            'end_right_offset': end_right_offset,
            'offset': offset,
            'miter': miter,
            'spread': spread,
            'segments': segments,
            'shape': shape,
            'profile': profile,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'affect_kind': ('Affect Kind', 'Affect Kind', 2, 'Edges'),
            'start_left_offset': ('Start Left Offset', 'Start Left Offset', 3, 0.10000000149011612),
            'start_right_offset': ('Start Right Offset', 'Start Right Offset', 4, 0.10000000149011612),
            'end_left_offset': ('End Left Offset', 'End Left Offset', 5, 0.10000000149011612),
            'end_right_offset': ('End Right Offset', 'End Right Offset', 6, 0.10000000149011612),
            'offset': ('Offset', 'Offset', 7, 0.10000000149011612),
            'miter': ('Miter', 'Miter', 8, False),
            'spread': ('Spread', 'Spread', 9, 0.10000000149011612),
            'segments': ('Segments', 'Segments', 10, 1),
            'shape': ('Shape', 'Shape', 11, 0.5),
            'profile': ('Profile', 'Profile', 12, None),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
            'vertex_face': ('Vertex Face', 'Vertex Face', 1, 'FIELD'),
            'edge_face': ('Edge Face', 'Edge Face', 2, 'FIELD'),
            'outer_edge': ('Outer Edge', 'Outer Edge', 3, 'FIELD'),
            'mid_edge': ('Mid Edge', 'Mid Edge', 4, 'FIELD'),
        },
        output_type=GeometryNodeMeshBevelOutputs,
    )

class GeometryNodeMeshBooleanOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]
    intersecting_edges: Socket[Field[bool]]

def mesh_boolean(*, mesh_1: Geometry | Socket[Geometry] | None = None, mesh_2: typing.Sequence[Geometry | Socket[Geometry]] = (), mesh: typing.Sequence[Geometry | Socket[Geometry]] = (), self_intersection: bool | Socket[bool] = False, hole_tolerant: bool | Socket[bool] = False, operation: typing.Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE', solver: typing.Literal['EXACT', 'FLOAT', 'MANIFOLD'] = 'FLOAT') -> GeometryNodeMeshBooleanOutputs:
    return _node_function(
        'GeometryNodeMeshBoolean',
        inputs={
            'mesh_1': mesh_1,
            'mesh_2': mesh_2,
            'mesh': mesh,
            'self_intersection': self_intersection,
            'hole_tolerant': hole_tolerant,
        },
        input_sockets={
            'mesh_1': ('Mesh 1', 'Mesh 1', 0, None),
            'mesh_2': ('Mesh 2', 'Mesh 2', 1, ()),
            'mesh': ('Mesh 2', 'Mesh', 1, ()),
            'self_intersection': ('Self Intersection', 'Self Intersection', 2, False),
            'hole_tolerant': ('Hole Tolerant', 'Hole Tolerant', 3, False),
        },
        properties={
            'operation': operation,
            'solver': solver,
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
            'intersecting_edges': ('Intersecting Edges', 'Intersecting Edges', 1, 'FIELD'),
        },
        output_type=GeometryNodeMeshBooleanOutputs,
    )

class GeometryNodeMeshCircleOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def mesh_circle(*, vertices: int | Socket[int] = 32, radius: float | Socket[float] = 1.0, fill_type: typing.Literal['NONE', 'NGON', 'TRIANGLE_FAN'] = 'NONE') -> GeometryNodeMeshCircleOutputs:
    return _node_function(
        'GeometryNodeMeshCircle',
        inputs={
            'vertices': vertices,
            'radius': radius,
        },
        input_sockets={
            'vertices': ('Vertices', 'Vertices', 0, 32),
            'radius': ('Radius', 'Radius', 1, 1.0),
        },
        properties={
            'fill_type': fill_type,
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeMeshCircleOutputs,
    )

class GeometryNodeInputMeshIslandOutputs(typing.NamedTuple):
    island_index: Socket[Field[int]]
    island_count: Socket[Field[int]]

def mesh_island() -> GeometryNodeInputMeshIslandOutputs:
    return _node_function(
        'GeometryNodeInputMeshIsland',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'island_index': ('Island Index', 'Island Index', 0, 'FIELD'),
            'island_count': ('Island Count', 'Island Count', 1, 'FIELD'),
        },
        output_type=GeometryNodeInputMeshIslandOutputs,
    )

class GeometryNodeMeshLineOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def mesh_line(*, count: int | Socket[int] = 10, start_location: Vector | Socket[Vector] = (0.0, 0.0, 0.0), offset: Vector | Socket[Vector] = (0.0, 0.0, 1.0), resolution: float | Socket[float] = 1.0, mode: typing.Literal['OFFSET', 'END_POINTS'] = 'OFFSET', count_mode: typing.Literal['TOTAL', 'RESOLUTION'] = 'TOTAL') -> GeometryNodeMeshLineOutputs:
    return _node_function(
        'GeometryNodeMeshLine',
        inputs={
            'count': count,
            'start_location': start_location,
            'offset': offset,
            'resolution': resolution,
        },
        input_sockets={
            'count': ('Count', 'Count', 0, 10),
            'start_location': ('Start Location', 'Start Location', 2, (0.0, 0.0, 0.0)),
            'offset': ('Offset', 'Offset', 3, (0.0, 0.0, 1.0)),
            'resolution': ('Resolution', 'Resolution', 1, 1.0),
        },
        properties={
            'mode': mode,
            'count_mode': count_mode,
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeMeshLineOutputs,
    )

class GeometryNodeMeshToCurveOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def mesh_to_curve(*, mesh: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, mode: typing.Literal['EDGES', 'FACES'] = 'EDGES') -> GeometryNodeMeshToCurveOutputs:
    return _node_function(
        'GeometryNodeMeshToCurve',
        inputs={
            'mesh': mesh,
            'selection': selection,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeMeshToCurveOutputs,
    )

class GeometryNodeMeshToDensityGridOutputs(typing.NamedTuple):
    density_grid: Socket[Grid[float]]

def mesh_to_density_grid(*, mesh: Geometry | Socket[Geometry] | None = None, density: float | Socket[float] = 1.0, voxel_size: float | Socket[float] = 0.30000001192092896, gradient_width: float | Socket[float] = 0.20000000298023224) -> GeometryNodeMeshToDensityGridOutputs:
    return _node_function(
        'GeometryNodeMeshToDensityGrid',
        inputs={
            'mesh': mesh,
            'density': density,
            'voxel_size': voxel_size,
            'gradient_width': gradient_width,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'density': ('Density', 'Density', 1, 1.0),
            'voxel_size': ('Voxel Size', 'Voxel Size', 2, 0.30000001192092896),
            'gradient_width': ('Gradient Width', 'Gradient Width', 3, 0.20000000298023224),
        },
        properties={
        },
        output_sockets={
            'density_grid': ('Density Grid', 'Density Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeMeshToDensityGridOutputs,
    )

class GeometryNodeMeshToPointsOutputs(typing.NamedTuple):
    points: Socket[Geometry]

def mesh_to_points(*, mesh: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, position: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), radius: float | Field[float] | Socket[float | Field[float]] = 0.05000000074505806, mode: typing.Literal['VERTICES', 'EDGES', 'FACES', 'CORNERS'] = 'VERTICES') -> GeometryNodeMeshToPointsOutputs:
    return _node_function(
        'GeometryNodeMeshToPoints',
        inputs={
            'mesh': mesh,
            'selection': selection,
            'position': position,
            'radius': radius,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'position': ('Position', 'Position', 2, (0.0, 0.0, 0.0)),
            'radius': ('Radius', 'Radius', 3, 0.05000000074505806),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'points': ('Points', 'Points', 0, 'AUTO'),
        },
        output_type=GeometryNodeMeshToPointsOutputs,
    )

class GeometryNodeMeshToSDFGridOutputs(typing.NamedTuple):
    sdf_grid: Socket[Grid[float]]

def mesh_to_sdf_grid(*, mesh: Geometry | Socket[Geometry] | None = None, voxel_size: float | Socket[float] = 0.30000001192092896, band_width: int | Socket[int] = 3) -> GeometryNodeMeshToSDFGridOutputs:
    return _node_function(
        'GeometryNodeMeshToSDFGrid',
        inputs={
            'mesh': mesh,
            'voxel_size': voxel_size,
            'band_width': band_width,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'voxel_size': ('Voxel Size', 'Voxel Size', 1, 0.30000001192092896),
            'band_width': ('Band Width', 'Band Width', 2, 3),
        },
        properties={
        },
        output_sockets={
            'sdf_grid': ('SDF Grid', 'SDF Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeMeshToSDFGridOutputs,
    )

class GeometryNodeMeshToVolumeOutputs(typing.NamedTuple):
    volume: Socket[Geometry]

def mesh_to_volume(*, mesh: Geometry | Socket[Geometry] | None = None, density: float | Socket[float] = 1.0, resolution_mode: Menu | Socket[Menu] = 'Amount', voxel_size: float | Socket[float] = 0.30000001192092896, voxel_amount: float | Socket[float] = 64.0, interior_band_width: float | Socket[float] = 0.20000000298023224) -> GeometryNodeMeshToVolumeOutputs:
    return _node_function(
        'GeometryNodeMeshToVolume',
        inputs={
            'mesh': mesh,
            'density': density,
            'resolution_mode': resolution_mode,
            'voxel_size': voxel_size,
            'voxel_amount': voxel_amount,
            'interior_band_width': interior_band_width,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'density': ('Density', 'Density', 1, 1.0),
            'resolution_mode': ('Resolution Mode', 'Resolution Mode', 2, 'Amount'),
            'voxel_size': ('Voxel Size', 'Voxel Size', 3, 0.30000001192092896),
            'voxel_amount': ('Voxel Amount', 'Voxel Amount', 4, 64.0),
            'interior_band_width': ('Interior Band Width', 'Interior Band Width', 5, 0.20000000298023224),
        },
        properties={
        },
        output_sockets={
            'volume': ('Volume', 'Volume', 0, 'AUTO'),
        },
        output_type=GeometryNodeMeshToVolumeOutputs,
    )

class ShaderNodeMixOutputs(typing.NamedTuple):
    result: Socket[float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]]

def mix(*, factor: float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector]] = 1.0, a: float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = 0.0, b: float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[float | Field[float] | Grid[float] | List[float] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = 0.0, data_type: typing.Literal['FLOAT', 'VECTOR', 'RGBA', 'ROTATION'] | None = None, factor_mode: typing.Literal['UNIFORM', 'NON_UNIFORM'] = 'UNIFORM', blend_type: typing.Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX', clamp_factor: bool = True, clamp_result: bool = False) -> ShaderNodeMixOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.\n    clamp_factor: Clamp the factor to [0,1] range\n    clamp_result: Clamp the result to [0,1] range'
    return _node_function(
        'ShaderNodeMix',
        inputs={
            'factor': factor,
            'a': a,
            'b': b,
        },
        input_sockets={
            'factor': ('Factor_Float', 'Factor', 0, 1.0),
            'a': ('A_Float', 'A', 2, 0.0),
            'b': ('B_Float', 'B', 3, 0.0),
        },
        properties={
            'data_type': data_type,
            'factor_mode': factor_mode,
            'blend_type': blend_type,
            'clamp_factor': clamp_factor,
            'clamp_result': clamp_result,
        },
        output_sockets={
            'result': ('Result_Float', 'Result', 0, 'AUTO'),
        },
        output_type=ShaderNodeMixOutputs,
        type_properties={'data_type': {'FLOAT': {'a': 'VALUE', 'b': 'VALUE'}, 'VECTOR': {'a': 'VECTOR', 'b': 'VECTOR'}, 'RGBA': {'a': 'RGBA', 'b': 'RGBA'}, 'ROTATION': {'a': 'ROTATION', 'b': 'ROTATION'}}},
    )

class ShaderNodeMixRGBOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]

def mix_legacy(*, factor: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5, color1: Color | Field[Color] | Grid[Color] | List[Color] | Socket[Color | Field[Color] | Grid[Color] | List[Color]] = (0.5, 0.5, 0.5, 1.0), color2: Color | Field[Color] | Grid[Color] | List[Color] | Socket[Color | Field[Color] | Grid[Color] | List[Color]] = (0.5, 0.5, 0.5, 1.0), blend_type: typing.Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX', use_alpha: bool = False, use_clamp: bool = False) -> ShaderNodeMixRGBOutputs:
    'Args:\n    use_alpha: Include alpha of second input in this operation\n    use_clamp: Clamp result of the node to 0.0 to 1.0 range'
    return _node_function(
        'ShaderNodeMixRGB',
        inputs={
            'factor': factor,
            'color1': color1,
            'color2': color2,
        },
        input_sockets={
            'factor': ('Fac', 'Factor', 0, 0.5),
            'color1': ('Color1', 'Color1', 1, (0.5, 0.5, 0.5, 1.0)),
            'color2': ('Color2', 'Color2', 2, (0.5, 0.5, 0.5, 1.0)),
        },
        properties={
            'blend_type': blend_type,
            'use_alpha': use_alpha,
            'use_clamp': use_clamp,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeMixRGBOutputs,
    )

class GeometryNodeToolMousePositionOutputs(typing.NamedTuple):
    mouse_x: Socket[int]
    mouse_y: Socket[int]
    region_width: Socket[int]
    region_height: Socket[int]

def mouse_position() -> GeometryNodeToolMousePositionOutputs:
    return _node_function(
        'GeometryNodeToolMousePosition',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'mouse_x': ('Mouse X', 'Mouse X', 0, 'AUTO'),
            'mouse_y': ('Mouse Y', 'Mouse Y', 1, 'AUTO'),
            'region_width': ('Region Width', 'Region Width', 2, 'AUTO'),
            'region_height': ('Region Height', 'Region Height', 3, 'AUTO'),
        },
        output_type=GeometryNodeToolMousePositionOutputs,
    )

class FunctionNodeMatrixMultiplyOutputs(typing.NamedTuple):
    matrix: Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]

def multiply_matrices(*, matrix: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None, matrix_2: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None) -> FunctionNodeMatrixMultiplyOutputs:
    return _node_function(
        'FunctionNodeMatrixMultiply',
        inputs={
            'matrix': matrix,
            'matrix_2': matrix_2,
        },
        input_sockets={
            'matrix': ('Matrix', 'Matrix', 0, None),
            'matrix_2': ('Matrix_001', 'Matrix', 1, None),
        },
        properties={
        },
        output_sockets={
            'matrix': ('Matrix', 'Matrix', 0, 'AUTO'),
        },
        output_type=FunctionNodeMatrixMultiplyOutputs,
    )

class GeometryNodeInputNamedAttributeOutputs(typing.NamedTuple):
    attribute: Socket[Field[float] | Field[int] | Field[bool] | Field[Vector] | Field[Color] | Field[Rotation] | Field[Matrix]]
    exists: Socket[Field[bool]]

def named_attribute(*, name: str | Socket[str] = '', data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None) -> GeometryNodeInputNamedAttributeOutputs:
    'Args:\n    data_type: The data type used to read the attribute values Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeInputNamedAttribute',
        inputs={
            'name': name,
        },
        input_sockets={
            'name': ('Name', 'Name', 0, ''),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'attribute': ('Attribute', 'Attribute', 0, 'FIELD'),
            'exists': ('Exists', 'Exists', 1, 'FIELD'),
        },
        output_type=GeometryNodeInputNamedAttributeOutputs,
        type_properties={'data_type': {'FLOAT': {}, 'INT': {}, 'BOOLEAN': {}, 'FLOAT_VECTOR': {}, 'FLOAT_COLOR': {}, 'QUATERNION': {}, 'FLOAT4X4': {}}},
    )

class GeometryNodeInputNamedLayerSelectionOutputs(typing.NamedTuple):
    selection: Socket[Field[bool]]

def named_layer_selection(*, name: str | Socket[str] = '') -> GeometryNodeInputNamedLayerSelectionOutputs:
    return _node_function(
        'GeometryNodeInputNamedLayerSelection',
        inputs={
            'name': name,
        },
        input_sockets={
            'name': ('Name', 'Name', 0, ''),
        },
        properties={
        },
        output_sockets={
            'selection': ('Selection', 'Selection', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputNamedLayerSelectionOutputs,
    )

class GeometryNodeTool3DCursorOutputs(typing.NamedTuple):
    location: Socket[Vector]
    rotation: Socket[Rotation]

def node_3_d_cursor() -> GeometryNodeTool3DCursorOutputs:
    return _node_function(
        'GeometryNodeTool3DCursor',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'location': ('Location', 'Location', 0, 'AUTO'),
            'rotation': ('Rotation', 'Rotation', 1, 'AUTO'),
        },
        output_type=GeometryNodeTool3DCursorOutputs,
    )

class ShaderNodeTexNoiseOutputs(typing.NamedTuple):
    factor: Socket[float | Field[float] | Grid[float] | List[float]]
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]

def noise_texture(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), scale: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 5.0, detail: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 2.0, roughness: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5, lacunarity: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 2.0, distortion: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, w: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, offset: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, gain: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, noise_dimensions: typing.Literal['1D', '2D', '3D', '4D'] = '3D', noise_type: typing.Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM', normalize: bool = True) -> ShaderNodeTexNoiseOutputs:
    'Args:\n    noise_dimensions: Number of dimensions to output noise for\n    noise_type: Type of the Noise texture\n    normalize: Normalize outputs to 0.0 to 1.0 range'
    return _node_function(
        'ShaderNodeTexNoise',
        inputs={
            'vector': vector,
            'scale': scale,
            'detail': detail,
            'roughness': roughness,
            'lacunarity': lacunarity,
            'distortion': distortion,
            'w': w,
            'offset': offset,
            'gain': gain,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'scale': ('Scale', 'Scale', 2, 5.0),
            'detail': ('Detail', 'Detail', 3, 2.0),
            'roughness': ('Roughness', 'Roughness', 4, 0.5),
            'lacunarity': ('Lacunarity', 'Lacunarity', 5, 2.0),
            'distortion': ('Distortion', 'Distortion', 8, 0.0),
            'w': ('W', 'W', 1, 0.0),
            'offset': ('Offset', 'Offset', 6, 0.0),
            'gain': ('Gain', 'Gain', 7, 1.0),
        },
        properties={
            'noise_dimensions': noise_dimensions,
            'noise_type': noise_type,
            'normalize': normalize,
        },
        output_sockets={
            'factor': ('Fac', 'Factor', 0, 'FIELD'),
            'color': ('Color', 'Color', 1, 'FIELD'),
        },
        output_type=ShaderNodeTexNoiseOutputs,
    )

class GeometryNodeInputNormalOutputs(typing.NamedTuple):
    normal: Socket[Field[Vector]]
    true_normal: Socket[Field[Vector]]

def normal(*, legacy_corner_normals: bool = False) -> GeometryNodeInputNormalOutputs:
    'Args:\n    legacy_corner_normals: Always use face normals for the face corner domain, matching old behavior of the node'
    return _node_function(
        'GeometryNodeInputNormal',
        inputs={
        },
        input_sockets={
        },
        properties={
            'legacy_corner_normals': legacy_corner_normals,
        },
        output_sockets={
            'normal': ('Normal', 'Normal', 0, 'FIELD'),
            'true_normal': ('True Normal', 'True Normal', 1, 'FIELD'),
        },
        output_type=GeometryNodeInputNormalOutputs,
    )

class GeometryNodeInputObjectOutputs(typing.NamedTuple):
    object: Socket[Object]

def object_(*, object: bpy.types.Object | None = None) -> GeometryNodeInputObjectOutputs:
    return _node_function(
        'GeometryNodeInputObject',
        inputs={
        },
        input_sockets={
        },
        properties={
            'object': object,
        },
        output_sockets={
            'object': ('Object', 'Object', 0, 'AUTO'),
        },
        output_type=GeometryNodeInputObjectOutputs,
    )

class GeometryNodeObjectInfoOutputs(typing.NamedTuple):
    transform: Socket[Matrix]
    location: Socket[Vector]
    rotation: Socket[Rotation]
    scale: Socket[Vector]
    geometry: Socket[Geometry]

def object_info(*, object: Object | Socket[Object] | None = None, as_instance: bool | Socket[bool] = False, transform_space: typing.Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL') -> GeometryNodeObjectInfoOutputs:
    'Args:\n    transform_space: The transformation of the vector and geometry outputs'
    return _node_function(
        'GeometryNodeObjectInfo',
        inputs={
            'object': object,
            'as_instance': as_instance,
        },
        input_sockets={
            'object': ('Object', 'Object', 0, None),
            'as_instance': ('As Instance', 'As Instance', 1, False),
        },
        properties={
            'transform_space': transform_space,
        },
        output_sockets={
            'transform': ('Transform', 'Transform', 0, 'AUTO'),
            'location': ('Location', 'Location', 1, 'AUTO'),
            'rotation': ('Rotation', 'Rotation', 2, 'AUTO'),
            'scale': ('Scale', 'Scale', 3, 'AUTO'),
            'geometry': ('Geometry', 'Geometry', 4, 'AUTO'),
        },
        output_type=GeometryNodeObjectInfoOutputs,
    )

class GeometryNodeOffsetCornerInFaceOutputs(typing.NamedTuple):
    corner_index: Socket[Field[int]]

def offset_corner_in_face(*, corner_index: int | Field[int] | Socket[int | Field[int]] = 0, offset: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeOffsetCornerInFaceOutputs:
    return _node_function(
        'GeometryNodeOffsetCornerInFace',
        inputs={
            'corner_index': corner_index,
            'offset': offset,
        },
        input_sockets={
            'corner_index': ('Corner Index', 'Corner Index', 0, 0),
            'offset': ('Offset', 'Offset', 1, 0),
        },
        properties={
        },
        output_sockets={
            'corner_index': ('Corner Index', 'Corner Index', 0, 'FIELD'),
        },
        output_type=GeometryNodeOffsetCornerInFaceOutputs,
    )

class GeometryNodeOffsetPointInCurveOutputs(typing.NamedTuple):
    is_valid_offset: Socket[Field[bool]]
    point_index: Socket[Field[int]]

def offset_point_in_curve(*, point_index: int | Field[int] | Socket[int | Field[int]] = 0, offset: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeOffsetPointInCurveOutputs:
    return _node_function(
        'GeometryNodeOffsetPointInCurve',
        inputs={
            'point_index': point_index,
            'offset': offset,
        },
        input_sockets={
            'point_index': ('Point Index', 'Point Index', 0, 0),
            'offset': ('Offset', 'Offset', 1, 0),
        },
        properties={
        },
        output_sockets={
            'is_valid_offset': ('Is Valid Offset', 'Is Valid Offset', 0, 'FIELD'),
            'point_index': ('Point Index', 'Point Index', 1, 'FIELD'),
        },
        output_type=GeometryNodeOffsetPointInCurveOutputs,
    )

class GeometryNodeUVPackIslandsOutputs(typing.NamedTuple):
    uv: Socket[Field[Vector]]

def pack_uv_islands(*, uv: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, margin: float | Socket[float] = 0.0010000000474974513, rotate: bool | Socket[bool] = True, method: Menu | Socket[Menu] = 'Bounding Box', bottom_left: Vector2 | Socket[Vector2] = (0.0, 0.0), top_right: Vector2 | Socket[Vector2] = (1.0, 1.0)) -> GeometryNodeUVPackIslandsOutputs:
    return _node_function(
        'GeometryNodeUVPackIslands',
        inputs={
            'uv': uv,
            'selection': selection,
            'margin': margin,
            'rotate': rotate,
            'method': method,
            'bottom_left': bottom_left,
            'top_right': top_right,
        },
        input_sockets={
            'uv': ('UV', 'UV', 0, (0.0, 0.0, 0.0)),
            'selection': ('Selection', 'Selection', 1, True),
            'margin': ('Margin', 'Margin', 2, 0.0010000000474974513),
            'rotate': ('Rotate', 'Rotate', 3, True),
            'method': ('Method', 'Method', 4, 'Bounding Box'),
            'bottom_left': ('Bottom Left', 'Bottom Left', 5, (0.0, 0.0)),
            'top_right': ('Top Right', 'Top Right', 6, (1.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'uv': ('UV', 'UV', 0, 'FIELD'),
        },
        output_type=GeometryNodeUVPackIslandsOutputs,
    )

class GeometryNodePointsOutputs(typing.NamedTuple):
    points: Socket[Geometry]

def points(*, count: int | Socket[int] = 1, position: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), radius: float | Field[float] | Socket[float | Field[float]] = 0.10000000149011612) -> GeometryNodePointsOutputs:
    return _node_function(
        'GeometryNodePoints',
        inputs={
            'count': count,
            'position': position,
            'radius': radius,
        },
        input_sockets={
            'count': ('Count', 'Count', 0, 1),
            'position': ('Position', 'Position', 1, (0.0, 0.0, 0.0)),
            'radius': ('Radius', 'Radius', 2, 0.10000000149011612),
        },
        properties={
        },
        output_sockets={
            'points': ('Geometry', 'Points', 0, 'AUTO'),
        },
        output_type=GeometryNodePointsOutputs,
    )

class GeometryNodePointsOfCurveOutputs(typing.NamedTuple):
    point_index: Socket[Field[int]]
    total: Socket[Field[int]]

def points_of_curve(*, curve_index: int | Field[int] | Socket[int | Field[int]] = 0, weights: float | Field[float] | Socket[float | Field[float]] = 0.0, sort_index: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodePointsOfCurveOutputs:
    return _node_function(
        'GeometryNodePointsOfCurve',
        inputs={
            'curve_index': curve_index,
            'weights': weights,
            'sort_index': sort_index,
        },
        input_sockets={
            'curve_index': ('Curve Index', 'Curve Index', 0, 0),
            'weights': ('Weights', 'Weights', 1, 0.0),
            'sort_index': ('Sort Index', 'Sort Index', 2, 0),
        },
        properties={
        },
        output_sockets={
            'point_index': ('Point Index', 'Point Index', 0, 'FIELD'),
            'total': ('Total', 'Total', 1, 'FIELD'),
        },
        output_type=GeometryNodePointsOfCurveOutputs,
    )

class GeometryNodePointsToCurvesOutputs(typing.NamedTuple):
    curves: Socket[Geometry]

def points_to_curves(*, points: Geometry | Socket[Geometry] | None = None, curve_group_id: int | Field[int] | Socket[int | Field[int]] = 0, weight: float | Field[float] | Socket[float | Field[float]] = 0.0) -> GeometryNodePointsToCurvesOutputs:
    return _node_function(
        'GeometryNodePointsToCurves',
        inputs={
            'points': points,
            'curve_group_id': curve_group_id,
            'weight': weight,
        },
        input_sockets={
            'points': ('Points', 'Points', 0, None),
            'curve_group_id': ('Curve Group ID', 'Curve Group ID', 1, 0),
            'weight': ('Weight', 'Weight', 2, 0.0),
        },
        properties={
        },
        output_sockets={
            'curves': ('Curves', 'Curves', 0, 'AUTO'),
        },
        output_type=GeometryNodePointsToCurvesOutputs,
    )

class GeometryNodePointsToSDFGridOutputs(typing.NamedTuple):
    sdf_grid: Socket[Grid[float]]

def points_to_sdf_grid(*, points: Geometry | Socket[Geometry] | None = None, radius: float | Field[float] | Socket[float | Field[float]] = 0.5, voxel_size: float | Socket[float] = 0.30000001192092896) -> GeometryNodePointsToSDFGridOutputs:
    return _node_function(
        'GeometryNodePointsToSDFGrid',
        inputs={
            'points': points,
            'radius': radius,
            'voxel_size': voxel_size,
        },
        input_sockets={
            'points': ('Points', 'Points', 0, None),
            'radius': ('Radius', 'Radius', 1, 0.5),
            'voxel_size': ('Voxel Size', 'Voxel Size', 2, 0.30000001192092896),
        },
        properties={
        },
        output_sockets={
            'sdf_grid': ('SDF Grid', 'SDF Grid', 0, 'GRID'),
        },
        output_type=GeometryNodePointsToSDFGridOutputs,
    )

class GeometryNodePointsToVerticesOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def points_to_vertices(*, points: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True) -> GeometryNodePointsToVerticesOutputs:
    return _node_function(
        'GeometryNodePointsToVertices',
        inputs={
            'points': points,
            'selection': selection,
        },
        input_sockets={
            'points': ('Points', 'Points', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodePointsToVerticesOutputs,
    )

class GeometryNodePointsToVolumeOutputs(typing.NamedTuple):
    volume: Socket[Geometry]

def points_to_volume(*, points: Geometry | Socket[Geometry] | None = None, density: float | Socket[float] = 1.0, resolution_mode: Menu | Socket[Menu] = 'Amount', voxel_size: float | Socket[float] = 0.30000001192092896, voxel_amount: float | Socket[float] = 64.0, radius: float | Field[float] | Socket[float | Field[float]] = 0.5) -> GeometryNodePointsToVolumeOutputs:
    return _node_function(
        'GeometryNodePointsToVolume',
        inputs={
            'points': points,
            'density': density,
            'resolution_mode': resolution_mode,
            'voxel_size': voxel_size,
            'voxel_amount': voxel_amount,
            'radius': radius,
        },
        input_sockets={
            'points': ('Points', 'Points', 0, None),
            'density': ('Density', 'Density', 1, 1.0),
            'resolution_mode': ('Resolution Mode', 'Resolution Mode', 2, 'Amount'),
            'voxel_size': ('Voxel Size', 'Voxel Size', 3, 0.30000001192092896),
            'voxel_amount': ('Voxel Amount', 'Voxel Amount', 4, 64.0),
            'radius': ('Radius', 'Radius', 5, 0.5),
        },
        properties={
        },
        output_sockets={
            'volume': ('Volume', 'Volume', 0, 'AUTO'),
        },
        output_type=GeometryNodePointsToVolumeOutputs,
    )

class GeometryNodeInputPositionOutputs(typing.NamedTuple):
    position: Socket[Field[Vector]]

def position() -> GeometryNodeInputPositionOutputs:
    return _node_function(
        'GeometryNodeInputPosition',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'position': ('Position', 'Position', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputPositionOutputs,
    )

class FunctionNodeProjectPointOutputs(typing.NamedTuple):
    vector: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def project_point(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), transform: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None) -> FunctionNodeProjectPointOutputs:
    return _node_function(
        'FunctionNodeProjectPoint',
        inputs={
            'vector': vector,
            'transform': transform,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'transform': ('Transform', 'Transform', 1, None),
        },
        properties={
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
        },
        output_type=FunctionNodeProjectPointOutputs,
    )

class GeometryNodeGridPruneOutputs(typing.NamedTuple):
    grid: Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]]

def prune_grid(*, grid: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, mode: Menu | Socket[Menu] = 'Threshold', threshold: float | int | Vector | Socket[float | int | Vector] = 0.009999999776482582, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeGridPruneOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeGridPrune',
        inputs={
            'grid': grid,
            'mode': mode,
            'threshold': threshold,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'mode': ('Mode', 'Mode', 1, 'Threshold'),
            'threshold': ('Threshold', 'Threshold', 2, 0.009999999776482582),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeGridPruneOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE', 'threshold': 'VALUE'}, 'INT': {'grid': 'INT', 'threshold': 'INT'}, 'BOOLEAN': {'grid': 'BOOLEAN'}, 'VECTOR': {'grid': 'VECTOR', 'threshold': 'VECTOR'}}},
    )

class GeometryNodeCurveQuadraticBezierOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def quadratic_b_zier(*, resolution: int | Socket[int] = 16, start: Vector | Socket[Vector] = (-1.0, 0.0, 0.0), middle: Vector | Socket[Vector] = (0.0, 2.0, 0.0), end: Vector | Socket[Vector] = (1.0, 0.0, 0.0)) -> GeometryNodeCurveQuadraticBezierOutputs:
    return _node_function(
        'GeometryNodeCurveQuadraticBezier',
        inputs={
            'resolution': resolution,
            'start': start,
            'middle': middle,
            'end': end,
        },
        input_sockets={
            'resolution': ('Resolution', 'Resolution', 0, 16),
            'start': ('Start', 'Start', 1, (-1.0, 0.0, 0.0)),
            'middle': ('Middle', 'Middle', 2, (0.0, 2.0, 0.0)),
            'end': ('End', 'End', 3, (1.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeCurveQuadraticBezierOutputs,
    )

class GeometryNodeCurvePrimitiveQuadrilateralOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def quadrilateral(*, width: float | Socket[float] = 2.0, height: float | Socket[float] = 2.0, offset: float | Socket[float] = 1.0, bottom_width: float | Socket[float] = 4.0, top_width: float | Socket[float] = 2.0, bottom_height: float | Socket[float] = 3.0, top_height: float | Socket[float] = 1.0, point_1: Vector | Socket[Vector] = (-1.0, -1.0, 0.0), point_2: Vector | Socket[Vector] = (1.0, -1.0, 0.0), point_3: Vector | Socket[Vector] = (1.0, 1.0, 0.0), point_4: Vector | Socket[Vector] = (-1.0, 1.0, 0.0), mode: typing.Literal['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS'] = 'RECTANGLE') -> GeometryNodeCurvePrimitiveQuadrilateralOutputs:
    return _node_function(
        'GeometryNodeCurvePrimitiveQuadrilateral',
        inputs={
            'width': width,
            'height': height,
            'offset': offset,
            'bottom_width': bottom_width,
            'top_width': top_width,
            'bottom_height': bottom_height,
            'top_height': top_height,
            'point_1': point_1,
            'point_2': point_2,
            'point_3': point_3,
            'point_4': point_4,
        },
        input_sockets={
            'width': ('Width', 'Width', 0, 2.0),
            'height': ('Height', 'Height', 1, 2.0),
            'offset': ('Offset', 'Offset', 4, 1.0),
            'bottom_width': ('Bottom Width', 'Bottom Width', 2, 4.0),
            'top_width': ('Top Width', 'Top Width', 3, 2.0),
            'bottom_height': ('Bottom Height', 'Bottom Height', 5, 3.0),
            'top_height': ('Top Height', 'Top Height', 6, 1.0),
            'point_1': ('Point 1', 'Point 1', 7, (-1.0, -1.0, 0.0)),
            'point_2': ('Point 2', 'Point 2', 8, (1.0, -1.0, 0.0)),
            'point_3': ('Point 3', 'Point 3', 9, (1.0, 1.0, 0.0)),
            'point_4': ('Point 4', 'Point 4', 10, (-1.0, 1.0, 0.0)),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeCurvePrimitiveQuadrilateralOutputs,
    )

class FunctionNodeQuaternionToRotationOutputs(typing.NamedTuple):
    rotation: Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]]

def quaternion_to_rotation(*, w: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, x: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, y: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, z: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0) -> FunctionNodeQuaternionToRotationOutputs:
    return _node_function(
        'FunctionNodeQuaternionToRotation',
        inputs={
            'w': w,
            'x': x,
            'y': y,
            'z': z,
        },
        input_sockets={
            'w': ('W', 'W', 0, 1.0),
            'x': ('X', 'X', 1, 0.0),
            'y': ('Y', 'Y', 2, 0.0),
            'z': ('Z', 'Z', 3, 0.0),
        },
        properties={
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'AUTO'),
        },
        output_type=FunctionNodeQuaternionToRotationOutputs,
    )

class ShaderNodeRadialTilingOutputs(typing.NamedTuple):
    segment_coordinates: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    segment_id: Socket[float | Field[float] | Grid[float] | List[float]]
    segment_width: Socket[float | Field[float] | Grid[float] | List[float]]
    segment_rotation: Socket[float | Field[float] | Grid[float] | List[float]]

def radial_tiling(*, vector: Vector2 | Field[Vector2] | Grid[Vector2] | List[Vector2] | Socket[Vector2 | Field[Vector2] | Grid[Vector2] | List[Vector2]] = (0.0, 0.0), sides: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 5.0, roundness: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, normalize: bool = False) -> ShaderNodeRadialTilingOutputs:
    "Args:\n    normalize: Normalize the X coordinate of the Segment Coordinates output to a [0, 1] interval and offset the Y coordinate into a [0, infinity) interval. When checked, the textures are stretched to fit into each angular segment. When not checked, the parts of the textures that don't fit into each angular segment are cropped"
    return _node_function(
        'ShaderNodeRadialTiling',
        inputs={
            'vector': vector,
            'sides': sides,
            'roundness': roundness,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0)),
            'sides': ('Sides', 'Sides', 1, 5.0),
            'roundness': ('Roundness', 'Roundness', 2, 0.0),
        },
        properties={
            'normalize': normalize,
        },
        output_sockets={
            'segment_coordinates': ('Segment Coordinates', 'Segment Coordinates', 0, 'AUTO'),
            'segment_id': ('Segment ID', 'Segment ID', 1, 'AUTO'),
            'segment_width': ('Segment Width', 'Segment Width', 2, 'AUTO'),
            'segment_rotation': ('Segment Rotation', 'Segment Rotation', 3, 'AUTO'),
        },
        output_type=ShaderNodeRadialTilingOutputs,
    )

class GeometryNodeInputRadiusOutputs(typing.NamedTuple):
    radius: Socket[Field[float]]

def radius() -> GeometryNodeInputRadiusOutputs:
    return _node_function(
        'GeometryNodeInputRadius',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'radius': ('Radius', 'Radius', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputRadiusOutputs,
    )

class FunctionNodeRandomValueOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def random_value(*, min: float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | Vector | Field[Vector] | Grid[Vector] | List[Vector]] = 0.0, max: float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | Vector | Field[Vector] | Grid[Vector] | List[Vector]] = 1.0, id: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, seed: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, probability: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None) -> FunctionNodeRandomValueOutputs:
    'Args:\n    data_type: Type of data stored in attribute Inferred from the linked inputs when None.'
    return _node_function(
        'FunctionNodeRandomValue',
        inputs={
            'min': min,
            'max': max,
            'id': id,
            'seed': seed,
            'probability': probability,
        },
        input_sockets={
            'min': ('Min', 'Min', 0, 0.0),
            'max': ('Max', 'Max', 1, 1.0),
            'id': ('ID', 'ID', 2, 0),
            'seed': ('Seed', 'Seed', 3, 0),
            'probability': ('Probability', 'Probability', 0, 0.5),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'FIELD'),
        },
        output_type=FunctionNodeRandomValueOutputs,
        type_properties={'data_type': {'FLOAT': {'min': 'VALUE', 'max': 'VALUE'}, 'INT': {'min': 'INT', 'max': 'INT'}, 'BOOLEAN': {}, 'FLOAT_VECTOR': {'min': 'VECTOR', 'max': 'VECTOR'}}},
    )

class GeometryNodeRaycastOutputs(typing.NamedTuple):
    is_hit: Socket[bool | Field[bool] | Grid[bool] | List[bool]]
    hit_position: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    hit_normal: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    hit_distance: Socket[float | Field[float] | Grid[float] | List[float]]
    attribute: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]

def raycast(*, target_geometry: Geometry | Socket[Geometry] | None = None, attribute: float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix] | Socket[float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix]] = 0.0, interpolation: Menu | Socket[Menu] = 'Interpolated', source_position: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), ray_direction: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, -1.0), ray_length: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 100.0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None) -> GeometryNodeRaycastOutputs:
    'Args:\n    data_type: Type of data stored in attribute Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeRaycast',
        inputs={
            'target_geometry': target_geometry,
            'attribute': attribute,
            'interpolation': interpolation,
            'source_position': source_position,
            'ray_direction': ray_direction,
            'ray_length': ray_length,
        },
        input_sockets={
            'target_geometry': ('Target Geometry', 'Target Geometry', 0, None),
            'attribute': ('Attribute', 'Attribute', 1, 0.0),
            'interpolation': ('Interpolation', 'Interpolation', 2, 'Interpolated'),
            'source_position': ('Source Position', 'Source Position', 3, (0.0, 0.0, 0.0)),
            'ray_direction': ('Ray Direction', 'Ray Direction', 4, (0.0, 0.0, -1.0)),
            'ray_length': ('Ray Length', 'Ray Length', 5, 100.0),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'is_hit': ('Is Hit', 'Is Hit', 0, 'FIELD'),
            'hit_position': ('Hit Position', 'Hit Position', 1, 'FIELD'),
            'hit_normal': ('Hit Normal', 'Hit Normal', 2, 'FIELD'),
            'hit_distance': ('Hit Distance', 'Hit Distance', 3, 'FIELD'),
            'attribute': ('Attribute', 'Attribute', 4, 'FIELD'),
        },
        output_type=GeometryNodeRaycastOutputs,
        type_properties={'data_type': {'FLOAT': {'attribute': 'VALUE'}, 'INT': {'attribute': 'INT'}, 'BOOLEAN': {'attribute': 'BOOLEAN'}, 'FLOAT_VECTOR': {'attribute': 'VECTOR'}, 'FLOAT_COLOR': {'attribute': 'RGBA'}, 'QUATERNION': {'attribute': 'ROTATION'}, 'FLOAT4X4': {'attribute': 'MATRIX'}}},
    )

class GeometryNodeRealizeInstancesOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def realize_instances(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, realize_all: bool | Field[bool] | Socket[bool | Field[bool]] = True, depth: int | Field[int] | Socket[int | Field[int]] = 0, realize_to_point_domain: bool = False) -> GeometryNodeRealizeInstancesOutputs:
    'Args:\n    realize_to_point_domain: Propagate instance attributes to the point domain rather than the curve domain. This property exists for compatibility with 5.0 and earlier.'
    return _node_function(
        'GeometryNodeRealizeInstances',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'realize_all': realize_all,
            'depth': depth,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'realize_all': ('Realize All', 'Realize All', 2, True),
            'depth': ('Depth', 'Depth', 3, 0),
        },
        properties={
            'realize_to_point_domain': realize_to_point_domain,
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeRealizeInstancesOutputs,
    )

class GeometryNodeRemoveAttributeOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def remove_named_attribute(*, geometry: Geometry | Socket[Geometry] | None = None, pattern_mode: Menu | Socket[Menu] = 'Exact', name: str | Socket[str] = '') -> GeometryNodeRemoveAttributeOutputs:
    return _node_function(
        'GeometryNodeRemoveAttribute',
        inputs={
            'geometry': geometry,
            'pattern_mode': pattern_mode,
            'name': name,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'pattern_mode': ('Pattern Mode', 'Pattern Mode', 1, 'Exact'),
            'name': ('Name', 'Name', 2, ''),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeRemoveAttributeOutputs,
    )

class GeometryNodeRenameAttributeOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def rename_attribute(*, geometry: Geometry | Socket[Geometry] | None = None, mode: Menu | Socket[Menu] = 'Single', old: str | Socket[str] = '', new: str | Socket[str] = '', overwrite: bool | Socket[bool] = False) -> GeometryNodeRenameAttributeOutputs:
    return _node_function(
        'GeometryNodeRenameAttribute',
        inputs={
            'geometry': geometry,
            'mode': mode,
            'old': old,
            'new': new,
            'overwrite': overwrite,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'mode': ('Mode', 'Mode', 1, 'Single'),
            'old': ('Old', 'Old', 2, ''),
            'new': ('New', 'New', 3, ''),
            'overwrite': ('Overwrite', 'Overwrite', 4, False),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeRenameAttributeOutputs,
    )

class GeometryNodeReplaceMaterialOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def replace_material(*, geometry: Geometry | Socket[Geometry] | None = None, old: Material | Socket[Material] | None = None, new: Material | Socket[Material] | None = None) -> GeometryNodeReplaceMaterialOutputs:
    return _node_function(
        'GeometryNodeReplaceMaterial',
        inputs={
            'geometry': geometry,
            'old': old,
            'new': new,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'old': ('Old', 'Old', 1, None),
            'new': ('New', 'New', 2, None),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeReplaceMaterialOutputs,
    )

class FunctionNodeReplaceStringOutputs(typing.NamedTuple):
    string: Socket[str | Field[str] | Grid[str] | List[str]]

def replace_string(*, string: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', find: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', replace: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '') -> FunctionNodeReplaceStringOutputs:
    return _node_function(
        'FunctionNodeReplaceString',
        inputs={
            'string': string,
            'find': find,
            'replace': replace,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
            'find': ('Find', 'Find', 1, ''),
            'replace': ('Replace', 'Replace', 2, ''),
        },
        properties={
        },
        output_sockets={
            'string': ('String', 'String', 0, 'AUTO'),
        },
        output_type=FunctionNodeReplaceStringOutputs,
    )

class GeometryNodeResampleCurveOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def resample_curve(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, mode: Menu | Socket[Menu] = 'Count', count: int | Field[int] | Socket[int | Field[int]] = 10, length: float | Field[float] | Socket[float | Field[float]] = 0.10000000149011612, keep_last_segment: bool = True) -> GeometryNodeResampleCurveOutputs:
    'Args:\n    keep_last_segment: Do not collapse curves to single points if they are shorter than the given length. The collapsing behavior exists for compatibility reasons.'
    return _node_function(
        'GeometryNodeResampleCurve',
        inputs={
            'curve': curve,
            'selection': selection,
            'mode': mode,
            'count': count,
            'length': length,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'mode': ('Mode', 'Mode', 2, 'Count'),
            'count': ('Count', 'Count', 3, 10),
            'length': ('Length', 'Length', 4, 0.10000000149011612),
        },
        properties={
            'keep_last_segment': keep_last_segment,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeResampleCurveOutputs,
    )

class GeometryNodeReverseCurveOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def reverse_curve(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True) -> GeometryNodeReverseCurveOutputs:
    return _node_function(
        'GeometryNodeReverseCurve',
        inputs={
            'curve': curve,
            'selection': selection,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeReverseCurveOutputs,
    )

class FunctionNodeReverseStringOutputs(typing.NamedTuple):
    string: Socket[str | Field[str] | Grid[str] | List[str]]

def reverse_string(*, string: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '') -> FunctionNodeReverseStringOutputs:
    return _node_function(
        'FunctionNodeReverseString',
        inputs={
            'string': string,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
        },
        properties={
        },
        output_sockets={
            'string': ('String', 'String', 0, 'AUTO'),
        },
        output_type=FunctionNodeReverseStringOutputs,
    )

class ShaderNodeRGBCurveOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]

def rgb_curves(*, factor: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, color: Color | Field[Color] | Grid[Color] | List[Color] | Socket[Color | Field[Color] | Grid[Color] | List[Color]] = (1.0, 1.0, 1.0, 1.0)) -> ShaderNodeRGBCurveOutputs:
    return _node_function(
        'ShaderNodeRGBCurve',
        inputs={
            'factor': factor,
            'color': color,
        },
        input_sockets={
            'factor': ('Fac', 'Factor', 0, 1.0),
            'color': ('Color', 'Color', 1, (1.0, 1.0, 1.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeRGBCurveOutputs,
    )

class FunctionNodeRotateEulerOutputs(typing.NamedTuple):
    rotation: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def rotate_euler(*, rotation: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), rotate_by: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), axis: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 1.0), angle: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, rotation_type: typing.Literal['AXIS_ANGLE', 'EULER'] = 'EULER', space: typing.Literal['OBJECT', 'LOCAL'] = 'OBJECT') -> FunctionNodeRotateEulerOutputs:
    'Args:\n    rotation_type: Method used to describe the rotation\n    space: Base orientation for rotation'
    return _node_function(
        'FunctionNodeRotateEuler',
        inputs={
            'rotation': rotation,
            'rotate_by': rotate_by,
            'axis': axis,
            'angle': angle,
        },
        input_sockets={
            'rotation': ('Rotation', 'Rotation', 0, (0.0, 0.0, 0.0)),
            'rotate_by': ('Rotate By', 'Rotate By', 1, (0.0, 0.0, 0.0)),
            'axis': ('Axis', 'Axis', 1, (0.0, 0.0, 1.0)),
            'angle': ('Angle', 'Angle', 2, 0.0),
        },
        properties={
            'rotation_type': rotation_type,
            'space': space,
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'AUTO'),
        },
        output_type=FunctionNodeRotateEulerOutputs,
    )

class GeometryNodeRotateInstancesOutputs(typing.NamedTuple):
    instances: Socket[Geometry]

def rotate_instances(*, instances: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, rotation: Rotation | Field[Rotation] | Socket[Rotation | Field[Rotation]] = (0.0, 0.0, 0.0), pivot_point: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), local_space: bool | Field[bool] | Socket[bool | Field[bool]] = True) -> GeometryNodeRotateInstancesOutputs:
    return _node_function(
        'GeometryNodeRotateInstances',
        inputs={
            'instances': instances,
            'selection': selection,
            'rotation': rotation,
            'pivot_point': pivot_point,
            'local_space': local_space,
        },
        input_sockets={
            'instances': ('Instances', 'Instances', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'rotation': ('Rotation', 'Rotation', 2, (0.0, 0.0, 0.0)),
            'pivot_point': ('Pivot Point', 'Pivot Point', 3, (0.0, 0.0, 0.0)),
            'local_space': ('Local Space', 'Local Space', 4, True),
        },
        properties={
        },
        output_sockets={
            'instances': ('Instances', 'Instances', 0, 'AUTO'),
        },
        output_type=GeometryNodeRotateInstancesOutputs,
    )

class FunctionNodeRotateRotationOutputs(typing.NamedTuple):
    rotation: Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]]

def rotate_rotation(*, rotation: Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = (0.0, 0.0, 0.0), rotate_by: Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = (0.0, 0.0, 0.0), rotation_space: typing.Literal['GLOBAL', 'LOCAL'] = 'GLOBAL') -> FunctionNodeRotateRotationOutputs:
    'Args:\n    rotation_space: Base orientation for the rotation'
    return _node_function(
        'FunctionNodeRotateRotation',
        inputs={
            'rotation': rotation,
            'rotate_by': rotate_by,
        },
        input_sockets={
            'rotation': ('Rotation', 'Rotation', 0, (0.0, 0.0, 0.0)),
            'rotate_by': ('Rotate By', 'Rotate By', 1, (0.0, 0.0, 0.0)),
        },
        properties={
            'rotation_space': rotation_space,
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'AUTO'),
        },
        output_type=FunctionNodeRotateRotationOutputs,
    )

class FunctionNodeRotateVectorOutputs(typing.NamedTuple):
    vector: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def rotate_vector(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), rotation: Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = (0.0, 0.0, 0.0)) -> FunctionNodeRotateVectorOutputs:
    return _node_function(
        'FunctionNodeRotateVector',
        inputs={
            'vector': vector,
            'rotation': rotation,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'rotation': ('Rotation', 'Rotation', 1, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
        },
        output_type=FunctionNodeRotateVectorOutputs,
    )

class FunctionNodeInputRotationOutputs(typing.NamedTuple):
    rotation: Socket[Rotation]

def rotation(*, rotation_euler: Vector = (0.0, 0.0, 0.0)) -> FunctionNodeInputRotationOutputs:
    'Args:\n    rotation_euler: Input value used for unconnected socket'
    return _node_function(
        'FunctionNodeInputRotation',
        inputs={
        },
        input_sockets={
        },
        properties={
            'rotation_euler': rotation_euler,
        },
        output_sockets={
            'rotation': ('Rotation', 'Rotation', 0, 'AUTO'),
        },
        output_type=FunctionNodeInputRotationOutputs,
    )

class FunctionNodeRotationToAxisAngleOutputs(typing.NamedTuple):
    axis: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    angle: Socket[float | Field[float] | Grid[float] | List[float]]

def rotation_to_axis_angle(*, rotation: Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = (0.0, 0.0, 0.0)) -> FunctionNodeRotationToAxisAngleOutputs:
    return _node_function(
        'FunctionNodeRotationToAxisAngle',
        inputs={
            'rotation': rotation,
        },
        input_sockets={
            'rotation': ('Rotation', 'Rotation', 0, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'axis': ('Axis', 'Axis', 0, 'AUTO'),
            'angle': ('Angle', 'Angle', 1, 'AUTO'),
        },
        output_type=FunctionNodeRotationToAxisAngleOutputs,
    )

class FunctionNodeRotationToEulerOutputs(typing.NamedTuple):
    euler: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def rotation_to_euler(*, rotation: Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = (0.0, 0.0, 0.0)) -> FunctionNodeRotationToEulerOutputs:
    return _node_function(
        'FunctionNodeRotationToEuler',
        inputs={
            'rotation': rotation,
        },
        input_sockets={
            'rotation': ('Rotation', 'Rotation', 0, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'euler': ('Euler', 'Euler', 0, 'AUTO'),
        },
        output_type=FunctionNodeRotationToEulerOutputs,
    )

class FunctionNodeRotationToQuaternionOutputs(typing.NamedTuple):
    w: Socket[float | Field[float] | Grid[float] | List[float]]
    x: Socket[float | Field[float] | Grid[float] | List[float]]
    y: Socket[float | Field[float] | Grid[float] | List[float]]
    z: Socket[float | Field[float] | Grid[float] | List[float]]

def rotation_to_quaternion(*, rotation: Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]] = (0.0, 0.0, 0.0)) -> FunctionNodeRotationToQuaternionOutputs:
    return _node_function(
        'FunctionNodeRotationToQuaternion',
        inputs={
            'rotation': rotation,
        },
        input_sockets={
            'rotation': ('Rotation', 'Rotation', 0, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'w': ('W', 'W', 0, 'AUTO'),
            'x': ('X', 'X', 1, 'AUTO'),
            'y': ('Y', 'Y', 2, 'AUTO'),
            'z': ('Z', 'Z', 3, 'AUTO'),
        },
        output_type=FunctionNodeRotationToQuaternionOutputs,
    )

class GeometryNodeSampleCurveOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]
    position: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    tangent: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    normal: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def sample_curve(*, curves: Geometry | Socket[Geometry] | None = None, value: float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix] | Socket[float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix]] = 0.0, factor: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, curve_index: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, length: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, mode: typing.Literal['FACTOR', 'LENGTH'] = 'FACTOR', use_all_curves: bool = False, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None) -> GeometryNodeSampleCurveOutputs:
    'Args:\n    mode: Method for sampling input\n    use_all_curves: Sample lengths based on the total length of all curves, rather than using a length inside each selected curve\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeSampleCurve',
        inputs={
            'curves': curves,
            'value': value,
            'factor': factor,
            'curve_index': curve_index,
            'length': length,
        },
        input_sockets={
            'curves': ('Curves', 'Curves', 0, None),
            'value': ('Value', 'Value', 1, 0.0),
            'factor': ('Factor', 'Factor', 2, 0.0),
            'curve_index': ('Curve Index', 'Curve Index', 4, 0),
            'length': ('Length', 'Length', 3, 0.0),
        },
        properties={
            'mode': mode,
            'use_all_curves': use_all_curves,
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
            'position': ('Position', 'Position', 1, 'AUTO'),
            'tangent': ('Tangent', 'Tangent', 2, 'AUTO'),
            'normal': ('Normal', 'Normal', 3, 'AUTO'),
        },
        output_type=GeometryNodeSampleCurveOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'BOOLEAN': {'value': 'BOOLEAN'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}, 'FLOAT_COLOR': {'value': 'RGBA'}, 'QUATERNION': {'value': 'ROTATION'}, 'FLOAT4X4': {'value': 'MATRIX'}}},
    )

class GeometryNodeSampleGridOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def sample_grid(*, grid: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, position: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), interpolation: Menu | Socket[Menu] = 'Trilinear', data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeSampleGridOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeSampleGrid',
        inputs={
            'grid': grid,
            'position': position,
            'interpolation': interpolation,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'position': ('Position', 'Position', 1, (0.0, 0.0, 0.0)),
            'interpolation': ('Interpolation', 'Interpolation', 2, 'Trilinear'),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'FIELD'),
        },
        output_type=GeometryNodeSampleGridOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'BOOLEAN': {'grid': 'BOOLEAN'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class GeometryNodeSampleGridIndexOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def sample_grid_index(*, grid: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, x: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, y: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, z: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeSampleGridIndexOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeSampleGridIndex',
        inputs={
            'grid': grid,
            'x': x,
            'y': y,
            'z': z,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'x': ('X', 'X', 1, 0),
            'y': ('Y', 'Y', 2, 0),
            'z': ('Z', 'Z', 3, 0),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=GeometryNodeSampleGridIndexOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'BOOLEAN': {'grid': 'BOOLEAN'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class GeometryNodeSampleIndexOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]

def sample_index(*, geometry: Geometry | Socket[Geometry] | None = None, value: float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix] | Socket[float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix]] = 0.0, index: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT', clamp: bool = False) -> GeometryNodeSampleIndexOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.\n    clamp: Clamp the indices to the size of the attribute domain instead of outputting a default value for invalid indices'
    return _node_function(
        'GeometryNodeSampleIndex',
        inputs={
            'geometry': geometry,
            'value': value,
            'index': index,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'value': ('Value', 'Value', 1, 0.0),
            'index': ('Index', 'Index', 2, 0),
        },
        properties={
            'data_type': data_type,
            'domain': domain,
            'clamp': clamp,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=GeometryNodeSampleIndexOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'BOOLEAN': {'value': 'BOOLEAN'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}, 'FLOAT_COLOR': {'value': 'RGBA'}, 'QUATERNION': {'value': 'ROTATION'}, 'FLOAT4X4': {'value': 'MATRIX'}}},
    )

class GeometryNodeSampleNearestOutputs(typing.NamedTuple):
    index: Socket[int | Field[int] | Grid[int] | List[int]]

def sample_nearest(*, geometry: Geometry | Socket[Geometry] | None = None, sample_position: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER'] = 'POINT') -> GeometryNodeSampleNearestOutputs:
    return _node_function(
        'GeometryNodeSampleNearest',
        inputs={
            'geometry': geometry,
            'sample_position': sample_position,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'sample_position': ('Sample Position', 'Sample Position', 1, (0.0, 0.0, 0.0)),
        },
        properties={
            'domain': domain,
        },
        output_sockets={
            'index': ('Index', 'Index', 0, 'FIELD'),
        },
        output_type=GeometryNodeSampleNearestOutputs,
    )

class GeometryNodeSampleNearestSurfaceOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]
    is_valid: Socket[bool | Field[bool] | Grid[bool] | List[bool]]

def sample_nearest_surface(*, mesh: Geometry | Socket[Geometry] | None = None, value: float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix] | Socket[float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix]] = 0.0, group_id: int | Field[int] | Socket[int | Field[int]] = 0, sample_position: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), sample_group_id: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None) -> GeometryNodeSampleNearestSurfaceOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeSampleNearestSurface',
        inputs={
            'mesh': mesh,
            'value': value,
            'group_id': group_id,
            'sample_position': sample_position,
            'sample_group_id': sample_group_id,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'value': ('Value', 'Value', 1, 0.0),
            'group_id': ('Group ID', 'Group ID', 2, 0),
            'sample_position': ('Sample Position', 'Sample Position', 3, (0.0, 0.0, 0.0)),
            'sample_group_id': ('Sample Group ID', 'Sample Group ID', 4, 0),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'FIELD'),
            'is_valid': ('Is Valid', 'Is Valid', 1, 'FIELD'),
        },
        output_type=GeometryNodeSampleNearestSurfaceOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'BOOLEAN': {'value': 'BOOLEAN'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}, 'FLOAT_COLOR': {'value': 'RGBA'}, 'QUATERNION': {'value': 'ROTATION'}, 'FLOAT4X4': {'value': 'MATRIX'}}},
    )

class GeometryNodeSampleSoundFrequenciesOutputs(typing.NamedTuple):
    amplitude: Socket[float | Field[float] | Grid[float] | List[float]]

def sample_sound_frequencies(*, sound: Sound | Socket[Sound] | None = None, time: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, all_channels: bool | Field[bool] | Grid[bool] | List[bool] | Socket[bool | Field[bool] | Grid[bool] | List[bool]] = True, channel: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, low: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, high: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 10000.0, fft_size: Menu | Socket[Menu] = '4096', window_function: Menu | Socket[Menu] = 'Hann') -> GeometryNodeSampleSoundFrequenciesOutputs:
    return _node_function(
        'GeometryNodeSampleSoundFrequencies',
        inputs={
            'sound': sound,
            'time': time,
            'all_channels': all_channels,
            'channel': channel,
            'low': low,
            'high': high,
            'fft_size': fft_size,
            'window_function': window_function,
        },
        input_sockets={
            'sound': ('Sound', 'Sound', 0, None),
            'time': ('Time', 'Time', 1, 0.0),
            'all_channels': ('All Channels', 'All Channels', 2, True),
            'channel': ('Channel', 'Channel', 3, 0),
            'low': ('Low', 'Low', 4, 0.0),
            'high': ('High', 'High', 5, 10000.0),
            'fft_size': ('FFT Size', 'FFT Size', 6, '4096'),
            'window_function': ('Window Function', 'Window Function', 7, 'Hann'),
        },
        properties={
        },
        output_sockets={
            'amplitude': ('Amplitude', 'Amplitude', 0, 'AUTO'),
        },
        output_type=GeometryNodeSampleSoundFrequenciesOutputs,
    )

class GeometryNodeSampleUVSurfaceOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]
    is_valid: Socket[bool | Field[bool] | Grid[bool] | List[bool]]

def sample_uv_surface(*, mesh: Geometry | Socket[Geometry] | None = None, value: float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix] | Socket[float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix]] = 0.0, uv_map: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), sample_uv: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None) -> GeometryNodeSampleUVSurfaceOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeSampleUVSurface',
        inputs={
            'mesh': mesh,
            'value': value,
            'uv_map': uv_map,
            'sample_uv': sample_uv,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'value': ('Value', 'Value', 1, 0.0),
            'uv_map': ('Source UV Map', 'UV Map', 2, (0.0, 0.0, 0.0)),
            'sample_uv': ('Sample UV', 'Sample UV', 3, (0.0, 0.0, 0.0)),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
            'is_valid': ('Is Valid', 'Is Valid', 1, 'AUTO'),
        },
        output_type=GeometryNodeSampleUVSurfaceOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'BOOLEAN': {'value': 'BOOLEAN'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}, 'FLOAT_COLOR': {'value': 'RGBA'}, 'QUATERNION': {'value': 'ROTATION'}, 'FLOAT4X4': {'value': 'MATRIX'}}},
    )

class GeometryNodeScaleElementsOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def scale_elements(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, scale: float | Field[float] | Socket[float | Field[float]] = 1.0, center: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), scale_mode: Menu | Socket[Menu] = 'Uniform', axis: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (1.0, 0.0, 0.0), domain: typing.Literal['FACE', 'EDGE'] = 'FACE') -> GeometryNodeScaleElementsOutputs:
    'Args:\n    domain: Element type to transform'
    return _node_function(
        'GeometryNodeScaleElements',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'scale': scale,
            'center': center,
            'scale_mode': scale_mode,
            'axis': axis,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'scale': ('Scale', 'Scale', 2, 1.0),
            'center': ('Center', 'Center', 3, (0.0, 0.0, 0.0)),
            'scale_mode': ('Scale Mode', 'Scale Mode', 4, 'Uniform'),
            'axis': ('Axis', 'Axis', 5, (1.0, 0.0, 0.0)),
        },
        properties={
            'domain': domain,
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeScaleElementsOutputs,
    )

class GeometryNodeScaleInstancesOutputs(typing.NamedTuple):
    instances: Socket[Geometry]

def scale_instances(*, instances: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, scale: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (1.0, 1.0, 1.0), center: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), local_space: bool | Field[bool] | Socket[bool | Field[bool]] = True) -> GeometryNodeScaleInstancesOutputs:
    return _node_function(
        'GeometryNodeScaleInstances',
        inputs={
            'instances': instances,
            'selection': selection,
            'scale': scale,
            'center': center,
            'local_space': local_space,
        },
        input_sockets={
            'instances': ('Instances', 'Instances', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'scale': ('Scale', 'Scale', 2, (1.0, 1.0, 1.0)),
            'center': ('Center', 'Center', 3, (0.0, 0.0, 0.0)),
            'local_space': ('Local Space', 'Local Space', 4, True),
        },
        properties={
        },
        output_sockets={
            'instances': ('Instances', 'Instances', 0, 'AUTO'),
        },
        output_type=GeometryNodeScaleInstancesOutputs,
    )

class GeometryNodeInputSceneTimeOutputs(typing.NamedTuple):
    seconds: Socket[float]
    frame: Socket[float]

def scene_time() -> GeometryNodeInputSceneTimeOutputs:
    return _node_function(
        'GeometryNodeInputSceneTime',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'seconds': ('Seconds', 'Seconds', 0, 'AUTO'),
            'frame': ('Frame', 'Frame', 1, 'AUTO'),
        },
        output_type=GeometryNodeInputSceneTimeOutputs,
    )

class GeometryNodeSDFGridBooleanOutputs(typing.NamedTuple):
    grid: Socket[Grid[float]]

def sdf_grid_boolean(*, grid_1: Grid[float] | Socket[Grid[float]] | None = None, grid_2: typing.Sequence[Grid[float] | Socket[Grid[float]]] = (), grid: typing.Sequence[Grid[float] | Socket[Grid[float]]] = (), operation: typing.Literal['INTERSECT', 'UNION', 'DIFFERENCE'] = 'DIFFERENCE') -> GeometryNodeSDFGridBooleanOutputs:
    return _node_function(
        'GeometryNodeSDFGridBoolean',
        inputs={
            'grid_1': grid_1,
            'grid_2': grid_2,
            'grid': grid,
        },
        input_sockets={
            'grid_1': ('Grid 1', 'Grid 1', 0, None),
            'grid_2': ('Grid 2', 'Grid 2', 1, ()),
            'grid': ('Grid 2', 'Grid', 1, ()),
        },
        properties={
            'operation': operation,
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeSDFGridBooleanOutputs,
    )

class GeometryNodeSDFGridFilletOutputs(typing.NamedTuple):
    grid: Socket[Grid[float]]

def sdf_grid_fillet(*, grid: Grid[float] | Socket[Grid[float]] | None = None, iterations: int | Socket[int] = 1) -> GeometryNodeSDFGridFilletOutputs:
    return _node_function(
        'GeometryNodeSDFGridFillet',
        inputs={
            'grid': grid,
            'iterations': iterations,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'iterations': ('Iterations', 'Iterations', 1, 1),
        },
        properties={
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeSDFGridFilletOutputs,
    )

class GeometryNodeSDFGridLaplacianOutputs(typing.NamedTuple):
    grid: Socket[Grid[float]]

def sdf_grid_laplacian(*, grid: Grid[float] | Socket[Grid[float]] | None = None, iterations: int | Socket[int] = 1) -> GeometryNodeSDFGridLaplacianOutputs:
    return _node_function(
        'GeometryNodeSDFGridLaplacian',
        inputs={
            'grid': grid,
            'iterations': iterations,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'iterations': ('Iterations', 'Iterations', 1, 1),
        },
        properties={
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeSDFGridLaplacianOutputs,
    )

class GeometryNodeSDFGridMeanOutputs(typing.NamedTuple):
    grid: Socket[Grid[float]]

def sdf_grid_mean(*, grid: Grid[float] | Socket[Grid[float]] | None = None, width: int | Socket[int] = 1, iterations: int | Socket[int] = 1) -> GeometryNodeSDFGridMeanOutputs:
    return _node_function(
        'GeometryNodeSDFGridMean',
        inputs={
            'grid': grid,
            'width': width,
            'iterations': iterations,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'width': ('Width', 'Width', 1, 1),
            'iterations': ('Iterations', 'Iterations', 2, 1),
        },
        properties={
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeSDFGridMeanOutputs,
    )

class GeometryNodeSDFGridMeanCurvatureOutputs(typing.NamedTuple):
    grid: Socket[Grid[float]]

def sdf_grid_mean_curvature(*, grid: Grid[float] | Socket[Grid[float]] | None = None, iterations: int | Socket[int] = 1) -> GeometryNodeSDFGridMeanCurvatureOutputs:
    return _node_function(
        'GeometryNodeSDFGridMeanCurvature',
        inputs={
            'grid': grid,
            'iterations': iterations,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'iterations': ('Iterations', 'Iterations', 1, 1),
        },
        properties={
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeSDFGridMeanCurvatureOutputs,
    )

class GeometryNodeSDFGridMedianOutputs(typing.NamedTuple):
    grid: Socket[Grid[float]]

def sdf_grid_median(*, grid: Grid[float] | Socket[Grid[float]] | None = None, width: int | Socket[int] = 1, iterations: int | Socket[int] = 1) -> GeometryNodeSDFGridMedianOutputs:
    return _node_function(
        'GeometryNodeSDFGridMedian',
        inputs={
            'grid': grid,
            'width': width,
            'iterations': iterations,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'width': ('Width', 'Width', 1, 1),
            'iterations': ('Iterations', 'Iterations', 2, 1),
        },
        properties={
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeSDFGridMedianOutputs,
    )

class GeometryNodeSDFGridOffsetOutputs(typing.NamedTuple):
    grid: Socket[Grid[float]]

def sdf_grid_offset(*, grid: Grid[float] | Socket[Grid[float]] | None = None, distance: float | Socket[float] = 0.10000000149011612) -> GeometryNodeSDFGridOffsetOutputs:
    return _node_function(
        'GeometryNodeSDFGridOffset',
        inputs={
            'grid': grid,
            'distance': distance,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'distance': ('Distance', 'Distance', 1, 0.10000000149011612),
        },
        properties={
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeSDFGridOffsetOutputs,
    )

class GeometryNodeToolSelectionOutputs(typing.NamedTuple):
    boolean: Socket[Field[bool]]
    float: Socket[Field[float]]

def selection() -> GeometryNodeToolSelectionOutputs:
    return _node_function(
        'GeometryNodeToolSelection',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'boolean': ('Selection', 'Boolean', 0, 'FIELD'),
            'float': ('Float', 'Float', 1, 'FIELD'),
        },
        output_type=GeometryNodeToolSelectionOutputs,
    )

class GeometryNodeSelfObjectOutputs(typing.NamedTuple):
    self_object: Socket[Object]

def self_object() -> GeometryNodeSelfObjectOutputs:
    return _node_function(
        'GeometryNodeSelfObject',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'self_object': ('Self Object', 'Self Object', 0, 'AUTO'),
        },
        output_type=GeometryNodeSelfObjectOutputs,
    )

class NodeSeparateBundleOutputs(ItemOutputs):
    pass

def separate_bundle(*, bundle: Bundle | Socket[Bundle] | None = None, define_signature: bool = False, items: typing.Mapping[str, typing.Any] | None = None) -> NodeSeparateBundleOutputs:
    'Args:\n    define_signature: This node defines a bundle signature that should be used by other nodes\n    items: Items to add, mapping each name to its type (float, Vector, Geometry, ...). Their outputs are available by name on the result.'
    return _node_function(
        'NodeSeparateBundle',
        inputs={
            'bundle': bundle,
        },
        input_sockets={
            'bundle': ('Bundle', 'Bundle', 0, None),
        },
        properties={
            'define_signature': define_signature,
        },
        output_sockets={
        },
        output_type=NodeSeparateBundleOutputs,
        item_collections=(
            ('bundle_items', 'types', items),
        ),
    )

class FunctionNodeSeparateColorOutputs(typing.NamedTuple):
    red: Socket[float | Field[float] | Grid[float] | List[float]]
    green: Socket[float | Field[float] | Grid[float] | List[float]]
    blue: Socket[float | Field[float] | Grid[float] | List[float]]
    alpha: Socket[float | Field[float] | Grid[float] | List[float]]

def separate_color(*, color: Color | Field[Color] | Grid[Color] | List[Color] | Socket[Color | Field[Color] | Grid[Color] | List[Color]] = (1.0, 1.0, 1.0, 1.0), mode: typing.Literal['RGB', 'HSV', 'HSL'] = 'RGB') -> FunctionNodeSeparateColorOutputs:
    'Args:\n    mode: Mode of color processing'
    return _node_function(
        'FunctionNodeSeparateColor',
        inputs={
            'color': color,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 1.0, 1.0, 1.0)),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'red': ('Red', 'Red', 0, 'AUTO'),
            'green': ('Green', 'Green', 1, 'AUTO'),
            'blue': ('Blue', 'Blue', 2, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 3, 'AUTO'),
        },
        output_type=FunctionNodeSeparateColorOutputs,
    )

class GeometryNodeSeparateComponentsOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]
    curve: Socket[Geometry]
    grease_pencil: Socket[Geometry]
    point_cloud: Socket[Geometry]
    volume: Socket[Geometry]
    instances: Socket[Geometry]

def separate_components(*, geometry: Geometry | Socket[Geometry] | None = None) -> GeometryNodeSeparateComponentsOutputs:
    return _node_function(
        'GeometryNodeSeparateComponents',
        inputs={
            'geometry': geometry,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
            'curve': ('Curve', 'Curve', 1, 'AUTO'),
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 2, 'AUTO'),
            'point_cloud': ('Point Cloud', 'Point Cloud', 3, 'AUTO'),
            'volume': ('Volume', 'Volume', 4, 'AUTO'),
            'instances': ('Instances', 'Instances', 5, 'AUTO'),
        },
        output_type=GeometryNodeSeparateComponentsOutputs,
    )

class GeometryNodeSeparateGeometryOutputs(typing.NamedTuple):
    selection: Socket[Geometry]
    inverted: Socket[Geometry]

def separate_geometry(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT') -> GeometryNodeSeparateGeometryOutputs:
    'Args:\n    domain: Which domain to separate on'
    return _node_function(
        'GeometryNodeSeparateGeometry',
        inputs={
            'geometry': geometry,
            'selection': selection,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
            'domain': domain,
        },
        output_sockets={
            'selection': ('Selection', 'Selection', 0, 'AUTO'),
            'inverted': ('Inverted', 'Inverted', 1, 'AUTO'),
        },
        output_type=GeometryNodeSeparateGeometryOutputs,
    )

class FunctionNodeSeparateMatrixOutputs(typing.NamedTuple):
    column_1_row_1: Socket[float | Field[float] | Grid[float] | List[float]]
    column_1_row_2: Socket[float | Field[float] | Grid[float] | List[float]]
    column_1_row_3: Socket[float | Field[float] | Grid[float] | List[float]]
    column_1_row_4: Socket[float | Field[float] | Grid[float] | List[float]]
    column_2_row_1: Socket[float | Field[float] | Grid[float] | List[float]]
    column_2_row_2: Socket[float | Field[float] | Grid[float] | List[float]]
    column_2_row_3: Socket[float | Field[float] | Grid[float] | List[float]]
    column_2_row_4: Socket[float | Field[float] | Grid[float] | List[float]]
    column_3_row_1: Socket[float | Field[float] | Grid[float] | List[float]]
    column_3_row_2: Socket[float | Field[float] | Grid[float] | List[float]]
    column_3_row_3: Socket[float | Field[float] | Grid[float] | List[float]]
    column_3_row_4: Socket[float | Field[float] | Grid[float] | List[float]]
    column_4_row_1: Socket[float | Field[float] | Grid[float] | List[float]]
    column_4_row_2: Socket[float | Field[float] | Grid[float] | List[float]]
    column_4_row_3: Socket[float | Field[float] | Grid[float] | List[float]]
    column_4_row_4: Socket[float | Field[float] | Grid[float] | List[float]]

def separate_matrix(*, matrix: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None) -> FunctionNodeSeparateMatrixOutputs:
    return _node_function(
        'FunctionNodeSeparateMatrix',
        inputs={
            'matrix': matrix,
        },
        input_sockets={
            'matrix': ('Matrix', 'Matrix', 0, None),
        },
        properties={
        },
        output_sockets={
            'column_1_row_1': ('Column 1 Row 1', 'Column 1 Row 1', 0, 'AUTO'),
            'column_1_row_2': ('Column 1 Row 2', 'Column 1 Row 2', 1, 'AUTO'),
            'column_1_row_3': ('Column 1 Row 3', 'Column 1 Row 3', 2, 'AUTO'),
            'column_1_row_4': ('Column 1 Row 4', 'Column 1 Row 4', 3, 'AUTO'),
            'column_2_row_1': ('Column 2 Row 1', 'Column 2 Row 1', 4, 'AUTO'),
            'column_2_row_2': ('Column 2 Row 2', 'Column 2 Row 2', 5, 'AUTO'),
            'column_2_row_3': ('Column 2 Row 3', 'Column 2 Row 3', 6, 'AUTO'),
            'column_2_row_4': ('Column 2 Row 4', 'Column 2 Row 4', 7, 'AUTO'),
            'column_3_row_1': ('Column 3 Row 1', 'Column 3 Row 1', 8, 'AUTO'),
            'column_3_row_2': ('Column 3 Row 2', 'Column 3 Row 2', 9, 'AUTO'),
            'column_3_row_3': ('Column 3 Row 3', 'Column 3 Row 3', 10, 'AUTO'),
            'column_3_row_4': ('Column 3 Row 4', 'Column 3 Row 4', 11, 'AUTO'),
            'column_4_row_1': ('Column 4 Row 1', 'Column 4 Row 1', 12, 'AUTO'),
            'column_4_row_2': ('Column 4 Row 2', 'Column 4 Row 2', 13, 'AUTO'),
            'column_4_row_3': ('Column 4 Row 3', 'Column 4 Row 3', 14, 'AUTO'),
            'column_4_row_4': ('Column 4 Row 4', 'Column 4 Row 4', 15, 'AUTO'),
        },
        output_type=FunctionNodeSeparateMatrixOutputs,
    )

class FunctionNodeSeparateTransformOutputs(typing.NamedTuple):
    translation: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    rotation: Socket[Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation]]
    scale: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def separate_transform(*, transform: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None) -> FunctionNodeSeparateTransformOutputs:
    return _node_function(
        'FunctionNodeSeparateTransform',
        inputs={
            'transform': transform,
        },
        input_sockets={
            'transform': ('Transform', 'Transform', 0, None),
        },
        properties={
        },
        output_sockets={
            'translation': ('Translation', 'Translation', 0, 'AUTO'),
            'rotation': ('Rotation', 'Rotation', 1, 'AUTO'),
            'scale': ('Scale', 'Scale', 2, 'AUTO'),
        },
        output_type=FunctionNodeSeparateTransformOutputs,
    )

class ShaderNodeSeparateXYZOutputs(typing.NamedTuple):
    x: Socket[float | Field[float] | Grid[float] | List[float]]
    y: Socket[float | Field[float] | Grid[float] | List[float]]
    z: Socket[float | Field[float] | Grid[float] | List[float]]

def separate_xyz(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0)) -> ShaderNodeSeparateXYZOutputs:
    return _node_function(
        'ShaderNodeSeparateXYZ',
        inputs={
            'vector': vector,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'x': ('X', 'X', 0, 'AUTO'),
            'y': ('Y', 'Y', 1, 'AUTO'),
            'z': ('Z', 'Z', 2, 'AUTO'),
        },
        output_type=ShaderNodeSeparateXYZOutputs,
    )

class GeometryNodeSetCurveNormalOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def set_curve_normal(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, mode: Menu | Socket[Menu] = 'Minimum Twist', normal: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 1.0)) -> GeometryNodeSetCurveNormalOutputs:
    return _node_function(
        'GeometryNodeSetCurveNormal',
        inputs={
            'curve': curve,
            'selection': selection,
            'mode': mode,
            'normal': normal,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'mode': ('Mode', 'Mode', 2, 'Minimum Twist'),
            'normal': ('Normal', 'Normal', 3, (0.0, 0.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetCurveNormalOutputs,
    )

class GeometryNodeSetCurveRadiusOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def set_curve_radius(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, radius: float | Field[float] | Socket[float | Field[float]] = 0.004999999888241291) -> GeometryNodeSetCurveRadiusOutputs:
    return _node_function(
        'GeometryNodeSetCurveRadius',
        inputs={
            'curve': curve,
            'selection': selection,
            'radius': radius,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'radius': ('Radius', 'Radius', 2, 0.004999999888241291),
        },
        properties={
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetCurveRadiusOutputs,
    )

class GeometryNodeSetCurveTiltOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def set_curve_tilt(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, tilt: float | Field[float] | Socket[float | Field[float]] = 0.0) -> GeometryNodeSetCurveTiltOutputs:
    return _node_function(
        'GeometryNodeSetCurveTilt',
        inputs={
            'curve': curve,
            'selection': selection,
            'tilt': tilt,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'tilt': ('Tilt', 'Tilt', 2, 0.0),
        },
        properties={
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetCurveTiltOutputs,
    )

class GeometryNodeToolSetFaceSetOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def set_face_set(*, mesh: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, face_set: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeToolSetFaceSetOutputs:
    return _node_function(
        'GeometryNodeToolSetFaceSet',
        inputs={
            'mesh': mesh,
            'selection': selection,
            'face_set': face_set,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'face_set': ('Face Set', 'Face Set', 2, 0),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeToolSetFaceSetOutputs,
    )

class GeometryNodeSetGeometryBundleOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def set_geometry_bundle(*, geometry: Geometry | Socket[Geometry] | None = None, bundle: Bundle | Socket[Bundle] | None = None) -> GeometryNodeSetGeometryBundleOutputs:
    return _node_function(
        'GeometryNodeSetGeometryBundle',
        inputs={
            'geometry': geometry,
            'bundle': bundle,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'bundle': ('Bundle', 'Bundle', 1, None),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetGeometryBundleOutputs,
    )

class GeometryNodeSetGeometryNameOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def set_geometry_name(*, geometry: Geometry | Socket[Geometry] | None = None, name: str | Socket[str] = '') -> GeometryNodeSetGeometryNameOutputs:
    return _node_function(
        'GeometryNodeSetGeometryName',
        inputs={
            'geometry': geometry,
            'name': name,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'name': ('Name', 'Name', 1, ''),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetGeometryNameOutputs,
    )

class GeometryNodeSetGreasePencilColorOutputs(typing.NamedTuple):
    grease_pencil: Socket[Geometry]

def set_grease_pencil_color(*, grease_pencil: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, color: Color | Field[Color] | Socket[Color | Field[Color]] = (1.0, 1.0, 1.0, 1.0), opacity: float | Field[float] | Socket[float | Field[float]] = 1.0, mode: typing.Literal['STROKE', 'FILL'] = 'STROKE') -> GeometryNodeSetGreasePencilColorOutputs:
    return _node_function(
        'GeometryNodeSetGreasePencilColor',
        inputs={
            'grease_pencil': grease_pencil,
            'selection': selection,
            'color': color,
            'opacity': opacity,
        },
        input_sockets={
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'color': ('Color', 'Color', 2, (1.0, 1.0, 1.0, 1.0)),
            'opacity': ('Opacity', 'Opacity', 3, 1.0),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetGreasePencilColorOutputs,
    )

class GeometryNodeSetGreasePencilDepthOutputs(typing.NamedTuple):
    grease_pencil: Socket[Geometry]

def set_grease_pencil_depth(*, grease_pencil: Geometry | Socket[Geometry] | None = None, depth_order: typing.Literal['2D', '3D'] = '2D') -> GeometryNodeSetGreasePencilDepthOutputs:
    return _node_function(
        'GeometryNodeSetGreasePencilDepth',
        inputs={
            'grease_pencil': grease_pencil,
        },
        input_sockets={
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 0, None),
        },
        properties={
            'depth_order': depth_order,
        },
        output_sockets={
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetGreasePencilDepthOutputs,
    )

class GeometryNodeSetGreasePencilSoftnessOutputs(typing.NamedTuple):
    grease_pencil: Socket[Geometry]

def set_grease_pencil_softness(*, grease_pencil: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, softness: float | Field[float] | Socket[float | Field[float]] = 0.0) -> GeometryNodeSetGreasePencilSoftnessOutputs:
    return _node_function(
        'GeometryNodeSetGreasePencilSoftness',
        inputs={
            'grease_pencil': grease_pencil,
            'selection': selection,
            'softness': softness,
        },
        input_sockets={
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'softness': ('Softness', 'Softness', 2, 0.0),
        },
        properties={
        },
        output_sockets={
            'grease_pencil': ('Grease Pencil', 'Grease Pencil', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetGreasePencilSoftnessOutputs,
    )

class GeometryNodeSetGridBackgroundOutputs(typing.NamedTuple):
    grid: Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]]

def set_grid_background(*, grid: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, background: float | int | bool | Vector | Socket[float | int | bool | Vector] = 0.0, update_inactive: bool | Socket[bool] = False, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeSetGridBackgroundOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeSetGridBackground',
        inputs={
            'grid': grid,
            'background': background,
            'update_inactive': update_inactive,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'background': ('Background', 'Background', 1, 0.0),
            'update_inactive': ('Update Inactive', 'Update Inactive', 2, False),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeSetGridBackgroundOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE', 'background': 'VALUE'}, 'INT': {'grid': 'INT', 'background': 'INT'}, 'BOOLEAN': {'grid': 'BOOLEAN', 'background': 'BOOLEAN'}, 'VECTOR': {'grid': 'VECTOR', 'background': 'VECTOR'}}},
    )

class GeometryNodeSetGridTransformOutputs(typing.NamedTuple):
    is_valid: Socket[bool]
    grid: Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]]

def set_grid_transform(*, grid: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, transform: Matrix | Socket[Matrix] | None = None, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeSetGridTransformOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeSetGridTransform',
        inputs={
            'grid': grid,
            'transform': transform,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
            'transform': ('Transform', 'Transform', 1, None),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'is_valid': ('Is Valid', 'Is Valid', 0, 'AUTO'),
            'grid': ('Grid', 'Grid', 1, 'GRID'),
        },
        output_type=GeometryNodeSetGridTransformOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'BOOLEAN': {'grid': 'BOOLEAN'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class GeometryNodeSetCurveHandlePositionsOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def set_handle_positions(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, position: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), offset: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), mode: typing.Literal['LEFT', 'RIGHT'] = 'LEFT') -> GeometryNodeSetCurveHandlePositionsOutputs:
    'Args:\n    mode: Whether to update left and right handles'
    return _node_function(
        'GeometryNodeSetCurveHandlePositions',
        inputs={
            'curve': curve,
            'selection': selection,
            'position': position,
            'offset': offset,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'position': ('Position', 'Position', 2, (0.0, 0.0, 0.0)),
            'offset': ('Offset', 'Offset', 3, (0.0, 0.0, 0.0)),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetCurveHandlePositionsOutputs,
    )

class GeometryNodeCurveSetHandlesOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def set_handle_type(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, handle_type: typing.Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO', mode: set[typing.Literal['LEFT', 'RIGHT']] = {'LEFT', 'RIGHT'}) -> GeometryNodeCurveSetHandlesOutputs:
    'Args:\n    mode: Whether to update left and right handles'
    return _node_function(
        'GeometryNodeCurveSetHandles',
        inputs={
            'curve': curve,
            'selection': selection,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
            'handle_type': handle_type,
            'mode': mode,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeCurveSetHandlesOutputs,
    )

class GeometryNodeSetIDOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def set_id(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, id: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeSetIDOutputs:
    return _node_function(
        'GeometryNodeSetID',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'id': id,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'id': ('ID', 'ID', 2, 0),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetIDOutputs,
    )

class GeometryNodeSetInstanceTransformOutputs(typing.NamedTuple):
    instances: Socket[Geometry]

def set_instance_transform(*, instances: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, transform: Matrix | Field[Matrix] | Socket[Matrix | Field[Matrix]] | None = None) -> GeometryNodeSetInstanceTransformOutputs:
    return _node_function(
        'GeometryNodeSetInstanceTransform',
        inputs={
            'instances': instances,
            'selection': selection,
            'transform': transform,
        },
        input_sockets={
            'instances': ('Instances', 'Instances', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'transform': ('Transform', 'Transform', 2, None),
        },
        properties={
        },
        output_sockets={
            'instances': ('Instances', 'Instances', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetInstanceTransformOutputs,
    )

class GeometryNodeSetMaterialOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def set_material(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, material: Material | Socket[Material] | None = None) -> GeometryNodeSetMaterialOutputs:
    return _node_function(
        'GeometryNodeSetMaterial',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'material': material,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'material': ('Material', 'Material', 2, None),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetMaterialOutputs,
    )

class GeometryNodeSetMaterialIndexOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def set_material_index(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, material_index: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeSetMaterialIndexOutputs:
    return _node_function(
        'GeometryNodeSetMaterialIndex',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'material_index': material_index,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'material_index': ('Material Index', 'Material Index', 2, 0),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetMaterialIndexOutputs,
    )

class GeometryNodeSetMeshNormalOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def set_mesh_normal(*, mesh: Geometry | Socket[Geometry] | None = None, remove_custom: bool | Socket[bool] = True, edge_sharpness: bool | Field[bool] | Socket[bool | Field[bool]] = False, face_sharpness: bool | Field[bool] | Socket[bool | Field[bool]] = False, custom_normal: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), mode: typing.Literal['SHARPNESS', 'FREE', 'TANGENT_SPACE'] = 'SHARPNESS', domain: typing.Literal['POINT', 'FACE', 'CORNER'] = 'POINT') -> GeometryNodeSetMeshNormalOutputs:
    'Args:\n    mode: Storage mode for custom normal data\n    domain: Attribute domain to store free custom normals'
    return _node_function(
        'GeometryNodeSetMeshNormal',
        inputs={
            'mesh': mesh,
            'remove_custom': remove_custom,
            'edge_sharpness': edge_sharpness,
            'face_sharpness': face_sharpness,
            'custom_normal': custom_normal,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'remove_custom': ('Remove Custom', 'Remove Custom', 1, True),
            'edge_sharpness': ('Edge Sharpness', 'Edge Sharpness', 2, False),
            'face_sharpness': ('Face Sharpness', 'Face Sharpness', 3, False),
            'custom_normal': ('Custom Normal', 'Custom Normal', 1, (0.0, 0.0, 0.0)),
        },
        properties={
            'mode': mode,
            'domain': domain,
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetMeshNormalOutputs,
    )

class GeometryNodeSetNURBSOrderOutputs(typing.NamedTuple):
    curves: Socket[Geometry]

def set_nurbs_order(*, curves: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, order: int | Field[int] | Socket[int | Field[int]] = 4) -> GeometryNodeSetNURBSOrderOutputs:
    return _node_function(
        'GeometryNodeSetNURBSOrder',
        inputs={
            'curves': curves,
            'selection': selection,
            'order': order,
        },
        input_sockets={
            'curves': ('Curves', 'Curves', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'order': ('Order', 'Order', 2, 4),
        },
        properties={
        },
        output_sockets={
            'curves': ('Curves', 'Curves', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetNURBSOrderOutputs,
    )

class GeometryNodeSetNURBSWeightOutputs(typing.NamedTuple):
    curves: Socket[Geometry]

def set_nurbs_weight(*, curves: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, weight: float | Field[float] | Socket[float | Field[float]] = 1.0) -> GeometryNodeSetNURBSWeightOutputs:
    return _node_function(
        'GeometryNodeSetNURBSWeight',
        inputs={
            'curves': curves,
            'selection': selection,
            'weight': weight,
        },
        input_sockets={
            'curves': ('Curves', 'Curves', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'weight': ('Weight', 'Weight', 2, 1.0),
        },
        properties={
        },
        output_sockets={
            'curves': ('Curves', 'Curves', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetNURBSWeightOutputs,
    )

class GeometryNodeSetPointRadiusOutputs(typing.NamedTuple):
    points: Socket[Geometry]

def set_point_radius(*, points: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, radius: float | Field[float] | Socket[float | Field[float]] = 0.05000000074505806) -> GeometryNodeSetPointRadiusOutputs:
    return _node_function(
        'GeometryNodeSetPointRadius',
        inputs={
            'points': points,
            'selection': selection,
            'radius': radius,
        },
        input_sockets={
            'points': ('Points', 'Points', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'radius': ('Radius', 'Radius', 2, 0.05000000074505806),
        },
        properties={
        },
        output_sockets={
            'points': ('Points', 'Points', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetPointRadiusOutputs,
    )

class GeometryNodeSetPositionOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def set_position(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, position: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), offset: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0)) -> GeometryNodeSetPositionOutputs:
    return _node_function(
        'GeometryNodeSetPosition',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'position': position,
            'offset': offset,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'position': ('Position', 'Position', 2, (0.0, 0.0, 0.0)),
            'offset': ('Offset', 'Offset', 3, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetPositionOutputs,
    )

class GeometryNodeToolSetSelectionOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def set_selection(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | float | Field[float] | Socket[bool | Field[bool] | float | Field[float]] = True, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CURVE'] = 'POINT', selection_type: typing.Literal['BOOLEAN', 'FLOAT'] | None = None) -> GeometryNodeToolSetSelectionOutputs:
    'Args:\n    selection_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeToolSetSelection',
        inputs={
            'geometry': geometry,
            'selection': selection,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
            'domain': domain,
            'selection_type': selection_type,
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeToolSetSelectionOutputs,
        type_properties={'selection_type': {'BOOLEAN': {'selection': 'BOOLEAN'}, 'FLOAT': {'selection': 'VALUE'}}},
    )

class GeometryNodeSetShadeSmoothOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def set_shade_smooth(*, mesh: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, shade_smooth: bool | Field[bool] | Socket[bool | Field[bool]] = True, domain: typing.Literal['EDGE', 'FACE'] = 'FACE') -> GeometryNodeSetShadeSmoothOutputs:
    return _node_function(
        'GeometryNodeSetShadeSmooth',
        inputs={
            'mesh': mesh,
            'selection': selection,
            'shade_smooth': shade_smooth,
        },
        input_sockets={
            'mesh': ('Geometry', 'Mesh', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'shade_smooth': ('Shade Smooth', 'Shade Smooth', 2, True),
        },
        properties={
            'domain': domain,
        },
        output_sockets={
            'mesh': ('Geometry', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetShadeSmoothOutputs,
    )

class GeometryNodeSetSplineCyclicOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def set_spline_cyclic(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, cyclic: bool | Field[bool] | Socket[bool | Field[bool]] = False) -> GeometryNodeSetSplineCyclicOutputs:
    return _node_function(
        'GeometryNodeSetSplineCyclic',
        inputs={
            'curve': curve,
            'selection': selection,
            'cyclic': cyclic,
        },
        input_sockets={
            'curve': ('Geometry', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'cyclic': ('Cyclic', 'Cyclic', 2, False),
        },
        properties={
        },
        output_sockets={
            'curve': ('Geometry', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetSplineCyclicOutputs,
    )

class GeometryNodeSetSplineResolutionOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def set_spline_resolution(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, resolution: int | Field[int] | Socket[int | Field[int]] = 12) -> GeometryNodeSetSplineResolutionOutputs:
    return _node_function(
        'GeometryNodeSetSplineResolution',
        inputs={
            'curve': curve,
            'selection': selection,
            'resolution': resolution,
        },
        input_sockets={
            'curve': ('Geometry', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'resolution': ('Resolution', 'Resolution', 2, 12),
        },
        properties={
        },
        output_sockets={
            'curve': ('Geometry', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeSetSplineResolutionOutputs,
    )

class GeometryNodeCurveSplineTypeOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def set_spline_type(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, spline_type: typing.Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'] = 'POLY') -> GeometryNodeCurveSplineTypeOutputs:
    'Args:\n    spline_type: The curve type to change the selected curves to'
    return _node_function(
        'GeometryNodeCurveSplineType',
        inputs={
            'curve': curve,
            'selection': selection,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
            'spline_type': spline_type,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeCurveSplineTypeOutputs,
    )

class FunctionNodeSetStringCaseOutputs(typing.NamedTuple):
    string: Socket[str | Field[str] | Grid[str] | List[str]]

def set_string_case(*, string: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', case: Menu | Socket[Menu] = 'Uppercase') -> FunctionNodeSetStringCaseOutputs:
    return _node_function(
        'FunctionNodeSetStringCase',
        inputs={
            'string': string,
            'case': case,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
            'case': ('Case', 'Case', 1, 'Uppercase'),
        },
        properties={
        },
        output_sockets={
            'string': ('String', 'String', 0, 'AUTO'),
        },
        output_type=FunctionNodeSetStringCaseOutputs,
    )

class GeometryNodeInputShortestEdgePathsOutputs(typing.NamedTuple):
    next_vertex_index: Socket[Field[int]]
    total_cost: Socket[Field[float]]

def shortest_edge_paths(*, end_vertex: bool | Field[bool] | Socket[bool | Field[bool]] = False, edge_cost: float | Field[float] | Socket[float | Field[float]] = 1.0) -> GeometryNodeInputShortestEdgePathsOutputs:
    return _node_function(
        'GeometryNodeInputShortestEdgePaths',
        inputs={
            'end_vertex': end_vertex,
            'edge_cost': edge_cost,
        },
        input_sockets={
            'end_vertex': ('End Vertex', 'End Vertex', 0, False),
            'edge_cost': ('Edge Cost', 'Edge Cost', 1, 1.0),
        },
        properties={
        },
        output_sockets={
            'next_vertex_index': ('Next Vertex Index', 'Next Vertex Index', 0, 'FIELD'),
            'total_cost': ('Total Cost', 'Total Cost', 1, 'FIELD'),
        },
        output_type=GeometryNodeInputShortestEdgePathsOutputs,
    )

class FunctionNodeSliceStringOutputs(typing.NamedTuple):
    string: Socket[str | Field[str] | Grid[str] | List[str]]

def slice_string(*, string: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', position: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, length: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 10) -> FunctionNodeSliceStringOutputs:
    return _node_function(
        'FunctionNodeSliceString',
        inputs={
            'string': string,
            'position': position,
            'length': length,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
            'position': ('Position', 'Position', 1, 0),
            'length': ('Length', 'Length', 2, 10),
        },
        properties={
        },
        output_sockets={
            'string': ('String', 'String', 0, 'AUTO'),
        },
        output_type=FunctionNodeSliceStringOutputs,
    )

class GeometryNodeSortElementsOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def sort_elements(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, group_id: int | Field[int] | Socket[int | Field[int]] = 0, sort_weight: float | Field[float] | Socket[float | Field[float]] = 0.0, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE'] = 'POINT') -> GeometryNodeSortElementsOutputs:
    return _node_function(
        'GeometryNodeSortElements',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'group_id': group_id,
            'sort_weight': sort_weight,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'group_id': ('Group ID', 'Group ID', 2, 0),
            'sort_weight': ('Sort Weight', 'Sort Weight', 3, 0.0),
        },
        properties={
            'domain': domain,
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeSortElementsOutputs,
    )

class GeometryNodeSortListOutputs(typing.NamedTuple):
    list: Socket[List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound]]

def sort_list(*, list: List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound] | Socket[List[float] | List[int] | List[bool] | List[Vector] | List[Color] | List[Rotation] | List[Matrix] | List[str] | List[Menu] | List[Object] | List[Image] | List[Geometry] | List[Collection] | List[Material] | List[Bundle] | List[Closure] | List[Font] | List[Sound]] | None = None, selection: bool | Field[bool] | Grid[bool] | List[bool] | Socket[bool | Field[bool] | Grid[bool] | List[bool]] = True, group_id: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, sort_weight: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, socket_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeSortListOutputs:
    'Args:\n    socket_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeSortList',
        inputs={
            'list': list,
            'selection': selection,
            'group_id': group_id,
            'sort_weight': sort_weight,
        },
        input_sockets={
            'list': ('List', 'List', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'group_id': ('Group ID', 'Group ID', 2, 0),
            'sort_weight': ('Sort Weight', 'Sort Weight', 3, 0.0),
        },
        properties={
            'socket_type': socket_type,
        },
        output_sockets={
            'list': ('List', 'List', 0, 'LIST'),
        },
        output_type=GeometryNodeSortListOutputs,
        type_properties={'socket_type': {'FLOAT': {'list': 'VALUE'}, 'INT': {'list': 'INT'}, 'BOOLEAN': {'list': 'BOOLEAN'}, 'VECTOR': {'list': 'VECTOR'}, 'RGBA': {'list': 'RGBA'}, 'ROTATION': {'list': 'ROTATION'}, 'MATRIX': {'list': 'MATRIX'}, 'STRING': {'list': 'STRING'}, 'MENU': {'list': 'MENU'}, 'OBJECT': {'list': 'OBJECT'}, 'IMAGE': {'list': 'IMAGE'}, 'GEOMETRY': {'list': 'GEOMETRY'}, 'COLLECTION': {'list': 'COLLECTION'}, 'MATERIAL': {'list': 'MATERIAL'}, 'BUNDLE': {'list': 'BUNDLE'}, 'CLOSURE': {'list': 'CLOSURE'}, 'FONT': {'list': 'FONT'}, 'SOUND': {'list': 'SOUND'}}},
    )

class FunctionNodeInputSpecialCharactersOutputs(typing.NamedTuple):
    line_break: Socket[str]
    tab: Socket[str]

def special_characters() -> FunctionNodeInputSpecialCharactersOutputs:
    return _node_function(
        'FunctionNodeInputSpecialCharacters',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'line_break': ('Line Break', 'Line Break', 0, 'AUTO'),
            'tab': ('Tab', 'Tab', 1, 'AUTO'),
        },
        output_type=FunctionNodeInputSpecialCharactersOutputs,
    )

class GeometryNodeCurveSpiralOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def spiral(*, resolution: int | Socket[int] = 32, rotations: float | Socket[float] = 2.0, start_radius: float | Socket[float] = 1.0, end_radius: float | Socket[float] = 2.0, height: float | Socket[float] = 2.0, reverse: bool | Socket[bool] = False) -> GeometryNodeCurveSpiralOutputs:
    return _node_function(
        'GeometryNodeCurveSpiral',
        inputs={
            'resolution': resolution,
            'rotations': rotations,
            'start_radius': start_radius,
            'end_radius': end_radius,
            'height': height,
            'reverse': reverse,
        },
        input_sockets={
            'resolution': ('Resolution', 'Resolution', 0, 32),
            'rotations': ('Rotations', 'Rotations', 1, 2.0),
            'start_radius': ('Start Radius', 'Start Radius', 2, 1.0),
            'end_radius': ('End Radius', 'End Radius', 3, 2.0),
            'height': ('Height', 'Height', 4, 2.0),
            'reverse': ('Reverse', 'Reverse', 5, False),
        },
        properties={
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeCurveSpiralOutputs,
    )

class GeometryNodeSplineLengthOutputs(typing.NamedTuple):
    length: Socket[Field[float]]
    point_count: Socket[Field[int]]

def spline_length() -> GeometryNodeSplineLengthOutputs:
    return _node_function(
        'GeometryNodeSplineLength',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'length': ('Length', 'Length', 0, 'FIELD'),
            'point_count': ('Point Count', 'Point Count', 1, 'FIELD'),
        },
        output_type=GeometryNodeSplineLengthOutputs,
    )

class GeometryNodeSplineParameterOutputs(typing.NamedTuple):
    factor: Socket[Field[float]]
    length: Socket[Field[float]]
    index: Socket[Field[int]]

def spline_parameter() -> GeometryNodeSplineParameterOutputs:
    return _node_function(
        'GeometryNodeSplineParameter',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'factor': ('Factor', 'Factor', 0, 'FIELD'),
            'length': ('Length', 'Length', 1, 'FIELD'),
            'index': ('Index', 'Index', 2, 'FIELD'),
        },
        output_type=GeometryNodeSplineParameterOutputs,
    )

class GeometryNodeInputSplineResolutionOutputs(typing.NamedTuple):
    resolution: Socket[Field[int]]

def spline_resolution() -> GeometryNodeInputSplineResolutionOutputs:
    return _node_function(
        'GeometryNodeInputSplineResolution',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'resolution': ('Resolution', 'Resolution', 0, 'FIELD'),
        },
        output_type=GeometryNodeInputSplineResolutionOutputs,
    )

class GeometryNodeSplitEdgesOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def split_edges(*, mesh: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True) -> GeometryNodeSplitEdgesOutputs:
    return _node_function(
        'GeometryNodeSplitEdges',
        inputs={
            'mesh': mesh,
            'selection': selection,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeSplitEdgesOutputs,
    )

class FunctionNodeSplitStringOutputs(typing.NamedTuple):
    list: Socket[List[str]]

def split_string(*, string: str | Socket[str] = '', separator: str | Socket[str] = '') -> FunctionNodeSplitStringOutputs:
    return _node_function(
        'FunctionNodeSplitString',
        inputs={
            'string': string,
            'separator': separator,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
            'separator': ('Separator', 'Separator', 1, ''),
        },
        properties={
        },
        output_sockets={
            'list': ('List', 'List', 0, 'LIST'),
        },
        output_type=FunctionNodeSplitStringOutputs,
    )

class GeometryNodeSplitToInstancesOutputs(typing.NamedTuple):
    instances: Socket[Geometry]
    group_id: Socket[Field[int]]

def split_to_instances(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, group_id: int | Field[int] | Socket[int | Field[int]] = 0, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT') -> GeometryNodeSplitToInstancesOutputs:
    'Args:\n    domain: Attribute domain for the Selection and Group ID inputs'
    return _node_function(
        'GeometryNodeSplitToInstances',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'group_id': group_id,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'group_id': ('Group ID', 'Group ID', 2, 0),
        },
        properties={
            'domain': domain,
        },
        output_sockets={
            'instances': ('Instances', 'Instances', 0, 'AUTO'),
            'group_id': ('Group ID', 'Group ID', 1, 'FIELD'),
        },
        output_type=GeometryNodeSplitToInstancesOutputs,
    )

class GeometryNodeCurveStarOutputs(typing.NamedTuple):
    curve: Socket[Geometry]
    outer_points: Socket[Field[bool]]

def star(*, points: int | Socket[int] = 8, inner_radius: float | Socket[float] = 1.0, outer_radius: float | Socket[float] = 2.0, twist: float | Socket[float] = 0.0) -> GeometryNodeCurveStarOutputs:
    return _node_function(
        'GeometryNodeCurveStar',
        inputs={
            'points': points,
            'inner_radius': inner_radius,
            'outer_radius': outer_radius,
            'twist': twist,
        },
        input_sockets={
            'points': ('Points', 'Points', 0, 8),
            'inner_radius': ('Inner Radius', 'Inner Radius', 1, 1.0),
            'outer_radius': ('Outer Radius', 'Outer Radius', 2, 2.0),
            'twist': ('Twist', 'Twist', 3, 0.0),
        },
        properties={
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
            'outer_points': ('Outer Points', 'Outer Points', 1, 'FIELD'),
        },
        output_type=GeometryNodeCurveStarOutputs,
    )

class NodeStoreBundleItemOutputs(typing.NamedTuple):
    bundle: Socket[Bundle]

def store_bundle_item(*, bundle: Bundle | Socket[Bundle] | None = None, path: str | Socket[str] = '', item: float | int | bool | Vector | Color | Rotation | Matrix | str | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound | Socket[float | int | bool | Vector | Color | Rotation | Matrix | str | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound] = 0.0, socket_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None, structure_type: typing.Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE'] = 'AUTO') -> NodeStoreBundleItemOutputs:
    'Args:\n    socket_type:  Inferred from the linked inputs when None.\n    structure_type: What kind of higher order types are expected to flow through this socket'
    return _node_function(
        'NodeStoreBundleItem',
        inputs={
            'bundle': bundle,
            'path': path,
            'item': item,
        },
        input_sockets={
            'bundle': ('Bundle', 'Bundle', 0, None),
            'path': ('Path', 'Path', 1, ''),
            'item': ('Item', 'Item', 2, 0.0),
        },
        properties={
            'socket_type': socket_type,
            'structure_type': structure_type,
        },
        output_sockets={
            'bundle': ('Bundle', 'Bundle', 0, 'AUTO'),
        },
        output_type=NodeStoreBundleItemOutputs,
        type_properties={'socket_type': {'FLOAT': {'item': 'VALUE'}, 'INT': {'item': 'INT'}, 'BOOLEAN': {'item': 'BOOLEAN'}, 'VECTOR': {'item': 'VECTOR'}, 'RGBA': {'item': 'RGBA'}, 'ROTATION': {'item': 'ROTATION'}, 'MATRIX': {'item': 'MATRIX'}, 'STRING': {'item': 'STRING'}, 'MENU': {'item': 'MENU'}, 'OBJECT': {'item': 'OBJECT'}, 'IMAGE': {'item': 'IMAGE'}, 'GEOMETRY': {'item': 'GEOMETRY'}, 'COLLECTION': {'item': 'COLLECTION'}, 'MATERIAL': {'item': 'MATERIAL'}, 'BUNDLE': {'item': 'BUNDLE'}, 'CLOSURE': {'item': 'CLOSURE'}, 'FONT': {'item': 'FONT'}, 'SOUND': {'item': 'SOUND'}}},
    )

class GeometryNodeStoreNamedAttributeOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def store_named_attribute(*, geometry: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, name: str | Socket[str] = '', value: float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix] | Socket[float | Field[float] | int | Field[int] | bool | Field[bool] | Vector | Field[Vector] | Color | Field[Color] | Rotation | Field[Rotation] | Matrix | Field[Matrix]] = 0.0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'QUATERNION', 'FLOAT4X4', 'STRING', 'INT8', 'INT16_2D', 'INT32_2D', 'FLOAT2', 'FLOAT4', 'BYTE_COLOR'] | None = None, domain: typing.Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT') -> GeometryNodeStoreNamedAttributeOutputs:
    'Args:\n    data_type: Type of data stored in attribute Inferred from the linked inputs when None.\n    domain: Which domain to store the data in'
    return _node_function(
        'GeometryNodeStoreNamedAttribute',
        inputs={
            'geometry': geometry,
            'selection': selection,
            'name': name,
            'value': value,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'name': ('Name', 'Name', 2, ''),
            'value': ('Value', 'Value', 3, 0.0),
        },
        properties={
            'data_type': data_type,
            'domain': domain,
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeStoreNamedAttributeOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'BOOLEAN': {'value': 'BOOLEAN'}, 'FLOAT_VECTOR': {'value': 'VECTOR'}, 'FLOAT_COLOR': {'value': 'RGBA'}, 'QUATERNION': {'value': 'ROTATION'}, 'FLOAT4X4': {'value': 'MATRIX'}, 'INT8': {'value': 'INT'}, 'FLOAT2': {'value': 'VECTOR'}, 'FLOAT4': {'value': 'VECTOR'}, 'BYTE_COLOR': {'value': 'RGBA'}}},
    )

class GeometryNodeStoreNamedGridOutputs(typing.NamedTuple):
    volume: Socket[Geometry]

def store_named_grid(*, volume: Geometry | Socket[Geometry] | None = None, name: str | Socket[str] = '', grid: Grid[float] | Grid[bool] | Grid[int] | Grid[Vector] | Socket[Grid[float] | Grid[bool] | Grid[int] | Grid[Vector]] | None = None, data_type: typing.Literal['BOOLEAN', 'FLOAT', 'DOUBLE', 'INT', 'INT64', 'MASK', 'VECTOR_FLOAT', 'VECTOR_DOUBLE', 'VECTOR_INT', 'POINTS', 'UNKNOWN'] | None = None) -> GeometryNodeStoreNamedGridOutputs:
    'Args:\n    data_type: Type of grid data Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeStoreNamedGrid',
        inputs={
            'volume': volume,
            'name': name,
            'grid': grid,
        },
        input_sockets={
            'volume': ('Volume', 'Volume', 0, None),
            'name': ('Name', 'Name', 1, ''),
            'grid': ('Grid', 'Grid', 2, None),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'volume': ('Volume', 'Volume', 0, 'AUTO'),
        },
        output_type=GeometryNodeStoreNamedGridOutputs,
        type_properties={'data_type': {'BOOLEAN': {'grid': 'BOOLEAN'}, 'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'VECTOR_FLOAT': {'grid': 'VECTOR'}}},
    )

class FunctionNodeInputStringOutputs(typing.NamedTuple):
    string: Socket[str]

def string_(*, string: str = '') -> FunctionNodeInputStringOutputs:
    return _node_function(
        'FunctionNodeInputString',
        inputs={
        },
        input_sockets={
        },
        properties={
            'string': string,
        },
        output_sockets={
            'string': ('String', 'String', 0, 'AUTO'),
        },
        output_type=FunctionNodeInputStringOutputs,
    )

class FunctionNodeStringLengthOutputs(typing.NamedTuple):
    length: Socket[int | Field[int] | Grid[int] | List[int]]

def string_length(*, string: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '') -> FunctionNodeStringLengthOutputs:
    return _node_function(
        'FunctionNodeStringLength',
        inputs={
            'string': string,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
        },
        properties={
        },
        output_sockets={
            'length': ('Length', 'Length', 0, 'AUTO'),
        },
        output_type=FunctionNodeStringLengthOutputs,
    )

class GeometryNodeStringToCurvesOutputs(typing.NamedTuple):
    curve_instances: Socket[Geometry]
    remainder: Socket[str]
    line: Socket[Field[int]]
    word: Socket[Field[int]]
    pivot_point: Socket[Field[Vector]]

def string_to_curves(*, string: str | Socket[str] = '', size: float | Socket[float] = 1.0, font: Font | Socket[Font] | None = None, align_x: Menu | Socket[Menu] = 'Left', align_y: Menu | Socket[Menu] = 'Top Baseline', pivot_point: Menu | Socket[Menu] = 'Midpoint', character_spacing: float | Socket[float] = 1.0, word_spacing: float | Socket[float] = 1.0, line_spacing: float | Socket[float] = 1.0, overflow: Menu | Socket[Menu] = 'Overflow', text_box_width: float | Socket[float] = 0.0, text_box_height: float | Socket[float] = 0.0) -> GeometryNodeStringToCurvesOutputs:
    return _node_function(
        'GeometryNodeStringToCurves',
        inputs={
            'string': string,
            'size': size,
            'font': font,
            'align_x': align_x,
            'align_y': align_y,
            'pivot_point': pivot_point,
            'character_spacing': character_spacing,
            'word_spacing': word_spacing,
            'line_spacing': line_spacing,
            'overflow': overflow,
            'text_box_width': text_box_width,
            'text_box_height': text_box_height,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
            'size': ('Size', 'Size', 1, 1.0),
            'font': ('Font', 'Font', 2, None),
            'align_x': ('Align X', 'Align X', 3, 'Left'),
            'align_y': ('Align Y', 'Align Y', 4, 'Top Baseline'),
            'pivot_point': ('Pivot Point', 'Pivot Point', 5, 'Midpoint'),
            'character_spacing': ('Character Spacing', 'Character Spacing', 6, 1.0),
            'word_spacing': ('Word Spacing', 'Word Spacing', 7, 1.0),
            'line_spacing': ('Line Spacing', 'Line Spacing', 8, 1.0),
            'overflow': ('Overflow', 'Overflow', 9, 'Overflow'),
            'text_box_width': ('Text Box Width', 'Text Box Width', 10, 0.0),
            'text_box_height': ('Text Box Height', 'Text Box Height', 11, 0.0),
        },
        properties={
        },
        output_sockets={
            'curve_instances': ('Curve Instances', 'Curve Instances', 0, 'AUTO'),
            'remainder': ('Remainder', 'Remainder', 1, 'AUTO'),
            'line': ('Line', 'Line', 2, 'FIELD'),
            'word': ('Word', 'Word', 3, 'FIELD'),
            'pivot_point': ('Pivot Point', 'Pivot Point', 4, 'FIELD'),
        },
        output_type=GeometryNodeStringToCurvesOutputs,
    )

class FunctionNodeStringToValueOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int]]
    length: Socket[int | Field[int] | Grid[int] | List[int]]

def string_to_value(*, string: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', base: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 10, data_type: typing.Literal['FLOAT', 'INT'] | None = None) -> FunctionNodeStringToValueOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'FunctionNodeStringToValue',
        inputs={
            'string': string,
            'base': base,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
            'base': ('Base', 'Base', 1, 10),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
            'length': ('Length', 'Length', 1, 'AUTO'),
        },
        output_type=FunctionNodeStringToValueOutputs,
        type_properties={'data_type': {'FLOAT': {}, 'INT': {}}},
    )

class GeometryNodeSubdivideCurveOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def subdivide_curve(*, curve: Geometry | Socket[Geometry] | None = None, cuts: int | Field[int] | Socket[int | Field[int]] = 1) -> GeometryNodeSubdivideCurveOutputs:
    return _node_function(
        'GeometryNodeSubdivideCurve',
        inputs={
            'curve': curve,
            'cuts': cuts,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'cuts': ('Cuts', 'Cuts', 1, 1),
        },
        properties={
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeSubdivideCurveOutputs,
    )

class GeometryNodeSubdivideMeshOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def subdivide_mesh(*, mesh: Geometry | Socket[Geometry] | None = None, level: int | Socket[int] = 1) -> GeometryNodeSubdivideMeshOutputs:
    return _node_function(
        'GeometryNodeSubdivideMesh',
        inputs={
            'mesh': mesh,
            'level': level,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'level': ('Level', 'Level', 1, 1),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeSubdivideMeshOutputs,
    )

class GeometryNodeSubdivisionSurfaceOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def subdivision_surface(*, mesh: Geometry | Socket[Geometry] | None = None, level: int | Socket[int] = 1, edge_crease: float | Field[float] | Socket[float | Field[float]] = 0.0, vertex_crease: float | Field[float] | Socket[float | Field[float]] = 0.0, limit_surface: bool | Socket[bool] = True, quality: int | Socket[int] = 3, uv_smooth: Menu | Socket[Menu] = 'Keep Boundaries', boundary_smooth: Menu | Socket[Menu] = 'All') -> GeometryNodeSubdivisionSurfaceOutputs:
    return _node_function(
        'GeometryNodeSubdivisionSurface',
        inputs={
            'mesh': mesh,
            'level': level,
            'edge_crease': edge_crease,
            'vertex_crease': vertex_crease,
            'limit_surface': limit_surface,
            'quality': quality,
            'uv_smooth': uv_smooth,
            'boundary_smooth': boundary_smooth,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'level': ('Level', 'Level', 1, 1),
            'edge_crease': ('Edge Crease', 'Edge Crease', 2, 0.0),
            'vertex_crease': ('Vertex Crease', 'Vertex Crease', 3, 0.0),
            'limit_surface': ('Limit Surface', 'Limit Surface', 4, True),
            'quality': ('Quality', 'Quality', 5, 3),
            'uv_smooth': ('UV Smooth', 'UV Smooth', 6, 'Keep Boundaries'),
            'boundary_smooth': ('Boundary Smooth', 'Boundary Smooth', 7, 'All'),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeSubdivisionSurfaceOutputs,
    )

class GeometryNodeSwitchOutputs(typing.NamedTuple):
    output: Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound]

def switch(*, switch: bool | Field[bool] | Grid[bool] | List[bool] | Socket[bool | Field[bool] | Grid[bool] | List[bool]] = False, false: float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound | Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound] = 0.0, true: float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound | Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | bool | Field[bool] | Grid[bool] | List[bool] | Vector | Field[Vector] | Grid[Vector] | List[Vector] | Color | Field[Color] | Grid[Color] | List[Color] | Rotation | Field[Rotation] | Grid[Rotation] | List[Rotation] | Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | str | Field[str] | Grid[str] | List[str] | Menu | Object | Image | Geometry | Collection | Material | Bundle | Closure | Font | Sound] = 0.0, input_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeSwitchOutputs:
    'Args:\n    input_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeSwitch',
        inputs={
            'switch': switch,
            'false': false,
            'true': true,
        },
        input_sockets={
            'switch': ('Switch', 'Switch', 0, False),
            'false': ('False', 'False', 1, 0.0),
            'true': ('True', 'True', 2, 0.0),
        },
        properties={
            'input_type': input_type,
        },
        output_sockets={
            'output': ('Output', 'Output', 0, 'AUTO'),
        },
        output_type=GeometryNodeSwitchOutputs,
        type_properties={'input_type': {'FLOAT': {'false': 'VALUE', 'true': 'VALUE'}, 'INT': {'false': 'INT', 'true': 'INT'}, 'BOOLEAN': {'false': 'BOOLEAN', 'true': 'BOOLEAN'}, 'VECTOR': {'false': 'VECTOR', 'true': 'VECTOR'}, 'RGBA': {'false': 'RGBA', 'true': 'RGBA'}, 'ROTATION': {'false': 'ROTATION', 'true': 'ROTATION'}, 'MATRIX': {'false': 'MATRIX', 'true': 'MATRIX'}, 'STRING': {'false': 'STRING', 'true': 'STRING'}, 'MENU': {'false': 'MENU', 'true': 'MENU'}, 'OBJECT': {'false': 'OBJECT', 'true': 'OBJECT'}, 'IMAGE': {'false': 'IMAGE', 'true': 'IMAGE'}, 'GEOMETRY': {'false': 'GEOMETRY', 'true': 'GEOMETRY'}, 'COLLECTION': {'false': 'COLLECTION', 'true': 'COLLECTION'}, 'MATERIAL': {'false': 'MATERIAL', 'true': 'MATERIAL'}, 'BUNDLE': {'false': 'BUNDLE', 'true': 'BUNDLE'}, 'CLOSURE': {'false': 'CLOSURE', 'true': 'CLOSURE'}, 'FONT': {'false': 'FONT', 'true': 'FONT'}, 'SOUND': {'false': 'SOUND', 'true': 'SOUND'}}},
    )

class GeometryNodeTagFilterOutputs(typing.NamedTuple):
    match: Socket[bool]

def tag_filter(*, tag_filter: str | Socket[str] = '', tags: List[str] | Socket[List[str]] | None = None) -> GeometryNodeTagFilterOutputs:
    return _node_function(
        'GeometryNodeTagFilter',
        inputs={
            'tag_filter': tag_filter,
            'tags': tags,
        },
        input_sockets={
            'tag_filter': ('Tag Filter', 'Tag Filter', 0, ''),
            'tags': ('Tags', 'Tags', 1, None),
        },
        properties={
        },
        output_sockets={
            'match': ('Match', 'Match', 0, 'AUTO'),
        },
        output_type=GeometryNodeTagFilterOutputs,
    )

class GeometryNodeTransferAttributesOutputs(typing.NamedTuple):
    target: Socket[Geometry]
    transferred_names: Socket[List[str]]

def transfer_attributes(*, target: Geometry | Socket[Geometry] | None = None, target_point_id: int | Field[int] | Socket[int | Field[int]] = 0, target_edge_id: int | Field[int] | Socket[int | Field[int]] = 0, target_face_id: int | Field[int] | Socket[int | Field[int]] = 0, target_corner_id: int | Field[int] | Socket[int | Field[int]] = 0, target_curve_id: int | Field[int] | Socket[int | Field[int]] = 0, target_instance_id: int | Field[int] | Socket[int | Field[int]] = 0, source: Geometry | Socket[Geometry] | None = None, source_point_id: int | Field[int] | Socket[int | Field[int]] = 0, source_edge_id: int | Field[int] | Socket[int | Field[int]] = 0, source_face_id: int | Field[int] | Socket[int | Field[int]] = 0, source_corner_id: int | Field[int] | Socket[int | Field[int]] = 0, source_curve_id: int | Field[int] | Socket[int | Field[int]] = 0, source_instance_id: int | Field[int] | Socket[int | Field[int]] = 0, pattern_mode: Menu | Socket[Menu] = 'Wildcard', attribute_names: List[str] | Socket[List[str]] | None = None, exclude_names: bool | Socket[bool] = False) -> GeometryNodeTransferAttributesOutputs:
    return _node_function(
        'GeometryNodeTransferAttributes',
        inputs={
            'target': target,
            'target_point_id': target_point_id,
            'target_edge_id': target_edge_id,
            'target_face_id': target_face_id,
            'target_corner_id': target_corner_id,
            'target_curve_id': target_curve_id,
            'target_instance_id': target_instance_id,
            'source': source,
            'source_point_id': source_point_id,
            'source_edge_id': source_edge_id,
            'source_face_id': source_face_id,
            'source_corner_id': source_corner_id,
            'source_curve_id': source_curve_id,
            'source_instance_id': source_instance_id,
            'pattern_mode': pattern_mode,
            'attribute_names': attribute_names,
            'exclude_names': exclude_names,
        },
        input_sockets={
            'target': ('Target', 'Target', 0, None),
            'target_point_id': ('Target Point ID', 'Target Point ID', 1, 0),
            'target_edge_id': ('Target Edge ID', 'Target Edge ID', 2, 0),
            'target_face_id': ('Target Face ID', 'Target Face ID', 3, 0),
            'target_corner_id': ('Target Corner ID', 'Target Corner ID', 4, 0),
            'target_curve_id': ('Target Curve ID', 'Target Curve ID', 5, 0),
            'target_instance_id': ('Target Instance ID', 'Target Instance ID', 6, 0),
            'source': ('Source', 'Source', 7, None),
            'source_point_id': ('Source Point ID', 'Source Point ID', 8, 0),
            'source_edge_id': ('Source Edge ID', 'Source Edge ID', 9, 0),
            'source_face_id': ('Source Face ID', 'Source Face ID', 10, 0),
            'source_corner_id': ('Source Corner ID', 'Source Corner ID', 11, 0),
            'source_curve_id': ('Source Curve ID', 'Source Curve ID', 12, 0),
            'source_instance_id': ('Source Instance ID', 'Source Instance ID', 13, 0),
            'pattern_mode': ('Pattern Mode', 'Pattern Mode', 14, 'Wildcard'),
            'attribute_names': ('Attribute Names', 'Attribute Names', 15, None),
            'exclude_names': ('Exclude Names', 'Exclude Names', 16, False),
        },
        properties={
        },
        output_sockets={
            'target': ('Target', 'Target', 0, 'AUTO'),
            'transferred_names': ('Transferred Names', 'Transferred Names', 1, 'LIST'),
        },
        output_type=GeometryNodeTransferAttributesOutputs,
    )

class FunctionNodeTransformDirectionOutputs(typing.NamedTuple):
    direction: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def transform_direction(*, direction: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), transform: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None) -> FunctionNodeTransformDirectionOutputs:
    return _node_function(
        'FunctionNodeTransformDirection',
        inputs={
            'direction': direction,
            'transform': transform,
        },
        input_sockets={
            'direction': ('Direction', 'Direction', 0, (0.0, 0.0, 0.0)),
            'transform': ('Transform', 'Transform', 1, None),
        },
        properties={
        },
        output_sockets={
            'direction': ('Direction', 'Direction', 0, 'AUTO'),
        },
        output_type=FunctionNodeTransformDirectionOutputs,
    )

class GeometryNodeTransformOutputs(typing.NamedTuple):
    geometry: Socket[Geometry]

def transform_geometry(*, geometry: Geometry | Socket[Geometry] | None = None, mode: Menu | Socket[Menu] = 'Components', translation: Vector | Socket[Vector] = (0.0, 0.0, 0.0), rotation: Rotation | Socket[Rotation] = (0.0, 0.0, 0.0), scale: Vector | Socket[Vector] = (1.0, 1.0, 1.0), transform: Matrix | Socket[Matrix] | None = None) -> GeometryNodeTransformOutputs:
    return _node_function(
        'GeometryNodeTransform',
        inputs={
            'geometry': geometry,
            'mode': mode,
            'translation': translation,
            'rotation': rotation,
            'scale': scale,
            'transform': transform,
        },
        input_sockets={
            'geometry': ('Geometry', 'Geometry', 0, None),
            'mode': ('Mode', 'Mode', 1, 'Components'),
            'translation': ('Translation', 'Translation', 2, (0.0, 0.0, 0.0)),
            'rotation': ('Rotation', 'Rotation', 3, (0.0, 0.0, 0.0)),
            'scale': ('Scale', 'Scale', 4, (1.0, 1.0, 1.0)),
            'transform': ('Transform', 'Transform', 5, None),
        },
        properties={
        },
        output_sockets={
            'geometry': ('Geometry', 'Geometry', 0, 'AUTO'),
        },
        output_type=GeometryNodeTransformOutputs,
    )

class GeometryNodeGizmoTransformOutputs(typing.NamedTuple):
    transform: Socket[Geometry]

def transform_gizmo(*, value: typing.Sequence[Matrix | Socket[Matrix]] = (), position: Vector | Socket[Vector] = (0.0, 0.0, 0.0), rotation: Rotation | Socket[Rotation] = (0.0, 0.0, 0.0), use_translation_x: bool = True, use_translation_y: bool = True, use_translation_z: bool = True, use_rotation_x: bool = True, use_rotation_y: bool = True, use_rotation_z: bool = True, use_scale_x: bool = True, use_scale_y: bool = True, use_scale_z: bool = True) -> GeometryNodeGizmoTransformOutputs:
    return _node_function(
        'GeometryNodeGizmoTransform',
        inputs={
            'value': value,
            'position': position,
            'rotation': rotation,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, ()),
            'position': ('Position', 'Position', 1, (0.0, 0.0, 0.0)),
            'rotation': ('Rotation', 'Rotation', 2, (0.0, 0.0, 0.0)),
        },
        properties={
            'use_translation_x': use_translation_x,
            'use_translation_y': use_translation_y,
            'use_translation_z': use_translation_z,
            'use_rotation_x': use_rotation_x,
            'use_rotation_y': use_rotation_y,
            'use_rotation_z': use_rotation_z,
            'use_scale_x': use_scale_x,
            'use_scale_y': use_scale_y,
            'use_scale_z': use_scale_z,
        },
        output_sockets={
            'transform': ('Transform', 'Transform', 0, 'AUTO'),
        },
        output_type=GeometryNodeGizmoTransformOutputs,
    )

class FunctionNodeTransformPointOutputs(typing.NamedTuple):
    vector: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def transform_point(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), transform: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None) -> FunctionNodeTransformPointOutputs:
    return _node_function(
        'FunctionNodeTransformPoint',
        inputs={
            'vector': vector,
            'transform': transform,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'transform': ('Transform', 'Transform', 1, None),
        },
        properties={
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
        },
        output_type=FunctionNodeTransformPointOutputs,
    )

class GeometryNodeTranslateInstancesOutputs(typing.NamedTuple):
    instances: Socket[Geometry]

def translate_instances(*, instances: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, translation: Vector | Field[Vector] | Socket[Vector | Field[Vector]] = (0.0, 0.0, 0.0), local_space: bool | Field[bool] | Socket[bool | Field[bool]] = True) -> GeometryNodeTranslateInstancesOutputs:
    return _node_function(
        'GeometryNodeTranslateInstances',
        inputs={
            'instances': instances,
            'selection': selection,
            'translation': translation,
            'local_space': local_space,
        },
        input_sockets={
            'instances': ('Instances', 'Instances', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'translation': ('Translation', 'Translation', 2, (0.0, 0.0, 0.0)),
            'local_space': ('Local Space', 'Local Space', 3, True),
        },
        properties={
        },
        output_sockets={
            'instances': ('Instances', 'Instances', 0, 'AUTO'),
        },
        output_type=GeometryNodeTranslateInstancesOutputs,
    )

class FunctionNodeTransposeMatrixOutputs(typing.NamedTuple):
    matrix: Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]]

def transpose_matrix(*, matrix: Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix] | Socket[Matrix | Field[Matrix] | Grid[Matrix] | List[Matrix]] | None = None) -> FunctionNodeTransposeMatrixOutputs:
    return _node_function(
        'FunctionNodeTransposeMatrix',
        inputs={
            'matrix': matrix,
        },
        input_sockets={
            'matrix': ('Matrix', 'Matrix', 0, None),
        },
        properties={
        },
        output_sockets={
            'matrix': ('Matrix', 'Matrix', 0, 'AUTO'),
        },
        output_type=FunctionNodeTransposeMatrixOutputs,
    )

class GeometryNodeTriangulateOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def triangulate(*, mesh: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, quad_method: Menu | Socket[Menu] = 'Shortest Diagonal', n_gon_method: Menu | Socket[Menu] = 'Beauty') -> GeometryNodeTriangulateOutputs:
    return _node_function(
        'GeometryNodeTriangulate',
        inputs={
            'mesh': mesh,
            'selection': selection,
            'quad_method': quad_method,
            'n_gon_method': n_gon_method,
        },
        input_sockets={
            'mesh': ('Mesh', 'Mesh', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'quad_method': ('Quad Method', 'Quad Method', 2, 'Shortest Diagonal'),
            'n_gon_method': ('N-gon Method', 'N-gon Method', 3, 'Beauty'),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeTriangulateOutputs,
    )

class GeometryNodeTrimCurveOutputs(typing.NamedTuple):
    curve: Socket[Geometry]

def trim_curve(*, curve: Geometry | Socket[Geometry] | None = None, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, start: float | Field[float] | Socket[float | Field[float]] = 0.0, end: float | Field[float] | Socket[float | Field[float]] = 1.0, mode: typing.Literal['FACTOR', 'LENGTH'] = 'FACTOR') -> GeometryNodeTrimCurveOutputs:
    'Args:\n    mode: How to find endpoint positions for the trimmed spline'
    return _node_function(
        'GeometryNodeTrimCurve',
        inputs={
            'curve': curve,
            'selection': selection,
            'start': start,
            'end': end,
        },
        input_sockets={
            'curve': ('Curve', 'Curve', 0, None),
            'selection': ('Selection', 'Selection', 1, True),
            'start': ('Start', 'Start', 2, 0.0),
            'end': ('End', 'End', 3, 1.0),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'curve': ('Curve', 'Curve', 0, 'AUTO'),
        },
        output_type=GeometryNodeTrimCurveOutputs,
    )

class FunctionNodeTrimStringOutputs(typing.NamedTuple):
    string: Socket[str | Field[str] | Grid[str] | List[str]]

def trim_string(*, string: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', characters: str | Field[str] | Grid[str] | List[str] | Socket[str | Field[str] | Grid[str] | List[str]] = '', whitespace: bool | Field[bool] | Grid[bool] | List[bool] | Socket[bool | Field[bool] | Grid[bool] | List[bool]] = True, start: bool | Field[bool] | Grid[bool] | List[bool] | Socket[bool | Field[bool] | Grid[bool] | List[bool]] = True, end: bool | Field[bool] | Grid[bool] | List[bool] | Socket[bool | Field[bool] | Grid[bool] | List[bool]] = True) -> FunctionNodeTrimStringOutputs:
    return _node_function(
        'FunctionNodeTrimString',
        inputs={
            'string': string,
            'characters': characters,
            'whitespace': whitespace,
            'start': start,
            'end': end,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
            'characters': ('Characters', 'Characters', 1, ''),
            'whitespace': ('Whitespace', 'Whitespace', 2, True),
            'start': ('Start', 'Start', 3, True),
            'end': ('End', 'End', 4, True),
        },
        properties={
        },
        output_sockets={
            'string': ('String', 'String', 0, 'AUTO'),
        },
        output_type=FunctionNodeTrimStringOutputs,
    )

class GeometryNodeMeshUVSphereOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]
    uv_map: Socket[Field[Vector]]

def uv_sphere(*, segments: int | Socket[int] = 32, rings: int | Socket[int] = 16, radius: float | Socket[float] = 1.0) -> GeometryNodeMeshUVSphereOutputs:
    return _node_function(
        'GeometryNodeMeshUVSphere',
        inputs={
            'segments': segments,
            'rings': rings,
            'radius': radius,
        },
        input_sockets={
            'segments': ('Segments', 'Segments', 0, 32),
            'rings': ('Rings', 'Rings', 1, 16),
            'radius': ('Radius', 'Radius', 2, 1.0),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
            'uv_map': ('UV Map', 'UV Map', 1, 'FIELD'),
        },
        output_type=GeometryNodeMeshUVSphereOutputs,
    )

class GeometryNodeUVTangentOutputs(typing.NamedTuple):
    tangent: Socket[Field[Vector]]

def uv_tangent(*, method: Menu | Socket[Menu] = 'Exact', uv: Vector2 | Field[Vector2] | Socket[Vector2 | Field[Vector2]] = (0.0, 0.0)) -> GeometryNodeUVTangentOutputs:
    return _node_function(
        'GeometryNodeUVTangent',
        inputs={
            'method': method,
            'uv': uv,
        },
        input_sockets={
            'method': ('Method', 'Method', 0, 'Exact'),
            'uv': ('UV', 'UV', 1, (0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'tangent': ('Tangent', 'Tangent', 0, 'FIELD'),
        },
        output_type=GeometryNodeUVTangentOutputs,
    )

class GeometryNodeUVUnwrapOutputs(typing.NamedTuple):
    uv: Socket[Field[Vector]]

def uv_unwrap(*, selection: bool | Field[bool] | Socket[bool | Field[bool]] = True, seam: bool | Field[bool] | Socket[bool | Field[bool]] = False, margin: float | Socket[float] = 0.0010000000474974513, fill_holes: bool | Socket[bool] = True, method: Menu | Socket[Menu] = 'Angle Based', iterations: int | Socket[int] = 10, no_flip: bool | Socket[bool] = False) -> GeometryNodeUVUnwrapOutputs:
    return _node_function(
        'GeometryNodeUVUnwrap',
        inputs={
            'selection': selection,
            'seam': seam,
            'margin': margin,
            'fill_holes': fill_holes,
            'method': method,
            'iterations': iterations,
            'no_flip': no_flip,
        },
        input_sockets={
            'selection': ('Selection', 'Selection', 0, True),
            'seam': ('Seam', 'Seam', 1, False),
            'margin': ('Margin', 'Margin', 2, 0.0010000000474974513),
            'fill_holes': ('Fill Holes', 'Fill Holes', 3, True),
            'method': ('Method', 'Method', 4, 'Angle Based'),
            'iterations': ('Iterations', 'Iterations', 5, 10),
            'no_flip': ('No Flip', 'No Flip', 6, False),
        },
        properties={
        },
        output_sockets={
            'uv': ('UV', 'UV', 0, 'FIELD'),
        },
        output_type=GeometryNodeUVUnwrapOutputs,
    )

class ShaderNodeValueOutputs(typing.NamedTuple):
    value: Socket[float]

def value() -> ShaderNodeValueOutputs:
    return _node_function(
        'ShaderNodeValue',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=ShaderNodeValueOutputs,
    )

class FunctionNodeValueToStringOutputs(typing.NamedTuple):
    string: Socket[str | Field[str] | Grid[str] | List[str]]

def value_to_string(*, value: float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int] | Socket[float | Field[float] | Grid[float] | List[float] | int | Field[int] | Grid[int] | List[int]] = 0.0, decimals: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, base: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 10, padding: int | Field[int] | Grid[int] | List[int] | Socket[int | Field[int] | Grid[int] | List[int]] = 0, data_type: typing.Literal['FLOAT', 'INT'] | None = None) -> FunctionNodeValueToStringOutputs:
    'Args:\n    data_type:  Inferred from the linked inputs when None.'
    return _node_function(
        'FunctionNodeValueToString',
        inputs={
            'value': value,
            'decimals': decimals,
            'base': base,
            'padding': padding,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0.0),
            'decimals': ('Decimals', 'Decimals', 1, 0),
            'base': ('Base', 'Base', 2, 10),
            'padding': ('Padding', 'Padding', 3, 0),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'string': ('String', 'String', 0, 'AUTO'),
        },
        output_type=FunctionNodeValueToStringOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}}},
    )

class FunctionNodeInputVectorOutputs(typing.NamedTuple):
    vector: Socket[Vector]

def vector(*, vector: Vector4 = (0.0, 0.0, 0.0), vector_dimensions: int = 3) -> FunctionNodeInputVectorOutputs:
    'Args:\n    vector_dimensions: Dimensions of the vector socket'
    return _node_function(
        'FunctionNodeInputVector',
        inputs={
        },
        input_sockets={
        },
        properties={
            'vector': vector,
            'vector_dimensions': vector_dimensions,
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
        },
        output_type=FunctionNodeInputVectorOutputs,
    )

class ShaderNodeVectorCurveOutputs(typing.NamedTuple):
    vector: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def vector_curves(*, factor: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0)) -> ShaderNodeVectorCurveOutputs:
    return _node_function(
        'ShaderNodeVectorCurve',
        inputs={
            'factor': factor,
            'vector': vector,
        },
        input_sockets={
            'factor': ('Fac', 'Factor', 0, 1.0),
            'vector': ('Vector', 'Vector', 1, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
        },
        output_type=ShaderNodeVectorCurveOutputs,
    )

class ShaderNodeVectorMathOutputs(typing.NamedTuple):
    vector: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    value: Socket[float | Field[float] | Grid[float] | List[float]]

def vector_math(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), vector_2: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), vector_3: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), scale: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, operation: typing.Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'ROUND', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'] = 'ADD') -> ShaderNodeVectorMathOutputs:
    return _node_function(
        'ShaderNodeVectorMath',
        inputs={
            'vector': vector,
            'vector_2': vector_2,
            'vector_3': vector_3,
            'scale': scale,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'vector_2': ('Vector_001', 'Vector', 1, (0.0, 0.0, 0.0)),
            'vector_3': ('Vector_002', 'Vector', 2, (0.0, 0.0, 0.0)),
            'scale': ('Scale', 'Scale', 3, 1.0),
        },
        properties={
            'operation': operation,
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
            'value': ('Value', 'Value', 1, 'AUTO'),
        },
        output_type=ShaderNodeVectorMathOutputs,
    )

class ShaderNodeVectorRotateOutputs(typing.NamedTuple):
    vector: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]

def vector_rotate(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), center: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), axis: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 1.0), angle: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, rotation: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), rotation_type: typing.Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE', invert: bool = False) -> ShaderNodeVectorRotateOutputs:
    'Args:\n    rotation_type: Type of angle input\n    invert: Invert the rotation angle'
    return _node_function(
        'ShaderNodeVectorRotate',
        inputs={
            'vector': vector,
            'center': center,
            'axis': axis,
            'angle': angle,
            'rotation': rotation,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'center': ('Center', 'Center', 1, (0.0, 0.0, 0.0)),
            'axis': ('Axis', 'Axis', 2, (0.0, 0.0, 1.0)),
            'angle': ('Angle', 'Angle', 3, 0.0),
            'rotation': ('Rotation', 'Rotation', 4, (0.0, 0.0, 0.0)),
        },
        properties={
            'rotation_type': rotation_type,
            'invert': invert,
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
        },
        output_type=ShaderNodeVectorRotateOutputs,
    )

class GeometryNodeInputMeshVertexNeighborsOutputs(typing.NamedTuple):
    vertex_count: Socket[Field[int]]
    face_count: Socket[Field[int]]

def vertex_neighbors() -> GeometryNodeInputMeshVertexNeighborsOutputs:
    return _node_function(
        'GeometryNodeInputMeshVertexNeighbors',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'vertex_count': ('Vertex Count', 'Vertex Count', 0, 'FIELD'),
            'face_count': ('Face Count', 'Face Count', 1, 'FIELD'),
        },
        output_type=GeometryNodeInputMeshVertexNeighborsOutputs,
    )

class GeometryNodeVertexOfCornerOutputs(typing.NamedTuple):
    vertex_index: Socket[Field[int]]

def vertex_of_corner(*, corner_index: int | Field[int] | Socket[int | Field[int]] = 0) -> GeometryNodeVertexOfCornerOutputs:
    return _node_function(
        'GeometryNodeVertexOfCorner',
        inputs={
            'corner_index': corner_index,
        },
        input_sockets={
            'corner_index': ('Corner Index', 'Corner Index', 0, 0),
        },
        properties={
        },
        output_sockets={
            'vertex_index': ('Vertex Index', 'Vertex Index', 0, 'FIELD'),
        },
        output_type=GeometryNodeVertexOfCornerOutputs,
    )

def viewer(*, domain: typing.Literal['AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'AUTO', **items: typing.Any) -> None:
    'Args:\n    domain: Domain to evaluate fields on\n    items: Items to add, by name; each socket type is inferred from its value.'
    return _node_function(
        'GeometryNodeViewer',
        inputs={
        },
        input_sockets={
        },
        properties={
            'domain': domain,
        },
        output_sockets={
        },
        output_type=None,
        item_collections=(
            ('viewer_items', 'values', items),
        ),
    )

class GeometryNodeViewportTransformOutputs(typing.NamedTuple):
    projection: Socket[Matrix]
    view: Socket[Matrix]
    is_orthographic: Socket[bool]

def viewport_transform() -> GeometryNodeViewportTransformOutputs:
    return _node_function(
        'GeometryNodeViewportTransform',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'projection': ('Projection', 'Projection', 0, 'AUTO'),
            'view': ('View', 'View', 1, 'AUTO'),
            'is_orthographic': ('Is Orthographic', 'Is Orthographic', 2, 'AUTO'),
        },
        output_type=GeometryNodeViewportTransformOutputs,
    )

class GeometryNodeVolumeCubeOutputs(typing.NamedTuple):
    volume: Socket[Geometry]

def volume_cube(*, density: float | Field[float] | Socket[float | Field[float]] = 1.0, background: float | Socket[float] = 0.0, min: Vector | Socket[Vector] = (-1.0, -1.0, -1.0), max: Vector | Socket[Vector] = (1.0, 1.0, 1.0), resolution_x: int | Socket[int] = 32, resolution_y: int | Socket[int] = 32, resolution_z: int | Socket[int] = 32) -> GeometryNodeVolumeCubeOutputs:
    return _node_function(
        'GeometryNodeVolumeCube',
        inputs={
            'density': density,
            'background': background,
            'min': min,
            'max': max,
            'resolution_x': resolution_x,
            'resolution_y': resolution_y,
            'resolution_z': resolution_z,
        },
        input_sockets={
            'density': ('Density', 'Density', 0, 1.0),
            'background': ('Background', 'Background', 1, 0.0),
            'min': ('Min', 'Min', 2, (-1.0, -1.0, -1.0)),
            'max': ('Max', 'Max', 3, (1.0, 1.0, 1.0)),
            'resolution_x': ('Resolution X', 'Resolution X', 4, 32),
            'resolution_y': ('Resolution Y', 'Resolution Y', 5, 32),
            'resolution_z': ('Resolution Z', 'Resolution Z', 6, 32),
        },
        properties={
        },
        output_sockets={
            'volume': ('Volume', 'Volume', 0, 'AUTO'),
        },
        output_type=GeometryNodeVolumeCubeOutputs,
    )

class GeometryNodeVolumeToMeshOutputs(typing.NamedTuple):
    mesh: Socket[Geometry]

def volume_to_mesh(*, volume: Geometry | Socket[Geometry] | None = None, resolution_mode: Menu | Socket[Menu] = 'Grid', voxel_size: float | Socket[float] = 0.30000001192092896, voxel_amount: float | Socket[float] = 64.0, threshold: float | Socket[float] = 0.10000000149011612, adaptivity: float | Socket[float] = 0.0) -> GeometryNodeVolumeToMeshOutputs:
    return _node_function(
        'GeometryNodeVolumeToMesh',
        inputs={
            'volume': volume,
            'resolution_mode': resolution_mode,
            'voxel_size': voxel_size,
            'voxel_amount': voxel_amount,
            'threshold': threshold,
            'adaptivity': adaptivity,
        },
        input_sockets={
            'volume': ('Volume', 'Volume', 0, None),
            'resolution_mode': ('Resolution Mode', 'Resolution Mode', 1, 'Grid'),
            'voxel_size': ('Voxel Size', 'Voxel Size', 2, 0.30000001192092896),
            'voxel_amount': ('Voxel Amount', 'Voxel Amount', 3, 64.0),
            'threshold': ('Threshold', 'Threshold', 4, 0.10000000149011612),
            'adaptivity': ('Adaptivity', 'Adaptivity', 5, 0.0),
        },
        properties={
        },
        output_sockets={
            'mesh': ('Mesh', 'Mesh', 0, 'AUTO'),
        },
        output_type=GeometryNodeVolumeToMeshOutputs,
    )

class ShaderNodeTexVoronoiOutputs(typing.NamedTuple):
    distance: Socket[float | Field[float] | Grid[float] | List[float]]
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]
    position: Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]]
    w: Socket[float | Field[float] | Grid[float] | List[float]]
    radius: Socket[float | Field[float] | Grid[float] | List[float]]

def voronoi_texture(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), scale: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 5.0, detail: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, roughness: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5, lacunarity: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 2.0, randomness: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, w: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, smoothness: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, exponent: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5, voronoi_dimensions: typing.Literal['1D', '2D', '3D', '4D'] = '3D', distance: typing.Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN', feature: typing.Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1', normalize: bool = False) -> ShaderNodeTexVoronoiOutputs:
    'Args:\n    voronoi_dimensions: Number of dimensions to output noise for\n    distance: The distance metric used to compute the texture\n    feature: The Voronoi feature that the node will compute\n    normalize: Normalize output Distance to 0.0 to 1.0 range'
    return _node_function(
        'ShaderNodeTexVoronoi',
        inputs={
            'vector': vector,
            'scale': scale,
            'detail': detail,
            'roughness': roughness,
            'lacunarity': lacunarity,
            'randomness': randomness,
            'w': w,
            'smoothness': smoothness,
            'exponent': exponent,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'scale': ('Scale', 'Scale', 2, 5.0),
            'detail': ('Detail', 'Detail', 3, 0.0),
            'roughness': ('Roughness', 'Roughness', 4, 0.5),
            'lacunarity': ('Lacunarity', 'Lacunarity', 5, 2.0),
            'randomness': ('Randomness', 'Randomness', 8, 1.0),
            'w': ('W', 'W', 1, 0.0),
            'smoothness': ('Smoothness', 'Smoothness', 6, 1.0),
            'exponent': ('Exponent', 'Exponent', 7, 0.5),
        },
        properties={
            'voronoi_dimensions': voronoi_dimensions,
            'distance': distance,
            'feature': feature,
            'normalize': normalize,
        },
        output_sockets={
            'distance': ('Distance', 'Distance', 0, 'FIELD'),
            'color': ('Color', 'Color', 1, 'FIELD'),
            'position': ('Position', 'Position', 2, 'FIELD'),
            'w': ('W', 'W', 3, 'AUTO'),
            'radius': ('Radius', 'Radius', 4, 'AUTO'),
        },
        output_type=ShaderNodeTexVoronoiOutputs,
    )

class GeometryNodeInputVoxelIndexOutputs(typing.NamedTuple):
    x: Socket[Field[int]]
    y: Socket[Field[int]]
    z: Socket[Field[int]]
    is_tile: Socket[Field[bool]]
    extent_x: Socket[Field[int]]
    extent_y: Socket[Field[int]]
    extent_z: Socket[Field[int]]

def voxel_index() -> GeometryNodeInputVoxelIndexOutputs:
    return _node_function(
        'GeometryNodeInputVoxelIndex',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'x': ('X', 'X', 0, 'FIELD'),
            'y': ('Y', 'Y', 1, 'FIELD'),
            'z': ('Z', 'Z', 2, 'FIELD'),
            'is_tile': ('Is Tile', 'Is Tile', 3, 'FIELD'),
            'extent_x': ('Extent X', 'Extent X', 4, 'FIELD'),
            'extent_y': ('Extent Y', 'Extent Y', 5, 'FIELD'),
            'extent_z': ('Extent Z', 'Extent Z', 6, 'FIELD'),
        },
        output_type=GeometryNodeInputVoxelIndexOutputs,
    )

class GeometryNodeGridVoxelizeOutputs(typing.NamedTuple):
    grid: Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]]

def voxelize_grid(*, grid: Grid[float] | Grid[int] | Grid[bool] | Grid[Vector] | Socket[Grid[float] | Grid[int] | Grid[bool] | Grid[Vector]] | None = None, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeGridVoxelizeOutputs:
    'Args:\n    data_type: Node socket data type Inferred from the linked inputs when None.'
    return _node_function(
        'GeometryNodeGridVoxelize',
        inputs={
            'grid': grid,
        },
        input_sockets={
            'grid': ('Grid', 'Grid', 0, None),
        },
        properties={
            'data_type': data_type,
        },
        output_sockets={
            'grid': ('Grid', 'Grid', 0, 'GRID'),
        },
        output_type=GeometryNodeGridVoxelizeOutputs,
        type_properties={'data_type': {'FLOAT': {'grid': 'VALUE'}, 'INT': {'grid': 'INT'}, 'BOOLEAN': {'grid': 'BOOLEAN'}, 'VECTOR': {'grid': 'VECTOR'}}},
    )

class GeometryNodeWarningOutputs(typing.NamedTuple):
    show: Socket[bool]

def warning(*, show: bool | Socket[bool] = True, message: str | Socket[str] = '', warning_type: typing.Literal['ERROR', 'WARNING', 'INFO'] = 'ERROR') -> GeometryNodeWarningOutputs:
    return _node_function(
        'GeometryNodeWarning',
        inputs={
            'show': show,
            'message': message,
        },
        input_sockets={
            'show': ('Show', 'Show', 0, True),
            'message': ('Message', 'Message', 1, ''),
        },
        properties={
            'warning_type': warning_type,
        },
        output_sockets={
            'show': ('Show', 'Show', 0, 'AUTO'),
        },
        output_type=GeometryNodeWarningOutputs,
    )

class ShaderNodeTexWaveOutputs(typing.NamedTuple):
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]
    factor: Socket[float | Field[float] | Grid[float] | List[float]]

def wave_texture(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), scale: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 5.0, distortion: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, detail: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 2.0, detail_scale: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 1.0, detail_roughness: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.5, phase_offset: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, wave_type: typing.Literal['BANDS', 'RINGS'] = 'BANDS', bands_direction: typing.Literal['X', 'Y', 'Z', 'DIAGONAL'] = 'X', rings_direction: typing.Literal['X', 'Y', 'Z', 'SPHERICAL'] = 'X', wave_profile: typing.Literal['SIN', 'SAW', 'TRI'] = 'SIN') -> ShaderNodeTexWaveOutputs:
    return _node_function(
        'ShaderNodeTexWave',
        inputs={
            'vector': vector,
            'scale': scale,
            'distortion': distortion,
            'detail': detail,
            'detail_scale': detail_scale,
            'detail_roughness': detail_roughness,
            'phase_offset': phase_offset,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'scale': ('Scale', 'Scale', 1, 5.0),
            'distortion': ('Distortion', 'Distortion', 2, 0.0),
            'detail': ('Detail', 'Detail', 3, 2.0),
            'detail_scale': ('Detail Scale', 'Detail Scale', 4, 1.0),
            'detail_roughness': ('Detail Roughness', 'Detail Roughness', 5, 0.5),
            'phase_offset': ('Phase Offset', 'Phase Offset', 6, 0.0),
        },
        properties={
            'wave_type': wave_type,
            'bands_direction': bands_direction,
            'rings_direction': rings_direction,
            'wave_profile': wave_profile,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'FIELD'),
            'factor': ('Fac', 'Factor', 1, 'FIELD'),
        },
        output_type=ShaderNodeTexWaveOutputs,
    )

class ShaderNodeTexWhiteNoiseOutputs(typing.NamedTuple):
    value: Socket[float | Field[float] | Grid[float] | List[float]]
    color: Socket[Color | Field[Color] | Grid[Color] | List[Color]]

def white_noise_texture(*, vector: Vector | Field[Vector] | Grid[Vector] | List[Vector] | Socket[Vector | Field[Vector] | Grid[Vector] | List[Vector]] = (0.0, 0.0, 0.0), w: float | Field[float] | Grid[float] | List[float] | Socket[float | Field[float] | Grid[float] | List[float]] = 0.0, noise_dimensions: typing.Literal['1D', '2D', '3D', '4D'] = '3D') -> ShaderNodeTexWhiteNoiseOutputs:
    'Args:\n    noise_dimensions: Number of dimensions to output noise for'
    return _node_function(
        'ShaderNodeTexWhiteNoise',
        inputs={
            'vector': vector,
            'w': w,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'w': ('W', 'W', 1, 0.0),
        },
        properties={
            'noise_dimensions': noise_dimensions,
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'FIELD'),
            'color': ('Color', 'Color', 1, 'FIELD'),
        },
        output_type=ShaderNodeTexWhiteNoiseOutputs,
    )

class GeometryNodeXPBDSolverOutputs(typing.NamedTuple):
    world: Socket[Bundle]

def xpbd_solver(*, world: Bundle | Socket[Bundle] | None = None, delta_time: float | Socket[float] = 0.03999999910593033, filter: str | Socket[str] = '', simulation_to_world: Matrix | Socket[Matrix] | None = None, substeps: int | Socket[int] = 10, constraint_iterations: int | Socket[int] = 1, solver_path: str | Socket[str] = '', begin: float | Socket[float] = 0.0, end: float | Socket[float] = 1.0) -> GeometryNodeXPBDSolverOutputs:
    return _node_function(
        'GeometryNodeXPBDSolver',
        inputs={
            'world': world,
            'delta_time': delta_time,
            'filter': filter,
            'simulation_to_world': simulation_to_world,
            'substeps': substeps,
            'constraint_iterations': constraint_iterations,
            'solver_path': solver_path,
            'begin': begin,
            'end': end,
        },
        input_sockets={
            'world': ('World', 'World', 0, None),
            'delta_time': ('Delta Time', 'Delta Time', 1, 0.03999999910593033),
            'filter': ('Filter', 'Filter', 2, ''),
            'simulation_to_world': ('Simulation to World', 'Simulation to World', 3, None),
            'substeps': ('Substeps', 'Substeps', 4, 10),
            'constraint_iterations': ('Constraint Iterations', 'Constraint Iterations', 5, 1),
            'solver_path': ('Solver Path', 'Solver Path', 6, ''),
            'begin': ('Begin', 'Begin', 7, 0.0),
            'end': ('End', 'End', 8, 1.0),
        },
        properties={
        },
        output_sockets={
            'world': ('World', 'World', 0, 'AUTO'),
        },
        output_type=GeometryNodeXPBDSolverOutputs,
    )
