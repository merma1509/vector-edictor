"""Unit tests for shape classes"""

import sys
import unittest
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from models.circle import Circle
from models.line import Line
from models.oval import Oval
from models.point import Point
from models.rectangle import Rectangle
from models.square import Square


class TestShapesEssential(unittest.TestCase):
    """Essential test cases for individual shape classes"""

    def test_point_creation_and_basic_properties(self):
        """Test point creation and basic properties"""
        point = Point(1, 10.0, 20.0)

        self.assertEqual(point.id, 1)
        self.assertEqual(point.x, 10.0)
        self.assertEqual(point.y, 20.0)
        self.assertEqual(point.area(), 0.0)
        self.assertEqual(point.perimeter(), 0.0)
        self.assertEqual(str(point), "Point(10.0, 20.0)")
        self.assertEqual(
            point.to_dict(), {"type": "point", "id": 1, "x": 10.0, "y": 20.0}
        )

    def test_line_creation_and_basic_properties(self):
        """Test line creation and basic properties"""
        line = Line(1, 0.0, 0.0, 3.0, 4.0)

        self.assertEqual(line.id, 1)
        self.assertEqual(line.x1, 0.0)
        self.assertEqual(line.y1, 0.0)
        self.assertEqual(line.x2, 3.0)
        self.assertEqual(line.y2, 4.0)
        self.assertAlmostEqual(line.area(), 0.0)
        self.assertAlmostEqual(
            line.perimeter(), 5.0
        )  # Distance from (0,0) to (3,4) is 5
        self.assertEqual(str(line), "Line((0.0, 0.0) to (3.0, 4.0))")

    def test_circle_creation_and_basic_properties(self):
        """Test circle creation and basic properties"""
        circle = Circle(1, 0.0, 0.0, 5.0)

        self.assertEqual(circle.id, 1)
        self.assertEqual(circle.center_x, 0.0)
        self.assertEqual(circle.center_y, 0.0)
        self.assertEqual(circle.radius, 5.0)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)
        self.assertAlmostEqual(circle.perimeter(), 31.41592653589793)
        self.assertEqual(str(circle), "Circle(center=(0.0, 0.0), radius=5.0)")

    def test_square_creation_and_basic_properties(self):
        """Test square creation and basic properties"""
        square = Square(1, 2.0, 3.0, 4.0)

        self.assertEqual(square.id, 1)
        self.assertEqual(square.x, 2.0)
        self.assertEqual(square.y, 3.0)
        self.assertEqual(square.side, 4.0)
        self.assertAlmostEqual(square.area(), 16.0)
        self.assertAlmostEqual(square.perimeter(), 16.0)
        self.assertEqual(str(square), "Square(top-left=(2.0, 3.0), side=4.0)")

    def test_oval_creation_and_basic_properties(self):
        """Test oval creation and basic properties"""
        oval = Oval(1, 0.0, 0.0, 8.0, 6.0)

        self.assertEqual(oval.id, 1)
        self.assertEqual(oval.center_x, 0.0)
        self.assertEqual(oval.center_y, 0.0)
        self.assertEqual(oval.width, 8.0)
        self.assertEqual(oval.height, 6.0)
        self.assertAlmostEqual(oval.area(), 37.69911184307752)  # pi * 4 * 3
        self.assertAlmostEqual(oval.perimeter(), 31.41592653589793)  # Approximation
        self.assertEqual(str(oval), "Oval(center=(0.0, 0.0), width=8.0, height=6.0)")
        self.assertEqual(
            oval.to_dict(),
            {
                "type": "oval",
                "id": 1,
                "center_x": 0.0,
                "center_y": 0.0,
                "width": 8.0,
                "height": 6.0,
            },
        )

    def test_rectangle_creation_and_basic_properties(self):
        """Test rectangle creation and basic properties"""
        rectangle = Rectangle(1, 2.0, 3.0, 10.0, 6.0)

        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.x, 2.0)
        self.assertEqual(rectangle.y, 3.0)
        self.assertEqual(rectangle.width, 10.0)
        self.assertEqual(rectangle.height, 6.0)
        self.assertEqual(rectangle.area(), 60.0)  # 10 * 6
        self.assertEqual(rectangle.perimeter(), 32.0)  # 2 * (10 + 6)
        self.assertEqual(
            str(rectangle), "Rectangle(top-left=(2.0, 3.0), width=10.0, height=6.0)"
        )
        self.assertEqual(
            rectangle.to_dict(),
            {
                "type": "rectangle",
                "id": 1,
                "x": 2.0,
                "y": 3.0,
                "width": 10.0,
                "height": 6.0,
            },
        )


if __name__ == "__main__":
    unittest.main()
