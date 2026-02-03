---
title: Cycle Detection
tags: [dsa, graphs, cycle, dfs, algorithm]
created: 2026-01-30
difficulty: intermediate
time_complexity: O(V + E)
---

# 🔄 Cycle Detection

[[00_Index|← Back to Index]] | [[13_Graph_Traversals|← Traversals]] | [[15_Shortest_Path|Shortest Path →]]

> **"Finding cycles: essential for deadlock detection and dependency validation"**

---

## 🎯 What is a Cycle?

```
┌─────────────────────────────────────────────────────────────────┐
│                    CYCLE DEFINITION                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A CYCLE is a path that starts and ends at the same vertex      │
│                                                                  │
│  UNDIRECTED GRAPH:           DIRECTED GRAPH:                    │
│                                                                  │
│      A ─── B                     A ──→ B                        │
│      │     │                     ↑     │                        │
│      │     │   ← Cycle!          │     ↓   ← Cycle!             │
│      C ─── D     A-B-D-C-A       D ←── C     A→B→C→D→A          │
│                                                                  │
│  NO CYCLE:                   NO CYCLE:                          │
│      A ─── B                     A ──→ B                        │
│            │                           │                        │
│            │                           ↓                        │
│      C ─── D                     C ──→ D                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔵 Cycle Detection in Undirected Graphs

### Using DFS with Parent Tracking

```python
# ═══════════════════════════════════════════════════════════════
# CYCLE DETECTION - UNDIRECTED GRAPH (DFS)
# ═══════════════════════════════════════════════════════════════

def has_cycle_undirected(graph):
    """
    Detect cycle in undirected graph using DFS.
    Key insight: If we reach a visited node that isn't our parent,
    we found a cycle!
    """
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # Found visited node that's not parent = cycle!
                return True

        return False

    # Check all components (graph might be disconnected)
    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True

    return False


# Usage
graph_with_cycle = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],  # C-D creates cycle A-B-D-C-A
    'D': ['B', 'C']
}

graph_no_cycle = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C']
}

print(has_cycle_undirected(graph_with_cycle))  # True
print(has_cycle_undirected(graph_no_cycle))    # False
```

### Using Union-Find

```python
# ═══════════════════════════════════════════════════════════════
# CYCLE DETECTION - UNION-FIND APPROACH
# ═══════════════════════════════════════════════════════════════

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already in same set = cycle!

        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


def has_cycle_union_find(edges):
    """
    Detect cycle using Union-Find.
    edges: list of (u, v) tuples
    """
    uf = UnionFind()

    for u, v in edges:
        if not uf.union(u, v):
            return True  # u and v already connected = cycle!

    return False


# Usage
edges_with_cycle = [('A', 'B'), ('B', 'D'), ('A', 'C'), ('C', 'D')]
edges_no_cycle = [('A', 'B'), ('A', 'C'), ('C', 'D')]

print(has_cycle_union_find(edges_with_cycle))  # True
print(has_cycle_union_find(edges_no_cycle))    # False
```

---

## 🔴 Cycle Detection in Directed Graphs

### Using DFS with Three Colors

```
┌─────────────────────────────────────────────────────────────────┐
│              THREE-COLOR DFS FOR DIRECTED GRAPHS                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  WHITE (0): Not visited yet                                     │
│  GRAY  (1): Currently being processed (in recursion stack)      │
│  BLACK (2): Completely processed                                │
│                                                                  │
│  CYCLE EXISTS if we encounter a GRAY node!                      │
│  (means we found a back edge to ancestor in current path)       │
│                                                                  │
│      A ──→ B ──→ C                                              │
│      ↑           │                                              │
│      └───────────┘                                              │
│                                                                  │
│  Processing A (gray) → B (gray) → C (gray) → A (gray!)          │
│  Found gray node = CYCLE!                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# CYCLE DETECTION - DIRECTED GRAPH (THREE COLORS)
# ═══════════════════════════════════════════════════════════════

WHITE, GRAY, BLACK = 0, 1, 2

def has_cycle_directed(graph):
    """
    Detect cycle in directed graph using three-color DFS.
    """
    color = {v: WHITE for v in graph}

    def dfs(node):
        color[node] = GRAY  # Start processing

        for neighbor in graph.get(node, []):
            if color.get(neighbor, WHITE) == GRAY:
                return True  # Back edge to ancestor = cycle!
            if color.get(neighbor, WHITE) == WHITE:
                if dfs(neighbor):
                    return True

        color[node] = BLACK  # Done processing
        return False

    for vertex in graph:
        if color[vertex] == WHITE:
            if dfs(vertex):
                return True

    return False


# Usage
digraph_with_cycle = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']  # Cycle: A → B → C → A
}

digraph_no_cycle = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

print(has_cycle_directed(digraph_with_cycle))  # True
print(has_cycle_directed(digraph_no_cycle))    # False
```

### Using Recursion Stack (Alternative)

```python
# ═══════════════════════════════════════════════════════════════
# CYCLE DETECTION - RECURSION STACK METHOD
# ═══════════════════════════════════════════════════════════════

def has_cycle_rec_stack(graph):
    """
    Detect cycle using visited set and recursion stack.
    """
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True  # Cycle found!

        rec_stack.remove(node)
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex):
                return True

    return False
```

---

## 🔍 Finding the Actual Cycle

```python
# ═══════════════════════════════════════════════════════════════
# FIND AND RETURN THE CYCLE PATH
# ═══════════════════════════════════════════════════════════════

def find_cycle_directed(graph):
    """
    Find and return a cycle in directed graph, or None if no cycle.
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph}
    parent = {}

    def dfs(node):
        color[node] = GRAY

        for neighbor in graph.get(node, []):
            if color.get(neighbor, WHITE) == GRAY:
                # Found cycle! Reconstruct it
                cycle = [neighbor, node]
                current = node
                while parent.get(current) != neighbor:
                    current = parent[current]
                    cycle.append(current)
                cycle.append(neighbor)
                return cycle[::-1]

            if color.get(neighbor, WHITE) == WHITE:
                parent[neighbor] = node
                result = dfs(neighbor)
                if result:
                    return result

        color[node] = BLACK
        return None

    for vertex in graph:
        if color[vertex] == WHITE:
            cycle = dfs(vertex)
            if cycle:
                return cycle

    return None


# Usage
digraph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D', 'A'],
    'D': []
}

cycle = find_cycle_directed(digraph)
print(cycle)  # ['A', 'B', 'C', 'A']
```

---

## 📊 Complexity Comparison

| Method | Graph Type | Time | Space |
|--------|------------|------|-------|
| DFS + Parent | Undirected | O(V+E) | O(V) |
| Union-Find | Undirected | O(E·α(V)) | O(V) |
| Three-Color DFS | Directed | O(V+E) | O(V) |
| Recursion Stack | Directed | O(V+E) | O(V) |

*α(V) is inverse Ackermann, effectively O(1)*

---

## 🎯 Use Cases

```
┌─────────────────────────────────────────────────────────────────┐
│              CYCLE DETECTION APPLICATIONS                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. DEADLOCK DETECTION                                          │
│     - Resource allocation graphs                                │
│     - Cycle = deadlock!                                         │
│                                                                  │
│  2. DEPENDENCY MANAGEMENT                                       │
│     - Package dependencies                                      │
│     - Build systems                                             │
│     - Cycle = invalid dependencies                              │
│                                                                  │
│  3. COURSE PREREQUISITES                                        │
│     - Cycle = impossible schedule                               │
│                                                                  │
│  4. SPREADSHEET FORMULAS                                        │
│     - Circular reference detection                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Using same algorithm for directed/undirected
# Parent tracking only works for UNDIRECTED graphs
# Three-color is needed for DIRECTED graphs

# ❌ WRONG: Not handling disconnected components
def bad_cycle_check(graph, start):
    # Only checks component containing 'start'!
    pass

# ✅ RIGHT: Check all components
def good_cycle_check(graph):
    visited = set()
    for vertex in graph:
        if vertex not in visited:
            if has_cycle_from(vertex, visited):
                return True
    return False
```

---

## 🎯 Exam Checklist

- [ ] Undirected: DFS + parent tracking
- [ ] Undirected: Union-Find (if edges given)
- [ ] Directed: Three-color DFS (WHITE/GRAY/BLACK)
- [ ] GRAY node = currently processing = back edge = cycle
- [ ] Time: O(V + E), Space: O(V)
- [ ] Check ALL components for disconnected graphs

---

[[13_Graph_Traversals|← Traversals]] | [[00_Index|Index]] | [[15_Shortest_Path|Shortest Path →]]
---

## 🎨 Visualization (Optional)

```python
import sys
from pathlib import Path

# Add vault root to sys.path (Obsidian runner)
# Tries current dir, parent dirs, then a known vault path fallback.
added = False
for p in [Path.cwd(), *Path.cwd().parents]:
    if (p / "DSA_Utils").exists():
        sys.path.append(str(p))
        added = True
        break

if not added:
    fallback = Path("/Users/jochenwahl/Library/CloudStorage/OneDrive-Persönlich/z99_Obsidian_Vault/Codex_Coding")
    if fallback.exists():
        sys.path.append(str(fallback))

from DSA_Utils.utils import draw_graph

cycle_graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"],
}

draw_graph(cycle_graph, title="Cycle Graph")
```
