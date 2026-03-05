"""Circle shape implementation"""

import math
from typing import Any, Dict
from .shape import Shape


class Circle(Shape):
    """Represents a circle with center and radius"""
    
    def __init__(self, id: int, center_x: float, center_y: float, radius: float):
        super().__init__(id)
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
    
    def area(self) -> float:
        """Calculate area of the circle"""
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate circumference of the circle"""
        return 2 * math.pi * self.radius
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert circle to dictionary"""
        return {
            'type': 'circle',
            'id': self.id,
            'center_x': self.center_x,
            'center_y': self.center_y,
            'radius': self.radius
        }
    
    def __str__(self) -> str:
        """String representation of circle"""
        return f"Circle(center=({self.center_x}, {self.center_y}), radius={self.radius})"
