---
title: AVL Trees (Self-Balancing BSTs)
description: Complete guide to AVL Trees with rotations, balancing, and guaranteed logarithmic operations
category: Non-Linear Data Structures
difficulty: Advanced
estimated_time: 60 minutes
prerequisites: ["Binary Search Trees", "Tree Rotations", "Recursion"]
tags: ["AVL Trees", "Self-Balancing", "Rotations", "Height-Balanced Trees"]
---

# AVL Trees (Self-Balancing Binary Search Trees)

## Table of Contents
1. [Fundamentals](#fundamentals)
2. [Balance Factor Concept](#balance-factor-concept)
3. [Tree Rotations](#tree-rotations)
4. [Rotation Types](#rotation-types)
5. [Insertion with Rebalancing](#insertion-with-rebalancing)
6. [Deletion with Rebalancing](#deletion-with-rebalancing)
7. [Full Implementation](#full-implementation)
8. [Complexity Analysis](#complexity-analysis)
9. [Common Pitfalls](#common-pitfalls)
10. [Best Practices](#best-practices)
11. [Exam Checklist](#exam-checklist)

---

## Fundamentals

### What is an AVL Tree?

An **AVL Tree** is a **self-balancing Binary Search Tree** where:
- The heights of left and right subtrees of any node differ by **at most 1**
- This property is maintained recursively throughout the tree
- Named after inventors: **Adelson-Velsky and Landis** (1962)

### Key Characteristics

```
AVL Tree Properties:
1. Valid Binary Search Tree (BST property maintained)
2. Height-balanced (|height(left) - height(right)| ≤ 1 for all nodes)
3. Automatically rebalances on insert/delete
4. Guarantees O(log n) for all operations
5. May be more balanced than needed (stricter than Red-Black Trees)
```

### Why AVL Trees?

```
Regular BST Problem:
Insert [1, 2, 3, 4, 5]
→ Degrades to linked list
→ O(n) operations

AVL Tree Solution:
Same insertions → Automatically rebalances
→ Remains balanced with height log(n)
→ O(log n) guaranteed
```

---

## Balance Factor Concept

### Definition

**Balance Factor (BF)** = height(left subtree) - height(right subtree)

### Rules

```
For a valid AVL Tree:
BF ∈ {-1, 0, 1} for ALL nodes

BF = -1: Right subtree is 1 unit taller (right-heavy)
BF = 0:  Both subtrees are same height (balanced)
BF = 1:  Left subtree is 1 unit taller (left-heavy)

Invalid:
BF ≤ -2: Too right-heavy (needs rebalancing)
BF ≥ 2:  Too left-heavy (needs rebalancing)
```

### Visual Examples

```
Balanced (BF = 0):
      50(0)
     /    \
   30(0)  70(0)

BF at 50 = height(left) - height(right) = 1 - 1 = 0

Left-Heavy (BF = 1):
      50(1)
     /    \
   30(0)  70
   /
  20

BF at 50 = 2 - 1 = 1

Right-Heavy (BF = -1):
      50(-1)
     /    \
   30    70(0)
           \
            80

BF at 50 = 1 - 2 = -1

Unbalanced (Invalid):
      50(2)        ← BF = 2 (needs rebalancing)
     /
   30
   /
  20

BF at 50 = 3 - 1 = 2 (too left-heavy!)
```

---

## Tree Rotations

### What are Rotations?

Rotations are **local operations** that:
- Change the structure of the tree
- Maintain the BST property
- Restore balance factor to valid range
- Take **O(1) time**

### Visual Concept

```
Rotation moves nodes without violating BST property

Right Rotation (LL case):
    C               B
   /              / \
  B      →        A   C
 /
A

Left Rotation (RR case):
  A                 B
   \              /  \
    B      →     A    C
     \
      C
```

---

## Rotation Types

### 1. Right Rotation (RR Rotation)

**When needed**: Unbalanced to the left (BF > 1)

#### Algorithm

```
Right-Rotate(Z):
    Y = Z.left
    T3 = Y.right

    // Rotate
    Y.right = Z
    Z.left = T3

    // Update heights
    Z.height = 1 + max(height(Z.left), height(Z.right))
    Y.height = 1 + max(height(Y.left), height(Y.right))

    return Y
```

#### Visual Step-by-Step

```
Before Right Rotation (BF = 2, too left-heavy):
        C
       /
      B
     /
    A

Step 1: Identify pivot (B) and rotation node (C)

Step 2: Move relationships
    - B becomes new root
    - C becomes right child of B
    - B's right child (empty here) becomes C's left

Step 3: After Right Rotation:
      B
     / \
    A   C

Heights updated: All nodes now have valid BF
```

#### Full Example with Values

```
Before (BF = 2):
        50
       /
      30
     /
    20

Step 1: Right-rotate around 50
    Pivot: 30
    New root: 30

Step 2: Connect children
    - 30's right child (null) → becomes 50's left
    - 50 → becomes 30's right

After (all BF valid):
      30
     /  \
    20  50
```

### 2. Left Rotation (LL Rotation)

**When needed**: Unbalanced to the right (BF < -1)

#### Algorithm

```
Left-Rotate(X):
    Y = X.right
    T2 = Y.left

    // Rotate
    Y.left = X
    X.right = T2

    // Update heights
    X.height = 1 + max(height(X.left), height(X.right))
    Y.height = 1 + max(height(Y.left), height(Y.right))

    return Y
```

#### Visual Step-by-Step

```
Before Left Rotation (BF = -2, too right-heavy):
    A
     \
      B
       \
        C

Step 1: Identify pivot (B) and rotation node (A)

Step 2: Move relationships
    - B becomes new root
    - A becomes left child of B
    - B's left child (empty here) becomes A's right

Step 3: After Left Rotation:
      B
     / \
    A   C

Heights updated: All nodes now have valid BF
```

#### Full Example with Values

```
Before (BF = -2):
    20
      \
      40
        \
        60

Step 1: Left-rotate around 20
    Pivot: 40
    New root: 40

Step 2: Connect children
    - 40's left child (null) → becomes 20's right
    - 20 → becomes 40's left

After (all BF valid):
      40
     /  \
    20  60
```

### 3. Left-Right Rotation (LR Rotation)

**When needed**: Left subtree's right subtree is taller (BF > 1 with left-child BF < 0)

#### Algorithm

```
LeftRight-Rotate(Z):
    // Step 1: Left-rotate the left subtree
    Z.left = Left-Rotate(Z.left)

    // Step 2: Right-rotate the main tree
    return Right-Rotate(Z)
```

#### Visual Step-by-Step

```
Original Tree (BF = 2, but left child is right-heavy):
        C
       /
      A
       \
        B

Problem: A is left child, but B (right child of A) is taller
Solution: Two rotations needed

Step 1: Left-rotate around A
        C
       /
      B
     /
    A

Now the tree is simple left-heavy

Step 2: Right-rotate around C
      B
     / \
    A   C

Final: Balanced tree
```

#### Full Example with Values

```
Before LR Rotation (BF = 2 at 30):
        50
       /
      20
        \
        40

Analysis: 50 is left-heavy (BF=2)
But 20's right child (40) is taller than its left

Step 1: Left-rotate around 20
        50
       /
      40
     /
    20

Step 2: Right-rotate around 50
      40
     /  \
    20  50

All balance factors: valid
```

### 4. Right-Left Rotation (RL Rotation)

**When needed**: Right subtree's left subtree is taller (BF < -1 with right-child BF > 0)

#### Algorithm

```
RightLeft-Rotate(Z):
    // Step 1: Right-rotate the right subtree
    Z.right = Right-Rotate(Z.right)

    // Step 2: Left-rotate the main tree
    return Left-Rotate(Z)
```

#### Visual Step-by-Step

```
Original Tree (BF = -2, but right child is left-heavy):
    A
     \
      C
     /
    B

Problem: C is right child, but B (left child of C) is taller
Solution: Two rotations needed

Step 1: Right-rotate around C
    A
     \
      B
       \
        C

Now the tree is simple right-heavy

Step 2: Left-rotate around A
      B
     / \
    A   C

Final: Balanced tree
```

#### Full Example with Values

```
Before RL Rotation (BF = -2 at 20):
    20
      \
      50
     /
    30

Analysis: 20 is right-heavy (BF=-2)
But 50's left child (30) is taller than its right

Step 1: Right-rotate around 50
    20
      \
      30
        \
        50

Step 2: Left-rotate around 20
      30
     /  \
    20  50

All balance factors: valid
```

---

## Rotation Decision Tree

### How to Choose Which Rotation?

```
At problematic node Z:

1. Calculate balance factor: BF = height(left) - height(right)

2. If BF > 1 (left-heavy):
   a. Check left child's BF
   b. If left-child BF ≥ 0:
      → Single Right Rotation (LL case)
   c. If left-child BF < 0:
      → Left-Right Rotation (LR case)

3. If BF < -1 (right-heavy):
   a. Check right child's BF
   b. If right-child BF ≤ 0:
      → Single Left Rotation (RR case)
   c. If right-child BF > 0:
      → Right-Left Rotation (RL case)

4. If BF ∈ {-1, 0, 1}:
   → No rotation needed
```

### Visual Decision Guide

```
BF > 1 (Left-heavy)
    ├─ Left-child BF ≥ 0  →  Right Rotation (LL)
    └─ Left-child BF < 0  →  Left-Right Rotation (LR)

BF < -1 (Right-heavy)
    ├─ Right-child BF ≤ 0  →  Left Rotation (RR)
    └─ Right-child BF > 0  →  Right-Left Rotation (RL)

BF ∈ {-1, 0, 1}  →  Balanced, no action
```

---

## Insertion with Rebalancing

### AVL Insert Algorithm

```
Insert(value):
    1. Insert as normal BST (value goes to proper position)
    2. Update heights from leaf to root
    3. Calculate balance factors
    4. If any node has |BF| > 1:
       → Apply appropriate rotation
    5. Continue up the tree checking all ancestors
```

### Step-by-Step Example: Insert [50, 25, 75, 10, 30, 5]

```
Step 1: Insert 50
        50 (BF=0)
    ✓ Balanced

Step 2: Insert 25
        50 (BF=1)
       /
      25 (BF=0)
    ✓ Balanced (BF=1 is valid)

Step 3: Insert 75
        50 (BF=0)
       /  \
      25  75
    ✓ Balanced

Step 4: Insert 10
        50 (BF=1)
       /  \
      25  75
     /
    10 (BF=0)
    ✓ Balanced (BF=1 is valid)

Step 5: Insert 30
        50 (BF=1)
       /  \
      25  75
     / \
    10 30
    ✓ Balanced

Step 6: Insert 5
        50 (BF=2)  ← Unbalanced! |BF| > 1
       /  \
      25  75
     / \
    10 30
   /
  5

Analysis: BF=2 (left-heavy)
Left-child (25) has BF=1 (≥0)
→ Apply Right Rotation (LL case)

After Right Rotation around 50:
        25 (BF=0)
       /  \
      10  50
     /  \ / \
    5  (none) 30 75

All balance factors valid!
```

### Insert Algorithm with Rotation

```python
def insert_avl(node, value):
    # Step 1: Normal BST insert
    if node is None:
        return TreeNode(value)

    if value < node.value:
        node.left = insert_avl(node.left, value)
    elif value > node.value:
        node.right = insert_avl(node.right, value)
    else:
        return node  # Duplicate

    # Step 2: Update height
    node.height = 1 + max(height(node.left), height(node.right))

    # Step 3: Calculate balance factor
    bf = get_balance(node)

    # Step 4: Left-heavy cases
    if bf > 1:
        # Left-Left case
        if value < node.left.value:
            return right_rotate(node)
        # Left-Right case
        if value > node.left.value:
            node.left = left_rotate(node.left)
            return right_rotate(node)

    # Step 5: Right-heavy cases
    if bf < -1:
        # Right-Right case
        if value > node.right.value:
            return left_rotate(node)
        # Right-Left case
        if value < node.right.value:
            node.right = right_rotate(node.right)
            return left_rotate(node)

    return node
```

---

## Deletion with Rebalancing

### AVL Delete Algorithm

```
Delete(value):
    1. Find and delete node (same as BST delete)
    2. Update heights from parent to root
    3. Calculate balance factors
    4. If any node has |BF| > 1:
       → Apply appropriate rotation
    5. Continue up the tree checking all ancestors
    6. May need multiple rotations on path to root
```

### Deletion Example: Delete 10 from Previous Tree

```
Before Deletion:
        25 (BF=0)
       /  \
      10  50
     /  \ / \
    5  (none) 30 75

Delete 10 (has one child: 5):
        25 (BF=-1)
       /  \
      5   50
          / \
        30  75

Check balance factors:
- 5: BF = 0 ✓
- 50: BF = 0 ✓
- 25: BF = height(5) - height(50) = 0 - 2 = -2 ✗

Unbalanced! Right-heavy (BF=-2)
Right-child 50 has BF = 0 (≤ 0)
→ Apply Left Rotation (RR case)

After Left Rotation around 25:
        50 (BF=0)
       /  \
      25  75
     / \
    5  30

All balance factors valid!
```

### Delete Algorithm with Rotation

```python
def delete_avl(node, value):
    # Step 1: Normal BST delete
    if node is None:
        return None

    if value < node.value:
        node.left = delete_avl(node.left, value)
    elif value > node.value:
        node.right = delete_avl(node.right, value)
    else:
        # Found node to delete
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        # Two children: use successor
        min_node = find_min(node.right)
        node.value = min_node.value
        node.right = delete_avl(node.right, min_node.value)

    if node is None:
        return None

    # Step 2: Update height
    node.height = 1 + max(height(node.left), height(node.right))

    # Step 3: Calculate balance factor
    bf = get_balance(node)

    # Step 4: Left-heavy cases
    if bf > 1:
        if get_balance(node.left) >= 0:
            return right_rotate(node)
        else:
            node.left = left_rotate(node.left)
            return right_rotate(node)

    # Step 5: Right-heavy cases
    if bf < -1:
        if get_balance(node.right) <= 0:
            return left_rotate(node)
        else:
            node.right = right_rotate(node.right)
            return left_rotate(node)

    return node
```

---

## Full Implementation

### Python Implementation

```python
class AVLNode:
    """Represents a node in the AVL Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.balance_factor = 0


class AVLTree:
    """Complete AVL Tree implementation with self-balancing"""

    def __init__(self):
        """Initialize empty AVL tree"""
        self.root = None

    # ============== HEIGHT & BALANCE FACTOR ==============
    def _height(self, node):
        """Get height of a node"""
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        """Calculate balance factor of a node"""
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _update_height(self, node):
        """Update height of a node"""
        if node is not None:
            node.height = 1 + max(self._height(node.left),
                                  self._height(node.right))
            node.balance_factor = self._balance_factor(node)

    # ============== ROTATIONS ==============
    def _right_rotate(self, z):
        """
        Right rotation (LL case)
          z               y
         /              / \
        y      -->      x   z
       /
      x
        """
        y = z.left
        t3 = y.right

        # Perform rotation
        y.right = z
        z.left = t3

        # Update heights
        self._update_height(z)
        self._update_height(y)

        return y

    def _left_rotate(self, x):
        """
        Left rotation (RR case)
        x                  y
         \              /  \
          y    -->      x    z
           \
            z
        """
        y = x.right
        t2 = y.left

        # Perform rotation
        y.left = x
        x.right = t2

        # Update heights
        self._update_height(x)
        self._update_height(y)

        return y

    def _left_right_rotate(self, z):
        """Left-Right rotation (LR case)"""
        z.left = self._left_rotate(z.left)
        return self._right_rotate(z)

    def _right_left_rotate(self, z):
        """Right-Left rotation (RL case)"""
        z.right = self._right_rotate(z.right)
        return self._left_rotate(z)

    # ============== INSERT ==============
    def insert(self, value):
        """
        Insert a value and maintain AVL property
        Time: O(log n)
        """
        self.root = self._insert_helper(self.root, value)

    def _insert_helper(self, node, value):
        """Recursive insert with rebalancing"""
        # Step 1: Normal BST insert
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert_helper(node.left, value)
        elif value > node.value:
            node.right = self._insert_helper(node.right, value)
        else:
            return node  # Duplicate - ignore

        # Step 2: Update height and balance factor
        self._update_height(node)

        # Step 3: Check balance and apply rotations
        bf = node.balance_factor

        # Left-heavy cases
        if bf > 1:
            # Left-Left case
            if value < node.left.value:
                return self._right_rotate(node)
            # Left-Right case
            if value > node.left.value:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        # Right-heavy cases
        if bf < -1:
            # Right-Right case
            if value > node.right.value:
                return self._left_rotate(node)
            # Right-Left case
            if value < node.right.value:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    # ============== DELETE ==============
    def delete(self, value):
        """
        Delete a value and maintain AVL property
        Time: O(log n)
        """
        self.root = self._delete_helper(self.root, value)

    def _delete_helper(self, node, value):
        """Recursive delete with rebalancing"""
        if node is None:
            return None

        # Step 1: Normal BST delete
        if value < node.value:
            node.left = self._delete_helper(node.left, value)
        elif value > node.value:
            node.right = self._delete_helper(node.right, value)
        else:
            # Found node to delete
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Two children: use in-order successor
            successor = self._find_min_node(node.right)
            node.value = successor.value
            node.right = self._delete_helper(node.right, successor.value)

        if node is None:
            return None

        # Step 2: Update height and balance factor
        self._update_height(node)

        # Step 3: Check balance and apply rotations
        bf = node.balance_factor

        # Left-heavy cases
        if bf > 1:
            if self._balance_factor(node.left) >= 0:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        # Right-heavy cases
        if bf < -1:
            if self._balance_factor(node.right) <= 0:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        return node

    # ============== SEARCH ==============
    def search(self, value):
        """
        Search for a value
        Time: O(log n) guaranteed
        """
        return self._search_helper(self.root, value)

    def _search_helper(self, node, value):
        """Recursive search"""
        if node is None:
            return False

        if value == node.value:
            return True
        elif value < node.value:
            return self._search_helper(node.left, value)
        else:
            return self._search_helper(node.right, value)

    # ============== FIND MIN/MAX ==============
    def find_min(self):
        """Find minimum value"""
        if self.root is None:
            return None
        return self._find_min_node(self.root).value

    def find_max(self):
        """Find maximum value"""
        if self.root is None:
            return None
        return self._find_max_node(self.root).value

    def _find_min_node(self, node):
        """Find node with minimum value"""
        while node.left is not None:
            node = node.left
        return node

    def _find_max_node(self, node):
        """Find node with maximum value"""
        while node.right is not None:
            node = node.right
        return node

    # ============== TRAVERSALS ==============
    def inorder(self):
        """In-order traversal (sorted)"""
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        """Recursive in-order traversal"""
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def preorder(self):
        """Pre-order traversal"""
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node, result):
        """Recursive pre-order traversal"""
        if node is not None:
            result.append(node.value)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def level_order(self):
        """Level-order traversal (BFS)"""
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    # ============== UTILITY METHODS ==============
    def is_avl(self):
        """Check if tree maintains AVL property"""
        return self._is_avl_helper(self.root)

    def _is_avl_helper(self, node):
        """Recursive AVL validation"""
        if node is None:
            return True

        # Check balance factor
        bf = self._balance_factor(node)
        if abs(bf) > 1:
            return False

        # Check recursively
        return (self._is_avl_helper(node.left) and
                self._is_avl_helper(node.right))

    def height(self):
        """Get height of tree"""
        return self._height(self.root)

    def size(self):
        """Get number of nodes"""
        return self._size_helper(self.root)

    def _size_helper(self, node):
        """Recursive size calculation"""
        if node is None:
            return 0
        return 1 + self._size_helper(node.left) + self._size_helper(node.right)

    def print_tree(self):
        """Print tree structure"""
        if not self.root:
            print("Empty tree")
            return

        self._print_helper(self.root, "", True)

    def _print_helper(self, node, prefix, is_tail):
        """Helper to print tree visually"""
        if node is None:
            return

        print(prefix + ("└── " if is_tail else "├── ") +
              f"{node.value}(h:{node.height}, bf:{node.balance_factor})")

        children = []
        if node.left:
            children.append((node.left, False))
        if node.right:
            children.append((node.right, True))

        for i, (child, is_last) in enumerate(children):
            extension = "    " if is_tail else "│   "
            self._print_helper(child, prefix + extension, is_last)


# ============== USAGE EXAMPLES ==============

# Create an AVL tree
avl = AVLTree()

# Insert values
values = [50, 25, 75, 10, 30, 5, 15, 27, 55, 100]
print("Inserting:", values)
for val in values:
    avl.insert(val)

print("\nTree structure:")
avl.print_tree()

print("\nIn-order traversal (sorted):", avl.inorder())
print("Tree height:", avl.height())
print("Tree size:", avl.size())
print("Is valid AVL:", avl.is_avl())

# Search
print("\nSearch 30:", avl.search(30))
print("Search 999:", avl.search(999))

# Min/Max
print("Min:", avl.find_min())
print("Max:", avl.find_max())

# Delete
print("\n--- Deleting 10 ---")
avl.delete(10)
print("After delete:")
avl.print_tree()
print("In-order:", avl.inorder())
print("Is valid AVL:", avl.is_avl())

print("\n--- Deleting 50 (root with 2 children) ---")
avl.delete(50)
print("After delete:")
avl.print_tree()
print("In-order:", avl.inorder())
print("Is valid AVL:", avl.is_avl())

# Test with worst-case data
print("\n--- Testing with sorted insertion ---")
avl2 = AVLTree()
for i in range(1, 8):
    avl2.insert(i)

print("Inserted [1,2,3,4,5,6,7] in order")
print("Height:", avl2.height(), "(should be ~3, not 7)")
avl2.print_tree()
print("Is valid AVL:", avl2.is_avl())
```

---

## Complexity Analysis

### Time Complexity

| Operation | Time      | Reason                                 |
|-----------|-----------|----------------------------------------|
| Search    | O(log n)  | Height always log(n) due to balancing |
| Insert    | O(log n)  | Insert + traversal up + rotations     |
| Delete    | O(log n)  | Delete + traversal up + rotations     |
| Find Min  | O(log n)  | Walk leftmost path                    |
| Find Max  | O(log n)  | Walk rightmost path                   |
| Traversal | O(n)      | Visit all nodes                       |

### Space Complexity

| Operation | Space    | Reason                        |
|-----------|----------|-------------------------------|
| Storage   | O(n)     | n nodes in tree              |
| Recursion | O(log n) | Height of tree               |

### Height Property

```
For an AVL tree with n nodes:
log(n+1) - 1 ≤ height ≤ 1.44 * log(n+2) - 1

Approximate: height ≈ 1.44 * log(n)

This guarantees O(log n) for all operations!
```

### Comparison with Regular BST

```
Regular BST (unbalanced):
Insert [1,2,3,4,5] → Height = 5 → Operations O(n)

AVL Tree (same insertions):
Same data → Height = 3 → Operations O(log n)

Balanced BST:
Height = log(n), operations = O(log n)

Skewed BST:
Height = n, operations = O(n)

AVL Tree:
Always height = log(n), always O(log n)
```

---

## Common Pitfalls

### Pitfall 1: Forgetting to Update Heights

```python
# WRONG - Heights not updated
def left_rotate(node):
    y = node.right
    node.right = y.left
    y.left = node
    return y  # Heights are wrong!

# CORRECT - Update heights after rotation
def left_rotate(node):
    y = node.right
    node.right = y.left
    y.left = node

    self._update_height(node)    # Update node first
    self._update_height(y)       # Then update rotated node
    return y
```

### Pitfall 2: Incorrect Balance Factor Calculation

```python
# WRONG - Forgot negation
bf = node.height - node.left.height - node.right.height

# CORRECT - Left height minus right height
bf = self._height(node.left) - self._height(node.right)
```

### Pitfall 3: Not Checking Correct Child for Rotation Type

```python
# WRONG - Only checks one child
if bf > 1:
    return right_rotate(node)  # What if it's LR case?

# CORRECT - Checks which child caused imbalance
if bf > 1:
    if value < node.left.value:
        return right_rotate(node)  # LL case
    else:
        node.left = left_rotate(node.left)
        return right_rotate(node)  # LR case
```

### Pitfall 4: Missing Rotations After Deletion

```python
# WRONG - Only checks immediate subtree
def delete_avl(node, value):
    # ... delete logic ...
    self._update_height(node)
    return node  # Doesn't check balance!

# CORRECT - Rebalances and checks ancestors
def delete_avl(node, value):
    # ... delete logic ...
    self._update_height(node)

    bf = self._balance_factor(node)
    # Apply rotations if needed...
    return node
```

### Pitfall 5: Modifying Tree Without Returning Node

```python
# WRONG - Rotation result not captured
def insert(node, value):
    if bf > 1:
        right_rotate(node)  # Result discarded!
        return node  # Still unbalanced!

    return node

# CORRECT - Capture rotation result
def insert(node, value):
    if bf > 1:
        node = right_rotate(node)  # Assign result
    return node
```

---

## Best Practices

### 1. Always Maintain Height Information

```python
class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Track height at each node
        self.balance_factor = 0  # Track balance factor
```

### 2. Centralize Rotation Logic

```python
def rotate_left(self, node):
    """Encapsulate rotation logic"""
    # ... rotation code ...
    self._update_height(node)
    self._update_height(new_root)
    return new_root
```

### 3. Validate After Operations

```python
def insert(self, value):
    self.root = self._insert_helper(self.root, value)
    # Validate tree integrity
    assert self.is_avl(), "Tree lost AVL property!"
```

### 4. Document Rotation Cases

```python
# LL case: Left child is left-heavy
# LR case: Left child is right-heavy
# RR case: Right child is right-heavy
# RL case: Right child is left-heavy
```

### 5. Use Consistent Naming

```python
# _height() - get height
# _balance_factor() - get balance factor
# _update_height() - update height and BF
# _left_rotate() - perform left rotation
# _right_rotate() - perform right rotation
```

---

## Exam Checklist

### Understand
- [ ] AVL tree definition (height-balanced BST)
- [ ] Balance factor concept (difference in subtree heights)
- [ ] Why |BF| ≤ 1 for all nodes
- [ ] Guaranteed O(log n) operations
- [ ] When rebalancing is needed

### Four Rotations
- [ ] Can identify Left-Left (LL) case and apply right rotation
- [ ] Can identify Right-Right (RR) case and apply left rotation
- [ ] Can identify Left-Right (LR) case and apply two rotations
- [ ] Can identify Right-Left (RL) case and apply two rotations
- [ ] Know when each rotation applies

### Implementation
- [ ] Can implement insert with rebalancing from scratch
- [ ] Can implement delete with rebalancing from scratch
- [ ] Can implement all four rotations correctly
- [ ] Update heights after every operation
- [ ] Calculate balance factors accurately

### Complexity
- [ ] Know all operations are O(log n)
- [ ] Understand why height is always O(log n)
- [ ] Know space complexity is O(n) for storage, O(log n) for recursion

### Problem Solving
- [ ] Can identify which rotation(s) are needed
- [ ] Can trace insertions and deletions step-by-step
- [ ] Can visualize tree transformations
- [ ] Can verify AVL property after operations

### Common Mistakes
- [ ] Forgetting to update heights
- [ ] Wrong rotation type
- [ ] Not returning rotated node
- [ ] Missing balance checks
- [ ] Confusing balance factor direction

### Comparisons
- [ ] AVL Tree vs Binary Search Tree
- [ ] AVL Tree vs Red-Black Tree (trade-offs)
- [ ] When to use AVL vs other structures

---

## Key Takeaways

1. **Self-Balancing**: AVL Trees automatically maintain balance after insert/delete

2. **Balance Factor**: |height(left) - height(right)| ≤ 1 for all nodes

3. **Four Rotations**: LL, RR, LR, RL handle all imbalance cases

4. **Guaranteed O(log n)**: Height is always log(n) due to balancing

5. **Height Update**: Must update heights from child to parent after operations

6. **Rotation Decision**: Check balance factor and child balance factors

7. **Double Rotation**: LR and RL cases need two rotations

8. **Cost vs Benefit**: More complex than BST, but guaranteed performance

9. **Implementation Details**: Both insert and delete need rebalancing

10. **Practical Use**: File systems, databases often use AVL Trees for guaranteed performance

---

## Related Topics

- **Binary Search Trees**: Foundation for AVL Trees
- **Red-Black Trees**: Alternative with relaxed balance constraints
- **B-Trees**: For external storage/databases
- **Splay Trees**: Self-adjusting without height constraint
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

# build a small balanced tree manually
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

draw_tree(root)
```
