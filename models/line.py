"""Line segment shape implementation"""

import math
from typing import Any, Dict, Tuple
from .shape import Shape


class Line(Shape):
    """Represents a line segment between two points"""
    
    def __init__(self, id: int, x1: float, y1: float, x2: float, y2: float):
        super().__init__(id)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def area(self) -> float:
        """Line has no area"""
        return 0.0
    
    def perimeter(self) -> float:
        """Length of the line segment"""
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
    
    def length(self) -> float:
        """Alias for perimeter - more intuitive for lines"""
        return self.perimeter()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert line to dictionary"""
        return {
            'type': 'line',
            'id': self.id,
            'x1': self.x1,
            'y1': self.y1,
            'x2': self.x2,
            'y2': self.y2
        }
    
    def __str__(self) -> str:
        """String representation of line"""
        return f"Line(({self.x1}, {self.y1}) to ({self.x2}, {self.y2}))"
