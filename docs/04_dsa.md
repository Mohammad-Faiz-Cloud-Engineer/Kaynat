# Data Structures and Algorithms in Kaynat

## Status: PLANNED FOR FUTURE RELEASE

This document describes the planned DSA features for Kaynat. These features are not yet implemented in version 1.0.0.

---

## Overview

Kaynat will include a comprehensive DSA library with:
- Stack, Queue, Linked List
- Binary Search Tree, Graph, Heap
- Hash Map, Trie
- Sorting algorithms
- Searching algorithms
- Graph algorithms

---

## Stack

### Operations

```kaynat
create a stack called history.

push page one onto history.
push page two onto history.
push page three onto history.

pop from history and store as last page.
say last page.

peek at history and store as top page.
say top page.

check if history is empty.
find the size of history.
```

### Use Cases
- Undo/redo functionality
- Expression evaluation
- Backtracking algorithms
- Browser history

---

## Queue

### Operations

```kaynat
create a queue called requests.

enqueue task one into requests.
enqueue task two into requests.
enqueue task three into requests.

dequeue from requests and store as next task.
say next task.

peek at the front of requests.
check if requests is empty.
find the size of requests.
```

### Use Cases
- Task scheduling
- Breadth-first search
- Print queue
- Message queues

---

## Linked List

### Operations

```kaynat
create a linked list called chain.

add node with value 10 to chain.
add node with value 20 to chain.
add node with value 30 to chain.

insert node with value 15 at position 1 in chain.
remove node with value 10 from chain.

find node with value 20 in chain.
find the length of chain.

convert chain to list and store as values.
reverse chain.
```

### Use Cases
- Dynamic memory allocation
- Implementation of other data structures
- Undo functionality
- Music playlists

---

## Binary Search Tree

### Operations

```kaynat
create a binary search tree called bst.

insert 50 into bst.
insert 30 into bst.
insert 70 into bst.
insert 20 into bst.
insert 40 into bst.

search for 30 in bst and store as found.

traverse bst inorder and store as sorted values.
traverse bst preorder and store as preorder values.
traverse bst postorder and store as postorder values.

find the height of bst.
find the minimum in bst.
find the maximum in bst.

delete 30 from bst.
```

### Use Cases
- Sorted data storage
- Fast search operations
- Range queries
- Database indexing

---

## Graph

### Operations

```kaynat
create a graph called network.

add node city a to network.
add node city b to network.
add node city c to network.

add edge from city a to city b with weight 10 in network.
add edge from city b to city c with weight 20 in network.
add edge from city a to city c with weight 30 in network.

find the shortest path from city a to city c in network using dijkstra.

traverse network from city a using breadth first and store as visited.
traverse network from city a using depth first and store as visited.

check if network has a cycle.
find all connected components in network.
```

### Use Cases
- Social networks
- Maps and navigation
- Network routing
- Dependency resolution

---

## Heap

### Min Heap

```kaynat
create a min heap called task heap.

insert task with priority 3 into task heap.
insert task with priority 1 into task heap.
insert task with priority 5 into task heap.

extract minimum from task heap and store as urgent task.
peek at minimum in task heap.
find the size of task heap.
```

### Max Heap

```kaynat
create a max heap called score heap.

insert 42 into score heap.
insert 17 into score heap.
insert 99 into score heap.

extract maximum from score heap and store as top score.
```

### Use Cases
- Priority queues
- Heap sort
- Finding k largest/smallest elements
- Median maintenance

---

## Hash Map

### Operations

```kaynat
create a hash map called index.

put key hello with value greeting into index.
put key goodbye with value farewell into index.

get key hello from index and store as word type.
remove key hello from index.

check if key hello exists in index.
find the load factor of index.
```

### Use Cases
- Fast lookups
- Caching
- Counting frequencies
- Implementing sets

---

## Trie

### Operations

```kaynat
create a trie called dictionary.

insert word hello into dictionary.
insert word help into dictionary.
insert word world into dictionary.

search for word hello in dictionary and store as found.
find all words starting with hel in dictionary and store as suggestions.

delete word help from dictionary.
```

### Use Cases
- Autocomplete
- Spell checking
- IP routing
- Dictionary implementation

---

## Sorting Algorithms

### Bubble Sort

```kaynat
set numbers to a list containing 64, 34, 25, 12, 22, 11, 90.
sort numbers using bubble sort and store as sorted.
say sorted.
```

### Merge Sort

```kaynat
set numbers to a list containing 38, 27, 43, 3, 9, 82, 10.
sort numbers using merge sort and store as sorted.
say sorted.
```

### Quick Sort

```kaynat
set numbers to a list containing 10, 7, 8, 9, 1, 5.
sort numbers using quick sort and store as sorted.
say sorted.
```

### Other Sorting Algorithms

- Insertion Sort
- Selection Sort
- Heap Sort
- Radix Sort
- Counting Sort

### Time Complexities

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

---

## Searching Algorithms

### Linear Search

```kaynat
set numbers to a list containing 10, 20, 30, 40, 50.
search for 30 in numbers using linear search and store as index.
say Found at index, index.
```

### Binary Search

```kaynat
set sorted numbers to a list containing 10, 20, 30, 40, 50, 60, 70.
search for 40 in sorted numbers using binary search and store as index.
say Found at index, index.
```

### Pattern Matching

```kaynat
set text to hello world hello.
set pattern to hello.
search for pattern in text using knuth morris pratt and store as positions.
say Found at positions, positions.
```

---

## Graph Algorithms

### Dijkstra's Algorithm

```kaynat
find shortest path from a to e in graph using dijkstra and store as path.
say Shortest path is, path.
```

### Bellman-Ford Algorithm

```kaynat
find shortest path from a to e in graph using bellman ford and store as path.
```

### Minimum Spanning Tree

```kaynat
find minimum spanning tree of graph using kruskal and store as tree.
find minimum spanning tree of graph using prim and store as tree.
```

### Topological Sort

```kaynat
perform topological sort on graph and store as order.
say Order is, order.
```

### Strongly Connected Components

```kaynat
find all strongly connected components in graph using kosaraju.
```

---

## Complete Example: Graph Shortest Path

```kaynat
begin program.

create a graph called city map.

add node home to city map.
add node work to city map.
add node gym to city map.
add node store to city map.

add edge from home to work with weight 5 in city map.
add edge from home to gym with weight 3 in city map.
add edge from gym to work with weight 2 in city map.
add edge from work to store with weight 4 in city map.
add edge from gym to store with weight 6 in city map.

find the shortest path from home to store in city map using dijkstra and store as path.

say Shortest path from home to store.
for each node in path.
    say node.
end.

end program.
```

---

## Implementation Status

**Current Status:** NOT IMPLEMENTED

**Planned for:** Version 2.0.0 - 3.0.0

**Required Components:**
- Data structure implementations
- Algorithm implementations
- Memory management
- Performance optimization
- Comprehensive testing

---

## Learning Path

1. **Start with:** Stack and Queue (simplest)
2. **Then learn:** Linked List
3. **Move to:** Trees (BST)
4. **Advanced:** Graphs and Heaps
5. **Master:** Sorting and searching algorithms

---

*This documentation describes planned features. Check PROJECT_STATUS.md for current implementation status.*
