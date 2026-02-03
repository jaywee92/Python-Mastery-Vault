---
title: "Preorder Traversal (Root → Left → Right)"
category: "Tree Traversals"
difficulty: "Medium"
order: 6
tags: ["tree", "traversal", "dfs", "recursive", "iterative"]
last_updated: "2025-01-30"
---

# Preorder Traversal: Root → Left → Right

## Overview

**Preorder traversal** visits nodes in the sequence: **Root first**, then **Left subtree**, then **Right subtree**. It's one of the three fundamental depth-first search (DFS) strategies for binary trees.

**Key Characteristic:** The root is always processed before its children, making it ideal for copying trees and prefix expressions.

```
Example Tree:
        1
       / \
      2   3
     / \
    4   5

Preorder: 1 → 2 → 4 → 5 → 3
```

---

## ✅ Beginner-Friendly Python Example

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder(node, out):
    if node is None:
        return
    out.append(node.value)      # Root
    preorder(node.left, out)    # Left
    preorder(node.right, out)   # Right

root = Node(1, Node(2), Node(3))
result = []
preorder(root, result)
print(result)  # [1, 2, 3]
```

---

## Concept Visualization

### Traversal Order Diagram

```
         1 (visit 1st)
        / \
       2   3 (visit 4th)
      / \
     4   5
   (visit 2nd)

Step-by-step execution:
1. Visit Node 1 → OUTPUT: [1]
2. Go to Left subtree (Node 2)
3. Visit Node 2 → OUTPUT: [1, 2]
4. Go to Left subtree (Node 4)
5. Visit Node 4 → OUTPUT: [1, 2, 4]
6. Node 4 has no children, backtrack
7. Go to Right subtree (Node 5)
8. Visit Node 5 → OUTPUT: [1, 2, 4, 5]
9. Node 5 has no children, backtrack
10. Go to Right subtree (Node 3)
11. Visit Node 3 → OUTPUT: [1, 2, 4, 5, 3]
```

### Execution Stack Visualization

```
With Recursive Calls:

preorder(1)
├─ process 1 → [1]
├─ preorder(2)
│  ├─ process 2 → [1, 2]
│  ├─ preorder(4)
│  │  ├─ process 4 → [1, 2, 4]
│  │  └─ return
│  └─ preorder(5)
│     ├─ process 5 → [1, 2, 4, 5]
│     └─ return
└─ preorder(3)
   ├─ process 3 → [1, 2, 4, 5, 3]
   └─ return
```

---

## Implementation Approaches

### 1. Recursive Implementation

**Most intuitive and clean approach:**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_recursive(root):
    """
    Recursive preorder traversal.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack depth equals tree height

    Args:
        root: TreeNode or None

    Returns:
        List of values in preorder sequence
    """
    result = []

    def traverse(node):
        if node is None:
            return

        # Process root first
        result.append(node.val)

        # Then process left subtree
        traverse(node.left)

        # Finally process right subtree
        traverse(node.right)

    traverse(root)
    return result


# Usage Example
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(preorder_recursive(root))  # Output: [1, 2, 4, 5, 3]
```

---

### 2. Iterative Implementation (Stack-Based)

**Uses an explicit stack to simulate recursion:**

```python
def preorder_iterative(root):
    """
    Iterative preorder traversal using a stack.

    Time: O(n) - visit each node once
    Space: O(h) - stack space for tree height

    Args:
        root: TreeNode or None

    Returns:
        List of values in preorder sequence
    """
    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        # Pop node and process it
        node = stack.pop()
        result.append(node.val)

        # Push children in REVERSE order (right first, then left)
        # so that left is popped and processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# Usage Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(preorder_iterative(root))  # Output: [1, 2, 4, 5, 3]
```

**Key Point:** Push right child before left child so that left is processed first.

---

### 3. Iterative with Explicit Processing Phase

**Alternative approach - explicitly separate visit and process:**

```python
def preorder_iterative_v2(root):
    """
    Iterative preorder with explicit processing marker.

    Uses a tuple: (node, is_processed) to track whether
    a node has been processed or is being visited.
    """
    if root is None:
        return []

    result = []
    stack = [(root, False)]  # (node, processed_flag)

    while stack:
        node, processed = stack.pop()

        if processed:
            # Node has been visited and children processed
            result.append(node.val)
        else:
            # First visit: push back with processed=True
            # then push children (right first, then left)
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return result
```

---

## Complexity Analysis

### Time Complexity: O(n)
- **Where n** = number of nodes in the tree
- **Why:** Each node is visited exactly once
- No redundant traversals or comparisons

### Space Complexity: O(h)
- **Recursive:** Call stack uses space proportional to height
- **Iterative:** Explicit stack uses space proportional to height
- **Best case:** O(log n) for balanced tree
- **Worst case:** O(n) for skewed tree (linked list shape)

```
Balanced Tree (n=7):        Skewed Tree (n=7):
      1                              1
     / \                              \
    2   3                              2
   / \ / \                              \
  4  5 6  7                              3
                                         \
h = 3, Space = O(3)                       4
Stack max = 3-4 nodes                     \
                                          5
                                          \
h = 7, Space = O(7)                       6
Stack max = 1 node                         \
                                           7
```

---

## Use Cases

### 1. **Copying a Tree**
Creating an identical copy of a tree structure.

```python
def copy_tree(root):
    """
    Create a deep copy of a binary tree using preorder.

    Preorder is ideal because the root is created first,
    then its subtrees can be recursively copied.
    """
    if root is None:
        return None

    # Create new node (process root first)
    new_root = TreeNode(root.val)

    # Copy left subtree
    new_root.left = copy_tree(root.left)

    # Copy right subtree
    new_root.right = copy_tree(root.right)

    return new_root
```

### 2. **Prefix Expression Evaluation**
Converting infix expressions to prefix notation.

```python
"""
Preorder traversal naturally produces prefix expressions:

Infix:   a + b * c  →  Prefix: + a * b c

Expression Tree:
      +
     / \
    a   *
       / \
      b   c

Preorder: + → a → * → b → c = "+ a * b c" (Polish Notation)
"""
```

### 3. **Creating a Tree from Preorder Sequence**
Reconstructing a tree when preorder and inorder are given.

```python
def build_tree_from_preorder_inorder(preorder, inorder):
    """
    Reconstruct binary tree from preorder and inorder traversals.

    Preorder tells us: first element is always root
    Inorder tells us: elements to left are in left subtree,
                     elements to right are in right subtree
    """
    if not preorder or not inorder:
        return None

    # First element in preorder is the root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find root position in inorder
    root_idx = inorder.index(root_val)

    # Elements before root_idx in inorder are in left subtree
    # Elements after root_idx in inorder are in right subtree

    # Recursively build left and right subtrees
    root.left = build_tree_from_preorder_inorder(
        preorder[1:root_idx+1],
        inorder[:root_idx]
    )
    root.right = build_tree_from_preorder_inorder(
        preorder[root_idx+1:],
        inorder[root_idx+1:]
    )

    return root
```

### 4. **Serialization for File/Network Transfer**
Preorder traversal can easily serialize a tree structure.

```python
def serialize_tree(root):
    """
    Serialize tree to string using preorder traversal.
    Useful for saving to file or sending over network.
    """
    def preorder_serialize(node):
        if node is None:
            return ["#"]  # Use "#" to mark null nodes

        return [str(node.val)] + preorder_serialize(node.left) + \
               preorder_serialize(node.right)

    return ",".join(preorder_serialize(root))

# Example: Tree serialized to "1,2,4,#,#,5,#,#,3,#,#"
```

---

## Practical Examples

### Example 1: Simple Tree

```
Tree:
      10
     /  \
    5    15
   / \     \
  3   7    20

Preorder: 10 → 5 → 3 → 7 → 15 → 20
```

**Code:**
```python
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

result = preorder_iterative(root)
print(result)  # [10, 5, 3, 7, 15, 20]
```

### Example 2: Unbalanced Tree

```
Tree:
      1
       \
        2
       /
      3
       \
        4

Preorder: 1 → 2 → 3 → 4
```

**Code:**
```python
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.left.right = TreeNode(4)

result = preorder_recursive(root)
print(result)  # [1, 2, 3, 4]
```

---

## Comparison: Preorder vs Other Traversals

| Traversal | Order | Best Use Case |
|-----------|-------|---------------|
| **Preorder** | Root → Left → Right | Copying trees, prefix expressions |
| Inorder | Left → Root → Right | Sorted BST output |
| Postorder | Left → Right → Root | Deleting trees, postfix expressions |

---

## Exam Checklist

- [ ] Can write recursive preorder traversal from memory
- [ ] Can write iterative preorder using explicit stack
- [ ] Understand why right child is pushed before left child
- [ ] Know time complexity is O(n) and space is O(h)
- [ ] Can identify best/worst case space scenarios
- [ ] Understand use case: tree copying
- [ ] Can solve "Build Tree from Preorder+Inorder" problem
- [ ] Know preorder = prefix notation (Polish notation)
- [ ] Can trace through example by hand
- [ ] Understand difference between recursive/iterative approaches

---

## Quick Reference

```python
# Recursive Template
def preorder(node):
    if not node:
        return
    process(node)           # 1. Process root
    preorder(node.left)     # 2. Traverse left
    preorder(node.right)    # 3. Traverse right

# Iterative Template
def preorder_iter(root):
    stack = [root]
    while stack:
        node = stack.pop()
        process(node)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
```

---

## Related Topics

- [Inorder Traversal](07_Inorder_Traversal.md)
- [Postorder Traversal](08_Postorder_Traversal.md)
- Binary Tree basics
- Depth-First Search (DFS)
- Expression evaluation

---

**Last Updated:** 2025-01-30
**Difficulty:** Medium
**Time to Master:** 1-2 hours
---

## 🎨 Visualization (Optional)

```python
import sys
import site
from pathlib import Path

# Ensure user site-packages are visible (Obsidian runner)
user_site = site.getusersitepackages()
if user_site and user_site not in sys.path:
    sys.path.append(user_site)

# Add vault root to sys.path (Obsidian runner)
# Tries current dir, parent dirs, then a known vault path fallback.
added = False
for p in [Path.cwd(), *Path.cwd().parents]:
    if (p / "DSA_Utils").exists():
        sys.path.append(str(p))
        added = True
        break

if not added:
    fallback = Path("/Users/jochenwahl/Library/CloudStorage/OneDrive-Persönlich/z99_Obsidian_Vault/Codex_Coding")
    if fallback.exists():
        sys.path.append(str(fallback))

from DSA_Utils.utils import draw_tree

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Preorder: 1, 2, 4, 5, 3, 6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

draw_tree(root)

```
