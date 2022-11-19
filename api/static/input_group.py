class _InputGroupMeta(type):
    def __getitem__(cls, args):
        if isinstance(args, str):
            class PrefixedInputGroup(InputGroup):
                prefix = args
            PrefixedInputGroup.__annotations__ = cls.__annotations__
            return PrefixedInputGroup
        return cls

class InputGroup(metaclass=_InputGroupMeta):
    """
    A group of inputs that will be expanded in the node tree.
    
    All properties must be annotated:
    ```python
    class MyInputGroup(InputGroup):
        my_float: Float
        my_bool: Bool
        my_string # Invalid
    ```
    """
    
    def __init__(self, **kwargs):
        for p in dir(self):
            if p in kwargs:
                setattr(self, p, kwargs[p])