# Vector Editor CLI

A simple command-line vector editor for creating and managing geometric shapes

## Features

- **Create shapes**: Point, Line segment, Circle, Square
- **Delete shapes**: Remove shapes by ID
- **List shapes**: View all created shapes
- **Interactive mode**: User-friendly CLI interface
- **Error handling**: Comprehensive input validation

## Installation

### Prerequisites

- Python 3.7+ (recommended 3.11)
- uv (modern Python package manager) - optional but recommended

### Setup with uv (Recommended)

1. **Install uv** (if not already installed):

```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2.**Clone and setup the project**:
  
```bash
git clone <repository-url>
cd vector-editor
   
# Create virtual environment
uv venv
   
# Activate environment
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
   
# Install dependencies
uv pip install -r requirements.txt
```

### Setup with Python venv (Traditional)

1. **Clone and setup the project**:

```bash
git clone <repository-url>
cd vector-editor
   
# Create virtual environment
python -m venv venv
   
# Activate environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
   
# Install dependencies
pip install -r requirements.txt
```

## Usage

### Interactive Mode

```bash
python main.py
```

### Command Line Mode

```bash
python main.py create point 10 20
python main.py list
python main.py delete 1
```

## Commands

### Create Shapes

```bash
# Create a point at coordinates (10, 20)
create point 10 20

# Create a line from (0, 0) to (5, 5)
create line 0 0 5 5

# Create a circle with center (0, 0) and radius 10
create circle 0 0 10

# Create a square with top-left corner (3, 3) and side length 5
create square 3 3 5
```

### Manage Shapes

```bash
# List all created shapes
list

# Delete shape with ID 1
delete 1

# Delete all shapes
clear

# Show help
help

# Exit the program
exit
```

## Architecture

The project follows a clean, object-oriented architecture:

```bash
vector_editor/
├── models/           # Shape classes (Point, Line, Circle, Square)
├── services/         # Business logic (ShapeManager)
├── cli/              # Command processing interface
├── tests/            # Test suite
├── main.py           # Entry point
└── README.md         # Documentation
```

### Key Components

- **Shape**: Abstract base class for all shapes
- **ShapeManager**: Handles CRUD operations for shapes
- **CommandProcessor**: Parses and executes CLI commands

## Examples

### Interactive Session

```bash
=== Vector Editor CLI ===
Type 'help' for available commands or 'exit' to quit.

> create point 10 20
Point created with ID: 1

> create circle 0 0 5
Circle created with ID: 2

> list
Created shapes:
  1: Point(10.0, 20.0)
  2: Circle(center=(0.0, 0.0), radius=5.0)

> delete 1
Shape 1 deleted successfully

> list
Created shapes:
  2: Circle(center=(0.0, 0.0), radius=5.0)

> exit
Goodbye!
```

## Testing

The code is designed to be easily testable. You can write unit tests for:

- Shape classes (`models/`)
- ShapeManager functionality (`services/`)
- Command processing (`cli/`)
