---
title: Graphs II (Beginner)
tags: [dsa, graphs, directed]
created: 2026-02-04
difficulty: beginner
---

# Graphs II (Beginner)

[[00_Index|← Back to Index]] | [[11_Graphs_I|← Graphs I]] | [[13_Graph_Traversals|Graph Traversals →]]

## Directed vs Undirected
```python
# Directed graph
digraph = {
    "A": ["B"],
    "B": ["C"],
    "C": [],
}

# Undirected graph (edges go both ways)
undirected = {
    "A": ["B"],
    "B": ["A"],
}
```

## Weighted Graph (Beginner Look)
```python
# Weight = cost of the edge
weighted = {
    "A": [("B", 5), ("C", 2)],
    "B": [("C", 1)],
    "C": [],
}
```
