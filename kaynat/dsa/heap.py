"""Kaynat Heap - Min and Max Heap implementations."""

import heapq


class MinHeap:
    """Min Heap data structure."""
    
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        """Insert value into heap."""
        heapq.heappush(self.heap, value)
    
    def extract_min(self):
        """Extract minimum value."""
        if not self.heap:
            raise RuntimeError("Heap is empty")
        return heapq.heappop(self.heap)
    
    def peek(self):
        """Peek at minimum value."""
        if not self.heap:
            raise RuntimeError("Heap is empty")
        return self.heap[0]
    
    def size(self):
        """Get size of heap."""
        return len(self.heap)


class MaxHeap:
    """Max Heap data structure."""
    
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        """Insert value into heap."""
        heapq.heappush(self.heap, -value)
    
    def extract_max(self):
        """Extract maximum value."""
        if not self.heap:
            raise RuntimeError("Heap is empty")
        return -heapq.heappop(self.heap)
    
    def peek(self):
        """Peek at maximum value."""
        if not self.heap:
            raise RuntimeError("Heap is empty")
        return -self.heap[0]
    
    def size(self):
        """Get size of heap."""
        return len(self.heap)
