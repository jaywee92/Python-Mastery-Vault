---
title: "Inorder Traversal (Left → Root → Right)"
category: "Tree Traversals"
difficulty: "Medium"
order: 7
tags: ["tree", "traversal", "dfs", "recursive", "iterative", "bst", "sorted"]
last_updated: "2025-01-30"
---

# Inorder Traversal: Left → Root → Right

## Overview

**Inorder traversal** visits nodes in the sequence: **Left subtree first**, then **Root**, then **Right subtree**. It's the second of three fundamental depth-first search (DFS) strategies for binary trees.

**Key Characteristic:** When applied to a Binary Search Tree (BST), inorder traversal produces values in **sorted ascending order**. This property makes it extremely valuable for BST operations.

```
Example Tree:
        2
       / \
      1   3

Inorder: 1 → 2 → 3  (Sorted!)
```

---

## ✅ Beginner-Friendly Python Example

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder(node, out):
    if node is None:
        return
    inorder(node.left, out)     # Left
    out.append(node.value)      # Root
    inorder(node.right, out)    # Right

root = Node(2, Node(1), Node(3))
result = []
inorder(root, result)
print(result)  # [1, 2, 3]
```

---

## Concept Visualization

### Traversal Order Diagram

```
         1
        / \
       2   3
      / \
     4   5

Step-by-step:
1. Start at 1, go left to 2
2. From 2, go left to 4
3. Visit 4 (leaf) → OUTPUT: [4]
4. Backtrack to 2
5. Visit 2 → OUTPUT: [4, 2]
6. Go right to 5
7. Visit 5 → OUTPUT: [4, 2, 5]
8. Backtrack to 1
9. Visit 1 → OUTPUT: [4, 2, 5, 1]
10. Go right to 3
11. Visit 3 → OUTPUT: [4, 2, 5, 1, 3]

Inorder: 4 → 2 → 5 → 1 → 3
```

### BST Example (Sorted Output!)

```
BST:
       5
      / \
     3   8
    / \ / \
   1  4 6  9

Inorder: 1 → 3 → 4 → 5 → 6 → 8 → 9
         ↑ ↑ ↑ ↑ ↑ ↑ ↑
      SORTED!

This is the KEY property of BST inorder traversal!
```

### Execution Stack Visualization

```
With Recursive Calls:

inorder(5)
├─ inorder(3)
│  ├─ inorder(1)
│  │  ├─ inorder(null) → return
│  │  ├─ process 1 → [1]
│  │  └─ inorder(null) → return
│  ├─ process 3 → [1, 3]
│  └─ inorder(4)
│     ├─ inorder(null) → return
│     ├─ process 4 → [1, 3, 4]
│     └─ inorder(null) → return
├─ process 5 → [1, 3, 4, 5]
└─ inorder(8)
   ├─ inorder(6)
   │  ├─ inorder(null) → return
   │  ├─ process 6 → [1, 3, 4, 5, 6]
   │  └─ inorder(null) → return
   ├─ process 8 → [1, 3, 4, 5, 6, 8]
   └─ inorder(9)
      ├─ inorder(null) → return
      ├─ process 9 → [1, 3, 4, 5, 6, 8, 9]
      └─ inorder(null) → return
```

---

## Implementation Approaches

### 1. Recursive Implementation

**Simplest and most intuitive:**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_recursive(root):
    """
    Recursive inorder traversal.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack depth equals tree height

    Args:
        root: TreeNode or None

    Returns:
        List of values in inorder sequence
    """
    result = []

    def traverse(node):
        if node is None:
            return

        # Process left subtree first
        traverse(node.left)

        # Then process root
        result.append(node.val)

        # Finally process right subtree
        traverse(node.right)

    traverse(root)
    return result


# Usage Example: BST
#       5
#      / \
#     3   8
#    / \ / \
#   1  4 6  9

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(inorder_recursive(root))  # Output: [1, 3, 4, 5, 6, 8, 9]
```

---

### 2. Iterative Implementation (Stack-Based)

**Uses an explicit stack to simulate recursion:**

```python
def inorder_iterative(root):
    """
    Iterative inorder traversal using a stack.

    Algorithm:
    1. Go to the leftmost node
    2. Pop a node, process it
    3. Go to its right child
    4. Repeat

    Time: O(n)
    Space: O(h)

    Args:
        root: TreeNode or None

    Returns:
        List of values in inorder sequence
    """
    result = []
    stack = []
    current = root

    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Current is None, pop from stack
        current = stack.pop()

        # Process the node
        result.append(current.val)

        # Visit right subtree
        current = current.right

    return result


# Usage Example
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(inorder_iterative(root))  # Output: [1, 3, 4, 5, 6, 8, 9]
```

**How it works:**
```
Steps for BST above:
1. current=5, stack=[]
2. Go left: current=3, stack=[5]
3. Go left: current=1, stack=[5,3]
4. Go left: current=None, stack=[5,3,1]
5. Pop 1, process, current=1.right=None → result=[1]
6. Pop 3, process, current=3.right=4 → result=[1,3]
7. Go left: current=None, stack=[5,4]
8. Pop 4, process, current=4.right=None → result=[1,3,4]
9. Pop 5, process, current=5.right=8 → result=[1,3,4,5]
10. Continue...
```

---

### 3. Morris Inorder Traversal (Advanced)

**Space-efficient O(1) space traversal using thread pointers:**

```python
def inorder_morris(root):
    """
    Morris inorder traversal - O(1) space complexity!

    Idea: Use right pointers of leaf nodes as "threads" to point
    back to their in-order successor (or parent).

    Algorithm:
    1. If left child exists, find rightmost node in left subtree
    2. Make it point to current node (thread it)
    3. Move to left child
    4. If no left child, process current and go right
    5. If already threaded (detecting a revisit), process and unthread

    Time: O(n)
    Space: O(1) - no recursion, no auxiliary stack!

    This is optimal for space-constrained scenarios.
    """
    result = []
    current = root

    while current:
        if current.left is None:
            # No left child: process current, go right
            result.append(current.val)
            current = current.right
        else:
            # Find rightmost node in left subtree
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                # First visit: thread the predecessor to current
                predecessor.right = current
                current = current.left
            else:
                # Second visit (from threading): process and unthread
                result.append(current.val)
                predecessor.right = None  # Remove the thread
                current = current.right

    return result


# Usage Example
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)

print(inorder_morris(root))  # Output: [1, 3, 4, 5, 8]

# Morris traversal is SPACE OPTIMAL but more complex
# Use when space is critical (embedded systems, large trees)
```

**Morris Traversal Visualization:**

```
Step 1: Current=5, no left → process 5, go right
Step 2: Current=3, has left
        Find predecessor (rightmost of left subtree) = 4
        4.right = None, so thread it: 4.right = 3
        Go to left = 3
Step 3: Current=3, has left
        Find predecessor = 1
        1.right = None, so thread it: 1.right = 3
        Go to left = 1
Step 4: Current=1, no left → process 1, go right (which is threaded to 3)
Step 5: Current=3, no left → process 3, go right (which is threaded to 5)
Step 6: Current=5 again, but now 3.left = already visited
        So process 5, go right = 8
```

---

## Complexity Analysis

### Time Complexity: O(n)
- **Where n** = number of nodes in the tree
- **Why:** Each node is visited exactly once
- All three approaches (recursive, iterative, Morris) are O(n)

### Space Complexity

| Approach | Space | Notes |
|----------|-------|-------|
| Recursive | O(h) | Call stack depth = tree height |
| Iterative | O(h) | Explicit stack size = tree height |
| Morris | O(1) | Thread-based, no extra space! |

```
Balanced Tree:      Skewed Tree:
    1                    1
   / \                    \
  2   3                    2
 / \ / \                    \
4  5 6  7                    3

h = 3                    h = 7
O(3) space           O(7) space
Best approach        Morris better
```

---

## The Key Property: BST Sorted Output

### Why Inorder on BST Gives Sorted Order

```
BST Property:
- All values in LEFT subtree < Node value
- All values in RIGHT subtree > Node value

Inorder visits:
1. LEFT subtree (all smaller values)
2. Current node
3. RIGHT subtree (all larger values)

Result: Sorted order!
```

### Practical Use: Validate BST

```python
def is_valid_bst(root):
    """
    Validate if a tree is a valid BST using inorder traversal.

    In a valid BST, inorder traversal produces strictly increasing sequence.
    """
    def inorder_validate(node):
        if not node:
            return True, float('-inf')

        # Check left subtree
        is_valid, prev = inorder_validate(node.left)
        if not is_valid:
            return False, prev

        # Check current node
        if node.val <= prev:
            return False, prev

        # Check right subtree
        is_valid, prev = inorder_validate(node.right)
        return is_valid, prev

    is_valid, _ = inorder_validate(root)
    return is_valid
```

---

## Use Cases

### 1. **Get BST in Sorted Order**

```python
def get_sorted_bst_values(root):
    """
    Return all BST values in sorted order.

    This is the #1 use case for inorder traversal!
    """
    result = []
    current = root

    while current:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                result.append(current.val)
                predecessor.right = None
                current = current.right

    return result

# For BST with values [5,3,8,1,4,6,9]
# Returns [1, 3, 4, 5, 6, 8, 9]
```

### 2. **Find kth Smallest Element in BST**

```python
def kth_smallest(root, k):
    """
    Find kth smallest element in BST using inorder.

    Strategy: Do inorder traversal, count nodes until we reach kth
    """
    result = []
    current = root
    count = 0

    while current:
        if current.left is None:
            count += 1
            if count == k:
                return current.val
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                count += 1
                if count == k:
                    return current.val
                predecessor.right = None
                current = current.right

    return -1  # k is out of range


# For BST [3,1,4,null,2] with k=1, returns 1
# Inorder: 1, 2, 3, 4
```

### 3. **Convert BST to Sorted Array**

```python
def bst_to_sorted_array(root):
    """
    Convert entire BST to sorted array using inorder.
    """
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    return inorder(root)
```

### 4. **Range Sum in BST**

```python
def range_sum_bst(root, low, high):
    """
    Sum all values in BST within [low, high] range.

    Use inorder to process nodes in order, skip out-of-range subtrees.
    """
    def inorder_range(node):
        if not node:
            return 0

        # Skip left subtree if all values there are < low
        left_sum = inorder_range(node.left) if node.val > low else 0

        # Skip right subtree if all values there are > high
        right_sum = inorder_range(node.right) if node.val < high else 0

        # Add current if in range
        current_sum = node.val if low <= node.val <= high else 0

        return left_sum + current_sum + right_sum

    return inorder_range(root)
```

---

## Practical Examples

### Example 1: Validate BST

```python
#       5
#      / \
#     3   8
#    / \ / \
#   1  4 6  9

root = TreeNode(5)
# ... setup tree ...

inorder_values = inorder_recursive(root)
print(inorder_values)  # [1, 3, 4, 5, 6, 8, 9] ✓ Sorted!
is_valid = all(inorder_values[i] < inorder_values[i+1]
               for i in range(len(inorder_values)-1))
print(is_valid)  # True - Valid BST
```

### Example 2: Morris Traversal Efficiency

```python
# For large BST with millions of nodes
# Recursive inorder: ~recursion_depth MB of stack memory
# Iterative inorder: ~tree_height MB of stack memory
# Morris inorder: ~0 MB extra memory (just pointers!)

# For tree height of 20+ levels, Morris is significantly better
```

---

## Comparison: All Three Traversals

| Traversal | Order | Best Use Case | Space |
|-----------|-------|---------------|-------|
| Preorder | Root → Left → Right | Copy tree, prefix expr | O(h) |
| **Inorder** | **Left → Root → Right** | **BST sorted, validation** | **O(h)** |
| Postorder | Left → Right → Root | Delete tree, postfix expr | O(h) |
| Morris-Inorder | Left → Root → Right | Memory-constrained | **O(1)!** |

---

## Interview Tips

1. **Always mention the sorted property for BST!**
2. **Know all three implementations:** recursive, iterative, Morris
3. **Morris traversal impresses interviewers** (O(1) space)
4. **Can validate BST using inorder** - no extra space needed
5. **Recognize BST problems** that benefit from inorder's sorted output

---

## Exam Checklist

- [ ] Can write recursive inorder from memory
- [ ] Can write iterative inorder with explicit stack
- [ ] Understand the "go left, process, go right" pattern
- [ ] Know the KEY property: BST inorder = sorted
- [ ] Can explain why BST inorder is sorted
- [ ] Know Morris traversal O(1) space concept
- [ ] Can trace iterative algorithm step-by-step
- [ ] Understand when to use Morris vs regular inorder
- [ ] Can solve "kth smallest in BST" problem
- [ ] Can validate BST using inorder
- [ ] Know time/space complexity for all approaches

---

## Quick Reference

```python
# Recursive Template
def inorder(node):
    if not node:
        return
    inorder(node.left)      # 1. Process left
    process(node)           # 2. Process root
    inorder(node.right)     # 3. Process right

# Iterative Template
def inorder_iter(root):
    stack, current = [], root
    while current or stack:
        while current:      # Go to leftmost
            stack.append(current)
            current = current.left
        current = stack.pop()
        process(current)    # Process after reaching leftmost
        current = current.right

# Morris Template
def inorder_morris(root):
    current = root
    while current:
        if not current.left:
            process(current)
            current = current.right
        else:
            pred = current.left
            while pred.right and pred.right != current:
                pred = pred.right
            if not pred.right:
                pred.right = current
                current = current.left
            else:
                process(current)
                pred.right = None
                current = current.right
```

---

## Related Topics

- [Preorder Traversal](06_Preorder_Traversal.md)
- [Postorder Traversal](08_Postorder_Traversal.md)
- Binary Search Trees (BST)
- Depth-First Search (DFS)
- Level-order traversal (BFS)

---

**Last Updated:** 2025-01-30
**Difficulty:** Medium
**Key Insight:** Inorder of BST = Sorted Order
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

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

draw_tree(root)
```

```python
import matplotlib
print(matplotlib.__version__)
```
