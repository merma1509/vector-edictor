# Vector Editor CLI

A professional command-line vector editor for creating and managing geometric shapes with file persistence

## Features

- **6 Shape Types**: Point, Line, Circle, Square, Oval, Rectangle
- **File Operations**: Save and load shapes to/from JSON files
- **CLI**: User-friendly commands with comprehensive help
- **Error Handling**: Robust input validation and error messages
- **Zero Dependencies**: Uses only Python standard library

## Quick Start

```bash
# Clone and setup
git clone <this repository URL>
cd vector-edictor
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Run the CLI
python main.py
```

## Usage

### Creating Shapes

```bash
create point 10 20
create line 0 0 5 5
create circle 0 0 10
create square 3 3 5
create oval 0 0 8 6
create rectangle 2 4 10 6
```

### File Operations

```bash
save my_shapes.json      # Save shapes with preview
load my_shapes.json      # Load shapes with JSON display
```

### Shape Management

```bash
list                    # Show all shapes
delete 1                # Delete shape by ID
clear                   # Delete all shapes
help                    # Show help
exit                    # Exit program
```

## Architecture

```markdown
vector-edictor/
├── models/           # Shape classes (Point, Line, Circle, Square, Oval, Rectangle)
├── services/         # Business logic (ShapeManager, FileManager)
├── cli/              # Command-line interface (CommandProcessor)
├── tests/            # Comprehensive test suite
└── main.py           # Application entry point
```

## File Format

Shapes are saved in JSON format:

```json
{
  "version": "1.0",
  "shape_count": 2,
  "shapes": [
    {
      "type": "rectangle",
      "id": 1,
      "x": 2.0,
      "y": 4.0,
      "width": 10.0,
      "height": 6.0
    },
    {
      "type": "circle",
      "id": 2,
      "center_x": 0.0,
      "center_y": 0.0,
      "radius": 5.0
    }
  ]
}
```

## Testing

Run the comprehensive test suite:

```bash
python run_tests.py              # Run all tests
python run_tests.py unit         # Run unit tests only
python run_tests.py integration  # Run integration tests only
```

- Shape classes: Properties, calculations, serialization
- ShapeManager: CRUD operations, file persistence
- CommandProcessor: CLI commands, error handling
- Integration: End-to-end workflows

## Development

```bash
# Code formatting
black .
isort .

# Type checking
mypy .

# Linting
flake8 .

# Testing with coverage
pytest --cov=. tests/
```
