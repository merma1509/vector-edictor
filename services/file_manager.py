"""File management service for saving and loading shapes"""

import json
from pathlib import Path
from typing import List
from models.shape import Shape


class FileManager:
    """Handles saving and loading shapes to/from files"""
    
    def __init__(self):
        """Initialize the file manager"""
        self.supported_formats = ['.json']
    
    def save_shapes(self, shapes: List[Shape], filename: str) -> str:
        """Save shapes to a file
        
        Args:
            shapes (list): List of shape objects to save
            filename (string): Name of the file to save to
            
        Returns:
            Success message with file path"""

        # Ensure filename has supported extension
        file_path = Path(filename)
        if file_path.suffix.lower() not in self.supported_formats:
            file_path = file_path.with_suffix('.json')
        
        # Convert shapes to dictionary format
        shapes_data = []
        for shape in shapes:
            shapes_data.append(shape.to_dict())
        
        # Create file data structure
        file_data = {
            'version': '1.0',
            'shape_count': len(shapes_data),
            'shapes': shapes_data
        }
        
        # Write to file
        try:
            with open(file_path, 'w') as f:
                json.dump(file_data, f, indent=2)
            
            return f"Successfully saved {len(shapes)} shapes to {file_path}"
        
        except Exception as e:
            return f"Error saving file: {str(e)}"
    
    def load_shapes(self, filename: str) -> tuple:
        """Load shapes from a file
        
        Args:
            filename (string): Name of the file to load from
            
        Returns:
            Tuple of (success: bool, message: str, shapes_data: List[Dict]) """

        file_path = Path(filename)
        
        # Check if file exists
        if not file_path.exists():
            return False, f"File not found: {file_path}", []
        
        # Check file extension
        if file_path.suffix.lower() not in self.supported_formats:
            return False, f"Unsupported file format: {file_path.suffix}", []
        
        # Read and parse file
        try:
            with open(file_path, 'r') as f:
                file_data = json.load(f)
            
            # Validate file structure
            if 'shapes' not in file_data:
                return False, "Invalid file format: missing 'shapes' section", []
            
            shapes_data = file_data['shapes']
            shape_count = len(shapes_data)
            
            return True, f"Successfully loaded {shape_count} shapes from {file_path}", shapes_data
        
        except json.JSONDecodeError:
            return False, f"Invalid JSON format in file: {file_path}", []
        except Exception as e:
            return False, f"Error loading file: {str(e)}", []
