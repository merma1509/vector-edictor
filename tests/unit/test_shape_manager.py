"""Essential unit tests for ShapeManager class"""

import unittest
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from services.shape_manager import ShapeManager
from models.point import Point
from models.circle import Circle
from models.line import Line
from models.square import Square


class TestShapeManagerEssential(unittest.TestCase):
    """Essential test cases for ShapeManager functionality"""
    
    def setUp(self):
        """Set up test fixtures."""
        self.manager = ShapeManager()
    
    def test_create_all_shape_types(self):
        """Test creating all different shape types"""
        point = self.manager.create_point(10.0, 20.0)
        circle = self.manager.create_circle(0.0, 0.0, 5.0)
        line = self.manager.create_line(0.0, 0.0, 3.0, 4.0)
        square = self.manager.create_square(2.0, 3.0, 4.0)
        
        # Verify all shapes were created with correct IDs
        self.assertEqual(point.id, 1)
        self.assertEqual(circle.id, 2)
        self.assertEqual(line.id, 3)
        self.assertEqual(square.id, 4)
        
        # Verify shapes are stored correctly
        shapes = self.manager.list_shapes()
        self.assertEqual(len(shapes), 4)
        self.assertIsInstance(shapes[0], Point)
        self.assertIsInstance(shapes[1], Circle)
        self.assertIsInstance(shapes[2], Line)
        self.assertIsInstance(shapes[3], Square)
    
    def test_delete_existing_and_nonexisting_shapes(self):
        """Test delete functionality for existing and non-existing shapes"""
        # Create some shapes
        self.manager.create_point(10.0, 20.0)
        self.manager.create_circle(0.0, 0.0, 5.0)
        
        # Delete existing shape
        self.assertTrue(self.manager.delete_shape(1))
        self.assertIsNone(self.manager.get_shape(1))
        
        # Try to delete non-existent shape
        self.assertFalse(self.manager.delete_shape(999))
        
        # Verify remaining shape
        shapes = self.manager.list_shapes()
        self.assertEqual(len(shapes), 1)
        self.assertEqual(shapes[0].id, 2)
    
    def test_list_shapes_and_clear_all(self):
        """Test list functionality and clear all operation"""
        # Initially empty
        self.assertEqual(len(self.manager.list_shapes()), 0)
        
        # Add shapes and verify listing
        self.manager.create_point(1.0, 2.0)
        self.manager.create_circle(3.0, 4.0, 5.0)
        
        shapes = self.manager.list_shapes()
        self.assertEqual(len(shapes), 2)
        
        # Clear all and verify empty
        self.manager.clear_all()  # clear_all returns None
        self.assertEqual(len(self.manager.list_shapes()), 0)


if __name__ == "__main__":
    unittest.main()
