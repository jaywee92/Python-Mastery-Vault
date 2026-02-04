---
title: Trees (Beginner)
tags: [dsa, trees]
created: 2026-02-04
difficulty: beginner
---

# Trees (Beginner)

[[00_Index|← Back to Index]] | [[03_Hash_Maps|← Hash Maps]] | [[05_Binary_Trees|Binary Trees →]]

## What it is
A tree is a structure of **nodes** connected in a parent → child way.
The top node is the **root**.

## Simple Tree Example
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

# Build a tiny tree
root = Node("A")
child1 = Node("B")
child2 = Node("C")
root.children.append(child1)
root.children.append(child2)

print(root.value)         # A
print(root.children[0].value)  # B
```

## Key Points
- Trees can have many children per node
- Used for menus, folder structures, and more
