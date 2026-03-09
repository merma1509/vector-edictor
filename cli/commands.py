"""Command processor for CLI interface"""

from typing import List
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.shape_manager import ShapeManager


class CommandProcessor:
    """Processes CLI commands for the vector editor"""
    
    def __init__(self):
        self.shape_manager = ShapeManager()
    
    def process_command(self, command_line: str) -> str:
        """Process a single command line"""
        if not command_line.strip():
            return ""
        
        parts = command_line.strip().split()
        command = parts[0].lower()
        
        if command == "help":
            return self._show_help()
        elif command == "exit" or command == "quit":
            return "Goodbye!"
        elif command == "create":
            return self._handle_create(parts[1:])
        elif command == "delete":
            return self._handle_delete(parts[1:])
        elif command == "list":
            return self._handle_list()
        elif command == "clear":
            return self._handle_clear()
        elif command == "save":
            return self._handle_save(parts[1:])
        elif command == "load":
            return self._handle_load(parts[1:])
        else:
            return f"Unknown command: {command}. Type 'help' for available commands."
    
    def _show_help(self) -> str:
        """Show help information"""
        help_text = """
Available commands:
  create <shape> <params>     - Create a new shape
    point <x> <y>             - Create a point
    line <x1> <y1> <x2> <y2>  - Create a line segment
    circle <cx> <cy> <r>      - Create a circle (center and radius)
    square <x> <y> <side>     - Create a square (top-left corner and side length)
    oval <cx> <cy> <width> <height> - Create an oval (center and dimensions)
  
  delete <id>                 - Delete a shape by ID
  list                        - List all created shapes
  clear                       - Delete all shapes
  save <filename>             - Save all shapes to a file
  load <filename>             - Load shapes from a file
  help                        - Show this help message
  exit/quit                   - Exit the program

Examples:
  create point 10 20
  create line 0 0 5 5
  create circle 0 0 10
  create square 3 3 5
  create oval 0 0 8 6
  save my_shapes.json
  load my_shapes.json
  delete 1
  list
"""
        return help_text.strip()
    
    def _handle_create(self, args: List[str]) -> str:
        """Handle create command"""
        if not args:
            return "Error: Please specify a shape type. Usage: create <shape> <params>"
        
        shape_type = args[0].lower()
        
        try:
            if shape_type == "point":
                if len(args) != 3:
                    return "Error: Point requires 2 coordinates. Usage: create point <x> <y>"
                x, y = float(args[1]), float(args[2])
                point = self.shape_manager.create_point(x, y)
                return f"Point created with ID: {point.id}"
            
            elif shape_type == "line":
                if len(args) != 5:
                    return "Error: Line requires 4 coordinates. Usage: create line <x1> <y1> <x2> <y2>"
                x1, y1, x2, y2 = map(float, args[1:5])
                line = self.shape_manager.create_line(x1, y1, x2, y2)
                return f"Line created with ID: {line.id}"
            
            elif shape_type == "circle":
                if len(args) != 4:
                    return "Error: Circle requires center and radius. Usage: create circle <cx> <cy> <radius>"
                cx, cy, radius = map(float, args[1:4])
                if radius <= 0:
                    return "Error: Radius must be positive"
                circle = self.shape_manager.create_circle(cx, cy, radius)
                return f"Circle created with ID: {circle.id}"
            
            elif shape_type == "square":
                if len(args) != 4:
                    return "Error: Square requires position and side length. Usage: create square <x> <y> <side>"
                x, y, side = map(float, args[1:4])
                if side <= 0:
                    return "Error: Side length must be positive"
                square = self.shape_manager.create_square(x, y, side)
                return f"Square created with ID: {square.id}"
            
            elif shape_type == "oval":
                if len(args) != 5:
                    return "Error: Oval requires center and dimensions. Usage: create oval <cx> <cy> <width> <height>"
                cx, cy, width, height = map(float, args[1:5])
                if width <= 0 or height <= 0:
                    return "Error: Width and height must be positive"
                oval = self.shape_manager.create_oval(cx, cy, width, height)
                return f"Oval created with ID: {oval.id}"
            
            else:
                return f"Error: Unknown shape type '{shape_type}'. Supported types: point, line, circle, square, oval"
        
        except ValueError as e:
            return f"Error: Invalid numeric value. {str(e)}"
    
    def _handle_delete(self, args: List[str]) -> str:
        """Handle delete command"""
        if len(args) != 1:
            return "Error: Please provide a shape ID. Usage: delete <id>"
        
        try:
            shape_id = int(args[0])
            if self.shape_manager.delete_shape(shape_id):
                return f"Shape {shape_id} deleted successfully"
            else:
                return f"Error: Shape with ID {shape_id} not found"
        except ValueError:
            return "Error: Shape ID must be a number"
    
    def _handle_list(self) -> str:
        """Handle list command"""
        shapes = self.shape_manager.list_shapes()
        
        if not shapes:
            return "No shapes created yet."
        
        # Sort by ID for consistent display
        shapes.sort(key=lambda s: s.id)
        
        result = "Created shapes:\n"
        for shape in shapes:
            result += f"  {shape.id}: {shape}\n"
        
        return result.strip()
    
    def _handle_clear(self) -> str:
        """Handle clear command"""
        count = len(self.shape_manager.list_shapes())
        self.shape_manager.clear_all()
        return f"Cleared {count} shape(s)."
    
    def run_interactive(self) -> None:
        """Run the CLI in interactive mode"""
        print("=== Vector Editor CLI ===")
        print("Type 'help' for available commands or 'exit' to quit.")
        print()
        
        while True:
            try:
                command = input("> ").strip()
                if not command:
                    continue
                
                result = self.process_command(command)
                if result:
                    print(result)
                
                if command.lower() in ["exit", "quit"]:
                    break
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
    
    def _handle_save(self, args: List[str]) -> str:
        """Handle save command"""
        if not args:
            return "Error: Please specify a filename. Usage: save <filename>"
        
        filename = args[0]
        
        # Show what's being saved if there are shapes
        if self.shape_manager.list_shapes():
            shapes_list = self._handle_list()
            result = self.shape_manager.save_shapes(filename)
            return f"{result}\n\n{shapes_list}"
        else:
            return self.shape_manager.save_shapes(filename)
    
    def _handle_load(self, args: List[str]) -> str:
        """Handle load command"""
        if not args:
            return "Error: Please specify a filename. Usage: load <filename>"
        
        filename = args[0]
        success, message = self.shape_manager.load_shapes(filename)
        
        if success and self.shape_manager.list_shapes():
            # Show the loaded shapes after successful load
            shapes_list = self._handle_list()
            return f"{message}\n\n{shapes_list}"
        
        return message
