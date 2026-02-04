---
title: Cycle Detection (Beginner)
tags: [dsa, graphs, cycle]
created: 2026-02-04
difficulty: beginner
---

# Cycle Detection (Beginner)

[[00_Index|← Back to Index]] | [[13_Graph_Traversals|← Graph Traversals]] | [[15_Shortest_Path|Shortest Path →]]

## Undirected Graph (Simple)
We check if we can come back to a visited node that is not the parent.

```python
def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

# Example graph with a cycle: A-B-C-A
graph = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
print(has_cycle(graph))  # True
```
