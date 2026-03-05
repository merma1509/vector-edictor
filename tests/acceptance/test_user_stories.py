"""Acceptance tests based on user stories"""

import unittest
import subprocess
import sys
import time
from pathlib import Path


class TestUserStories(unittest.TestCase):
    """Acceptance tests based on real user scenarios"""
    
    def setUp(self):
        """Set up test fixtures."""
        self.project_root = Path(__file__).parent.parent.parent
        self.main_script = self.project_root / "main.py"
    
    def test_user_story_1_basic_shape_creation(self):
        """User Story 1: As a user, I want to create basic shapes to work with geometric objects"""
        
        # Scenario: Create a point
        result = subprocess.run(
            [sys.executable, str(self.main_script), "create", "point", "10", "20"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("Point created with ID: 1", result.stdout)
        
        # Scenario: Create a circle
        result = subprocess.run(
            [sys.executable, str(self.main_script), "create", "circle", "0", "0", "5"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("Circle created with ID: 1", result.stdout)
        
        # Scenario: Create a line
        result = subprocess.run(
            [sys.executable, str(self.main_script), "create", "line", "0", "0", "10", "10"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("Line created with ID: 1", result.stdout)
        
        # Scenario: Create a square
        result = subprocess.run(
            [sys.executable, str(self.main_script), "create", "square", "3", "3", "4"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("Square created with ID: 1", result.stdout)
    
    def test_user_story_2_shape_management(self):
        """User Story 2: As a user, I want to view and manage my created shapes."""
        
        # This test uses a single processor instance to maintain state
        test_script = """
import sys
sys.path.insert(0, '.')

from cli.commands import CommandProcessor

processor = CommandProcessor()

# Create multiple shapes
print(processor.process_command("create point 10 20"))
print(processor.process_command("create circle 0 0 5"))
print(processor.process_command("create line 0 0 3 4"))

# List all shapes
list_result = processor.process_command("list")
print(list_result)

# Verify all shapes are listed
assert "1: Point(10.0, 20.0)" in list_result
assert "2: Circle(center=(0.0, 0.0), radius=5.0)" in list_result
assert "3: Line((0.0, 0.0) to (3.0, 4.0))" in list_result

# Delete one shape
delete_result = processor.process_command("delete 2")
print(delete_result)
assert "Shape 2 deleted successfully" in delete_result

# List remaining shapes
list_result2 = processor.process_command("list")
print(list_result2)

# Verify deleted shape is gone
assert "1: Point(10.0, 20.0)" in list_result2
assert "3: Line((0.0, 0.0) to (3.0, 4.0))" in list_result2
assert "Circle" not in list_result2

print("SUCCESS: Shape management workflow completed")
"""
        
        result = subprocess.run(
            [sys.executable, "-c", test_script],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("SUCCESS:", result.stdout)
    
    def test_user_story_3_error_handling(self):
        """User Story 3: As a user, I want clear error messages when I make mistakes."""
        
        test_script = """
import sys
sys.path.insert(0, '.')

from cli.commands import CommandProcessor

processor = CommandProcessor()

# Test invalid shape creation
result1 = processor.process_command("create point")
assert "Error:" in result1
assert "requires 2 coordinates" in result1
print("Point error test passed")

# Test negative radius
result2 = processor.process_command("create circle 0 0 -5")
assert "Error:" in result2
assert "Radius must be positive" in result2
print("Circle error test passed")

# Test invalid deletion
result3 = processor.process_command("delete 999")
assert "Error:" in result3
assert "Shape with ID 999 not found" in result3
print("Delete error test passed")

# Test unknown command
result4 = processor.process_command("invalid_command")
assert "Unknown command:" in result4
assert "help" in result4
print("Unknown command error test passed")

print("SUCCESS: All error handling tests passed")
"""
        
        result = subprocess.run(
            [sys.executable, "-c", test_script],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("SUCCESS:", result.stdout)
    
    def test_user_story_4_help_system(self):
        """User Story 4: As a user, I want help to learn how to use the application."""
        
        # Test help command
        result = subprocess.run(
            [sys.executable, str(self.main_script), "help"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        
        # Verify help contains all expected sections
        help_content = result.stdout
        self.assertIn("Available commands:", help_content)
        self.assertIn("create", help_content)
        self.assertIn("delete", help_content)
        self.assertIn("list", help_content)
        self.assertIn("clear", help_content)
        self.assertIn("help", help_content)
        self.assertIn("exit", help_content)
        
        # Verify specific shape examples are included
        self.assertIn("point <x> <y>", help_content)
        self.assertIn("circle <cx> <cy> <r>", help_content)
        self.assertIn("line <x1> <y1> <x2> <y2>", help_content)
        self.assertIn("square <x> <y> <side>", help_content)
        
        # Verify examples are included
        self.assertIn("create point 10 20", help_content)
        self.assertIn("create line 0 0 5 5", help_content)
    
    def test_user_story_5_complex_workflow(self):
        """User Story 5: As a user, I want to perform complex geometric workflows."""
        
        test_script = """
import sys
sys.path.insert(0, '.')

from cli.commands import CommandProcessor

processor = CommandProcessor()

# Complex workflow: Create geometric construction
# 1. Create origin point
result1 = processor.process_command("create point 0 0")
assert "Point created with ID: 1" in result1

# 2. Create circle centered at origin
result2 = processor.process_command("create circle 0 0 10")
assert "Circle created with ID: 2" in result2

# 3. Create points on the circle
result3 = processor.process_command("create point 10 0")  # Rightmost point
assert "Point created with ID: 3" in result3

result4 = processor.process_command("create point 0 10")  # Top point
assert "Point created with ID: 4" in result4

result5 = processor.process_command("create point -10 0")  # Leftmost point
assert "Point created with ID: 5" in result5

result6 = processor.process_command("create point 0 -10")  # Bottom point
assert "Point created with ID: 6" in result6

# 4. Create lines to form a square
result7 = processor.process_command("create line 10 0 0 10")  # Top-right edge
assert "Line created with ID: 7" in result7

result8 = processor.process_command("create line 0 10 -10 0")  # Top-left edge
assert "Line created with ID: 8" in result8

result9 = processor.process_command("create line -10 0 0 -10")  # Bottom-left edge
assert "Line created with ID: 9" in result9

result10 = processor.process_command("create line 0 -10 10 0")  # Bottom-right edge
assert "Line created with ID: 10" in result10

# 5. Create bounding square
result11 = processor.process_command("create square -10 -10 20")
assert "Square created with ID: 11" in result11

# 6. List all shapes to verify construction
list_result = processor.process_command("list")
print("=== GEOMETRIC CONSTRUCTION ===")
print(list_result)

# Verify all shapes exist
shapes_count = len(processor.shape_manager.list_shapes())
assert shapes_count == 11, f"Expected 11 shapes, got {shapes_count}"

# 7. Clean up construction (remove circle and keep square)
processor.process_command("delete 2")

# 8. Verify final state
final_list = processor.process_command("list")
assert "Circle" not in final_list
assert "Square" in final_list

print("SUCCESS: Complex geometric workflow completed")
"""
        
        result = subprocess.run(
            [sys.executable, "-c", test_script],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("SUCCESS:", result.stdout)
        self.assertIn("GEOMETRIC CONSTRUCTION", result.stdout)
    
    def test_user_story_6_performance_with_many_shapes(self):
        """User Story 6: As a user, I want the application to handle many shapes efficiently."""
        
        test_script = """
import sys
import time
sys.path.insert(0, '.')

from cli.commands import CommandProcessor

processor = CommandProcessor()

# Performance test: Create 100 shapes
start_time = time.time()

for i in range(25):  # 25 points
    processor.process_command(f"create point {i} {i}")

for i in range(25):  # 25 circles
    processor.process_command(f"create circle {i} {i} {i+1}")

for i in range(25):  # 25 lines
    processor.process_command(f"create line {i} {i} {i+1} {i+1}")

for i in range(25):  # 25 squares
    processor.process_command(f"create square {i} {i} {i+1}")

creation_time = time.time() - start_time

# Test listing performance
start_time = time.time()
list_result = processor.process_command("list")
list_time = time.time() - start_time

# Verify all shapes were created
shapes_count = len(processor.shape_manager.list_shapes())
assert shapes_count == 100, f"Expected 100 shapes, got {shapes_count}"

# Performance assertions (should be fast)
assert creation_time < 2.0, f"Creation too slow: {creation_time}s"
assert list_time < 0.5, f"Listing too slow: {list_time}s"

print(f"SUCCESS: Created {shapes_count} shapes in {creation_time:.3f}s")
print(f"Listed shapes in {list_time:.3f}s")
"""
        
        result = subprocess.run(
            [sys.executable, "-c", test_script],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("SUCCESS:", result.stdout)
        self.assertIn("Created 100 shapes", result.stdout)
    
    def test_user_story_7_data_persistence_simulation(self):
        """User Story 7: As a user, I want to export/import shape data (simulated)."""
        
        test_script = """
import sys
import json
sys.path.insert(0, '.')

from cli.commands import CommandProcessor

processor = CommandProcessor()

# Create some shapes
processor.process_command("create point 10 20")
processor.process_command("create circle 0 0 5")
processor.process_command("create line 0 0 3 4")

# Export shapes to JSON format (simulate persistence)
shapes = processor.shape_manager.list_shapes()
export_data = [shape.to_dict() for shape in shapes]

# Verify export format
assert len(export_data) == 3
assert export_data[0]['type'] == 'point'
assert export_data[1]['type'] == 'circle'
assert export_data[2]['type'] == 'line'

# Convert to JSON and back
json_data = json.dumps(export_data)
imported_data = json.loads(json_data)

# Verify data integrity
assert len(imported_data) == 3
assert imported_data[0]['x'] == 10.0
assert imported_data[0]['y'] == 20.0
assert imported_data[1]['radius'] == 5.0

print("SUCCESS: Data export/import simulation completed")
print(f"Exported {len(export_data)} shapes")
print(f"JSON data: {json_data}")
"""
        
        result = subprocess.run(
            [sys.executable, "-c", test_script],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("SUCCESS:", result.stdout)
        self.assertIn("Exported 3 shapes", result.stdout)


if __name__ == "__main__":
    unittest.main()
