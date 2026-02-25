"""
Kaynat Blueprint System - Class definitions.

Stub implementation for OOP features.
This will be fully implemented in version 2.0.0.
"""


class Blueprint:
    """
    Represents a class definition in Kaynat.
    
    Blueprints define the structure and behavior of objects.
    """
    
    def __init__(self, name, parent=None, properties=None, methods=None):
        """
        Initialize a blueprint.
        
        Args:
            name: Blueprint name
            parent: Parent blueprint for inheritance
            properties: List of property names
            methods: Dictionary of method definitions
        """
        self.name = name
        self.parent = parent
        self.properties = properties or []
        self.methods = methods or {}
        self.is_abstract = False
    
    def create_instance(self, *args, **kwargs):
        """Create an instance of this blueprint."""
        from kaynat.oop.instance import Instance
        return Instance(self, *args, **kwargs)
    
    def add_method(self, name, function):
        """Add a method to the blueprint."""
        self.methods[name] = function
    
    def add_property(self, name):
        """Add a property to the blueprint."""
        if name not in self.properties:
            self.properties.append(name)
    
    def __repr__(self):
        return f"<Blueprint {self.name}>"
