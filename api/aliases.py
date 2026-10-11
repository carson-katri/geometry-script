"""Names the generated functions avoid, for scripts that guess them anyway."""

from __future__ import annotations

import math as _math_module
from collections.abc import Callable
from typing import Any

from .nodes import math_


class MathNodeAndModule:
    """``math(...)`` adds a Math node; ``math.pi`` and friends are Python's math module.

    The generated function is ``math_`` so a star import cannot hide the
    module. This alias keeps both working whichever was imported last.
    """

    __slots__ = ("_node_function",)

    def __init__(self, node_function: Callable[..., Any]) -> None:
        self._node_function = node_function

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self._node_function(*args, **kwargs)

    def __getattr__(self, name: str) -> Any:
        return getattr(_math_module, name)

    def __dir__(self) -> list[str]:
        return dir(_math_module)

    def __repr__(self) -> str:
        return "<math: Math node function and Python math module>"


math = MathNodeAndModule(math_)

__all__ = ["math"]
