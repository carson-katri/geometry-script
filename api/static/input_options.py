import enum

class Subtype(enum.Enum):
    """
    If using subtype option, your geometry script must run in the active workspace containing the Geometry Node Editor 
    """

class SubtypeInt(Subtype):
    NONE = 'NONE'
    PERCENTAGE = 'PERCENTAGE'
    FACTOR = 'FACTOR'

class SubtypeFloat(Subtype):
    NONE = 'NONE'
    PERCENTAGE = 'PERCENTAGE'
    FACTOR = 'FACTOR'
    ANGLE = 'ANGLE'
    TIME = 'TIME'
    TIME_ABSOLUTE = 'TIME_ABSOLUTE'
    DISTANCE = 'DISTANCE'

class SubtypeVector(Subtype):
    NONE = 'NONE'
    TRANSLATION = 'TRANSLATION'
    VELOCITY = 'VELOCITY'
    ACCELERATION = 'ACCELERATION'
    EULER = 'EULER'
    XYZ = 'XYZ'


class _InputOptions:
    """Input options parent class."""
    def __init__(self, default, min, max, subtype, name, tooltip, hide_in_modifier):
        self.default_value = default 
        self.min_value = min   
        self.max_value = max
        self.bl_subtype_label = subtype.value if subtype != None else None
        self.name = name
        self.description = tooltip
        self.hide_in_modifier = hide_in_modifier


class IntOptions(_InputOptions):
    """
    Integer input options.
    
    Usage example:
    ```python
    my_int: Float = IntOptions(
        default=3,
        min=1,
        max=5,
        subtype=SubtypeInt.DISTANCE
    ),
    ```
    """
    MAX = 2147483647
    MIN = -MAX -1
    
    def __init__(
        self,
        default: int | None = None,
        min: int | None = None,
        max: int | None = None,
        subtype: SubtypeInt | None = None,
        name: str | None = None,
        tooltip: str = None,
        hide_in_modifier: bool = None,
    ):
        super().__init__(default, min, max, subtype, name, tooltip, hide_in_modifier)


class FloatOptions(_InputOptions):
    """
    Float input options.
    
    Usage example:
    ```python
    my_float: Float = FloatOptions(
        default=1.5,
        min=-0.5,
        max=2.5,
        subtype=SubtypeFloat.DISTANCE
    ),
    ```
    """
    MAX = float('inf')
    MIN = float('-inf')
    
    def __init__(
        self,
        default: float | None = None,
        min: float | None = None,
        max: float | None = None,
        subtype: SubtypeFloat | None = None,
        name: str | None = None,
        tooltip: str = None,
        hide_in_modifier: bool = None,
    ):
        super().__init__(default, min, max, subtype, name, tooltip, hide_in_modifier)


class VectorOptions(_InputOptions):
    """
    Vector input options.
    
    Usage example:
    ```python
    my_float: Vector = VectorOptions(
        default_x=0.5,
        default_y=1.0,
        default_z=1.5,
        min=-0.5,
        max=2.5,
        subtype=SubtypeVecotr.TRANSLATION
    ),
    ```
    """

    def __init__(
        self,
        default_x: float | None = None,
        default_y: float | None = None,
        default_z: float | None = None,
        min: float | None = None,
        max: float | None = None,
        subtype: SubtypeVector | None = None,
        name: str | None = None,
        tooltip: str = None,
        hide_in_modifier: bool = None,
    ):
        super().__init__((default_x, default_y, default_z), min, max, subtype, name, tooltip, hide_in_modifier)