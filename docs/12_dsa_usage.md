# Data Structures & Algorithms Usage Guide

## Practical Guide to Using DSA in Kaynat

**Status:** Planned for v3.0.0 - Syntax designed, implementation pending

---

## Overview

Kaynat provides built-in data structures and algorithms:

**Data Structures:**
- Stack (LIFO)
- Queue (FIFO)
- Linked List
- Binary Search Tree
- Graph
- Heap (Min/Max)
- Hash Map
- Trie

**Algorithms:**
- Sorting (bubble, merge, quick, insertion, selection)
- Searching (linear, binary, jump)
- Graph algorithms (BFS, DFS)

---

## Stack (Last In, First Out)

### Basic Operations

```kaynat
use data structures.

note. Create a stack.
create a stack called my stack.

note. Push elements.
push 10 onto my stack.
push 20 onto my stack.
push 30 onto my stack.

say Stack created with 3 elements.
```

### Pop and Peek

```kaynat
use data structures.

create a stack called my stack.
push 10 onto my stack.
push 20 onto my stack.
push 30 onto my stack.

note. Pop removes and returns top element.
pop from my stack and store as top.
say Popped, top.

note. Peek returns top without removing.
peek at my stack and store as next.
say Next element is, next.
```

### Stack Information

```kaynat
use data structures.

create a stack called my stack.
push 10 onto my stack.
push 20 onto my stack.

if my stack is empty then.
    say Stack is empty.
otherwise.
    say Stack has elements.
end.

get size of my stack and store as size.
say Stack size is, size.

convert my stack to list and store as items.
say Stack contents, items.
```

### Practical Example: Undo System

```kaynat
use data structures.

create a stack called undo stack.

note. User actions.
push action 1 onto undo stack.
push action 2 onto undo stack.
push action 3 onto undo stack.

say Performing undo.
pop from undo stack and store as last action.
say Undoing, last action.
```

---

## Queue (First In, First Out)

### Basic Operations

```kaynat
use data structures.

note. Create a queue.
create a queue called my queue.

note. Enqueue elements.
enqueue 10 into my queue.
enqueue 20 into my queue.
enqueue 30 into my queue.

say Queue created with 3 elements.
```

### Dequeue and Peek

```kaynat
use data structures.

create a queue called my queue.
enqueue 10 into my queue.
enqueue 20 into my queue.
enqueue 30 into my queue.

note. Dequeue removes and returns first element.
dequeue from my queue and store as first.
say Dequeued, first.

note. Peek returns first without removing.
peek at my queue and store as next.
say Next element is, next.
```

---

## Linked List

### Basic Operations

```kaynat
use data structures.

create a linked list called my list.

note. Append to end.
append 10 to my list.
append 20 to my list.
append 30 to my list.

note. Prepend to beginning.
prepend 5 to my list.

note. Delete element.
delete 20 from my list.

note. Find element.
find 30 in my list and store as found.
if found is true then.
    say Found 30 in list.
end.

note. Get size.
get size of my list and store as size.
say List size is, size.
```

---

## Binary Search Tree

### Basic Operations

```kaynat
use data structures.

create a binary search tree called my tree.

note. Insert elements.
insert 50 into my tree.
insert 30 into my tree.
insert 70 into my tree.
insert 20 into my tree.
insert 40 into my tree.

note. Search for element.
search for 30 in my tree and store as found.
if found is true then.
    say Found 30 in tree.
end.
```

---

## Sorting Algorithms

### Bubble Sort

```kaynat
use algorithms.

set numbers to a list containing 64, 34, 25, 12, 22, 11, 90.

bubble sort numbers.
say Sorted, numbers.
```

### Quick Sort

```kaynat
use algorithms.

set numbers to a list containing 64, 34, 25, 12, 22, 11, 90.

quick sort numbers.
say Sorted, numbers.
```

### Merge Sort

```kaynat
use algorithms.

set numbers to a list containing 64, 34, 25, 12, 22, 11, 90.

merge sort numbers.
say Sorted, numbers.
```

---

## Searching Algorithms

### Linear Search

```kaynat
use algorithms.

set numbers to a list containing 10, 20, 30, 40, 50.

linear search for 30 in numbers and store as index.
if index is greater than minus 1 then.
    say Found at index, index.
end.
```

### Binary Search

```kaynat
use algorithms.

note. List must be sorted.
set numbers to a list containing 10, 20, 30, 40, 50.

binary search for 30 in numbers and store as index.
if index is greater than minus 1 then.
    say Found at index, index.
end.
```

---

## Complete Examples

### Example 1: Task Queue System

```kaynat
use data structures.

create a queue called task queue.

note. Add tasks.
enqueue task 1 into task queue.
enqueue task 2 into task queue.
enqueue task 3 into task queue.

say Processing tasks.

repeat 3 times.
    dequeue from task queue and store as task.
    say Processing, task.
end.
```

### Example 2: Browser History

```kaynat
use data structures.

create a stack called history.

note. Visit pages.
push page 1 onto history.
push page 2 onto history.
push page 3 onto history.

say Going back.
pop from history and store as current page.
say Left, current page.

peek at history and store as previous page.
say Now on, previous page.
```

### Example 3: Sorting Numbers

```kaynat
use algorithms.

set scores to a list containing 85, 92, 78, 95, 88, 76, 90.

say Original scores, scores.

quick sort scores.

say Sorted scores, scores.

get element at position 0 from scores and store as lowest.
get element at position 6 from scores and store as highest.

say Lowest score, lowest.
say Highest score, highest.
```

---

## Implementation Status

**Current Status:** NOT IMPLEMENTED

All data structures and algorithms are designed but not yet implemented.

**Planned for:** Version 3.0.0

---

*This guide describes planned features for Kaynat v3.0.0.*

