---
title: Queues - FIFO Data Structure
tags: [dsa, queue, fifo, data-structures]
created: 2026-01-28
difficulty: beginner
---

# 14. Queues

[[00_Index|← Back to Index]] | [[13_Stacks|← Previous]]

> **First-In-First-Out - like waiting in line**

---

## 🎯 What is a Queue?

A **queue** is a linear data structure that follows **FIFO** (First-In-First-Out) principle.

**Think of it like:**
- Waiting in line 👥
- Printer queue 🖨️
- Task scheduling ⏰
- BFS traversal 🌳

---

## 📊 Operations & Complexity

| Operation | Time | Description |
|-----------|------|-------------|
| **enqueue(x)** | O(1) | Add to back |
| **dequeue()** | O(1) | Remove from front |
| **front()** | O(1) | View front element |
| **is_empty()** | O(1) | Check if empty |
| **size()** | O(1) | Get size |

---

## 🎨 Visualization

```
Enqueue operations:
───────────────────
enqueue(1)    enqueue(2)    enqueue(3)

Front → [1] ← Back
Front → [1, 2] ← Back
Front → [1, 2, 3] ← Back

Dequeue operations:
───────────────────
dequeue()     dequeue()     dequeue()

Front → [2, 3] ← Back     Returns 1
Front → [3] ← Back        Returns 2
Front → [] ← Back         Returns 3

First in → First out!
```

---

## 💻 Implementation

### Beginner-Friendly Version (Using `deque`)

```python
from collections import deque

queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")

# Peek (front item)
print(queue[0])  # A

# Dequeue
print(queue.popleft())  # A
print(list(queue))      # ['B', 'C']
```

### Using collections.deque (Best)

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add to back - O(1)"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove from front - O(1)"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()
    
    def front(self):
        """View front without removing - O(1)"""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]
    
    def is_empty(self):
        """Check if empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Get size - O(1)"""
        return len(self.items)
    
    def __str__(self):
        return f"Queue({list(self.items)})"

# Usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)          # Queue([1, 2, 3])
print(queue.front())  # 1
print(queue.dequeue())# 1
print(queue.size())   # 2
```

### Using List (Simple but Slower)

```python
class QueueList:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add to back - O(1)"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove from front - O(n) ⚠️ Slow!"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)  # O(n) - shifts all elements!

# Note: pop(0) is O(n) because all elements shift left
# Use deque for O(1) operations!
```

---

## 💡 Practical Applications

### 1. Task Scheduling

```python
class TaskScheduler:
    def __init__(self):
        self.queue = deque()
    
    def add_task(self, task):
        """Add task to queue"""
        self.queue.append(task)
        print(f"Added: {task}")
    
    def process_next(self):
        """Process next task"""
        if self.queue:
            task = self.queue.popleft()
            print(f"Processing: {task}")
            return task
        print("No tasks to process")
        return None
    
    def show_queue(self):
        """Show all pending tasks"""
        print(f"Pending tasks: {list(self.queue)}")

# Usage
scheduler = TaskScheduler()
scheduler.add_task("Send email")
scheduler.add_task("Update database")
scheduler.add_task("Generate report")
scheduler.show_queue()  # [Send email, Update database, Generate report]
scheduler.process_next()  # Processing: Send email
scheduler.show_queue()  # [Update database, Generate report]
```

### 2. BFS (Breadth-First Search)

```python
def bfs_tree(root):
    """Level-order traversal using queue"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Visual:
#       1
#      / \
#     2   3
#    / \
#   4   5
# BFS: [1, 2, 3, 4, 5]
```

### 3. Recent Calls Tracker

```python
class RecentCounter:
    """Track requests in last 3000ms"""
    def __init__(self):
        self.queue = deque()
    
    def ping(self, t):
        """Add new request at time t"""
        self.queue.append(t)
        
        # Remove old requests (> 3000ms ago)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        return len(self.queue)

# Usage
counter = RecentCounter()
print(counter.ping(1))     # 1 request in [1, 3001]
print(counter.ping(100))   # 2 requests
print(counter.ping(3001))  # 3 requests
print(counter.ping(3002))  # 3 requests (1 is old, removed)
```

### 4. Printer Queue

```python
class PrinterQueue:
    def __init__(self):
        self.queue = deque()
    
    def add_job(self, job):
        """Add print job"""
        self.queue.append(job)
        print(f"Added to queue: {job}")
    
    def print_next(self):
        """Print next job"""
        if self.queue:
            job = self.queue.popleft()
            print(f"Printing: {job}")
            return job
        print("Queue empty")
        return None
    
    def jobs_waiting(self):
        """Count waiting jobs"""
        return len(self.queue)

# Usage
printer = PrinterQueue()
printer.add_job("Document1.pdf")
printer.add_job("Photo.jpg")
printer.add_job("Report.docx")
print(f"Jobs waiting: {printer.jobs_waiting()}")  # 3
printer.print_next()  # Prints Document1.pdf first (FIFO)
```

---

## 🔧 Queue Variations

### Circular Queue

```python
class CircularQueue:
    """Fixed-size circular queue"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
    
    def enqueue(self, item):
        if self.size == self.capacity:
            raise OverflowError("Queue is full")
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

# Visual:
# [_, _, _, _]  capacity=4
#  ↑
#  front, rear
# 
# enqueue(1): [1, _, _, _] front=0, rear=1
# enqueue(2): [1, 2, _, _] front=0, rear=2
# dequeue():  [_, 2, _, _] front=1, rear=2, returns 1
```

### Priority Queue

```python
import heapq

class PriorityQueue:
    """Items with higher priority are dequeued first"""
    def __init__(self):
        self.heap = []
    
    def enqueue(self, item, priority):
        """Add item with priority (lower number = higher priority)"""
        heapq.heappush(self.heap, (priority, item))
    
    def dequeue(self):
        """Remove highest priority item"""
        if not self.heap:
            raise IndexError("Queue is empty")
        return heapq.heappop(self.heap)[1]
    
    def is_empty(self):
        return len(self.heap) == 0

# Usage
pq = PriorityQueue()
pq.enqueue("Low priority task", 3)
pq.enqueue("High priority task", 1)
pq.enqueue("Medium priority task", 2)

print(pq.dequeue())  # "High priority task" (priority 1)
print(pq.dequeue())  # "Medium priority task" (priority 2)
print(pq.dequeue())  # "Low priority task" (priority 3)
```

---

## 🎯 Stack vs Queue

| Feature | Stack | Queue |
|---------|-------|-------|
| **Order** | LIFO | FIFO |
| **Add** | Push (top) | Enqueue (back) |
| **Remove** | Pop (top) | Dequeue (front) |
| **Use case** | Undo/Redo | Task scheduling |
| **Example** | Browser back | Print queue |
| **Traversal** | DFS | BFS |

```
Stack (LIFO):         Queue (FIFO):
   ↓ push               enqueue →
[3, 2, 1]             [1, 2, 3]
   ↑ pop               ← dequeue
Last → First          First → First
```

---

## ✅ When to Use Queues

**Perfect for:**
- ✅ Task scheduling
- ✅ BFS traversal
- ✅ Request handling
- ✅ Message queues
- ✅ Print spooling
- ✅ Order processing
- ✅ Streaming buffers

**Not suitable for:**
- ❌ Need LIFO (use stack)
- ❌ Need random access
- ❌ Need to access middle elements

---

## 🎓 Key Takeaways

✅ **FIFO** - First In, First Out  
✅ **O(1)** for enqueue, dequeue  
✅ **Use deque** for O(1) operations  
✅ **Not list.pop(0)** - that's O(n)!  
✅ **BFS uses queue**, DFS uses stack  
✅ **Many variations** - circular, priority

---

## 🚀 You've Completed the Course!

Congratulations! You now understand:
- ✅ Big O notation
- ✅ Arrays and operations
- ✅ 8 sorting algorithms
- ✅ 2 search algorithms
- ✅ Stacks (LIFO)
- ✅ Queues (FIFO)

**Next steps:**
1. Practice on LeetCode/HackerRank
2. Build projects using these structures
3. Learn trees, graphs, and dynamic programming
4. Keep coding! 💪

---

[[00_Index|← Back to Index]] | [[13_Stacks|← Previous]]

*Queue it up! 🎫*
---

## 🎨 Visualization (Optional)

```python
from DSA_Utils.utils import draw_queue

queue = ["A", "B", "C"]
draw_queue(queue)
```
