---
title: Graph Traversals (Beginner)
tags: [dsa, graphs, bfs, dfs]
created: 2026-02-04
difficulty: beginner
---

# Graph Traversals (Beginner)

[[00_Index|← Back to Index]] | [[12_Graphs_II|← Graphs II]] | [[14_Cycle_Detection|Cycle Detection →]]

## BFS (Breadth-First Search)
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

graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
print(bfs(graph, "A"))  # ['A', 'B', 'C', 'D']
```

## DFS (Depth-First Search)
```python
def dfs(graph, start):
    visited = set()
    order = []

    def helper(node):
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            helper(neighbor)

    helper(start)
    return order

print(dfs(graph, "A"))  # ['A', 'B', 'D', 'C']
```
