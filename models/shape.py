"""Base shape class for the vector editor"""

from abc import ABC, abstractmethod
from typing import Any, Dict
from dataclasses import dataclass


@dataclass
class Shape(ABC):
    """Abstract base class for all shapes"""
    
    id: int
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape"""
        pass
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convert shape to dictionary representation"""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """String representation of the shape"""
        pass
