---
title: Bellman-Ford (Beginner)
tags: [dsa, graphs, bellman-ford]
created: 2026-02-04
difficulty: beginner
---

# Bellman-Ford (Beginner)

[[00_Index|← Back to Index]] | [[16_Dijkstras|← Dijkstra]] | [[00_Index|Index →]]

## What it does
Finds the shortest paths even when **negative weights** exist.

## Beginner-Friendly Version
```python
import math

# Edge list: (from, to, weight)
edges = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("C", "B", -1),
    ("B", "D", 2),
    ("C", "D", 5),
]

nodes = {"A", "B", "C", "D"}

# Bellman-Ford

def bellman_ford(nodes, edges, start):
    dist = {n: math.inf for n in nodes}
    dist[start] = 0

    # Relax edges |V|-1 times
    for _ in range(len(nodes) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist

print(bellman_ford(nodes, edges, "A"))
```
