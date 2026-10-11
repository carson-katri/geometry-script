"""Marker types used in node function signatures and @tree annotations.

These names describe socket data types. They carry no runtime behavior; at
build time every value is either a Python literal or a ``Socket``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated, Generic, TypeAlias, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class SocketMarker:
    """Names the socket type of an ``Annotated`` alias.

    Aliases such as ``Vector`` and ``Color`` read as plain tuples to type
    checkers, but ``tuple[float, float, float, float]`` alone cannot tell a
    Color from a Vector4, and ``typing.get_type_hints`` rebuilds bare generic
    aliases, so the socket type travels in the ``Annotated`` metadata instead.
    """

    name: str


Vector: TypeAlias = Annotated[tuple[float, float, float], SocketMarker("Vector")]
Vector2: TypeAlias = Annotated[tuple[float, float], SocketMarker("Vector2")]
Vector4: TypeAlias = Annotated[tuple[float, float, float, float], SocketMarker("Vector4")]
Color: TypeAlias = Annotated[tuple[float, float, float, float], SocketMarker("Color")]
IntVector2: TypeAlias = Annotated[tuple[int, int], SocketMarker("IntVector2")]
IntVector3: TypeAlias = Annotated[tuple[int, int, int], SocketMarker("IntVector3")]

# NodeSocketMenu.default_value is a string enum identifier.
Menu: TypeAlias = Annotated[str, SocketMarker("Menu")]


class Field(Generic[T]):
    """A value evaluated per element of the geometry it is used on."""


class Grid(Generic[T]):
    """A volume grid of values."""


class List(Generic[T]):
    """A list of values."""


class Geometry: ...
class Rotation: ...
class Matrix: ...
class Bundle: ...
class Closure: ...
class Object: ...
class Collection: ...
class Image: ...
class Material: ...
class Texture: ...
class Shader: ...
class Font: ...
class Scene: ...
class Sound: ...
class Text: ...
class Mask: ...


__all__ = [
    "Bundle",
    "Closure",
    "Collection",
    "Color",
    "Field",
    "Font",
    "Geometry",
    "Grid",
    "Image",
    "IntVector2",
    "IntVector3",
    "List",
    "Mask",
    "Material",
    "Matrix",
    "Menu",
    "Object",
    "Rotation",
    "Scene",
    "Shader",
    "Sound",
    "Text",
    "Texture",
    "Vector",
    "Vector2",
    "Vector4",
]
