"""Square shape implementation"""

from typing import Any, Dict

from .shape import Shape


class Square(Shape):
    """Represents a square with top-left corner and side length"""

    def __init__(self, id: int, x: float, y: float, side: float):
        super().__init__(id)
        self.x = x  # Top-left corner x
        self.y = y  # Top-left corner y
        self.side = side

    def area(self) -> float:
        """Calculate area of the square"""
        return self.side**2

    def perimeter(self) -> float:
        """Calculate perimeter of the square"""
        return 4 * self.side

    def to_dict(self) -> Dict[str, Any]:
        """Convert square to dictionary"""
        return {
            "type": "square",
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "side": self.side,
        }

    def __str__(self) -> str:
        """String representation of square"""
        return f"Square(top-left=({self.x}, {self.y}), side={self.side})"
