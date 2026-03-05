"""Demo script showcasing the Vector Editor CLI functionality"""

from cli.commands import CommandProcessor


def run_demo():
    """Run a comprehensive demo of the vector editor"""
    processor = CommandProcessor()
    
    print("=== Vector Editor CLI Demo ===\n")
    
    # Demo 1: Create various shapes
    print("1. Creating shapes:")
    commands = [
        "create point 10 20",
        "create circle 0 0 5",
        "create line 0 0 10 10",
        "create square 3 3 4"
    ]
    
    for cmd in commands:
        result = processor.process_command(cmd)
        print(f"  > {cmd}")
        print(f"  {result}")
    
    print()
    
    # Demo 2: List all shapes
    print("2. Listing all shapes:")
    result = processor.process_command("list")
    print("  > list")
    for line in result.split('\n'):
        print(f"  {line}")
    
    print()
    
    # Demo 3: Delete a shape
    print("3. Deleting a shape:")
    result = processor.process_command("delete 2")
    print("  > delete 2")
    print(f"  {result}")
    
    print()
    
    # Demo 4: List remaining shapes
    print("4. Listing remaining shapes:")
    result = processor.process_command("list")
    print("  > list")
    for line in result.split('\n'):
        print(f"  {line}")
    
    print()
    
    # Demo 5: Error handling
    print("5. Error handling examples:")
    error_commands = [
        "create point",
        "create circle 0 0 -5",
        "delete 999",
        "unknown_command"
    ]
    
    for cmd in error_commands:
        result = processor.process_command(cmd)
        print(f"  > {cmd}")
        print(f"  {result}")
    
    print()
    
    # Demo 6: Clear all
    print("6. Clearing all shapes:")
    result = processor.process_command("clear")
    print("  > clear")
    print(f"  {result}")
    
    print()
    
    # Demo 7: Verify empty
    print("7. Verifying empty state:")
    result = processor.process_command("list")
    print("  > list")
    print(f"  {result}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    run_demo()
