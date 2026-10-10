"""Choose Blender socket types for Python annotations and literal values."""

from __future__ import annotations

import inspect
import re
import types
import typing
from collections.abc import Callable, Mapping, Sequence
from typing import Any


SOCKET_TYPES = {
    "bool": "NodeSocketBool",
    "boolean": "NodeSocketBool",
    "int": "NodeSocketInt",
    "integer": "NodeSocketInt",
    "float": "NodeSocketFloat",
    "value": "NodeSocketFloat",
    "str": "NodeSocketString",
    "string": "NodeSocketString",
    "Color": "NodeSocketColor",
    "Vector": "NodeSocketVector",
    "Vector2": "NodeSocketVector2D",
    "Vector4": "NodeSocketVector4D",
    "IntVector2": "NodeSocketIntVector2D",
    "IntVector3": "NodeSocketIntVector3D",
    "Geometry": "NodeSocketGeometry",
    "Shader": "NodeSocketShader",
    "Object": "NodeSocketObject",
    "Image": "NodeSocketImage",
    "Collection": "NodeSocketCollection",
    "Material": "NodeSocketMaterial",
    "Texture": "NodeSocketTexture",
    "Rotation": "NodeSocketRotation",
    "Matrix": "NodeSocketMatrix",
    "Bundle": "NodeSocketBundle",
    "Closure": "NodeSocketClosure",
    "Menu": "NodeSocketMenu",
    "Font": "NodeSocketFont",
    "Scene": "NodeSocketScene",
    "Sound": "NodeSocketSound",
    "Text": "NodeSocketText",
    "Mask": "NodeSocketMask",
}
_STRUCTURE_TYPES = {"Field": "FIELD", "Grid": "GRID", "List": "LIST"}
_BUILTIN_TYPE_NAMES = {float: "float", int: "int", bool: "bool", str: "str"}


def _flatten_annotation(
    annotation: Any, namespace: Mapping[str, Any]
) -> tuple[list[str], set[str]]:
    """Return the socket type names and structures an annotation mentions."""
    names: list[str] = []
    structures: set[str] = set()

    def visit(value: Any) -> None:
        # Built-in types first: aliases such as ``Menu = str`` are the same object.
        builtin_name = _BUILTIN_TYPE_NAMES.get(value)
        if builtin_name is not None:
            names.append(builtin_name)
            return
        for alias_name, alias_value in namespace.items():
            if alias_name in SOCKET_TYPES and value is alias_value:
                names.append(alias_name)
                return

        if isinstance(value, str):
            for token in re.findall(r"[A-Za-z_][A-Za-z_0-9]*", value):
                if token in _STRUCTURE_TYPES:
                    structures.add(_STRUCTURE_TYPES[token])
                elif token in SOCKET_TYPES:
                    names.append(token)
                elif token == "Literal":
                    names.append("str")
            return

        origin = typing.get_origin(value)
        if origin in {typing.Union, types.UnionType}:
            for argument in typing.get_args(value):
                visit(argument)
            return

        name = getattr(origin or value, "__name__", "")
        if name in _STRUCTURE_TYPES:
            structures.add(_STRUCTURE_TYPES[name])
            for argument in typing.get_args(value):
                visit(argument)
        elif name in {"Socket", "Annotated"}:
            for argument in typing.get_args(value):
                visit(argument)
        elif name == "Literal":
            names.append("str")
        elif name in SOCKET_TYPES:
            names.append(name)

    visit(annotation)
    return names, structures


def _default_annotation(default: Any, parameter_name: str) -> Any:
    """Infer an annotation from a parameter's default value."""
    if default is inspect.Parameter.empty:
        raise TypeError(
            f"Tree input {parameter_name!r} needs a socket type annotation."
        )
    for builtin_type in (bool, int, float, str):
        if isinstance(default, builtin_type):
            return builtin_type
    if isinstance(default, Sequence):
        return f"Vector{len(default)}" if len(default) != 3 else "Vector"
    raise TypeError(
        f"Cannot infer a Blender socket type for tree input {parameter_name!r}."
    )


def interface_socket_spec(
    annotation: Any,
    *,
    namespace: Mapping[str, Any],
    default: Any,
    parameter_name: str,
) -> tuple[str, str]:
    """Return the socket type and structure type for an annotated parameter."""
    if annotation is inspect.Parameter.empty:
        annotation = _default_annotation(default, parameter_name)

    names, structures = _flatten_annotation(annotation, namespace)
    if not names and isinstance(annotation, str):
        annotation_name = annotation.rsplit(".", 1)[-1].strip()
        if annotation_name in SOCKET_TYPES:
            names.append(annotation_name)
    if not names:
        raise TypeError(
            f"Tree input {parameter_name!r} has unsupported socket annotation "
            f"{annotation!r}."
        )

    socket_type = SOCKET_TYPES[names[0]]
    if len(structures) > 1:
        structure_type = "DYNAMIC"
    else:
        structure_type = next(iter(structures), "AUTO")
    return socket_type, structure_type


def resolve_builder_annotations(builder: Callable[..., Any]) -> dict[str, Any]:
    try:
        return typing.get_type_hints(
            builder,
            globalns=getattr(builder, "__globals__", {}),
            include_extras=True,
        )
    except Exception:
        return dict(getattr(builder, "__annotations__", {}))


def literal_socket_type(value: Any) -> str:
    """The socket type that holds a Python literal."""
    if isinstance(value, bool):
        return "NodeSocketBool"
    if isinstance(value, int):
        return "NodeSocketInt"
    if isinstance(value, float):
        return "NodeSocketFloat"
    if isinstance(value, str):
        return "NodeSocketString"
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        socket_type = {
            2: "NodeSocketVector2D",
            3: "NodeSocketVector",
            4: "NodeSocketColor",
        }.get(len(value))
        if socket_type is not None:
            return socket_type
    raise TypeError(
        f"Tree outputs must be sockets or supported literals, got {type(value).__name__}."
    )
