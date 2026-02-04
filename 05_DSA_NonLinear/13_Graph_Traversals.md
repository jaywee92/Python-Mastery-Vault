---
title: Graph Traversals - BFS & DFS
tags: [dsa, graphs, bfs, dfs, traversal, algorithm]
created: 2026-01-30
difficulty: intermediate
time_complexity: O(V + E)
space_complexity: O(V)
---

# 🔍 Graph Traversals

[[00_Index|← Back to Index]] | [[12_Graphs_II|← Graphs II]] | [[14_Cycle_Detection|Cycle Detection →]]

> **"BFS goes wide, DFS goes deep - both visit every vertex"**

---

## 🎯 Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                 BFS vs DFS COMPARISON                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  BFS (Breadth-First Search)    DFS (Depth-First Search)         │
│  ─────────────────────────     ─────────────────────────        │
│  Uses: QUEUE                   Uses: STACK (or recursion)       │
│  Explores: Level by level      Explores: As deep as possible    │
│  Finds: Shortest path (unw.)   Finds: Any path                  │
│                                                                  │
│       START                          START                       │
│         1                              1                         │
│        /|\                            /|\                        │
│       2 3 4   BFS: 1,2,3,4,5,6,7     2 3 4   DFS: 1,2,5,6,3,7,4 │
│      /|   |                         /|   |                       │
│     5 6   7                        5 6   7                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Breadth-First Search (BFS)

```
┌─────────────────────────────────────────────────────────────────┐
│                    BFS VISUALIZATION                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Start at A, explore all neighbors before going deeper          │
│                                                                  │
│       (A)                Level 0: A                             │
│      / | \                                                       │
│    (B)(C)(D)             Level 1: B, C, D                       │
│    /       \                                                     │
│  (E)       (F)           Level 2: E, F                          │
│                                                                  │
│  Visit Order: A → B → C → D → E → F                             │
│                                                                  │
│  Queue trace:                                                    │
│  [A]       → visit A, add B,C,D                                 │
│  [B,C,D]   → visit B, add E                                     │
│  [C,D,E]   → visit C                                            │
│  [D,E]     → visit D, add F                                     │
│  [E,F]     → visit E                                            │
│  [F]       → visit F                                            │
│  []        → done!                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### ✅ Beginner-Friendly BFS Example

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

g = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}
print(bfs(g, "A"))  # ['A', 'B', 'C', 'D']
```

### BFS Implementation

```python
# ═══════════════════════════════════════════════════════════════
# BREADTH-FIRST SEARCH (BFS)
# ═══════════════════════════════════════════════════════════════
from collections import deque

def bfs(graph, start):
    """
    BFS traversal from start vertex.
    Returns list of vertices in BFS order.
    """
    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# Usage
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A'],
    'D': ['A', 'F'],
    'E': ['B'],
    'F': ['D']
}

print(bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
```

### BFS for Shortest Path (Unweighted)

```python
# ═══════════════════════════════════════════════════════════════
# BFS SHORTEST PATH (Unweighted Graphs)
# ═══════════════════════════════════════════════════════════════

def bfs_shortest_path(graph, start, end):
    """
    Find shortest path from start to end in unweighted graph.
    Returns path as list or None if no path exists.
    """
    if start == end:
        return [start]

    visited = set([start])
    queue = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()

        for neighbor in graph.get(vertex, []):
            if neighbor == end:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found


# Usage
path = bfs_shortest_path(graph, 'A', 'F')
print(path)  # ['A', 'D', 'F']
```

---

## 🌊 Depth-First Search (DFS)

```
┌─────────────────────────────────────────────────────────────────┐
│                    DFS VISUALIZATION                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Start at A, go as deep as possible before backtracking         │
│                                                                  │
│       (A) ←─── start                                            │
│      / | \                                                       │
│    (B)(C)(D)                                                    │
│    /       \                                                     │
│  (E)       (F)                                                  │
│                                                                  │
│  Visit Order (recursive): A → B → E → C → D → F                 │
│                                                                  │
│  Stack trace (iterative):                                        │
│  [A]       → visit A, push D,C,B (reverse order)                │
│  [D,C,B]   → visit B, push E                                    │
│  [D,C,E]   → visit E                                            │
│  [D,C]     → visit C                                            │
│  [D]       → visit D, push F                                    │
│  [F]       → visit F                                            │
│  []        → done!                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### ✅ Beginner-Friendly DFS Example (Recursive)

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    order = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))

    return order

g = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}
print(dfs(g, "A"))  # ['A', 'B', 'D', 'C']
```

### DFS Recursive Implementation

```python
# ═══════════════════════════════════════════════════════════════
# DFS - RECURSIVE VERSION
# ═══════════════════════════════════════════════════════════════

def dfs_recursive(graph, start, visited=None):
    """
    DFS traversal using recursion.
    Returns list of vertices in DFS order.
    """
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


# Usage
print(dfs_recursive(graph, 'A'))  # ['A', 'B', 'E', 'C', 'D', 'F']
```

### DFS Iterative Implementation

```python
# ═══════════════════════════════════════════════════════════════
# DFS - ITERATIVE VERSION (using stack)
# ═══════════════════════════════════════════════════════════════

def dfs_iterative(graph, start):
    """
    DFS traversal using explicit stack.
    Returns list of vertices in DFS order.
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # Add neighbors to stack (reverse for left-to-right order)
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


# Usage
print(dfs_iterative(graph, 'A'))  # ['A', 'B', 'E', 'C', 'D', 'F']
```

### DFS for Path Finding

```python
# ═══════════════════════════════════════════════════════════════
# DFS PATH FINDING
# ═══════════════════════════════════════════════════════════════

def dfs_path(graph, start, end, path=None):
    """
    Find a path from start to end using DFS.
    Returns path as list or None if no path exists.
    """
    if path is None:
        path = []

    path = path + [start]

    if start == end:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, end, path)
            if new_path:
                return new_path

    return None


# Find all paths
def dfs_all_paths(graph, start, end, path=None):
    """Find ALL paths from start to end."""
    if path is None:
        path = []

    path = path + [start]

    if start == end:
        return [path]

    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_paths = dfs_all_paths(graph, neighbor, end, path)
            paths.extend(new_paths)

    return paths


# Usage
print(dfs_path(graph, 'A', 'F'))       # ['A', 'D', 'F']
print(dfs_all_paths(graph, 'A', 'F'))  # [['A', 'D', 'F']]
```

---

## 🆚 BFS vs DFS Comparison

| Aspect | BFS | DFS |
|--------|-----|-----|
| Data Structure | Queue | Stack / Recursion |
| Order | Level by level | Deep first |
| Shortest Path | ✅ Yes (unweighted) | ❌ No |
| Space (tree) | O(width) | O(height) |
| Space (graph) | O(V) | O(V) |
| Complete? | ✅ Yes | ✅ Yes |
| Time | O(V + E) | O(V + E) |

---

## 🎯 When to Use Which?

```
┌─────────────────────────────────────────────────────────────────┐
│                  CHOOSING BFS vs DFS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  USE BFS WHEN:                                                   │
│  • Finding shortest path (unweighted)                           │
│  • Level-order traversal needed                                 │
│  • Solution is close to root/start                              │
│  • Need to explore neighbors first                              │
│                                                                  │
│  USE DFS WHEN:                                                   │
│  • Detecting cycles                                              │
│  • Topological sorting                                          │
│  • Finding connected components                                  │
│  • Maze solving / backtracking                                  │
│  • Solution is deep in the tree/graph                           │
│  • Memory is limited (recursive DFS)                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🌳 Tree Traversal Connection

```python
# BFS on a tree = Level-order traversal
# DFS on a tree = Pre/In/Post-order traversal

#        1
#       / \
#      2   3
#     / \
#    4   5

# BFS: 1, 2, 3, 4, 5 (level order)
# DFS: 1, 2, 4, 5, 3 (pre-order)
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Not marking as visited before adding to queue (BFS)
def bad_bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        v = queue.popleft()
        visited.add(v)  # Too late! May add duplicates
        for n in graph[v]:
            if n not in visited:
                queue.append(n)  # n might be added multiple times!

# ✅ RIGHT: Mark visited when adding to queue
def good_bfs(graph, start):
    visited = set([start])  # Mark start immediately
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if n not in visited:
                visited.add(n)  # Mark before adding
                queue.append(n)

# ❌ WRONG: Infinite loop on cyclic graphs
def bad_dfs(graph, start):
    for neighbor in graph[start]:
        bad_dfs(graph, neighbor)  # No visited check!

# ✅ RIGHT: Track visited vertices
def good_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            good_dfs(graph, neighbor, visited)
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Mark visited early | Mark after processing |
| Use deque for BFS | Use list for BFS (slow popleft) |
| Consider iterative DFS for deep graphs | Risk stack overflow |
| Return early if target found | Process entire graph unnecessarily |

---

## 🎯 Exam Checklist

- [ ] BFS uses Queue, DFS uses Stack
- [ ] BFS: level-by-level, finds shortest path (unweighted)
- [ ] DFS: go deep first, good for cycles/backtracking
- [ ] Both are O(V + E) time, O(V) space
- [ ] Mark visited BEFORE adding to queue/stack
- [ ] DFS can be recursive or iterative

---

[[12_Graphs_II|← Graphs II]] | [[00_Index|Index]] | [[14_Cycle_Detection|Cycle Detection →]]
