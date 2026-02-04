---
title: Inorder Traversal (Beginner)
tags: [dsa, tree, traversal]
created: 2026-02-04
difficulty: beginner
---

# Inorder Traversal (Beginner)

[[00_Index|← Back to Index]] | [[06_Preorder_Traversal|← Preorder]] | [[08_Postorder_Traversal|Postorder →]]

## Order
**Inorder = Left → Root → Right**

## Example Code
```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = Node(2, Node(1), Node(3))

result = []

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    result.append(node.value)
    inorder(node.right)

inorder(root)
print(result)  # [1, 2, 3]
```
