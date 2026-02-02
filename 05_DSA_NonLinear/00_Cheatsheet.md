---
title: Non-Linear Data Structures - Cheatsheet
tags: [dsa, nonlinear, hash, trees, graphs, cheatsheet]
created: 2026-02-01
---

# 🌳 Non-Linear Data Structures - Cheatsheet

---

## #️⃣ Hash Tables

```
Key → Hash Function → Index → Value

┌─────┬───────────┐
│  0  │           │
├─────┼───────────┤
│  1  │ "Alice"   │ ← hash("name") = 1
├─────┼───────────┤
│  2  │           │
├─────┼───────────┤
│  3  │ 25        │ ← hash("age") = 3
└─────┴───────────┘
```

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Search | O(1) | O(n) |

```python
# Python dict (hash table)
d = {"name": "Alice", "age": 25}
d["city"] = "Berlin"  # Insert O(1)
del d["age"]          # Delete O(1)
"name" in d           # Search O(1)

# Hash Set
s = {1, 2, 3}
s.add(4)              # O(1)
s.remove(1)           # O(1)
3 in s                # O(1)

# Collision handling:
# 1. Chaining (linked lists)
# 2. Open Addressing (probing)
```

---

## 🌲 Binary Trees

```
        ┌───┐
        │ A │         ← Root
        └─┬─┘
       ┌──┴──┐
     ┌─┴─┐ ┌─┴─┐
     │ B │ │ C │      ← Internal nodes
     └─┬─┘ └─┬─┘
    ┌──┴─┐  ┌┴──┐
  ┌─┴─┐┌┴┐┌┴┐┌─┴─┐
  │ D ││E││F││ G │    ← Leaves
  └───┘└─┘└─┘└───┘
```

**Tree Terms:**
- **Root**: Top node
- **Leaf**: Node with no children
- **Height**: Longest path from root to leaf
- **Depth**: Distance from root
- **Subtree**: Tree formed by a node and descendants

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

---

## 🔄 Tree Traversals

```
         1
       /   \
      2     3
     / \
    4   5

Pre-order  (Root-L-R): 1, 2, 4, 5, 3
In-order   (L-Root-R): 4, 2, 5, 1, 3
Post-order (L-R-Root): 4, 5, 2, 3, 1
Level-order (BFS):     1, 2, 3, 4, 5
```

```python
# Pre-order (Root → Left → Right)
def preorder(node):
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)

# In-order (Left → Root → Right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

# Post-order (Left → Right → Root)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)

# Level-order (BFS)
from collections import deque
def levelorder(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

---

## 🔍 Binary Search Tree (BST)

```
BST Property:
left < root < right

         8
       /   \
      3     10
     / \      \
    1   6      14
       / \    /
      4   7  13
```

| Operation | Average | Worst (unbalanced) |
|-----------|---------|-------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

```python
def search_bst(root, target):
    if not root or root.val == target:
        return root
    if target < root.val:
        return search_bst(root.left, target)
    return search_bst(root.right, target)

def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root
```

---

## ⚖️ AVL Trees

```
Self-balancing BST
Balance Factor = height(left) - height(right)
Must be: -1, 0, or 1

Rotations:
LL → Right Rotate
RR → Left Rotate
LR → Left-Right Rotate
RL → Right-Left Rotate
```

| Operation | Time |
|-----------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

---

## 🕸️ Graphs

```
Undirected:          Directed:
  A───B               A───►B
  │   │               │    │
  │   │               ▼    ▼
  C───D               C───►D
```

**Graph Representations:**

```python
# Adjacency List (more efficient)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Adjacency Matrix
#     A  B  C  D
# A [[0, 1, 1, 0],
# B  [1, 0, 0, 1],
# C  [1, 0, 0, 1],
# D  [0, 1, 1, 0]]
```

---

## 🔍 Graph Traversals

```python
# BFS (Breadth-First Search)
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS (Depth-First Search)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

| Algorithm | Space | Use Case |
|-----------|-------|----------|
| BFS | O(V) | Shortest path (unweighted) |
| DFS | O(V) | Cycle detection, topological sort |

---

## 🛤️ Shortest Path Algorithms

| Algorithm | Time | Use Case |
|-----------|------|----------|
| Dijkstra | O((V+E) log V) | Non-negative weights |
| Bellman-Ford | O(V·E) | Negative weights, detect negative cycles |

```python
# Dijkstra's Algorithm
import heapq

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist
```

---

## 🔄 Cycle Detection

```python
# Undirected Graph (DFS)
def has_cycle_undirected(graph, node, visited, parent):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle_undirected(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True
    return False

# Directed Graph (colors: white→gray→black)
def has_cycle_directed(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph}

    def dfs(node):
        color[node] = GRAY
        for neighbor in graph[node]:
            if color[neighbor] == GRAY:
                return True  # Back edge → cycle
            if color[neighbor] == WHITE:
                if dfs(neighbor):
                    return True
        color[node] = BLACK
        return False

    return any(dfs(v) for v in graph if color[v] == WHITE)
```

---

## ⏱️ Time Complexity Summary

| Structure | Search | Insert | Delete |
|-----------|--------|--------|--------|
| Hash Table | O(1)* | O(1)* | O(1)* |
| BST (balanced) | O(log n) | O(log n) | O(log n) |
| BST (unbalanced) | O(n) | O(n) | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) |

| Algorithm | Time |
|-----------|------|
| BFS/DFS | O(V + E) |
| Dijkstra | O((V+E) log V) |
| Bellman-Ford | O(V · E) |

---

## 🎯 Quick Tips

| Structure | Best For |
|-----------|----------|
| Hash Table | Fast lookup, unique keys |
| Hash Set | Unique values, membership |
| BST | Ordered data, range queries |
| AVL | Balanced BST, guaranteed O(log n) |
| Graph | Relationships, networks |

**Remember:**
- Hash: O(1) average, O(n) worst
- BST: Only balanced gives O(log n)
- BFS: Shortest path (unweighted)
- DFS: Cycle detection, topological sort
- Dijkstra: No negative weights!
- Bellman-Ford: Handles negative weights

---

[[00_Index|← Back to Index]]
