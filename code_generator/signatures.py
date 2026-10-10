"""Node signatures read from Blender, and the naming rules shared by the generator."""

from __future__ import annotations

import keyword
import re
import typing
from dataclasses import dataclass, field


NO_DEFAULT = object()


@dataclass(frozen=True, slots=True)
class NodeMetatype:
    """A socket as it appears in a generated function signature."""

    name: str
    type: str
    default_value: object = NO_DEFAULT
    description: str = ""
    display_shape: str = ""
    structure_type: str = ""
    enum_values: tuple[str, ...] = ()
    is_menu: bool = False
    supports_field: bool = False
    supports_geometry_structures: bool = False
    is_multi_input: bool = False
    socket_identifier: str = ""
    socket_index: int = -1
    # Blender's socket type enum (VALUE, VECTOR, GEOMETRY, ...).
    kind: str = ""
    # Set when the socket only exists for some property values.
    is_conditional: bool = False


@dataclass(frozen=True, slots=True)
class NodeProperty:
    """A settable node property exposed as a function parameter."""

    identifier: str
    type: str
    default_value: object = NO_DEFAULT
    description: str = ""


@dataclass(frozen=True, slots=True)
class ItemCollection:
    """A node's user-defined item list, such as Capture Attribute's items."""

    identifier: str
    # How the DSL passes items, chosen by what adding an item creates:
    #   values:   input sockets with a chosen type -> keyword arguments
    #   named:    input sockets typed by the node  -> {name: value}
    #   sequence: unnamed input sockets            -> [value, ...]
    #   types:    output sockets only              -> {name: type}
    mode: str
    creates_outputs: bool


@dataclass(frozen=True, slots=True)
class NodeSignature:
    name: str
    function_name: str
    node_type_id: str
    output_type_name: str
    description: str
    inputs: tuple[NodeMetatype, ...]
    outputs: tuple[NodeMetatype, ...]
    properties: tuple[NodeProperty, ...] = ()
    # Enum properties that change socket types, mapped to the socket kind each
    # property value gives the inputs it affects: {property: {value: {input index: kind}}}.
    type_properties: dict[str, dict[str, dict[int, str]]] = field(default_factory=dict)
    item_collections: tuple[ItemCollection, ...] = ()

    @property
    def has_item_outputs(self) -> bool:
        return any(collection.creates_outputs for collection in self.item_collections)


def snake_case(value: str, *, fallback: str = "socket") -> str:
    """Convert a UI label or RNA name into a valid, readable Python identifier."""
    value = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = re.sub(r"[^0-9a-zA-Z_]+", "_", value).strip("_").lower()
    value = re.sub(r"_+", "_", value)
    if not value:
        value = fallback
    if value[0].isdigit():
        value = f"{fallback}_{value}"
    if keyword.iskeyword(value):
        value += "_"
    return value


def unique_name(name: str, used: set[str]) -> str:
    """Return ``name``, numbered from 2 if it is taken, and mark it used."""
    candidate = name
    suffix = 2
    while candidate in used:
        candidate = f"{name}_{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def unique_names(names: typing.Iterable[str]) -> list[str]:
    used: set[str] = set()
    return [unique_name(name, used) for name in names]
