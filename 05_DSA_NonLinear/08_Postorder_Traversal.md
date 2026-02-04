---
title: Postorder Traversal (Beginner)
tags: [dsa, tree, traversal]
created: 2026-02-04
difficulty: beginner
---

# Postorder Traversal (Beginner)

[[00_Index|← Back to Index]] | [[07_Inorder_Traversal|← Inorder]] | [[09_Binary_Search_Trees|BST →]]

## Order
**Postorder = Left → Right → Root**

## Example Code
```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = Node("A", Node("B"), Node("C"))

result = []

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    result.append(node.value)

postorder(root)
print(result)  # ['B', 'C', 'A']
```
