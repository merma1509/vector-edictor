"""Integration tests for complete CLI workflows"""

import unittest
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from cli.commands import CommandProcessor


class TestCLIWorkflow(unittest.TestCase):
    """Test complete user workflows through the CLI"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.processor = CommandProcessor()
    
    def test_complete_shape_lifecycle(self):
        """Test complete lifecycle: create -> list -> delete -> list"""
        # Create multiple shapes
        result1 = self.processor.process_command("create point 10 20")
        result2 = self.processor.process_command("create circle 0 0 5")
        result3 = self.processor.process_command("create line 0 0 3 4")
        result4 = self.processor.process_command("create square 2 2 3")
        
        # Verify creation
        self.assertEqual(result1, "Point created with ID: 1")
        self.assertEqual(result2, "Circle created with ID: 2")
        self.assertEqual(result3, "Line created with ID: 3")
        self.assertEqual(result4, "Square created with ID: 4")
        
        # List all shapes
        list_result = self.processor.process_command("list")
        self.assertIn("1: Point(10.0, 20.0)", list_result)
        self.assertIn("2: Circle(center=(0.0, 0.0), radius=5.0)", list_result)
        self.assertIn("3: Line((0.0, 0.0) to (3.0, 4.0))", list_result)
        self.assertIn("4: Square(top-left=(2.0, 2.0), side=3.0)", list_result)
        
        # Delete middle shapes
        delete_result1 = self.processor.process_command("delete 2")
        delete_result2 = self.processor.process_command("delete 3")
        
        self.assertEqual(delete_result1, "Shape 2 deleted successfully")
        self.assertEqual(delete_result2, "Shape 3 deleted successfully")
        
        # List remaining shapes
        list_result2 = self.processor.process_command("list")
        self.assertIn("1: Point(10.0, 20.0)", list_result2)
        self.assertIn("4: Square(top-left=(2.0, 2.0), side=3.0)", list_result2)
        self.assertNotIn("Circle", list_result2)
        self.assertNotIn("Line", list_result2)
        
        # Clear all
        clear_result = self.processor.process_command("clear")
        self.assertEqual(clear_result, "Cleared 2 shape(s).")
        
        # Verify empty
        empty_result = self.processor.process_command("list")
        self.assertEqual(empty_result, "No shapes created yet.")
    
    def test_error_recovery_workflow(self):
        """Test workflow with error handling and recovery"""
        # Try invalid commands
        error1 = self.processor.process_command("create point")
        self.assertIn("Error:", error1)
        
        error2 = self.processor.process_command("create circle 0 0 -5")
        self.assertIn("Error:", error2)
        
        error3 = self.processor.process_command("delete 999")
        self.assertIn("Error:", error3)
        
        # Verify no shapes were created during errors
        list_result = self.processor.process_command("list")
        self.assertEqual(list_result, "No shapes created yet.")
        
        # Now create valid shapes
        valid1 = self.processor.process_command("create point 10 20")
        valid2 = self.processor.process_command("create circle 0 0 5")
        
        self.assertEqual(valid1, "Point created with ID: 1")
        self.assertEqual(valid2, "Circle created with ID: 2")
        
        # Verify shapes exist after errors
        list_result2 = self.processor.process_command("list")
        self.assertIn("1: Point(10.0, 20.0)", list_result2)
        self.assertIn("2: Circle(center=(0.0, 0.0), radius=5.0)", list_result2)
    
    def test_mixed_case_and_spacing_workflow(self):
        """Test workflow with mixed case and extra spacing"""
        # Test case insensitive commands
        result1 = self.processor.process_command("CREATE point 10 20")
        result2 = self.processor.process_command("Create Circle 0 0 5")
        result3 = self.processor.process_command("LIST")
        
        self.assertEqual(result1, "Point created with ID: 1")
        self.assertEqual(result2, "Circle created with ID: 2")
        self.assertIn("1: Point(10.0, 20.0)", result3)
        self.assertIn("2: Circle(center=(0.0, 0.0), radius=5.0)", result3)
        
        # Test commands with extra spacing
        result4 = self.processor.process_command("  create   line   0   0   3   4  ")
        self.assertEqual(result4, "Line created with ID: 3")
        
        result5 = self.processor.process_command("\tdelete\t1\t")
        self.assertEqual(result5, "Shape 1 deleted successfully")
    
    def test_complex_geometric_operations(self):
        """Test workflow with complex geometric operations"""
        # Create shapes with specific geometric properties
        shapes_data = [
            ("create point 0 0", "origin point"),
            ("create point 10 0", "point on x-axis"),
            ("create point 0 10", "point on y-axis"),
            ("create circle 0 0 5", "circle at origin"),
            ("create line 0 0 10 0", "horizontal line"),
            ("create line 0 0 0 10", "vertical line"),
            ("create square -5 -5 10", "large square"),
        ]
        
        created_ids = []
        for cmd, description in shapes_data:
            result = self.processor.process_command(cmd)
            self.assertIn("created with ID:", result)
            # Extract ID from result
            id_str = result.split("ID: ")[1]
            created_ids.append(int(id_str))
        
        # Verify all shapes exist
        list_result = self.processor.process_command("list")
        for shape_id in created_ids:
            self.assertIn(f"{shape_id}:", list_result)
        
        # Test selective deletion
        # Delete the origin point
        delete_result = self.processor.process_command("delete 1")
        self.assertEqual(delete_result, "Shape 1 deleted successfully")
        
        # Delete the circle
        delete_result = self.processor.process_command("delete 4")
        self.assertEqual(delete_result, "Shape 4 deleted successfully")
        
        # Verify remaining shapes
        final_list = self.processor.process_command("list")
        self.assertNotIn("1:", final_list)
        self.assertNotIn("4:", final_list)
        self.assertIn("2:", final_list)  # point on x-axis
        self.assertIn("3:", final_list)  # point on y-axis
        self.assertIn("5:", final_list)  # horizontal line
        self.assertIn("6:", final_list)  # vertical line
        self.assertIn("7:", final_list)  # large square
    
    def test_help_and_exit_workflow(self):
        """Test help and exit commands in workflow"""
        # Start with help
        help_result = self.processor.process_command("help")
        self.assertIn("Available commands:", help_result)
        
        # Create some shapes
        self.processor.process_command("create point 10 20")
        self.processor.process_command("create circle 0 0 5")
        
        # List shapes
        list_result = self.processor.process_command("list")
        self.assertIn("Created shapes:", list_result)
        
        # Test exit command
        exit_result = self.processor.process_command("exit")
        self.assertEqual(exit_result, "Goodbye!")
        
        # Test quit command
        quit_result = self.processor.process_command("quit")
        self.assertEqual(quit_result, "Goodbye!")
    
    def test_boundary_value_workflow(self):
        """Test workflow with boundary values"""
        # Test with zero and very small values
        result1 = self.processor.process_command("create point 0 0")
        self.assertEqual(result1, "Point created with ID: 1")
        
        result2 = self.processor.process_command("create circle 0 0 0.001")
        self.assertEqual(result2, "Circle created with ID: 2")
        
        result3 = self.processor.process_command("create square 0 0 0.001")
        self.assertEqual(result3, "Square created with ID: 3")
        
        # Test with large values
        result4 = self.processor.process_command("create point 999999 999999")
        self.assertEqual(result4, "Point created with ID: 4")
        
        result5 = self.processor.process_command("create circle 0 0 1000000")
        self.assertEqual(result5, "Circle created with ID: 5")
        
        # Verify all shapes exist and have correct properties
        shapes = self.processor.shape_manager.list_shapes()
        self.assertEqual(len(shapes), 5)
        
        # Check specific properties
        point_origin = self.processor.shape_manager.get_shape(1)
        self.assertEqual(point_origin.x, 0.0)
        self.assertEqual(point_origin.y, 0.0)
        
        tiny_circle = self.processor.shape_manager.get_shape(2)
        self.assertEqual(tiny_circle.radius, 0.001)
        self.assertGreater(tiny_circle.area(), 0.0)
        
        large_point = self.processor.shape_manager.get_shape(4)
        self.assertEqual(large_point.x, 999999.0)
        self.assertEqual(large_point.y, 999999.0)


if __name__ == "__main__":
    unittest.main()
