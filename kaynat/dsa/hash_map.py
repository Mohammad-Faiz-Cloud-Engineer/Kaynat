"""Kaynat Hash Map."""


class HashMap:
    """Hash Map data structure."""
    
    def __init__(self):
        self.map = {}
    
    def put(self, key, value):
        """Put key-value pair."""
        self.map[key] = value
    
    def get(self, key):
        """Get value by key."""
        return self.map.get(key)
    
    def remove(self, key):
        """Remove key-value pair."""
        if key in self.map:
            del self.map[key]
    
    def contains(self, key):
        """Check if key exists."""
        return key in self.map
    
    def size(self):
        """Get size of map."""
        return len(self.map)
    
    def keys(self):
        """Get all keys."""
        return list(self.map.keys())
    
    def values(self):
        """Get all values."""
        return list(self.map.values())
