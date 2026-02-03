---
title: Graphs I - Basics
tags: [dsa, graphs, adjacency-matrix, adjacency-list, data-structure]
created: 2026-01-30
difficulty: intermediate
---

# 🕸️ Graphs I - Basics

[[00_Index|← Back to Index]] | [[10_AVL_Trees|← AVL Trees]] | [[12_Graphs_II|Graphs II →]]

> **"Graphs are everywhere: social networks, maps, the internet itself"**

---

## 🎯 What is a Graph?

```
┌─────────────────────────────────────────────────────────────────┐
│                    GRAPH DEFINITION                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A Graph G = (V, E) consists of:                                │
│    • V = set of VERTICES (nodes)                                │
│    • E = set of EDGES (connections)                             │
│                                                                  │
│  Example:                                                        │
│       (A)───────(B)                                             │
│        │ \     / │                                              │
│        │  \   /  │        V = {A, B, C, D}                      │
│        │   \ /   │        E = {(A,B), (A,C), (A,D),             │
│        │    X    │             (B,C), (B,D)}                    │
│        │   / \   │                                              │
│        │  /   \  │                                              │
│       (C)───────(D)                                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✅ Beginner-Friendly Python Example (Adjacency List)

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}

print(graph["A"])  # ['B', 'C']
```

Adjacency lists are the most common and beginner-friendly way to store graphs in Python.

---

## 📚 Graph Terminology

```
┌─────────────────────────────────────────────────────────────────┐
│                    KEY TERMS                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  VERTEX (Node): A point in the graph                            │
│  EDGE: Connection between two vertices                          │
│                                                                  │
│  DEGREE: Number of edges connected to a vertex                  │
│    • In-degree: incoming edges (directed)                       │
│    • Out-degree: outgoing edges (directed)                      │
│                                                                  │
│  PATH: Sequence of vertices connected by edges                  │
│    A → B → C is a path of length 2                              │
│                                                                  │
│  CYCLE: Path that starts and ends at same vertex                │
│    A → B → C → A is a cycle                                     │
│                                                                  │
│  CONNECTED: Path exists between every pair of vertices          │
│                                                                  │
│  ADJACENT: Two vertices connected by an edge                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Directed vs Undirected

```
┌─────────────────────────────────────────────────────────────────┐
│              UNDIRECTED vs DIRECTED GRAPHS                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  UNDIRECTED:                    DIRECTED (Digraph):             │
│  Edges have no direction        Edges have direction (arrows)   │
│                                                                  │
│       (A)───(B)                      (A)───→(B)                 │
│        │     │                        │      ↓                  │
│        │     │                        ↓      │                  │
│       (C)───(D)                      (C)←───(D)                 │
│                                                                  │
│  Edge (A,B) = Edge (B,A)        Edge A→B ≠ Edge B→A            │
│                                                                  │
│  Examples:                      Examples:                       │
│  • Facebook friends             • Twitter followers             │
│  • Road networks (2-way)        • Web page links                │
│  • Electrical circuits          • Prerequisites                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Graph Representations

### 1. Adjacency Matrix

```python
# ═══════════════════════════════════════════════════════════════
# ADJACENCY MATRIX REPRESENTATION
# ═══════════════════════════════════════════════════════════════

#     A  B  C  D
# A [ 0  1  1  1 ]     1 = edge exists
# B [ 1  0  1  1 ]     0 = no edge
# C [ 1  1  0  0 ]
# D [ 1  1  0  0 ]

class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices = {}  # name → index mapping
        self.index = 0

    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = self.index
            self.index += 1

    def add_edge(self, v1, v2, directed=False):
        i, j = self.vertices[v1], self.vertices[v2]
        self.matrix[i][j] = 1
        if not directed:
            self.matrix[j][i] = 1

    def has_edge(self, v1, v2):
        i, j = self.vertices[v1], self.vertices[v2]
        return self.matrix[i][j] == 1

    def get_neighbors(self, v):
        i = self.vertices[v]
        neighbors = []
        for name, j in self.vertices.items():
            if self.matrix[i][j] == 1:
                neighbors.append(name)
        return neighbors

    def display(self):
        names = list(self.vertices.keys())
        print("   ", "  ".join(names))
        for name in names:
            i = self.vertices[name]
            row = [str(self.matrix[i][j]) for j in range(len(names))]
            print(f"{name}  [{', '.join(row)}]")


# Usage
g = GraphMatrix(4)
for v in ['A', 'B', 'C', 'D']:
    g.add_vertex(v)

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

g.display()
print(g.get_neighbors('A'))  # ['B', 'C']
```

### 2. Adjacency List

```python
# ═══════════════════════════════════════════════════════════════
# ADJACENCY LIST REPRESENTATION (Most Common!)
# ═══════════════════════════════════════════════════════════════

# A: [B, C, D]
# B: [A, C, D]
# C: [A, B]
# D: [A, B]

class GraphList:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)

        self.adj_list[v1].append(v2)
        if not self.directed:
            self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
        if not self.directed:
            if v2 in self.adj_list and v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)

    def has_edge(self, v1, v2):
        return v1 in self.adj_list and v2 in self.adj_list[v1]

    def get_neighbors(self, v):
        return self.adj_list.get(v, [])

    def get_vertices(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges = []
        seen = set()
        for v1 in self.adj_list:
            for v2 in self.adj_list[v1]:
                edge = (min(v1, v2), max(v1, v2)) if not self.directed else (v1, v2)
                if edge not in seen:
                    edges.append(edge)
                    seen.add(edge)
        return edges

    def __str__(self):
        result = []
        for v in sorted(self.adj_list.keys()):
            result.append(f"{v}: {self.adj_list[v]}")
        return "\n".join(result)


# Usage
g = GraphList()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')

print(g)
# A: ['B', 'C']
# B: ['A', 'C', 'D']
# C: ['A', 'B']
# D: ['B']

print(g.get_neighbors('B'))  # ['A', 'C', 'D']
```

### 3. Edge List

```python
# ═══════════════════════════════════════════════════════════════
# EDGE LIST REPRESENTATION
# ═══════════════════════════════════════════════════════════════

# edges = [(A,B), (A,C), (B,C), (B,D)]

class GraphEdgeList:
    def __init__(self, directed=False):
        self.edges = []
        self.vertices = set()
        self.directed = directed

    def add_edge(self, v1, v2, weight=1):
        self.vertices.add(v1)
        self.vertices.add(v2)
        self.edges.append((v1, v2, weight))

    def get_neighbors(self, v):
        neighbors = []
        for v1, v2, w in self.edges:
            if v1 == v:
                neighbors.append(v2)
            elif not self.directed and v2 == v:
                neighbors.append(v1)
        return neighbors

    def __str__(self):
        return f"Vertices: {self.vertices}\nEdges: {self.edges}"


# Usage - good for weighted graphs
g = GraphEdgeList()
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'D', 2)
print(g)
```

---

## 📊 Representation Comparison

| Aspect | Adjacency Matrix | Adjacency List | Edge List |
|--------|-----------------|----------------|-----------|
| Space | O(V²) | O(V + E) | O(E) |
| Add Edge | O(1) | O(1) | O(1) |
| Remove Edge | O(1) | O(E) | O(E) |
| Has Edge? | O(1) | O(degree) | O(E) |
| Get Neighbors | O(V) | O(degree) | O(E) |
| Best For | Dense graphs | Sparse graphs | Weighted/sorting |

---

## 🎯 When to Use Which?

```
┌─────────────────────────────────────────────────────────────────┐
│                CHOOSING REPRESENTATION                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ADJACENCY MATRIX when:                                         │
│  • Dense graph (many edges)                                     │
│  • Need O(1) edge lookup                                        │
│  • Small number of vertices                                     │
│  • Frequent edge existence checks                               │
│                                                                  │
│  ADJACENCY LIST when: (MOST COMMON)                             │
│  • Sparse graph (few edges)                                     │
│  • Need to iterate over neighbors                               │
│  • Memory is a concern                                          │
│  • BFS/DFS traversals                                           │
│                                                                  │
│  EDGE LIST when:                                                │
│  • Need to sort edges (Kruskal's MST)                          │
│  • Simple storage needed                                        │
│  • Weighted graphs                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🐍 Quick Python Graph (dict-based)

```python
# ═══════════════════════════════════════════════════════════════
# SIMPLEST GRAPH USING DICT
# ═══════════════════════════════════════════════════════════════

# Undirected graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B'],
    'D': ['B']
}

# Directed graph
digraph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# Weighted graph
weighted = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('D', 2)],
    'C': [('A', 3), ('D', 4)],
    'D': [('B', 2), ('C', 4)]
}

# Get neighbors
print(graph['A'])  # ['B', 'C']

# Check edge exists
print('B' in graph['A'])  # True
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Forgetting to add both directions for undirected
graph = {}
graph['A'] = ['B']
# Missing: graph['B'] = ['A']

# ✅ RIGHT: Add both directions
def add_undirected_edge(graph, v1, v2):
    graph.setdefault(v1, []).append(v2)
    graph.setdefault(v2, []).append(v1)

# ❌ WRONG: Using matrix for sparse graph (wastes memory)
# 1000 vertices with 100 edges = 1,000,000 cells for 100 edges!

# ✅ RIGHT: Use adjacency list for sparse graphs

# ❌ WRONG: Self-loops when not intended
graph['A'].append('A')  # A connects to itself?

# ✅ RIGHT: Check for self-loops if not allowed
def add_edge(graph, v1, v2):
    if v1 != v2:  # Prevent self-loops
        graph.setdefault(v1, []).append(v2)
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Use adjacency list for most cases | Use matrix for sparse graphs |
| Use defaultdict for cleaner code | Forget to initialize vertices |
| Consider directed vs undirected | Mix up edge directions |
| Track visited nodes in traversals | Infinite loop in cyclic graphs |

---

## 🎯 Exam Checklist

- [ ] Graph = Vertices + Edges
- [ ] Directed vs undirected graphs
- [ ] Degree, path, cycle, connected
- [ ] Adjacency matrix: O(V²) space, O(1) edge lookup
- [ ] Adjacency list: O(V+E) space, O(degree) lookup
- [ ] Choose representation based on density
- [ ] Most algorithms use adjacency list

---

[[10_AVL_Trees|← AVL Trees]] | [[00_Index|Index]] | [[12_Graphs_II|Graphs II →]]
---

## 🎨 Visualization (Optional)

```python
import sys
from pathlib import Path

# Add vault root to sys.path (Obsidian runner)
vault_root = Path.cwd()
if str(vault_root) not in sys.path:
    sys.path.append(str(vault_root))

from DSA_Utils.utils import draw_graph

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}

draw_graph(graph)
```
