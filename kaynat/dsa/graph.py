"""Kaynat Graph - Stub implementation."""

from collections import defaultdict, deque


class Graph:
    """Graph data structure."""
    
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.weights = {}
    
    def add_node(self, node):
        """Add node to graph."""
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []
    
    def add_edge(self, from_node, to_node, weight=1):
        """Add edge between nodes."""
        self.adjacency_list[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight
    
    def bfs(self, start):
        """Breadth-first search."""
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.adjacency_list[node])
        
        return result
    
    def dfs(self, start):
        """Depth-first search."""
        visited = set()
        result = []
        
        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adjacency_list[node]:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result
