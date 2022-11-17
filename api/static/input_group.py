class InputGroup:
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