"""Shader nodes, and the decorators that build shader trees.

    from geometry_script.shader import *

    @material
    def gold():
        return principled_bsdf(base_color=(1.0, 0.8, 0.3, 1.0), metallic=1.0)

``@shader`` builds a reusable shader node group, ``@material`` a material and
``@world`` a world. The node functions here are the nodes shader trees accept.
"""

from .api import shader_nodes as _shader_nodes
from .api import types as _types
from .api.aliases import MathNodeAndModule as _MathNodeAndModule
from .api.materials import material, world
from .api.runtime import Socket
from .api.shader_nodes import *
from .api.tree import shader
from .api.types import *
from .api.zones import closure_zone, repeat_zone

math = _MathNodeAndModule(_shader_nodes.math_)

__all__ = [
    "Socket",
    "closure_zone",
    "material",
    "math",
    "repeat_zone",
    "shader",
    "world",
]
__all__ += _types.__all__
__all__ += _shader_nodes.__all__
