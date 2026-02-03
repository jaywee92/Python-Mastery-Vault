---
title: "Postorder Traversal (Left → Right → Root)"
category: "Tree Traversals"
difficulty: "Medium"
order: 8
tags: ["tree", "traversal", "dfs", "recursive", "iterative", "deletion", "postfix"]
last_updated: "2025-01-30"
---

# Postorder Traversal: Left → Right → Root

## Overview

**Postorder traversal** visits nodes in the sequence: **Left subtree first**, then **Right subtree**, then **Root last**. It's the third of three fundamental depth-first search (DFS) strategies for binary trees.

**Key Characteristic:** The root is always processed after its children, making it ideal for deleting trees and postfix expressions. Children must be processed before their parent.

```
Example Tree:
        1
       / \
      2   3
     / \
    4   5

Postorder: 4 → 5 → 2 → 3 → 1
           (child processing completes before parent)
```

---

## ✅ Beginner-Friendly Python Example

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def postorder(node, out):
    if node is None:
        return
    postorder(node.left, out)   # Left
    postorder(node.right, out)  # Right
    out.append(node.value)      # Root

root = Node(1, Node(2), Node(3))
result = []
postorder(root, result)
print(result)  # [2, 3, 1]
```

---

## Concept Visualization

### Traversal Order Diagram

```
         1 (visit last)
        / \
       2   3 (visit 2nd)
      / \
     4   5
  (visit 1st, 2nd)

Step-by-step execution:
1. Start at 1, go left to 2
2. Go left to 4
3. Visit 4 (no children) → OUTPUT: [4]
4. Backtrack to 2
5. Go right to 5
6. Visit 5 (no children) → OUTPUT: [4, 5]
7. Backtrack to 2
8. Visit 2 (both children processed) → OUTPUT: [4, 5, 2]
9. Backtrack to 1
10. Go right to 3
11. Visit 3 (no children) → OUTPUT: [4, 5, 2, 3]
12. Backtrack to 1
13. Visit 1 (all children processed) → OUTPUT: [4, 5, 2, 3, 1]

KEY: Node 1 visited AFTER all descendants!
```

### Why Postorder for Deletion

```
Tree to delete:
       1
      / \
     2   3
    / \
   4   5

Postorder processing:
1. Process node 4 (no children) → delete 4
2. Process node 5 (no children) → delete 5
3. Process node 2 (children already deleted) → delete 2
4. Process node 3 (no children) → delete 3
5. Process node 1 (all children deleted) → delete 1

SAFE! Children are deleted before parents.
If we deleted parent first, we'd lose reference to children!
```

### Execution Stack Visualization

```
With Recursive Calls:

postorder(1)
├─ postorder(2)
│  ├─ postorder(4)
│  │  ├─ postorder(null) → return
│  │  ├─ postorder(null) → return
│  │  └─ process 4 → [4]
│  ├─ postorder(5)
│  │  ├─ postorder(null) → return
│  │  ├─ postorder(null) → return
│  │  └─ process 5 → [4, 5]
│  └─ process 2 → [4, 5, 2]
├─ postorder(3)
│  ├─ postorder(null) → return
│  ├─ postorder(null) → return
│  └─ process 3 → [4, 5, 2, 3]
└─ process 1 → [4, 5, 2, 3, 1]

Notice: 1 processed LAST
```

---

## Implementation Approaches

### 1. Recursive Implementation

**Most intuitive and natural approach:**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_recursive(root):
    """
    Recursive postorder traversal.

    Time: O(n) - visit each node once
    Space: O(h) - recursion stack depth equals tree height

    Args:
        root: TreeNode or None

    Returns:
        List of values in postorder sequence
    """
    result = []

    def traverse(node):
        if node is None:
            return

        # Process left subtree first
        traverse(node.left)

        # Then process right subtree
        traverse(node.right)

        # Finally process root (after both children)
        result.append(node.val)

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

print(postorder_recursive(root))  # Output: [4, 5, 2, 3, 1]
```

---

### 2. Iterative Implementation (Two Stack Approach)

**Uses two stacks to manage traversal:**

```python
def postorder_iterative_two_stack(root):
    """
    Iterative postorder traversal using two stacks.

    Algorithm:
    1. Push root to first stack
    2. While first stack not empty:
       - Pop from first stack, push to second stack
       - Push left and right children to first stack
    3. Pop from second stack (gives postorder)

    Time: O(n)
    Space: O(h)
    """
    if root is None:
        return []

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        # Push left and right to stack1
        # (opposite of preorder)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    # Pop from stack2 for postorder
    result = []
    while stack2:
        result.append(stack2.pop().val)

    return result


# Usage Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(postorder_iterative_two_stack(root))  # Output: [4, 5, 2, 3, 1]
```

**How it works:**
```
Tree:      1
          / \
         2   3
        / \

Stack1 = [1]    Stack2 = []

Iteration 1:
  Pop 1 from Stack1 → Stack2 = [1]
  Push left(2), right(3) → Stack1 = [2, 3]

Iteration 2:
  Pop 3 from Stack1 → Stack2 = [1, 3]
  Push nothing (no children) → Stack1 = [2]

Iteration 3:
  Pop 2 from Stack1 → Stack2 = [1, 3, 2]
  Push left(4), right(5) → Stack1 = [4, 5]

Iteration 4:
  Pop 5 from Stack1 → Stack2 = [1, 3, 2, 5]
  Push nothing → Stack1 = [4]

Iteration 5:
  Pop 4 from Stack1 → Stack2 = [1, 3, 2, 5, 4]
  Push nothing → Stack1 = []

Final: Pop Stack2 in reverse: [4, 5, 2, 3, 1] ✓
```

---

### 3. Iterative Implementation (One Stack with Tracking)

**More memory-efficient single stack approach:**

```python
def postorder_iterative_one_stack(root):
    """
    Iterative postorder traversal using ONE stack with tracking.

    Uses a tuple (node, visited_children) to track if a node's
    children have been processed.

    Time: O(n)
    Space: O(h)
    """
    if root is None:
        return []

    result = []
    stack = [(root, False)]  # (node, children_processed)

    while stack:
        node, children_processed = stack.pop()

        if children_processed:
            # Both children have been processed
            result.append(node.val)
        else:
            # First visit: push back with flag set, then push children
            stack.append((node, True))
            # Push right first, then left (so left is processed first)
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return result


# Usage Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(postorder_iterative_one_stack(root))  # Output: [4, 5, 2, 3, 1]
```

**How it works:**
```
Stack = [(1, False)]

Process (1, False):
  Not processed yet, push (1, True), then children
  Stack = [(1, True), (3, False), (2, False)]

Process (2, False):
  Not processed yet, push (2, True), then children
  Stack = [(1, True), (3, False), (2, True), (5, False), (4, False)]

Process (4, False):
  Not processed yet, push (4, True), no children
  Stack = [(1, True), (3, False), (2, True), (5, False), (4, True)]

Process (4, True):
  Processed! Output 4
  Stack = [(1, True), (3, False), (2, True), (5, False)]

... continue similarly ...

Final output: [4, 5, 2, 3, 1]
```

---

### 4. Single Stack (Clever Solution)

**Most elegant single-stack approach:**

```python
def postorder_iterative_elegant(root):
    """
    Single stack postorder using prev pointer.

    Keep track of previously processed node to determine
    if we should process current node or continue recursing.
    """
    if root is None:
        return []

    result = []
    stack = [root]
    prev = None

    while stack:
        current = stack[-1]  # Peek at top

        # If current is leaf or both children processed
        if current.left is None and current.right is None:
            result.append(current.val)
            stack.pop()
            prev = current
        elif prev and (prev == current.left or prev == current.right):
            # We're coming back from a child
            result.append(current.val)
            stack.pop()
            prev = current
        else:
            # Going down: push right then left (for proper order)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    return result


# Usage Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(postorder_iterative_elegant(root))  # Output: [4, 5, 2, 3, 1]
```

---

## Complexity Analysis

### Time Complexity: O(n)
- **Where n** = number of nodes in the tree
- **Why:** Each node is visited exactly once
- All implementations achieve O(n) time

### Space Complexity: O(h)
- **Recursive:** Call stack = tree height
- **Two-stack iterative:** Both stacks = O(n) worst case but O(h) average
- **One-stack with tracking:** Explicit stack = O(h)
- **Single stack elegant:** Explicit stack = O(h)

```
Space Usage by Implementation:

Recursive:     O(h) - call stack
Two-stack:     O(n) worst - but more intuitive
One-stack:     O(h) - optimal for iterative
Elegant:       O(h) - most elegant solution

For large trees:
- Recursive at limit for depth
- Two-stack uses more memory
- One-stack elegant is best overall
```

---

## Use Cases

### 1. **Delete Entire Tree**

```python
def delete_tree(root):
    """
    Safely delete entire tree using postorder traversal.

    Postorder ensures children are deleted before parent.
    """
    if root is None:
        return

    # Process left subtree
    delete_tree(root.left)

    # Process right subtree
    delete_tree(root.right)

    # Finally delete current node
    # (In Python, just remove reference; in C++/Java, call delete)
    del root

    return None


# Example: Clean up after using tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root = delete_tree(root)  # root is now None
print(root)  # None
```

**Why postorder for deletion?**
```
If we used preorder (delete parent first):
    1
   / \
  2   3

Delete 1 first → lose reference to 2 and 3!
Memory leak!

Postorder (delete children first):
Delete 2 (no children) ✓
Delete 3 (no children) ✓
Delete 1 (children already gone) ✓
Safe!
```

### 2. **Postfix Expression Evaluation**

```python
"""
Postorder traversal naturally produces postfix (Reverse Polish) notation:

Infix:   a + b * c  →  Postfix: a b c * +

Expression Tree:
      +
     / \
    a   *
       / \
      b   c

Postorder: a → b → c → * → +
         "a b c * +" (Polish Reverse Notation)

Postfix evaluation is easy:
- Stack-based
- Operators work on most recent operands
- No precedence needed
"""

def postfix_evaluate(postfix_expr):
    """
    Evaluate postfix expression.
    """
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in postfix_expr:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack[0]

# Example: "5 3 +" = 5 + 3 = 8
print(postfix_evaluate(['5', '3', '+']))  # 8

# Tree traversal to postfix:
# Expression tree postorder → postfix expression → evaluate
```

### 3. **Calculate Tree Height**

```python
def tree_height(root):
    """
    Calculate height of tree using postorder.

    Height is only known AFTER processing children.
    This requires postorder (process children first).
    """
    if root is None:
        return 0

    # Process left and right subtrees first
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    # Then combine results for current node
    return 1 + max(left_height, right_height)


# Example Tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(tree_height(root))  # 3
```

### 4. **Calculate Tree Size/Node Count**

```python
def tree_size(root):
    """
    Count total nodes in tree using postorder.

    Size calculation requires processing children first.
    """
    if root is None:
        return 0

    # Get sizes of left and right subtrees first
    left_size = tree_size(root.left)
    right_size = tree_size(root.right)

    # Combine: 1 (current) + left + right
    return 1 + left_size + right_size


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(tree_size(root))  # 4 nodes
```

### 5. **Lowest Common Ancestor (LCA)**

```python
def lowest_common_ancestor(root, p, q):
    """
    Find LCA of nodes p and q using postorder.

    Must process both subtrees first (bottom-up) to know
    if p or q exist in each subtree.
    """
    if root is None:
        return None

    # If either p or q is current node
    if root == p or root == q:
        return root

    # Recursively find in left and right
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # Combine results (this is the postorder processing)
    if left and right:
        # Both found in different subtrees
        return root
    elif left:
        # Both found in left subtree
        return left
    else:
        # Both found in right subtree (or both None)
        return right


# Example: Find LCA of nodes 4 and 5
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

lca = lowest_common_ancestor(root, root.left.left, root.left.right)
print(lca.val)  # 2
```

---

## Practical Examples

### Example 1: Delete Binary Tree

```python
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

# Traverse to get order of deletion
deletion_order = postorder_recursive(root)
print(deletion_order)  # [4, 5, 2, 3, 1]

# Safe to delete in this order
root = delete_tree(root)
print(root)  # None
```

### Example 2: Tree Height

```
Balanced Tree:
       1           height = 2
      / \
     2   3

Skewed Tree:
     1              height = 3
      \
       2
        \
         3

For height calculation:
- Must know children's heights first
- Must process bottom-up
- Postorder required!
```

---

## Comparison: All Three Traversals

| Traversal | Order | Best Use Case | Why |
|-----------|-------|---------------|-----|
| Preorder | Root → Left → Right | Copy tree | Root needed first |
| Inorder | Left → Root → Right | BST sorted | Root in middle |
| **Postorder** | **Left → Right → Root** | **Delete tree, height** | **Children before parent** |

---

## Interview Tips

1. **Postorder = "Clean-up" traversal** - good for deletion, cleanup
2. **Always explain why postorder for deletion:** parent depends on children being gone
3. **Recursive postorder is simplest** - most interviewers ask for this
4. **Know at least one iterative version** - shows deeper understanding
5. **Recognize postorder problems:** height, size, deletion, LCA

---

## Exam Checklist

- [ ] Can write recursive postorder from memory
- [ ] Can write iterative postorder (at least one approach)
- [ ] Understand why postorder processes children before parents
- [ ] Know best use case: deleting trees safely
- [ ] Can explain why preorder deletion would fail
- [ ] Know postorder = postfix notation for expression trees
- [ ] Can calculate tree height using postorder
- [ ] Can count tree nodes using postorder
- [ ] Understand all three implementations (two-stack, one-stack, elegant)
- [ ] Can trace iterative algorithm step-by-step
- [ ] Know time O(n) and space O(h) complexity
- [ ] Can solve LCA problem using postorder

---

## Quick Reference

```python
# Recursive Template (SIMPLEST)
def postorder(node):
    if not node:
        return
    postorder(node.left)      # 1. Process left
    postorder(node.right)     # 2. Process right
    process(node)             # 3. Process root LAST

# Iterative Two-Stack Template
def postorder_iter_two_stack(root):
    stack1, stack2 = [root], []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left: stack1.append(node.left)
        if node.right: stack1.append(node.right)
    return [stack2.pop().val for _ in range(len(stack2))]

# One-Stack with Tracking Template
def postorder_iter_one_stack(root):
    result, stack = [], [(root, False)]
    while stack:
        node, processed = stack.pop()
        if processed:
            result.append(node.val)
        else:
            stack.append((node, True))
            if node.right: stack.append((node.right, False))
            if node.left: stack.append((node.left, False))
    return result
```

---

## Related Topics

- [Preorder Traversal](06_Preorder_Traversal.md)
- [Inorder Traversal](07_Inorder_Traversal.md)
- Binary Trees
- Depth-First Search (DFS)
- Tree deletion patterns
- Expression evaluation

---

**Last Updated:** 2025-01-30
**Difficulty:** Medium
**Key Insight:** Postorder processes children before parents
**Best Use Case:** Tree deletion and cleanup operations
**Time to Master:** 1-2 hours
---

## 🎨 Visualization (Optional)

```python
import sys
from pathlib import Path

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

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

draw_tree(root)
```
