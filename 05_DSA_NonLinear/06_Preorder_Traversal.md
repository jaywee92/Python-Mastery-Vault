---
title: Preorder Traversal (Beginner)
tags: [dsa, tree, traversal]
created: 2026-02-04
difficulty: beginner
---

# Preorder Traversal (Beginner)

[[00_Index|← Back to Index]] | [[05_Binary_Trees|← Binary Trees]] | [[07_Inorder_Traversal|Inorder →]]

## Order
**Preorder = Root → Left → Right**

## Example Code
```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Build a small tree
root = Node("A", Node("B"), Node("C"))

# Preorder traversal
result = []

def preorder(node):
    if node is None:
        return
    # 1) Visit root
    result.append(node.value)
    # 2) Visit left
    preorder(node.left)
    # 3) Visit right
    preorder(node.right)

preorder(root)
print(result)  # ['A', 'B', 'C']
```
