# Generated from Blender 5.2.0 LTS (ShaderNodeTree).
# Do not edit: run code_generator/node_functions_generator.py instead.

from __future__ import annotations

import typing

import bpy

from .runtime import ItemOutputs, Socket, node_function as _node_function
from .types import *

BLENDER_VERSION = (5, 2, 0)

__all__ = [
    'add_shader',
    'ambient_occlusion',
    'aov_output',
    'attribute',
    'background',
    'bevel',
    'blackbody',
    'boolean',
    'brick_texture',
    'brightness_contrast',
    'bump',
    'camera_data',
    'checker_texture',
    'clamp',
    'color',
    'color_attribute',
    'color_ramp',
    'combine_bundle',
    'combine_color',
    'combine_xyz',
    'curves_info',
    'diffuse_bsdf',
    'displacement',
    'emission',
    'environment_texture',
    'evaluate_closure',
    'float_curve',
    'fresnel',
    'gabor_texture',
    'gamma',
    'geometry',
    'glass_bsdf',
    'glossy_bsdf',
    'gradient_texture',
    'hair_bsdf',
    'holdout',
    'hue_saturation_value',
    'ies_texture',
    'image_texture',
    'integer',
    'invert_color',
    'join_bundle',
    'layer_weight',
    'light_falloff',
    'light_output',
    'light_path',
    'line_style_output',
    'magic_texture',
    'map_range',
    'mapping',
    'material_output',
    'math_',
    'menu',
    'menu_switch',
    'metallic_bsdf',
    'mix',
    'mix_legacy',
    'mix_shader',
    'noise_texture',
    'normal',
    'normal_map',
    'object_info',
    'particle_info',
    'point_info',
    'principled_bsdf',
    'principled_hair_bsdf',
    'principled_volume',
    'radial_tiling',
    'ray_portal_bsdf',
    'raycast',
    'refraction_bsdf',
    'rgb_curves',
    'rgb_to_bw',
    'scene_time',
    'script',
    'separate_bundle',
    'separate_color',
    'separate_xyz',
    'shader_to_rgb',
    'sheen_bsdf',
    'sky_texture',
    'specular_bsdf',
    'squeeze_value_legacy',
    'subsurface_scattering',
    'tangent',
    'texture_coordinate',
    'toon_bsdf',
    'translucent_bsdf',
    'transparent_bsdf',
    'uv_along_stroke',
    'uv_map',
    'value',
    'vector',
    'vector_curves',
    'vector_displacement',
    'vector_math',
    'vector_rotate',
    'vector_transform',
    'volume_absorption',
    'volume_coefficients',
    'volume_info',
    'volume_scatter',
    'voronoi_texture',
    'wave_texture',
    'wavelength',
    'white_noise_texture',
    'wireframe',
    'world_output',
]

class ShaderNodeAddShaderOutputs(typing.NamedTuple):
    'Outputs from Add Shader: Add two Shaders together'
    shader: Socket[Shader]

def add_shader(*, shader: Shader | Socket[Shader] | None = None, shader_2: Shader | Socket[Shader] | None = None) -> ShaderNodeAddShaderOutputs:
    'Add two Shaders together'
    return _node_function(
        'ShaderNodeAddShader',
        inputs={
            'shader': shader,
            'shader_2': shader_2,
        },
        input_sockets={
            'shader': ('Shader', 'Shader', 0, None),
            'shader_2': ('Shader_001', 'Shader', 1, None),
        },
        properties={
        },
        output_sockets={
            'shader': ('Shader', 'Shader', 0, 'AUTO'),
        },
        output_type=ShaderNodeAddShaderOutputs,
    )

class ShaderNodeAmbientOcclusionOutputs(typing.NamedTuple):
    'Outputs from Ambient Occlusion: Compute how much the hemisphere above the shading point is occluded, for example to add weathering effects to corners.\nNote: For Cycles, this may slow down renders significantly'
    color: Socket[Color]
    ao: Socket[float]

def ambient_occlusion(*, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), distance: float | Socket[float] = 1.0, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), samples: int = 16, inside: bool = False, only_local: bool = False) -> ShaderNodeAmbientOcclusionOutputs:
    'Compute how much the hemisphere above the shading point is occluded, for example to add weathering effects to corners.\nNote: For Cycles, this may slow down renders significantly\n\nArgs:\n    samples: Number of rays to trace per shader evaluation\n    inside: Trace rays towards the inside of the object\n    only_local: Only consider the object itself when computing AO'
    return _node_function(
        'ShaderNodeAmbientOcclusion',
        inputs={
            'color': color,
            'distance': distance,
            'normal': normal,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 1.0, 1.0, 1.0)),
            'distance': ('Distance', 'Distance', 1, 1.0),
            'normal': ('Normal', 'Normal', 2, (0.0, 0.0, 0.0)),
        },
        properties={
            'samples': samples,
            'inside': inside,
            'only_local': only_local,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
            'ao': ('AO', 'AO', 1, 'AUTO'),
        },
        output_type=ShaderNodeAmbientOcclusionOutputs,
    )

def aov_output(*, color: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), value: float | Socket[float] = 0.0, aov_name: str = '') -> None:
    'Arbitrary Output Variables.\nProvide custom render passes for arbitrary shader node outputs\n\nArgs:\n    aov_name: Name of the AOV that this output writes to'
    return _node_function(
        'ShaderNodeOutputAOV',
        inputs={
            'color': color,
            'value': value,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.0, 0.0, 0.0, 1.0)),
            'value': ('Value', 'Value', 1, 0.0),
        },
        properties={
            'aov_name': aov_name,
        },
        output_sockets={
        },
        output_type=None,
    )

class ShaderNodeAttributeOutputs(typing.NamedTuple):
    'Outputs from Attribute: Retrieve attributes attached to objects or geometry'
    color: Socket[Color]
    vector: Socket[Vector]
    factor: Socket[float]
    alpha: Socket[float]

def attribute(*, attribute_type: typing.Literal['GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER'] = 'GEOMETRY', attribute_name: str = '') -> ShaderNodeAttributeOutputs:
    'Retrieve attributes attached to objects or geometry\n\nArgs:\n    attribute_type: General type of the attribute'
    return _node_function(
        'ShaderNodeAttribute',
        inputs={
        },
        input_sockets={
        },
        properties={
            'attribute_type': attribute_type,
            'attribute_name': attribute_name,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
            'vector': ('Vector', 'Vector', 1, 'AUTO'),
            'factor': ('Fac', 'Factor', 2, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 3, 'AUTO'),
        },
        output_type=ShaderNodeAttributeOutputs,
    )

class ShaderNodeBackgroundOutputs(typing.NamedTuple):
    'Outputs from Background: Add background light emission.\nNote: This node should only be used for the world surface output'
    background: Socket[Shader]

def background(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), strength: float | Socket[float] = 1.0) -> ShaderNodeBackgroundOutputs:
    'Add background light emission.\nNote: This node should only be used for the world surface output'
    return _node_function(
        'ShaderNodeBackground',
        inputs={
            'color': color,
            'strength': strength,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'strength': ('Strength', 'Strength', 1, 1.0),
        },
        properties={
        },
        output_sockets={
            'background': ('Background', 'Background', 0, 'AUTO'),
        },
        output_type=ShaderNodeBackgroundOutputs,
    )

class ShaderNodeBevelOutputs(typing.NamedTuple):
    'Outputs from Bevel: Generates normals with round corners.\nNote: only supported in Cycles, and may slow down renders'
    normal: Socket[Vector]

def bevel(*, radius: float | Socket[float] = 0.05000000074505806, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), samples: int = 4) -> ShaderNodeBevelOutputs:
    'Generates normals with round corners.\nNote: only supported in Cycles, and may slow down renders\n\nArgs:\n    samples: Number of rays to trace per shader evaluation'
    return _node_function(
        'ShaderNodeBevel',
        inputs={
            'radius': radius,
            'normal': normal,
        },
        input_sockets={
            'radius': ('Radius', 'Radius', 0, 0.05000000074505806),
            'normal': ('Normal', 'Normal', 1, (0.0, 0.0, 0.0)),
        },
        properties={
            'samples': samples,
        },
        output_sockets={
            'normal': ('Normal', 'Normal', 0, 'AUTO'),
        },
        output_type=ShaderNodeBevelOutputs,
    )

class ShaderNodeBlackbodyOutputs(typing.NamedTuple):
    'Outputs from Blackbody: Convert a blackbody temperature to an RGB value'
    color: Socket[Color]

def blackbody(*, temperature: float | Socket[float] = 6500.0) -> ShaderNodeBlackbodyOutputs:
    'Convert a blackbody temperature to an RGB value'
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

class FunctionNodeInputBoolOutputs(typing.NamedTuple):
    'Outputs from Boolean: Provide a True/False value that can be connected to other nodes in the tree'
    boolean: Socket[bool]

def boolean(*, boolean: bool = False) -> FunctionNodeInputBoolOutputs:
    'Provide a True/False value that can be connected to other nodes in the tree\n\nArgs:\n    boolean: Input value used for unconnected socket'
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

class ShaderNodeTexBrickOutputs(typing.NamedTuple):
    'Outputs from Brick Texture: Generate a procedural texture producing bricks'
    color: Socket[Color]
    factor: Socket[float]

def brick_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), color1: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), color2: Color | Socket[Color] = (0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0), mortar: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), scale: float | Socket[float] = 5.0, mortar_size: float | Socket[float] = 0.019999999552965164, mortar_smooth: float | Socket[float] = 0.10000000149011612, bias: float | Socket[float] = 0.0, brick_width: float | Socket[float] = 0.5, row_height: float | Socket[float] = 0.25, offset_frequency: int = 2, squash_frequency: int = 2, offset: float = 0.5, squash: float = 1.0) -> ShaderNodeTexBrickOutputs:
    'Generate a procedural texture producing bricks\n\nArgs:\n    offset_frequency: How often rows are offset. A value of 2 gives an even/uneven pattern of rows.\n    squash_frequency: How often rows consist of "squished" bricks\n    offset: Determines the brick offset of the various rows\n    squash: Factor to adjust the brick\'s width for particular rows determined by the Offset Frequency'
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
            'color': ('Color', 'Color', 0, 'AUTO'),
            'factor': ('Fac', 'Factor', 1, 'AUTO'),
        },
        output_type=ShaderNodeTexBrickOutputs,
    )

class ShaderNodeBrightContrastOutputs(typing.NamedTuple):
    'Outputs from Brightness/Contrast: Control the brightness and contrast of the input color'
    color: Socket[Color]

def brightness_contrast(*, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), brightness: float | Socket[float] = 0.0, contrast: float | Socket[float] = 0.0) -> ShaderNodeBrightContrastOutputs:
    'Control the brightness and contrast of the input color'
    return _node_function(
        'ShaderNodeBrightContrast',
        inputs={
            'color': color,
            'brightness': brightness,
            'contrast': contrast,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 1.0, 1.0, 1.0)),
            'brightness': ('Bright', 'Brightness', 1, 0.0),
            'contrast': ('Contrast', 'Contrast', 2, 0.0),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeBrightContrastOutputs,
    )

class ShaderNodeBumpOutputs(typing.NamedTuple):
    'Outputs from Bump: Generate a perturbed normal from a height texture for bump mapping. Typically used for faking highly detailed surfaces'
    normal: Socket[Vector]

def bump(*, strength: float | Socket[float] = 1.0, distance: float | Socket[float] = 0.0010000000474974513, filter_width: float | Socket[float] = 0.10000000149011612, height: float | Socket[float] = 1.0, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), invert: bool = False) -> ShaderNodeBumpOutputs:
    'Generate a perturbed normal from a height texture for bump mapping. Typically used for faking highly detailed surfaces\n\nArgs:\n    invert: Invert the bump mapping direction to push into the surface instead of out'
    return _node_function(
        'ShaderNodeBump',
        inputs={
            'strength': strength,
            'distance': distance,
            'filter_width': filter_width,
            'height': height,
            'normal': normal,
        },
        input_sockets={
            'strength': ('Strength', 'Strength', 0, 1.0),
            'distance': ('Distance', 'Distance', 1, 0.0010000000474974513),
            'filter_width': ('Filter Width', 'Filter Width', 2, 0.10000000149011612),
            'height': ('Height', 'Height', 3, 1.0),
            'normal': ('Normal', 'Normal', 4, (0.0, 0.0, 0.0)),
        },
        properties={
            'invert': invert,
        },
        output_sockets={
            'normal': ('Normal', 'Normal', 0, 'AUTO'),
        },
        output_type=ShaderNodeBumpOutputs,
    )

class ShaderNodeCameraDataOutputs(typing.NamedTuple):
    "Outputs from Camera Data: Retrieve information about the camera and how it relates to the current shading point's position"
    view_vector: Socket[Vector]
    view_z_depth: Socket[float]
    view_distance: Socket[float]

def camera_data() -> ShaderNodeCameraDataOutputs:
    "Retrieve information about the camera and how it relates to the current shading point's position"
    return _node_function(
        'ShaderNodeCameraData',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'view_vector': ('View Vector', 'View Vector', 0, 'AUTO'),
            'view_z_depth': ('View Z Depth', 'View Z Depth', 1, 'AUTO'),
            'view_distance': ('View Distance', 'View Distance', 2, 'AUTO'),
        },
        output_type=ShaderNodeCameraDataOutputs,
    )

class ShaderNodeTexCheckerOutputs(typing.NamedTuple):
    'Outputs from Checker Texture: Generate a checkerboard texture'
    color: Socket[Color]
    factor: Socket[float]

def checker_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), color1: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), color2: Color | Socket[Color] = (0.20000000298023224, 0.20000000298023224, 0.20000000298023224, 1.0), scale: float | Socket[float] = 5.0) -> ShaderNodeTexCheckerOutputs:
    'Generate a checkerboard texture'
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
            'color': ('Color', 'Color', 0, 'AUTO'),
            'factor': ('Fac', 'Factor', 1, 'AUTO'),
        },
        output_type=ShaderNodeTexCheckerOutputs,
    )

class ShaderNodeClampOutputs(typing.NamedTuple):
    'Outputs from Clamp: Clamp a value between a minimum and a maximum'
    result: Socket[float]

def clamp(*, value: float | Socket[float] = 1.0, min: float | Socket[float] = 0.0, max: float | Socket[float] = 1.0, clamp_type: typing.Literal['MINMAX', 'RANGE'] = 'MINMAX') -> ShaderNodeClampOutputs:
    'Clamp a value between a minimum and a maximum'
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

class ShaderNodeRGBOutputs(typing.NamedTuple):
    'Outputs from Color: A color picker'
    color: Socket[Color]

def color() -> ShaderNodeRGBOutputs:
    'A color picker'
    return _node_function(
        'ShaderNodeRGB',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeRGBOutputs,
    )

class ShaderNodeVertexColorOutputs(typing.NamedTuple):
    'Outputs from Color Attribute: Retrieve a color attribute, or the default fallback if none is specified'
    color: Socket[Color]
    alpha: Socket[float]

def color_attribute(*, layer_name: str = '') -> ShaderNodeVertexColorOutputs:
    'Retrieve a color attribute, or the default fallback if none is specified\n\nArgs:\n    layer_name: Color Attribute'
    return _node_function(
        'ShaderNodeVertexColor',
        inputs={
        },
        input_sockets={
        },
        properties={
            'layer_name': layer_name,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 1, 'AUTO'),
        },
        output_type=ShaderNodeVertexColorOutputs,
    )

class ShaderNodeValToRGBOutputs(typing.NamedTuple):
    'Outputs from Color Ramp: Map values to colors with the use of a gradient'
    color: Socket[Color]
    alpha: Socket[float]

def color_ramp(*, factor: float | Socket[float] = 0.5) -> ShaderNodeValToRGBOutputs:
    'Map values to colors with the use of a gradient'
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
    'Outputs from Combine Bundle: Combine multiple socket values into one.'
    bundle: Socket[Bundle]

def combine_bundle(*, define_signature: bool = False, **items: typing.Any) -> NodeCombineBundleOutputs:
    'Combine multiple socket values into one.\n\nArgs:\n    define_signature: This node defines a bundle signature that should be used by other nodes\n    items: Items to add, by name; each socket type is inferred from its value.'
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

class ShaderNodeCombineColorOutputs(typing.NamedTuple):
    'Outputs from Combine Color: Create a color from individual components using multiple models'
    color: Socket[Color]

def combine_color(*, red: float | Socket[float] = 0.0, green: float | Socket[float] = 0.0, blue: float | Socket[float] = 0.0, mode: typing.Literal['RGB', 'HSV', 'HSL'] = 'RGB') -> ShaderNodeCombineColorOutputs:
    'Create a color from individual components using multiple models\n\nArgs:\n    mode: Mode of color processing'
    return _node_function(
        'ShaderNodeCombineColor',
        inputs={
            'red': red,
            'green': green,
            'blue': blue,
        },
        input_sockets={
            'red': ('Red', 'Red', 0, 0.0),
            'green': ('Green', 'Green', 1, 0.0),
            'blue': ('Blue', 'Blue', 2, 0.0),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeCombineColorOutputs,
    )

class ShaderNodeCombineXYZOutputs(typing.NamedTuple):
    'Outputs from Combine XYZ: Create a vector from X, Y, and Z components'
    vector: Socket[Vector]

def combine_xyz(*, x: float | Socket[float] = 0.0, y: float | Socket[float] = 0.0, z: float | Socket[float] = 0.0) -> ShaderNodeCombineXYZOutputs:
    'Create a vector from X, Y, and Z components'
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

class ShaderNodeHairInfoOutputs(typing.NamedTuple):
    'Outputs from Curves Info: Retrieve hair curve information'
    is_strand: Socket[float]
    intercept: Socket[float]
    length: Socket[float]
    thickness: Socket[float]
    tangent_normal: Socket[Vector]
    random: Socket[float]

def curves_info() -> ShaderNodeHairInfoOutputs:
    'Retrieve hair curve information'
    return _node_function(
        'ShaderNodeHairInfo',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'is_strand': ('Is Strand', 'Is Strand', 0, 'AUTO'),
            'intercept': ('Intercept', 'Intercept', 1, 'AUTO'),
            'length': ('Length', 'Length', 2, 'AUTO'),
            'thickness': ('Thickness', 'Thickness', 3, 'AUTO'),
            'tangent_normal': ('Tangent Normal', 'Tangent Normal', 4, 'AUTO'),
            'random': ('Random', 'Random', 5, 'AUTO'),
        },
        output_type=ShaderNodeHairInfoOutputs,
    )

class ShaderNodeBsdfDiffuseOutputs(typing.NamedTuple):
    'Outputs from Diffuse BSDF: Lambertian and Oren-Nayar diffuse reflection'
    bsdf: Socket[Shader]

def diffuse_bsdf(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), roughness: float | Socket[float] = 0.0, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0)) -> ShaderNodeBsdfDiffuseOutputs:
    'Lambertian and Oren-Nayar diffuse reflection'
    return _node_function(
        'ShaderNodeBsdfDiffuse',
        inputs={
            'color': color,
            'roughness': roughness,
            'normal': normal,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'roughness': ('Roughness', 'Roughness', 1, 0.0),
            'normal': ('Normal', 'Normal', 2, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfDiffuseOutputs,
    )

class ShaderNodeDisplacementOutputs(typing.NamedTuple):
    'Outputs from Displacement: Displace the surface along the surface normal'
    displacement: Socket[Vector]

def displacement(*, height: float | Socket[float] = 0.0, midlevel: float | Socket[float] = 0.5, scale: float | Socket[float] = 0.009999999776482582, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), space: typing.Literal['OBJECT', 'WORLD'] = 'OBJECT') -> ShaderNodeDisplacementOutputs:
    'Displace the surface along the surface normal\n\nArgs:\n    space: Space of the input height'
    return _node_function(
        'ShaderNodeDisplacement',
        inputs={
            'height': height,
            'midlevel': midlevel,
            'scale': scale,
            'normal': normal,
        },
        input_sockets={
            'height': ('Height', 'Height', 0, 0.0),
            'midlevel': ('Midlevel', 'Midlevel', 1, 0.5),
            'scale': ('Scale', 'Scale', 2, 0.009999999776482582),
            'normal': ('Normal', 'Normal', 3, (0.0, 0.0, 0.0)),
        },
        properties={
            'space': space,
        },
        output_sockets={
            'displacement': ('Displacement', 'Displacement', 0, 'AUTO'),
        },
        output_type=ShaderNodeDisplacementOutputs,
    )

class ShaderNodeEmissionOutputs(typing.NamedTuple):
    'Outputs from Emission: Lambertian emission shader'
    emission: Socket[Shader]

def emission(*, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), strength: float | Socket[float] = 1.0) -> ShaderNodeEmissionOutputs:
    'Lambertian emission shader'
    return _node_function(
        'ShaderNodeEmission',
        inputs={
            'color': color,
            'strength': strength,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 1.0, 1.0, 1.0)),
            'strength': ('Strength', 'Strength', 1, 1.0),
        },
        properties={
        },
        output_sockets={
            'emission': ('Emission', 'Emission', 0, 'AUTO'),
        },
        output_type=ShaderNodeEmissionOutputs,
    )

class ShaderNodeTexEnvironmentOutputs(typing.NamedTuple):
    'Outputs from Environment Texture: Sample an image file as an environment texture. Typically used to light the scene with the background node'
    color: Socket[Color]

def environment_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), image: bpy.types.Image | None = None, projection: typing.Literal['EQUIRECTANGULAR', 'MIRROR_BALL'] = 'EQUIRECTANGULAR', interpolation: typing.Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear') -> ShaderNodeTexEnvironmentOutputs:
    'Sample an image file as an environment texture. Typically used to light the scene with the background node\n\nArgs:\n    projection: Projection of the input image\n    interpolation: Texture interpolation'
    return _node_function(
        'ShaderNodeTexEnvironment',
        inputs={
            'vector': vector,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
        },
        properties={
            'image': image,
            'projection': projection,
            'interpolation': interpolation,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeTexEnvironmentOutputs,
    )

class NodeEvaluateClosureOutputs(ItemOutputs):
    'Outputs from Evaluate Closure: Execute a given closure'

def evaluate_closure(*, closure: Closure | Socket[Closure] | None = None, define_signature: bool = False, outputs: typing.Mapping[str, typing.Any] | None = None, **items: typing.Any) -> NodeEvaluateClosureOutputs:
    'Execute a given closure\n\nArgs:\n    define_signature: This node defines a closure signature that should be used by other nodes\n    items: Items to add, by name; each socket type is inferred from its value.\n    outputs: Items to add, mapping each name to its type (float, Vector, Geometry, ...). Their outputs are available by name on the result.'
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

class ShaderNodeFloatCurveOutputs(typing.NamedTuple):
    'Outputs from Float Curve: Map an input float to a curve and outputs a float value'
    value: Socket[float]

def float_curve(*, factor: float | Socket[float] = 1.0, value: float | Socket[float] = 1.0) -> ShaderNodeFloatCurveOutputs:
    'Map an input float to a curve and outputs a float value'
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

class ShaderNodeFresnelOutputs(typing.NamedTuple):
    'Outputs from Fresnel: Produce a blending factor depending on the angle between the surface normal and the view direction using Fresnel equations.\nTypically used for mixing reflections at grazing angles'
    factor: Socket[float]

def fresnel(*, ior: float | Socket[float] = 1.5, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0)) -> ShaderNodeFresnelOutputs:
    'Produce a blending factor depending on the angle between the surface normal and the view direction using Fresnel equations.\nTypically used for mixing reflections at grazing angles'
    return _node_function(
        'ShaderNodeFresnel',
        inputs={
            'ior': ior,
            'normal': normal,
        },
        input_sockets={
            'ior': ('IOR', 'IOR', 0, 1.5),
            'normal': ('Normal', 'Normal', 1, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'factor': ('Fac', 'Factor', 0, 'AUTO'),
        },
        output_type=ShaderNodeFresnelOutputs,
    )

class ShaderNodeTexGaborOutputs(typing.NamedTuple):
    'Outputs from Gabor Texture: Generate Gabor noise'
    value: Socket[float]
    phase: Socket[float]
    intensity: Socket[float]

def gabor_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), scale: float | Socket[float] = 5.0, frequency: float | Socket[float] = 2.0, anisotropy: float | Socket[float] = 1.0, orientation: float | Vector | Socket[float | Vector] = 0.7853981852531433, gabor_type: typing.Literal['2D', '3D'] | None = None) -> ShaderNodeTexGaborOutputs:
    'Generate Gabor noise\n\nArgs:\n    gabor_type: The type of Gabor noise to evaluate Inferred from the linked inputs when None.'
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
            'value': ('Value', 'Value', 0, 'AUTO'),
            'phase': ('Phase', 'Phase', 1, 'AUTO'),
            'intensity': ('Intensity', 'Intensity', 2, 'AUTO'),
        },
        output_type=ShaderNodeTexGaborOutputs,
        type_properties={'gabor_type': {'2D': {'orientation': 'VALUE'}, '3D': {'orientation': 'VECTOR'}}},
    )

class ShaderNodeGammaOutputs(typing.NamedTuple):
    'Outputs from Gamma: Apply a gamma correction'
    color: Socket[Color]

def gamma(*, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), gamma: float | Socket[float] = 1.0) -> ShaderNodeGammaOutputs:
    'Apply a gamma correction'
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

class ShaderNodeNewGeometryOutputs(typing.NamedTuple):
    'Outputs from Geometry: Retrieve geometric information about the current shading point'
    position: Socket[Vector]
    normal: Socket[Vector]
    tangent: Socket[Vector]
    true_normal: Socket[Vector]
    incoming: Socket[Vector]
    parametric: Socket[Vector]
    backfacing: Socket[float]
    pointiness: Socket[float]
    random_per_island: Socket[float]

def geometry() -> ShaderNodeNewGeometryOutputs:
    'Retrieve geometric information about the current shading point'
    return _node_function(
        'ShaderNodeNewGeometry',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'position': ('Position', 'Position', 0, 'AUTO'),
            'normal': ('Normal', 'Normal', 1, 'AUTO'),
            'tangent': ('Tangent', 'Tangent', 2, 'AUTO'),
            'true_normal': ('True Normal', 'True Normal', 3, 'AUTO'),
            'incoming': ('Incoming', 'Incoming', 4, 'AUTO'),
            'parametric': ('Parametric', 'Parametric', 5, 'AUTO'),
            'backfacing': ('Backfacing', 'Backfacing', 6, 'AUTO'),
            'pointiness': ('Pointiness', 'Pointiness', 7, 'AUTO'),
            'random_per_island': ('Random Per Island', 'Random Per Island', 8, 'AUTO'),
        },
        output_type=ShaderNodeNewGeometryOutputs,
    )

class ShaderNodeBsdfGlassOutputs(typing.NamedTuple):
    'Outputs from Glass BSDF: Glass-like shader mixing refraction and reflection at grazing angles'
    bsdf: Socket[Shader]

def glass_bsdf(*, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), roughness: float | Socket[float] = 0.0, ior: float | Socket[float] = 1.5, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), thin_film_thickness: float | Socket[float] = 0.0, thin_film_ior: float | Socket[float] = 1.3300000429153442, distribution: typing.Literal['BECKMANN', 'GGX', 'MULTI_GGX'] = 'MULTI_GGX') -> ShaderNodeBsdfGlassOutputs:
    'Glass-like shader mixing refraction and reflection at grazing angles\n\nArgs:\n    distribution: Light scattering distribution on rough surface'
    return _node_function(
        'ShaderNodeBsdfGlass',
        inputs={
            'color': color,
            'roughness': roughness,
            'ior': ior,
            'normal': normal,
            'thin_film_thickness': thin_film_thickness,
            'thin_film_ior': thin_film_ior,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 1.0, 1.0, 1.0)),
            'roughness': ('Roughness', 'Roughness', 1, 0.0),
            'ior': ('IOR', 'IOR', 2, 1.5),
            'normal': ('Normal', 'Normal', 3, (0.0, 0.0, 0.0)),
            'thin_film_thickness': ('Thin Film Thickness', 'Thin Film Thickness', 5, 0.0),
            'thin_film_ior': ('Thin Film IOR', 'Thin Film IOR', 6, 1.3300000429153442),
        },
        properties={
            'distribution': distribution,
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfGlassOutputs,
    )

class ShaderNodeBsdfAnisotropicOutputs(typing.NamedTuple):
    'Outputs from Glossy BSDF: Reflection with microfacet distribution, used for materials such as metal or mirrors'
    bsdf: Socket[Shader]

def glossy_bsdf(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), roughness: float | Socket[float] = 0.5, anisotropy: float | Socket[float] = 0.0, rotation: float | Socket[float] = 0.0, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), tangent: Vector | Socket[Vector] = (0.0, 0.0, 0.0), distribution: typing.Literal['BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX'] = 'MULTI_GGX') -> ShaderNodeBsdfAnisotropicOutputs:
    'Reflection with microfacet distribution, used for materials such as metal or mirrors\n\nArgs:\n    distribution: Light scattering distribution on rough surface'
    return _node_function(
        'ShaderNodeBsdfAnisotropic',
        inputs={
            'color': color,
            'roughness': roughness,
            'anisotropy': anisotropy,
            'rotation': rotation,
            'normal': normal,
            'tangent': tangent,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'roughness': ('Roughness', 'Roughness', 1, 0.5),
            'anisotropy': ('Anisotropy', 'Anisotropy', 2, 0.0),
            'rotation': ('Rotation', 'Rotation', 3, 0.0),
            'normal': ('Normal', 'Normal', 4, (0.0, 0.0, 0.0)),
            'tangent': ('Tangent', 'Tangent', 5, (0.0, 0.0, 0.0)),
        },
        properties={
            'distribution': distribution,
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfAnisotropicOutputs,
    )

class ShaderNodeTexGradientOutputs(typing.NamedTuple):
    'Outputs from Gradient Texture: Generate interpolated color and intensity values based on the input vector'
    color: Socket[Color]
    factor: Socket[float]

def gradient_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), gradient_type: typing.Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL'] = 'LINEAR') -> ShaderNodeTexGradientOutputs:
    'Generate interpolated color and intensity values based on the input vector\n\nArgs:\n    gradient_type: Style of the color blending'
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
            'color': ('Color', 'Color', 0, 'AUTO'),
            'factor': ('Fac', 'Factor', 1, 'AUTO'),
        },
        output_type=ShaderNodeTexGradientOutputs,
    )

class ShaderNodeBsdfHairOutputs(typing.NamedTuple):
    'Outputs from Hair BSDF: Reflection and transmission shaders optimized for hair rendering'
    bsdf: Socket[Shader]

def hair_bsdf(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), offset: float | Socket[float] = 0.0, roughness_u: float | Socket[float] = 0.10000000149011612, roughness_v: float | Socket[float] = 1.0, tangent: Vector | Socket[Vector] = (0.0, 0.0, 0.0), component: typing.Literal['Reflection', 'Transmission'] = 'Reflection') -> ShaderNodeBsdfHairOutputs:
    'Reflection and transmission shaders optimized for hair rendering\n\nArgs:\n    component: Hair BSDF component to use'
    return _node_function(
        'ShaderNodeBsdfHair',
        inputs={
            'color': color,
            'offset': offset,
            'roughness_u': roughness_u,
            'roughness_v': roughness_v,
            'tangent': tangent,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'offset': ('Offset', 'Offset', 1, 0.0),
            'roughness_u': ('RoughnessU', 'RoughnessU', 2, 0.10000000149011612),
            'roughness_v': ('RoughnessV', 'RoughnessV', 3, 1.0),
            'tangent': ('Tangent', 'Tangent', 4, (0.0, 0.0, 0.0)),
        },
        properties={
            'component': component,
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfHairOutputs,
    )

class ShaderNodeHoldoutOutputs(typing.NamedTuple):
    'Outputs from Holdout: Create a "hole" in the image with zero alpha transparency, which is useful for compositing.\nNote: the holdout shader can only create alpha when transparency is enabled in the film settings'
    holdout: Socket[Shader]

def holdout() -> ShaderNodeHoldoutOutputs:
    'Create a "hole" in the image with zero alpha transparency, which is useful for compositing.\nNote: the holdout shader can only create alpha when transparency is enabled in the film settings'
    return _node_function(
        'ShaderNodeHoldout',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'holdout': ('Holdout', 'Holdout', 0, 'AUTO'),
        },
        output_type=ShaderNodeHoldoutOutputs,
    )

class ShaderNodeHueSaturationOutputs(typing.NamedTuple):
    'Outputs from Hue/Saturation/Value: Apply a color transformation in the HSV color model'
    color: Socket[Color]

def hue_saturation_value(*, hue: float | Socket[float] = 0.5, saturation: float | Socket[float] = 1.0, value: float | Socket[float] = 1.0, factor: float | Socket[float] = 1.0, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)) -> ShaderNodeHueSaturationOutputs:
    'Apply a color transformation in the HSV color model'
    return _node_function(
        'ShaderNodeHueSaturation',
        inputs={
            'hue': hue,
            'saturation': saturation,
            'value': value,
            'factor': factor,
            'color': color,
        },
        input_sockets={
            'hue': ('Hue', 'Hue', 0, 0.5),
            'saturation': ('Saturation', 'Saturation', 1, 1.0),
            'value': ('Value', 'Value', 2, 1.0),
            'factor': ('Fac', 'Factor', 3, 1.0),
            'color': ('Color', 'Color', 4, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeHueSaturationOutputs,
    )

class ShaderNodeTexIESOutputs(typing.NamedTuple):
    'Outputs from IES Texture: Match real world lights with IES files, which store the directional intensity distribution of light sources'
    factor: Socket[float]

def ies_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), strength: float | Socket[float] = 1.0, ies: bpy.types.Text | None = None, filepath: str = '', mode: typing.Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL') -> ShaderNodeTexIESOutputs:
    'Match real world lights with IES files, which store the directional intensity distribution of light sources\n\nArgs:\n    ies: Internal IES file\n    filepath: IES light path\n    mode: Whether the IES file is loaded from disk or from a text data-block'
    return _node_function(
        'ShaderNodeTexIES',
        inputs={
            'vector': vector,
            'strength': strength,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'strength': ('Strength', 'Strength', 1, 1.0),
        },
        properties={
            'ies': ies,
            'filepath': filepath,
            'mode': mode,
        },
        output_sockets={
            'factor': ('Fac', 'Factor', 0, 'AUTO'),
        },
        output_type=ShaderNodeTexIESOutputs,
    )

class ShaderNodeTexImageOutputs(typing.NamedTuple):
    'Outputs from Image Texture: Sample an image file as a texture'
    color: Socket[Color]
    alpha: Socket[float]

def image_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), image: bpy.types.Image | None = None, projection: typing.Literal['FLAT', 'BOX', 'SPHERE', 'TUBE'] = 'FLAT', interpolation: typing.Literal['Linear', 'Closest', 'Cubic', 'Smart'] = 'Linear', projection_blend: float = 0.0, extension: typing.Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR'] = 'REPEAT') -> ShaderNodeTexImageOutputs:
    'Sample an image file as a texture\n\nArgs:\n    projection: Method to project 2D image on object with a 3D texture vector\n    interpolation: Texture interpolation\n    projection_blend: For box projection, amount of blend to use between sides\n    extension: How the image is extrapolated past its original bounds'
    return _node_function(
        'ShaderNodeTexImage',
        inputs={
            'vector': vector,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
        },
        properties={
            'image': image,
            'projection': projection,
            'interpolation': interpolation,
            'projection_blend': projection_blend,
            'extension': extension,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 1, 'AUTO'),
        },
        output_type=ShaderNodeTexImageOutputs,
    )

class FunctionNodeInputIntOutputs(typing.NamedTuple):
    'Outputs from Integer: Provide an integer value that can be connected to other nodes in the tree'
    integer: Socket[int]

def integer(*, integer: int = 0) -> FunctionNodeInputIntOutputs:
    'Provide an integer value that can be connected to other nodes in the tree\n\nArgs:\n    integer: Input value used for unconnected socket'
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

class ShaderNodeInvertOutputs(typing.NamedTuple):
    'Outputs from Invert Color: Invert a color, producing a negative'
    color: Socket[Color]

def invert_color(*, factor: float | Socket[float] = 1.0, color: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0)) -> ShaderNodeInvertOutputs:
    'Invert a color, producing a negative'
    return _node_function(
        'ShaderNodeInvert',
        inputs={
            'factor': factor,
            'color': color,
        },
        input_sockets={
            'factor': ('Fac', 'Factor', 0, 1.0),
            'color': ('Color', 'Color', 1, (0.0, 0.0, 0.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeInvertOutputs,
    )

class NodeJoinBundleOutputs(typing.NamedTuple):
    'Outputs from Join Bundle: Join multiple bundles together'
    bundle: Socket[Bundle]

def join_bundle(*, bundle: typing.Sequence[Bundle | Socket[Bundle]] = ()) -> NodeJoinBundleOutputs:
    'Join multiple bundles together'
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

class ShaderNodeLayerWeightOutputs(typing.NamedTuple):
    'Outputs from Layer Weight: Produce a blending factor depending on the angle between the surface normal and the view direction.\nTypically used for layering shaders with the Mix Shader node'
    fresnel: Socket[float]
    facing: Socket[float]

def layer_weight(*, blend: float | Socket[float] = 0.5, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0)) -> ShaderNodeLayerWeightOutputs:
    'Produce a blending factor depending on the angle between the surface normal and the view direction.\nTypically used for layering shaders with the Mix Shader node'
    return _node_function(
        'ShaderNodeLayerWeight',
        inputs={
            'blend': blend,
            'normal': normal,
        },
        input_sockets={
            'blend': ('Blend', 'Blend', 0, 0.5),
            'normal': ('Normal', 'Normal', 1, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'fresnel': ('Fresnel', 'Fresnel', 0, 'AUTO'),
            'facing': ('Facing', 'Facing', 1, 'AUTO'),
        },
        output_type=ShaderNodeLayerWeightOutputs,
    )

class ShaderNodeLightFalloffOutputs(typing.NamedTuple):
    'Outputs from Light Falloff: Manipulate how light intensity decreases over distance. Typically used for non-physically-based effects; in reality light always falls off quadratically'
    quadratic: Socket[float]
    linear: Socket[float]
    constant: Socket[float]

def light_falloff(*, strength: float | Socket[float] = 100.0, smooth: float | Socket[float] = 0.0) -> ShaderNodeLightFalloffOutputs:
    'Manipulate how light intensity decreases over distance. Typically used for non-physically-based effects; in reality light always falls off quadratically'
    return _node_function(
        'ShaderNodeLightFalloff',
        inputs={
            'strength': strength,
            'smooth': smooth,
        },
        input_sockets={
            'strength': ('Strength', 'Strength', 0, 100.0),
            'smooth': ('Smooth', 'Smooth', 1, 0.0),
        },
        properties={
        },
        output_sockets={
            'quadratic': ('Quadratic', 'Quadratic', 0, 'AUTO'),
            'linear': ('Linear', 'Linear', 1, 'AUTO'),
            'constant': ('Constant', 'Constant', 2, 'AUTO'),
        },
        output_type=ShaderNodeLightFalloffOutputs,
    )

def light_output(*, surface: Shader | Socket[Shader] | None = None, is_active_output: bool = True, target: typing.Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL') -> None:
    'Output light information to a light object\n\nArgs:\n    is_active_output: True if this node is used as the active output\n    target: Which renderer and viewport shading types to use the shaders for'
    return _node_function(
        'ShaderNodeOutputLight',
        inputs={
            'surface': surface,
        },
        input_sockets={
            'surface': ('Surface', 'Surface', 0, None),
        },
        properties={
            'is_active_output': is_active_output,
            'target': target,
        },
        output_sockets={
        },
        output_type=None,
    )

class ShaderNodeLightPathOutputs(typing.NamedTuple):
    'Outputs from Light Path: Retrieve the type of incoming ray for which the shader is being executed.\nTypically used for non-physically-based tricks'
    is_camera_ray: Socket[float]
    is_shadow_ray: Socket[float]
    is_diffuse_ray: Socket[float]
    is_glossy_ray: Socket[float]
    is_singular_ray: Socket[float]
    is_reflection_ray: Socket[float]
    is_transmission_ray: Socket[float]
    is_volume_scatter_ray: Socket[float]
    ray_length: Socket[float]
    ray_depth: Socket[float]
    diffuse_depth: Socket[float]
    glossy_depth: Socket[float]
    transparent_depth: Socket[float]
    transmission_depth: Socket[float]
    portal_depth: Socket[float]

def light_path() -> ShaderNodeLightPathOutputs:
    'Retrieve the type of incoming ray for which the shader is being executed.\nTypically used for non-physically-based tricks'
    return _node_function(
        'ShaderNodeLightPath',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'is_camera_ray': ('Is Camera Ray', 'Is Camera Ray', 0, 'AUTO'),
            'is_shadow_ray': ('Is Shadow Ray', 'Is Shadow Ray', 1, 'AUTO'),
            'is_diffuse_ray': ('Is Diffuse Ray', 'Is Diffuse Ray', 2, 'AUTO'),
            'is_glossy_ray': ('Is Glossy Ray', 'Is Glossy Ray', 3, 'AUTO'),
            'is_singular_ray': ('Is Singular Ray', 'Is Singular Ray', 4, 'AUTO'),
            'is_reflection_ray': ('Is Reflection Ray', 'Is Reflection Ray', 5, 'AUTO'),
            'is_transmission_ray': ('Is Transmission Ray', 'Is Transmission Ray', 6, 'AUTO'),
            'is_volume_scatter_ray': ('Is Volume Scatter Ray', 'Is Volume Scatter Ray', 7, 'AUTO'),
            'ray_length': ('Ray Length', 'Ray Length', 8, 'AUTO'),
            'ray_depth': ('Ray Depth', 'Ray Depth', 9, 'AUTO'),
            'diffuse_depth': ('Diffuse Depth', 'Diffuse Depth', 10, 'AUTO'),
            'glossy_depth': ('Glossy Depth', 'Glossy Depth', 11, 'AUTO'),
            'transparent_depth': ('Transparent Depth', 'Transparent Depth', 12, 'AUTO'),
            'transmission_depth': ('Transmission Depth', 'Transmission Depth', 13, 'AUTO'),
            'portal_depth': ('Portal Depth', 'Portal Depth', 14, 'AUTO'),
        },
        output_type=ShaderNodeLightPathOutputs,
    )

def line_style_output(*, color: Color | Socket[Color] = (1.0, 0.0, 1.0, 1.0), color_fac: float | Socket[float] = 1.0, alpha: float | Socket[float] = 1.0, alpha_fac: float | Socket[float] = 1.0, is_active_output: bool = True, target: typing.Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL', blend_type: typing.Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX', use_alpha: bool = False, use_clamp: bool = False) -> None:
    'Control the mixing of texture information into the base color of line styles\n\nArgs:\n    is_active_output: True if this node is used as the active output\n    target: Which renderer and viewport shading types to use the shaders for\n    use_alpha: Include alpha of second input in this operation\n    use_clamp: Clamp result of the node to 0.0 to 1.0 range'
    return _node_function(
        'ShaderNodeOutputLineStyle',
        inputs={
            'color': color,
            'color_fac': color_fac,
            'alpha': alpha,
            'alpha_fac': alpha_fac,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 0.0, 1.0, 1.0)),
            'color_fac': ('Color Fac', 'Color Fac', 1, 1.0),
            'alpha': ('Alpha', 'Alpha', 2, 1.0),
            'alpha_fac': ('Alpha Fac', 'Alpha Fac', 3, 1.0),
        },
        properties={
            'is_active_output': is_active_output,
            'target': target,
            'blend_type': blend_type,
            'use_alpha': use_alpha,
            'use_clamp': use_clamp,
        },
        output_sockets={
        },
        output_type=None,
    )

class ShaderNodeTexMagicOutputs(typing.NamedTuple):
    'Outputs from Magic Texture: Generate a psychedelic color texture'
    color: Socket[Color]
    factor: Socket[float]

def magic_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), scale: float | Socket[float] = 5.0, distortion: float | Socket[float] = 1.0, turbulence_depth: int = 2) -> ShaderNodeTexMagicOutputs:
    'Generate a psychedelic color texture\n\nArgs:\n    turbulence_depth: Level of detail in the added turbulent noise'
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
            'color': ('Color', 'Color', 0, 'AUTO'),
            'factor': ('Fac', 'Factor', 1, 'AUTO'),
        },
        output_type=ShaderNodeTexMagicOutputs,
    )

class ShaderNodeMapRangeOutputs(typing.NamedTuple):
    'Outputs from Map Range: Remap a value from a range to a target range'
    result: Socket[float]
    vector: Socket[Vector]

def map_range(*, value: float | Socket[float] = 1.0, from_min: float | Vector | Socket[float | Vector] = 0.0, from_max: float | Vector | Socket[float | Vector] = 1.0, to_min: float | Vector | Socket[float | Vector] = 0.0, to_max: float | Vector | Socket[float | Vector] = 1.0, steps: float | Vector | Socket[float | Vector] = 4.0, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), clamp: bool = True, interpolation_type: typing.Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP'] = 'LINEAR', data_type: typing.Literal['FLOAT', 'FLOAT_VECTOR'] | None = None) -> ShaderNodeMapRangeOutputs:
    'Remap a value from a range to a target range\n\nArgs:\n    clamp: Clamp the result to the target range [To Min, To Max]\n    data_type:  Inferred from the linked inputs when None.'
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

class ShaderNodeMappingOutputs(typing.NamedTuple):
    'Outputs from Mapping: Transform the input vector by applying translation, rotation, and scale'
    vector: Socket[Vector]

def mapping(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), location: Vector | Socket[Vector] = (0.0, 0.0, 0.0), rotation: Vector | Socket[Vector] = (0.0, 0.0, 0.0), scale: Vector | Socket[Vector] = (1.0, 1.0, 1.0), vector_type: typing.Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL'] = 'POINT') -> ShaderNodeMappingOutputs:
    'Transform the input vector by applying translation, rotation, and scale\n\nArgs:\n    vector_type: Type of vector that the mapping transforms'
    return _node_function(
        'ShaderNodeMapping',
        inputs={
            'vector': vector,
            'location': location,
            'rotation': rotation,
            'scale': scale,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
            'location': ('Location', 'Location', 1, (0.0, 0.0, 0.0)),
            'rotation': ('Rotation', 'Rotation', 2, (0.0, 0.0, 0.0)),
            'scale': ('Scale', 'Scale', 3, (1.0, 1.0, 1.0)),
        },
        properties={
            'vector_type': vector_type,
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
        },
        output_type=ShaderNodeMappingOutputs,
    )

def material_output(*, surface: Shader | Socket[Shader] | None = None, volume: Shader | Socket[Shader] | None = None, displacement: Vector | Socket[Vector] = (0.0, 0.0, 0.0), thickness: float | Socket[float] = 0.0, is_active_output: bool = True, target: typing.Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL') -> None:
    'Output surface material information for use in rendering\n\nArgs:\n    is_active_output: True if this node is used as the active output\n    target: Which renderer and viewport shading types to use the shaders for'
    return _node_function(
        'ShaderNodeOutputMaterial',
        inputs={
            'surface': surface,
            'volume': volume,
            'displacement': displacement,
            'thickness': thickness,
        },
        input_sockets={
            'surface': ('Surface', 'Surface', 0, None),
            'volume': ('Volume', 'Volume', 1, None),
            'displacement': ('Displacement', 'Displacement', 2, (0.0, 0.0, 0.0)),
            'thickness': ('Thickness', 'Thickness', 3, 0.0),
        },
        properties={
            'is_active_output': is_active_output,
            'target': target,
        },
        output_sockets={
        },
        output_type=None,
    )

class ShaderNodeMathOutputs(typing.NamedTuple):
    'Outputs from Math: Perform math operations'
    value: Socket[float]

def math_(*, value: float | Socket[float] = 0.5, value_2: float | Socket[float] = 0.5, value_3: float | Socket[float] = 0.5, operation: typing.Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'FLOORED_MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES'] = 'ADD', use_clamp: bool = False) -> ShaderNodeMathOutputs:
    'Perform math operations\n\nArgs:\n    use_clamp: Clamp result of the node to 0.0 to 1.0 range'
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

class FunctionNodeInputMenuOutputs(typing.NamedTuple):
    'Outputs from Menu: Provide a menu value that can be connected to other nodes in the tree'
    menu: Socket[Menu]

def menu(*, value: str = '') -> FunctionNodeInputMenuOutputs:
    'Provide a menu value that can be connected to other nodes in the tree\n\nArgs:\n    value: Value of the output socket'
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
    'Outputs from Menu Switch: Select from multiple inputs by name'
    output: Socket[Color | float | int | bool | Vector | Menu | Shader | Bundle | Closure]

def menu_switch(*, menu: Menu | Socket[Menu] = '', data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None, items: typing.Mapping[str, typing.Any] | None = None) -> GeometryNodeMenuSwitchOutputs:
    'Select from multiple inputs by name\n\nArgs:\n    data_type:  Inferred from the linked inputs when None.\n    items: Items to add, mapping each name to its input value. Their outputs are available by name on the result.'
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
        type_properties={'data_type': {'FLOAT': {}, 'INT': {}, 'BOOLEAN': {}, 'VECTOR': {}, 'RGBA': {}, 'MENU': {}, 'SHADER': {}, 'BUNDLE': {}, 'CLOSURE': {}}},
    )

class ShaderNodeBsdfMetallicOutputs(typing.NamedTuple):
    'Outputs from Metallic BSDF: Metallic reflection with microfacet distribution, and metallic fresnel'
    bsdf: Socket[Shader]

def metallic_bsdf(*, base_color: Color | Socket[Color] = (0.6169999837875366, 0.5770000219345093, 0.5400000214576721, 1.0), edge_tint: Color | Socket[Color] = (0.6949999928474426, 0.7260000109672546, 0.7699999809265137, 1.0), roughness: float | Socket[float] = 0.5, anisotropy: float | Socket[float] = 0.0, rotation: float | Socket[float] = 0.0, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), tangent: Vector | Socket[Vector] = (0.0, 0.0, 0.0), thin_film_thickness: float | Socket[float] = 0.0, thin_film_ior: float | Socket[float] = 1.3300000429153442, ior: Vector | Socket[Vector] = (2.756999969482422, 2.513000011444092, 2.2309999465942383), extinction: Vector | Socket[Vector] = (3.867000102996826, 3.4040000438690186, 3.009000062942505), distribution: typing.Literal['BECKMANN', 'GGX', 'MULTI_GGX'] = 'MULTI_GGX', fresnel_type: typing.Literal['PHYSICAL_CONDUCTOR', 'F82'] = 'F82') -> ShaderNodeBsdfMetallicOutputs:
    'Metallic reflection with microfacet distribution, and metallic fresnel\n\nArgs:\n    distribution: Light scattering distribution on rough surface\n    fresnel_type: Fresnel method used to tint the metal'
    return _node_function(
        'ShaderNodeBsdfMetallic',
        inputs={
            'base_color': base_color,
            'edge_tint': edge_tint,
            'roughness': roughness,
            'anisotropy': anisotropy,
            'rotation': rotation,
            'normal': normal,
            'tangent': tangent,
            'thin_film_thickness': thin_film_thickness,
            'thin_film_ior': thin_film_ior,
            'ior': ior,
            'extinction': extinction,
        },
        input_sockets={
            'base_color': ('Base Color', 'Base Color', 0, (0.6169999837875366, 0.5770000219345093, 0.5400000214576721, 1.0)),
            'edge_tint': ('Edge Tint', 'Edge Tint', 1, (0.6949999928474426, 0.7260000109672546, 0.7699999809265137, 1.0)),
            'roughness': ('Roughness', 'Roughness', 4, 0.5),
            'anisotropy': ('Anisotropy', 'Anisotropy', 5, 0.0),
            'rotation': ('Rotation', 'Rotation', 6, 0.0),
            'normal': ('Normal', 'Normal', 7, (0.0, 0.0, 0.0)),
            'tangent': ('Tangent', 'Tangent', 8, (0.0, 0.0, 0.0)),
            'thin_film_thickness': ('Thin Film Thickness', 'Thin Film Thickness', 10, 0.0),
            'thin_film_ior': ('Thin Film IOR', 'Thin Film IOR', 11, 1.3300000429153442),
            'ior': ('IOR', 'IOR', 2, (2.756999969482422, 2.513000011444092, 2.2309999465942383)),
            'extinction': ('Extinction', 'Extinction', 3, (3.867000102996826, 3.4040000438690186, 3.009000062942505)),
        },
        properties={
            'distribution': distribution,
            'fresnel_type': fresnel_type,
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfMetallicOutputs,
    )

class ShaderNodeMixOutputs(typing.NamedTuple):
    'Outputs from Mix: Mix values by a factor'
    result: Socket[float | Vector | Color]

def mix(*, factor: float | Vector | Socket[float | Vector] = 1.0, a: float | Vector | Color | Socket[float | Vector | Color] = 0.0, b: float | Vector | Color | Socket[float | Vector | Color] = 0.0, data_type: typing.Literal['FLOAT', 'VECTOR', 'RGBA', 'ROTATION'] | None = None, factor_mode: typing.Literal['UNIFORM', 'NON_UNIFORM'] = 'UNIFORM', blend_type: typing.Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX', clamp_factor: bool = True, clamp_result: bool = False) -> ShaderNodeMixOutputs:
    'Mix values by a factor\n\nArgs:\n    data_type:  Inferred from the linked inputs when None.\n    clamp_factor: Clamp the factor to [0,1] range\n    clamp_result: Clamp the result to [0,1] range'
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
        type_properties={'data_type': {'FLOAT': {'a': 'VALUE', 'b': 'VALUE'}, 'VECTOR': {'a': 'VECTOR', 'b': 'VECTOR'}, 'RGBA': {'a': 'RGBA', 'b': 'RGBA'}}},
    )

class ShaderNodeMixRGBOutputs(typing.NamedTuple):
    'Outputs from Mix (Legacy): Mix two input colors'
    color: Socket[Color]

def mix_legacy(*, factor: float | Socket[float] = 0.5, color1: Color | Socket[Color] = (0.5, 0.5, 0.5, 1.0), color2: Color | Socket[Color] = (0.5, 0.5, 0.5, 1.0), blend_type: typing.Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX', use_alpha: bool = False, use_clamp: bool = False) -> ShaderNodeMixRGBOutputs:
    'Mix two input colors\n\nArgs:\n    use_alpha: Include alpha of second input in this operation\n    use_clamp: Clamp result of the node to 0.0 to 1.0 range'
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

class ShaderNodeMixShaderOutputs(typing.NamedTuple):
    'Outputs from Mix Shader: Mix two shaders together. Typically used for material layering'
    shader: Socket[Shader]

def mix_shader(*, factor: float | Socket[float] = 0.5, shader: Shader | Socket[Shader] | None = None, shader_2: Shader | Socket[Shader] | None = None) -> ShaderNodeMixShaderOutputs:
    'Mix two shaders together. Typically used for material layering'
    return _node_function(
        'ShaderNodeMixShader',
        inputs={
            'factor': factor,
            'shader': shader,
            'shader_2': shader_2,
        },
        input_sockets={
            'factor': ('Fac', 'Factor', 0, 0.5),
            'shader': ('Shader', 'Shader', 1, None),
            'shader_2': ('Shader_001', 'Shader', 2, None),
        },
        properties={
        },
        output_sockets={
            'shader': ('Shader', 'Shader', 0, 'AUTO'),
        },
        output_type=ShaderNodeMixShaderOutputs,
    )

class ShaderNodeTexNoiseOutputs(typing.NamedTuple):
    'Outputs from Noise Texture: Generate fractal Perlin noise'
    factor: Socket[float]
    color: Socket[Color]

def noise_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), scale: float | Socket[float] = 5.0, detail: float | Socket[float] = 2.0, roughness: float | Socket[float] = 0.5, lacunarity: float | Socket[float] = 2.0, distortion: float | Socket[float] = 0.0, w: float | Socket[float] = 0.0, offset: float | Socket[float] = 0.0, gain: float | Socket[float] = 1.0, noise_dimensions: typing.Literal['1D', '2D', '3D', '4D'] = '3D', noise_type: typing.Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM', normalize: bool = True) -> ShaderNodeTexNoiseOutputs:
    'Generate fractal Perlin noise\n\nArgs:\n    noise_dimensions: Number of dimensions to output noise for\n    noise_type: Type of the Noise texture\n    normalize: Normalize outputs to 0.0 to 1.0 range'
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
            'factor': ('Fac', 'Factor', 0, 'AUTO'),
            'color': ('Color', 'Color', 1, 'AUTO'),
        },
        output_type=ShaderNodeTexNoiseOutputs,
    )

class ShaderNodeNormalOutputs(typing.NamedTuple):
    'Outputs from Normal: Generate a normal vector and a dot product'
    normal: Socket[Vector]
    dot: Socket[float]

def normal(*, normal: Vector | Socket[Vector] = (0.0, 0.0, 1.0)) -> ShaderNodeNormalOutputs:
    'Generate a normal vector and a dot product'
    return _node_function(
        'ShaderNodeNormal',
        inputs={
            'normal': normal,
        },
        input_sockets={
            'normal': ('Normal', 'Normal', 0, (0.0, 0.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'normal': ('Normal', 'Normal', 0, 'AUTO'),
            'dot': ('Dot', 'Dot', 1, 'AUTO'),
        },
        output_type=ShaderNodeNormalOutputs,
    )

class ShaderNodeNormalMapOutputs(typing.NamedTuple):
    'Outputs from Normal Map: Generate a perturbed normal from an RGB normal map image. Typically used for faking highly detailed surfaces'
    normal: Socket[Vector]

def normal_map(*, strength: float | Socket[float] = 1.0, color: Color | Socket[Color] = (0.5, 0.5, 1.0, 1.0), space: typing.Literal['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD'] = 'TANGENT', uv_map: str = '', convention: typing.Literal['OPENGL', 'DIRECTX'] = 'OPENGL', base: typing.Literal['ORIGINAL', 'DISPLACED'] = 'DISPLACED') -> ShaderNodeNormalMapOutputs:
    'Generate a perturbed normal from an RGB normal map image. Typically used for faking highly detailed surfaces\n\nArgs:\n    space: Space of the input normal\n    uv_map: UV Map for tangent space maps\n    convention: OpenGL or DirectX\n    base: Base surface that the normal map is applied relative to, when displacement is used'
    return _node_function(
        'ShaderNodeNormalMap',
        inputs={
            'strength': strength,
            'color': color,
        },
        input_sockets={
            'strength': ('Strength', 'Strength', 0, 1.0),
            'color': ('Color', 'Color', 1, (0.5, 0.5, 1.0, 1.0)),
        },
        properties={
            'space': space,
            'uv_map': uv_map,
            'convention': convention,
            'base': base,
        },
        output_sockets={
            'normal': ('Normal', 'Normal', 0, 'AUTO'),
        },
        output_type=ShaderNodeNormalMapOutputs,
    )

class ShaderNodeObjectInfoOutputs(typing.NamedTuple):
    'Outputs from Object Info: Retrieve information about the object instance'
    location: Socket[Vector]
    color: Socket[Color]
    alpha: Socket[float]
    object_index: Socket[float]
    material_index: Socket[float]
    random: Socket[float]

def object_info() -> ShaderNodeObjectInfoOutputs:
    'Retrieve information about the object instance'
    return _node_function(
        'ShaderNodeObjectInfo',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'location': ('Location', 'Location', 0, 'AUTO'),
            'color': ('Color', 'Color', 1, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 2, 'AUTO'),
            'object_index': ('Object Index', 'Object Index', 3, 'AUTO'),
            'material_index': ('Material Index', 'Material Index', 4, 'AUTO'),
            'random': ('Random', 'Random', 5, 'AUTO'),
        },
        output_type=ShaderNodeObjectInfoOutputs,
    )

class ShaderNodeParticleInfoOutputs(typing.NamedTuple):
    'Outputs from Particle Info: Retrieve the data of the particle that spawned the object instance, for example to give variation to multiple instances of an object'
    index: Socket[float]
    random: Socket[float]
    age: Socket[float]
    lifetime: Socket[float]
    location: Socket[Vector]
    size: Socket[float]
    velocity: Socket[Vector]
    angular_velocity: Socket[Vector]

def particle_info() -> ShaderNodeParticleInfoOutputs:
    'Retrieve the data of the particle that spawned the object instance, for example to give variation to multiple instances of an object'
    return _node_function(
        'ShaderNodeParticleInfo',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'index': ('Index', 'Index', 0, 'AUTO'),
            'random': ('Random', 'Random', 1, 'AUTO'),
            'age': ('Age', 'Age', 2, 'AUTO'),
            'lifetime': ('Lifetime', 'Lifetime', 3, 'AUTO'),
            'location': ('Location', 'Location', 4, 'AUTO'),
            'size': ('Size', 'Size', 5, 'AUTO'),
            'velocity': ('Velocity', 'Velocity', 6, 'AUTO'),
            'angular_velocity': ('Angular Velocity', 'Angular Velocity', 7, 'AUTO'),
        },
        output_type=ShaderNodeParticleInfoOutputs,
    )

class ShaderNodePointInfoOutputs(typing.NamedTuple):
    'Outputs from Point Info: Retrieve information about points in a point cloud'
    position: Socket[Vector]
    radius: Socket[float]
    random: Socket[float]

def point_info() -> ShaderNodePointInfoOutputs:
    'Retrieve information about points in a point cloud'
    return _node_function(
        'ShaderNodePointInfo',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'position': ('Position', 'Position', 0, 'AUTO'),
            'radius': ('Radius', 'Radius', 1, 'AUTO'),
            'random': ('Random', 'Random', 2, 'AUTO'),
        },
        output_type=ShaderNodePointInfoOutputs,
    )

class ShaderNodeBsdfPrincipledOutputs(typing.NamedTuple):
    'Outputs from Principled BSDF: Physically-based, easy-to-use shader for rendering surface materials, based on the OpenPBR model'
    bsdf: Socket[Shader]

def principled_bsdf(*, base_color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), metallic: float | Socket[float] = 0.0, roughness: float | Socket[float] = 0.5, ior: float | Socket[float] = 1.5, alpha: float | Socket[float] = 1.0, thin_wall: bool | Socket[bool] = False, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), diffuse_roughness: float | Socket[float] = 0.0, subsurface_weight: float | Socket[float] = 0.0, subsurface_radius: Vector | Socket[Vector] = (1.0, 0.20000000298023224, 0.10000000149011612), subsurface_scale: float | Socket[float] = 0.004999999888241291, subsurface_anisotropy: float | Socket[float] = 0.0, specular_ior_level: float | Socket[float] = 0.5, specular_tint: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), anisotropic: float | Socket[float] = 0.0, anisotropic_rotation: float | Socket[float] = 0.0, tangent: Vector | Socket[Vector] = (0.0, 0.0, 0.0), transmission_weight: float | Socket[float] = 0.0, coat_weight: float | Socket[float] = 0.0, coat_roughness: float | Socket[float] = 0.029999999329447746, coat_ior: float | Socket[float] = 1.5, coat_tint: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), coat_normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), sheen_weight: float | Socket[float] = 0.0, sheen_roughness: float | Socket[float] = 0.5, sheen_tint: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), emission_color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), emission_strength: float | Socket[float] = 0.0, thin_film_thickness: float | Socket[float] = 0.0, thin_film_ior: float | Socket[float] = 1.3300000429153442, subsurface_ior: float | Socket[float] = 1.399999976158142, distribution: typing.Literal['GGX', 'MULTI_GGX'] = 'MULTI_GGX', subsurface_method: typing.Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN', 'RANDOM_WALK_LEGACY'] = 'RANDOM_WALK') -> ShaderNodeBsdfPrincipledOutputs:
    'Physically-based, easy-to-use shader for rendering surface materials, based on the OpenPBR model\n\nArgs:\n    distribution: Light scattering distribution on rough surface\n    subsurface_method: Method for rendering subsurface scattering'
    return _node_function(
        'ShaderNodeBsdfPrincipled',
        inputs={
            'base_color': base_color,
            'metallic': metallic,
            'roughness': roughness,
            'ior': ior,
            'alpha': alpha,
            'thin_wall': thin_wall,
            'normal': normal,
            'diffuse_roughness': diffuse_roughness,
            'subsurface_weight': subsurface_weight,
            'subsurface_radius': subsurface_radius,
            'subsurface_scale': subsurface_scale,
            'subsurface_anisotropy': subsurface_anisotropy,
            'specular_ior_level': specular_ior_level,
            'specular_tint': specular_tint,
            'anisotropic': anisotropic,
            'anisotropic_rotation': anisotropic_rotation,
            'tangent': tangent,
            'transmission_weight': transmission_weight,
            'coat_weight': coat_weight,
            'coat_roughness': coat_roughness,
            'coat_ior': coat_ior,
            'coat_tint': coat_tint,
            'coat_normal': coat_normal,
            'sheen_weight': sheen_weight,
            'sheen_roughness': sheen_roughness,
            'sheen_tint': sheen_tint,
            'emission_color': emission_color,
            'emission_strength': emission_strength,
            'thin_film_thickness': thin_film_thickness,
            'thin_film_ior': thin_film_ior,
            'subsurface_ior': subsurface_ior,
        },
        input_sockets={
            'base_color': ('Base Color', 'Base Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'metallic': ('Metallic', 'Metallic', 1, 0.0),
            'roughness': ('Roughness', 'Roughness', 2, 0.5),
            'ior': ('IOR', 'IOR', 3, 1.5),
            'alpha': ('Alpha', 'Alpha', 4, 1.0),
            'thin_wall': ('Thin Wall', 'Thin Wall', 5, False),
            'normal': ('Normal', 'Normal', 6, (0.0, 0.0, 0.0)),
            'diffuse_roughness': ('Diffuse Roughness', 'Diffuse Roughness', 8, 0.0),
            'subsurface_weight': ('Subsurface Weight', 'Subsurface Weight', 9, 0.0),
            'subsurface_radius': ('Subsurface Radius', 'Subsurface Radius', 10, (1.0, 0.20000000298023224, 0.10000000149011612)),
            'subsurface_scale': ('Subsurface Scale', 'Subsurface Scale', 11, 0.004999999888241291),
            'subsurface_anisotropy': ('Subsurface Anisotropy', 'Subsurface Anisotropy', 13, 0.0),
            'specular_ior_level': ('Specular IOR Level', 'Specular IOR Level', 14, 0.5),
            'specular_tint': ('Specular Tint', 'Specular Tint', 15, (1.0, 1.0, 1.0, 1.0)),
            'anisotropic': ('Anisotropic', 'Anisotropic', 16, 0.0),
            'anisotropic_rotation': ('Anisotropic Rotation', 'Anisotropic Rotation', 17, 0.0),
            'tangent': ('Tangent', 'Tangent', 18, (0.0, 0.0, 0.0)),
            'transmission_weight': ('Transmission Weight', 'Transmission Weight', 19, 0.0),
            'coat_weight': ('Coat Weight', 'Coat Weight', 20, 0.0),
            'coat_roughness': ('Coat Roughness', 'Coat Roughness', 21, 0.029999999329447746),
            'coat_ior': ('Coat IOR', 'Coat IOR', 22, 1.5),
            'coat_tint': ('Coat Tint', 'Coat Tint', 23, (1.0, 1.0, 1.0, 1.0)),
            'coat_normal': ('Coat Normal', 'Coat Normal', 24, (0.0, 0.0, 0.0)),
            'sheen_weight': ('Sheen Weight', 'Sheen Weight', 25, 0.0),
            'sheen_roughness': ('Sheen Roughness', 'Sheen Roughness', 26, 0.5),
            'sheen_tint': ('Sheen Tint', 'Sheen Tint', 27, (1.0, 1.0, 1.0, 1.0)),
            'emission_color': ('Emission Color', 'Emission Color', 28, (1.0, 1.0, 1.0, 1.0)),
            'emission_strength': ('Emission Strength', 'Emission Strength', 29, 0.0),
            'thin_film_thickness': ('Thin Film Thickness', 'Thin Film Thickness', 30, 0.0),
            'thin_film_ior': ('Thin Film IOR', 'Thin Film IOR', 31, 1.3300000429153442),
            'subsurface_ior': ('Subsurface IOR', 'Subsurface IOR', 12, 1.399999976158142),
        },
        properties={
            'distribution': distribution,
            'subsurface_method': subsurface_method,
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfPrincipledOutputs,
    )

class ShaderNodeBsdfHairPrincipledOutputs(typing.NamedTuple):
    'Outputs from Principled Hair BSDF: Physically-based, easy-to-use shader for rendering hair and fur'
    bsdf: Socket[Shader]

def principled_hair_bsdf(*, color: Color | Socket[Color] = (0.01751299947500229, 0.005762999877333641, 0.002059000078588724, 1.0), roughness: float | Socket[float] = 0.30000001192092896, radial_roughness: float | Socket[float] = 0.30000001192092896, coat: float | Socket[float] = 0.0, ior: float | Socket[float] = 1.5499999523162842, offset: float | Socket[float] = 0.03490658476948738, random_roughness: float | Socket[float] = 0.0, random: float | Socket[float] = 0.0, aspect_ratio: float | Socket[float] = 0.8500000238418579, reflection: float | Socket[float] = 1.0, transmission: float | Socket[float] = 1.0, secondary_reflection: float | Socket[float] = 1.0, absorption_coefficient: Vector | Socket[Vector] = (0.24553099274635315, 0.5199999809265137, 1.3650000095367432), melanin: float | Socket[float] = 0.800000011920929, melanin_redness: float | Socket[float] = 1.0, tint: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), random_color: float | Socket[float] = 0.0, model: typing.Literal['CHIANG', 'HUANG'] = 'CHIANG', parametrization: typing.Literal['ABSORPTION', 'MELANIN', 'COLOR'] = 'COLOR') -> ShaderNodeBsdfHairPrincipledOutputs:
    "Physically-based, easy-to-use shader for rendering hair and fur\n\nArgs:\n    model: Select from Chiang or Huang model\n    parametrization: Select the shader's color parametrization"
    return _node_function(
        'ShaderNodeBsdfHairPrincipled',
        inputs={
            'color': color,
            'roughness': roughness,
            'radial_roughness': radial_roughness,
            'coat': coat,
            'ior': ior,
            'offset': offset,
            'random_roughness': random_roughness,
            'random': random,
            'aspect_ratio': aspect_ratio,
            'reflection': reflection,
            'transmission': transmission,
            'secondary_reflection': secondary_reflection,
            'absorption_coefficient': absorption_coefficient,
            'melanin': melanin,
            'melanin_redness': melanin_redness,
            'tint': tint,
            'random_color': random_color,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.01751299947500229, 0.005762999877333641, 0.002059000078588724, 1.0)),
            'roughness': ('Roughness', 'Roughness', 6, 0.30000001192092896),
            'radial_roughness': ('Radial Roughness', 'Radial Roughness', 7, 0.30000001192092896),
            'coat': ('Coat', 'Coat', 8, 0.0),
            'ior': ('IOR', 'IOR', 9, 1.5499999523162842),
            'offset': ('Offset', 'Offset', 10, 0.03490658476948738),
            'random_roughness': ('Random Roughness', 'Random Roughness', 12, 0.0),
            'random': ('Random', 'Random', 13, 0.0),
            'aspect_ratio': ('Aspect Ratio', 'Aspect Ratio', 5, 0.8500000238418579),
            'reflection': ('R lobe', 'Reflection', 15, 1.0),
            'transmission': ('TT lobe', 'Transmission', 16, 1.0),
            'secondary_reflection': ('TRT lobe', 'Secondary Reflection', 17, 1.0),
            'absorption_coefficient': ('Absorption Coefficient', 'Absorption Coefficient', 4, (0.24553099274635315, 0.5199999809265137, 1.3650000095367432)),
            'melanin': ('Melanin', 'Melanin', 1, 0.800000011920929),
            'melanin_redness': ('Melanin Redness', 'Melanin Redness', 2, 1.0),
            'tint': ('Tint', 'Tint', 3, (1.0, 1.0, 1.0, 1.0)),
            'random_color': ('Random Color', 'Random Color', 11, 0.0),
        },
        properties={
            'model': model,
            'parametrization': parametrization,
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfHairPrincipledOutputs,
    )

class ShaderNodeVolumePrincipledOutputs(typing.NamedTuple):
    'Outputs from Principled Volume: Combine all volume shading components into a single easy to use node'
    volume: Socket[Shader]

def principled_volume(*, color: Color | Socket[Color] = (0.5, 0.5, 0.5, 1.0), color_attribute: str | Socket[str] = '', density: float | Socket[float] = 1.0, density_attribute: str | Socket[str] = 'density', anisotropy: float | Socket[float] = 0.0, absorption_color: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), emission_strength: float | Socket[float] = 0.0, emission_color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), blackbody_intensity: float | Socket[float] = 0.0, blackbody_tint: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), temperature: float | Socket[float] = 1000.0, temperature_attribute: str | Socket[str] = 'temperature') -> ShaderNodeVolumePrincipledOutputs:
    'Combine all volume shading components into a single easy to use node'
    return _node_function(
        'ShaderNodeVolumePrincipled',
        inputs={
            'color': color,
            'color_attribute': color_attribute,
            'density': density,
            'density_attribute': density_attribute,
            'anisotropy': anisotropy,
            'absorption_color': absorption_color,
            'emission_strength': emission_strength,
            'emission_color': emission_color,
            'blackbody_intensity': blackbody_intensity,
            'blackbody_tint': blackbody_tint,
            'temperature': temperature,
            'temperature_attribute': temperature_attribute,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.5, 0.5, 0.5, 1.0)),
            'color_attribute': ('Color Attribute', 'Color Attribute', 1, ''),
            'density': ('Density', 'Density', 2, 1.0),
            'density_attribute': ('Density Attribute', 'Density Attribute', 3, 'density'),
            'anisotropy': ('Anisotropy', 'Anisotropy', 4, 0.0),
            'absorption_color': ('Absorption Color', 'Absorption Color', 5, (0.0, 0.0, 0.0, 1.0)),
            'emission_strength': ('Emission Strength', 'Emission Strength', 6, 0.0),
            'emission_color': ('Emission Color', 'Emission Color', 7, (1.0, 1.0, 1.0, 1.0)),
            'blackbody_intensity': ('Blackbody Intensity', 'Blackbody Intensity', 8, 0.0),
            'blackbody_tint': ('Blackbody Tint', 'Blackbody Tint', 9, (1.0, 1.0, 1.0, 1.0)),
            'temperature': ('Temperature', 'Temperature', 10, 1000.0),
            'temperature_attribute': ('Temperature Attribute', 'Temperature Attribute', 11, 'temperature'),
        },
        properties={
        },
        output_sockets={
            'volume': ('Volume', 'Volume', 0, 'AUTO'),
        },
        output_type=ShaderNodeVolumePrincipledOutputs,
    )

class ShaderNodeRadialTilingOutputs(typing.NamedTuple):
    'Outputs from Radial Tiling: Transform Coordinate System for Radial Tiling'
    segment_coordinates: Socket[Vector]
    segment_id: Socket[float]
    segment_width: Socket[float]
    segment_rotation: Socket[float]

def radial_tiling(*, vector: Vector2 | Socket[Vector2] = (0.0, 0.0), sides: float | Socket[float] = 5.0, roundness: float | Socket[float] = 0.0, normalize: bool = False) -> ShaderNodeRadialTilingOutputs:
    "Transform Coordinate System for Radial Tiling\n\nArgs:\n    normalize: Normalize the X coordinate of the Segment Coordinates output to a [0, 1] interval and offset the Y coordinate into a [0, infinity) interval. When checked, the textures are stretched to fit into each angular segment. When not checked, the parts of the textures that don't fit into each angular segment are cropped"
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

class ShaderNodeBsdfRayPortalOutputs(typing.NamedTuple):
    'Outputs from Ray Portal BSDF: Continue tracing from an arbitrary new position and in a new direction'
    bsdf: Socket[Shader]

def ray_portal_bsdf(*, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), position: Vector | Socket[Vector] = (0.0, 0.0, 0.0), direction: Vector | Socket[Vector] = (0.0, 0.0, 0.0)) -> ShaderNodeBsdfRayPortalOutputs:
    'Continue tracing from an arbitrary new position and in a new direction'
    return _node_function(
        'ShaderNodeBsdfRayPortal',
        inputs={
            'color': color,
            'position': position,
            'direction': direction,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 1.0, 1.0, 1.0)),
            'position': ('Position', 'Position', 1, (0.0, 0.0, 0.0)),
            'direction': ('Direction', 'Direction', 2, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfRayPortalOutputs,
    )

class ShaderNodeRaycastOutputs(ItemOutputs):
    'Outputs from Raycast: Cast rays and retrieve information from the hit point'
    is_hit: Socket[float]
    self_hit: Socket[float]
    hit_distance: Socket[float]
    hit_position: Socket[Vector]
    hit_normal: Socket[Vector]

def raycast(*, position: Vector | Socket[Vector] = (0.0, 0.0, 0.0), direction: Vector | Socket[Vector] = (0.0, 0.0, 0.0), length: float | Socket[float] = 1.0, only_local: bool = False, **items: typing.Any) -> ShaderNodeRaycastOutputs:
    'Cast rays and retrieve information from the hit point\n\nArgs:\n    only_local: Only raycast against the object itself\n    items: Items to add, by name; each socket type is inferred from its value. Their outputs are available by name on the result.'
    return _node_function(
        'ShaderNodeRaycast',
        inputs={
            'position': position,
            'direction': direction,
            'length': length,
        },
        input_sockets={
            'position': ('Position', 'Position', 0, (0.0, 0.0, 0.0)),
            'direction': ('Direction', 'Direction', 1, (0.0, 0.0, 0.0)),
            'length': ('Length', 'Length', 2, 1.0),
        },
        properties={
            'only_local': only_local,
        },
        output_sockets={
            'is_hit': ('Is Hit', 'Is Hit', 0, 'AUTO'),
            'self_hit': ('Self Hit', 'Self Hit', 1, 'AUTO'),
            'hit_distance': ('Hit Distance', 'Hit Distance', 2, 'AUTO'),
            'hit_position': ('Hit Position', 'Hit Position', 3, 'AUTO'),
            'hit_normal': ('Hit Normal', 'Hit Normal', 4, 'AUTO'),
        },
        output_type=ShaderNodeRaycastOutputs,
        item_collections=(
            ('sample_attribute_items', 'values', items),
        ),
    )

class ShaderNodeBsdfRefractionOutputs(typing.NamedTuple):
    'Outputs from Refraction BSDF: Glossy refraction with sharp or microfacet distribution, typically used for materials that transmit light'
    bsdf: Socket[Shader]

def refraction_bsdf(*, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), roughness: float | Socket[float] = 0.0, ior: float | Socket[float] = 1.4500000476837158, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), distribution: typing.Literal['BECKMANN', 'GGX'] = 'BECKMANN') -> ShaderNodeBsdfRefractionOutputs:
    'Glossy refraction with sharp or microfacet distribution, typically used for materials that transmit light\n\nArgs:\n    distribution: Light scattering distribution on rough surface'
    return _node_function(
        'ShaderNodeBsdfRefraction',
        inputs={
            'color': color,
            'roughness': roughness,
            'ior': ior,
            'normal': normal,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 1.0, 1.0, 1.0)),
            'roughness': ('Roughness', 'Roughness', 1, 0.0),
            'ior': ('IOR', 'IOR', 2, 1.4500000476837158),
            'normal': ('Normal', 'Normal', 3, (0.0, 0.0, 0.0)),
        },
        properties={
            'distribution': distribution,
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfRefractionOutputs,
    )

class ShaderNodeRGBCurveOutputs(typing.NamedTuple):
    'Outputs from RGB Curves: Apply color corrections for each color channel'
    color: Socket[Color]

def rgb_curves(*, factor: float | Socket[float] = 1.0, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0)) -> ShaderNodeRGBCurveOutputs:
    'Apply color corrections for each color channel'
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

class ShaderNodeRGBToBWOutputs(typing.NamedTuple):
    "Outputs from RGB to BW: Convert a color's luminance to a grayscale value"
    val: Socket[float]

def rgb_to_bw(*, color: Color | Socket[Color] = (0.5, 0.5, 0.5, 1.0)) -> ShaderNodeRGBToBWOutputs:
    "Convert a color's luminance to a grayscale value"
    return _node_function(
        'ShaderNodeRGBToBW',
        inputs={
            'color': color,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.5, 0.5, 0.5, 1.0)),
        },
        properties={
        },
        output_sockets={
            'val': ('Val', 'Val', 0, 'AUTO'),
        },
        output_type=ShaderNodeRGBToBWOutputs,
    )

class GeometryNodeInputSceneTimeOutputs(typing.NamedTuple):
    "Outputs from Scene Time: Retrieve the current time in the scene's animation in units of seconds or frames"
    seconds: Socket[float]
    frame: Socket[float]

def scene_time() -> GeometryNodeInputSceneTimeOutputs:
    "Retrieve the current time in the scene's animation in units of seconds or frames"
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

def script(*, script: bpy.types.Text | None = None, filepath: str = '', mode: typing.Literal['INTERNAL', 'EXTERNAL'] = 'INTERNAL', use_auto_update: bool = False, bytecode: str = '', bytecode_hash: str = '') -> None:
    'Generate an OSL shader from a file or text data-block.\nNote: OSL shaders are not supported on all GPU backends\n\nArgs:\n    script: Internal shader script to define the shader\n    filepath: Shader script path\n    use_auto_update: Automatically update the shader when the .osl file changes (external scripts only)\n    bytecode: Compile bytecode for shader script node\n    bytecode_hash: Hash of compile bytecode, for quick equality checking'
    return _node_function(
        'ShaderNodeScript',
        inputs={
        },
        input_sockets={
        },
        properties={
            'script': script,
            'filepath': filepath,
            'mode': mode,
            'use_auto_update': use_auto_update,
            'bytecode': bytecode,
            'bytecode_hash': bytecode_hash,
        },
        output_sockets={
        },
        output_type=None,
    )

class NodeSeparateBundleOutputs(ItemOutputs):
    'Outputs from Separate Bundle: Split a bundle into multiple sockets.'

def separate_bundle(*, bundle: Bundle | Socket[Bundle] | None = None, define_signature: bool = False, items: typing.Mapping[str, typing.Any] | None = None) -> NodeSeparateBundleOutputs:
    'Split a bundle into multiple sockets.\n\nArgs:\n    define_signature: This node defines a bundle signature that should be used by other nodes\n    items: Items to add, mapping each name to its type (float, Vector, Geometry, ...). Their outputs are available by name on the result.'
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

class ShaderNodeSeparateColorOutputs(typing.NamedTuple):
    'Outputs from Separate Color: Split a color into its individual components using multiple models'
    red: Socket[float]
    green: Socket[float]
    blue: Socket[float]

def separate_color(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), mode: typing.Literal['RGB', 'HSV', 'HSL'] = 'RGB') -> ShaderNodeSeparateColorOutputs:
    'Split a color into its individual components using multiple models\n\nArgs:\n    mode: Mode of color processing'
    return _node_function(
        'ShaderNodeSeparateColor',
        inputs={
            'color': color,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
        },
        properties={
            'mode': mode,
        },
        output_sockets={
            'red': ('Red', 'Red', 0, 'AUTO'),
            'green': ('Green', 'Green', 1, 'AUTO'),
            'blue': ('Blue', 'Blue', 2, 'AUTO'),
        },
        output_type=ShaderNodeSeparateColorOutputs,
    )

class ShaderNodeSeparateXYZOutputs(typing.NamedTuple):
    'Outputs from Separate XYZ: Split a vector into its X, Y, and Z components'
    x: Socket[float]
    y: Socket[float]
    z: Socket[float]

def separate_xyz(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0)) -> ShaderNodeSeparateXYZOutputs:
    'Split a vector into its X, Y, and Z components'
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

class ShaderNodeShaderToRGBOutputs(typing.NamedTuple):
    'Outputs from Shader to RGB: Convert rendering effect (such as light and shadow) to color. Typically used for non-photorealistic rendering, to apply additional effects on the output of BSDFs.\nNote: only supported in EEVEE'
    color: Socket[Color]
    alpha: Socket[float]

def shader_to_rgb(*, shader: Shader | Socket[Shader] | None = None) -> ShaderNodeShaderToRGBOutputs:
    'Convert rendering effect (such as light and shadow) to color. Typically used for non-photorealistic rendering, to apply additional effects on the output of BSDFs.\nNote: only supported in EEVEE'
    return _node_function(
        'ShaderNodeShaderToRGB',
        inputs={
            'shader': shader,
        },
        input_sockets={
            'shader': ('Shader', 'Shader', 0, None),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 1, 'AUTO'),
        },
        output_type=ShaderNodeShaderToRGBOutputs,
    )

class ShaderNodeBsdfSheenOutputs(typing.NamedTuple):
    'Outputs from Sheen BSDF: Reflection for materials such as cloth.\nTypically mixed with other shaders (such as a Diffuse Shader) and is not particularly useful on its own'
    bsdf: Socket[Shader]

def sheen_bsdf(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), roughness: float | Socket[float] = 0.5, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), distribution: typing.Literal['ASHIKHMIN', 'MICROFIBER'] = 'MICROFIBER') -> ShaderNodeBsdfSheenOutputs:
    'Reflection for materials such as cloth.\nTypically mixed with other shaders (such as a Diffuse Shader) and is not particularly useful on its own\n\nArgs:\n    distribution: Sheen shading model'
    return _node_function(
        'ShaderNodeBsdfSheen',
        inputs={
            'color': color,
            'roughness': roughness,
            'normal': normal,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'roughness': ('Roughness', 'Roughness', 1, 0.5),
            'normal': ('Normal', 'Normal', 2, (0.0, 0.0, 0.0)),
        },
        properties={
            'distribution': distribution,
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfSheenOutputs,
    )

class ShaderNodeTexSkyOutputs(typing.NamedTuple):
    'Outputs from Sky Texture: Generate a procedural sky texture'
    color: Socket[Color]

def sky_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), sky_type: typing.Literal['SINGLE_SCATTERING', 'MULTIPLE_SCATTERING', 'PREETHAM', 'HOSEK_WILKIE'] = 'MULTIPLE_SCATTERING', sun_disc: bool = True, sun_size: float = 0.009512044489383698, sun_intensity: float = 1.0, sun_elevation: float = 0.2617993950843811, sun_rotation: float = 0.0, altitude: float = 100.0, air_density: float = 1.0, aerosol_density: float = 1.0, ozone_density: float = 1.0, sun_direction: Vector = (0.0, 0.0, 1.0), turbidity: float = 2.200000047683716, ground_albedo: float = 0.30000001192092896) -> ShaderNodeTexSkyOutputs:
    'Generate a procedural sky texture\n\nArgs:\n    sky_type: Which sky model should be used\n    sun_disc: Include the sun itself in the output\n    sun_size: Size of sun disc\n    sun_intensity: Strength of Sun\n    sun_elevation: Sun angle from horizon\n    sun_rotation: Rotation of sun around zenith\n    altitude: Height from sea level\n    air_density: Density of air molecules.\n0 means no air, 1 means urban city air\n    aerosol_density: Density of dust, pollution and water droplets.\n0 means no aerosols, 1 means urban city aerosols\n    ozone_density: Density of ozone layer.\n0 means no ozone, 1 means urban city ozone\n    sun_direction: Direction from where the sun is shining\n    turbidity: Atmospheric turbidity\n    ground_albedo: Ground color that is subtly reflected in the sky'
    return _node_function(
        'ShaderNodeTexSky',
        inputs={
            'vector': vector,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.0, 0.0, 0.0)),
        },
        properties={
            'sky_type': sky_type,
            'sun_disc': sun_disc,
            'sun_size': sun_size,
            'sun_intensity': sun_intensity,
            'sun_elevation': sun_elevation,
            'sun_rotation': sun_rotation,
            'altitude': altitude,
            'air_density': air_density,
            'aerosol_density': aerosol_density,
            'ozone_density': ozone_density,
            'sun_direction': sun_direction,
            'turbidity': turbidity,
            'ground_albedo': ground_albedo,
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeTexSkyOutputs,
    )

class ShaderNodeEeveeSpecularOutputs(typing.NamedTuple):
    'Outputs from Specular BSDF: Similar to the Principled BSDF node but uses the specular workflow instead of metallic, which functions by specifying the facing (along normal) reflection color. Energy is not conserved, so the result may not be physically accurate'
    bsdf: Socket[Shader]

def specular_bsdf(*, base_color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), specular: Color | Socket[Color] = (0.029999999329447746, 0.029999999329447746, 0.029999999329447746, 1.0), roughness: float | Socket[float] = 0.20000000298023224, emissive_color: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), transparency: float | Socket[float] = 0.0, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), clear_coat: float | Socket[float] = 0.0, clear_coat_roughness: float | Socket[float] = 0.0, clear_coat_normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0)) -> ShaderNodeEeveeSpecularOutputs:
    'Similar to the Principled BSDF node but uses the specular workflow instead of metallic, which functions by specifying the facing (along normal) reflection color. Energy is not conserved, so the result may not be physically accurate'
    return _node_function(
        'ShaderNodeEeveeSpecular',
        inputs={
            'base_color': base_color,
            'specular': specular,
            'roughness': roughness,
            'emissive_color': emissive_color,
            'transparency': transparency,
            'normal': normal,
            'clear_coat': clear_coat,
            'clear_coat_roughness': clear_coat_roughness,
            'clear_coat_normal': clear_coat_normal,
        },
        input_sockets={
            'base_color': ('Base Color', 'Base Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'specular': ('Specular', 'Specular', 1, (0.029999999329447746, 0.029999999329447746, 0.029999999329447746, 1.0)),
            'roughness': ('Roughness', 'Roughness', 2, 0.20000000298023224),
            'emissive_color': ('Emissive Color', 'Emissive Color', 3, (0.0, 0.0, 0.0, 1.0)),
            'transparency': ('Transparency', 'Transparency', 4, 0.0),
            'normal': ('Normal', 'Normal', 5, (0.0, 0.0, 0.0)),
            'clear_coat': ('Clear Coat', 'Clear Coat', 6, 0.0),
            'clear_coat_roughness': ('Clear Coat Roughness', 'Clear Coat Roughness', 7, 0.0),
            'clear_coat_normal': ('Clear Coat Normal', 'Clear Coat Normal', 8, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeEeveeSpecularOutputs,
    )

class ShaderNodeSqueezeOutputs(typing.NamedTuple):
    'Outputs from Squeeze Value (Legacy): Deprecated'
    value: Socket[float]

def squeeze_value_legacy(*, value: float | Socket[float] = 0.0, width: float | Socket[float] = 1.0, center: float | Socket[float] = 0.0) -> ShaderNodeSqueezeOutputs:
    'Deprecated'
    return _node_function(
        'ShaderNodeSqueeze',
        inputs={
            'value': value,
            'width': width,
            'center': center,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 0.0),
            'width': ('Width', 'Width', 1, 1.0),
            'center': ('Center', 'Center', 2, 0.0),
        },
        properties={
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=ShaderNodeSqueezeOutputs,
    )

class ShaderNodeSubsurfaceScatteringOutputs(typing.NamedTuple):
    'Outputs from Subsurface Scattering: Subsurface multiple scattering shader to simulate light entering the surface and bouncing internally.\nTypically used for materials such as skin, wax, marble or milk'
    bssrdf: Socket[Shader]

def subsurface_scattering(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), scale: float | Socket[float] = 0.004999999888241291, radius: Vector | Socket[Vector] = (1.0, 0.20000000298023224, 0.10000000149011612), ior: float | Socket[float] = 1.399999976158142, roughness: float | Socket[float] = 1.0, anisotropy: float | Socket[float] = 0.0, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), falloff: typing.Literal['BURLEY', 'RANDOM_WALK', 'RANDOM_WALK_SKIN', 'RANDOM_WALK_LEGACY'] = 'RANDOM_WALK') -> ShaderNodeSubsurfaceScatteringOutputs:
    'Subsurface multiple scattering shader to simulate light entering the surface and bouncing internally.\nTypically used for materials such as skin, wax, marble or milk\n\nArgs:\n    falloff: Method for rendering subsurface scattering'
    return _node_function(
        'ShaderNodeSubsurfaceScattering',
        inputs={
            'color': color,
            'scale': scale,
            'radius': radius,
            'ior': ior,
            'roughness': roughness,
            'anisotropy': anisotropy,
            'normal': normal,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'scale': ('Scale', 'Scale', 1, 0.004999999888241291),
            'radius': ('Radius', 'Radius', 2, (1.0, 0.20000000298023224, 0.10000000149011612)),
            'ior': ('IOR', 'IOR', 3, 1.399999976158142),
            'roughness': ('Roughness', 'Roughness', 4, 1.0),
            'anisotropy': ('Anisotropy', 'Anisotropy', 5, 0.0),
            'normal': ('Normal', 'Normal', 6, (0.0, 0.0, 0.0)),
        },
        properties={
            'falloff': falloff,
        },
        output_sockets={
            'bssrdf': ('BSSRDF', 'BSSRDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeSubsurfaceScatteringOutputs,
    )

class ShaderNodeTangentOutputs(typing.NamedTuple):
    'Outputs from Tangent: Generate a tangent direction for the Anisotropic BSDF'
    tangent: Socket[Vector]

def tangent(*, direction_type: typing.Literal['RADIAL', 'UV_MAP'] = 'RADIAL', axis: typing.Literal['X', 'Y', 'Z'] = 'Z', uv_map: str = '') -> ShaderNodeTangentOutputs:
    'Generate a tangent direction for the Anisotropic BSDF\n\nArgs:\n    direction_type: Method to use for the tangent\n    axis: Axis for radial tangents\n    uv_map: UV Map for tangent generated from UV'
    return _node_function(
        'ShaderNodeTangent',
        inputs={
        },
        input_sockets={
        },
        properties={
            'direction_type': direction_type,
            'axis': axis,
            'uv_map': uv_map,
        },
        output_sockets={
            'tangent': ('Tangent', 'Tangent', 0, 'AUTO'),
        },
        output_type=ShaderNodeTangentOutputs,
    )

class ShaderNodeTexCoordOutputs(typing.NamedTuple):
    'Outputs from Texture Coordinate: Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes'
    generated: Socket[Vector]
    normal: Socket[Vector]
    uv: Socket[Vector]
    object: Socket[Vector]
    camera: Socket[Vector]
    window: Socket[Vector]
    reflection: Socket[Vector]

def texture_coordinate(*, object: bpy.types.Object | None = None, from_instancer: bool = False) -> ShaderNodeTexCoordOutputs:
    'Retrieve multiple types of texture coordinates.\nTypically used as inputs for texture nodes\n\nArgs:\n    object: Use coordinates from this object (for object texture coordinates output)\n    from_instancer: Use the parent of the instance object if possible'
    return _node_function(
        'ShaderNodeTexCoord',
        inputs={
        },
        input_sockets={
        },
        properties={
            'object': object,
            'from_instancer': from_instancer,
        },
        output_sockets={
            'generated': ('Generated', 'Generated', 0, 'AUTO'),
            'normal': ('Normal', 'Normal', 1, 'AUTO'),
            'uv': ('UV', 'UV', 2, 'AUTO'),
            'object': ('Object', 'Object', 3, 'AUTO'),
            'camera': ('Camera', 'Camera', 4, 'AUTO'),
            'window': ('Window', 'Window', 5, 'AUTO'),
            'reflection': ('Reflection', 'Reflection', 6, 'AUTO'),
        },
        output_type=ShaderNodeTexCoordOutputs,
    )

class ShaderNodeBsdfToonOutputs(typing.NamedTuple):
    'Outputs from Toon BSDF: Diffuse and Glossy shaders with cartoon light effects'
    bsdf: Socket[Shader]

def toon_bsdf(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), size: float | Socket[float] = 0.5, smooth: float | Socket[float] = 0.0, normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), component: typing.Literal['DIFFUSE', 'GLOSSY'] = 'DIFFUSE') -> ShaderNodeBsdfToonOutputs:
    'Diffuse and Glossy shaders with cartoon light effects\n\nArgs:\n    component: Toon BSDF component to use'
    return _node_function(
        'ShaderNodeBsdfToon',
        inputs={
            'color': color,
            'size': size,
            'smooth': smooth,
            'normal': normal,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'size': ('Size', 'Size', 1, 0.5),
            'smooth': ('Smooth', 'Smooth', 2, 0.0),
            'normal': ('Normal', 'Normal', 3, (0.0, 0.0, 0.0)),
        },
        properties={
            'component': component,
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfToonOutputs,
    )

class ShaderNodeBsdfTranslucentOutputs(typing.NamedTuple):
    'Outputs from Translucent BSDF: Lambertian diffuse transmission'
    bsdf: Socket[Shader]

def translucent_bsdf(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0)) -> ShaderNodeBsdfTranslucentOutputs:
    'Lambertian diffuse transmission'
    return _node_function(
        'ShaderNodeBsdfTranslucent',
        inputs={
            'color': color,
            'normal': normal,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'normal': ('Normal', 'Normal', 1, (0.0, 0.0, 0.0)),
        },
        properties={
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfTranslucentOutputs,
    )

class ShaderNodeBsdfTransparentOutputs(typing.NamedTuple):
    'Outputs from Transparent BSDF: Transparency without refraction, passing straight through the surface as if there were no geometry'
    bsdf: Socket[Shader]

def transparent_bsdf(*, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0)) -> ShaderNodeBsdfTransparentOutputs:
    'Transparency without refraction, passing straight through the surface as if there were no geometry'
    return _node_function(
        'ShaderNodeBsdfTransparent',
        inputs={
            'color': color,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 1.0, 1.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'bsdf': ('BSDF', 'BSDF', 0, 'AUTO'),
        },
        output_type=ShaderNodeBsdfTransparentOutputs,
    )

class ShaderNodeUVAlongStrokeOutputs(typing.NamedTuple):
    'Outputs from UV Along Stroke: UV coordinates that map a texture along the stroke length'
    uv: Socket[Vector]

def uv_along_stroke(*, use_tips: bool = False) -> ShaderNodeUVAlongStrokeOutputs:
    'UV coordinates that map a texture along the stroke length\n\nArgs:\n    use_tips: Lower half of the texture is for tips of the stroke'
    return _node_function(
        'ShaderNodeUVAlongStroke',
        inputs={
        },
        input_sockets={
        },
        properties={
            'use_tips': use_tips,
        },
        output_sockets={
            'uv': ('UV', 'UV', 0, 'AUTO'),
        },
        output_type=ShaderNodeUVAlongStrokeOutputs,
    )

class ShaderNodeUVMapOutputs(typing.NamedTuple):
    'Outputs from UV Map: Retrieve a UV map from the geometry, or the default fallback if none is specified'
    uv: Socket[Vector]

def uv_map(*, from_instancer: bool = False, uv_map: str = '') -> ShaderNodeUVMapOutputs:
    'Retrieve a UV map from the geometry, or the default fallback if none is specified\n\nArgs:\n    from_instancer: Use the parent of the instance object if possible\n    uv_map: UV coordinates to be used for mapping'
    return _node_function(
        'ShaderNodeUVMap',
        inputs={
        },
        input_sockets={
        },
        properties={
            'from_instancer': from_instancer,
            'uv_map': uv_map,
        },
        output_sockets={
            'uv': ('UV', 'UV', 0, 'AUTO'),
        },
        output_type=ShaderNodeUVMapOutputs,
    )

class ShaderNodeValueOutputs(typing.NamedTuple):
    'Outputs from Value: Input numerical values to other nodes in the tree'
    value: Socket[float]

def value() -> ShaderNodeValueOutputs:
    'Input numerical values to other nodes in the tree'
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

class FunctionNodeInputVectorOutputs(typing.NamedTuple):
    'Outputs from Vector: Provide a vector value that can be connected to other nodes in the tree'
    vector: Socket[Vector]

def vector(*, vector: Vector4 = (0.0, 0.0, 0.0), vector_dimensions: int = 3) -> FunctionNodeInputVectorOutputs:
    'Provide a vector value that can be connected to other nodes in the tree\n\nArgs:\n    vector_dimensions: Dimensions of the vector socket'
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
    'Outputs from Vector Curves: Map input vector components with curves'
    vector: Socket[Vector]

def vector_curves(*, factor: float | Socket[float] = 1.0, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0)) -> ShaderNodeVectorCurveOutputs:
    'Map input vector components with curves'
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

class ShaderNodeVectorDisplacementOutputs(typing.NamedTuple):
    'Outputs from Vector Displacement: Displace the surface along an arbitrary direction'
    displacement: Socket[Vector]

def vector_displacement(*, vector: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), midlevel: float | Socket[float] = 0.0, scale: float | Socket[float] = 0.009999999776482582, space: typing.Literal['TANGENT', 'OBJECT', 'WORLD'] = 'TANGENT') -> ShaderNodeVectorDisplacementOutputs:
    'Displace the surface along an arbitrary direction\n\nArgs:\n    space: Space of the input height'
    return _node_function(
        'ShaderNodeVectorDisplacement',
        inputs={
            'vector': vector,
            'midlevel': midlevel,
            'scale': scale,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'midlevel': ('Midlevel', 'Midlevel', 1, 0.0),
            'scale': ('Scale', 'Scale', 2, 0.009999999776482582),
        },
        properties={
            'space': space,
        },
        output_sockets={
            'displacement': ('Displacement', 'Displacement', 0, 'AUTO'),
        },
        output_type=ShaderNodeVectorDisplacementOutputs,
    )

class ShaderNodeVectorMathOutputs(typing.NamedTuple):
    'Outputs from Vector Math: Perform vector math operation'
    vector: Socket[Vector]
    value: Socket[float]

def vector_math(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), vector_2: Vector | Socket[Vector] = (0.0, 0.0, 0.0), vector_3: Vector | Socket[Vector] = (0.0, 0.0, 0.0), scale: float | Socket[float] = 1.0, operation: typing.Literal['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'POWER', 'SIGN', 'MINIMUM', 'MAXIMUM', 'ROUND', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT'] = 'ADD') -> ShaderNodeVectorMathOutputs:
    'Perform vector math operation'
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
    'Outputs from Vector Rotate: Rotate a vector around a pivot point (center)'
    vector: Socket[Vector]

def vector_rotate(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), center: Vector | Socket[Vector] = (0.0, 0.0, 0.0), axis: Vector | Socket[Vector] = (0.0, 0.0, 1.0), angle: float | Socket[float] = 0.0, rotation: Vector | Socket[Vector] = (0.0, 0.0, 0.0), rotation_type: typing.Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ'] = 'AXIS_ANGLE', invert: bool = False) -> ShaderNodeVectorRotateOutputs:
    'Rotate a vector around a pivot point (center)\n\nArgs:\n    rotation_type: Type of angle input\n    invert: Invert the rotation angle'
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

class ShaderNodeVectorTransformOutputs(typing.NamedTuple):
    'Outputs from Vector Transform: Convert a vector, point, or normal between world, camera, and object coordinate space'
    vector: Socket[Vector]

def vector_transform(*, vector: Vector | Socket[Vector] = (0.5, 0.5, 0.5), vector_type: typing.Literal['POINT', 'VECTOR', 'NORMAL'] = 'VECTOR', convert_from: typing.Literal['WORLD', 'OBJECT', 'CAMERA'] = 'WORLD', convert_to: typing.Literal['WORLD', 'OBJECT', 'CAMERA'] = 'OBJECT') -> ShaderNodeVectorTransformOutputs:
    'Convert a vector, point, or normal between world, camera, and object coordinate space\n\nArgs:\n    convert_from: Space to convert from\n    convert_to: Space to convert to'
    return _node_function(
        'ShaderNodeVectorTransform',
        inputs={
            'vector': vector,
        },
        input_sockets={
            'vector': ('Vector', 'Vector', 0, (0.5, 0.5, 0.5)),
        },
        properties={
            'vector_type': vector_type,
            'convert_from': convert_from,
            'convert_to': convert_to,
        },
        output_sockets={
            'vector': ('Vector', 'Vector', 0, 'AUTO'),
        },
        output_type=ShaderNodeVectorTransformOutputs,
    )

class ShaderNodeVolumeAbsorptionOutputs(typing.NamedTuple):
    'Outputs from Volume Absorption: Absorb light as it passes through the volume'
    volume: Socket[Shader]

def volume_absorption(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), density: float | Socket[float] = 1.0) -> ShaderNodeVolumeAbsorptionOutputs:
    'Absorb light as it passes through the volume'
    return _node_function(
        'ShaderNodeVolumeAbsorption',
        inputs={
            'color': color,
            'density': density,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'density': ('Density', 'Density', 1, 1.0),
        },
        properties={
        },
        output_sockets={
            'volume': ('Volume', 'Volume', 0, 'AUTO'),
        },
        output_type=ShaderNodeVolumeAbsorptionOutputs,
    )

class ShaderNodeVolumeCoefficientsOutputs(typing.NamedTuple):
    'Outputs from Volume Coefficients: Model all three physical processes in a volume, represented by their coefficients'
    volume: Socket[Shader]

def volume_coefficients(*, absorption_coefficients: Vector | Socket[Vector] = (1.0, 1.0, 1.0), scatter_coefficients: Vector | Socket[Vector] = (1.0, 1.0, 1.0), anisotropy: float | Socket[float] = 0.0, emission_coefficients: Vector | Socket[Vector] = (0.0, 0.0, 0.0), ior: float | Socket[float] = 1.3300000429153442, backscatter: float | Socket[float] = 0.10000000149011612, alpha: float | Socket[float] = 0.5, diameter: float | Socket[float] = 20.0, phase: typing.Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'] = 'HENYEY_GREENSTEIN') -> ShaderNodeVolumeCoefficientsOutputs:
    'Model all three physical processes in a volume, represented by their coefficients\n\nArgs:\n    phase: Phase function for the scattered light'
    return _node_function(
        'ShaderNodeVolumeCoefficients',
        inputs={
            'absorption_coefficients': absorption_coefficients,
            'scatter_coefficients': scatter_coefficients,
            'anisotropy': anisotropy,
            'emission_coefficients': emission_coefficients,
            'ior': ior,
            'backscatter': backscatter,
            'alpha': alpha,
            'diameter': diameter,
        },
        input_sockets={
            'absorption_coefficients': ('Absorption Coefficients', 'Absorption Coefficients', 1, (1.0, 1.0, 1.0)),
            'scatter_coefficients': ('Scatter Coefficients', 'Scatter Coefficients', 2, (1.0, 1.0, 1.0)),
            'anisotropy': ('Anisotropy', 'Anisotropy', 3, 0.0),
            'emission_coefficients': ('Emission Coefficients', 'Emission Coefficients', 8, (0.0, 0.0, 0.0)),
            'ior': ('IOR', 'IOR', 4, 1.3300000429153442),
            'backscatter': ('Backscatter', 'Backscatter', 5, 0.10000000149011612),
            'alpha': ('Alpha', 'Alpha', 6, 0.5),
            'diameter': ('Diameter', 'Diameter', 7, 20.0),
        },
        properties={
            'phase': phase,
        },
        output_sockets={
            'volume': ('Volume', 'Volume', 0, 'AUTO'),
        },
        output_type=ShaderNodeVolumeCoefficientsOutputs,
    )

class ShaderNodeVolumeInfoOutputs(typing.NamedTuple):
    'Outputs from Volume Info: Read volume data attributes from volume grids'
    color: Socket[Color]
    density: Socket[float]
    flame: Socket[float]
    temperature: Socket[float]

def volume_info() -> ShaderNodeVolumeInfoOutputs:
    'Read volume data attributes from volume grids'
    return _node_function(
        'ShaderNodeVolumeInfo',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
            'density': ('Density', 'Density', 1, 'AUTO'),
            'flame': ('Flame', 'Flame', 2, 'AUTO'),
            'temperature': ('Temperature', 'Temperature', 3, 'AUTO'),
        },
        output_type=ShaderNodeVolumeInfoOutputs,
    )

class ShaderNodeVolumeScatterOutputs(typing.NamedTuple):
    'Outputs from Volume Scatter: Scatter light as it passes through the volume, often used to add fog to a scene'
    volume: Socket[Shader]

def volume_scatter(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), density: float | Socket[float] = 1.0, anisotropy: float | Socket[float] = 0.0, ior: float | Socket[float] = 1.3300000429153442, backscatter: float | Socket[float] = 0.10000000149011612, alpha: float | Socket[float] = 0.5, diameter: float | Socket[float] = 20.0, phase: typing.Literal['HENYEY_GREENSTEIN', 'FOURNIER_FORAND', 'DRAINE', 'RAYLEIGH', 'MIE'] = 'HENYEY_GREENSTEIN') -> ShaderNodeVolumeScatterOutputs:
    'Scatter light as it passes through the volume, often used to add fog to a scene\n\nArgs:\n    phase: Phase function for the scattered light'
    return _node_function(
        'ShaderNodeVolumeScatter',
        inputs={
            'color': color,
            'density': density,
            'anisotropy': anisotropy,
            'ior': ior,
            'backscatter': backscatter,
            'alpha': alpha,
            'diameter': diameter,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'density': ('Density', 'Density', 1, 1.0),
            'anisotropy': ('Anisotropy', 'Anisotropy', 2, 0.0),
            'ior': ('IOR', 'IOR', 3, 1.3300000429153442),
            'backscatter': ('Backscatter', 'Backscatter', 4, 0.10000000149011612),
            'alpha': ('Alpha', 'Alpha', 5, 0.5),
            'diameter': ('Diameter', 'Diameter', 6, 20.0),
        },
        properties={
            'phase': phase,
        },
        output_sockets={
            'volume': ('Volume', 'Volume', 0, 'AUTO'),
        },
        output_type=ShaderNodeVolumeScatterOutputs,
    )

class ShaderNodeTexVoronoiOutputs(typing.NamedTuple):
    'Outputs from Voronoi Texture: Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells'
    distance: Socket[float]
    color: Socket[Color]
    position: Socket[Vector]
    w: Socket[float]
    radius: Socket[float]

def voronoi_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), scale: float | Socket[float] = 5.0, detail: float | Socket[float] = 0.0, roughness: float | Socket[float] = 0.5, lacunarity: float | Socket[float] = 2.0, randomness: float | Socket[float] = 1.0, w: float | Socket[float] = 0.0, smoothness: float | Socket[float] = 1.0, exponent: float | Socket[float] = 0.5, voronoi_dimensions: typing.Literal['1D', '2D', '3D', '4D'] = '3D', distance: typing.Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN', feature: typing.Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1', normalize: bool = False) -> ShaderNodeTexVoronoiOutputs:
    'Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells\n\nArgs:\n    voronoi_dimensions: Number of dimensions to output noise for\n    distance: The distance metric used to compute the texture\n    feature: The Voronoi feature that the node will compute\n    normalize: Normalize output Distance to 0.0 to 1.0 range'
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
            'distance': ('Distance', 'Distance', 0, 'AUTO'),
            'color': ('Color', 'Color', 1, 'AUTO'),
            'position': ('Position', 'Position', 2, 'AUTO'),
            'w': ('W', 'W', 3, 'AUTO'),
            'radius': ('Radius', 'Radius', 4, 'AUTO'),
        },
        output_type=ShaderNodeTexVoronoiOutputs,
    )

class ShaderNodeTexWaveOutputs(typing.NamedTuple):
    'Outputs from Wave Texture: Generate procedural bands or rings with noise'
    color: Socket[Color]
    factor: Socket[float]

def wave_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), scale: float | Socket[float] = 5.0, distortion: float | Socket[float] = 0.0, detail: float | Socket[float] = 2.0, detail_scale: float | Socket[float] = 1.0, detail_roughness: float | Socket[float] = 0.5, phase_offset: float | Socket[float] = 0.0, wave_type: typing.Literal['BANDS', 'RINGS'] = 'BANDS', bands_direction: typing.Literal['X', 'Y', 'Z', 'DIAGONAL'] = 'X', rings_direction: typing.Literal['X', 'Y', 'Z', 'SPHERICAL'] = 'X', wave_profile: typing.Literal['SIN', 'SAW', 'TRI'] = 'SIN') -> ShaderNodeTexWaveOutputs:
    'Generate procedural bands or rings with noise'
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
            'color': ('Color', 'Color', 0, 'AUTO'),
            'factor': ('Fac', 'Factor', 1, 'AUTO'),
        },
        output_type=ShaderNodeTexWaveOutputs,
    )

class ShaderNodeWavelengthOutputs(typing.NamedTuple):
    'Outputs from Wavelength: Convert a wavelength value to an RGB value'
    color: Socket[Color]

def wavelength(*, wavelength: float | Socket[float] = 500.0) -> ShaderNodeWavelengthOutputs:
    'Convert a wavelength value to an RGB value'
    return _node_function(
        'ShaderNodeWavelength',
        inputs={
            'wavelength': wavelength,
        },
        input_sockets={
            'wavelength': ('Wavelength', 'Wavelength', 0, 500.0),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=ShaderNodeWavelengthOutputs,
    )

class ShaderNodeTexWhiteNoiseOutputs(typing.NamedTuple):
    'Outputs from White Noise Texture: Calculate a random value or color based on an input seed'
    value: Socket[float]
    color: Socket[Color]

def white_noise_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), w: float | Socket[float] = 0.0, noise_dimensions: typing.Literal['1D', '2D', '3D', '4D'] = '3D') -> ShaderNodeTexWhiteNoiseOutputs:
    'Calculate a random value or color based on an input seed\n\nArgs:\n    noise_dimensions: Number of dimensions to output noise for'
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
            'value': ('Value', 'Value', 0, 'AUTO'),
            'color': ('Color', 'Color', 1, 'AUTO'),
        },
        output_type=ShaderNodeTexWhiteNoiseOutputs,
    )

class ShaderNodeWireframeOutputs(typing.NamedTuple):
    'Outputs from Wireframe: Retrieve the edges of an object as it appears to Cycles.\nNote: as meshes are triangulated before being processed by Cycles, topology will always appear triangulated'
    factor: Socket[float]

def wireframe(*, size: float | Socket[float] = 0.009999999776482582, use_pixel_size: bool = False) -> ShaderNodeWireframeOutputs:
    'Retrieve the edges of an object as it appears to Cycles.\nNote: as meshes are triangulated before being processed by Cycles, topology will always appear triangulated\n\nArgs:\n    use_pixel_size: Use screen pixel size instead of world units'
    return _node_function(
        'ShaderNodeWireframe',
        inputs={
            'size': size,
        },
        input_sockets={
            'size': ('Size', 'Size', 0, 0.009999999776482582),
        },
        properties={
            'use_pixel_size': use_pixel_size,
        },
        output_sockets={
            'factor': ('Fac', 'Factor', 0, 'AUTO'),
        },
        output_type=ShaderNodeWireframeOutputs,
    )

def world_output(*, surface: Shader | Socket[Shader] | None = None, volume: Shader | Socket[Shader] | None = None, is_active_output: bool = True, target: typing.Literal['ALL', 'EEVEE', 'CYCLES'] = 'ALL') -> None:
    "Output light color information to the scene's World\n\nArgs:\n    is_active_output: True if this node is used as the active output\n    target: Which renderer and viewport shading types to use the shaders for"
    return _node_function(
        'ShaderNodeOutputWorld',
        inputs={
            'surface': surface,
            'volume': volume,
        },
        input_sockets={
            'surface': ('Surface', 'Surface', 0, None),
            'volume': ('Volume', 'Volume', 1, None),
        },
        properties={
            'is_active_output': is_active_output,
            'target': target,
        },
        output_sockets={
        },
        output_type=None,
    )
