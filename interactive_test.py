"""Test the interactive mode functionality"""

from cli.commands import CommandProcessor


def test_interactive_mode():
    """Test interactive mode with simulated input"""
    processor = CommandProcessor()
    
    # Simulate user input
    simulated_input = """
    create point 15 25
    create circle 5 5 3
    list
    delete 1
    list
    exit
    """
    
    print("=== Interactive Mode Test ===")
    print("Simulating the following commands:")
    for line in simulated_input.strip().split('\n'):
        print(f"  > {line.strip()}")
    
    print("\nProcessing commands:")
    
    for line in simulated_input.strip().split('\n'):
        cmd = line.strip()
        if cmd:
            result = processor.process_command(cmd)
            print(f"  {result}")
            if cmd.lower() in ["exit", "quit"]:
                break
    
    print("\n=== Test Complete ===")


if __name__ == "__main__":
    test_interactive_mode()
