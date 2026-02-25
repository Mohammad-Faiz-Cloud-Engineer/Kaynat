"""
Kaynat Instance System - Object instances.

Stub implementation for OOP features.
"""


class Instance:
    """
    Represents an instance of a blueprint (class).
    """
    
    def __init__(self, blueprint, *args, **kwargs):
        """
        Initialize an instance.
        
        Args:
            blueprint: The blueprint this is an instance of
            args: Arguments for initialization
            kwargs: Keyword arguments for initialization
        """
        self.blueprint = blueprint
        self.properties = {}
        
        # Initialize properties
        for prop in blueprint.properties:
            self.properties[prop] = None
        
        # Call initializer if exists
        if 'initialize' in blueprint.methods:
            blueprint.methods['initialize'](self, *args, **kwargs)
    
    def get_property(self, name):
        """Get property value."""
        if name in self.properties:
            return self.properties[name]
        raise AttributeError(f"Property '{name}' not found")
    
    def set_property(self, name, value):
        """Set property value."""
        self.properties[name] = value
    
    def call_method(self, name, *args, **kwargs):
        """Call a method on this instance."""
        if name in self.blueprint.methods:
            return self.blueprint.methods[name](self, *args, **kwargs)
        raise AttributeError(f"Method '{name}' not found")
    
    def __repr__(self):
        return f"<Instance of {self.blueprint.name}>"
