---
title: Dijkstra's Algorithm
tags: [dsa, graphs, dijkstra, shortest-path, greedy]
created: 2026-01-30
difficulty: advanced
time_complexity: O((V+E) log V)
space_complexity: O(V)
---

# 🎯 Dijkstra's Algorithm

[[00_Index|← Back to Index]] | [[15_Shortest_Path|← Shortest Path]] | [[17_Bellman_Ford|Bellman-Ford →]]

> **"The greedy algorithm that always finds the shortest path (with non-negative weights)"**

---

## 🎯 The Algorithm

```
┌─────────────────────────────────────────────────────────────────┐
│              DIJKSTRA'S ALGORITHM                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  IDEA: Greedily pick the closest unvisited vertex               │
│                                                                  │
│  1. Initialize distances: source = 0, all others = ∞           │
│  2. Add source to priority queue (min-heap)                     │
│  3. While queue not empty:                                      │
│     a. Pop vertex u with minimum distance                       │
│     b. For each neighbor v of u:                                │
│        - If dist[u] + weight(u,v) < dist[v]:                   │
│          - Update dist[v]                                       │
│          - Add v to queue (or update priority)                  │
│  4. Return distances                                            │
│                                                                  │
│  KEY: Once a vertex is popped, its shortest path is FINAL!     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Step-by-Step Example

```
┌─────────────────────────────────────────────────────────────────┐
│                    DIJKSTRA TRACE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Graph:        4                                                │
│           A ─────── B                                           │
│           │\        │\                                          │
│         2 │ \ 1     │ \ 3                                       │
│           │  \      │  \                                        │
│           C ─ D ─── E ── F                                      │
│             3     2    1                                        │
│                                                                  │
│  Start: A                                                       │
│                                                                  │
│  Initial:  dist = {A:0, B:∞, C:∞, D:∞, E:∞, F:∞}              │
│                                                                  │
│  Step 1: Pop A (dist=0)                                         │
│          Update: B=4, C=2, D=1                                  │
│          dist = {A:0, B:4, C:2, D:1, E:∞, F:∞}                 │
│                                                                  │
│  Step 2: Pop D (dist=1)                                         │
│          Update: C=min(2,1+3)=2, E=1+2=3                        │
│          dist = {A:0, B:4, C:2, D:1, E:3, F:∞}                 │
│                                                                  │
│  Step 3: Pop C (dist=2)                                         │
│          No updates needed                                      │
│                                                                  │
│  Step 4: Pop E (dist=3)                                         │
│          Update: B=min(4,3+3)=4, F=3+1=4                        │
│          dist = {A:0, B:4, C:2, D:1, E:3, F:4}                 │
│                                                                  │
│  Step 5: Pop B (dist=4), Pop F (dist=4)                         │
│          No improvements                                        │
│                                                                  │
│  FINAL: {A:0, B:4, C:2, D:1, E:3, F:4}                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Implementation with Min-Heap

```python
# ═══════════════════════════════════════════════════════════════
# DIJKSTRA'S ALGORITHM - PRIORITY QUEUE VERSION
# ═══════════════════════════════════════════════════════════════
import heapq

def dijkstra(graph, start):
    """
    Find shortest distances from start to all vertices.

    Args:
        graph: dict where graph[u] = [(v, weight), ...]
        start: starting vertex

    Returns:
        dist: dict of shortest distances
        prev: dict for path reconstruction
    """
    # Initialize distances
    dist = {v: float('inf') for v in graph}
    dist[start] = 0

    # For path reconstruction
    prev = {v: None for v in graph}

    # Priority queue: (distance, vertex)
    pq = [(0, start)]
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        # Skip if already processed
        if u in visited:
            continue
        visited.add(u)

        # Relax edges
        for v, weight in graph.get(u, []):
            if v not in visited:
                new_dist = dist[u] + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    prev[v] = u
                    heapq.heappush(pq, (new_dist, v))

    return dist, prev


def get_path(prev, start, end):
    """Reconstruct path from prev dict."""
    if prev[end] is None and end != start:
        return None  # No path

    path = []
    current = end
    while current is not None:
        path.append(current)
        current = prev[current]
    return path[::-1]


# Usage
graph = {
    'A': [('B', 4), ('C', 2), ('D', 1)],
    'B': [('A', 4), ('E', 3), ('F', 3)],
    'C': [('A', 2), ('D', 3)],
    'D': [('A', 1), ('C', 3), ('E', 2)],
    'E': [('D', 2), ('B', 3), ('F', 1)],
    'F': [('B', 3), ('E', 1)]
}

dist, prev = dijkstra(graph, 'A')
print("Distances:", dist)
# {'A': 0, 'B': 4, 'C': 2, 'D': 1, 'E': 3, 'F': 4}

print("Path A→F:", get_path(prev, 'A', 'F'))
# ['A', 'D', 'E', 'F']
```

---

## 🔄 Simplified Version (Just Distances)

```python
# ═══════════════════════════════════════════════════════════════
# DIJKSTRA - SIMPLIFIED VERSION
# ═══════════════════════════════════════════════════════════════
import heapq

def dijkstra_simple(graph, start):
    """Simplified Dijkstra returning just distances."""
    dist = {start: 0}
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist.get(u, float('inf')):
            continue  # Outdated entry

        for v, weight in graph.get(u, []):
            new_dist = d + weight
            if new_dist < dist.get(v, float('inf')):
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist


# Even simpler using defaultdict
from collections import defaultdict

def dijkstra_clean(adj, start):
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dict(dist)
```

---

## ⚠️ Why No Negative Weights?

```
┌─────────────────────────────────────────────────────────────────┐
│              DIJKSTRA FAILS WITH NEGATIVE WEIGHTS               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│         1                                                        │
│      A ───→ B                                                   │
│       \     │                                                   │
│      2 \    │ -3                                                │
│         \   ↓                                                   │
│          → C                                                    │
│                                                                  │
│  Dijkstra would:                                                │
│  1. Start at A (dist=0)                                         │
│  2. Pop B (dist=1) - FINALIZED!                                 │
│  3. Pop C (dist=2)                                              │
│  4. From C, can't update B (already visited)                    │
│                                                                  │
│  Dijkstra says: A→B = 1                                         │
│  Actually:       A→C→B = 2 + (-3) = -1  ← SHORTER!             │
│                                                                  │
│  Problem: Dijkstra assumes finalized distances are optimal,     │
│  but negative edges can provide "shortcuts" later.              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Time Complexity Analysis

| Implementation | Time | Notes |
|----------------|------|-------|
| Array (naive) | O(V²) | Good for dense graphs |
| Binary Heap | O((V+E) log V) | Most common |
| Fibonacci Heap | O(E + V log V) | Theoretically best |

**In practice:** Binary heap is usually the best choice.

---

## 🎯 Common Interview Variations

```python
# ═══════════════════════════════════════════════════════════════
# VARIATION: Shortest path with exactly K edges
# ═══════════════════════════════════════════════════════════════

def shortest_path_k_edges(graph, start, end, k):
    """Find shortest path using exactly k edges."""
    # DP approach: dp[v][i] = min dist to v using i edges
    n = len(graph)
    INF = float('inf')

    dp = {v: [INF] * (k + 1) for v in graph}
    dp[start][0] = 0

    for i in range(1, k + 1):
        for u in graph:
            for v, w in graph[u]:
                if dp[u][i-1] != INF:
                    dp[v][i] = min(dp[v][i], dp[u][i-1] + w)

    return dp[end][k] if dp[end][k] != INF else -1


# ═══════════════════════════════════════════════════════════════
# VARIATION: Shortest path with at most K stops
# ═══════════════════════════════════════════════════════════════

def cheapest_flight(n, flights, src, dst, k):
    """
    Leetcode 787: Cheapest Flights Within K Stops
    """
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0

    for _ in range(k + 1):
        temp = dist.copy()
        for u, v, w in flights:
            if dist[u] != INF:
                temp[v] = min(temp[v], dist[u] + w)
        dist = temp

    return dist[dst] if dist[dst] != INF else -1
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Not handling already-visited nodes
while pq:
    d, u = heapq.heappop(pq)
    for v, w in graph[u]:
        # Will process same node multiple times!

# ✅ RIGHT: Skip outdated entries
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue  # Skip outdated
    for v, w in graph[u]:
        # ...

# ❌ WRONG: Using with negative weights
# Dijkstra WILL give wrong answers!

# ✅ RIGHT: Use Bellman-Ford for negative weights

# ❌ WRONG: Forgetting path reconstruction
# Only returning distances, losing path info

# ✅ RIGHT: Track predecessors for path
prev[v] = u  # When updating dist[v]
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Use heapq for priority queue | Use sorted list (slow!) |
| Skip outdated heap entries | Process same node twice |
| Check for negative weights first | Assume all graphs work |
| Store predecessors for paths | Only compute distances |

---

## 🎯 Exam Checklist

- [ ] Greedy algorithm: always pick closest unvisited vertex
- [ ] Uses priority queue (min-heap)
- [ ] Time: O((V+E) log V) with binary heap
- [ ] DOES NOT work with negative weights
- [ ] Once a vertex is popped, its distance is FINAL
- [ ] Track prev[] for path reconstruction

---

[[15_Shortest_Path|← Shortest Path]] | [[00_Index|Index]] | [[17_Bellman_Ford|Bellman-Ford →]]
---

## 🎨 Visualization (Optional)

```python
import sys
import site
from pathlib import Path

# Ensure user site-packages are visible (Obsidian runner)
user_site = site.getusersitepackages()
if user_site and user_site not in sys.path:
    sys.path.append(user_site)

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
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": [],
}

draw_graph(graph, title="Dijkstra Graph (visual)")

```
