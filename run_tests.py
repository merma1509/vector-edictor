"""Test runner for the vector editor project"""

import unittest
import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


def run_all_tests():
    """Run all tests in the tests directory"""
    # Import essential test modules directly
    import tests.unit.test_shapes
    import tests.unit.test_shape_manager
    import tests.unit.test_command_processor
    import tests.integration.test_cli_workflow
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all essential test cases
    suite.addTests(loader.loadTestsFromModule(tests.unit.test_shapes))
    suite.addTests(loader.loadTestsFromModule(tests.unit.test_shape_manager))
    suite.addTests(loader.loadTestsFromModule(tests.unit.test_command_processor))
    suite.addTests(loader.loadTestsFromModule(tests.integration.test_cli_workflow))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


def run_unit_tests():
    """Run only essential unit tests"""
    # Import essential test modules directly
    import tests.unit.test_shapes
    import tests.unit.test_shape_manager
    import tests.unit.test_command_processor
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add essential unit test cases
    suite.addTests(loader.loadTestsFromModule(tests.unit.test_shapes))
    suite.addTests(loader.loadTestsFromModule(tests.unit.test_shape_manager))
    suite.addTests(loader.loadTestsFromModule(tests.unit.test_command_processor))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


def run_integration_tests():
    """Run only integration tests"""
    # Import test modules directly
    import tests.integration.test_cli_workflow
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add integration test cases
    suite.addTests(loader.loadTestsFromModule(tests.integration.test_cli_workflow))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


def main():
    """Main test runner"""
    if len(sys.argv) > 1:
        test_type = sys.argv[1].lower()
        
        if test_type == "unit":
            success = run_unit_tests()
        elif test_type == "integration":
            success = run_integration_tests()
        else:
            print(f"Unknown test type: {test_type}")
            print("Available options: unit, integration")
            success = False
    else:
        print("Running all tests...")
        success = run_all_tests()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
