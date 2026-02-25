"""Kaynat Queue - FIFO data structure."""

from collections import deque
from kaynat.interpreter.runtime_types import KaynatNumber
from kaynat.errors.error_types import RuntimeError as KaynatRuntimeError


class Queue:
    """Queue data structure (First In, First Out)."""
    
    def __init__(self):
        """Initialize empty queue."""
        self.items = deque()
    
    def enqueue(self, item):
        """Add item to rear of queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return item from front of queue."""
        if self.is_empty():
            raise KaynatRuntimeError("Cannot dequeue from empty queue")
        return self.items.popleft()
    
    def peek(self):
        """Peek at front item without removing."""
        if self.is_empty():
            raise KaynatRuntimeError("Cannot peek at empty queue")
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Get size of queue."""
        return KaynatNumber(len(self.items))
    
    def clear(self):
        """Clear all items from queue."""
        self.items.clear()
    
    def to_list(self):
        """Convert queue to list."""
        from kaynat.interpreter.runtime_types import KaynatList
        return KaynatList(list(self.items))
