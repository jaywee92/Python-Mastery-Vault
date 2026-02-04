---
title: Shortest Path (Beginner)
tags: [dsa, graphs, shortest-path]
created: 2026-02-04
difficulty: beginner
---

# Shortest Path (Beginner)

[[00_Index|← Back to Index]] | [[14_Cycle_Detection|← Cycle Detection]] | [[16_Dijkstras|Dijkstra →]]

## Unweighted Graph
For unweighted graphs, **BFS** finds the shortest path.

```python
from collections import deque

def shortest_path(graph, start, target):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        node, path = queue.popleft()
        if node == target:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
print(shortest_path(graph, "A", "D"))  # ['A', 'B', 'D']
```
