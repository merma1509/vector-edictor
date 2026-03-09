"""Unit tests for ShapeManager class"""

import unittest
import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from models.shape import Shape
from models.point import Point
from models.line import Line
from models.circle import Circle
from models.square import Square
from models.oval import Oval
from services.shape_manager import ShapeManager


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
        oval = self.manager.create_oval(0.0, 0.0, 8.0, 6.0)
        
        # Verify all shapes were created with correct IDs
        self.assertEqual(point.id, 1)
        self.assertEqual(circle.id, 2)
        self.assertEqual(line.id, 3)
        self.assertEqual(square.id, 4)
        self.assertEqual(oval.id, 5)
        
        # Verify shapes are stored correctly
        shapes = self.manager.list_shapes()
        self.assertEqual(len(shapes), 5)
        self.assertIsInstance(shapes[0], Point)
        self.assertIsInstance(shapes[1], Circle)
        self.assertIsInstance(shapes[2], Line)
        self.assertIsInstance(shapes[3], Square)
        self.assertIsInstance(shapes[4], Oval)
    
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
    
    def test_save_shapes_to_file(self):
        """Test saving shapes to a file"""
        # Create some shapes
        self.manager.create_point(10.0, 20.0)
        self.manager.create_circle(0.0, 0.0, 5.0)
        
        # Save shapes
        result = self.manager.save_shapes("test_save.json")
        self.assertIn("Successfully saved", result)
        self.assertIn("2 shapes", result)
        
        # Clean up
        import os
        if os.path.exists("test_save.json"):
            os.remove("test_save.json")
    
    def test_save_empty_shapes(self):
        """Test saving when no shapes exist"""
        result = self.manager.save_shapes("empty.json")
        self.assertEqual(result, "No shapes to save")
    
    def test_load_shapes_from_file(self):
        """Test loading shapes from a file"""
        # Create and save shapes first
        self.manager.create_point(10.0, 20.0)
        self.manager.create_circle(0.0, 0.0, 5.0)
        
        # Save to file
        self.manager.save_shapes("test_load.json")
        
        # Clear current shapes
        self.manager.clear_all()
        self.assertEqual(len(self.manager.list_shapes()), 0)
        
        # Load shapes from file
        success, message = self.manager.load_shapes("test_load.json")
        self.assertTrue(success)
        self.assertIn("Successfully loaded", message)
        
        # Verify shapes were loaded
        shapes = self.manager.list_shapes()
        self.assertEqual(len(shapes), 2)
        
        # Clean up
        import os
        if os.path.exists("test_load.json"):
            os.remove("test_load.json")
    
    def test_load_nonexistent_file(self):
        """Test loading from a non-existent file"""
        success, message = self.manager.load_shapes("nonexistent.json")
        self.assertFalse(success)
        self.assertIn("File not found", message)


if __name__ == "__main__":
    unittest.main()
