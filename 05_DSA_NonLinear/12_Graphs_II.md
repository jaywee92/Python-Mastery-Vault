---
title: Graphs II - Advanced Concepts
tags: [dsa, graphs, weighted, directed, components]
created: 2026-01-30
difficulty: intermediate
---

# 🕸️ Graphs II - Advanced Concepts

[[00_Index|← Back to Index]] | [[11_Graphs_I|← Graphs I]] | [[13_Graph_Traversals|Traversals →]]

> **"Understanding graph properties unlocks powerful algorithms"**

---

## ⚖️ Weighted Graphs

```
┌─────────────────────────────────────────────────────────────────┐
│                    WEIGHTED GRAPHS                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Edges have associated WEIGHTS (costs, distances, etc.)         │
│                                                                  │
│         5                                                        │
│    (A)─────(B)                                                  │
│     │\      │                                                   │
│   3 │ \ 2   │ 4                                                 │
│     │  \    │                                                   │
│    (C)─────(D)                                                  │
│         6                                                        │
│                                                                  │
│  Examples:                                                       │
│  • Road networks (distance in km)                               │
│  • Flight routes (cost in $)                                    │
│  • Network latency (time in ms)                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# WEIGHTED GRAPH IMPLEMENTATION
# ═══════════════════════════════════════════════════════════════

class WeightedGraph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, v1, v2, weight):
        self.add_vertex(v1)
        self.add_vertex(v2)

        self.adj_list[v1].append((v2, weight))
        if not self.directed:
            self.adj_list[v2].append((v1, weight))

    def get_weight(self, v1, v2):
        for neighbor, weight in self.adj_list.get(v1, []):
            if neighbor == v2:
                return weight
        return float('inf')

    def get_neighbors(self, v):
        return self.adj_list.get(v, [])


# Usage
g = WeightedGraph()
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'D', 4)
g.add_edge('C', 'D', 6)

print(g.get_neighbors('A'))  # [('B', 5), ('C', 3)]
print(g.get_weight('A', 'B'))  # 5
```

---

## 📊 Dense vs Sparse Graphs

```
┌─────────────────────────────────────────────────────────────────┐
│                DENSE vs SPARSE GRAPHS                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  SPARSE GRAPH:              DENSE GRAPH:                        │
│  Few edges                  Many edges                          │
│  E << V²                    E ≈ V²                              │
│                                                                  │
│    ○     ○                    ○─────○                           │
│     \   /                    /│\   /│\                          │
│      \ /                    / │ \ / │ \                         │
│       ○                    ○──│──○──│──○                        │
│      / \                    \ │ / \ │ /                         │
│     /   \                    \│/   \│/                          │
│    ○     ○                    ○─────○                           │
│                                                                  │
│  Use: Adjacency List        Use: Adjacency Matrix               │
│  Space: O(V + E)            Space: O(V²)                        │
│                                                                  │
│  Graph Density = E / (V * (V-1) / 2)  for undirected           │
│  Dense if density > 0.5                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
def graph_density(vertices, edges, directed=False):
    """Calculate graph density (0 to 1)."""
    v = vertices
    max_edges = v * (v - 1) if directed else v * (v - 1) // 2
    return edges / max_edges if max_edges > 0 else 0

# Example
print(graph_density(5, 4))   # 0.4 (sparse)
print(graph_density(5, 8))   # 0.8 (dense)
print(graph_density(5, 10))  # 1.0 (complete)
```

---

## 🔗 Connected Components

```
┌─────────────────────────────────────────────────────────────────┐
│              CONNECTED COMPONENTS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A connected component is a maximal set of vertices             │
│  where every vertex is reachable from every other.              │
│                                                                  │
│    Component 1        Component 2       Component 3             │
│    ┌─────────┐       ┌─────────┐       ┌─────┐                 │
│    │ A ─── B │       │ E ─── F │       │  H  │                 │
│    │ │     │ │       │         │       └─────┘                 │
│    │ C ─── D │       │    G    │                               │
│    └─────────┘       └─────────┘                               │
│                                                                  │
│  This graph has 3 connected components                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# FINDING CONNECTED COMPONENTS (DFS)
# ═══════════════════════════════════════════════════════════════

def find_connected_components(graph):
    """Find all connected components using DFS."""
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)

    for vertex in graph:
        if vertex not in visited:
            component = []
            dfs(vertex, component)
            components.append(component)

    return components


# Usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['F'],
    'F': ['E', 'G'],
    'G': ['F'],
    'H': []
}

components = find_connected_components(graph)
print(f"Number of components: {len(components)}")
print(f"Components: {components}")
# Number of components: 3
# Components: [['A', 'B', 'D', 'C'], ['E', 'F', 'G'], ['H']]
```

---

## 🔄 Strongly Connected Components (Directed)

```
┌─────────────────────────────────────────────────────────────────┐
│         STRONGLY CONNECTED COMPONENTS (SCC)                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  In directed graphs, an SCC is a maximal set where              │
│  every vertex is reachable from every other (both ways!)        │
│                                                                  │
│      ┌───→───┐                                                  │
│      A       B ──→ E                                            │
│      ↑   ↙   ↓     ↓                                            │
│      └─ C ←─ D     F                                            │
│                    ↑│                                           │
│                    └┘                                           │
│                                                                  │
│  SCCs: {A,B,C,D}, {E}, {F}                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# KOSARAJU'S ALGORITHM FOR SCC
# ═══════════════════════════════════════════════════════════════

def kosaraju_scc(graph):
    """Find strongly connected components using Kosaraju's algorithm."""

    # Step 1: Get vertices in order of finish time (DFS)
    visited = set()
    stack = []

    def dfs1(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs1(neighbor)
        stack.append(node)

    for vertex in graph:
        if vertex not in visited:
            dfs1(vertex)

    # Step 2: Create reversed graph
    reversed_graph = {v: [] for v in graph}
    for v in graph:
        for neighbor in graph[v]:
            reversed_graph[neighbor].append(v)

    # Step 3: DFS on reversed graph in stack order
    visited.clear()
    sccs = []

    def dfs2(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in reversed_graph.get(node, []):
            if neighbor not in visited:
                dfs2(neighbor, component)

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            component = []
            dfs2(vertex, component)
            sccs.append(component)

    return sccs


# Usage
digraph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['A'],
    'D': ['E'],
    'E': ['F'],
    'F': ['E']
}

sccs = kosaraju_scc(digraph)
print(f"SCCs: {sccs}")
# SCCs: [['F', 'E'], ['D'], ['A', 'C', 'B']]
```

---

## 🎨 Bipartite Graphs

```
┌─────────────────────────────────────────────────────────────────┐
│                  BIPARTITE GRAPHS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Vertices can be divided into TWO disjoint sets where           │
│  every edge connects a vertex from one set to the other.        │
│                                                                  │
│   Set A        Set B          NOT Bipartite (has triangle):     │
│   ┌───┐       ┌───┐                                             │
│   │ 1 │───────│ A │              1 ─── 2                        │
│   │ 2 │───┬───│ B │               \ ┃ /                         │
│   │ 3 │──┬┼───│ C │                \┃/                          │
│   └───┘  │└───│ D │                 3                           │
│          └────┴───┘                                             │
│                                                                  │
│  A graph is bipartite iff it contains NO odd-length cycles      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# CHECK IF GRAPH IS BIPARTITE (2-colorable)
# ═══════════════════════════════════════════════════════════════

from collections import deque

def is_bipartite(graph):
    """Check if graph is bipartite using BFS coloring."""
    color = {}

    for start in graph:
        if start in color:
            continue

        queue = deque([start])
        color[start] = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]  # Alternate color
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False  # Same color = not bipartite

    return True


# Usage
bipartite = {
    1: ['A', 'B'],
    2: ['B', 'C'],
    3: ['C', 'D'],
    'A': [1],
    'B': [1, 2],
    'C': [2, 3],
    'D': [3]
}

not_bipartite = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2]  # Triangle!
}

print(is_bipartite(bipartite))      # True
print(is_bipartite(not_bipartite))  # False
```

---

## 🌟 Complete Graphs

```
┌─────────────────────────────────────────────────────────────────┐
│                  COMPLETE GRAPH (Kn)                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Every vertex connected to every other vertex                   │
│                                                                  │
│   K3         K4              K5                                 │
│    △        ╱│╲            ╱│╲│╲                               │
│   ╱ ╲      ╱ │ ╲          ╱ │ ╲│ ╲                             │
│  ●───●    ●──│──●        ●──│──●│  ●                           │
│            ╲ │ ╱          ╲ │ ╱│ ╱                             │
│             ╲│╱            ╲│╱ │╱                              │
│              ●              ●──●                                │
│                                                                  │
│  Edges in Kn = n(n-1)/2                                         │
│  K4 has 6 edges, K5 has 10 edges                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Consider edge weights for real problems | Ignore weights in shortest path |
| Check graph connectivity first | Assume all vertices reachable |
| Use appropriate SCC algorithm | Use undirected component algorithm for digraphs |
| Verify bipartiteness for matching | Assume 2-colorability |

---

## 🎯 Exam Checklist

- [ ] Weighted graphs store cost/distance on edges
- [ ] Sparse: E << V², Dense: E ≈ V²
- [ ] Connected component: all vertices mutually reachable
- [ ] SCC: strongly connected in directed graphs
- [ ] Bipartite: 2-colorable, no odd cycles
- [ ] Complete graph Kn has n(n-1)/2 edges

---

[[11_Graphs_I|← Graphs I]] | [[00_Index|Index]] | [[13_Graph_Traversals|Traversals →]]
