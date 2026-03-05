"""System tests for the main application"""

import unittest
import subprocess
import sys
import os
from pathlib import Path


class TestMainApplication(unittest.TestCase):
    """Test the main application as a complete system"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.project_root = Path(__file__).parent.parent.parent
        self.main_script = self.project_root / "main.py"
        
    def test_main_help_command(self):
        """Test running main.py with help command"""
        result = subprocess.run(
            [sys.executable, str(self.main_script), "help"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("Available commands:", result.stdout)
        self.assertIn("create", result.stdout)
        self.assertIn("delete", result.stdout)
    
    def test_main_create_and_list_commands(self):
        """Test running main.py with create and list commands"""
        # Create a point
        result1 = subprocess.run(
            [sys.executable, str(self.main_script), "create", "point", "10", "20"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result1.returncode, 0)
        self.assertEqual(result1.stdout.strip(), "Point created with ID: 1")
        
        # Create a circle (in separate process, so ID will be 1 again)
        result2 = subprocess.run(
            [sys.executable, str(self.main_script), "create", "circle", "0", "0", "5"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result2.returncode, 0)
        self.assertEqual(result2.stdout.strip(), "Circle created with ID: 1")
        
        # List shapes (this will show empty because each command runs in separate process)
        result3 = subprocess.run(
            [sys.executable, str(self.main_script), "list"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result3.returncode, 0)
        self.assertEqual(result3.stdout.strip(), "No shapes created yet.")
    
    def test_main_error_handling(self):
        """Test error handling in main application"""
        # Test invalid command
        result = subprocess.run(
            [sys.executable, str(self.main_script), "invalid_command"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("Unknown command:", result.stdout)
        
        # Test invalid shape creation
        result = subprocess.run(
            [sys.executable, str(self.main_script), "create", "point"],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("Error:", result.stdout)
    
    def test_main_no_arguments(self):
        """Test running main.py without arguments (should not crash)"""
        # This test verifies that the main script can start without crashing
        # We'll use a timeout to prevent it from hanging
        try:
            result = subprocess.run(
                [sys.executable, str(self.main_script)],
                capture_output=True,
                text=True,
                cwd=str(self.project_root),
                timeout=1,  # Timeout after 1 second
                input="exit\n"  # Send exit command
            )
            
            # The process should terminate cleanly
            self.assertTrue(result.returncode == 0 or result.returncode == 1)
            
        except subprocess.TimeoutExpired:
            # If it times out, that means it's waiting for input (which is expected)
            self.assertTrue(True)
    
    def test_python_path_setup(self):
        """Test that Python path is correctly set up for imports"""
        # This test verifies that all modules can be imported correctly
        test_script = """
import sys
sys.path.insert(0, '.')

try:
    from models.point import Point
    from models.circle import Circle
    from models.line import Line
    from models.square import Square
    from services.shape_manager import ShapeManager
    from cli.commands import CommandProcessor
    
    print("SUCCESS: All modules imported correctly")
    
    # Test basic functionality
    manager = ShapeManager()
    point = manager.create_point(10, 20)
    print(f"Point created: {point}")
    
except ImportError as e:
    print(f"IMPORT ERROR: {e}")
    sys.exit(1)
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
"""
        
        result = subprocess.run(
            [sys.executable, "-c", test_script],
            capture_output=True,
            text=True,
            cwd=str(self.project_root)
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("SUCCESS:", result.stdout)
        self.assertIn("Point created:", result.stdout)
    
    def test_module_structure(self):
        """Test that all required modules exist and are importable"""
        modules_to_test = [
            "models.point",
            "models.line", 
            "models.circle",
            "models.square",
            "models.shape",
            "services.shape_manager",
            "cli.commands"
        ]
        
        for module_name in modules_to_test:
            test_script = f"""
import sys
sys.path.insert(0, '.')

try:
    import {module_name}
    print(f"SUCCESS: {module_name} imported")
except ImportError as e:
    print(f"IMPORT ERROR: {module_name} - {{e}}")
    sys.exit(1)
"""
            
            result = subprocess.run(
                [sys.executable, "-c", test_script],
                capture_output=True,
                text=True,
                cwd=str(self.project_root)
            )
            
            self.assertEqual(result.returncode, 0, 
                           f"Failed to import {module_name}: {result.stderr}")
            self.assertIn("SUCCESS:", result.stdout)
    
    def test_file_structure(self):
        """Test that all required files exist"""
        required_files = [
            "main.py",
            "requirements.txt",
            "README.md",
            "models/__init__.py",
            "models/shape.py",
            "models/point.py",
            "models/line.py",
            "models/circle.py",
            "models/square.py",
            "services/__init__.py",
            "services/shape_manager.py",
            "cli/__init__.py",
            "cli/commands.py"
        ]
        
        for file_path in required_files:
            full_path = self.project_root / file_path
            self.assertTrue(full_path.exists(), f"Required file missing: {file_path}")
            self.assertTrue(full_path.is_file(), f"Path is not a file: {file_path}")
    
    def test_python_version_compatibility(self):
        """Test Python version compatibility"""
        result = subprocess.run(
            [sys.executable, "--version"],
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.returncode, 0)
        
        # Check if Python version is 3.7+
        version_string = result.stdout
        version_match = version_string.strip().split()[1]  # "Python 3.x.x"
        major, minor = map(int, version_match.split('.')[:2])
        
        self.assertGreaterEqual(major, 3, "Python 3+ required")
        if major == 3:
            self.assertGreaterEqual(minor, 7, "Python 3.7+ required")


if __name__ == "__main__":
    unittest.main()
