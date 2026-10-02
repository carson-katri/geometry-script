from typing import Generic, TypeVar

T = TypeVar("T")

class Field(Generic[T]):
    ...