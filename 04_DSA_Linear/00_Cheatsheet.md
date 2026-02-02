---
title: Linear Data Structures - Cheatsheet
tags: [dsa, linear, arrays, linked-lists, stacks, queues, cheatsheet]
created: 2026-02-01
---

# 📊 Linear Data Structures - Cheatsheet

---

## 🔢 Arrays

```
┌───┬───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │ 4 │  ← Index
├───┼───┼───┼───┼───┤
│ A │ B │ C │ D │ E │  ← Elements
└───┴───┴───┴───┴───┘
     Contiguous Memory
```

| Operation | Time | Description |
|-----------|------|-------------|
| Access | O(1) | By index |
| Search | O(n) | Linear scan |
| Insert (end) | O(1)* | Amortized |
| Insert (middle) | O(n) | Shift elements |
| Delete | O(n) | Shift elements |

```python
# Python List (Dynamic Array)
arr = [1, 2, 3, 4, 5]
arr[0]           # O(1) access
arr.append(6)    # O(1) amortized
arr.insert(2, x) # O(n)
arr.pop()        # O(1)
arr.remove(x)    # O(n)
```

---

## 🔗 Linked Lists

```
Singly Linked:
┌───┬───┐   ┌───┬───┐   ┌───┬───┐
│ A │ ●─┼──►│ B │ ●─┼──►│ C │ ∅ │
└───┴───┘   └───┴───┘   └───┴───┘
HEAD                     TAIL

Doubly Linked:
┌───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
│ ∅ │ A │ ●─┼──►│◄──┼ B │ ●─┼──►│◄──┼ C │ ∅ │
└───┴───┴───┘   └───┴───┴───┘   └───┴───┴───┘
```

| Operation | Singly | Doubly |
|-----------|--------|--------|
| Access by index | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(n)/O(1)* | O(1) |
| Delete head | O(1) | O(1) |
| Delete tail | O(n) | O(1) |
| Delete by node | O(n) | O(1) |

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  # Singly
        self.prev = None  # Doubly

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
```

---

## 📚 Stacks (LIFO)

```
     ┌───┐
     │ 3 │ ← TOP (push/pop here)
     ├───┤
     │ 2 │
     ├───┤
     │ 1 │
     └───┘
   Last In, First Out
```

| Operation | Time |
|-----------|------|
| Push | O(1) |
| Pop | O(1) |
| Peek/Top | O(1) |
| isEmpty | O(1) |

```python
# Using list
stack = []
stack.append(1)  # Push
stack.pop()      # Pop
stack[-1]        # Peek

# Using collections.deque (faster)
from collections import deque
stack = deque()
stack.append(1)
stack.pop()
```

**Common Use Cases:**
- Function call stack
- Undo/Redo operations
- Expression evaluation
- Balanced parentheses check
- DFS traversal

---

## 🚶 Queues (FIFO)

```
FRONT ──────────────────► BACK
┌───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │
└───┴───┴───┴───┴───┘
  ↑                 ↑
Dequeue          Enqueue
  First In, First Out
```

| Operation | Time |
|-----------|------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Peek | O(1) |
| isEmpty | O(1) |

```python
from collections import deque

queue = deque()
queue.append(1)     # Enqueue
queue.popleft()     # Dequeue
queue[0]            # Peek front

# Priority Queue
import heapq
pq = []
heapq.heappush(pq, 3)
heapq.heappop(pq)   # Returns smallest
```

**Queue Types:**
- Simple Queue (FIFO)
- Double-ended Queue (Deque)
- Priority Queue (Heap)
- Circular Queue

---

## 🔍 Searching Algorithms

| Algorithm | Best | Average | Worst | Notes |
|-----------|------|---------|-------|-------|
| Linear Search | O(1) | O(n) | O(n) | Unsorted data |
| Binary Search | O(1) | O(log n) | O(log n) | **Sorted only!** |

```python
# Linear Search
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## 📊 Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |

```python
# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

---

## ⏱️ Time Complexity Summary

```
                   FAST
                    ↑
   O(1)      ━━━━━━━━━━━━━━━
   O(log n)  ━━━━━━━━━━━
   O(n)      ━━━━━━━
   O(n log n)━━━━
   O(n²)     ━━
   O(2ⁿ)     ━
                    ↓
                   SLOW
```

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Array access |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort |
| O(n²) | Quadratic | Bubble sort |
| O(2ⁿ) | Exponential | Fibonacci naive |

---

## 🎯 Quick Tips

| Structure | Best For |
|-----------|----------|
| Array | Random access, cache-friendly |
| Linked List | Frequent insertions/deletions |
| Stack | LIFO operations, backtracking |
| Queue | FIFO operations, BFS |
| Deque | Both ends operations |

**Remember:**
- Arrays: Fast access, slow insert/delete
- Linked Lists: Slow access, fast insert/delete
- Binary Search: Only works on SORTED data!
- Stable sort: Equal elements keep order

---

[[00_Index|← Back to Index]]
