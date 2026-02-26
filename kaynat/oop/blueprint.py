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
    
    def __init__(self, name, parent=None, properties=None, methods=None, is_abstract=False):
        """
        Initialize a blueprint.
        
        Args:
            name: Blueprint name
            parent: Parent blueprint for inheritance
            properties: List of property names
            methods: Dictionary of method definitions
            is_abstract: Whether this is an abstract blueprint
        """
        self.name = name
        self.parent = parent
        self.properties = properties or []
        self.methods = methods or {}
        self.is_abstract = is_abstract
    
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
    
    def get_all_properties(self):
        """Get all properties including inherited ones."""
        props = list(self.properties)
        if self.parent:
            props.extend(self.parent.get_all_properties())
        return props
    
    def get_all_methods(self):
        """Get all methods including inherited ones."""
        methods = dict(self.methods)
        if self.parent:
            parent_methods = self.parent.get_all_methods()
            # Parent methods are overridden by child methods
            for name, method in parent_methods.items():
                if name not in methods:
                    methods[name] = method
        return methods
    
    def has_method(self, method_name):
        """Check if blueprint has a method."""
        if method_name in self.methods:
            return True
        if self.parent:
            return self.parent.has_method(method_name)
        return False
    
    def __repr__(self):
        return f"<Blueprint {self.name}>"

    
    def to_string(self):
        """Convert to string for printing."""
        return f"<Blueprint {self.name}>"
