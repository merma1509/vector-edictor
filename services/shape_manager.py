"""Shape manager for CRUD operations"""

import os
import sys
from typing import Dict, List, Optional, Tuple

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.circle import Circle
from models.line import Line
from models.oval import Oval
from models.point import Point
from models.rectangle import Rectangle
from models.shape import Shape
from models.square import Square

from .file_manager import FileManager


class ShapeManager:
    """Manages creation, deletion, and listing of shapes"""

    def __init__(self):
        """Initialize the shape manager"""
        self.shapes: Dict[int, Shape] = {}
        self.next_id: int = 1
        self.file_manager = FileManager()

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

    def create_oval(
        self, center_x: float, center_y: float, width: float, height: float
    ) -> Oval:
        """Create a new oval"""
        oval = Oval(self.next_id, center_x, center_y, width, height)
        self.shapes[self.next_id] = oval
        self.next_id += 1
        return oval

    def create_rectangle(
        self, x: float, y: float, width: float, height: float
    ) -> Rectangle:
        """Create a new rectangle"""
        rectangle = Rectangle(self.next_id, x, y, width, height)
        self.shapes[self.next_id] = rectangle
        self.next_id += 1
        return rectangle

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

    def save_shapes(self, filename: str) -> str:
        """Save all current shapes to a file

        Args:
            filename (string): Name of the file to save to

        Returns:
            Success or error message
        """
        if not self.shapes:
            return "No shapes to save"

        return self.file_manager.save_shapes(self.list_shapes(), filename)

    def load_shapes(self, filename: str) -> Tuple[bool, str]:
        """Load shapes from a file

        Args:
            filename (string): Name of the file to load from

        Returns:
            Tuple of (success: bool, message: str)
        """
        success, message, shapes_data = self.file_manager.load_shapes(filename)

        if not success:
            return False, message

        if not shapes_data:
            return True, "No shapes found in file"

        # Clear current shapes before loading
        self.clear_all()

        # Load shapes from data
        loaded_count = 0
        for shape_data in shapes_data:
            try:
                shape = self._create_shape_from_dict(shape_data)
                if shape:
                    self.shapes[shape.id] = shape
                    loaded_count += 1
                    # Update next_id to be higher than any loaded shape
                    if shape.id >= self.next_id:
                        self.next_id = shape.id + 1
            except Exception as e:
                # Skip invalid shapes but continue loading others
                continue

        return True, f"Successfully loaded {loaded_count} shapes"

    def _create_shape_from_dict(self, shape_data: Dict) -> Optional[Shape]:
        """Create a shape object from dictionary data

        Args:
            shape_data (dict): Dictionary containing shape information

        Returns:
            Shape object or None if creation failed
        """
        shape_type = shape_data.get("type", "").lower()
        shape_id = shape_data.get("id", 0)

        if shape_type == "point":
            return Point(shape_id, shape_data["x"], shape_data["y"])
        elif shape_type == "line":
            return Line(
                shape_id,
                shape_data["x1"],
                shape_data["y1"],
                shape_data["x2"],
                shape_data["y2"],
            )
        elif shape_type == "circle":
            return Circle(
                shape_id,
                shape_data["center_x"],
                shape_data["center_y"],
                shape_data["radius"],
            )
        elif shape_type == "square":
            return Square(
                shape_id, shape_data["x"], shape_data["y"], shape_data["side"]
            )
        elif shape_type == "oval":
            return Oval(
                shape_id,
                shape_data["center_x"],
                shape_data["center_y"],
                shape_data["width"],
                shape_data["height"],
            )
        elif shape_type == "rectangle":
            return Rectangle(
                shape_id,
                shape_data["x"],
                shape_data["y"],
                shape_data["width"],
                shape_data["height"],
            )

        return None
