"""Compositor nodes, and the decorator that builds compositor node groups.

    from geometry_script.compositor import *

    @compositor(scene=True)
    def soften():
        image = render_layers().image
        return blur(image=image, size=(4, 4))

The node functions here are the nodes compositor trees accept.
"""

from .api import compositor_nodes as _compositor_nodes
from .api import types as _types
from .api.aliases import MathNodeAndModule as _MathNodeAndModule
from .api.compositor_nodes import *
from .api.runtime import Socket
from .api.tree import compositor
from .api.types import *

math = _MathNodeAndModule(_compositor_nodes.math_)

__all__ = [
    "Socket",
    "compositor",
    "math",
]
__all__ += _types.__all__
__all__ += _compositor_nodes.__all__
