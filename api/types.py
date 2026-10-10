"""Marker types used in node function signatures and @tree annotations.

These names describe socket data types. They carry no runtime behavior; at
build time every value is either a Python literal or a ``Socket``.
"""

from __future__ import annotations

from typing import Generic, TypeAlias, TypeVar

T = TypeVar("T")

Vector: TypeAlias = tuple[float, float, float]
Vector2: TypeAlias = tuple[float, float]
Vector4: TypeAlias = tuple[float, float, float, float]
Color: TypeAlias = tuple[float, float, float, float]
IntVector2: TypeAlias = tuple[int, int]
IntVector3: TypeAlias = tuple[int, int, int]

# NodeSocketMenu.default_value is a string enum identifier.
Menu: TypeAlias = str


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
