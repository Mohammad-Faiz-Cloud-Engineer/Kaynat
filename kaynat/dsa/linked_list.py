"""Kaynat Linked List."""

from kaynat.interpreter.runtime_types import KaynatNumber


class Node:
    """Node in linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Singly linked list."""
    
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, value):
        """Add node to end."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
    
    def prepend(self, value):
        """Add node to beginning."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def delete(self, value):
        """Delete first node with value."""
        if not self.head:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return
        
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next
    
    def find(self, value):
        """Find node with value."""
        current = self.head
        while current:
            if current.value == value:
                return current.value
            current = current.next
        return None
    
    def size(self):
        """Get size of list."""
        return KaynatNumber(self._size)
    
    def to_list(self):
        """Convert to Kaynat list."""
        from kaynat.interpreter.runtime_types import KaynatList
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return KaynatList(result)
