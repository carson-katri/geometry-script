import enum

class SubtypeInt(enum.Enum):
    NONE = 'None'
    PERCENTAGE = 'Percentage'
    FACTOR = 'Factor'

class SubtypeFloat(enum.Enum):
    NONE = 'None'
    PERCENTAGE = 'Percentage'
    FACTOR = 'Factor'
    ANGLE = 'Angle'
    TIME = 'Time (Scene Relative)'
    TIME_ABSOLUTE = 'Time (Absolute)'
    DISTANCE = 'Distance'

class InputOptions:
    """Input options parent class"""

class IntOptions(InputOptions):
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
        self.default_value = default 
        self.min_value = min   
        self.max_value = max
        self.bl_subtype_label = subtype.value if subtype != None else None
        self.name = name
        self.description = tooltip
        self.hide_in_modifier = hide_in_modifier

class FloatOptions(InputOptions):
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
        self.default_value = default 
        self.min_value = min   
        self.max_value = max
        self.bl_subtype_label = subtype.value if subtype != None else None
        self.name = name
        self.description = tooltip
        self.hide_in_modifier = hide_in_modifier