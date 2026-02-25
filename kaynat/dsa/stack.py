"""Kaynat Stack - LIFO data structure."""

from kaynat.interpreter.runtime_types import KaynatNumber, KaynatBoolean
from kaynat.errors.error_types import RuntimeError as KaynatRuntimeError


class Stack:
    """Stack data structure (Last In, First Out)."""
    
    def __init__(self):
        """Initialize empty stack."""
        self.items = []
    
    def push(self, item):
        """Push item onto stack."""
        self.items.append(item)
    
    def pop(self):
        """Pop item from stack."""
        if self.is_empty():
            raise KaynatRuntimeError("Cannot pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Peek at top item without removing."""
        if self.is_empty():
            raise KaynatRuntimeError("Cannot peek at empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Get size of stack."""
        return KaynatNumber(len(self.items))
    
    def clear(self):
        """Clear all items from stack."""
        self.items.clear()
    
    def to_list(self):
        """Convert stack to list."""
        from kaynat.interpreter.runtime_types import KaynatList
        return KaynatList(self.items.copy())
