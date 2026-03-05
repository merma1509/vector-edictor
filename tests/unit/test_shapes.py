"""Unit tests for shape classes"""

import unittest
import math
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from models.point import Point
from models.line import Line
from models.circle import Circle
from models.square import Square


class TestShapes(unittest.TestCase):
    """Test cases for individual shape classes"""
    
    def test_point_creation_and_properties(self):
        """Test point creation and basic properties"""
        point = Point(1, 10.0, 20.0)
        
        self.assertEqual(point.id, 1)
        self.assertEqual(point.x, 10.0)
        self.assertEqual(point.y, 20.0)
        self.assertEqual(point.area(), 0.0)
        self.assertEqual(point.perimeter(), 0.0)
        
        # Test string representation
        self.assertEqual(str(point), "Point(10.0, 20.0)")
        
        # Test dictionary conversion
        expected_dict = {
            'type': 'point',
            'id': 1,
            'x': 10.0,
            'y': 20.0
        }
        self.assertEqual(point.to_dict(), expected_dict)
    
    def test_line_creation_and_properties(self):
        """Test line creation and basic properties"""
        line = Line(1, 0.0, 0.0, 3.0, 4.0)
        
        self.assertEqual(line.id, 1)
        self.assertEqual(line.x1, 0.0)
        self.assertEqual(line.y1, 0.0)
        self.assertEqual(line.x2, 3.0)
        self.assertEqual(line.y2, 4.0)
        
        # Test length calculation (3-4-5 triangle)
        self.assertEqual(line.area(), 0.0)
        self.assertEqual(line.perimeter(), 5.0)
        self.assertEqual(line.length(), 5.0)
        
        # Test string representation
        self.assertEqual(str(line), "Line((0.0, 0.0) to (3.0, 4.0))")
        
        # Test dictionary conversion
        expected_dict = {
            'type': 'line',
            'id': 1,
            'x1': 0.0,
            'y1': 0.0,
            'x2': 3.0,
            'y2': 4.0
        }
        self.assertEqual(line.to_dict(), expected_dict)
    
    def test_circle_creation_and_properties(self):
        """Test circle creation and basic properties."""
        circle = Circle(1, 0.0, 0.0, 5.0)
        
        self.assertEqual(circle.id, 1)
        self.assertEqual(circle.center_x, 0.0)
        self.assertEqual(circle.center_y, 0.0)
        self.assertEqual(circle.radius, 5.0)
        
        # Test area and circumference
        expected_area = math.pi * 5.0 ** 2
        expected_perimeter = 2 * math.pi * 5.0
        
        self.assertAlmostEqual(circle.area(), expected_area, places=5)
        self.assertAlmostEqual(circle.perimeter(), expected_perimeter, places=5)
        
        # Test string representation
        self.assertEqual(str(circle), "Circle(center=(0.0, 0.0), radius=5.0)")
        
        # Test dictionary conversion
        expected_dict = {
            'type': 'circle',
            'id': 1,
            'center_x': 0.0,
            'center_y': 0.0,
            'radius': 5.0
        }
        self.assertEqual(circle.to_dict(), expected_dict)
    
    def test_square_creation_and_properties(self):
        """Test square creation and basic properties"""
        square = Square(1, 2.0, 3.0, 4.0)
        
        self.assertEqual(square.id, 1)
        self.assertEqual(square.x, 2.0)
        self.assertEqual(square.y, 3.0)
        self.assertEqual(square.side, 4.0)
        
        # Test area and perimeter
        self.assertEqual(square.area(), 16.0)
        self.assertEqual(square.perimeter(), 16.0)
        
        # Test string representation
        self.assertEqual(str(square), "Square(top-left=(2.0, 3.0), side=4.0)")
        
        # Test dictionary conversion
        expected_dict = {
            'type': 'square',
            'id': 1,
            'x': 2.0,
            'y': 3.0,
            'side': 4.0
        }
        self.assertEqual(square.to_dict(), expected_dict)
    
    def test_shape_edge_cases(self):
        """Test edge cases for shape calculations"""
        # Point with negative coordinates
        point = Point(1, -10.5, -20.5)
        self.assertEqual(point.x, -10.5)
        self.assertEqual(point.y, -20.5)
        
        # Line with same start and end point (zero length)
        line = Line(1, 0.0, 0.0, 0.0, 0.0)
        self.assertEqual(line.length(), 0.0)
        
        # Circle with small radius
        circle = Circle(1, 0.0, 0.0, 0.1)
        self.assertGreater(circle.area(), 0.0)
        self.assertGreater(circle.perimeter(), 0.0)
        
        # Square with small side
        square = Square(1, 0.0, 0.0, 0.1)
        self.assertAlmostEqual(square.area(), 0.01, places=5)
        self.assertAlmostEqual(square.perimeter(), 0.4, places=5)


if __name__ == "__main__":
    unittest.main()
