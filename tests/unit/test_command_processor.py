"""Essential unit tests for CommandProcessor class"""

import unittest
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from cli.commands import CommandProcessor


class TestCommandProcessorEssential(unittest.TestCase):
    """Essential test cases for CommandProcessor functionality"""
    
    def setUp(self):
        """Set up test fixtures."""
        self.processor = CommandProcessor()
    
    def test_create_all_shape_types(self):
        """Test creating all shape types via commands"""
        # Test point creation
        result = self.processor.process_command("create point 10 20")
        self.assertEqual(result, "Point created with ID: 1")
        
        # Test circle creation
        result = self.processor.process_command("create circle 0 0 5")
        self.assertEqual(result, "Circle created with ID: 2")
        
        # Test line creation
        result = self.processor.process_command("create line 0 0 3 4")
        self.assertEqual(result, "Line created with ID: 3")
        
        # Test square creation
        result = self.processor.process_command("create square 2 3 4")
        self.assertEqual(result, "Square created with ID: 4")
        
        # Verify all shapes were created
        shapes = self.processor.shape_manager.list_shapes()
        self.assertEqual(len(shapes), 4)
    
    def test_list_and_delete_commands(self):
        """Test list and delete commands functionality"""
        # Create some shapes first
        self.processor.process_command("create point 10 20")
        self.processor.process_command("create circle 0 0 5")
        
        # Test list command
        result = self.processor.process_command("list")
        self.assertIn("Point(10.0, 20.0)", result)
        self.assertIn("Circle(center=(0.0, 0.0), radius=5.0)", result)
        
        # Test delete command
        result = self.processor.process_command("delete 1")
        self.assertEqual(result, "Shape 1 deleted successfully")
        
        # Verify deletion
        shapes = self.processor.shape_manager.list_shapes()
        self.assertEqual(len(shapes), 1)
        self.assertEqual(shapes[0].id, 2)
    
    def test_error_handling_for_invalid_commands(self):
        """Test error handling for various invalid commands"""
        # Test invalid create command (missing arguments)
        result = self.processor.process_command("create point")
        self.assertIn("Error:", result)
        
        # Test invalid shape type
        result = self.processor.process_command("create triangle 0 0 1 1 1")
        self.assertIn("Error:", result)
        
        # Test invalid delete (non-existent ID)
        result = self.processor.process_command("delete 999")
        self.assertIn("Error:", result)
        
        # Test unknown command
        result = self.processor.process_command("unknown_command")
        self.assertIn("Unknown command", result)  # Check for actual error message
    
    def test_help_and_exit_commands(self):
        """Test help and exit commands functionality"""
        # Test help command
        result = self.processor.process_command("help")
        self.assertIn("Available commands:", result)
        self.assertIn("create", result)
        self.assertIn("delete", result)
        self.assertIn("list", result)
        
        # Test exit command
        result = self.processor.process_command("exit")
        self.assertEqual(result, "Goodbye!")


if __name__ == "__main__":
    unittest.main()
