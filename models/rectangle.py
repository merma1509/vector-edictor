"""Rectangle shape implementation"""

from .shape import Shape


class Rectangle(Shape):
    """Represents a rectangle shape"""

    def __init__(
        self, shape_id: int, x: float, y: float, width: float, height: float
    ):
        """Initialize rectangle with top-left corner and dimensions"""
        self.id = shape_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate rectangle area: width * height"""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate rectangle perimeter: 2 * (width + height)"""
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """String representation of rectangle"""
        return f"Rectangle(top-left=({self.x}, {self.y}), width={self.width}, height={self.height})"

    def to_dict(self) -> dict:
        """Convert rectangle to dictionary for serialization"""
        return {
            "type": "rectangle",
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
        }
