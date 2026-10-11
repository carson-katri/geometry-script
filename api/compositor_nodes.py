# Generated from Blender 5.2.0 LTS (CompositorNodeTree).
# Do not edit: run code_generator/node_functions_generator.py instead.

from __future__ import annotations

import typing

import bpy

from .runtime import ItemOutputs, Socket, node_function as _node_function
from .types import *

BLENDER_VERSION = (5, 2, 0)

__all__ = [
    'active_camera',
    'align_rotation_to_vector',
    'alpha_convert',
    'alpha_over',
    'anti_aliasing',
    'axes_to_rotation',
    'axis_angle_to_rotation',
    'bilateral_blur',
    'blackbody',
    'blank_image',
    'blur',
    'bokeh_blur',
    'bokeh_image',
    'boolean',
    'box_mask',
    'brick_texture',
    'brightness_contrast',
    'camera_info',
    'channel_key',
    'checker_texture',
    'chroma_key',
    'clamp',
    'color',
    'color_balance',
    'color_correction',
    'color_key',
    'color_ramp',
    'color_spill',
    'combine_color',
    'combine_matrix',
    'combine_xyz',
    'convert_colorspace',
    'convert_to_display',
    'convolve',
    'corner_pin',
    'crop',
    'cryptomatte',
    'cryptomatte_legacy',
    'defocus',
    'denoise',
    'depth_combine',
    'despeckle',
    'difference_key',
    'dilate_erode',
    'directional_blur',
    'displace',
    'distance_key',
    'double_edge_mask',
    'ellipse_mask',
    'enable_output',
    'euler_to_rotation',
    'exposure',
    'file_output',
    'filter',
    'find_in_string',
    'flip',
    'float_curve',
    'font',
    'format_string',
    'gabor_texture',
    'gamma',
    'glare',
    'gradient_texture',
    'hue_correct',
    'hue_saturation_value',
    'id_mask',
    'image',
    'image_coordinates',
    'image_info',
    'index_switch',
    'inpaint',
    'integer',
    'integer_vector',
    'invert_color',
    'invert_matrix',
    'invert_rotation',
    'keying',
    'keying_screen',
    'kuwahara',
    'lens_distortion',
    'levels',
    'luminance_key',
    'magic_texture',
    'map_range',
    'map_uv',
    'mask',
    'mask_to_sdf',
    'match_string',
    'math_',
    'matrix_determinant',
    'menu',
    'menu_switch',
    'mix',
    'mix_legacy',
    'movie_clip',
    'movie_distortion',
    'multiply_matrices',
    'noise_texture',
    'normal',
    'normalize',
    'object_',
    'object_info',
    'pixelate',
    'plane_track_deform',
    'posterize',
    'project_point',
    'quaternion_to_rotation',
    'radial_tiling',
    'relative_to_pixel',
    'render_layers',
    'replace_string',
    'reverse_string',
    'rgb_curves_compositor_node_curve_rgb',
    'rgb_curves_shader_node_rgb_curve',
    'rgb_to_bw',
    'rotate',
    'rotate_rotation',
    'rotate_vector',
    'rotation',
    'rotation_to_axis_angle',
    'rotation_to_euler',
    'rotation_to_quaternion',
    'scale',
    'scene_time',
    'separate_color',
    'separate_matrix',
    'separate_xyz',
    'sequencer_strip_info',
    'set_alpha',
    'set_string_case',
    'slice_string',
    'special_characters',
    'split',
    'stabilize_2_d',
    'string_',
    'string_length',
    'string_to_image',
    'string_to_value',
    'switch_compositor_node_switch',
    'switch_geometry_node_switch',
    'switch_view',
    'time_curve',
    'tonemap',
    'track_position',
    'transform',
    'transform_direction',
    'transform_point',
    'translate',
    'transpose_matrix',
    'trim_string',
    'value',
    'value_to_string',
    'vector',
    'vector_blur',
    'vector_curves',
    'vector_math',
    'vector_rotate',
    'viewer',
    'voronoi_texture',
    'warning',
    'wave_texture',
    'white_noise_texture',
]

class GeometryNodeInputActiveCameraOutputs(typing.NamedTuple):
    "Outputs from Active Camera: Retrieve the scene's active camera"
    active_camera: Socket[Object]

def active_camera() -> GeometryNodeInputActiveCameraOutputs:
    "Retrieve the scene's active camera"
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

class FunctionNodeAlignRotationToVectorOutputs(typing.NamedTuple):
    'Outputs from Align Rotation to Vector: Orient a rotation along the given direction'
    rotation: Socket[Rotation]

def align_rotation_to_vector(*, rotation: Rotation | Socket[Rotation] = (0.0, 0.0, 0.0), factor: float | Socket[float] = 1.0, vector: Vector | Socket[Vector] = (0.0, 0.0, 1.0), axis: typing.Literal['X', 'Y', 'Z'] = 'Z', pivot_axis: typing.Literal['AUTO', 'X', 'Y', 'Z'] = 'AUTO') -> FunctionNodeAlignRotationToVectorOutputs:
    'Orient a rotation along the given direction\n\nArgs:\n    axis: Axis to align to the vector\n    pivot_axis: Axis to rotate around'
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

class CompositorNodePremulKeyOutputs(typing.NamedTuple):
    'Outputs from Alpha Convert: Convert to and from premultiplied (associated) alpha'
    image: Socket[Color]

def alpha_convert(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), type: Menu | Socket[Menu] = 'To Premultiplied') -> CompositorNodePremulKeyOutputs:
    'Convert to and from premultiplied (associated) alpha'
    return _node_function(
        'CompositorNodePremulKey',
        inputs={
            'image': image,
            'type': type,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'type': ('Type', 'Type', 1, 'To Premultiplied'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodePremulKeyOutputs,
    )

class CompositorNodeAlphaOverOutputs(typing.NamedTuple):
    'Outputs from Alpha Over: Overlay a foreground image onto a background image'
    image: Socket[Color]

def alpha_over(*, background: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), foreground: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), factor: float | Socket[float] = 1.0, type: Menu | Socket[Menu] = 'Over', straight_alpha: bool | Socket[bool] = False) -> CompositorNodeAlphaOverOutputs:
    'Overlay a foreground image onto a background image'
    return _node_function(
        'CompositorNodeAlphaOver',
        inputs={
            'background': background,
            'foreground': foreground,
            'factor': factor,
            'type': type,
            'straight_alpha': straight_alpha,
        },
        input_sockets={
            'background': ('Background', 'Background', 0, (1.0, 1.0, 1.0, 1.0)),
            'foreground': ('Foreground', 'Foreground', 1, (1.0, 1.0, 1.0, 1.0)),
            'factor': ('Fac', 'Factor', 2, 1.0),
            'type': ('Type', 'Type', 3, 'Over'),
            'straight_alpha': ('Straight Alpha', 'Straight Alpha', 4, False),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeAlphaOverOutputs,
    )

class CompositorNodeAntiAliasingOutputs(typing.NamedTuple):
    'Outputs from Anti-Aliasing: Smooth away jagged edges'
    image: Socket[Color]

def anti_aliasing(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), threshold: float | Socket[float] = 0.20000000298023224, contrast_limit: float | Socket[float] = 2.0, corner_rounding: float | Socket[float] = 0.25) -> CompositorNodeAntiAliasingOutputs:
    'Smooth away jagged edges'
    return _node_function(
        'CompositorNodeAntiAliasing',
        inputs={
            'image': image,
            'threshold': threshold,
            'contrast_limit': contrast_limit,
            'corner_rounding': corner_rounding,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'threshold': ('Threshold', 'Threshold', 1, 0.20000000298023224),
            'contrast_limit': ('Contrast Limit', 'Contrast Limit', 2, 2.0),
            'corner_rounding': ('Corner Rounding', 'Corner Rounding', 3, 0.25),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeAntiAliasingOutputs,
    )

class FunctionNodeAxesToRotationOutputs(typing.NamedTuple):
    'Outputs from Axes to Rotation: Create a rotation from a primary and (ideally orthogonal) secondary axis'
    rotation: Socket[Rotation]

def axes_to_rotation(*, primary_axis: Vector | Socket[Vector] = (0.0, 0.0, 1.0), secondary_axis: Vector | Socket[Vector] = (1.0, 0.0, 0.0), primary_axis_property: typing.Literal['X', 'Y', 'Z'] = 'Z', secondary_axis_property: typing.Literal['X', 'Y', 'Z'] = 'X') -> FunctionNodeAxesToRotationOutputs:
    'Create a rotation from a primary and (ideally orthogonal) secondary axis\n\nArgs:\n    primary_axis_property: Axis that is aligned exactly to the provided primary direction\n    secondary_axis_property: Axis that is aligned as well as possible given the alignment of the primary axis'
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
    'Outputs from Axis Angle to Rotation: Build a rotation from an axis and a rotation around that axis'
    rotation: Socket[Rotation]

def axis_angle_to_rotation(*, axis: Vector | Socket[Vector] = (0.0, 0.0, 1.0), angle: float | Socket[float] = 0.0) -> FunctionNodeAxisAngleToRotationOutputs:
    'Build a rotation from an axis and a rotation around that axis'
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

class CompositorNodeBilateralblurOutputs(typing.NamedTuple):
    'Outputs from Bilateral Blur: Adaptively blur image, while retaining sharp edges'
    image: Socket[Color]

def bilateral_blur(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), determinator: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), size: int | Socket[int] = 0, threshold: float | Socket[float] = 0.10000000149011612) -> CompositorNodeBilateralblurOutputs:
    'Adaptively blur image, while retaining sharp edges'
    return _node_function(
        'CompositorNodeBilateralblur',
        inputs={
            'image': image,
            'determinator': determinator,
            'size': size,
            'threshold': threshold,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'determinator': ('Determinator', 'Determinator', 1, (1.0, 1.0, 1.0, 1.0)),
            'size': ('Size', 'Size', 2, 0),
            'threshold': ('Threshold', 'Threshold', 3, 0.10000000149011612),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeBilateralblurOutputs,
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

class CompositorNodeBlankImageOutputs(typing.NamedTuple):
    'Outputs from Blank Image: Returns an image with the given size and constant color'
    image: Socket[Color]

def blank_image(*, color: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), size: IntVector2 | Socket[IntVector2] = (1920, 1080)) -> CompositorNodeBlankImageOutputs:
    'Returns an image with the given size and constant color'
    return _node_function(
        'CompositorNodeBlankImage',
        inputs={
            'color': color,
            'size': size,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.0, 0.0, 0.0, 1.0)),
            'size': ('Size', 'Size', 1, (1920, 1080)),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeBlankImageOutputs,
    )

class CompositorNodeBlurOutputs(typing.NamedTuple):
    'Outputs from Blur: Blur an image, using several blur modes'
    image: Socket[Color]

def blur(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), size: Vector2 | Socket[Vector2] = (0.0, 0.0), type: Menu | Socket[Menu] = 'Gaussian', extend_bounds: bool | Socket[bool] = False, separable: bool | Socket[bool] = True) -> CompositorNodeBlurOutputs:
    'Blur an image, using several blur modes'
    return _node_function(
        'CompositorNodeBlur',
        inputs={
            'image': image,
            'size': size,
            'type': type,
            'extend_bounds': extend_bounds,
            'separable': separable,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'size': ('Size', 'Size', 1, (0.0, 0.0)),
            'type': ('Type', 'Type', 2, 'Gaussian'),
            'extend_bounds': ('Extend Bounds', 'Extend Bounds', 3, False),
            'separable': ('Separable', 'Separable', 4, True),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeBlurOutputs,
    )

class CompositorNodeBokehBlurOutputs(typing.NamedTuple):
    'Outputs from Bokeh Blur: Generate a bokeh type blur similar to Defocus. Unlike defocus an in-focus region is defined in the compositor'
    image: Socket[Color]

def bokeh_blur(*, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), bokeh: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), size: float | Socket[float] = 0.0, mask: float | Socket[float] = 1.0, extend_bounds: bool | Socket[bool] = False) -> CompositorNodeBokehBlurOutputs:
    'Generate a bokeh type blur similar to Defocus. Unlike defocus an in-focus region is defined in the compositor'
    return _node_function(
        'CompositorNodeBokehBlur',
        inputs={
            'image': image,
            'bokeh': bokeh,
            'size': size,
            'mask': mask,
            'extend_bounds': extend_bounds,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'bokeh': ('Bokeh', 'Bokeh', 1, (1.0, 1.0, 1.0, 1.0)),
            'size': ('Size', 'Size', 2, 0.0),
            'mask': ('Mask', 'Mask', 3, 1.0),
            'extend_bounds': ('Extend Bounds', 'Extend Bounds', 4, False),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeBokehBlurOutputs,
    )

class CompositorNodeBokehImageOutputs(typing.NamedTuple):
    'Outputs from Bokeh Image: Generate image with bokeh shape for use with the Bokeh Blur filter node'
    image: Socket[Color]

def bokeh_image(*, flaps: int | Socket[int] = 5, angle: float | Socket[float] = 0.0, roundness: float | Socket[float] = 0.0, catadioptric_size: float | Socket[float] = 0.0, color_shift: float | Socket[float] = 0.0) -> CompositorNodeBokehImageOutputs:
    'Generate image with bokeh shape for use with the Bokeh Blur filter node'
    return _node_function(
        'CompositorNodeBokehImage',
        inputs={
            'flaps': flaps,
            'angle': angle,
            'roundness': roundness,
            'catadioptric_size': catadioptric_size,
            'color_shift': color_shift,
        },
        input_sockets={
            'flaps': ('Flaps', 'Flaps', 0, 5),
            'angle': ('Angle', 'Angle', 1, 0.0),
            'roundness': ('Roundness', 'Roundness', 2, 0.0),
            'catadioptric_size': ('Catadioptric Size', 'Catadioptric Size', 3, 0.0),
            'color_shift': ('Color Shift', 'Color Shift', 4, 0.0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeBokehImageOutputs,
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

class CompositorNodeBoxMaskOutputs(typing.NamedTuple):
    'Outputs from Box Mask: Create rectangular mask suitable for use as a simple matte'
    mask: Socket[float]

def box_mask(*, operation: Menu | Socket[Menu] = 'Add', mask: float | Socket[float] = 0.0, value: float | Socket[float] = 1.0, position: Vector2 | Socket[Vector2] = (0.5, 0.5), size: Vector2 | Socket[Vector2] = (0.20000000298023224, 0.10000000149011612), rotation: float | Socket[float] = 0.0) -> CompositorNodeBoxMaskOutputs:
    'Create rectangular mask suitable for use as a simple matte'
    return _node_function(
        'CompositorNodeBoxMask',
        inputs={
            'operation': operation,
            'mask': mask,
            'value': value,
            'position': position,
            'size': size,
            'rotation': rotation,
        },
        input_sockets={
            'operation': ('Operation', 'Operation', 0, 'Add'),
            'mask': ('Mask', 'Mask', 1, 0.0),
            'value': ('Value', 'Value', 2, 1.0),
            'position': ('Position', 'Position', 3, (0.5, 0.5)),
            'size': ('Size', 'Size', 4, (0.20000000298023224, 0.10000000149011612)),
            'rotation': ('Rotation', 'Rotation', 5, 0.0),
        },
        properties={
        },
        output_sockets={
            'mask': ('Mask', 'Mask', 0, 'AUTO'),
        },
        output_type=CompositorNodeBoxMaskOutputs,
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

class CompositorNodeBrightContrastOutputs(typing.NamedTuple):
    'Outputs from Brightness/Contrast: Adjust brightness and contrast'
    image: Socket[Color]

def brightness_contrast(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), brightness: float | Socket[float] = 0.0, contrast: float | Socket[float] = 0.0) -> CompositorNodeBrightContrastOutputs:
    'Adjust brightness and contrast'
    return _node_function(
        'CompositorNodeBrightContrast',
        inputs={
            'image': image,
            'brightness': brightness,
            'contrast': contrast,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'brightness': ('Bright', 'Brightness', 1, 0.0),
            'contrast': ('Contrast', 'Contrast', 2, 0.0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeBrightContrastOutputs,
    )

class GeometryNodeCameraInfoOutputs(typing.NamedTuple):
    'Outputs from Camera Info: Retrieve information from a camera object'
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
    'Retrieve information from a camera object'
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

class CompositorNodeChannelMatteOutputs(typing.NamedTuple):
    'Outputs from Channel Key: Create matte based on differences in color channels'
    image: Socket[Color]
    matte: Socket[float]

def channel_key(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), minimum: float | Socket[float] = 0.0, maximum: float | Socket[float] = 1.0, color_space: Menu | Socket[Menu] = 'RGB', rgb_key_channel: Menu | Socket[Menu] = 'G', hsv_key_channel: Menu | Socket[Menu] = 'H', yuv_key_channel: Menu | Socket[Menu] = 'V', y_cb_cr_key_channel: Menu | Socket[Menu] = 'Cr', limit_method: Menu | Socket[Menu] = 'Max', rgb_limit_channel: Menu | Socket[Menu] = 'R', hsv_limit_channel: Menu | Socket[Menu] = 'S', yuv_limit_channel: Menu | Socket[Menu] = 'U', y_cb_cr_limit_channel: Menu | Socket[Menu] = 'Cb') -> CompositorNodeChannelMatteOutputs:
    'Create matte based on differences in color channels'
    return _node_function(
        'CompositorNodeChannelMatte',
        inputs={
            'image': image,
            'minimum': minimum,
            'maximum': maximum,
            'color_space': color_space,
            'rgb_key_channel': rgb_key_channel,
            'hsv_key_channel': hsv_key_channel,
            'yuv_key_channel': yuv_key_channel,
            'y_cb_cr_key_channel': y_cb_cr_key_channel,
            'limit_method': limit_method,
            'rgb_limit_channel': rgb_limit_channel,
            'hsv_limit_channel': hsv_limit_channel,
            'yuv_limit_channel': yuv_limit_channel,
            'y_cb_cr_limit_channel': y_cb_cr_limit_channel,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'minimum': ('Minimum', 'Minimum', 1, 0.0),
            'maximum': ('Maximum', 'Maximum', 2, 1.0),
            'color_space': ('Color Space', 'Color Space', 3, 'RGB'),
            'rgb_key_channel': ('RGB Key Channel', 'RGB Key Channel', 4, 'G'),
            'hsv_key_channel': ('HSV Key Channel', 'HSV Key Channel', 5, 'H'),
            'yuv_key_channel': ('YUV Key Channel', 'YUV Key Channel', 6, 'V'),
            'y_cb_cr_key_channel': ('YCbCr Key Channel', 'YCbCr Key Channel', 7, 'Cr'),
            'limit_method': ('Limit Method', 'Limit Method', 8, 'Max'),
            'rgb_limit_channel': ('RGB Limit Channel', 'RGB Limit Channel', 9, 'R'),
            'hsv_limit_channel': ('HSV Limit Channel', 'HSV Limit Channel', 10, 'S'),
            'yuv_limit_channel': ('YUV Limit Channel', 'YUV Limit Channel', 11, 'U'),
            'y_cb_cr_limit_channel': ('YCbCr Limit Channel', 'YCbCr Limit Channel', 12, 'Cb'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'matte': ('Matte', 'Matte', 1, 'AUTO'),
        },
        output_type=CompositorNodeChannelMatteOutputs,
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

class CompositorNodeChromaMatteOutputs(typing.NamedTuple):
    'Outputs from Chroma Key: Create matte based on chroma values'
    image: Socket[Color]
    matte: Socket[float]

def chroma_key(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), key_color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), minimum: float | Socket[float] = 0.1745329201221466, maximum: float | Socket[float] = 0.5235987901687622, falloff: float | Socket[float] = 1.0) -> CompositorNodeChromaMatteOutputs:
    'Create matte based on chroma values'
    return _node_function(
        'CompositorNodeChromaMatte',
        inputs={
            'image': image,
            'key_color': key_color,
            'minimum': minimum,
            'maximum': maximum,
            'falloff': falloff,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'key_color': ('Key Color', 'Key Color', 1, (1.0, 1.0, 1.0, 1.0)),
            'minimum': ('Minimum', 'Minimum', 2, 0.1745329201221466),
            'maximum': ('Maximum', 'Maximum', 3, 0.5235987901687622),
            'falloff': ('Falloff', 'Falloff', 4, 1.0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'matte': ('Matte', 'Matte', 1, 'AUTO'),
        },
        output_type=CompositorNodeChromaMatteOutputs,
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

class CompositorNodeRGBOutputs(typing.NamedTuple):
    'Outputs from Color: A color picker'
    color: Socket[Color]

def color() -> CompositorNodeRGBOutputs:
    'A color picker'
    return _node_function(
        'CompositorNodeRGB',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=CompositorNodeRGBOutputs,
    )

class CompositorNodeColorBalanceOutputs(typing.NamedTuple):
    'Outputs from Color Balance: Adjust color and values'
    image: Socket[Color]

def color_balance(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), factor: float | Socket[float] = 1.0, type: Menu | Socket[Menu] = 'Lift/Gamma/Gain', lift: float | Socket[float] = 0.0, lift_2: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), gamma: float | Socket[float] = 1.0, gamma_2: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), gain: float | Socket[float] = 1.0, gain_2: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), offset: float | Socket[float] = 0.0, offset_2: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), power: float | Socket[float] = 1.0, power_2: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), slope: float | Socket[float] = 1.0, slope_2: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), temperature: float | Socket[float] = 6500.0, tint: float | Socket[float] = 10.0, temperature_2: float | Socket[float] = 6500.0, tint_2: float | Socket[float] = 10.0, input_whitepoint: Color = (0.9993047714233398, 1.0003489255905151, 0.9985780119895935), output_whitepoint: Color = (0.9993047714233398, 1.0003489255905151, 0.9985780119895935)) -> CompositorNodeColorBalanceOutputs:
    'Adjust color and values\n\nArgs:\n    input_whitepoint: The color which gets mapped to white (automatically converted to/from temperature and tint)\n    output_whitepoint: The color which gets white gets mapped to (automatically converted to/from temperature and tint)'
    return _node_function(
        'CompositorNodeColorBalance',
        inputs={
            'image': image,
            'factor': factor,
            'type': type,
            'lift': lift,
            'lift_2': lift_2,
            'gamma': gamma,
            'gamma_2': gamma_2,
            'gain': gain,
            'gain_2': gain_2,
            'offset': offset,
            'offset_2': offset_2,
            'power': power,
            'power_2': power_2,
            'slope': slope,
            'slope_2': slope_2,
            'temperature': temperature,
            'tint': tint,
            'temperature_2': temperature_2,
            'tint_2': tint_2,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'factor': ('Fac', 'Factor', 1, 1.0),
            'type': ('Type', 'Type', 2, 'Lift/Gamma/Gain'),
            'lift': ('Base Lift', 'Lift', 3, 0.0),
            'lift_2': ('Color Lift', 'Lift', 4, (1.0, 1.0, 1.0, 1.0)),
            'gamma': ('Base Gamma', 'Gamma', 5, 1.0),
            'gamma_2': ('Color Gamma', 'Gamma', 6, (1.0, 1.0, 1.0, 1.0)),
            'gain': ('Base Gain', 'Gain', 7, 1.0),
            'gain_2': ('Color Gain', 'Gain', 8, (1.0, 1.0, 1.0, 1.0)),
            'offset': ('Base Offset', 'Offset', 9, 0.0),
            'offset_2': ('Color Offset', 'Offset', 10, (0.0, 0.0, 0.0, 1.0)),
            'power': ('Base Power', 'Power', 11, 1.0),
            'power_2': ('Color Power', 'Power', 12, (1.0, 1.0, 1.0, 1.0)),
            'slope': ('Base Slope', 'Slope', 13, 1.0),
            'slope_2': ('Color Slope', 'Slope', 14, (1.0, 1.0, 1.0, 1.0)),
            'temperature': ('Input Temperature', 'Temperature', 15, 6500.0),
            'tint': ('Input Tint', 'Tint', 16, 10.0),
            'temperature_2': ('Output Temperature', 'Temperature', 17, 6500.0),
            'tint_2': ('Output Tint', 'Tint', 18, 10.0),
        },
        properties={
            'input_whitepoint': input_whitepoint,
            'output_whitepoint': output_whitepoint,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeColorBalanceOutputs,
    )

class CompositorNodeColorCorrectionOutputs(typing.NamedTuple):
    'Outputs from Color Correction: Adjust the color of an image, separately in several tonal ranges (highlights, midtones and shadows)'
    image: Socket[Color]

def color_correction(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), mask: float | Socket[float] = 1.0, saturation: float | Socket[float] = 1.0, contrast: float | Socket[float] = 1.0, gamma: float | Socket[float] = 1.0, gain: float | Socket[float] = 1.0, offset: float | Socket[float] = 0.0, saturation_2: float | Socket[float] = 1.0, contrast_2: float | Socket[float] = 1.0, gamma_2: float | Socket[float] = 1.0, gain_2: float | Socket[float] = 1.0, offset_2: float | Socket[float] = 0.0, saturation_3: float | Socket[float] = 1.0, contrast_3: float | Socket[float] = 1.0, gamma_3: float | Socket[float] = 1.0, gain_3: float | Socket[float] = 1.0, offset_3: float | Socket[float] = 0.0, saturation_4: float | Socket[float] = 1.0, contrast_4: float | Socket[float] = 1.0, gamma_4: float | Socket[float] = 1.0, gain_4: float | Socket[float] = 1.0, offset_4: float | Socket[float] = 0.0, midtones_start: float | Socket[float] = 0.20000000298023224, midtones_end: float | Socket[float] = 0.699999988079071, red: bool | Socket[bool] = True, green: bool | Socket[bool] = True, blue: bool | Socket[bool] = True) -> CompositorNodeColorCorrectionOutputs:
    'Adjust the color of an image, separately in several tonal ranges (highlights, midtones and shadows)'
    return _node_function(
        'CompositorNodeColorCorrection',
        inputs={
            'image': image,
            'mask': mask,
            'saturation': saturation,
            'contrast': contrast,
            'gamma': gamma,
            'gain': gain,
            'offset': offset,
            'saturation_2': saturation_2,
            'contrast_2': contrast_2,
            'gamma_2': gamma_2,
            'gain_2': gain_2,
            'offset_2': offset_2,
            'saturation_3': saturation_3,
            'contrast_3': contrast_3,
            'gamma_3': gamma_3,
            'gain_3': gain_3,
            'offset_3': offset_3,
            'saturation_4': saturation_4,
            'contrast_4': contrast_4,
            'gamma_4': gamma_4,
            'gain_4': gain_4,
            'offset_4': offset_4,
            'midtones_start': midtones_start,
            'midtones_end': midtones_end,
            'red': red,
            'green': green,
            'blue': blue,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'mask': ('Mask', 'Mask', 1, 1.0),
            'saturation': ('Master Saturation', 'Saturation', 2, 1.0),
            'contrast': ('Master Contrast', 'Contrast', 3, 1.0),
            'gamma': ('Master Gamma', 'Gamma', 4, 1.0),
            'gain': ('Master Gain', 'Gain', 5, 1.0),
            'offset': ('Master Offset', 'Offset', 6, 0.0),
            'saturation_2': ('Highlights Saturation', 'Saturation', 7, 1.0),
            'contrast_2': ('Highlights Contrast', 'Contrast', 8, 1.0),
            'gamma_2': ('Highlights Gamma', 'Gamma', 9, 1.0),
            'gain_2': ('Highlights Gain', 'Gain', 10, 1.0),
            'offset_2': ('Highlights Offset', 'Offset', 11, 0.0),
            'saturation_3': ('Midtones Saturation', 'Saturation', 12, 1.0),
            'contrast_3': ('Midtones Contrast', 'Contrast', 13, 1.0),
            'gamma_3': ('Midtones Gamma', 'Gamma', 14, 1.0),
            'gain_3': ('Midtones Gain', 'Gain', 15, 1.0),
            'offset_3': ('Midtones Offset', 'Offset', 16, 0.0),
            'saturation_4': ('Shadows Saturation', 'Saturation', 17, 1.0),
            'contrast_4': ('Shadows Contrast', 'Contrast', 18, 1.0),
            'gamma_4': ('Shadows Gamma', 'Gamma', 19, 1.0),
            'gain_4': ('Shadows Gain', 'Gain', 20, 1.0),
            'offset_4': ('Shadows Offset', 'Offset', 21, 0.0),
            'midtones_start': ('Midtones Start', 'Midtones Start', 22, 0.20000000298023224),
            'midtones_end': ('Midtones End', 'Midtones End', 23, 0.699999988079071),
            'red': ('Apply On Red', 'Red', 24, True),
            'green': ('Apply On Green', 'Green', 25, True),
            'blue': ('Apply On Blue', 'Blue', 26, True),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeColorCorrectionOutputs,
    )

class CompositorNodeColorMatteOutputs(typing.NamedTuple):
    'Outputs from Color Key: Create matte using a given color, for green or blue screen footage'
    image: Socket[Color]
    matte: Socket[float]

def color_key(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), key_color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), hue: float | Socket[float] = 0.009999999776482582, saturation: float | Socket[float] = 0.10000000149011612, value: float | Socket[float] = 0.10000000149011612) -> CompositorNodeColorMatteOutputs:
    'Create matte using a given color, for green or blue screen footage'
    return _node_function(
        'CompositorNodeColorMatte',
        inputs={
            'image': image,
            'key_color': key_color,
            'hue': hue,
            'saturation': saturation,
            'value': value,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'key_color': ('Key Color', 'Key Color', 1, (1.0, 1.0, 1.0, 1.0)),
            'hue': ('Hue', 'Hue', 2, 0.009999999776482582),
            'saturation': ('Saturation', 'Saturation', 3, 0.10000000149011612),
            'value': ('Value', 'Value', 4, 0.10000000149011612),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'matte': ('Matte', 'Matte', 1, 'AUTO'),
        },
        output_type=CompositorNodeColorMatteOutputs,
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

class CompositorNodeColorSpillOutputs(typing.NamedTuple):
    'Outputs from Color Spill: Remove colors from a blue or green screen, by reducing one RGB channel compared to the others'
    image: Socket[Color]

def color_spill(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), factor: float | Socket[float] = 1.0, spill_channel: Menu | Socket[Menu] = 'G', limit_method: Menu | Socket[Menu] = 'Single', limit_channel: Menu | Socket[Menu] = 'R', limit_strength: float | Socket[float] = 1.0, use_spill_strength: bool | Socket[bool] = False, strength: Color | Socket[Color] = (0.0, 1.0, 0.0, 1.0)) -> CompositorNodeColorSpillOutputs:
    'Remove colors from a blue or green screen, by reducing one RGB channel compared to the others'
    return _node_function(
        'CompositorNodeColorSpill',
        inputs={
            'image': image,
            'factor': factor,
            'spill_channel': spill_channel,
            'limit_method': limit_method,
            'limit_channel': limit_channel,
            'limit_strength': limit_strength,
            'use_spill_strength': use_spill_strength,
            'strength': strength,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'factor': ('Fac', 'Factor', 1, 1.0),
            'spill_channel': ('Spill Channel', 'Spill Channel', 2, 'G'),
            'limit_method': ('Limit Method', 'Limit Method', 3, 'Single'),
            'limit_channel': ('Limit Channel', 'Limit Channel', 4, 'R'),
            'limit_strength': ('Limit Strength', 'Limit Strength', 5, 1.0),
            'use_spill_strength': ('Use Spill Strength', 'Use Spill Strength', 6, False),
            'strength': ('Spill Strength', 'Strength', 7, (0.0, 1.0, 0.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeColorSpillOutputs,
    )

class CompositorNodeCombineColorOutputs(typing.NamedTuple):
    'Outputs from Combine Color: Combine an image from its composite color channels'
    image: Socket[Color]

def combine_color(*, red: float | Socket[float] = 0.0, green: float | Socket[float] = 0.0, blue: float | Socket[float] = 0.0, alpha: float | Socket[float] = 1.0, mode: typing.Literal['RGB', 'HSV', 'HSL', 'YCC', 'YUV'] = 'RGB', ycc_mode: typing.Literal['ITUBT601', 'ITUBT709', 'JFIF'] = 'ITUBT709') -> CompositorNodeCombineColorOutputs:
    'Combine an image from its composite color channels\n\nArgs:\n    mode: Mode of color processing\n    ycc_mode: Color space used for YCbCrA processing'
    return _node_function(
        'CompositorNodeCombineColor',
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
            'ycc_mode': ycc_mode,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeCombineColorOutputs,
    )

class FunctionNodeCombineMatrixOutputs(typing.NamedTuple):
    'Outputs from Combine Matrix: Construct a 4x4 matrix from its individual values'
    matrix: Socket[Matrix]

def combine_matrix(*, column_1_row_1: float | Socket[float] = 1.0, column_1_row_2: float | Socket[float] = 0.0, column_1_row_3: float | Socket[float] = 0.0, column_1_row_4: float | Socket[float] = 0.0, column_2_row_1: float | Socket[float] = 0.0, column_2_row_2: float | Socket[float] = 1.0, column_2_row_3: float | Socket[float] = 0.0, column_2_row_4: float | Socket[float] = 0.0, column_3_row_1: float | Socket[float] = 0.0, column_3_row_2: float | Socket[float] = 0.0, column_3_row_3: float | Socket[float] = 1.0, column_3_row_4: float | Socket[float] = 0.0, column_4_row_1: float | Socket[float] = 0.0, column_4_row_2: float | Socket[float] = 0.0, column_4_row_3: float | Socket[float] = 0.0, column_4_row_4: float | Socket[float] = 1.0) -> FunctionNodeCombineMatrixOutputs:
    'Construct a 4x4 matrix from its individual values'
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

class CompositorNodeConvertColorSpaceOutputs(typing.NamedTuple):
    'Outputs from Convert Colorspace: Convert between color spaces'
    image: Socket[Color]

def convert_colorspace(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), from_color_space: str | None = None, to_color_space: str | None = None) -> CompositorNodeConvertColorSpaceOutputs:
    'Convert between color spaces\n\nArgs:\n    from_color_space: Color space of the input image\n    to_color_space: Color space of the output image'
    return _node_function(
        'CompositorNodeConvertColorSpace',
        inputs={
            'image': image,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
        },
        properties={
            'from_color_space': from_color_space,
            'to_color_space': to_color_space,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeConvertColorSpaceOutputs,
    )

class CompositorNodeConvertToDisplayOutputs(typing.NamedTuple):
    'Outputs from Convert to Display: Convert from scene linear to display color space, with a view transform and look for tone mapping'
    image: Socket[Color]

def convert_to_display(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), invert: bool | Socket[bool] = False) -> CompositorNodeConvertToDisplayOutputs:
    'Convert from scene linear to display color space, with a view transform and look for tone mapping'
    return _node_function(
        'CompositorNodeConvertToDisplay',
        inputs={
            'image': image,
            'invert': invert,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'invert': ('Invert', 'Invert', 1, False),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeConvertToDisplayOutputs,
    )

class CompositorNodeConvolveOutputs(typing.NamedTuple):
    'Outputs from Convolve: Convolves an image with a kernel'
    image: Socket[Color]

def convolve(*, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), kernel_data_type: Menu | Socket[Menu] = 'Float', kernel: float | Socket[float] = 0.0, kernel_2: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), normalize_kernel: bool | Socket[bool] = True) -> CompositorNodeConvolveOutputs:
    'Convolves an image with a kernel'
    return _node_function(
        'CompositorNodeConvolve',
        inputs={
            'image': image,
            'kernel_data_type': kernel_data_type,
            'kernel': kernel,
            'kernel_2': kernel_2,
            'normalize_kernel': normalize_kernel,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'kernel_data_type': ('Kernel Data Type', 'Kernel Data Type', 1, 'Float'),
            'kernel': ('Float Kernel', 'Kernel', 2, 0.0),
            'kernel_2': ('Color Kernel', 'Kernel', 3, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'normalize_kernel': ('Normalize Kernel', 'Normalize Kernel', 4, True),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeConvolveOutputs,
    )

class CompositorNodeCornerPinOutputs(typing.NamedTuple):
    'Outputs from Corner Pin: Plane warp transformation using explicit corner values'
    image: Socket[Color]
    plane: Socket[float]

def corner_pin(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), upper_left: Vector2 | Socket[Vector2] = (0.0, 1.0), upper_right: Vector2 | Socket[Vector2] = (1.0, 1.0), lower_left: Vector2 | Socket[Vector2] = (0.0, 0.0), lower_right: Vector2 | Socket[Vector2] = (1.0, 0.0), interpolation: Menu | Socket[Menu] = 'Bilinear', extension_x: Menu | Socket[Menu] = 'Clip', extension_y: Menu | Socket[Menu] = 'Clip') -> CompositorNodeCornerPinOutputs:
    'Plane warp transformation using explicit corner values'
    return _node_function(
        'CompositorNodeCornerPin',
        inputs={
            'image': image,
            'upper_left': upper_left,
            'upper_right': upper_right,
            'lower_left': lower_left,
            'lower_right': lower_right,
            'interpolation': interpolation,
            'extension_x': extension_x,
            'extension_y': extension_y,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'upper_left': ('Upper Left', 'Upper Left', 1, (0.0, 1.0)),
            'upper_right': ('Upper Right', 'Upper Right', 2, (1.0, 1.0)),
            'lower_left': ('Lower Left', 'Lower Left', 3, (0.0, 0.0)),
            'lower_right': ('Lower Right', 'Lower Right', 4, (1.0, 0.0)),
            'interpolation': ('Interpolation', 'Interpolation', 5, 'Bilinear'),
            'extension_x': ('Extension X', 'Extension X', 6, 'Clip'),
            'extension_y': ('Extension Y', 'Extension Y', 7, 'Clip'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'plane': ('Plane', 'Plane', 1, 'AUTO'),
        },
        output_type=CompositorNodeCornerPinOutputs,
    )

class CompositorNodeCropOutputs(typing.NamedTuple):
    'Outputs from Crop: Crops image to a smaller region, either making the cropped area transparent or resizing the image'
    image: Socket[Color]

def crop(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), x: int | Socket[int] = 0, y: int | Socket[int] = 0, width: int | Socket[int] = 1920, height: int | Socket[int] = 1080, alpha_crop: bool | Socket[bool] = False) -> CompositorNodeCropOutputs:
    'Crops image to a smaller region, either making the cropped area transparent or resizing the image'
    return _node_function(
        'CompositorNodeCrop',
        inputs={
            'image': image,
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'alpha_crop': alpha_crop,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'x': ('X', 'X', 1, 0),
            'y': ('Y', 'Y', 2, 0),
            'width': ('Width', 'Width', 3, 1920),
            'height': ('Height', 'Height', 4, 1080),
            'alpha_crop': ('Alpha Crop', 'Alpha Crop', 5, False),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeCropOutputs,
    )

class CompositorNodeCryptomatteV2Outputs(typing.NamedTuple):
    'Outputs from Cryptomatte: Generate matte for individual objects and materials using Cryptomatte render passes'
    image: Socket[Color]
    matte: Socket[float]
    pick: Socket[Color]

def cryptomatte(*, image: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), source: typing.Literal['RENDER', 'IMAGE'] = 'RENDER', scene: bpy.types.Scene | None = None, image_property: bpy.types.Image | None = None, matte_id: str = '', add: Color = (1.0, 1.0, 1.0), remove: Color = (1.0, 1.0, 1.0), layer_name: str | None = None, frame_duration: int = 0, frame_start: int = 0, frame_offset: int = 0, use_cyclic: bool = False, use_auto_refresh: bool = False, layer: str | None = None, view: str | None = None) -> CompositorNodeCryptomatteV2Outputs:
    'Generate matte for individual objects and materials using Cryptomatte render passes\n\nArgs:\n    source: Where the Cryptomatte passes are loaded from\n    matte_id: List of object and material crypto IDs to include in matte\n    add: Add object or material to matte, by picking a color from the Pick output\n    remove: Remove object or material from matte, by picking a color from the Pick output\n    layer_name: What Cryptomatte layer is used\n    frame_duration: Number of images of a movie to use\n    frame_start: Global starting frame of the movie/sequence, assuming first picture has a #1\n    frame_offset: Offset the number of the frame to use in the animation\n    use_cyclic: Cycle the images in the movie\n    use_auto_refresh: Always refresh image on frame changes'
    return _node_function(
        'CompositorNodeCryptomatteV2',
        inputs={
            'image': image,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.0, 0.0, 0.0, 1.0)),
        },
        properties={
            'source': source,
            'scene': scene,
            'image': image_property,
            'matte_id': matte_id,
            'add': add,
            'remove': remove,
            'layer_name': layer_name,
            'frame_duration': frame_duration,
            'frame_start': frame_start,
            'frame_offset': frame_offset,
            'use_cyclic': use_cyclic,
            'use_auto_refresh': use_auto_refresh,
            'layer': layer,
            'view': view,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'matte': ('Matte', 'Matte', 1, 'AUTO'),
            'pick': ('Pick', 'Pick', 2, 'AUTO'),
        },
        output_type=CompositorNodeCryptomatteV2Outputs,
    )

class CompositorNodeCryptomatteOutputs(typing.NamedTuple):
    'Outputs from Cryptomatte (Legacy): Deprecated. Use Cryptomatte Node instead'
    image: Socket[Color]
    matte: Socket[float]
    pick: Socket[Color]

def cryptomatte_legacy(*, image: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), crypto_00: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), crypto_01: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), crypto_02: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), matte_id: str = '', add: Color = (1.0, 1.0, 1.0), remove: Color = (1.0, 1.0, 1.0)) -> CompositorNodeCryptomatteOutputs:
    'Deprecated. Use Cryptomatte Node instead\n\nArgs:\n    matte_id: List of object and material crypto IDs to include in matte\n    add: Add object or material to matte, by picking a color from the Pick output\n    remove: Remove object or material from matte, by picking a color from the Pick output'
    return _node_function(
        'CompositorNodeCryptomatte',
        inputs={
            'image': image,
            'crypto_00': crypto_00,
            'crypto_01': crypto_01,
            'crypto_02': crypto_02,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.0, 0.0, 0.0, 1.0)),
            'crypto_00': ('Crypto 00', 'Crypto 00', 1, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'crypto_01': ('Crypto 01', 'Crypto 01', 2, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'crypto_02': ('Crypto 02', 'Crypto 02', 3, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
        },
        properties={
            'matte_id': matte_id,
            'add': add,
            'remove': remove,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'matte': ('Matte', 'Matte', 1, 'AUTO'),
            'pick': ('Pick', 'Pick', 2, 'AUTO'),
        },
        output_type=CompositorNodeCryptomatteOutputs,
    )

class CompositorNodeDefocusOutputs(typing.NamedTuple):
    'Outputs from Defocus: Apply depth of field in 2D, using a Z depth map or mask'
    image: Socket[Color]

def defocus(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), z: float | Socket[float] = 1.0, scene: bpy.types.Scene | None = None, bokeh: typing.Literal['OCTAGON', 'HEPTAGON', 'HEXAGON', 'PENTAGON', 'SQUARE', 'TRIANGLE', 'CIRCLE'] = 'CIRCLE', angle: float = 0.0, f_stop: float = 128.0, blur_max: float = 16.0, use_zbuffer: bool = False, z_scale: float = 1.0) -> CompositorNodeDefocusOutputs:
    'Apply depth of field in 2D, using a Z depth map or mask\n\nArgs:\n    scene: Scene from which to select the active camera (render scene if undefined)\n    angle: Bokeh shape rotation offset\n    f_stop: Amount of focal blur, 128 (infinity) is perfect focus, half the value doubles the blur radius\n    blur_max: Blur limit, maximum CoC radius\n    use_zbuffer: Disable when using an image as input instead of actual z-buffer (auto enabled if node not image based, eg. time node)\n    z_scale: Scale the Z input when not using a z-buffer, controls maximum blur designated by the color white or input value 1'
    return _node_function(
        'CompositorNodeDefocus',
        inputs={
            'image': image,
            'z': z,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'z': ('Z', 'Z', 1, 1.0),
        },
        properties={
            'scene': scene,
            'bokeh': bokeh,
            'angle': angle,
            'f_stop': f_stop,
            'blur_max': blur_max,
            'use_zbuffer': use_zbuffer,
            'z_scale': z_scale,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeDefocusOutputs,
    )

class CompositorNodeDenoiseOutputs(typing.NamedTuple):
    'Outputs from Denoise: Denoise renders from Cycles and other ray tracing renderers'
    image: Socket[Color]

def denoise(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), albedo: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), normal: Vector | Socket[Vector] = (0.0, 0.0, 0.0), hdr: bool | Socket[bool] = True, prefilter: Menu | Socket[Menu] = 'Accurate', quality: Menu | Socket[Menu] = 'Follow Scene') -> CompositorNodeDenoiseOutputs:
    'Denoise renders from Cycles and other ray tracing renderers'
    return _node_function(
        'CompositorNodeDenoise',
        inputs={
            'image': image,
            'albedo': albedo,
            'normal': normal,
            'hdr': hdr,
            'prefilter': prefilter,
            'quality': quality,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'albedo': ('Albedo', 'Albedo', 1, (1.0, 1.0, 1.0, 1.0)),
            'normal': ('Normal', 'Normal', 2, (0.0, 0.0, 0.0)),
            'hdr': ('HDR', 'HDR', 3, True),
            'prefilter': ('Prefilter', 'Prefilter', 4, 'Accurate'),
            'quality': ('Quality', 'Quality', 5, 'Follow Scene'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeDenoiseOutputs,
    )

class CompositorNodeZcombineOutputs(typing.NamedTuple):
    'Outputs from Depth Combine: Combine two images using depth maps'
    result: Socket[Color]
    depth: Socket[float]

def depth_combine(*, a: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), depth_a: float | Socket[float] = 1.0, b: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), depth_b: float | Socket[float] = 1.0, use_alpha: bool | Socket[bool] = False, anti_alias: bool | Socket[bool] = True) -> CompositorNodeZcombineOutputs:
    'Combine two images using depth maps'
    return _node_function(
        'CompositorNodeZcombine',
        inputs={
            'a': a,
            'depth_a': depth_a,
            'b': b,
            'depth_b': depth_b,
            'use_alpha': use_alpha,
            'anti_alias': anti_alias,
        },
        input_sockets={
            'a': ('A', 'A', 0, (1.0, 1.0, 1.0, 1.0)),
            'depth_a': ('Depth A', 'Depth A', 1, 1.0),
            'b': ('B', 'B', 2, (1.0, 1.0, 1.0, 1.0)),
            'depth_b': ('Depth B', 'Depth B', 3, 1.0),
            'use_alpha': ('Use Alpha', 'Use Alpha', 4, False),
            'anti_alias': ('Anti-Alias', 'Anti-Alias', 5, True),
        },
        properties={
        },
        output_sockets={
            'result': ('Result', 'Result', 0, 'AUTO'),
            'depth': ('Depth', 'Depth', 1, 'AUTO'),
        },
        output_type=CompositorNodeZcombineOutputs,
    )

class CompositorNodeDespeckleOutputs(typing.NamedTuple):
    'Outputs from Despeckle: Smooth areas of an image in which noise is noticeable, while leaving complex areas untouched'
    image: Socket[Color]

def despeckle(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), factor: float | Socket[float] = 1.0, color_threshold: float | Socket[float] = 0.5, neighbor_threshold: float | Socket[float] = 0.5) -> CompositorNodeDespeckleOutputs:
    'Smooth areas of an image in which noise is noticeable, while leaving complex areas untouched'
    return _node_function(
        'CompositorNodeDespeckle',
        inputs={
            'image': image,
            'factor': factor,
            'color_threshold': color_threshold,
            'neighbor_threshold': neighbor_threshold,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'factor': ('Fac', 'Factor', 1, 1.0),
            'color_threshold': ('Color Threshold', 'Color Threshold', 2, 0.5),
            'neighbor_threshold': ('Neighbor Threshold', 'Neighbor Threshold', 3, 0.5),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeDespeckleOutputs,
    )

class CompositorNodeDiffMatteOutputs(typing.NamedTuple):
    'Outputs from Difference Key: Produce a matte that isolates foreground content by comparing it with a reference background image'
    image: Socket[Color]
    matte: Socket[float]

def difference_key(*, image_1: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), image_2: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), tolerance: float | Socket[float] = 0.10000000149011612, falloff: float | Socket[float] = 0.10000000149011612) -> CompositorNodeDiffMatteOutputs:
    'Produce a matte that isolates foreground content by comparing it with a reference background image'
    return _node_function(
        'CompositorNodeDiffMatte',
        inputs={
            'image_1': image_1,
            'image_2': image_2,
            'tolerance': tolerance,
            'falloff': falloff,
        },
        input_sockets={
            'image_1': ('Image 1', 'Image 1', 0, (1.0, 1.0, 1.0, 1.0)),
            'image_2': ('Image 2', 'Image 2', 1, (1.0, 1.0, 1.0, 1.0)),
            'tolerance': ('Tolerance', 'Tolerance', 2, 0.10000000149011612),
            'falloff': ('Falloff', 'Falloff', 3, 0.10000000149011612),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'matte': ('Matte', 'Matte', 1, 'AUTO'),
        },
        output_type=CompositorNodeDiffMatteOutputs,
    )

class CompositorNodeDilateErodeOutputs(typing.NamedTuple):
    'Outputs from Dilate/Erode: Expand and shrink masks'
    mask: Socket[float]

def dilate_erode(*, mask: float | Socket[float] = 0.0, size: int | Socket[int] = 0, type: Menu | Socket[Menu] = 'Steps', falloff_size: float | Socket[float] = 0.0, falloff: Menu | Socket[Menu] = 'Smooth') -> CompositorNodeDilateErodeOutputs:
    'Expand and shrink masks'
    return _node_function(
        'CompositorNodeDilateErode',
        inputs={
            'mask': mask,
            'size': size,
            'type': type,
            'falloff_size': falloff_size,
            'falloff': falloff,
        },
        input_sockets={
            'mask': ('Mask', 'Mask', 0, 0.0),
            'size': ('Size', 'Size', 1, 0),
            'type': ('Type', 'Type', 2, 'Steps'),
            'falloff_size': ('Falloff Size', 'Falloff Size', 3, 0.0),
            'falloff': ('Falloff', 'Falloff', 4, 'Smooth'),
        },
        properties={
        },
        output_sockets={
            'mask': ('Mask', 'Mask', 0, 'AUTO'),
        },
        output_type=CompositorNodeDilateErodeOutputs,
    )

class CompositorNodeDBlurOutputs(typing.NamedTuple):
    'Outputs from Directional Blur: Blur an image along a direction'
    image: Socket[Color]

def directional_blur(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), samples: int | Socket[int] = 1, center: Vector2 | Socket[Vector2] = (0.5, 0.5), rotation: float | Socket[float] = 0.0, scale: float | Socket[float] = 1.0, amount: float | Socket[float] = 0.0, direction: float | Socket[float] = 0.0) -> CompositorNodeDBlurOutputs:
    'Blur an image along a direction'
    return _node_function(
        'CompositorNodeDBlur',
        inputs={
            'image': image,
            'samples': samples,
            'center': center,
            'rotation': rotation,
            'scale': scale,
            'amount': amount,
            'direction': direction,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'samples': ('Samples', 'Samples', 1, 1),
            'center': ('Center', 'Center', 2, (0.5, 0.5)),
            'rotation': ('Rotation', 'Rotation', 3, 0.0),
            'scale': ('Scale', 'Scale', 4, 1.0),
            'amount': ('Translation Amount', 'Amount', 5, 0.0),
            'direction': ('Translation Direction', 'Direction', 6, 0.0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeDBlurOutputs,
    )

class CompositorNodeDisplaceOutputs(typing.NamedTuple):
    'Outputs from Displace: Displace pixel position using an offset vector'
    image: Socket[Color]

def displace(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), displacement: Vector2 | Socket[Vector2] = (0.0, 0.0), interpolation: Menu | Socket[Menu] = 'Bilinear', extension_x: Menu | Socket[Menu] = 'Clip', extension_y: Menu | Socket[Menu] = 'Clip') -> CompositorNodeDisplaceOutputs:
    'Displace pixel position using an offset vector'
    return _node_function(
        'CompositorNodeDisplace',
        inputs={
            'image': image,
            'displacement': displacement,
            'interpolation': interpolation,
            'extension_x': extension_x,
            'extension_y': extension_y,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'displacement': ('Displacement', 'Displacement', 1, (0.0, 0.0)),
            'interpolation': ('Interpolation', 'Interpolation', 2, 'Bilinear'),
            'extension_x': ('Extension X', 'Extension X', 3, 'Clip'),
            'extension_y': ('Extension Y', 'Extension Y', 4, 'Clip'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeDisplaceOutputs,
    )

class CompositorNodeDistanceMatteOutputs(typing.NamedTuple):
    'Outputs from Distance Key: Create matte based on 3D distance between colors'
    image: Socket[Color]
    matte: Socket[float]

def distance_key(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), key_color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), color_space: Menu | Socket[Menu] = 'RGB', tolerance: float | Socket[float] = 0.10000000149011612, falloff: float | Socket[float] = 0.10000000149011612) -> CompositorNodeDistanceMatteOutputs:
    'Create matte based on 3D distance between colors'
    return _node_function(
        'CompositorNodeDistanceMatte',
        inputs={
            'image': image,
            'key_color': key_color,
            'color_space': color_space,
            'tolerance': tolerance,
            'falloff': falloff,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'key_color': ('Key Color', 'Key Color', 1, (1.0, 1.0, 1.0, 1.0)),
            'color_space': ('Color Space', 'Color Space', 2, 'RGB'),
            'tolerance': ('Tolerance', 'Tolerance', 3, 0.10000000149011612),
            'falloff': ('Falloff', 'Falloff', 4, 0.10000000149011612),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'matte': ('Matte', 'Matte', 1, 'AUTO'),
        },
        output_type=CompositorNodeDistanceMatteOutputs,
    )

class CompositorNodeDoubleEdgeMaskOutputs(typing.NamedTuple):
    'Outputs from Double Edge Mask: Create a gradient between two masks'
    mask: Socket[float]

def double_edge_mask(*, outer_mask: float | Socket[float] = 0.800000011920929, inner_mask: float | Socket[float] = 0.800000011920929, image_edges: bool | Socket[bool] = False, only_inside_outer: bool | Socket[bool] = False) -> CompositorNodeDoubleEdgeMaskOutputs:
    'Create a gradient between two masks'
    return _node_function(
        'CompositorNodeDoubleEdgeMask',
        inputs={
            'outer_mask': outer_mask,
            'inner_mask': inner_mask,
            'image_edges': image_edges,
            'only_inside_outer': only_inside_outer,
        },
        input_sockets={
            'outer_mask': ('Outer Mask', 'Outer Mask', 0, 0.800000011920929),
            'inner_mask': ('Inner Mask', 'Inner Mask', 1, 0.800000011920929),
            'image_edges': ('Image Edges', 'Image Edges', 2, False),
            'only_inside_outer': ('Only Inside Outer', 'Only Inside Outer', 3, False),
        },
        properties={
        },
        output_sockets={
            'mask': ('Mask', 'Mask', 0, 'AUTO'),
        },
        output_type=CompositorNodeDoubleEdgeMaskOutputs,
    )

class CompositorNodeEllipseMaskOutputs(typing.NamedTuple):
    'Outputs from Ellipse Mask: Create elliptical mask suitable for use as a simple matte or vignette mask'
    mask: Socket[float]

def ellipse_mask(*, operation: Menu | Socket[Menu] = 'Add', mask: float | Socket[float] = 0.0, value: float | Socket[float] = 1.0, position: Vector2 | Socket[Vector2] = (0.5, 0.5), size: Vector2 | Socket[Vector2] = (0.20000000298023224, 0.10000000149011612), rotation: float | Socket[float] = 0.0) -> CompositorNodeEllipseMaskOutputs:
    'Create elliptical mask suitable for use as a simple matte or vignette mask'
    return _node_function(
        'CompositorNodeEllipseMask',
        inputs={
            'operation': operation,
            'mask': mask,
            'value': value,
            'position': position,
            'size': size,
            'rotation': rotation,
        },
        input_sockets={
            'operation': ('Operation', 'Operation', 0, 'Add'),
            'mask': ('Mask', 'Mask', 1, 0.0),
            'value': ('Value', 'Value', 2, 1.0),
            'position': ('Position', 'Position', 3, (0.5, 0.5)),
            'size': ('Size', 'Size', 4, (0.20000000298023224, 0.10000000149011612)),
            'rotation': ('Rotation', 'Rotation', 5, 0.0),
        },
        properties={
        },
        output_sockets={
            'mask': ('Mask', 'Mask', 0, 'AUTO'),
        },
        output_type=CompositorNodeEllipseMaskOutputs,
    )

class NodeEnableOutputOutputs(typing.NamedTuple):
    'Outputs from Enable Output: Either pass through the input value or output the fallback value'
    value: Socket[float | int | bool | Vector | Color | Rotation | Matrix | str | Menu | Object | Font | IntVector3]

def enable_output(*, enable: bool | Socket[bool] = False, value: float | int | bool | Vector | Color | Rotation | Matrix | str | Menu | Object | Font | IntVector3 | Socket[float | int | bool | Vector | Color | Rotation | Matrix | str | Menu | Object | Font | IntVector3] = 0.0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> NodeEnableOutputOutputs:
    'Either pass through the input value or output the fallback value\n\nArgs:\n    data_type:  Inferred from the linked inputs when None.'
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
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'INT': {'value': 'INT'}, 'BOOLEAN': {'value': 'BOOLEAN'}, 'VECTOR': {'value': 'VECTOR'}, 'RGBA': {'value': 'RGBA'}, 'ROTATION': {'value': 'ROTATION'}, 'MATRIX': {'value': 'MATRIX'}, 'STRING': {'value': 'STRING'}, 'MENU': {'value': 'MENU'}, 'OBJECT': {'value': 'OBJECT'}, 'FONT': {'value': 'FONT'}, 'INT_VECTOR': {'value': 'INT_VECTOR'}}},
    )

class FunctionNodeEulerToRotationOutputs(typing.NamedTuple):
    'Outputs from Euler to Rotation: Build a rotation from separate angles around each axis'
    rotation: Socket[Rotation]

def euler_to_rotation(*, euler: Vector | Socket[Vector] = (0.0, 0.0, 0.0)) -> FunctionNodeEulerToRotationOutputs:
    'Build a rotation from separate angles around each axis'
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

class CompositorNodeExposureOutputs(typing.NamedTuple):
    'Outputs from Exposure: Adjust brightness using a camera exposure parameter'
    image: Socket[Color]

def exposure(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), exposure: float | Socket[float] = 0.0) -> CompositorNodeExposureOutputs:
    'Adjust brightness using a camera exposure parameter'
    return _node_function(
        'CompositorNodeExposure',
        inputs={
            'image': image,
            'exposure': exposure,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'exposure': ('Exposure', 'Exposure', 1, 0.0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeExposureOutputs,
    )

def file_output(*, directory: str = '/tmp/', file_name: str = '{blend_name}', save_as_render: bool = True, use_file_extension: bool = True, **items: typing.Any) -> None:
    'Write image file to disk\n\nArgs:\n    directory: The directory where the image will be written\n    file_name: The base name of the file. Other information might be included in the final file name depending on the node options\n    save_as_render: Apply render part of display transform when saving byte image\n    use_file_extension: Add the file format extensions to the saved file name (eg: filename + .jpg)\n    items: Items to add, by name; each socket type is inferred from its value.'
    return _node_function(
        'CompositorNodeOutputFile',
        inputs={
        },
        input_sockets={
        },
        properties={
            'directory': directory,
            'file_name': file_name,
            'save_as_render': save_as_render,
            'use_file_extension': use_file_extension,
        },
        output_sockets={
        },
        output_type=None,
        item_collections=(
            ('file_output_items', 'values', items),
        ),
    )

class CompositorNodeFilterOutputs(typing.NamedTuple):
    'Outputs from Filter: Apply common image enhancement filters'
    image: Socket[Color]

def filter(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), factor: float | Socket[float] = 1.0, type: Menu | Socket[Menu] = 'Soften') -> CompositorNodeFilterOutputs:
    'Apply common image enhancement filters'
    return _node_function(
        'CompositorNodeFilter',
        inputs={
            'image': image,
            'factor': factor,
            'type': type,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'factor': ('Fac', 'Factor', 1, 1.0),
            'type': ('Type', 'Type', 2, 'Soften'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeFilterOutputs,
    )

class FunctionNodeFindInStringOutputs(typing.NamedTuple):
    'Outputs from Find in String: Find the number of times a given string occurs in another string and the position of the first match'
    first_found: Socket[int]
    count: Socket[int]

def find_in_string(*, string: str | Socket[str] = '', search: str | Socket[str] = '', mode: Menu | Socket[Menu] = 'From Start') -> FunctionNodeFindInStringOutputs:
    'Find the number of times a given string occurs in another string and the position of the first match'
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

class CompositorNodeFlipOutputs(typing.NamedTuple):
    'Outputs from Flip: Flip an image along a defined axis'
    image: Socket[Color]

def flip(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), flip_x: bool | Socket[bool] = False, flip_y: bool | Socket[bool] = False) -> CompositorNodeFlipOutputs:
    'Flip an image along a defined axis'
    return _node_function(
        'CompositorNodeFlip',
        inputs={
            'image': image,
            'flip_x': flip_x,
            'flip_y': flip_y,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'flip_x': ('Flip X', 'Flip X', 1, False),
            'flip_y': ('Flip Y', 'Flip Y', 2, False),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeFlipOutputs,
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

class GeometryNodeInputFontOutputs(typing.NamedTuple):
    'Outputs from Font: Output a font'
    font: Socket[Font]

def font(*, font: bpy.types.VectorFont | None = None) -> GeometryNodeInputFontOutputs:
    'Output a font'
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
    'Outputs from Format String: Insert values into a string using a Python and path template compatible formatting syntax'
    string: Socket[str]

def format_string(*, format: str | Socket[str] = '', **items: typing.Any) -> FunctionNodeFormatStringOutputs:
    'Insert values into a string using a Python and path template compatible formatting syntax\n\nArgs:\n    items: Items to add, by name; each socket type is inferred from its value.'
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

class CompositorNodeGlareOutputs(typing.NamedTuple):
    'Outputs from Glare: Add lens flares, fog and glows around bright parts of the image'
    image: Socket[Color]
    glare: Socket[Color]
    highlights: Socket[Color]

def glare(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), type: Menu | Socket[Menu] = 'Streaks', quality: Menu | Socket[Menu] = 'Medium', threshold: float | Socket[float] = 1.0, smoothness: float | Socket[float] = 0.10000000149011612, clamp: bool | Socket[bool] = False, maximum: float | Socket[float] = 10.0, strength: float | Socket[float] = 1.0, saturation: float | Socket[float] = 1.0, tint: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), size: float | Socket[float] = 0.5, streaks: int | Socket[int] = 4, streaks_angle: float | Socket[float] = 0.0, iterations: int | Socket[int] = 3, fade: float | Socket[float] = 0.8999999761581421, color_modulation: float | Socket[float] = 0.25, diagonal: bool | Socket[bool] = True, sun_position: Vector2 | Socket[Vector2] = (0.5, 0.5), jitter: float | Socket[float] = 0.0, kernel_data_type: Menu | Socket[Menu] = 'Float', kernel: float | Socket[float] = 0.0, kernel_2: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)) -> CompositorNodeGlareOutputs:
    'Add lens flares, fog and glows around bright parts of the image'
    return _node_function(
        'CompositorNodeGlare',
        inputs={
            'image': image,
            'type': type,
            'quality': quality,
            'threshold': threshold,
            'smoothness': smoothness,
            'clamp': clamp,
            'maximum': maximum,
            'strength': strength,
            'saturation': saturation,
            'tint': tint,
            'size': size,
            'streaks': streaks,
            'streaks_angle': streaks_angle,
            'iterations': iterations,
            'fade': fade,
            'color_modulation': color_modulation,
            'diagonal': diagonal,
            'sun_position': sun_position,
            'jitter': jitter,
            'kernel_data_type': kernel_data_type,
            'kernel': kernel,
            'kernel_2': kernel_2,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'type': ('Type', 'Type', 1, 'Streaks'),
            'quality': ('Quality', 'Quality', 2, 'Medium'),
            'threshold': ('Highlights Threshold', 'Threshold', 3, 1.0),
            'smoothness': ('Highlights Smoothness', 'Smoothness', 4, 0.10000000149011612),
            'clamp': ('Clamp Highlights', 'Clamp', 5, False),
            'maximum': ('Maximum Highlights', 'Maximum', 6, 10.0),
            'strength': ('Strength', 'Strength', 7, 1.0),
            'saturation': ('Saturation', 'Saturation', 8, 1.0),
            'tint': ('Tint', 'Tint', 9, (1.0, 1.0, 1.0, 1.0)),
            'size': ('Size', 'Size', 10, 0.5),
            'streaks': ('Streaks', 'Streaks', 11, 4),
            'streaks_angle': ('Streaks Angle', 'Streaks Angle', 12, 0.0),
            'iterations': ('Iterations', 'Iterations', 13, 3),
            'fade': ('Fade', 'Fade', 14, 0.8999999761581421),
            'color_modulation': ('Color Modulation', 'Color Modulation', 15, 0.25),
            'diagonal': ('Diagonal Star', 'Diagonal', 16, True),
            'sun_position': ('Sun Position', 'Sun Position', 17, (0.5, 0.5)),
            'jitter': ('Jitter', 'Jitter', 18, 0.0),
            'kernel_data_type': ('Kernel Data Type', 'Kernel Data Type', 19, 'Float'),
            'kernel': ('Float Kernel', 'Kernel', 20, 0.0),
            'kernel_2': ('Color Kernel', 'Kernel', 21, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'glare': ('Glare', 'Glare', 1, 'AUTO'),
            'highlights': ('Highlights', 'Highlights', 2, 'AUTO'),
        },
        output_type=CompositorNodeGlareOutputs,
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

class CompositorNodeHueCorrectOutputs(typing.NamedTuple):
    'Outputs from Hue Correct: Adjust hue, saturation, and value with a curve'
    image: Socket[Color]

def hue_correct(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), factor: float | Socket[float] = 1.0) -> CompositorNodeHueCorrectOutputs:
    'Adjust hue, saturation, and value with a curve'
    return _node_function(
        'CompositorNodeHueCorrect',
        inputs={
            'image': image,
            'factor': factor,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'factor': ('Fac', 'Factor', 1, 1.0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeHueCorrectOutputs,
    )

class CompositorNodeHueSatOutputs(typing.NamedTuple):
    'Outputs from Hue/Saturation/Value: Apply a color transformation in the HSV color model'
    image: Socket[Color]

def hue_saturation_value(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), hue: float | Socket[float] = 0.5, saturation: float | Socket[float] = 1.0, value: float | Socket[float] = 1.0, factor: float | Socket[float] = 1.0) -> CompositorNodeHueSatOutputs:
    'Apply a color transformation in the HSV color model'
    return _node_function(
        'CompositorNodeHueSat',
        inputs={
            'image': image,
            'hue': hue,
            'saturation': saturation,
            'value': value,
            'factor': factor,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'hue': ('Hue', 'Hue', 1, 0.5),
            'saturation': ('Saturation', 'Saturation', 2, 1.0),
            'value': ('Value', 'Value', 3, 1.0),
            'factor': ('Fac', 'Factor', 4, 1.0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeHueSatOutputs,
    )

class CompositorNodeIDMaskOutputs(typing.NamedTuple):
    'Outputs from ID Mask: Create a matte from an object or material index pass'
    alpha: Socket[float]

def id_mask(*, id_value: float | Socket[float] = 1.0, index: int | Socket[int] = 0, anti_alias: bool | Socket[bool] = False) -> CompositorNodeIDMaskOutputs:
    'Create a matte from an object or material index pass'
    return _node_function(
        'CompositorNodeIDMask',
        inputs={
            'id_value': id_value,
            'index': index,
            'anti_alias': anti_alias,
        },
        input_sockets={
            'id_value': ('ID value', 'ID value', 0, 1.0),
            'index': ('Index', 'Index', 1, 0),
            'anti_alias': ('Anti-Alias', 'Anti-Alias', 2, False),
        },
        properties={
        },
        output_sockets={
            'alpha': ('Alpha', 'Alpha', 0, 'AUTO'),
        },
        output_type=CompositorNodeIDMaskOutputs,
    )

class CompositorNodeImageOutputs(typing.NamedTuple):
    'Outputs from Image: Input image or movie file'
    image: Socket[Color]
    alpha: Socket[float]

def image(*, image: bpy.types.Image | None = None, frame_duration: int = 1, frame_start: int = 1, frame_offset: int = 0, use_cyclic: bool = False, use_auto_refresh: bool = True, layer: str | None = None, view: str | None = None) -> CompositorNodeImageOutputs:
    'Input image or movie file\n\nArgs:\n    frame_duration: Number of images of a movie to use\n    frame_start: Global starting frame of the movie/sequence, assuming first picture has a #1\n    frame_offset: Offset the number of the frame to use in the animation\n    use_cyclic: Cycle the images in the movie\n    use_auto_refresh: Always refresh image on frame changes'
    return _node_function(
        'CompositorNodeImage',
        inputs={
        },
        input_sockets={
        },
        properties={
            'image': image,
            'frame_duration': frame_duration,
            'frame_start': frame_start,
            'frame_offset': frame_offset,
            'use_cyclic': use_cyclic,
            'use_auto_refresh': use_auto_refresh,
            'layer': layer,
            'view': view,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 1, 'AUTO'),
        },
        output_type=CompositorNodeImageOutputs,
    )

class CompositorNodeImageCoordinatesOutputs(typing.NamedTuple):
    'Outputs from Image Coordinates: Returns the coordinates of the pixels of an image'
    uniform: Socket[Vector2]
    normalized: Socket[Vector2]
    pixel: Socket[IntVector2]

def image_coordinates(*, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)) -> CompositorNodeImageCoordinatesOutputs:
    'Returns the coordinates of the pixels of an image'
    return _node_function(
        'CompositorNodeImageCoordinates',
        inputs={
            'image': image,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
        },
        properties={
        },
        output_sockets={
            'uniform': ('Uniform', 'Uniform', 0, 'AUTO'),
            'normalized': ('Normalized', 'Normalized', 1, 'AUTO'),
            'pixel': ('Pixel', 'Pixel', 2, 'AUTO'),
        },
        output_type=CompositorNodeImageCoordinatesOutputs,
    )

class CompositorNodeImageInfoOutputs(typing.NamedTuple):
    'Outputs from Image Info: Returns information about an image'
    dimensions: Socket[IntVector2]
    resolution: Socket[IntVector2]
    location: Socket[Vector2]
    rotation: Socket[float]
    scale: Socket[Vector2]

def image_info(*, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)) -> CompositorNodeImageInfoOutputs:
    'Returns information about an image'
    return _node_function(
        'CompositorNodeImageInfo',
        inputs={
            'image': image,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
        },
        properties={
        },
        output_sockets={
            'dimensions': ('Dimensions', 'Dimensions', 0, 'AUTO'),
            'resolution': ('Resolution', 'Resolution', 1, 'AUTO'),
            'location': ('Location', 'Location', 2, 'AUTO'),
            'rotation': ('Rotation', 'Rotation', 3, 'AUTO'),
            'scale': ('Scale', 'Scale', 4, 'AUTO'),
        },
        output_type=CompositorNodeImageInfoOutputs,
    )

class GeometryNodeIndexSwitchOutputs(typing.NamedTuple):
    'Outputs from Index Switch: Choose between an arbitrary number of values with an index'
    output: Socket[Color | float | int | bool | Vector | Rotation | Matrix | str | Menu | Object | Font | IntVector3]

def index_switch(*, index: int | Socket[int] = 0, data_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None, items: typing.Sequence[typing.Any] = ()) -> GeometryNodeIndexSwitchOutputs:
    'Choose between an arbitrary number of values with an index\n\nArgs:\n    data_type:  Inferred from the linked inputs when None.\n    items: Item input values, in order.'
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
        type_properties={'data_type': {'FLOAT': {}, 'INT': {}, 'BOOLEAN': {}, 'VECTOR': {}, 'RGBA': {}, 'ROTATION': {}, 'MATRIX': {}, 'STRING': {}, 'MENU': {}, 'OBJECT': {}, 'FONT': {}, 'INT_VECTOR': {}}},
    )

class CompositorNodeInpaintOutputs(typing.NamedTuple):
    'Outputs from Inpaint: Extend borders of an image into transparent or masked regions'
    image: Socket[Color]

def inpaint(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), size: int | Socket[int] = 0) -> CompositorNodeInpaintOutputs:
    'Extend borders of an image into transparent or masked regions'
    return _node_function(
        'CompositorNodeInpaint',
        inputs={
            'image': image,
            'size': size,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'size': ('Size', 'Size', 1, 0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeInpaintOutputs,
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

class FunctionNodeInputIntVectorOutputs(typing.NamedTuple):
    'Outputs from Integer Vector: Provide an integer vector value that can be connected to other nodes in the tree'
    vector: Socket[IntVector3]

def integer_vector(*, vector: IntVector3 = (0, 0, 0), vector_dimensions: int = 3) -> FunctionNodeInputIntVectorOutputs:
    'Provide an integer vector value that can be connected to other nodes in the tree\n\nArgs:\n    vector_dimensions: Dimensions of the vector socket'
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

class CompositorNodeInvertOutputs(typing.NamedTuple):
    'Outputs from Invert Color: Invert colors, producing a negative'
    color: Socket[Color]

def invert_color(*, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), factor: float | Socket[float] = 1.0, invert_color: bool | Socket[bool] = True, invert_alpha: bool | Socket[bool] = False) -> CompositorNodeInvertOutputs:
    'Invert colors, producing a negative'
    return _node_function(
        'CompositorNodeInvert',
        inputs={
            'color': color,
            'factor': factor,
            'invert_color': invert_color,
            'invert_alpha': invert_alpha,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (1.0, 1.0, 1.0, 1.0)),
            'factor': ('Fac', 'Factor', 1, 1.0),
            'invert_color': ('Invert Color', 'Invert Color', 2, True),
            'invert_alpha': ('Invert Alpha', 'Invert Alpha', 3, False),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=CompositorNodeInvertOutputs,
    )

class FunctionNodeInvertMatrixOutputs(typing.NamedTuple):
    'Outputs from Invert Matrix: Compute the inverse of the given matrix, if one exists'
    matrix: Socket[Matrix]
    invertible: Socket[bool]

def invert_matrix(*, matrix: Matrix | Socket[Matrix] | None = None) -> FunctionNodeInvertMatrixOutputs:
    'Compute the inverse of the given matrix, if one exists'
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
    'Outputs from Invert Rotation: Compute the inverse of the given rotation'
    rotation: Socket[Rotation]

def invert_rotation(*, rotation: Rotation | Socket[Rotation] = (0.0, 0.0, 0.0)) -> FunctionNodeInvertRotationOutputs:
    'Compute the inverse of the given rotation'
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

class CompositorNodeKeyingOutputs(typing.NamedTuple):
    'Outputs from Keying: Perform both chroma keying (to remove the backdrop) and despill (to correct color cast from the backdrop)'
    image: Socket[Color]
    matte: Socket[float]
    edges: Socket[float]

def keying(*, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), key_color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), blur_size: int | Socket[int] = 0, balance: float | Socket[float] = 0.5, black_level: float | Socket[float] = 0.0, white_level: float | Socket[float] = 1.0, size: int | Socket[int] = 3, tolerance: float | Socket[float] = 0.10000000149011612, garbage_matte: float | Socket[float] = 0.0, core_matte: float | Socket[float] = 0.0, blur_size_2: int | Socket[int] = 0, dilate_size: int | Socket[int] = 0, feather_size: int | Socket[int] = 0, feather_falloff: Menu | Socket[Menu] = 'Smooth', strength: float | Socket[float] = 1.0, balance_2: float | Socket[float] = 0.5) -> CompositorNodeKeyingOutputs:
    'Perform both chroma keying (to remove the backdrop) and despill (to correct color cast from the backdrop)'
    return _node_function(
        'CompositorNodeKeying',
        inputs={
            'image': image,
            'key_color': key_color,
            'blur_size': blur_size,
            'balance': balance,
            'black_level': black_level,
            'white_level': white_level,
            'size': size,
            'tolerance': tolerance,
            'garbage_matte': garbage_matte,
            'core_matte': core_matte,
            'blur_size_2': blur_size_2,
            'dilate_size': dilate_size,
            'feather_size': feather_size,
            'feather_falloff': feather_falloff,
            'strength': strength,
            'balance_2': balance_2,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'key_color': ('Key Color', 'Key Color', 1, (1.0, 1.0, 1.0, 1.0)),
            'blur_size': ('Preprocess Blur Size', 'Blur Size', 2, 0),
            'balance': ('Key Balance', 'Balance', 3, 0.5),
            'black_level': ('Black Level', 'Black Level', 4, 0.0),
            'white_level': ('White Level', 'White Level', 5, 1.0),
            'size': ('Edge Search Size', 'Size', 6, 3),
            'tolerance': ('Edge Tolerance', 'Tolerance', 7, 0.10000000149011612),
            'garbage_matte': ('Garbage Matte', 'Garbage Matte', 8, 0.0),
            'core_matte': ('Core Matte', 'Core Matte', 9, 0.0),
            'blur_size_2': ('Postprocess Blur Size', 'Blur Size', 10, 0),
            'dilate_size': ('Postprocess Dilate Size', 'Dilate Size', 11, 0),
            'feather_size': ('Postprocess Feather Size', 'Feather Size', 12, 0),
            'feather_falloff': ('Feather Falloff', 'Feather Falloff', 13, 'Smooth'),
            'strength': ('Despill Strength', 'Strength', 14, 1.0),
            'balance_2': ('Despill Balance', 'Balance', 15, 0.5),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'matte': ('Matte', 'Matte', 1, 'AUTO'),
            'edges': ('Edges', 'Edges', 2, 'AUTO'),
        },
        output_type=CompositorNodeKeyingOutputs,
    )

class CompositorNodeKeyingScreenOutputs(typing.NamedTuple):
    'Outputs from Keying Screen: Create plates for use as a color reference for keying nodes'
    screen: Socket[Color]

def keying_screen(*, smoothness: float | Socket[float] = 0.0, clip: bpy.types.MovieClip | None = None, tracking_object: str = '') -> CompositorNodeKeyingScreenOutputs:
    'Create plates for use as a color reference for keying nodes'
    return _node_function(
        'CompositorNodeKeyingScreen',
        inputs={
            'smoothness': smoothness,
        },
        input_sockets={
            'smoothness': ('Smoothness', 'Smoothness', 0, 0.0),
        },
        properties={
            'clip': clip,
            'tracking_object': tracking_object,
        },
        output_sockets={
            'screen': ('Screen', 'Screen', 0, 'AUTO'),
        },
        output_type=CompositorNodeKeyingScreenOutputs,
    )

class CompositorNodeKuwaharaOutputs(typing.NamedTuple):
    'Outputs from Kuwahara: Apply smoothing filter that preserves edges, for stylized and painterly effects'
    image: Socket[Color]

def kuwahara(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), size: float | Socket[float] = 6.0, type: Menu | Socket[Menu] = 'Anisotropic', uniformity: int | Socket[int] = 4, sharpness: float | Socket[float] = 1.0, eccentricity: float | Socket[float] = 1.0, high_precision: bool | Socket[bool] = False) -> CompositorNodeKuwaharaOutputs:
    'Apply smoothing filter that preserves edges, for stylized and painterly effects'
    return _node_function(
        'CompositorNodeKuwahara',
        inputs={
            'image': image,
            'size': size,
            'type': type,
            'uniformity': uniformity,
            'sharpness': sharpness,
            'eccentricity': eccentricity,
            'high_precision': high_precision,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'size': ('Size', 'Size', 1, 6.0),
            'type': ('Type', 'Type', 2, 'Anisotropic'),
            'uniformity': ('Uniformity', 'Uniformity', 3, 4),
            'sharpness': ('Sharpness', 'Sharpness', 4, 1.0),
            'eccentricity': ('Eccentricity', 'Eccentricity', 5, 1.0),
            'high_precision': ('High Precision', 'High Precision', 6, False),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeKuwaharaOutputs,
    )

class CompositorNodeLensdistOutputs(typing.NamedTuple):
    'Outputs from Lens Distortion: Simulate distortion and dispersion from camera lenses'
    image: Socket[Color]

def lens_distortion(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), type: Menu | Socket[Menu] = 'Radial', distortion: float | Socket[float] = 0.0, dispersion: float | Socket[float] = 0.0, jitter: bool | Socket[bool] = False, fit: bool | Socket[bool] = False) -> CompositorNodeLensdistOutputs:
    'Simulate distortion and dispersion from camera lenses'
    return _node_function(
        'CompositorNodeLensdist',
        inputs={
            'image': image,
            'type': type,
            'distortion': distortion,
            'dispersion': dispersion,
            'jitter': jitter,
            'fit': fit,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'type': ('Type', 'Type', 1, 'Radial'),
            'distortion': ('Distortion', 'Distortion', 2, 0.0),
            'dispersion': ('Dispersion', 'Dispersion', 3, 0.0),
            'jitter': ('Jitter', 'Jitter', 4, False),
            'fit': ('Fit', 'Fit', 5, False),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeLensdistOutputs,
    )

class CompositorNodeLevelsOutputs(typing.NamedTuple):
    'Outputs from Levels: Compute average and standard deviation of pixel values'
    mean: Socket[float]
    standard_deviation: Socket[float]
    minimum: Socket[float]
    maximum: Socket[float]

def levels(*, image: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), channel: Menu | Socket[Menu] = 'Combined') -> CompositorNodeLevelsOutputs:
    'Compute average and standard deviation of pixel values'
    return _node_function(
        'CompositorNodeLevels',
        inputs={
            'image': image,
            'channel': channel,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.0, 0.0, 0.0, 1.0)),
            'channel': ('Channel', 'Channel', 1, 'Combined'),
        },
        properties={
        },
        output_sockets={
            'mean': ('Mean', 'Mean', 0, 'AUTO'),
            'standard_deviation': ('Standard Deviation', 'Standard Deviation', 1, 'AUTO'),
            'minimum': ('Minimum', 'Minimum', 2, 'AUTO'),
            'maximum': ('Maximum', 'Maximum', 3, 'AUTO'),
        },
        output_type=CompositorNodeLevelsOutputs,
    )

class CompositorNodeLumaMatteOutputs(typing.NamedTuple):
    'Outputs from Luminance Key: Create a matte based on luminance (brightness) difference'
    image: Socket[Color]
    matte: Socket[float]

def luminance_key(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), minimum: float | Socket[float] = 0.0, maximum: float | Socket[float] = 1.0) -> CompositorNodeLumaMatteOutputs:
    'Create a matte based on luminance (brightness) difference'
    return _node_function(
        'CompositorNodeLumaMatte',
        inputs={
            'image': image,
            'minimum': minimum,
            'maximum': maximum,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'minimum': ('Minimum', 'Minimum', 1, 0.0),
            'maximum': ('Maximum', 'Maximum', 2, 1.0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'matte': ('Matte', 'Matte', 1, 'AUTO'),
        },
        output_type=CompositorNodeLumaMatteOutputs,
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

class CompositorNodeMapUVOutputs(typing.NamedTuple):
    'Outputs from Map UV: Map a texture using UV coordinates, to apply a texture to objects in compositing'
    image: Socket[Color]

def map_uv(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), uv: Vector | Socket[Vector] = (1.0, 0.0, 0.0), interpolation: Menu | Socket[Menu] = 'Bilinear', extension_x: Menu | Socket[Menu] = 'Clip', extension_y: Menu | Socket[Menu] = 'Clip') -> CompositorNodeMapUVOutputs:
    'Map a texture using UV coordinates, to apply a texture to objects in compositing'
    return _node_function(
        'CompositorNodeMapUV',
        inputs={
            'image': image,
            'uv': uv,
            'interpolation': interpolation,
            'extension_x': extension_x,
            'extension_y': extension_y,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'uv': ('UV', 'UV', 1, (1.0, 0.0, 0.0)),
            'interpolation': ('Interpolation', 'Interpolation', 2, 'Bilinear'),
            'extension_x': ('Extension X', 'Extension X', 3, 'Clip'),
            'extension_y': ('Extension Y', 'Extension Y', 4, 'Clip'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeMapUVOutputs,
    )

class CompositorNodeMaskOutputs(typing.NamedTuple):
    'Outputs from Mask: Input mask from a mask data-block, created in the image editor'
    mask: Socket[float]

def mask(*, size_source: Menu | Socket[Menu] = 'Scene Size', size_x: int | Socket[int] = 256, size_y: int | Socket[int] = 256, feather: bool | Socket[bool] = True, motion_blur: bool | Socket[bool] = False, samples: int | Socket[int] = 16, shutter: float | Socket[float] = 0.5, mask: bpy.types.Mask | None = None) -> CompositorNodeMaskOutputs:
    'Input mask from a mask data-block, created in the image editor'
    return _node_function(
        'CompositorNodeMask',
        inputs={
            'size_source': size_source,
            'size_x': size_x,
            'size_y': size_y,
            'feather': feather,
            'motion_blur': motion_blur,
            'samples': samples,
            'shutter': shutter,
        },
        input_sockets={
            'size_source': ('Size Source', 'Size Source', 0, 'Scene Size'),
            'size_x': ('Size X', 'Size X', 1, 256),
            'size_y': ('Size Y', 'Size Y', 2, 256),
            'feather': ('Feather', 'Feather', 3, True),
            'motion_blur': ('Motion Blur', 'Motion Blur', 4, False),
            'samples': ('Motion Blur Samples', 'Samples', 5, 16),
            'shutter': ('Motion Blur Shutter', 'Shutter', 6, 0.5),
        },
        properties={
            'mask': mask,
        },
        output_sockets={
            'mask': ('Mask', 'Mask', 0, 'AUTO'),
        },
        output_type=CompositorNodeMaskOutputs,
    )

class CompositorNodeMaskToSDFOutputs(typing.NamedTuple):
    'Outputs from Mask To SDF: Computes a signed distance field from the given mask'
    sdf: Socket[float]
    nearest_pixel: Socket[IntVector2]

def mask_to_sdf(*, mask: bool | Socket[bool] = False) -> CompositorNodeMaskToSDFOutputs:
    'Computes a signed distance field from the given mask'
    return _node_function(
        'CompositorNodeMaskToSDF',
        inputs={
            'mask': mask,
        },
        input_sockets={
            'mask': ('Mask', 'Mask', 0, False),
        },
        properties={
        },
        output_sockets={
            'sdf': ('SDF', 'SDF', 0, 'AUTO'),
            'nearest_pixel': ('Nearest Pixel', 'Nearest Pixel', 1, 'AUTO'),
        },
        output_type=CompositorNodeMaskToSDFOutputs,
    )

class FunctionNodeMatchStringOutputs(typing.NamedTuple):
    'Outputs from Match String: Check if a given string exists within another string'
    result: Socket[bool]

def match_string(*, string: str | Socket[str] = '', operation: Menu | Socket[Menu] = 'Starts With', key: str | Socket[str] = '') -> FunctionNodeMatchStringOutputs:
    'Check if a given string exists within another string'
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

class FunctionNodeMatrixDeterminantOutputs(typing.NamedTuple):
    'Outputs from Matrix Determinant: Compute the determinant of the given matrix'
    determinant: Socket[float]

def matrix_determinant(*, matrix: Matrix | Socket[Matrix] | None = None) -> FunctionNodeMatrixDeterminantOutputs:
    'Compute the determinant of the given matrix'
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
    output: Socket[Color | float | int | bool | Vector | Rotation | Matrix | str | Menu | Object | Font | IntVector3]

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
        type_properties={'data_type': {'FLOAT': {}, 'INT': {}, 'BOOLEAN': {}, 'VECTOR': {}, 'RGBA': {}, 'ROTATION': {}, 'MATRIX': {}, 'STRING': {}, 'MENU': {}, 'OBJECT': {}, 'FONT': {}, 'INT_VECTOR': {}}},
    )

class ShaderNodeMixOutputs(typing.NamedTuple):
    'Outputs from Mix: Mix values by a factor'
    result: Socket[float | Vector | Color | Rotation]

def mix(*, factor: float | Vector | Socket[float | Vector] = 1.0, a: float | Vector | Color | Rotation | Socket[float | Vector | Color | Rotation] = 0.0, b: float | Vector | Color | Rotation | Socket[float | Vector | Color | Rotation] = 0.0, data_type: typing.Literal['FLOAT', 'VECTOR', 'RGBA', 'ROTATION'] | None = None, factor_mode: typing.Literal['UNIFORM', 'NON_UNIFORM'] = 'UNIFORM', blend_type: typing.Literal['MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'] = 'MIX', clamp_factor: bool = True, clamp_result: bool = False) -> ShaderNodeMixOutputs:
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
        type_properties={'data_type': {'FLOAT': {'a': 'VALUE', 'b': 'VALUE'}, 'VECTOR': {'a': 'VECTOR', 'b': 'VECTOR'}, 'RGBA': {'a': 'RGBA', 'b': 'RGBA'}, 'ROTATION': {'a': 'ROTATION', 'b': 'ROTATION'}}},
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

class CompositorNodeMovieClipOutputs(typing.NamedTuple):
    'Outputs from Movie Clip: Input image or movie from a movie clip data-block, typically used for motion tracking'
    image: Socket[Color]
    alpha: Socket[float]
    offset_x: Socket[float]
    offset_y: Socket[float]
    scale: Socket[float]
    angle: Socket[float]

def movie_clip(*, clip: bpy.types.MovieClip | None = None) -> CompositorNodeMovieClipOutputs:
    'Input image or movie from a movie clip data-block, typically used for motion tracking'
    return _node_function(
        'CompositorNodeMovieClip',
        inputs={
        },
        input_sockets={
        },
        properties={
            'clip': clip,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 1, 'AUTO'),
            'offset_x': ('Offset X', 'Offset X', 2, 'AUTO'),
            'offset_y': ('Offset Y', 'Offset Y', 3, 'AUTO'),
            'scale': ('Scale', 'Scale', 4, 'AUTO'),
            'angle': ('Angle', 'Angle', 5, 'AUTO'),
        },
        output_type=CompositorNodeMovieClipOutputs,
    )

class CompositorNodeMovieDistortionOutputs(typing.NamedTuple):
    'Outputs from Movie Distortion: Remove lens distortion from footage, using motion tracking camera lens settings'
    image: Socket[Color]

def movie_distortion(*, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), type: Menu | Socket[Menu] = 'Undistort', clip: bpy.types.MovieClip | None = None) -> CompositorNodeMovieDistortionOutputs:
    'Remove lens distortion from footage, using motion tracking camera lens settings'
    return _node_function(
        'CompositorNodeMovieDistortion',
        inputs={
            'image': image,
            'type': type,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'type': ('Type', 'Type', 1, 'Undistort'),
        },
        properties={
            'clip': clip,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeMovieDistortionOutputs,
    )

class FunctionNodeMatrixMultiplyOutputs(typing.NamedTuple):
    'Outputs from Multiply Matrices: Perform a matrix multiplication on two input matrices'
    matrix: Socket[Matrix]

def multiply_matrices(*, matrix: Matrix | Socket[Matrix] | None = None, matrix_2: Matrix | Socket[Matrix] | None = None) -> FunctionNodeMatrixMultiplyOutputs:
    'Perform a matrix multiplication on two input matrices'
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

class ShaderNodeTexNoiseOutputs(typing.NamedTuple):
    'Outputs from Noise Texture: Generate fractal Perlin noise'
    factor: Socket[float]
    color: Socket[Color]

def noise_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), scale: float | Socket[float] = 5.0, detail: float | Socket[float] = 2.0, roughness: float | Socket[float] = 0.5, lacunarity: float | Socket[float] = 2.0, distortion: float | Socket[float] = 0.0, w: float | Socket[float] = 0.0, offset: float | Socket[float] = 0.0, gain: float | Socket[float] = 1.0, noise_dimensions: typing.Literal['1D', '2D', '3D', '4D'] = '2D', noise_type: typing.Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN'] = 'FBM', normalize: bool = True) -> ShaderNodeTexNoiseOutputs:
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

class CompositorNodeNormalOutputs(typing.NamedTuple):
    'Outputs from Normal: Input normalized normal values to other nodes in the tree'
    normal: Socket[Vector]

def normal() -> CompositorNodeNormalOutputs:
    'Input normalized normal values to other nodes in the tree'
    return _node_function(
        'CompositorNodeNormal',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'normal': ('Normal', 'Normal', 0, 'AUTO'),
        },
        output_type=CompositorNodeNormalOutputs,
    )

class CompositorNodeNormalizeOutputs(typing.NamedTuple):
    'Outputs from Normalize: Map values to 0 to 1 range, based on the minimum and maximum pixel values'
    value: Socket[float]

def normalize(*, value: float | Socket[float] = 1.0) -> CompositorNodeNormalizeOutputs:
    'Map values to 0 to 1 range, based on the minimum and maximum pixel values'
    return _node_function(
        'CompositorNodeNormalize',
        inputs={
            'value': value,
        },
        input_sockets={
            'value': ('Value', 'Value', 0, 1.0),
        },
        properties={
        },
        output_sockets={
            'value': ('Value', 'Value', 0, 'AUTO'),
        },
        output_type=CompositorNodeNormalizeOutputs,
    )

class GeometryNodeInputObjectOutputs(typing.NamedTuple):
    'Outputs from Object: Output a single object'
    object: Socket[Object]

def object_(*, object: bpy.types.Object | None = None) -> GeometryNodeInputObjectOutputs:
    'Output a single object'
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
    'Outputs from Object Info: Retrieve information from an object'
    transform: Socket[Matrix]
    location: Socket[Vector]
    rotation: Socket[Rotation]
    scale: Socket[Vector]

def object_info(*, object: Object | Socket[Object] | None = None, transform_space: typing.Literal['ORIGINAL', 'RELATIVE'] = 'ORIGINAL') -> GeometryNodeObjectInfoOutputs:
    'Retrieve information from an object\n\nArgs:\n    transform_space: The transformation of the vector and geometry outputs'
    return _node_function(
        'GeometryNodeObjectInfo',
        inputs={
            'object': object,
        },
        input_sockets={
            'object': ('Object', 'Object', 0, None),
        },
        properties={
            'transform_space': transform_space,
        },
        output_sockets={
            'transform': ('Transform', 'Transform', 0, 'AUTO'),
            'location': ('Location', 'Location', 1, 'AUTO'),
            'rotation': ('Rotation', 'Rotation', 2, 'AUTO'),
            'scale': ('Scale', 'Scale', 3, 'AUTO'),
        },
        output_type=GeometryNodeObjectInfoOutputs,
    )

class CompositorNodePixelateOutputs(typing.NamedTuple):
    'Outputs from Pixelate: Reduce detail in an image by making individual pixels more prominent, for a blocky or mosaic-like appearance'
    color: Socket[Color]

def pixelate(*, color: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), size: int | Socket[int] = 1) -> CompositorNodePixelateOutputs:
    'Reduce detail in an image by making individual pixels more prominent, for a blocky or mosaic-like appearance'
    return _node_function(
        'CompositorNodePixelate',
        inputs={
            'color': color,
            'size': size,
        },
        input_sockets={
            'color': ('Color', 'Color', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'size': ('Size', 'Size', 1, 1),
        },
        properties={
        },
        output_sockets={
            'color': ('Color', 'Color', 0, 'AUTO'),
        },
        output_type=CompositorNodePixelateOutputs,
    )

class CompositorNodePlaneTrackDeformOutputs(typing.NamedTuple):
    'Outputs from Plane Track Deform: Replace flat planes in footage by another image, detected by plane tracks from motion tracking'
    image: Socket[Color]
    plane: Socket[float]

def plane_track_deform(*, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), motion_blur: bool | Socket[bool] = False, samples: int | Socket[int] = 16, shutter: float | Socket[float] = 0.5, clip: bpy.types.MovieClip | None = None, tracking_object: str = '', plane_track_name: str = '') -> CompositorNodePlaneTrackDeformOutputs:
    'Replace flat planes in footage by another image, detected by plane tracks from motion tracking'
    return _node_function(
        'CompositorNodePlaneTrackDeform',
        inputs={
            'image': image,
            'motion_blur': motion_blur,
            'samples': samples,
            'shutter': shutter,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'motion_blur': ('Motion Blur', 'Motion Blur', 1, False),
            'samples': ('Motion Blur Samples', 'Samples', 2, 16),
            'shutter': ('Motion Blur Shutter', 'Shutter', 3, 0.5),
        },
        properties={
            'clip': clip,
            'tracking_object': tracking_object,
            'plane_track_name': plane_track_name,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'plane': ('Plane', 'Plane', 1, 'AUTO'),
        },
        output_type=CompositorNodePlaneTrackDeformOutputs,
    )

class CompositorNodePosterizeOutputs(typing.NamedTuple):
    'Outputs from Posterize: Reduce number of colors in an image, converting smooth gradients into sharp transitions'
    image: Socket[Color]

def posterize(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), steps: float | Socket[float] = 8.0) -> CompositorNodePosterizeOutputs:
    'Reduce number of colors in an image, converting smooth gradients into sharp transitions'
    return _node_function(
        'CompositorNodePosterize',
        inputs={
            'image': image,
            'steps': steps,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'steps': ('Steps', 'Steps', 1, 8.0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodePosterizeOutputs,
    )

class FunctionNodeProjectPointOutputs(typing.NamedTuple):
    'Outputs from Project Point: Project a point using a matrix, using location, rotation, scale, and perspective divide'
    vector: Socket[Vector]

def project_point(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), transform: Matrix | Socket[Matrix] | None = None) -> FunctionNodeProjectPointOutputs:
    'Project a point using a matrix, using location, rotation, scale, and perspective divide'
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

class FunctionNodeQuaternionToRotationOutputs(typing.NamedTuple):
    'Outputs from Quaternion to Rotation: Build a rotation from quaternion components'
    rotation: Socket[Rotation]

def quaternion_to_rotation(*, w: float | Socket[float] = 1.0, x: float | Socket[float] = 0.0, y: float | Socket[float] = 0.0, z: float | Socket[float] = 0.0) -> FunctionNodeQuaternionToRotationOutputs:
    'Build a rotation from quaternion components'
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

class CompositorNodeRelativeToPixelOutputs(typing.NamedTuple):
    'Outputs from Relative To Pixel: Converts values that are relative to the image size to be in terms of pixels'
    value: Socket[float | Vector2]

def relative_to_pixel(*, value: float | Vector2 | Socket[float | Vector2] = 0.0, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), data_type: typing.Literal['FLOAT', 'VECTOR'] | None = None, reference_dimension: typing.Literal['PER_DIMENSION', 'X', 'Y', 'Greater', 'Smaller', 'Diagonal'] | None = None) -> CompositorNodeRelativeToPixelOutputs:
    'Converts values that are relative to the image size to be in terms of pixels\n\nArgs:\n    data_type: The type of data Inferred from the linked inputs when None.\n    reference_dimension: Defines the dimension of the image that the relative value is in reference to Inferred from the linked inputs when None.'
    return _node_function(
        'CompositorNodeRelativeToPixel',
        inputs={
            'value': value,
            'image': image,
        },
        input_sockets={
            'value': ('Float Value', 'Value', 1, 0.0),
            'image': ('Image', 'Image', 2, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
        },
        properties={
            'data_type': data_type,
            'reference_dimension': reference_dimension,
        },
        output_sockets={
            'value': ('Float Value', 'Value', 0, 'AUTO'),
        },
        output_type=CompositorNodeRelativeToPixelOutputs,
        type_properties={'data_type': {'FLOAT': {'value': 'VALUE'}, 'VECTOR': {'value': 'VECTOR'}}, 'reference_dimension': {'PER_DIMENSION': {}, 'X': {}, 'Y': {}, 'Greater': {}, 'Smaller': {}, 'Diagonal': {}}},
    )

class CompositorNodeRLayersOutputs(typing.NamedTuple):
    'Outputs from Render Layers: Input render passes from a scene render'
    image: Socket[Color]
    alpha: Socket[float]

def render_layers(*, scene: bpy.types.Scene | None = None, layer: str | None = None) -> CompositorNodeRLayersOutputs:
    'Input render passes from a scene render'
    return _node_function(
        'CompositorNodeRLayers',
        inputs={
        },
        input_sockets={
        },
        properties={
            'scene': scene,
            'layer': layer,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 1, 'AUTO'),
        },
        output_type=CompositorNodeRLayersOutputs,
    )

class FunctionNodeReplaceStringOutputs(typing.NamedTuple):
    'Outputs from Replace String: Replace a given string segment with another'
    string: Socket[str]

def replace_string(*, string: str | Socket[str] = '', find: str | Socket[str] = '', replace: str | Socket[str] = '') -> FunctionNodeReplaceStringOutputs:
    'Replace a given string segment with another'
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

class FunctionNodeReverseStringOutputs(typing.NamedTuple):
    'Outputs from Reverse String: Reverse the order of the characters in a string'
    string: Socket[str]

def reverse_string(*, string: str | Socket[str] = '') -> FunctionNodeReverseStringOutputs:
    'Reverse the order of the characters in a string'
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

class CompositorNodeCurveRGBOutputs(typing.NamedTuple):
    'Outputs from RGB Curves: Perform level adjustments on each color channel of an image'
    image: Socket[Color]

def rgb_curves_compositor_node_curve_rgb(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), factor: float | Socket[float] = 1.0, black_level: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), white_level: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0)) -> CompositorNodeCurveRGBOutputs:
    'Perform level adjustments on each color channel of an image'
    return _node_function(
        'CompositorNodeCurveRGB',
        inputs={
            'image': image,
            'factor': factor,
            'black_level': black_level,
            'white_level': white_level,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'factor': ('Fac', 'Factor', 1, 1.0),
            'black_level': ('Black Level', 'Black Level', 2, (0.0, 0.0, 0.0, 1.0)),
            'white_level': ('White Level', 'White Level', 3, (1.0, 1.0, 1.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeCurveRGBOutputs,
    )

class ShaderNodeRGBCurveOutputs(typing.NamedTuple):
    'Outputs from RGB Curves: Apply color corrections for each color channel'
    color: Socket[Color]

def rgb_curves_shader_node_rgb_curve(*, factor: float | Socket[float] = 1.0, color: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0)) -> ShaderNodeRGBCurveOutputs:
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

class CompositorNodeRGBToBWOutputs(typing.NamedTuple):
    'Outputs from RGB to BW: Convert RGB input into grayscale using luminance'
    val: Socket[float]

def rgb_to_bw(*, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)) -> CompositorNodeRGBToBWOutputs:
    'Convert RGB input into grayscale using luminance'
    return _node_function(
        'CompositorNodeRGBToBW',
        inputs={
            'image': image,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
        },
        properties={
        },
        output_sockets={
            'val': ('Val', 'Val', 0, 'AUTO'),
        },
        output_type=CompositorNodeRGBToBWOutputs,
    )

class CompositorNodeRotateOutputs(typing.NamedTuple):
    'Outputs from Rotate: Rotate image by specified angle'
    image: Socket[Color]

def rotate(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), angle: float | Socket[float] = 0.0, interpolation: Menu | Socket[Menu] = 'Bilinear', extension_x: Menu | Socket[Menu] = 'Clip', extension_y: Menu | Socket[Menu] = 'Clip') -> CompositorNodeRotateOutputs:
    'Rotate image by specified angle'
    return _node_function(
        'CompositorNodeRotate',
        inputs={
            'image': image,
            'angle': angle,
            'interpolation': interpolation,
            'extension_x': extension_x,
            'extension_y': extension_y,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'angle': ('Angle', 'Angle', 1, 0.0),
            'interpolation': ('Interpolation', 'Interpolation', 2, 'Bilinear'),
            'extension_x': ('Extension X', 'Extension X', 3, 'Clip'),
            'extension_y': ('Extension Y', 'Extension Y', 4, 'Clip'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeRotateOutputs,
    )

class FunctionNodeRotateRotationOutputs(typing.NamedTuple):
    'Outputs from Rotate Rotation: Apply a secondary rotation to a given rotation value'
    rotation: Socket[Rotation]

def rotate_rotation(*, rotation: Rotation | Socket[Rotation] = (0.0, 0.0, 0.0), rotate_by: Rotation | Socket[Rotation] = (0.0, 0.0, 0.0), rotation_space: typing.Literal['GLOBAL', 'LOCAL'] = 'GLOBAL') -> FunctionNodeRotateRotationOutputs:
    'Apply a secondary rotation to a given rotation value\n\nArgs:\n    rotation_space: Base orientation for the rotation'
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
    'Outputs from Rotate Vector: Apply a rotation to a given vector'
    vector: Socket[Vector]

def rotate_vector(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), rotation: Rotation | Socket[Rotation] = (0.0, 0.0, 0.0)) -> FunctionNodeRotateVectorOutputs:
    'Apply a rotation to a given vector'
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
    'Outputs from Rotation: Provide a rotation value that can be connected to other nodes in the tree'
    rotation: Socket[Rotation]

def rotation(*, rotation_euler: Vector = (0.0, 0.0, 0.0)) -> FunctionNodeInputRotationOutputs:
    'Provide a rotation value that can be connected to other nodes in the tree\n\nArgs:\n    rotation_euler: Input value used for unconnected socket'
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
    'Outputs from Rotation to Axis Angle: Convert a rotation to axis angle components'
    axis: Socket[Vector]
    angle: Socket[float]

def rotation_to_axis_angle(*, rotation: Rotation | Socket[Rotation] = (0.0, 0.0, 0.0)) -> FunctionNodeRotationToAxisAngleOutputs:
    'Convert a rotation to axis angle components'
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
    'Outputs from Rotation to Euler: Convert a standard rotation value to an Euler rotation'
    euler: Socket[Vector]

def rotation_to_euler(*, rotation: Rotation | Socket[Rotation] = (0.0, 0.0, 0.0)) -> FunctionNodeRotationToEulerOutputs:
    'Convert a standard rotation value to an Euler rotation'
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
    'Outputs from Rotation to Quaternion: Retrieve the quaternion components representing a rotation'
    w: Socket[float]
    x: Socket[float]
    y: Socket[float]
    z: Socket[float]

def rotation_to_quaternion(*, rotation: Rotation | Socket[Rotation] = (0.0, 0.0, 0.0)) -> FunctionNodeRotationToQuaternionOutputs:
    'Retrieve the quaternion components representing a rotation'
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

class CompositorNodeScaleOutputs(typing.NamedTuple):
    'Outputs from Scale: Change the size of the image'
    image: Socket[Color]

def scale(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), type: Menu | Socket[Menu] = 'Relative', x: float | Socket[float] = 1.0, y: float | Socket[float] = 1.0, frame_type: Menu | Socket[Menu] = 'Stretch', interpolation: Menu | Socket[Menu] = 'Bilinear', extension_x: Menu | Socket[Menu] = 'Clip', extension_y: Menu | Socket[Menu] = 'Clip') -> CompositorNodeScaleOutputs:
    'Change the size of the image'
    return _node_function(
        'CompositorNodeScale',
        inputs={
            'image': image,
            'type': type,
            'x': x,
            'y': y,
            'frame_type': frame_type,
            'interpolation': interpolation,
            'extension_x': extension_x,
            'extension_y': extension_y,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'type': ('Type', 'Type', 1, 'Relative'),
            'x': ('X', 'X', 2, 1.0),
            'y': ('Y', 'Y', 3, 1.0),
            'frame_type': ('Frame Type', 'Frame Type', 4, 'Stretch'),
            'interpolation': ('Interpolation', 'Interpolation', 5, 'Bilinear'),
            'extension_x': ('Extension X', 'Extension X', 6, 'Clip'),
            'extension_y': ('Extension Y', 'Extension Y', 7, 'Clip'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeScaleOutputs,
    )

class CompositorNodeSceneTimeOutputs(typing.NamedTuple):
    'Outputs from Scene Time: Input the current scene time in seconds or frames'
    seconds: Socket[float]
    frame: Socket[float]

def scene_time() -> CompositorNodeSceneTimeOutputs:
    'Input the current scene time in seconds or frames'
    return _node_function(
        'CompositorNodeSceneTime',
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
        output_type=CompositorNodeSceneTimeOutputs,
    )

class CompositorNodeSeparateColorOutputs(typing.NamedTuple):
    'Outputs from Separate Color: Split an image into its composite color channels'
    red: Socket[float]
    green: Socket[float]
    blue: Socket[float]
    alpha: Socket[float]

def separate_color(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), mode: typing.Literal['RGB', 'HSV', 'HSL', 'YCC', 'YUV'] = 'RGB', ycc_mode: typing.Literal['ITUBT601', 'ITUBT709', 'JFIF'] = 'ITUBT709') -> CompositorNodeSeparateColorOutputs:
    'Split an image into its composite color channels\n\nArgs:\n    mode: Mode of color processing\n    ycc_mode: Color space used for YCbCrA processing'
    return _node_function(
        'CompositorNodeSeparateColor',
        inputs={
            'image': image,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
        },
        properties={
            'mode': mode,
            'ycc_mode': ycc_mode,
        },
        output_sockets={
            'red': ('Red', 'Red', 0, 'AUTO'),
            'green': ('Green', 'Green', 1, 'AUTO'),
            'blue': ('Blue', 'Blue', 2, 'AUTO'),
            'alpha': ('Alpha', 'Alpha', 3, 'AUTO'),
        },
        output_type=CompositorNodeSeparateColorOutputs,
    )

class FunctionNodeSeparateMatrixOutputs(typing.NamedTuple):
    'Outputs from Separate Matrix: Split a 4x4 matrix into its individual values'
    column_1_row_1: Socket[float]
    column_1_row_2: Socket[float]
    column_1_row_3: Socket[float]
    column_1_row_4: Socket[float]
    column_2_row_1: Socket[float]
    column_2_row_2: Socket[float]
    column_2_row_3: Socket[float]
    column_2_row_4: Socket[float]
    column_3_row_1: Socket[float]
    column_3_row_2: Socket[float]
    column_3_row_3: Socket[float]
    column_3_row_4: Socket[float]
    column_4_row_1: Socket[float]
    column_4_row_2: Socket[float]
    column_4_row_3: Socket[float]
    column_4_row_4: Socket[float]

def separate_matrix(*, matrix: Matrix | Socket[Matrix] | None = None) -> FunctionNodeSeparateMatrixOutputs:
    'Split a 4x4 matrix into its individual values'
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

class CompositorNodeSequencerStripInfoOutputs(typing.NamedTuple):
    'Outputs from Sequencer Strip Info: Returns information about the active strip of the modifier'
    start_frame: Socket[int]
    end_frame: Socket[int]
    location: Socket[Vector2]
    rotation: Socket[float]
    scale: Socket[Vector2]

def sequencer_strip_info() -> CompositorNodeSequencerStripInfoOutputs:
    'Returns information about the active strip of the modifier'
    return _node_function(
        'CompositorNodeSequencerStripInfo',
        inputs={
        },
        input_sockets={
        },
        properties={
        },
        output_sockets={
            'start_frame': ('Start Frame', 'Start Frame', 0, 'AUTO'),
            'end_frame': ('End Frame', 'End Frame', 1, 'AUTO'),
            'location': ('Location', 'Location', 2, 'AUTO'),
            'rotation': ('Rotation', 'Rotation', 3, 'AUTO'),
            'scale': ('Scale', 'Scale', 4, 'AUTO'),
        },
        output_type=CompositorNodeSequencerStripInfoOutputs,
    )

class CompositorNodeSetAlphaOutputs(typing.NamedTuple):
    'Outputs from Set Alpha: Add an alpha channel to an image'
    image: Socket[Color]

def set_alpha(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), alpha: float | Socket[float] = 1.0, type: Menu | Socket[Menu] = 'Apply Mask') -> CompositorNodeSetAlphaOutputs:
    'Add an alpha channel to an image'
    return _node_function(
        'CompositorNodeSetAlpha',
        inputs={
            'image': image,
            'alpha': alpha,
            'type': type,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'alpha': ('Alpha', 'Alpha', 1, 1.0),
            'type': ('Type', 'Type', 2, 'Apply Mask'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeSetAlphaOutputs,
    )

class FunctionNodeSetStringCaseOutputs(typing.NamedTuple):
    'Outputs from Set String Case: Convert the case of a string'
    string: Socket[str]

def set_string_case(*, string: str | Socket[str] = '', case: Menu | Socket[Menu] = 'Uppercase') -> FunctionNodeSetStringCaseOutputs:
    'Convert the case of a string'
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

class FunctionNodeSliceStringOutputs(typing.NamedTuple):
    'Outputs from Slice String: Extract a string segment from a larger string'
    string: Socket[str]

def slice_string(*, string: str | Socket[str] = '', position: int | Socket[int] = 0, length: int | Socket[int] = 10) -> FunctionNodeSliceStringOutputs:
    'Extract a string segment from a larger string'
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

class FunctionNodeInputSpecialCharactersOutputs(typing.NamedTuple):
    'Outputs from Special Characters: Output string characters that cannot be typed directly with the keyboard'
    line_break: Socket[str]
    tab: Socket[str]

def special_characters() -> FunctionNodeInputSpecialCharactersOutputs:
    'Output string characters that cannot be typed directly with the keyboard'
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

class CompositorNodeSplitOutputs(typing.NamedTuple):
    'Outputs from Split: Combine two images for side-by-side display. Typically used in combination with a Viewer node'
    image: Socket[Color]

def split(*, position: Vector2 | Socket[Vector2] = (0.5, 0.5), rotation: float | Socket[float] = 0.7853981852531433, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), image_2: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)) -> CompositorNodeSplitOutputs:
    'Combine two images for side-by-side display. Typically used in combination with a Viewer node'
    return _node_function(
        'CompositorNodeSplit',
        inputs={
            'position': position,
            'rotation': rotation,
            'image': image,
            'image_2': image_2,
        },
        input_sockets={
            'position': ('Position', 'Position', 0, (0.5, 0.5)),
            'rotation': ('Rotation', 'Rotation', 1, 0.7853981852531433),
            'image': ('Image', 'Image', 2, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'image_2': ('Image_001', 'Image', 3, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeSplitOutputs,
    )

class CompositorNodeStabilizeOutputs(typing.NamedTuple):
    'Outputs from Stabilize 2D: Stabilize footage using 2D stabilization motion tracking settings'
    image: Socket[Color]

def stabilize_2_d(*, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), frame: int | Socket[int] = 0, invert: bool | Socket[bool] = False, interpolation: Menu | Socket[Menu] = 'Bilinear', extension_x: Menu | Socket[Menu] = 'Clip', extension_y: Menu | Socket[Menu] = 'Clip', clip: bpy.types.MovieClip | None = None) -> CompositorNodeStabilizeOutputs:
    'Stabilize footage using 2D stabilization motion tracking settings'
    return _node_function(
        'CompositorNodeStabilize',
        inputs={
            'image': image,
            'frame': frame,
            'invert': invert,
            'interpolation': interpolation,
            'extension_x': extension_x,
            'extension_y': extension_y,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'frame': ('Frame', 'Frame', 1, 0),
            'invert': ('Invert', 'Invert', 2, False),
            'interpolation': ('Interpolation', 'Interpolation', 3, 'Bilinear'),
            'extension_x': ('Extension X', 'Extension X', 4, 'Clip'),
            'extension_y': ('Extension Y', 'Extension Y', 5, 'Clip'),
        },
        properties={
            'clip': clip,
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeStabilizeOutputs,
    )

class FunctionNodeInputStringOutputs(typing.NamedTuple):
    'Outputs from String: Provide a string value that can be connected to other nodes in the tree'
    string: Socket[str]

def string_(*, string: str = '') -> FunctionNodeInputStringOutputs:
    'Provide a string value that can be connected to other nodes in the tree'
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
    'Outputs from String Length: Output the number of characters in the given string'
    length: Socket[int]

def string_length(*, string: str | Socket[str] = '') -> FunctionNodeStringLengthOutputs:
    'Output the number of characters in the given string'
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

class CompositorNodeStringToImageOutputs(typing.NamedTuple):
    'Outputs from String To Image: Generates an image containing the given paragraph of text'
    image: Socket[float]

def string_to_image(*, string: str | Socket[str] = '', font: Font | Socket[Font] | None = None, size: float | Socket[float] = 128.0, horizontal_alignment: Menu | Socket[Menu] = 'Center', vertical_alignment: Menu | Socket[Menu] = 'Middle', wrap: bool | Socket[bool] = True, width: int | Socket[int] = 1920) -> CompositorNodeStringToImageOutputs:
    'Generates an image containing the given paragraph of text'
    return _node_function(
        'CompositorNodeStringToImage',
        inputs={
            'string': string,
            'font': font,
            'size': size,
            'horizontal_alignment': horizontal_alignment,
            'vertical_alignment': vertical_alignment,
            'wrap': wrap,
            'width': width,
        },
        input_sockets={
            'string': ('String', 'String', 0, ''),
            'font': ('Font', 'Font', 1, None),
            'size': ('Size', 'Size', 2, 128.0),
            'horizontal_alignment': ('Horizontal Alignment', 'Horizontal Alignment', 3, 'Center'),
            'vertical_alignment': ('Vertical Alignment', 'Vertical Alignment', 4, 'Middle'),
            'wrap': ('Wrap', 'Wrap', 5, True),
            'width': ('Wrap Width', 'Width', 6, 1920),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeStringToImageOutputs,
    )

class FunctionNodeStringToValueOutputs(typing.NamedTuple):
    'Outputs from String to Value: Derive a numeric value from a given string representation'
    value: Socket[float | int]
    length: Socket[int]

def string_to_value(*, string: str | Socket[str] = '', base: int | Socket[int] = 10, data_type: typing.Literal['FLOAT', 'INT'] | None = None) -> FunctionNodeStringToValueOutputs:
    'Derive a numeric value from a given string representation\n\nArgs:\n    data_type:  Inferred from the linked inputs when None.'
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

class CompositorNodeSwitchOutputs(typing.NamedTuple):
    'Outputs from Switch: Switch between two images using a checkbox'
    image: Socket[Color]

def switch_compositor_node_switch(*, switch: bool | Socket[bool] = False, off: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), on: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)) -> CompositorNodeSwitchOutputs:
    'Switch between two images using a checkbox'
    return _node_function(
        'CompositorNodeSwitch',
        inputs={
            'switch': switch,
            'off': off,
            'on': on,
        },
        input_sockets={
            'switch': ('Switch', 'Switch', 0, False),
            'off': ('Off', 'Off', 1, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'on': ('On', 'On', 2, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeSwitchOutputs,
    )

class GeometryNodeSwitchOutputs(typing.NamedTuple):
    'Outputs from Switch: Switch between two inputs'
    output: Socket[float | int | bool | Vector | Color | Rotation | Matrix | str | Menu | Object | Font | IntVector3]

def switch_geometry_node_switch(*, switch: bool | Socket[bool] = False, false: float | int | bool | Vector | Color | Rotation | Matrix | str | Menu | Object | Font | IntVector3 | Socket[float | int | bool | Vector | Color | Rotation | Matrix | str | Menu | Object | Font | IntVector3] = 0.0, true: float | int | bool | Vector | Color | Rotation | Matrix | str | Menu | Object | Font | IntVector3 | Socket[float | int | bool | Vector | Color | Rotation | Matrix | str | Menu | Object | Font | IntVector3] = 0.0, input_type: typing.Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'SHADER', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT', 'SCENE', 'TEXT', 'MASK', 'SOUND', 'INT_VECTOR'] | None = None) -> GeometryNodeSwitchOutputs:
    'Switch between two inputs\n\nArgs:\n    input_type:  Inferred from the linked inputs when None.'
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
        type_properties={'input_type': {'FLOAT': {'false': 'VALUE', 'true': 'VALUE'}, 'INT': {'false': 'INT', 'true': 'INT'}, 'BOOLEAN': {'false': 'BOOLEAN', 'true': 'BOOLEAN'}, 'VECTOR': {'false': 'VECTOR', 'true': 'VECTOR'}, 'RGBA': {'false': 'RGBA', 'true': 'RGBA'}, 'ROTATION': {'false': 'ROTATION', 'true': 'ROTATION'}, 'MATRIX': {'false': 'MATRIX', 'true': 'MATRIX'}, 'STRING': {'false': 'STRING', 'true': 'STRING'}, 'MENU': {'false': 'MENU', 'true': 'MENU'}, 'OBJECT': {'false': 'OBJECT', 'true': 'OBJECT'}, 'FONT': {'false': 'FONT', 'true': 'FONT'}, 'INT_VECTOR': {'false': 'INT_VECTOR', 'true': 'INT_VECTOR'}}},
    )

class CompositorNodeSwitchViewOutputs(typing.NamedTuple):
    'Outputs from Switch View: Combine the views (left and right) into a single stereo 3D output'
    image: Socket[Color]

def switch_view(*, left: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0), right: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0)) -> CompositorNodeSwitchViewOutputs:
    'Combine the views (left and right) into a single stereo 3D output'
    return _node_function(
        'CompositorNodeSwitchView',
        inputs={
            'left': left,
            'right': right,
        },
        input_sockets={
            'left': ('left', 'left', 0, (0.0, 0.0, 0.0, 1.0)),
            'right': ('right', 'right', 1, (0.0, 0.0, 0.0, 1.0)),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeSwitchViewOutputs,
    )

class CompositorNodeTimeOutputs(typing.NamedTuple):
    'Outputs from Time Curve: Generate a factor value (from 0.0 to 1.0) between scene start and end time, using a curve mapping'
    factor: Socket[float]

def time_curve(*, start_frame: int | Socket[int] = 1, end_frame: int | Socket[int] = 250) -> CompositorNodeTimeOutputs:
    'Generate a factor value (from 0.0 to 1.0) between scene start and end time, using a curve mapping'
    return _node_function(
        'CompositorNodeTime',
        inputs={
            'start_frame': start_frame,
            'end_frame': end_frame,
        },
        input_sockets={
            'start_frame': ('Start Frame', 'Start Frame', 0, 1),
            'end_frame': ('End Frame', 'End Frame', 1, 250),
        },
        properties={
        },
        output_sockets={
            'factor': ('Fac', 'Factor', 0, 'AUTO'),
        },
        output_type=CompositorNodeTimeOutputs,
    )

class CompositorNodeTonemapOutputs(typing.NamedTuple):
    'Outputs from Tonemap: Map one set of colors to another in order to approximate the appearance of high dynamic range'
    image: Socket[Color]

def tonemap(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), type: Menu | Socket[Menu] = 'R/D Photoreceptor', key: float | Socket[float] = 0.18000000715255737, balance: float | Socket[float] = 1.0, gamma: float | Socket[float] = 1.0, intensity: float | Socket[float] = 0.0, contrast: float | Socket[float] = 0.0, light_adaptation: float | Socket[float] = 0.0, chromatic_adaptation: float | Socket[float] = 0.0) -> CompositorNodeTonemapOutputs:
    'Map one set of colors to another in order to approximate the appearance of high dynamic range'
    return _node_function(
        'CompositorNodeTonemap',
        inputs={
            'image': image,
            'type': type,
            'key': key,
            'balance': balance,
            'gamma': gamma,
            'intensity': intensity,
            'contrast': contrast,
            'light_adaptation': light_adaptation,
            'chromatic_adaptation': chromatic_adaptation,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'type': ('Type', 'Type', 1, 'R/D Photoreceptor'),
            'key': ('Key', 'Key', 2, 0.18000000715255737),
            'balance': ('Balance', 'Balance', 3, 1.0),
            'gamma': ('Gamma', 'Gamma', 4, 1.0),
            'intensity': ('Intensity', 'Intensity', 5, 0.0),
            'contrast': ('Contrast', 'Contrast', 6, 0.0),
            'light_adaptation': ('Light Adaptation', 'Light Adaptation', 7, 0.0),
            'chromatic_adaptation': ('Chromatic Adaptation', 'Chromatic Adaptation', 8, 0.0),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeTonemapOutputs,
    )

class CompositorNodeTrackPosOutputs(typing.NamedTuple):
    'Outputs from Track Position: Provide information about motion tracking points, such as x and y values'
    x: Socket[float]
    y: Socket[float]
    speed: Socket[Vector4]

def track_position(*, mode: Menu | Socket[Menu] = 'Absolute', frame: int | Socket[int] = 0, clip: bpy.types.MovieClip | None = None, tracking_object: str = '', track_name: str = '') -> CompositorNodeTrackPosOutputs:
    'Provide information about motion tracking points, such as x and y values'
    return _node_function(
        'CompositorNodeTrackPos',
        inputs={
            'mode': mode,
            'frame': frame,
        },
        input_sockets={
            'mode': ('Mode', 'Mode', 0, 'Absolute'),
            'frame': ('Frame', 'Frame', 1, 0),
        },
        properties={
            'clip': clip,
            'tracking_object': tracking_object,
            'track_name': track_name,
        },
        output_sockets={
            'x': ('X', 'X', 0, 'AUTO'),
            'y': ('Y', 'Y', 1, 'AUTO'),
            'speed': ('Speed', 'Speed', 2, 'AUTO'),
        },
        output_type=CompositorNodeTrackPosOutputs,
    )

class CompositorNodeTransformOutputs(typing.NamedTuple):
    'Outputs from Transform: Scale, translate and rotate an image'
    image: Socket[Color]

def transform(*, image: Color | Socket[Color] = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0), x: float | Socket[float] = 0.0, y: float | Socket[float] = 0.0, angle: float | Socket[float] = 0.0, scale: float | Socket[float] = 1.0, interpolation: Menu | Socket[Menu] = 'Bilinear', extension_x: Menu | Socket[Menu] = 'Clip', extension_y: Menu | Socket[Menu] = 'Clip') -> CompositorNodeTransformOutputs:
    'Scale, translate and rotate an image'
    return _node_function(
        'CompositorNodeTransform',
        inputs={
            'image': image,
            'x': x,
            'y': y,
            'angle': angle,
            'scale': scale,
            'interpolation': interpolation,
            'extension_x': extension_x,
            'extension_y': extension_y,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)),
            'x': ('X', 'X', 1, 0.0),
            'y': ('Y', 'Y', 2, 0.0),
            'angle': ('Angle', 'Angle', 3, 0.0),
            'scale': ('Scale', 'Scale', 4, 1.0),
            'interpolation': ('Interpolation', 'Interpolation', 5, 'Bilinear'),
            'extension_x': ('Extension X', 'Extension X', 6, 'Clip'),
            'extension_y': ('Extension Y', 'Extension Y', 7, 'Clip'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeTransformOutputs,
    )

class FunctionNodeTransformDirectionOutputs(typing.NamedTuple):
    'Outputs from Transform Direction: Apply a transformation matrix (excluding translation) to the given vector'
    direction: Socket[Vector]

def transform_direction(*, direction: Vector | Socket[Vector] = (0.0, 0.0, 0.0), transform: Matrix | Socket[Matrix] | None = None) -> FunctionNodeTransformDirectionOutputs:
    'Apply a transformation matrix (excluding translation) to the given vector'
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

class FunctionNodeTransformPointOutputs(typing.NamedTuple):
    'Outputs from Transform Point: Apply a transformation matrix to the given vector'
    vector: Socket[Vector]

def transform_point(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), transform: Matrix | Socket[Matrix] | None = None) -> FunctionNodeTransformPointOutputs:
    'Apply a transformation matrix to the given vector'
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

class CompositorNodeTranslateOutputs(typing.NamedTuple):
    'Outputs from Translate: Offset an image'
    image: Socket[Color]

def translate(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), x: float | Socket[float] = 0.0, y: float | Socket[float] = 0.0, interpolation: Menu | Socket[Menu] = 'Bilinear', extension_x: Menu | Socket[Menu] = 'Clip', extension_y: Menu | Socket[Menu] = 'Clip') -> CompositorNodeTranslateOutputs:
    'Offset an image'
    return _node_function(
        'CompositorNodeTranslate',
        inputs={
            'image': image,
            'x': x,
            'y': y,
            'interpolation': interpolation,
            'extension_x': extension_x,
            'extension_y': extension_y,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'x': ('X', 'X', 1, 0.0),
            'y': ('Y', 'Y', 2, 0.0),
            'interpolation': ('Interpolation', 'Interpolation', 3, 'Bilinear'),
            'extension_x': ('Extension X', 'Extension X', 4, 'Clip'),
            'extension_y': ('Extension Y', 'Extension Y', 5, 'Clip'),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeTranslateOutputs,
    )

class FunctionNodeTransposeMatrixOutputs(typing.NamedTuple):
    'Outputs from Transpose Matrix: Flip a matrix over its diagonal, turning columns into rows and vice-versa'
    matrix: Socket[Matrix]

def transpose_matrix(*, matrix: Matrix | Socket[Matrix] | None = None) -> FunctionNodeTransposeMatrixOutputs:
    'Flip a matrix over its diagonal, turning columns into rows and vice-versa'
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

class FunctionNodeTrimStringOutputs(typing.NamedTuple):
    'Outputs from Trim String: Remove characters from the beginning and end of a string'
    string: Socket[str]

def trim_string(*, string: str | Socket[str] = '', characters: str | Socket[str] = '', whitespace: bool | Socket[bool] = True, start: bool | Socket[bool] = True, end: bool | Socket[bool] = True) -> FunctionNodeTrimStringOutputs:
    'Remove characters from the beginning and end of a string'
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

class FunctionNodeValueToStringOutputs(typing.NamedTuple):
    'Outputs from Value to String: Generate a string representation of the given input value'
    string: Socket[str]

def value_to_string(*, value: float | int | Socket[float | int] = 0.0, decimals: int | Socket[int] = 0, base: int | Socket[int] = 10, padding: int | Socket[int] = 0, data_type: typing.Literal['FLOAT', 'INT'] | None = None) -> FunctionNodeValueToStringOutputs:
    'Generate a string representation of the given input value\n\nArgs:\n    data_type:  Inferred from the linked inputs when None.'
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

class CompositorNodeVecBlurOutputs(typing.NamedTuple):
    'Outputs from Vector Blur: Uses the vector speed render pass to blur the image pixels in 2D'
    image: Socket[Color]

def vector_blur(*, image: Color | Socket[Color] = (1.0, 1.0, 1.0, 1.0), speed: Vector4 | Socket[Vector4] = (0.0, 0.0, 0.0, 0.0), depth: float | Socket[float] = 0.0, samples: int | Socket[int] = 32, shutter: float | Socket[float] = 0.5) -> CompositorNodeVecBlurOutputs:
    'Uses the vector speed render pass to blur the image pixels in 2D'
    return _node_function(
        'CompositorNodeVecBlur',
        inputs={
            'image': image,
            'speed': speed,
            'depth': depth,
            'samples': samples,
            'shutter': shutter,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (1.0, 1.0, 1.0, 1.0)),
            'speed': ('Speed', 'Speed', 1, (0.0, 0.0, 0.0, 0.0)),
            'depth': ('Z', 'Depth', 2, 0.0),
            'samples': ('Samples', 'Samples', 3, 32),
            'shutter': ('Shutter', 'Shutter', 4, 0.5),
        },
        properties={
        },
        output_sockets={
            'image': ('Image', 'Image', 0, 'AUTO'),
        },
        output_type=CompositorNodeVecBlurOutputs,
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

def viewer(*, image: Color | Socket[Color] = (0.0, 0.0, 0.0, 1.0)) -> None:
    'Visualize data from inside a node graph, in the image editor or as a backdrop'
    return _node_function(
        'CompositorNodeViewer',
        inputs={
            'image': image,
        },
        input_sockets={
            'image': ('Image', 'Image', 0, (0.0, 0.0, 0.0, 1.0)),
        },
        properties={
        },
        output_sockets={
        },
        output_type=None,
    )

class ShaderNodeTexVoronoiOutputs(typing.NamedTuple):
    'Outputs from Voronoi Texture: Generate Worley noise based on the distance to random points. Typically used to generate textures such as stones, water, or biological cells'
    distance: Socket[float]
    color: Socket[Color]
    position: Socket[Vector]
    w: Socket[float]
    radius: Socket[float]

def voronoi_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), scale: float | Socket[float] = 5.0, detail: float | Socket[float] = 0.0, roughness: float | Socket[float] = 0.5, lacunarity: float | Socket[float] = 2.0, randomness: float | Socket[float] = 1.0, w: float | Socket[float] = 0.0, smoothness: float | Socket[float] = 1.0, exponent: float | Socket[float] = 0.5, voronoi_dimensions: typing.Literal['1D', '2D', '3D', '4D'] = '2D', distance: typing.Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'] = 'EUCLIDEAN', feature: typing.Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'] = 'F1', normalize: bool = False) -> ShaderNodeTexVoronoiOutputs:
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

class GeometryNodeWarningOutputs(typing.NamedTuple):
    'Outputs from Warning: Create custom warnings in node groups'
    show: Socket[bool]

def warning(*, show: bool | Socket[bool] = True, message: str | Socket[str] = '', warning_type: typing.Literal['ERROR', 'WARNING', 'INFO'] = 'ERROR') -> GeometryNodeWarningOutputs:
    'Create custom warnings in node groups'
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

class ShaderNodeTexWhiteNoiseOutputs(typing.NamedTuple):
    'Outputs from White Noise Texture: Calculate a random value or color based on an input seed'
    value: Socket[float]
    color: Socket[Color]

def white_noise_texture(*, vector: Vector | Socket[Vector] = (0.0, 0.0, 0.0), w: float | Socket[float] = 0.0, noise_dimensions: typing.Literal['1D', '2D', '3D', '4D'] = '2D') -> ShaderNodeTexWhiteNoiseOutputs:
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
