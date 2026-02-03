---
title: Binary Trees
tags: [dsa, binary-tree, bst, complete, perfect, balanced, data-structure]
created: 2026-01-30
difficulty: intermediate
time_complexity: varies
space_complexity: O(n)
---

# 🌲 Binary Trees

[[04_Trees|← Trees]] | [[00_Index|Back to Index]]

> **"Binary trees: Where every node makes a choice - left or right"**

---

## 🎯 The Concept

```
┌─────────────────────────────────────────────────────────────────┐
│                WHAT IS A BINARY TREE?                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A Binary Tree is a tree where each node has AT MOST 2 children │
│  (called left child and right child).                           │
│                                                                  │
│  DEFINITION:                                                     │
│  • Every node has 0, 1, or 2 children                           │
│  • Children are distinguished as LEFT and RIGHT                 │
│  • Still maintains tree properties (acyclic, connected)         │
│                                                                  │
│            SIMPLE BINARY TREE                                   │
│                                                                  │
│                     A                                           │
│                    / \                                          │
│                   B   C                                         │
│                  / \     \                                      │
│                 D   E     F                                     │
│                /                                                │
│               G                                                 │
│                                                                  │
│  Each node has: value, left pointer, right pointer             │
│  (either can be None/NULL)                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✅ Beginner-Friendly Python Example

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)

print(root.value)       # 10
print(root.left.value)  # 5
print(root.right.value) # 15
```

Each node has at most **two** children: `left` and `right`.

---

## 🔄 Binary Tree Node Structure

```python
# ═══════════════════════════════════════════════════════════════
# BINARY TREE NODE
# ═══════════════════════════════════════════════════════════════

class BinaryTreeNode:
    """A node in a binary tree with exactly 2 possible children."""

    def __init__(self, value):
        """Initialize a binary tree node.

        Args:
            value: The data stored in this node
        """
        self.value = value
        self.left = None   # Left child node
        self.right = None  # Right child node

    def set_left(self, node):
        """Set the left child."""
        self.left = node

    def set_right(self, node):
        """Set the right child."""
        self.right = node

    def is_leaf(self):
        """Check if this node is a leaf (no children)."""
        return self.left is None and self.right is None

    def has_left(self):
        """Check if left child exists."""
        return self.left is not None

    def has_right(self):
        """Check if right child exists."""
        return self.right is not None

    def degree(self):
        """Return number of children (0, 1, or 2)."""
        count = 0
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        return count

    def __repr__(self):
        return f"BTNode({self.value})"


# Usage Example
root = BinaryTreeNode(1)
root.set_left(BinaryTreeNode(2))
root.set_right(BinaryTreeNode(3))
root.left.set_left(BinaryTreeNode(4))
root.left.set_right(BinaryTreeNode(5))

#         1
#        / \
#       2   3
#      / \
#     4   5

print(f"Root: {root.value}")
print(f"Root left: {root.left.value}")
print(f"Root right: {root.right.value}")
print(f"Node 2 degree: {root.left.degree()}")  # 2
print(f"Node 3 is leaf: {root.right.is_leaf()}")  # True
```

---

## 🌳 Types of Binary Trees

### 1. Full Binary Tree (Proper Binary Tree)

```
Every node has EITHER 0 or 2 children (no node with just 1 child)

         A
        / \
       B   C
      / \ / \
     D  E F  G

Property: If a tree has n nodes, it has (n+1)/2 leaves
Property: Number of edges = n - 1
Property: Height h → nodes between (2^h) to (2^(h+1) - 1)

Example count:
- 1 node (just root): Full ✓
- 3 nodes: Full ✓
- 5 nodes: Full ✓
- 7 nodes: Full ✓
```

### 2. Complete Binary Tree

```
All levels are completely filled except possibly the last level
Last level is filled from left to right

VALID Complete Binary Trees:

         A                        A
        / \                      / \
       B   C                    B   C
      / \ / \                  / \ / \
     D  E F  G               D  E F  G
                             /
                            H

INVALID (not complete):

         A
        / \
       B   C
      /     \
     D       E  ← Gap! Not filled left to right

Useful for: HEAPS (min-heap, max-heap)
Implementation: Often use array representation
```

### 3. Perfect Binary Tree

```
ALL internal nodes have 2 children & ALL leaves at the same level
(All levels completely filled)

         A
        / \
       B   C
      / \ / \
     D  E F  G

Properties:
- If height h: total nodes = 2^(h+1) - 1
- If n nodes: height = log2(n+1) - 1
- Number of leaves = 2^h
- Number of internal nodes = 2^h - 1

Perfect tree heights:
- Height 0: 1 node (just root)
- Height 1: 3 nodes
- Height 2: 7 nodes
- Height 3: 15 nodes
```

### 4. Balanced Binary Tree

```
For every node, height of left and right subtrees differ by at most 1

BALANCED:                  UNBALANCED:
     A                           A
    / \                         /
   B   C                       B
  / \                         /
 D   E                       C
                            /
                           D

Used in: AVL Trees, Red-Black Trees
Guarantees: Operations in O(log n)
```

---

## 📊 Binary Tree Properties

```
┌─────────────────────────────────────────────────────────────────┐
│                 BINARY TREE PROPERTIES                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PROPERTY 1: Maximum nodes at level i                           │
│  Max nodes at level i = 2^i                                     │
│                                                                  │
│  Example:                                                        │
│    Level 0: 2^0 = 1 node                                        │
│    Level 1: 2^1 = 2 nodes                                       │
│    Level 2: 2^2 = 4 nodes                                       │
│    Level 3: 2^3 = 8 nodes                                       │
│                                                                  │
│  PROPERTY 2: Maximum nodes in tree with height h                │
│  Max nodes = 2^(h+1) - 1                                        │
│                                                                  │
│  Example:                                                        │
│    Height 0 (1 level):     2^1 - 1 = 1 node                    │
│    Height 1 (2 levels):    2^2 - 1 = 3 nodes                   │
│    Height 2 (3 levels):    2^3 - 1 = 7 nodes                   │
│    Height 3 (4 levels):    2^4 - 1 = 15 nodes                  │
│                                                                  │
│  PROPERTY 3: Minimum height with n nodes                        │
│  Min height = ceil(log2(n+1)) - 1  or  floor(log2(n))           │
│                                                                  │
│  Example:                                                        │
│    1 node:   height 0                                           │
│    2-3 nodes: height 1                                          │
│    4-7 nodes: height 2                                          │
│    8-15 nodes: height 3                                         │
│                                                                  │
│  PROPERTY 4: Maximum height with n nodes                        │
│  Max height = n - 1 (completely unbalanced, like linked list)   │
│                                                                  │
│  PROPERTY 5: For complete binary tree with n nodes             │
│  Height = floor(log2(n))                                        │
│                                                                  │
│  PROPERTY 6: Leaf nodes in full binary tree                     │
│  If tree has n nodes → leaf count = (n + 1) / 2                │
│  Internal node count = (n - 1) / 2                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔍 Calculating Tree Properties

```python
# ═══════════════════════════════════════════════════════════════
# CALCULATING BINARY TREE PROPERTIES
# ═══════════════════════════════════════════════════════════════

import math

def get_height(root):
    """Calculate height of binary tree.

    Height = distance from root to furthest leaf
    Leaf node has height 0
    Empty tree has height -1

    Time: O(n)
    Space: O(h) recursion stack
    """
    if root is None:
        return -1

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    return 1 + max(left_height, right_height)


def count_nodes(root):
    """Count total number of nodes in tree.

    Time: O(n)
    Space: O(h)
    """
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_leaves(root):
    """Count number of leaf nodes.

    Time: O(n)
    Space: O(h)
    """
    if root is None:
        return 0

    if root.is_leaf():
        return 1

    return count_leaves(root.left) + count_leaves(root.right)


def count_internal_nodes(root):
    """Count nodes that are not leaves.

    Time: O(n)
    Space: O(h)
    """
    if root is None:
        return 0

    total_nodes = count_nodes(root)
    leaf_nodes = count_leaves(root)

    return total_nodes - leaf_nodes


def is_perfect(root):
    """Check if tree is perfect (all levels completely filled).

    Perfect tree property:
    All levels completely filled = total nodes = 2^(h+1) - 1
    """
    if root is None:
        return True

    h = get_height(root)
    n = count_nodes(root)

    return n == (2 ** (h + 1) - 1)


def is_complete(root):
    """Check if tree is complete.

    Complete tree: All levels full except possibly last level,
    and last level filled left to right.
    """
    if root is None:
        return True

    # Use level-order traversal
    from collections import deque
    queue = deque([root])
    last_node_reached = False

    while queue:
        node = queue.popleft()

        if last_node_reached:
            # If we already found an incomplete node,
            # no more nodes should follow
            return False

        if node.left is not None:
            queue.append(node.left)
        else:
            last_node_reached = True

        if node.right is not None:
            if last_node_reached:
                # Right child exists but left didn't
                return False
            queue.append(node.right)
        else:
            last_node_reached = True

    return True


def is_balanced(root):
    """Check if tree is balanced.

    Balanced: height difference of left and right subtrees ≤ 1
    at every node.

    Time: O(n)
    Space: O(h)
    """
    if root is None:
        return True

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    # Height difference must be ≤ 1
    if abs(left_height - right_height) > 1:
        return False

    # Both subtrees must also be balanced
    return is_balanced(root.left) and is_balanced(root.right)


# Example usage
root = BinaryTreeNode(1)
root.set_left(BinaryTreeNode(2))
root.set_right(BinaryTreeNode(3))
root.left.set_left(BinaryTreeNode(4))
root.left.set_right(BinaryTreeNode(5))

#         1
#        / \
#       2   3
#      / \
#     4   5

print(f"Height: {get_height(root)}")           # 2
print(f"Total nodes: {count_nodes(root)}")     # 5
print(f"Leaf nodes: {count_leaves(root)}")     # 3
print(f"Is perfect: {is_perfect(root)}")       # False
print(f"Is complete: {is_complete(root)}")     # True
print(f"Is balanced: {is_balanced(root)}")     # True
```

---

## 🔄 Binary Tree Traversals

### Level-Order Traversal (BFS - Breadth First Search)

```python
# ═══════════════════════════════════════════════════════════════
# LEVEL-ORDER TRAVERSAL (Breadth-First Search)
# ═══════════════════════════════════════════════════════════════

from collections import deque

def traverse_level_order(root):
    """Visit nodes level by level from top to bottom, left to right.

    Uses: Queue (FIFO)
    Order: All level 0 → all level 1 → all level 2 → ...

    Time: O(n) - visit each node once
    Space: O(w) - w is maximum width (nodes at one level)
    """
    if root is None:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


def traverse_level_order_lines(root):
    """Level-order traversal with level information."""
    if root is None:
        return

    queue = deque([(root, 0)])  # (node, level)
    current_level = 0
    level_values = []

    while queue:
        node, level = queue.popleft()

        if level != current_level:
            print(f"Level {current_level}: {level_values}")
            level_values = []
            current_level = level

        level_values.append(node.value)

        if node.left is not None:
            queue.append((node.left, level + 1))

        if node.right is not None:
            queue.append((node.right, level + 1))

    print(f"Level {current_level}: {level_values}")


# Example:
#         1
#        / \
#       2   3
#      / \
#     4   5

root = BinaryTreeNode(1)
root.set_left(BinaryTreeNode(2))
root.set_right(BinaryTreeNode(3))
root.left.set_left(BinaryTreeNode(4))
root.left.set_right(BinaryTreeNode(5))

print("Level-order: ", end="")
traverse_level_order(root)  # 1 2 3 4 5
print()

print("Level-order with lines:")
traverse_level_order_lines(root)
# Level 0: [1]
# Level 1: [2, 3]
# Level 2: [4, 5]
```

### Depth-First Traversals

```python
# ═══════════════════════════════════════════════════════════════
# DEPTH-FIRST TRAVERSALS (Using Recursion)
# ═══════════════════════════════════════════════════════════════

def traverse_preorder(root):
    """Visit node BEFORE left and right subtrees.

    Order: Node → Left → Right (NLR)
    Uses: Stack (via recursion)

    Time: O(n)
    Space: O(h) recursion stack
    """
    if root is None:
        return

    print(root.value, end=" ")        # Process node first
    traverse_preorder(root.left)      # Then left subtree
    traverse_preorder(root.right)     # Then right subtree


def traverse_inorder(root):
    """Visit node BETWEEN left and right subtrees.

    Order: Left → Node → Right (LNR)
    Uses: Stack (via recursion)

    For BST: gives sorted order!

    Time: O(n)
    Space: O(h)
    """
    if root is None:
        return

    traverse_inorder(root.left)       # Left subtree first
    print(root.value, end=" ")        # Process node
    traverse_inorder(root.right)      # Right subtree last


def traverse_postorder(root):
    """Visit node AFTER left and right subtrees.

    Order: Left → Right → Node (LRN)
    Uses: Stack (via recursion)

    Useful for: deletion, postfix expressions

    Time: O(n)
    Space: O(h)
    """
    if root is None:
        return

    traverse_postorder(root.left)     # Left subtree first
    traverse_postorder(root.right)    # Right subtree second
    print(root.value, end=" ")        # Process node last


# Example tree:
#         1
#        / \
#       2   3
#      / \
#     4   5

root = BinaryTreeNode(1)
root.set_left(BinaryTreeNode(2))
root.set_right(BinaryTreeNode(3))
root.left.set_left(BinaryTreeNode(4))
root.left.set_right(BinaryTreeNode(5))

print("Preorder (NLR):   ", end="")
traverse_preorder(root)    # 1 2 4 5 3
print()

print("Inorder (LNR):    ", end="")
traverse_inorder(root)     # 4 2 5 1 3
print()

print("Postorder (LRN):  ", end="")
traverse_postorder(root)   # 4 5 2 3 1
print()
```

---

## 🔍 Basic Search and Insert

```python
# ═══════════════════════════════════════════════════════════════
# SEARCH AND INSERT IN BINARY TREE
# ═══════════════════════════════════════════════════════════════

def search_binary_tree(root, target):
    """Search for a value in binary tree (unordered).

    Since tree is unordered, must do DFS traversal.

    Time: O(n)
    Space: O(h)
    """
    if root is None:
        return None

    if root.value == target:
        return root

    # Search left subtree
    left_result = search_binary_tree(root.left, target)
    if left_result is not None:
        return left_result

    # Search right subtree
    return search_binary_tree(root.right, target)


def insert_binary_tree(root, value):
    """Insert value into binary tree (no specific ordering).

    Typically: Insert at first available position (level-order)

    Time: O(n) - need to find insertion point
    Space: O(h)
    """
    new_node = BinaryTreeNode(value)

    if root is None:
        return new_node

    # Use level-order to find first empty position
    from collections import deque
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.left is None:
            node.left = new_node
            return root

        if node.right is None:
            node.right = new_node
            return root

        queue.append(node.left)
        queue.append(node.right)

    return root


def delete_binary_tree(root, value):
    """Delete a node from binary tree.

    Replace with last node, then delete last node.

    Time: O(n)
    Space: O(h)
    """
    if root is None:
        return None

    # Find the node to delete
    if root.value == value:
        # Node found - handle deletion
        # If it's a leaf, just return None
        if root.is_leaf():
            return None

        # If it has children, replace with last node
        last_node = find_last_node(root)

        if last_node is None or last_node == root:
            # Only root exists or only one node
            return None

        root.value = last_node.value
        root.right = delete_binary_tree(root.right, last_node.value)

        if root.right is None:
            root.left = delete_binary_tree(root.left, last_node.value)

        return root

    # Recursively find and delete in subtrees
    root.left = delete_binary_tree(root.left, value)
    root.right = delete_binary_tree(root.right, value)

    return root


def find_last_node(root):
    """Find the last node added (rightmost node at last level)."""
    if root is None:
        return None

    from collections import deque
    queue = deque([root])
    last = None

    while queue:
        last = queue.popleft()

        if last.left is not None:
            queue.append(last.left)

        if last.right is not None:
            queue.append(last.right)

    return last


# Example usage
root = None
root = insert_binary_tree(root, 1)
root = insert_binary_tree(root, 2)
root = insert_binary_tree(root, 3)
root = insert_binary_tree(root, 4)
root = insert_binary_tree(root, 5)

#         1
#        / \
#       2   3
#      / \
#     4   5

print("Tree after inserts: ", end="")
traverse_level_order(root)  # 1 2 3 4 5
print()

found = search_binary_tree(root, 4)
print(f"Found 4: {found is not None}")  # True

found = search_binary_tree(root, 10)
print(f"Found 10: {found is not None}")  # False
```

---

## 📊 Time and Space Complexity

```
┌─────────────────────────────────────────────────────────────────┐
│           BINARY TREE OPERATIONS COMPLEXITY                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ Operation        │ Balanced Tree  │ Unbalanced Tree │ Notes      │
│ ─────────────────┼────────────────┼─────────────────┼────────────│
│ Search           │ O(log n)       │ O(n)            │ DFS needed │
│ Insert           │ O(log n)       │ O(n)            │ Find spot  │
│ Delete           │ O(log n)       │ O(n)            │ Complex    │
│ Traversal        │ O(n)           │ O(n)            │ All nodes  │
│ Get Height       │ O(n)           │ O(n)            │ All nodes  │
│ Count Nodes      │ O(n)           │ O(n)            │ All nodes  │
│ ─────────────────┴────────────────┴─────────────────┴────────────│
│ Space (Tree)     │ O(n)           │ O(n)            │ n nodes    │
│ Space (DFS)      │ O(log n)       │ O(n)            │ Recursion  │
│ Space (BFS)      │ O(log n)       │ O(n)            │ Queue size │
│                                                                  │
│ KEY INSIGHT: Balanced trees guarantee O(log n) height!         │
│             Unbalanced trees can degrade to O(n).              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📈 Array Representation

```python
# ═══════════════════════════════════════════════════════════════
# ARRAY REPRESENTATION OF COMPLETE BINARY TREE
# ═══════════════════════════════════════════════════════════════

"""
For a complete binary tree, can use array with implicit pointers:

Index-based positioning:
- Element at index i:
  - Parent: (i - 1) // 2
  - Left child: 2*i + 1
  - Right child: 2*i + 2

Example:
       Tree          Array
         0            [0, 1, 2,
        / \            3, 4, 5]
       1   2
      / \
     3   4

Index:  0  1  2  3  4
Value:  0  1  2  3  4

Node 0: left=2*0+1=1, right=2*0+2=2
Node 1: left=2*1+1=3, right=2*1+2=4
Node 3: left=2*3+1=7 (doesn't exist), right=8 (doesn't exist)

Parent of index 3: (3-1)//2 = 1 ✓
Parent of index 4: (4-1)//2 = 1 ✓
"""

class ArrayBinaryTree:
    """Binary tree implemented using array (implicit structure)."""

    def __init__(self):
        self.tree = []

    def insert(self, value):
        """Insert at next available position (level-order)."""
        self.tree.append(value)

    def parent(self, index):
        """Get parent index."""
        if index == 0:
            return None
        return (index - 1) // 2

    def left_child(self, index):
        """Get left child index."""
        left_idx = 2 * index + 1
        return left_idx if left_idx < len(self.tree) else None

    def right_child(self, index):
        """Get right child index."""
        right_idx = 2 * index + 2
        return right_idx if right_idx < len(self.tree) else None

    def get_value(self, index):
        """Get value at index."""
        return self.tree[index] if index < len(self.tree) else None

    def level_order(self):
        """Traverse level-order."""
        return self.tree

    def height(self):
        """Get height of tree."""
        if not self.tree:
            return -1

        import math
        return math.floor(math.log2(len(self.tree)))


# Example usage
tree = ArrayBinaryTree()
for val in [1, 2, 3, 4, 5]:
    tree.insert(val)

#         1
#        / \
#       2   3
#      / \
#     4   5

print(f"Tree: {tree.level_order()}")  # [1, 2, 3, 4, 5]
print(f"Parent of index 3: {tree.parent(3)}")  # 1 (value 2)
print(f"Left child of index 0: {tree.left_child(0)}")  # 1 (value 2)
print(f"Right child of index 0: {tree.right_child(0)}")  # 2 (value 3)
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Confusing height and depth
def bad_height(node):
    """Incorrectly calculates height."""
    if node is None:
        return 0  # Wrong! Empty tree should be -1
    return 1 + max(get_height(node.left), get_height(node.right))

# ✅ RIGHT: Correct height calculation
def correct_height(node):
    """Correctly calculates height."""
    if node is None:
        return -1  # Empty tree has height -1

    left_h = correct_height(node.left)
    right_h = correct_height(node.right)
    return 1 + max(left_h, right_h)


# ❌ WRONG: Not handling empty tree in traversal
def bad_traversal(root):
    """Crashes on None."""
    print(root.value)  # AttributeError if root is None!
    bad_traversal(root.left)
    bad_traversal(root.right)

# ✅ RIGHT: Check for None first
def good_traversal(root):
    """Handles None properly."""
    if root is None:
        return

    print(root.value)
    good_traversal(root.left)
    good_traversal(root.right)


# ❌ WRONG: Assuming tree is balanced
def bad_complexity_estimate():
    """Assumes all trees are balanced."""
    # "Search is O(log n)"
    # Wrong! Could be O(n) in skewed tree
    pass

# ✅ RIGHT: Consider both cases
def good_complexity_estimate():
    """Considers balance."""
    # Balanced tree: O(log n)
    # Unbalanced tree: O(n)
    # Must verify or enforce balance
    pass


# ❌ WRONG: Modifying tree while traversing
def bad_delete_while_traversing(root):
    """Causes issues."""
    if root is None:
        return

    if root.value < 5:
        del root.left  # Modifying structure!

    bad_delete_while_traversing(root.left)
    bad_delete_while_traversing(root.right)

# ✅ RIGHT: Collect changes, then apply
def good_delete_while_traversing(root):
    """Safer approach."""
    to_delete = []

    # First pass: identify
    def identify(node):
        if node is None:
            return
        if node.value < 5:
            to_delete.append(node)
        identify(node.left)
        identify(node.right)

    identify(root)

    # Second pass: delete
    for node in to_delete:
        # Properly handle deletion
        pass


# ❌ WRONG: Assuming left/right order matters in unordered tree
def bad_search(root, target):
    """Assumes binary search property."""
    if root is None:
        return None

    if root.value == target:
        return root

    if target < root.value:
        return bad_search(root.left, target)  # Wrong!
    else:
        return bad_search(root.right, target)  # Wrong!

# ✅ RIGHT: Search both subtrees
def good_search(root, target):
    """Searches both subtrees."""
    if root is None:
        return None

    if root.value == target:
        return root

    left_result = good_search(root.left, target)
    if left_result is not None:
        return left_result

    return good_search(root.right, target)
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Initialize left and right to None | Forget to initialize children |
| Check for None before accessing | Assume node exists |
| Use proper height definition (-1 for None) | Be inconsistent with height |
| Understand height vs depth | Confuse the two concepts |
| Verify tree is balanced for O(log n) | Assume all trees are balanced |
| Use appropriate traversal for task | Use wrong traversal type |
| Collect changes, apply carefully | Modify while traversing |
| Handle edge cases (empty tree, single node) | Overlook edge cases |
| Document tree invariants | Leave structure ambiguous |
| Test with unbalanced trees | Only test balanced cases |

---

## 🎯 Exam Checklist

- [ ] Binary tree: each node has 0, 1, or 2 children
- [ ] Left child and right child are distinguished
- [ ] Full binary tree: every node has 0 or 2 children
- [ ] Complete binary tree: all levels full except possibly last level, last level filled left-to-right
- [ ] Perfect binary tree: all levels completely filled
- [ ] Balanced binary tree: height difference of left and right subtrees ≤ 1 at every node
- [ ] Maximum nodes at level i = 2^i
- [ ] Maximum total nodes with height h = 2^(h+1) - 1
- [ ] Minimum height with n nodes = ceil(log2(n+1)) - 1
- [ ] Height of leaf node = 0
- [ ] Height of empty tree = -1
- [ ] Preorder (NLR): node → left → right
- [ ] Inorder (LNR): left → node → right
- [ ] Postorder (LRN): left → right → node
- [ ] Level-order (BFS): level by level, left to right
- [ ] Balanced tree operations: O(log n) time
- [ ] Unbalanced tree operations: O(n) time
- [ ] BinaryTreeNode: value, left pointer, right pointer
- [ ] Array representation: parent at (i-1)//2, left at 2i+1, right at 2i+2
- [ ] Search in unordered tree: must check both subtrees
- [ ] DFS uses recursion stack: O(h) space
- [ ] BFS uses queue: O(width) space, w can be O(n) for unbalanced

---

[[04_Trees|← Trees]] | [[00_Index|Back to Index]]
---

## 🎨 Visualization (Optional)

```python
import sys
import site
from pathlib import Path

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

draw_tree(root)
```
