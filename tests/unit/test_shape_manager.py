"""Unit tests for ShapeManager class"""

import unittest
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from services.shape_manager import ShapeManager
from models.point import Point
from models.circle import Circle


class TestShapeManager(unittest.TestCase):
    """Test cases for ShapeManager functionality"""
    
    def setUp(self):
        """Set up test fixtures."""
        self.manager = ShapeManager()
    
    def test_initial_state(self):
        """Test initial state of ShapeManager."""
        self.assertEqual(len(self.manager.list_shapes()), 0)
        self.assertEqual(self.manager.next_id, 1)
        self.assertIsNone(self.manager.get_shape(1))
    
    def test_create_point(self):
        """Test point creation."""
        point = self.manager.create_point(10.0, 20.0)
        
        self.assertEqual(point.id, 1)
        self.assertEqual(point.x, 10.0)
        self.assertEqual(point.y, 20.0)
        self.assertEqual(self.manager.next_id, 2)
        
        # Verify it's stored correctly
        retrieved = self.manager.get_shape(1)
        self.assertIs(retrieved, point)
        self.assertEqual(len(self.manager.list_shapes()), 1)
    
    def test_create_circle(self):
        """Test circle creation."""
        circle = self.manager.create_circle(0.0, 0.0, 5.0)
        
        self.assertEqual(circle.id, 1)
        self.assertEqual(circle.center_x, 0.0)
        self.assertEqual(circle.center_y, 0.0)
        self.assertEqual(circle.radius, 5.0)
        self.assertEqual(self.manager.next_id, 2)
        
        # Verify it's stored correctly
        retrieved = self.manager.get_shape(1)
        self.assertIs(retrieved, circle)
        self.assertEqual(len(self.manager.list_shapes()), 1)
    
    def test_create_line(self):
        """Test line creation."""
        line = self.manager.create_line(0.0, 0.0, 3.0, 4.0)
        
        self.assertEqual(line.id, 1)
        self.assertEqual(line.x1, 0.0)
        self.assertEqual(line.y1, 0.0)
        self.assertEqual(line.x2, 3.0)
        self.assertEqual(line.y2, 4.0)
        self.assertEqual(self.manager.next_id, 2)
    
    def test_create_square(self):
        """Test square creation."""
        square = self.manager.create_square(2.0, 3.0, 4.0)
        
        self.assertEqual(square.id, 1)
        self.assertEqual(square.x, 2.0)
        self.assertEqual(square.y, 3.0)
        self.assertEqual(square.side, 4.0)
        self.assertEqual(self.manager.next_id, 2)
    
    def test_id_increment(self):
        """Test that IDs increment correctly."""
        point1 = self.manager.create_point(0.0, 0.0)
        point2 = self.manager.create_point(1.0, 1.0)
        
        self.assertEqual(point1.id, 1)
        self.assertEqual(point2.id, 2)
        self.assertEqual(self.manager.next_id, 3)
        
        # Verify both shapes are stored
        self.assertEqual(len(self.manager.list_shapes()), 2)
        self.assertIs(self.manager.get_shape(1), point1)
        self.assertIs(self.manager.get_shape(2), point2)
    
    def test_delete_existing_shape(self):
        """Test deleting an existing shape."""
        point = self.manager.create_point(10.0, 20.0)
        
        # Delete the shape
        result = self.manager.delete_shape(1)
        
        self.assertTrue(result)
        self.assertEqual(len(self.manager.list_shapes()), 0)
        self.assertIsNone(self.manager.get_shape(1))
    
    def test_delete_nonexistent_shape(self):
        """Test deleting a non-existent shape."""
        result = self.manager.delete_shape(999)
        
        self.assertFalse(result)
        self.assertEqual(len(self.manager.list_shapes()), 0)
    
    def test_clear_all(self):
        """Test clearing all shapes."""
        # Create multiple shapes
        self.manager.create_point(0.0, 0.0)
        self.manager.create_circle(1.0, 1.0, 2.0)
        self.manager.create_line(0.0, 0.0, 1.0, 1.0)
        
        self.assertEqual(len(self.manager.list_shapes()), 3)
        self.assertEqual(self.manager.next_id, 4)
        
        # Clear all shapes
        self.manager.clear_all()
        
        self.assertEqual(len(self.manager.list_shapes()), 0)
        self.assertEqual(self.manager.next_id, 1)
        self.assertIsNone(self.manager.get_shape(1))
    
    def test_list_shapes_order(self):
        """Test that list_shapes returns shapes in insertion order."""
        point1 = self.manager.create_point(0.0, 0.0)
        point2 = self.manager.create_point(1.0, 1.0)
        point3 = self.manager.create_point(2.0, 2.0)
        
        shapes = self.manager.list_shapes()
        
        self.assertEqual(len(shapes), 3)
        self.assertIs(shapes[0], point1)
        self.assertIs(shapes[1], point2)
        self.assertIs(shapes[2], point3)
    
    def test_mixed_shape_types(self):
        """Test creating and managing different shape types."""
        point = self.manager.create_point(0.0, 0.0)
        circle = self.manager.create_circle(1.0, 1.0, 2.0)
        line = self.manager.create_line(0.0, 0.0, 3.0, 4.0)
        square = self.manager.create_square(2.0, 2.0, 3.0)
        
        self.assertEqual(len(self.manager.list_shapes()), 4)
        
        # Verify each shape can be retrieved
        self.assertIsInstance(self.manager.get_shape(1), Point)
        self.assertIsInstance(self.manager.get_shape(2), Circle)
        self.assertIsInstance(self.manager.get_shape(3), type(line))
        self.assertIsInstance(self.manager.get_shape(4), type(square))
        
        # Delete middle shape
        self.assertTrue(self.manager.delete_shape(2))
        self.assertEqual(len(self.manager.list_shapes()), 3)
        self.assertIsNone(self.manager.get_shape(2))
        
        # Verify other shapes still exist
        self.assertIsNotNone(self.manager.get_shape(1))
        self.assertIsNotNone(self.manager.get_shape(3))
        self.assertIsNotNone(self.manager.get_shape(4))


if __name__ == "__main__":
    unittest.main()
