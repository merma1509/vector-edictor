"""Unit tests for CommandProcessor class."""

import unittest
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from cli.commands import CommandProcessor


class TestCommandProcessor(unittest.TestCase):
    """Test cases for CommandProcessor functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.processor = CommandProcessor()
    
    def test_help_command(self):
        """Test help command."""
        result = self.processor.process_command("help")
        
        self.assertIn("Available commands:", result)
        self.assertIn("create", result)
        self.assertIn("delete", result)
        self.assertIn("list", result)
        self.assertIn("exit", result)
    
    def test_exit_command(self):
        """Test exit command."""
        result = self.processor.process_command("exit")
        self.assertEqual(result, "Goodbye!")
        
        result = self.processor.process_command("quit")
        self.assertEqual(result, "Goodbye!")
    
    def test_empty_command(self):
        """Test empty command handling."""
        result = self.processor.process_command("")
        self.assertEqual(result, "")
        
        result = self.processor.process_command("   ")
        self.assertEqual(result, "")
    
    def test_unknown_command(self):
        """Test unknown command handling."""
        result = self.processor.process_command("unknown")
        self.assertIn("Unknown command:", result)
        self.assertIn("help", result)
    
    def test_create_point_success(self):
        """Test successful point creation."""
        result = self.processor.process_command("create point 10 20")
        
        self.assertEqual(result, "Point created with ID: 1")
        
        # Verify the shape was created
        shapes = self.processor.shape_manager.list_shapes()
        self.assertEqual(len(shapes), 1)
        self.assertEqual(shapes[0].x, 10.0)
        self.assertEqual(shapes[0].y, 20.0)
    
    def test_create_point_invalid_args(self):
        """Test point creation with invalid arguments."""
        # Too few arguments
        result = self.processor.process_command("create point 10")
        self.assertIn("Error:", result)
        self.assertIn("requires 2 coordinates", result)
        
        # Too many arguments
        result = self.processor.process_command("create point 10 20 30")
        self.assertIn("Error:", result)
        
        # Invalid numeric values
        result = self.processor.process_command("create point abc def")
        self.assertIn("Error:", result)
        self.assertIn("Invalid numeric value", result)
    
    def test_create_circle_success(self):
        """Test successful circle creation."""
        result = self.processor.process_command("create circle 0 0 5")
        
        self.assertEqual(result, "Circle created with ID: 1")
        
        # Verify the shape was created
        shapes = self.processor.shape_manager.list_shapes()
        self.assertEqual(len(shapes), 1)
        self.assertEqual(shapes[0].center_x, 0.0)
        self.assertEqual(shapes[0].center_y, 0.0)
        self.assertEqual(shapes[0].radius, 5.0)
    
    def test_create_circle_invalid_radius(self):
        """Test circle creation with invalid radius."""
        result = self.processor.process_command("create circle 0 0 -5")
        self.assertIn("Error:", result)
        self.assertIn("Radius must be positive", result)
        
        result = self.processor.process_command("create circle 0 0 0")
        self.assertIn("Error:", result)
        self.assertIn("Radius must be positive", result)
    
    def test_create_circle_invalid_args(self):
        """Test circle creation with invalid arguments."""
        # Too few arguments
        result = self.processor.process_command("create circle 0 0")
        self.assertIn("Error:", result)
        self.assertIn("requires center and radius", result)
        
        # Invalid numeric values
        result = self.processor.process_command("create circle abc def ghi")
        self.assertIn("Error:", result)
        self.assertIn("Invalid numeric value", result)
    
    def test_create_line_success(self):
        """Test successful line creation."""
        result = self.processor.process_command("create line 0 0 3 4")
        
        self.assertEqual(result, "Line created with ID: 1")
        
        # Verify the shape was created
        shapes = self.processor.shape_manager.list_shapes()
        self.assertEqual(len(shapes), 1)
        self.assertEqual(shapes[0].x1, 0.0)
        self.assertEqual(shapes[0].y1, 0.0)
        self.assertEqual(shapes[0].x2, 3.0)
        self.assertEqual(shapes[0].y2, 4.0)
    
    def test_create_line_invalid_args(self):
        """Test line creation with invalid arguments."""
        # Too few arguments
        result = self.processor.process_command("create line 0 0 3")
        self.assertIn("Error:", result)
        self.assertIn("requires 4 coordinates", result)
        
        # Invalid numeric values
        result = self.processor.process_command("create line abc def ghi jkl")
        self.assertIn("Error:", result)
        self.assertIn("Invalid numeric value", result)
    
    def test_create_square_success(self):
        """Test successful square creation."""
        result = self.processor.process_command("create square 3 3 4")
        
        self.assertEqual(result, "Square created with ID: 1")
        
        # Verify the shape was created
        shapes = self.processor.shape_manager.list_shapes()
        self.assertEqual(len(shapes), 1)
        self.assertEqual(shapes[0].x, 3.0)
        self.assertEqual(shapes[0].y, 3.0)
        self.assertEqual(shapes[0].side, 4.0)
    
    def test_create_square_invalid_side(self):
        """Test square creation with invalid side length."""
        result = self.processor.process_command("create square 0 0 -5")
        self.assertIn("Error:", result)
        self.assertIn("Side length must be positive", result)
        
        result = self.processor.process_command("create square 0 0 0")
        self.assertIn("Error:", result)
        self.assertIn("Side length must be positive", result)
    
    def test_create_square_invalid_args(self):
        """Test square creation with invalid arguments."""
        # Too few arguments
        result = self.processor.process_command("create square 0 0")
        self.assertIn("Error:", result)
        self.assertIn("requires position and side length", result)
        
        # Invalid numeric values
        result = self.processor.process_command("create square abc def ghi")
        self.assertIn("Error:", result)
        self.assertIn("Invalid numeric value", result)
    
    def test_create_unknown_shape(self):
        """Test creating an unknown shape type."""
        result = self.processor.process_command("create triangle 0 0 1 1 2 2")
        self.assertIn("Error:", result)
        self.assertIn("Unknown shape type", result)
        self.assertIn("triangle", result)
    
    def test_delete_existing_shape(self):
        """Test deleting an existing shape."""
        # Create a shape first
        self.processor.process_command("create point 10 20")
        
        # Delete it
        result = self.processor.process_command("delete 1")
        self.assertEqual(result, "Shape 1 deleted successfully")
        
        # Verify it's gone
        shapes = self.processor.shape_manager.list_shapes()
        self.assertEqual(len(shapes), 0)
    
    def test_delete_nonexistent_shape(self):
        """Test deleting a non-existent shape."""
        result = self.processor.process_command("delete 999")
        self.assertIn("Error:", result)
        self.assertIn("Shape with ID 999 not found", result)
    
    def test_delete_invalid_args(self):
        """Test delete command with invalid arguments."""
        # No arguments
        result = self.processor.process_command("delete")
        self.assertIn("Error:", result)
        self.assertIn("Please provide a shape ID", result)
        
        # Invalid ID
        result = self.processor.process_command("delete abc")
        self.assertIn("Error:", result)
        self.assertIn("Shape ID must be a number", result)
    
    def test_list_empty(self):
        """Test listing when no shapes exist."""
        result = self.processor.process_command("list")
        self.assertEqual(result, "No shapes created yet.")
    
    def test_list_with_shapes(self):
        """Test listing when shapes exist."""
        # Create multiple shapes
        self.processor.process_command("create point 10 20")
        self.processor.process_command("create circle 0 0 5")
        
        result = self.processor.process_command("list")
        
        self.assertIn("Created shapes:", result)
        self.assertIn("1: Point(10.0, 20.0)", result)
        self.assertIn("2: Circle(center=(0.0, 0.0), radius=5.0)", result)
    
    def test_clear_command(self):
        """Test clear command."""
        # Create multiple shapes
        self.processor.process_command("create point 10 20")
        self.processor.process_command("create circle 0 0 5")
        
        # Clear all
        result = self.processor.process_command("clear")
        self.assertEqual(result, "Cleared 2 shape(s).")
        
        # Verify all are gone
        shapes = self.processor.shape_manager.list_shapes()
        self.assertEqual(len(shapes), 0)
    
    def test_case_insensitive_commands(self):
        """Test that commands are case insensitive."""
        result = self.processor.process_command("HELP")
        self.assertIn("Available commands:", result)
        
        result = self.processor.process_command("Create Point 10 20")
        self.assertEqual(result, "Point created with ID: 1")
        
        result = self.processor.process_command("LIST")
        self.assertIn("Created shapes:", result)
        
        result = self.processor.process_command("EXIT")
        self.assertEqual(result, "Goodbye!")


if __name__ == "__main__":
    unittest.main()
