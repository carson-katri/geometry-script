class Attribute:
    """
    A class that represents named attributes, providing methods for accessing and storing them.

    Create an attribute with a name, data type, and optional domain.
    ```python
    height_level = Attribute(
        "height_level",
        NamedAttribute.DataType.FLOAT,
        StoreNamedAttribute.Domain.POINT # optional
    )
    ```

    Access the attribute value by calling the class instance.
    ```python
    height_level()
    ```

    Store a value for the named attribute on some geometry with `store(...)`.
    ```python
    height_level.store(geometry, value)
    ```

    Check if the attribute exists on some geometry with `exists()`.
    ```python
    selection = height_level.exists()
    ```
    """
    name: str
    data_type: 'NamedAttribute.DataType'
    domain: 'StoreNamedAttribute.Domain'

    def __init__(
        self,
        name: str,
        data_type: 'NamedAttribute.DataType',
        domain: 'StoreNamedAttribute.Domain' = 'POINT'
    ):
        self.name = name
        self.data_type = data_type
        self.domain = domain

    def __call__(self, *args, **kwargs):
        """
        Creates a "Named Attribute" node with the correct arguments passed, and returns the "Attribute" socket.
        """
        from geometry_script import named_attribute
        return named_attribute(data_type=self.data_type, name=self.name, *args, **kwargs).attribute
    
    def exists(self, *args, **kwargs):
        """
        Creates a "Named Attribute" node with the correct arguments passed, and returns the "Exists" socket.
        """
        from geometry_script import named_attribute
        return named_attribute(data_type=self.data_type, name=self.name, *args, **kwargs).exists
    
    def store(self, geometry: 'Geometry', value, *args, **kwargs) -> 'Geometry':
        """
        Creates a "Store Named Attribute" node with the correct arguments passed, and returns the modified `Geometry`.
        """
        from geometry_script import store_named_attribute
        return store_named_attribute(
            data_type=self.data_type,
            domain=self.domain,
            geometry=geometry,
            name=self.name,
            value=value,
            *args,
            **kwargs
        )