---
title: Shortest Path - Overview
tags: [dsa, graphs, shortest-path, dijkstra, bellman-ford]
created: 2026-01-30
difficulty: intermediate
---

# 🛤️ Shortest Path

[[00_Index|← Back to Index]] | [[14_Cycle_Detection|← Cycle Detection]] | [[16_Dijkstras|Dijkstra's →]]

> **"Finding the best route - the fundamental graph optimization problem"**

---

## 🎨 Visual Memory Aid

```
╔═════════════════════════════════════════════════════════════════╗
║      🛤️ SHORTEST PATH - FINDING MINIMUM COST ROUTE             ║
╠═════════════════════════════════════════════════════════════════╣
║                                                                 ║
║   PROBLEM: Find path with MINIMUM total weight/cost             ║
║                                                                 ║
║   EXAMPLE GRAPH (edges show weights):                          ║
║            5                                                    ║
║       [A]─────[B]                                              ║
║       │\       │                                               ║
║      1│ \3  2  │                                               ║
║       │  \     │                                               ║
║      [C]──────[D]                                              ║
║            4                                                    ║
║                                                                 ║
║   FINDING SHORTEST PATH FROM A TO D:                           ║
║   Path 1: A → B → D  = 5 + 2 = 7                              ║
║   Path 2: A → C → D  = 1 + 4 = 5 ✓ SHORTEST!                  ║
║   Path 3: A → D      = 3     ✓ DIRECT BEST!                    ║
║                                                                 ║
║   SOLUTION METHODS:                                            ║
║   • DIJKSTRA'S: Greedy approach, always picks closest          ║
║     Works only with NON-NEGATIVE weights                       ║
║     Time: O((V+E)log V)                                        ║
║                                                                 ║
║   • BELLMAN-FORD: Dynamic programming approach                 ║
║     Works with NEGATIVE weights (but not negative cycles)      ║
║     Time: O(VE)                                                ║
║                                                                 ║
║   • FLOYD-WARSHALL: All-pairs shortest paths                   ║
║     Find shortest between every pair of vertices               ║
║     Time: O(V³)                                                ║
║                                                                 ║
║   💡 GPS/Maps use Dijkstra's for fast routes                   ║
║   💡 Negative weights appear in arbitrage/profit problems      ║
║   💡 Choose algorithm based on graph properties                ║
║                                                                 ║
╚═════════════════════════════════════════════════════════════════╝
```

---

## 🎯 The Problem

```
┌─────────────────────────────────────────────────────────────────┐
│              SHORTEST PATH PROBLEM                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Given a weighted graph, find the path with minimum total       │
│  weight (cost/distance) between two vertices.                   │
│                                                                  │
│           5                                                      │
│      A ─────── B                                                │
│      │\        │                                                │
│    1 │ \ 3     │ 2                                              │
│      │  \      │                                                │
│      C ─────── D                                                │
│           4                                                      │
│                                                                  │
│  Shortest A → D:                                                │
│  • A → B → D = 5 + 2 = 7                                        │
│  • A → C → D = 1 + 4 = 5  ← SHORTEST!                          │
│  • A → D     = 3                                                │
│                                                                  │
│  Answer: A → D (direct) with cost 3                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Types of Shortest Path Problems

```
┌─────────────────────────────────────────────────────────────────┐
│              PROBLEM VARIANTS                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. SINGLE-SOURCE SHORTEST PATH                                 │
│     Find shortest path from ONE source to ALL other vertices    │
│     → Dijkstra's, Bellman-Ford                                  │
│                                                                  │
│  2. SINGLE-PAIR SHORTEST PATH                                   │
│     Find shortest path between TWO specific vertices            │
│     → A* (with heuristic), or single-source algorithms          │
│                                                                  │
│  3. ALL-PAIRS SHORTEST PATH                                     │
│     Find shortest path between EVERY pair of vertices           │
│     → Floyd-Warshall                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Algorithm Selection

```
┌─────────────────────────────────────────────────────────────────┐
│              CHOOSING THE RIGHT ALGORITHM                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  UNWEIGHTED GRAPH?                                              │
│  └─→ Use BFS! (O(V+E))                                          │
│                                                                  │
│  WEIGHTED, NO NEGATIVE EDGES?                                   │
│  └─→ Use DIJKSTRA'S (O((V+E) log V) with heap)                 │
│                                                                  │
│  NEGATIVE EDGES (no negative cycles)?                           │
│  └─→ Use BELLMAN-FORD (O(V·E))                                  │
│                                                                  │
│  DETECT NEGATIVE CYCLES?                                        │
│  └─→ Use BELLMAN-FORD (one extra iteration)                     │
│                                                                  │
│  ALL PAIRS?                                                     │
│  └─→ Use FLOYD-WARSHALL (O(V³))                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📝 BFS for Unweighted Graphs

```python
# ═══════════════════════════════════════════════════════════════
# BFS SHORTEST PATH (UNWEIGHTED)
# ═══════════════════════════════════════════════════════════════
from collections import deque

def bfs_shortest(graph, start):
    """
    Find shortest path from start to all vertices (unweighted).
    Returns dict of distances.
    """
    dist = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


def bfs_shortest_path(graph, start, end):
    """
    Find shortest path and return the actual path.
    """
    if start == end:
        return [start]

    visited = {start: None}  # vertex: parent
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited[neighbor] = node
                if neighbor == end:
                    # Reconstruct path
                    path = []
                    current = end
                    while current is not None:
                        path.append(current)
                        current = visited[current]
                    return path[::-1]
                queue.append(neighbor)

    return None  # No path


# Usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs_shortest(graph, 'A'))
# {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}

print(bfs_shortest_path(graph, 'A', 'F'))
# ['A', 'C', 'F']
```

---

## ⚠️ The Negative Weight Problem

```
┌─────────────────────────────────────────────────────────────────┐
│              WHY NEGATIVE WEIGHTS ARE TRICKY                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  NEGATIVE EDGES: Some algorithms fail!                          │
│                                                                  │
│         2                                                        │
│      A ───→ B                                                   │
│      │      ↓                                                   │
│    5 │     -4    Dijkstra would find A→B = 2                    │
│      ↓      │    But A→C→B = 5 + (-4) = 1 is shorter!           │
│      C ─────┘                                                   │
│                                                                  │
│  NEGATIVE CYCLES: No solution exists!                           │
│                                                                  │
│         -1                                                       │
│      A ───→ B                                                   │
│      ↑      ↓                                                   │
│      └──────┘    Total: -1 + (-1) + (-1) = -3                   │
│         -1       Going around = always shorter!                  │
│                  Path can be infinitely negative.                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Algorithm Comparison

| Algorithm | Weights | Negative? | Time | Space |
|-----------|---------|-----------|------|-------|
| BFS | Unweighted | N/A | O(V+E) | O(V) |
| Dijkstra | Non-negative | ❌ | O((V+E)log V) | O(V) |
| Bellman-Ford | Any | ✅ | O(V·E) | O(V) |
| Floyd-Warshall | Any | ✅ | O(V³) | O(V²) |

---

## 🎯 Quick Reference

```python
# Decision flowchart in code
def shortest_path(graph, start, end=None, has_negative=False):
    """Choose algorithm based on graph properties."""

    # Check if unweighted
    is_weighted = any(
        isinstance(n, tuple)
        for neighbors in graph.values()
        for n in neighbors
    )

    if not is_weighted:
        return bfs_shortest(graph, start)

    if has_negative:
        return bellman_ford(graph, start)
    else:
        return dijkstra(graph, start)
```

---

## 🔗 Related Topics

| Topic | Description |
|-------|-------------|
| [[16_Dijkstras\|Dijkstra's Algorithm]] | Greedy approach, no negative weights |
| [[17_Bellman_Ford\|Bellman-Ford]] | Handles negative weights |
| A* Algorithm | Dijkstra + heuristic |
| Floyd-Warshall | All-pairs shortest path |

---

## 🎯 Exam Checklist

- [ ] BFS for unweighted graphs
- [ ] Dijkstra for non-negative weights
- [ ] Bellman-Ford for negative weights
- [ ] Negative cycles = no valid shortest path
- [ ] Know time complexity of each algorithm

---

[[14_Cycle_Detection|← Cycle Detection]] | [[00_Index|Index]] | [[16_Dijkstras|Dijkstra's →]]
