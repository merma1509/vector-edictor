"""Shape manager for CRUD operations"""

from typing import Dict, List, Optional
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.shape import Shape
from models.point import Point
from models.line import Line
from models.circle import Circle
from models.square import Square


class ShapeManager:
    """Manages creation, deletion, and listing of shapes"""
    
    def __init__(self):
        self.shapes: Dict[int, Shape] = {}
        self.next_id: int = 1
    
    def create_point(self, x: float, y: float) -> Point:
        """Create a new point"""
        point = Point(self.next_id, x, y)
        self.shapes[self.next_id] = point
        self.next_id += 1
        return point
    
    def create_line(self, x1: float, y1: float, x2: float, y2: float) -> Line:
        """Create a new line segment"""
        line = Line(self.next_id, x1, y1, x2, y2)
        self.shapes[self.next_id] = line
        self.next_id += 1
        return line
    
    def create_circle(self, center_x: float, center_y: float, radius: float) -> Circle:
        """Create a new circle"""
        circle = Circle(self.next_id, center_x, center_y, radius)
        self.shapes[self.next_id] = circle
        self.next_id += 1
        return circle
    
    def create_square(self, x: float, y: float, side: float) -> Square:
        """Create a new square"""
        square = Square(self.next_id, x, y, side)
        self.shapes[self.next_id] = square
        self.next_id += 1
        return square
    
    def delete_shape(self, shape_id: int) -> bool:
        """Delete a shape by ID. Returns True if deleted, False if not found"""
        if shape_id in self.shapes:
            del self.shapes[shape_id]
            return True
        return False
    
    def get_shape(self, shape_id: int) -> Optional[Shape]:
        """Get a shape by ID"""
        return self.shapes.get(shape_id)
    
    def list_shapes(self) -> List[Shape]:
        """Get all shapes"""
        return list(self.shapes.values())
    
    def clear_all(self) -> None:
        """Clear all shapes"""
        self.shapes.clear()
        self.next_id = 1
