"""Point shape implementation"""

from typing import Any, Dict
from .shape import Shape


class Point(Shape):
    """Represents a point in 2D space"""
    
    def __init__(self, id: int, x: float, y: float):
        super().__init__(id)
        self.x = x
        self.y = y
    
    def area(self) -> float:
        """Point has no area"""
        return 0.0
    
    def perimeter(self) -> float:
        """Point has no perimeter"""
        return 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert point to dictionary"""
        return {
            'type': 'point',
            'id': self.id,
            'x': self.x,
            'y': self.y
        }
    
    def __str__(self) -> str:
        """String representation of point"""
        return f"Point({self.x}, {self.y})"
