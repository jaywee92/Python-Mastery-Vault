---
title: Binary Search Trees (BST)
description: Complete guide to Binary Search Trees with properties, operations, and implementations
category: Non-Linear Data Structures
difficulty: Intermediate
estimated_time: 45 minutes
prerequisites: ["Trees (basics)", "Recursion"]
tags: ["BST", "Search Trees", "Self-Balancing Trees", "Binary Trees"]
---

# Binary Search Trees (BST)

## 🎨 Visual Memory Aid

```
╔═════════════════════════════════════════════════════════════════╗
║     🔍 BINARY SEARCH TREE - ORDERED BINARY TREE                ║
╠═════════════════════════════════════════════════════════════════╣
║                                                                 ║
║   BST PROPERTY: Left < Node < Right (recursively!)             ║
║                                                                 ║
║                        [10]                                     ║
║                       /    \                                    ║
║                      /      \                                   ║
║                    [5]      [15]                                ║
║                   /  \      /   \                               ║
║                 [3]  [7]  [12] [20]                             ║
║                                                                 ║
║   VALIDATION:                                                  ║
║   Left subtree:  3, 5, 7  ─ all < 10  ✓                        ║
║   Right subtree: 12, 15, 20 ─ all > 10 ✓                       ║
║                                                                 ║
║   SEARCH PROCESS (looking for 7):                              ║
║   Start [10]: 7 < 10, go LEFT                                  ║
║   Visit [5]:  7 > 5,  go RIGHT                                 ║
║   Visit [7]:  FOUND! ← Direct path (no searching all nodes)    ║
║                                                                 ║
║   INORDER TRAVERSAL: 3 → 5 → 7 → 10 → 12 → 15 → 20 (SORTED!)  ║
║                                                                 ║
║   OPERATIONS:                                                  ║
║   • SEARCH: O(log n) average, O(n) worst (unbalanced)          ║
║   • INSERT: Compare and place recursively                      ║
║   • DELETE: Replace with successor/predecessor                 ║
║   • MIN/MAX: Go LEFT/RIGHT until leaf                          ║
║                                                                 ║
║   💡 KEY: Order enables fast searching via elimination!        ║
║   💡 UNBALANCED: Can degrade to linked list → O(n) search     ║
║   💡 FIX: Use AVL Trees or Red-Black Trees for balance         ║
║                                                                 ║
╚═════════════════════════════════════════════════════════════════╝
```

---

## Table of Contents
1. [Fundamentals](#fundamentals)
2. [BST Property](#bst-property)
3. [Core Operations](#core-operations)
4. [Advanced Operations](#advanced-operations)
5. [Full Implementation](#full-implementation)
6. [Complexity Analysis](#complexity-analysis)
7. [Common Pitfalls](#common-pitfalls)
8. [Best Practices](#best-practices)
9. [Exam Checklist](#exam-checklist)

---

## Fundamentals

### What is a Binary Search Tree?

A **Binary Search Tree (BST)** is a binary tree where each node contains a value, and:
- The **left subtree** contains values **less than** the node's value
- The **right subtree** contains values **greater than** the node's value
- This property holds **recursively** for all subtrees

### Key Characteristics

```
Properties:
- Each node has at most 2 children (left and right)
- Values in left subtree < Node value < Values in right subtree
- No duplicate values (typically, though some variants allow them)
- Enables efficient searching, insertion, and deletion
```

### Beginner-Friendly Python Example

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None:
        return False
    if value == root.value:
        return True
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

root = None
for v in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, v)

print(search(root, 40))  # True
print(search(root, 25))  # False
```

---

## BST Property

### The Fundamental Property

```
For every node N in a BST:
- All values in N.left subtree < N.value
- All values in N.right subtree > N.value
- This property is RECURSIVE (holds for all subtrees)
```

### Visual Example

```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Valid BST because:
- 20, 30, 40 < 50
- 70, 60, 80 > 50
- Property holds recursively in all subtrees
```

### Non-BST Example

```
        50
       /  \
      30   70
     / \   / \
    60 40 60 80

NOT a valid BST because:
- Left subtree has 60, which is > 50
```

---

## Core Operations

### 1. Search Operation

#### Algorithm
```
function search(node, value):
    if node is null:
        return False

    if value == node.value:
        return True
    elif value < node.value:
        return search(node.left, value)
    else:
        return search(node.right, value)
```

#### Time Complexity
- **Best/Average Case**: O(log n) - balanced tree
- **Worst Case**: O(n) - skewed tree (degenerate to linked list)

#### Example: Search 40 in BST
```
        50
       /  \
      30   70
     / \
    20 40

Steps:
1. 40 < 50 → Go left
2. 40 > 30 → Go right
3. 40 == 40 → Found! (3 comparisons)
```

### 2. Insert Operation

#### Algorithm
```
function insert(node, value):
    if node is null:
        return new Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    // else: duplicate, handle according to requirement

    return node
```

#### Step-by-Step Example: Insert 35 into BST

```
Step 1: Start at root (50)
        50
       /  \
      30   70
     / \
    20 40

Step 2: 35 < 50, go left to 30

Step 3: 35 > 30, go right to 40

Step 4: 35 < 40, go left (null)

Step 5: Insert 35 as left child of 40
        50
       /  \
      30   70
     / \
    20 40
       /
      35
```

#### Multiple Insertions: Build Tree from [50, 30, 70, 20, 40, 60, 80]

```
Insert 50:
        50

Insert 30:
        50
       /
      30

Insert 70:
        50
       /  \
      30   70

Insert 20:
        50
       /  \
      30   70
     /
    20

Insert 40:
        50
       /  \
      30   70
     / \
    20 40

Insert 60:
        50
       /  \
      30   70
     / \   /
    20 40 60

Insert 80:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80
```

### 3. Delete Operation

The delete operation has three cases:

#### Case 1: Deleting a Leaf Node
Simply remove it - it has no children.

```
Delete 20:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Step 1: Find 20 (left child of 30)
Step 2: Has no children → Remove

Result:
        50
       /  \
      30   70
        \  / \
        40 60 80
```

#### Case 2: Deleting a Node with One Child
Replace the node with its child.

```
Delete 30 (has one child: 40):
        50
       /  \
      30   70
        \  / \
        40 60 80

Step 1: Find 30
Step 2: Has one child (40) → Replace 30 with 40

Result:
        50
       /  \
      40   70
          / \
        60  80
```

#### Case 3: Deleting a Node with Two Children
Find the **in-order successor** (smallest value in right subtree) or **in-order predecessor** (largest value in left subtree), replace the node's value with it, and delete that node.

```
Delete 50 (has two children):
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Option A: Use In-Order Successor (60)
Step 1: Find in-order successor in right subtree
        - Go right to 70, then left to 60
        - Successor is 60

Step 2: Replace 50's value with 60
Step 3: Delete 60 from its original position (Case 1 - leaf)

Result:
        60
       /  \
      30   70
     / \     \
    20 40    80

Option B: Use In-Order Predecessor (40)
Step 1: Find in-order predecessor in left subtree
        - Go left to 30, then right to 40
        - Predecessor is 40

Step 2: Replace 50's value with 40
Step 3: Delete 40 from its original position

Result:
        40
       /  \
      30   70
     /    / \
    20   60  80
```

#### Delete Algorithm
```
function delete(node, value):
    if node is null:
        return null

    if value < node.value:
        node.left = delete(node.left, value)
    elif value > node.value:
        node.right = delete(node.right, value)
    else:
        // Found the node to delete

        // Case 1: No children (leaf)
        if node.left is null and node.right is null:
            return null

        // Case 2: One child
        if node.left is null:
            return node.right
        if node.right is null:
            return node.left

        // Case 3: Two children
        // Find in-order successor
        successor = findMin(node.right)
        node.value = successor.value
        node.right = delete(node.right, successor.value)

    return node
```

---

## Advanced Operations

### Find Minimum

```
function findMin(node):
    if node is null:
        return null

    while node.left is not null:
        node = node.left

    return node.value

// In BST, minimum is always the leftmost node
```

**Example:**
```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Min value: 20 (follow left pointers until null)
```

### Find Maximum

```
function findMax(node):
    if node is null:
        return null

    while node.right is not null:
        node = node.right

    return node.value

// In BST, maximum is always the rightmost node
```

**Example:**
```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Max value: 80 (follow right pointers until null)
```

### Find In-Order Successor

The successor of a node is the **smallest value greater than that node**.

```
function successor(node, value):
    // Case 1: If right subtree exists, successor is min of right subtree
    if node.right is not null:
        return findMin(node.right)

    // Case 2: If no right subtree, go up until we find parent where
    // node is in left subtree
    current = node
    parent = null
    // Find the node first (implementation needed)
    while parent is not null and current == parent.right:
        current = parent
        parent = parent.parent
    return parent
```

**Example: Find successor of 40**
```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Node 40 has no right child.
Go up: 40's parent is 30
40 is the right child of 30
30's parent is 50
40 is in the left subtree of 50
So successor is 50
```

### Find In-Order Predecessor

The predecessor of a node is the **largest value less than that node**.

```
function predecessor(node, value):
    // Case 1: If left subtree exists, predecessor is max of left subtree
    if node.left is not null:
        return findMax(node.left)

    // Case 2: If no left subtree, go up until we find parent where
    // node is in right subtree
    current = node
    parent = null
    while parent is not null and current == parent.left:
        current = parent
        parent = parent.parent
    return parent
```

**Example: Find predecessor of 40**
```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

Node 40 has a left child (none in this view, but if it had):
Actually, 40 has no left child.
Go up: 40's parent is 30
40 is the right child of 30
30 is the predecessor
```

### In-Order Traversal (Returns Sorted Values)

```
function inOrder(node):
    if node is null:
        return []

    result = []
    result.extend(inOrder(node.left))
    result.append(node.value)
    result.extend(inOrder(node.right))
    return result

// In-order traversal of BST gives values in sorted order!
```

**Example:**
```
        50
       /  \
      30   70
     / \   / \
    20 40 60 80

In-order traversal: [20, 30, 40, 50, 60, 70, 80]
```

---

## Full Implementation

### Python Implementation

```python
class TreeNode:
    """Represents a single node in the BST"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Complete Binary Search Tree implementation"""

    def __init__(self):
        """Initialize empty BST"""
        self.root = None

    # ============== SEARCH ==============
    def search(self, value):
        """
        Search for a value in the BST
        Time: O(log n) avg, O(n) worst
        """
        return self._search_helper(self.root, value)

    def _search_helper(self, node, value):
        """Recursive search helper"""
        if node is None:
            return False

        if value == node.value:
            return True
        elif value < node.value:
            return self._search_helper(node.left, value)
        else:
            return self._search_helper(node.right, value)

    # ============== INSERT ==============
    def insert(self, value):
        """
        Insert a value into the BST
        Time: O(log n) avg, O(n) worst
        """
        self.root = self._insert_helper(self.root, value)

    def _insert_helper(self, node, value):
        """Recursive insert helper"""
        if node is None:
            return TreeNode(value)

        if value < node.value:
            node.left = self._insert_helper(node.left, value)
        elif value > node.value:
            node.right = self._insert_helper(node.right, value)
        # If value == node.value, treat as duplicate (ignore or handle as needed)

        return node

    # ============== DELETE ==============
    def delete(self, value):
        """
        Delete a value from the BST
        Time: O(log n) avg, O(n) worst
        """
        self.root = self._delete_helper(self.root, value)

    def _delete_helper(self, node, value):
        """Recursive delete helper"""
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_helper(node.left, value)
        elif value > node.value:
            node.right = self._delete_helper(node.right, value)
        else:
            # Found the node to delete

            # Case 1: No children (leaf node)
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: Two children
            # Find in-order successor (min of right subtree)
            successor_node = self._find_min_node(node.right)
            node.value = successor_node.value
            node.right = self._delete_helper(node.right, successor_node.value)

        return node

    # ============== FIND MIN/MAX ==============
    def find_min(self):
        """Find minimum value in BST"""
        if self.root is None:
            return None
        node = self.root
        while node.left is not None:
            node = node.left
        return node.value

    def find_max(self):
        """Find maximum value in BST"""
        if self.root is None:
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.value

    def _find_min_node(self, node):
        """Find node with minimum value in subtree"""
        while node.left is not None:
            node = node.left
        return node

    def _find_max_node(self, node):
        """Find node with maximum value in subtree"""
        while node.right is not None:
            node = node.right
        return node

    # ============== SUCCESSOR/PREDECESSOR ==============
    def find_successor(self, value):
        """Find in-order successor of a value"""
        node = self._find_node(self.root, value)
        if node is None:
            return None

        # If right subtree exists, successor is min of right subtree
        if node.right is not None:
            return self._find_min_node(node.right).value

        # Otherwise, find ancestor where node is in left subtree
        return self._find_successor_ancestor(self.root, value)

    def find_predecessor(self, value):
        """Find in-order predecessor of a value"""
        node = self._find_node(self.root, value)
        if node is None:
            return None

        # If left subtree exists, predecessor is max of left subtree
        if node.left is not None:
            return self._find_max_node(node.left).value

        # Otherwise, find ancestor where node is in right subtree
        return self._find_predecessor_ancestor(self.root, value)

    def _find_node(self, node, value):
        """Find a node with given value"""
        if node is None:
            return None

        if value == node.value:
            return node
        elif value < node.value:
            return self._find_node(node.left, value)
        else:
            return self._find_node(node.right, value)

    def _find_successor_ancestor(self, node, value):
        """Find successor by traversing up the tree"""
        if node is None:
            return None

        if value >= node.value:
            return self._find_successor_ancestor(node.right, value)
        else:
            left_successor = self._find_successor_ancestor(node.left, value)
            return node.value if left_successor is None else left_successor

    def _find_predecessor_ancestor(self, node, value):
        """Find predecessor by traversing up the tree"""
        if node is None:
            return None

        if value <= node.value:
            return self._find_predecessor_ancestor(node.left, value)
        else:
            right_predecessor = self._find_predecessor_ancestor(node.right, value)
            return node.value if right_predecessor is None else right_predecessor

    # ============== TRAVERSALS ==============
    def inorder(self):
        """In-order traversal (Left-Root-Right) - returns sorted"""
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        """Recursive in-order helper"""
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def preorder(self):
        """Pre-order traversal (Root-Left-Right)"""
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node, result):
        """Recursive pre-order helper"""
        if node is not None:
            result.append(node.value)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def postorder(self):
        """Post-order traversal (Left-Right-Root)"""
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node, result):
        """Recursive post-order helper"""
        if node is not None:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.value)

    # ============== UTILITY METHODS ==============
    def is_bst(self):
        """Check if tree is a valid BST"""
        return self._is_bst_helper(self.root, float('-inf'), float('inf'))

    def _is_bst_helper(self, node, min_val, max_val):
        """Recursive BST validation"""
        if node is None:
            return True

        if node.value <= min_val or node.value >= max_val:
            return False

        return (self._is_bst_helper(node.left, min_val, node.value) and
                self._is_bst_helper(node.right, node.value, max_val))

    def height(self):
        """Get height of the tree"""
        return self._height_helper(self.root)

    def _height_helper(self, node):
        """Recursive height calculation"""
        if node is None:
            return -1
        return 1 + max(self._height_helper(node.left),
                      self._height_helper(node.right))

    def size(self):
        """Get number of nodes in tree"""
        return self._size_helper(self.root)

    def _size_helper(self, node):
        """Recursive size calculation"""
        if node is None:
            return 0
        return 1 + self._size_helper(node.left) + self._size_helper(node.right)


# ============== USAGE EXAMPLES ==============

# Create a BST
bst = BinarySearchTree()

# Insert values
values = [50, 30, 70, 20, 40, 60, 80]
for val in values:
    bst.insert(val)

# Search
print("Search 40:", bst.search(40))  # True
print("Search 100:", bst.search(100))  # False

# Find min/max
print("Min:", bst.find_min())  # 20
print("Max:", bst.find_max())  # 80

# Traversals
print("In-order:", bst.inorder())  # [20, 30, 40, 50, 60, 70, 80]
print("Pre-order:", bst.preorder())  # [50, 30, 20, 40, 70, 60, 80]
print("Post-order:", bst.postorder())  # [20, 40, 30, 60, 80, 70, 50]

# Successor/Predecessor
print("Successor of 40:", bst.find_successor(40))  # 50
print("Predecessor of 40:", bst.find_predecessor(40))  # 30

# Delete
bst.delete(20)  # Delete leaf
print("After deleting 20:", bst.inorder())  # [30, 40, 50, 60, 70, 80]

bst.delete(30)  # Delete node with one child
print("After deleting 30:", bst.inorder())  # [40, 50, 60, 70, 80]

bst.delete(50)  # Delete node with two children
print("After deleting 50:", bst.inorder())  # [40, 60, 70, 80]

# Tree properties
print("Height:", bst.height())  # Height of remaining tree
print("Size:", bst.size())  # Number of nodes
print("Is valid BST:", bst.is_bst())  # True
```

---

## Complexity Analysis

### Time Complexity

| Operation | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Search    | O(1)      | O(log n)     | O(n)       |
| Insert    | O(1)      | O(log n)     | O(n)       |
| Delete    | O(1)      | O(log n)     | O(n)       |
| Find Min  | O(1)      | O(log n)     | O(n)       |
| Find Max  | O(1)      | O(log n)     | O(n)       |
| Traversal | O(n)      | O(n)         | O(n)       |

### Space Complexity

| Operation | Best Case | Average Case | Worst Case |
|-----------|-----------|--------------|------------|
| Storage   | O(n)      | O(n)         | O(n)       |
| Recursion | O(log n)  | O(log n)     | O(n)       |

### Why Worst Case is O(n)?

```
Balanced BST:
        50
       /  \
      30   70
     / \   / \
    20 40 60 80
    Height: 3, Operations: O(log 8) = O(3)

Skewed BST (like linked list):
    50
    /
   30
   /
  20
  /
 10

Height: 4, Operations: O(n) for n nodes
```

---

## Common Pitfalls

### Pitfall 1: Not Maintaining BST Property During Insert

```python
# WRONG - Creates invalid BST
node.left = insert_random_position(node.left, value)

# CORRECT - Compares value with node
if value < node.value:
    node.left = insert(node.left, value)
else:
    node.right = insert(node.right, value)
```

### Pitfall 2: Incorrect Delete with Two Children

```python
# WRONG - Picks arbitrary child
if node.left and node.right:
    node = node.left  # Losing right subtree!

# CORRECT - Uses successor/predecessor
if node.left and node.right:
    successor = find_min(node.right)
    node.value = successor.value
    node.right = delete(node.right, successor.value)
```

### Pitfall 3: Unbalanced Tree Degradation

```
Problem: If you insert sorted data, BST degrades to linked list

Insert: [1, 2, 3, 4, 5]

Results in:
1
 \
  2
   \
    3
     \
      4
       \
        5

All operations become O(n) instead of O(log n)!

Solution: Use AVL Trees or Red-Black Trees for self-balancing
```

### Pitfall 4: Forgetting to Return Updated Node

```python
# WRONG - Tree structure not updated
def insert(node, value):
    if node is None:
        TreeNode(value)  # Creates but doesn't return!
    # ...

# CORRECT
def insert(node, value):
    if node is None:
        return TreeNode(value)  # Returns the new node
    # ...
```

### Pitfall 5: Incorrect In-Order Successor

```python
# WRONG - Only checks right subtree
def successor(node):
    return find_min(node.right)  # What if no right subtree?

# CORRECT
def successor(node):
    if node.right:
        return find_min(node.right)
    else:
        return find_successor_ancestor(root, node.value)
```

---

## Best Practices

### 1. Always Validate Input
```python
def insert(self, value):
    if value is None:
        raise ValueError("Cannot insert None")
    self.root = self._insert_helper(self.root, value)
```

### 2. Use Helper Methods for Clarity
```python
def find_min(self):
    """Public method"""
    return self._get_min_value(self.root)

def _get_min_value(self, node):
    """Private helper"""
    # Implementation here
```

### 3. Handle Edge Cases
```python
# Empty tree
if self.root is None:
    return None

# Single node
if node.left is None and node.right is None:
    return node.value

# Non-existent value
if self._find_node(self.root, value) is None:
    return None
```

### 4. Consider Duplicates
```python
def insert(self, value):
    """Handle duplicates - ignore them"""
    self.root = self._insert_helper(self.root, value)

def _insert_helper(self, node, value):
    if node is None:
        return TreeNode(value)

    if value < node.value:
        node.left = self._insert_helper(node.left, value)
    elif value > node.value:
        node.right = self._insert_helper(node.right, value)
    # else: duplicate - ignore

    return node
```

### 5. Optimize for Balanced Trees
```python
# Consider using AVL Tree or Red-Black Tree
# if you expect unbalanced insertions
from avl_tree import AVLTree

# For random data, BST is usually fine
# For sorted data, use self-balancing variant
```

---

## Exam Checklist

### Understand
- [ ] BST property (left < root < right)
- [ ] Why BST enables efficient searching
- [ ] Difference between BST and Binary Tree
- [ ] In-order traversal gives sorted sequence

### Implementation
- [ ] Can implement search from scratch
- [ ] Can implement insert with proper recursion
- [ ] Can handle all three delete cases
- [ ] Can find min, max, successor, predecessor
- [ ] Can validate if tree is valid BST

### Complexity
- [ ] Know O(log n) average, O(n) worst case
- [ ] Understand why worst case happens
- [ ] Know when to use BST vs alternatives

### Problem Solving
- [ ] Can identify when to use BST
- [ ] Can handle duplicate values
- [ ] Can optimize tree balance
- [ ] Can write clean, recursion-based code

### Edge Cases
- [ ] Empty tree (null root)
- [ ] Single node tree
- [ ] Duplicate values
- [ ] Deletion of root node
- [ ] Successor/predecessor at boundaries
- [ ] Unbalanced (skewed) tree

### Alternatives
- [ ] Know limitations of BST
- [ ] Understand when AVL Trees are needed
- [ ] Know about Red-Black Trees
- [ ] Understand B-Trees for databases

---

## Key Takeaways

1. **BST Property**: Left subtree < Root < Right subtree (recursive)

2. **Efficient Search**: O(log n) on balanced trees, using comparison-based navigation

3. **Delete Complexity**: Three cases (leaf, one child, two children) require careful handling

4. **Sorted Traversal**: In-order traversal gives values in sorted order

5. **Main Weakness**: Can degrade to O(n) if tree becomes unbalanced

6. **Solution**: Use self-balancing variants (AVL Trees, Red-Black Trees)

7. **Successor/Predecessor**: Essential operations often tested in interviews

8. **Implementation**: Recursive approach is cleaner and more intuitive
