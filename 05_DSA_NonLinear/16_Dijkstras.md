---
title: Dijkstra's Algorithm (Beginner)
tags: [dsa, graphs, dijkstra]
created: 2026-02-04
difficulty: beginner
---

# Dijkstra's Algorithm (Beginner)

[[00_Index|← Back to Index]] | [[15_Shortest_Path|← Shortest Path]] | [[17_Bellman_Ford|Bellman-Ford →]]

## What it does
Finds the **shortest path** in a graph with **non-negative weights**.

## Beginner-Friendly Version (No Heap)
This version is easy to read, but slower for large graphs.

```python
import math

# Weighted graph as adjacency list: node -> list of (neighbor, weight)
graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("E", 3)],
    "D": [("F", 11)],
    "E": [("D", 4)],
    "F": [],
}

# Dijkstra without a priority queue (beginner friendly)

def dijkstra(graph, start):
    # Step 1: distances (unknown = infinity)
    dist = {node: math.inf for node in graph}
    dist[start] = 0

    # Step 2: visited set
    visited = set()

    while len(visited) < len(graph):
        # Step 3: pick the unvisited node with smallest distance
        current = None
        current_dist = math.inf
        for node in graph:
            if node not in visited and dist[node] < current_dist:
                current = node
                current_dist = dist[node]

        if current is None:
            break

        visited.add(current)

        # Step 4: relax neighbors
        for neighbor, weight in graph[current]:
            new_dist = dist[current] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist

    return dist

print(dijkstra(graph, "A"))
```
