---
title: Binary Search Trees (Beginner)
tags: [dsa, bst]
created: 2026-02-04
difficulty: beginner
---

# Binary Search Trees (Beginner)

[[00_Index|← Back to Index]] | [[08_Postorder_Traversal|← Postorder]] | [[10_AVL_Trees|AVL Trees →]]

## What it is
A BST keeps values **sorted**:
- Left subtree < node value
- Right subtree > node value

## Simple Insert + Search
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Insert a value into the BST

def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

# Search a value in the BST

def search(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    if target < node.value:
        return search(node.left, target)
    else:
        return search(node.right, target)

# Build a BST
root = None
for v in [8, 3, 10, 1, 6, 14]:
    root = insert(root, v)

print(search(root, 6))  # True
print(search(root, 7))  # False
```
