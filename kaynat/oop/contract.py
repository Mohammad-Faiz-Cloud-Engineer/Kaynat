"""
Kaynat Contract System - Interfaces.

Stub implementation for OOP features.
"""


class Contract:
    """
    Represents an interface/contract in Kaynat.
    
    Contracts define required methods that blueprints must implement.
    """
    
    def __init__(self, name, required_methods=None):
        """
        Initialize a contract.
        
        Args:
            name: Contract name
            required_methods: List of required method names
        """
        self.name = name
        self.required_methods = required_methods or []
    
    def add_required_method(self, method_name):
        """Add a required method to the contract."""
        if method_name not in self.required_methods:
            self.required_methods.append(method_name)
    
    def is_implemented_by(self, blueprint):
        """Check if blueprint implements this contract."""
        for method in self.required_methods:
            if method not in blueprint.methods:
                return False
        return True
    
    def __repr__(self):
        return f"<Contract {self.name}>"
