---
title: Binary Trees (Beginner)
tags: [dsa, binary-tree]
created: 2026-02-04
difficulty: beginner
---

# Binary Trees (Beginner)

[[00_Index|← Back to Index]] | [[04_Trees|← Trees]] | [[06_Preorder_Traversal|Preorder →]]

## What it is
A **binary tree** is a tree where each node has **at most 2 children**: left and right.

## Simple Example
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Build a small tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print(root.value)      # 1
print(root.left.value) # 2
print(root.right.value)# 3
```

## Key Points
- Left and right children are optional
- Many algorithms use binary trees
