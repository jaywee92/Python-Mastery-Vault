---
title: AVL Trees (Beginner)
tags: [dsa, avl, balanced-tree]
created: 2026-02-04
difficulty: beginner
---

# AVL Trees (Beginner)

[[00_Index|← Back to Index]] | [[09_Binary_Search_Trees|← BST]] | [[11_Graphs_I|Graphs I →]]

## What it is
An **AVL tree** is a BST that keeps itself **balanced**.
Balanced means the tree does not get too tall.

## Beginner View
We only calculate **height** and **balance factor** here.
Rotations are **advanced**, so we skip them.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Height of a tree

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

# Balance factor = left height - right height

def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)

print(height(root))         # 2
print(balance_factor(root)) # 0 (balanced)
```

## Key Point
AVL trees stay balanced so searches stay fast.
