---
title: Bellman-Ford Algorithm
tags: [dsa, graphs, bellman-ford, shortest-path, negative-weights]
created: 2026-01-30
difficulty: advanced
time_complexity: O(V * E)
space_complexity: O(V)
---

# 🔔 Bellman-Ford Algorithm

[[00_Index|← Back to Index]] | [[16_Dijkstras|← Dijkstra's]]

> **"The algorithm that handles negative weights and detects negative cycles"**

---

## 🎯 The Algorithm

```
┌─────────────────────────────────────────────────────────────────┐
│              BELLMAN-FORD ALGORITHM                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  IDEA: Relax ALL edges V-1 times                                │
│                                                                  │
│  1. Initialize: dist[source] = 0, all others = ∞               │
│  2. Repeat V-1 times:                                           │
│     - For each edge (u, v, weight):                             │
│       - If dist[u] + weight < dist[v]:                          │
│         - dist[v] = dist[u] + weight                            │
│  3. Check for negative cycles (optional):                       │
│     - For each edge (u, v, weight):                             │
│       - If dist[u] + weight < dist[v]:                          │
│         - NEGATIVE CYCLE EXISTS!                                │
│                                                                  │
│  WHY V-1 times?                                                 │
│  A shortest path has at most V-1 edges.                         │
│  Each iteration finds paths with one more edge.                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Step-by-Step Example

```
┌─────────────────────────────────────────────────────────────────┐
│              BELLMAN-FORD TRACE                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Graph (with negative edge):                                    │
│           4           -2                                        │
│      A ─────→ B ─────→ C                                        │
│      │        ↑        │                                        │
│    2 │        │ 3      │ 2                                      │
│      ↓        │        ↓                                        │
│      D ───────┴────────→ E                                      │
│           1        5                                            │
│                                                                  │
│  Edges: (A,B,4), (A,D,2), (B,C,-2), (C,E,2), (D,B,3), (D,E,5)  │
│                                                                  │
│  V=5, so iterate V-1=4 times                                    │
│                                                                  │
│  Initial:    dist = {A:0, B:∞, C:∞, D:∞, E:∞}                  │
│                                                                  │
│  Iteration 1:                                                   │
│    (A,B): dist[B] = min(∞, 0+4) = 4                            │
│    (A,D): dist[D] = min(∞, 0+2) = 2                            │
│    dist = {A:0, B:4, C:∞, D:2, E:∞}                            │
│                                                                  │
│  Iteration 2:                                                   │
│    (B,C): dist[C] = min(∞, 4-2) = 2                            │
│    (D,B): dist[B] = min(4, 2+3) = 4 (no change)                │
│    (D,E): dist[E] = min(∞, 2+5) = 7                            │
│    dist = {A:0, B:4, C:2, D:2, E:7}                            │
│                                                                  │
│  Iteration 3:                                                   │
│    (C,E): dist[E] = min(7, 2+2) = 4                            │
│    dist = {A:0, B:4, C:2, D:2, E:4}                            │
│                                                                  │
│  Iteration 4: No changes                                        │
│                                                                  │
│  FINAL: {A:0, B:4, C:2, D:2, E:4}                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Implementation

```python
# ═══════════════════════════════════════════════════════════════
# BELLMAN-FORD ALGORITHM
# ═══════════════════════════════════════════════════════════════

def bellman_ford(vertices, edges, source):
    """
    Find shortest paths from source using Bellman-Ford.

    Args:
        vertices: list of vertex names
        edges: list of (u, v, weight) tuples
        source: starting vertex

    Returns:
        dist: dict of shortest distances
        prev: dict for path reconstruction
        has_negative_cycle: bool
    """
    # Initialize
    dist = {v: float('inf') for v in vertices}
    prev = {v: None for v in vertices}
    dist[source] = 0

    # Relax all edges V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u

    # Check for negative cycles
    has_negative_cycle = False
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            has_negative_cycle = True
            break

    return dist, prev, has_negative_cycle


def get_path(prev, source, target):
    """Reconstruct path from prev dict."""
    if prev[target] is None and target != source:
        return None
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = prev[current]
    return path[::-1]


# Usage
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 4),
    ('A', 'D', 2),
    ('B', 'C', -2),  # Negative weight!
    ('C', 'E', 2),
    ('D', 'B', 3),
    ('D', 'E', 5)
]

dist, prev, has_cycle = bellman_ford(vertices, edges, 'A')
print("Distances:", dist)
print("Has negative cycle:", has_cycle)
print("Path A→E:", get_path(prev, 'A', 'E'))
# Distances: {'A': 0, 'B': 4, 'C': 2, 'D': 2, 'E': 4}
# Has negative cycle: False
# Path A→E: ['A', 'B', 'C', 'E']
```

---

## 🔴 Detecting Negative Cycles

```python
# ═══════════════════════════════════════════════════════════════
# NEGATIVE CYCLE DETECTION AND FINDING
# ═══════════════════════════════════════════════════════════════

def find_negative_cycle(vertices, edges, source):
    """
    Find a negative cycle if one exists.
    """
    dist = {v: float('inf') for v in vertices}
    prev = {v: None for v in vertices}
    dist[source] = 0

    # Relax V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u

    # One more iteration to find cycle
    cycle_vertex = None
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            cycle_vertex = v
            break

    if cycle_vertex is None:
        return None  # No negative cycle

    # Find the cycle
    # Go back V times to ensure we're in the cycle
    for _ in range(len(vertices)):
        cycle_vertex = prev[cycle_vertex]

    # Trace the cycle
    cycle = []
    current = cycle_vertex
    while True:
        cycle.append(current)
        current = prev[current]
        if current == cycle_vertex:
            cycle.append(current)
            break

    return cycle[::-1]


# Test with negative cycle
vertices = ['A', 'B', 'C']
edges_with_cycle = [
    ('A', 'B', 1),
    ('B', 'C', -3),
    ('C', 'A', 1)  # Total: 1 + (-3) + 1 = -1 (negative cycle!)
]

cycle = find_negative_cycle(vertices, edges_with_cycle, 'A')
print("Negative cycle:", cycle)
# Negative cycle: ['A', 'B', 'C', 'A']
```

---

## 🆚 Dijkstra vs Bellman-Ford

| Aspect | Dijkstra | Bellman-Ford |
|--------|----------|--------------|
| Negative edges | ❌ No | ✅ Yes |
| Negative cycles | ❌ Fails | ✅ Detects |
| Time complexity | O((V+E) log V) | O(V·E) |
| Space complexity | O(V) | O(V) |
| Algorithm type | Greedy | Dynamic Programming |
| Best for | Non-negative weights | Negative weights |

---

## 🎯 When to Use Bellman-Ford?

```
┌─────────────────────────────────────────────────────────────────┐
│              USE BELLMAN-FORD WHEN:                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ✅ Graph has NEGATIVE edge weights                             │
│                                                                  │
│  ✅ Need to DETECT negative cycles                              │
│                                                                  │
│  ✅ Graph is relatively SPARSE (fewer edges)                    │
│                                                                  │
│  ✅ Simpler implementation needed                               │
│                                                                  │
│  ❌ DON'T use when:                                             │
│     • All weights are non-negative (use Dijkstra)              │
│     • Graph is very large (Dijkstra is faster)                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Not checking for negative cycles
dist, prev, _ = bellman_ford(vertices, edges, 'A')
# If there's a negative cycle, distances are INVALID!

# ✅ RIGHT: Always check
dist, prev, has_cycle = bellman_ford(vertices, edges, 'A')
if has_cycle:
    print("No valid shortest paths - negative cycle exists!")
else:
    print(dist)

# ❌ WRONG: Starting relaxation from infinity
# If dist[u] == inf, then dist[u] + w might overflow or be wrong

# ✅ RIGHT: Check for infinity before relaxing
if dist[u] != float('inf') and dist[u] + weight < dist[v]:
    dist[v] = dist[u] + weight

# ❌ WRONG: Only V-2 iterations
for _ in range(len(vertices) - 2):  # Too few!

# ✅ RIGHT: Exactly V-1 iterations
for _ in range(len(vertices) - 1):  # Correct!
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Check for negative cycles | Assume no cycles exist |
| Use Dijkstra if no negative weights | Use Bellman-Ford always |
| Initialize source to 0, rest to ∞ | Initialize all to 0 |
| Iterate exactly V-1 times | Under-iterate |

---

## 🎯 Exam Checklist

- [ ] Relax ALL edges V-1 times
- [ ] Handles negative edge weights
- [ ] Extra iteration detects negative cycles
- [ ] Time: O(V·E), Space: O(V)
- [ ] If no negative cycle, distances are correct
- [ ] Path can have at most V-1 edges (why V-1 iterations)

---

[[16_Dijkstras|← Dijkstra's]] | [[00_Index|Index]]
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

graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["D"],
    "D": [],
}

draw_graph(graph, title="Path Graph")
```
