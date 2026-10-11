"""Turn node, socket and item names into Python names and back."""

from __future__ import annotations

import re
from collections.abc import Iterable


_NON_IDENTIFIER = re.compile(r"[^0-9a-zA-Z_]+")


def humanize(name: str) -> str:
    """A UI socket name for a Python parameter name."""
    return name.replace("_", " ").strip().title() or "Input"


def identifier(name: str) -> str:
    """Replace the characters a Python identifier cannot hold; may return ""."""
    return _NON_IDENTIFIER.sub("_", name).strip("_")


def unique_name(name: str, used: set[str]) -> str:
    """Return ``name``, numbered from 2 if it is taken, and mark it used."""
    candidate = name
    suffix = 2
    while candidate in used:
        candidate = f"{name}_{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def attribute_names(names: Iterable[str]) -> list[str]:
    """Unique attribute names for socket names, e.g. on a namedtuple of outputs."""
    used: set[str] = set()
    result: list[str] = []
    for index, name in enumerate(names):
        attribute = identifier(name) or f"output_{index + 1}"
        if attribute[0].isdigit():
            attribute = f"output_{attribute}"
        result.append(unique_name(attribute, used))
    return result


def class_name(name: str, fallback: str) -> str:
    """A CamelCase class name for a function name such as ``grow_tree``."""
    result = _NON_IDENTIFIER.sub("", name.title().replace("_", "")) or fallback
    if result[0].isdigit():
        result = f"{fallback}{result}"
    return result
