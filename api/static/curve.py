from typing import List
import enum

class HandleType(enum.Enum):
    AUTO = 'AUTO'
    VECTOR = 'VECTOR'
    AUTO_CLAMPED = 'AUTO_CLAMPED'

class Point:
    """
    A single point on a curve
    """

    x: float
    y: float
    handle_type: HandleType

    def __init__(self, x: float, y: float, handle_type: HandleType = HandleType.AUTO):
        self.x = x
        self.y = y
        self.handle_type = handle_type

class Curve:
    """
    A class that represents a curve.

    Create a curve from a set of `Point`s.
    ```python
    my_curve = Curve(
        Point(0, 0, Handle.AUTO_CLAMPED),
        Point(0.2, 0.3, Handle.AUTO),
        Point(1, 1, Handle.VECTOR)
    )
    ```
    """

    points: List[Point]

    def __init__(self, *points: Point):
        if len(points) == 1 and isinstance(points[0], list):
            self.points = points[0]
        else:
            self.points = list(points)

    def apply(self, curve):
        """
        Apply the points to a curve object.
        """
        for i, point in enumerate(self.points):
            if len(curve.points) > i:
                curve.points[i].location = (point.x, point.y)
                curve.points[i].handle_type = point.handle_type.value
            else:
                curve.points.new(point.x, point.y).handle_type = point.handle_type.value