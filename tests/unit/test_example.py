"""Example test file to demonstrate testing capabilities"""

import unittest
from models.point import Point
from models.circle import Circle
from services.shape_manager import ShapeManager
from cli.commands import CommandProcessor


class TestVectorEditor(unittest.TestCase):
    """Test cases for the vector editor."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.manager = ShapeManager()
        self.processor = CommandProcessor()
    
    def test_point_creation(self):
        """Test point creation and properties."""
        point = Point(1, 10.0, 20.0)
        self.assertEqual(point.x, 10.0)
        self.assertEqual(point.y, 20.0)
        self.assertEqual(point.area(), 0.0)
        self.assertEqual(point.perimeter(), 0.0)
        self.assertEqual(str(point), "Point(10.0, 20.0)")
    
    def test_circle_creation(self):
        """Test circle creation and properties."""
        circle = Circle(1, 0.0, 0.0, 5.0)
        self.assertEqual(circle.center_x, 0.0)
        self.assertEqual(circle.center_y, 0.0)
        self.assertEqual(circle.radius, 5.0)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)
        self.assertAlmostEqual(circle.perimeter(), 31.41592653589793)
    
    def test_shape_manager_create_point(self):
        """Test ShapeManager point creation."""
        point = self.manager.create_point(10.0, 20.0)
        self.assertEqual(point.id, 1)
        self.assertEqual(point.x, 10.0)
        self.assertEqual(point.y, 20.0)
    
    def test_shape_manager_delete(self):
        """Test ShapeManager delete functionality."""
        point = self.manager.create_point(10.0, 20.0)
        self.assertTrue(self.manager.delete_shape(1))
        self.assertFalse(self.manager.delete_shape(999))
        self.assertIsNone(self.manager.get_shape(1))
    
    def test_command_processor_create_point(self):
        """Test CommandProcessor point creation."""
        result = self.processor.process_command("create point 10 20")
        self.assertEqual(result, "Point created with ID: 1")
        
        # Verify the shape was created
        shapes = self.processor.shape_manager.list_shapes()
        self.assertEqual(len(shapes), 1)
        self.assertEqual(shapes[0].x, 10.0)
        self.assertEqual(shapes[0].y, 20.0)
    
    def test_command_processor_error_handling(self):
        """Test CommandProcessor error handling."""
        result = self.processor.process_command("create point")
        self.assertIn("Error:", result)
        
        result = self.processor.process_command("create circle 0 0 -5")
        self.assertIn("Error:", result)
        
        result = self.processor.process_command("delete 999")
        self.assertIn("Error:", result)


if __name__ == "__main__":
    unittest.main()
