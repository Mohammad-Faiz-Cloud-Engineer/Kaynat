"""
Kaynat Environment - Variable scope management.

Manages variable storage and scope chains.
"""

from typing import Any, Optional, Dict
from kaynat.errors.error_types import NameError as KaynatNameError


class Environment:
    """
    Manages variable scopes and lookups.
    
    Each environment has an optional parent, creating a scope chain.
    Variables are looked up in the current scope first, then parent scopes.
    """
    
    def __init__(self, parent: Optional['Environment'] = None):
        """
        Initialize a new environment.
        
        Args:
            parent: Parent environment for scope chain
        """
        self.parent = parent
        self.variables: Dict[str, Any] = {}
        self.constants: set = set()
    
    def define(self, name: str, value: Any, is_constant: bool = False):
        """
        Define a new variable in this scope.
        
        Args:
            name: Variable name
            value: Variable value
            is_constant: Whether variable is constant
        """
        self.variables[name] = value
        if is_constant:
            self.constants.add(name)
    
    def get(self, name: str) -> Any:
        """
        Get a variable value.
        
        Args:
            name: Variable name
            
        Returns:
            Variable value
            
        Raises:
            KaynatNameError: If variable is not defined
        """
        if name in self.variables:
            return self.variables[name]
        
        if self.parent:
            return self.parent.get(name)
        
        raise KaynatNameError(f"Variable '{name}' is not defined")
    
    def exists(self, name: str) -> bool:
        """
        Check if a variable exists.
        
        Args:
            name: Variable name
            
        Returns:
            True if variable exists
        """
        if name in self.variables:
            return True
        
        if self.parent:
            return self.parent.exists(name)
        
        return False
    
    def set(self, name: str, value: Any):
        """
        Set a variable value.
        
        Args:
            name: Variable name
            value: New value
            
        Raises:
            KaynatNameError: If variable is not defined or is constant
        """
        if name in self.variables:
            if name in self.constants:
                raise KaynatNameError(f"Cannot change constant '{name}'")
            self.variables[name] = value
            return
        
        if self.parent:
            self.parent.set(name, value)
            return
        
        raise KaynatNameError(f"Variable '{name}' is not defined")
    
    def delete(self, name: str):
        """
        Delete a variable.
        
        Args:
            name: Variable name
            
        Raises:
            KaynatNameError: If variable is not defined or is constant
        """
        if name in self.variables:
            if name in self.constants:
                raise KaynatNameError(f"Cannot delete constant '{name}'")
            del self.variables[name]
            return
        
        if self.parent:
            self.parent.delete(name)
            return
        
        raise KaynatNameError(f"Variable '{name}' is not defined")
