---
title: Graphs I (Beginner)
tags: [dsa, graphs]
created: 2026-02-04
difficulty: beginner
---

# Graphs I (Beginner)

[[00_Index|← Back to Index]] | [[10_AVL_Trees|← AVL Trees]] | [[12_Graphs_II|Graphs II →]]

## What it is
A graph is a set of **nodes (vertices)** and **edges** between them.

## Adjacency List (Most Common)
```python
# Undirected graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}

# Neighbors of B
print(graph["B"])  # ['A', 'D']
```

## Key Points
- Use a dict of lists for adjacency lists
- Good for BFS/DFS
