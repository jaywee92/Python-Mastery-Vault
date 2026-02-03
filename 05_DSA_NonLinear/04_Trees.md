---
title: Trees
tags: [dsa, tree, node, root, leaf, height, depth, data-structure]
created: 2026-01-30
difficulty: intermediate
time_complexity: varies
space_complexity: O(n)
---

# 🌳 Trees

[[00_Index|← Back to Index]] | [[05_Binary_Trees|Binary Trees →]]

> **"Trees: Hierarchical thinking made concrete"**

---

## 🎯 The Concept

```
┌─────────────────────────────────────────────────────────────────┐
│                    WHAT IS A TREE?                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A Tree is a hierarchical data structure composed of nodes      │
│  connected by edges, with a single root node and no cycles.     │
│                                                                  │
│  KEY PROPERTIES:                                                │
│  • One ROOT node (no parent)                                    │
│  • Every other node has exactly ONE parent                      │
│  • NO CYCLES (acyclic structure)                                │
│  • Connected structure (all nodes reachable from root)          │
│                                                                  │
│                       SIMPLE TREE                               │
│                                                                  │
│                           A (ROOT)                              │
│                          / | \                                  │
│                         B  C  D                                 │
│                        /|     |                                 │
│                       E F     G                                 │
│                                                                  │
│  Nodes: A, B, C, D, E, F, G                                    │
│  Edges: Connections between parent-child pairs                  │
│  Root: A (top node, no parent)                                 │
│  Leaves: E, F, C, G (nodes with no children)                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✅ Beginner-Friendly Python Example

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

root = Node("A")
child_b = Node("B")
child_c = Node("C")

root.children.append(child_b)
root.children.append(child_c)

print(root.value)            # A
print(root.children[0].value)  # B
```

This is a **general tree** where each node can have many children.

---

## 📚 Tree Terminology

```
┌─────────────────────────────────────────────────────────────────┐
│                    TREE TERMINOLOGY                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                        A                                        │
│                      /   \                                      │
│                     B     C                                     │
│                    / \   / \                                    │
│                   D   E F   G                                   │
│                  /                                              │
│                 H                                               │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ TERM           │ MEANING                                │   │
│  ├────────────────┼─────────────────────────────────────────┤   │
│  │ ROOT           │ A (top node, no parent)               │   │
│  │ LEAF/TERMINAL  │ D, E, F, G, H (nodes with no kids)   │   │
│  │ INTERNAL NODE  │ A, B, C (nodes with children)         │   │
│  │ PARENT         │ B is parent of D, E; A is parent of B │   │
│  │ CHILD          │ D, E are children of B                │   │
│  │ SIBLING        │ D and E are siblings (same parent)    │   │
│  │ ANCESTOR       │ A, B are ancestors of D               │   │
│  │ DESCENDANT     │ E, B, D are descendants of A          │   │
│  │ SUBTREE        │ Node B and all its descendants        │   │
│  │ EDGE           │ Connection between parent and child   │   │
│  │ PATH           │ A→B→D→H (sequence of nodes)           │   │
│  └────────────────┴─────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📏 Tree Measurements

```
┌─────────────────────────────────────────────────────────────────┐
│                    HEIGHT, DEPTH, LEVEL                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                        A (LEVEL 0)                              │
│                      /   \                                      │
│                     B     C (LEVEL 1)                           │
│                    / \   / \                                    │
│                   D   E F   G (LEVEL 2)                         │
│                  /                                              │
│                 H (LEVEL 3)                                     │
│                                                                  │
│  HEIGHT: Maximum distance from node to a leaf                  │
│    • Height of H = 0 (leaf node)                               │
│    • Height of D = 1 (distance to furthest leaf H)             │
│    • Height of B = 2 (distance to furthest leaf D→H)           │
│    • Height of A = 3 (root, distance to H)                     │
│    • Height of tree = Height of root = 3                       │
│                                                                  │
│  DEPTH: Distance from root to a specific node                  │
│    • Depth of A = 0 (root node)                                │
│    • Depth of B = 1 (one step from root)                       │
│    • Depth of D = 2 (two steps from root)                      │
│    • Depth of H = 3 (three steps from root)                    │
│                                                                  │
│  LEVEL: All nodes at the same distance from root               │
│    • Level 0: {A}                                              │
│    • Level 1: {B, C}                                           │
│    • Level 2: {D, E, F, G}                                     │
│    • Level 3: {H}                                              │
│                                                                  │
│  Height-related Definitions:                                    │
│    • Height of a leaf node = 0                                 │
│    • Height of empty tree = -1 or undefined                    │
│    • Height of single node tree = 0                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🌲 Types of Trees

### 1. Binary Tree
```
Maximum 2 children per node

         A
        / \
       B   C
      / \
     D   E

Max nodes at level i: 2^i
Max total nodes with height h: 2^(h+1) - 1
```

### 2. N-ary Tree (General Tree)
```
Any number of children per node

         A
       / | \ \
      B  C  D E
     /|    |
    F G    H

Example: File system, organization charts
```

### 3. Balanced Tree
```
Height difference between left and right subtrees ≤ 1

         A              (Balanced)
        / \
       B   C
      / \
     D   E

         A              (Unbalanced)
        /
       B
      /
     C
    /
   D
```

### 4. Full Tree
```
Every node has 0 or maximum children (no partial nodes)

         A
        / \
       B   C
      / \
     D   E

Every node has either 0 or 2 children
```

### 5. Complete Tree
```
All levels completely filled except possibly last level
Last level filled from left to right

         A
        / \
       B   C
      / \ / \
     D  E F  G

All levels full, or last level has nodes pushed to left
```

### 6. Perfect Tree
```
All internal nodes have 2 children & all leaves at same level

         A
        / \
       B   C
      / \ / \
     D  E F  G

All levels completely filled
Total nodes = 2^(h+1) - 1
```

---

## 🔗 Tree Properties

```python
# ═══════════════════════════════════════════════════════════════
# TREE PROPERTIES
# ═══════════════════════════════════════════════════════════════

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        """Add a child node."""
        self.children.append(child)


# PROPERTY 1: Number of nodes at level i
# For binary tree: 2^i nodes (maximum)
# Example: Level 0 has 2^0 = 1 node (root)
#          Level 1 has 2^1 = 2 nodes
#          Level 2 has 2^2 = 4 nodes

# PROPERTY 2: Maximum nodes in tree with height h
# For binary tree: 2^(h+1) - 1 total nodes
# Example: Height 0 (single node) = 2^1 - 1 = 1 node
#          Height 2 = 2^3 - 1 = 7 nodes
#          Height 3 = 2^4 - 1 = 15 nodes

# PROPERTY 3: Minimum height for n nodes
# For binary tree: h >= log2(n+1) - 1
# Rearranged: h >= ceil(log2(n+1)) - 1

# PROPERTY 4: Relationship between internal and leaf nodes
# For full binary tree: leaf_nodes = internal_nodes + 1

# PROPERTY 5: Number of edges in tree with n nodes
# Edges = n - 1 (tree is acyclic, connected graph)

# Example tree verification
root = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)

# This tree has:
# - 5 nodes (A, B, C, D, E)
# - 4 edges (A-B, A-C, B-D, B-E)
# - Height 2
# - Levels: {A}, {B,C}, {D,E}
```

---

## 🏗️ Basic Tree Node Implementation

```python
# ═══════════════════════════════════════════════════════════════
# TREE NODE - GENERAL N-ARY TREE
# ═══════════════════════════════════════════════════════════════

class TreeNode:
    """A node in a general tree (any number of children)."""

    def __init__(self, value):
        """Initialize a tree node.

        Args:
            value: The data stored in this node
        """
        self.value = value
        self.children = []  # List of child nodes

    def add_child(self, child):
        """Add a child node.

        Args:
            child: TreeNode to add as a child
        """
        if isinstance(child, TreeNode):
            self.children.append(child)
        else:
            raise ValueError("Child must be a TreeNode instance")

    def remove_child(self, child):
        """Remove a child node.

        Args:
            child: TreeNode to remove
        """
        if child in self.children:
            self.children.remove(child)

    def is_leaf(self):
        """Check if this node is a leaf (has no children)."""
        return len(self.children) == 0

    def is_root(self, parent=None):
        """Check if this node is a root."""
        return parent is None

    def get_degree(self):
        """Get the number of children."""
        return len(self.children)

    def __repr__(self):
        return f"TreeNode({self.value})"


# Usage Example
root = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)

print(f"Root: {root.value}")
print(f"Root children: {[child.value for child in root.children]}")  # ['B', 'C']
print(f"B degree: {b.get_degree()}")  # 2
print(f"D is leaf: {d.is_leaf()}")    # True
print(f"B is leaf: {b.is_leaf()}")    # False
```

---

## 🔍 Basic Tree Operations

### Tree Traversal

```python
# ═══════════════════════════════════════════════════════════════
# TREE TRAVERSALS (Using N-ary tree)
# ═══════════════════════════════════════════════════════════════

def traverse_preorder(node):
    """Visit node BEFORE its children.

    Order: node → left → middle → right
    Useful for: copying tree, prefix expression
    """
    if node is None:
        return

    print(node.value, end=" ")  # Process node first

    for child in node.children:
        traverse_preorder(child)


def traverse_postorder(node):
    """Visit node AFTER its children.

    Order: left → middle → right → node
    Useful for: deleting tree, postfix expression
    """
    if node is None:
        return

    for child in node.children:
        traverse_postorder(child)

    print(node.value, end=" ")  # Process node last


def traverse_levelorder(root):
    """Visit nodes level by level (breadth-first).

    Order: All level 0 → all level 1 → all level 2 → ...
    Useful for: finding shortest path, tree visualization
    """
    if root is None:
        return

    from collections import deque
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        for child in node.children:
            queue.append(child)


# Example tree:
#         A
#       / | \
#      B  C  D
#     /|
#    E F

root = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')

root.add_child(b)
root.add_child(c)
root.add_child(d)
b.add_child(e)
b.add_child(f)

print("Preorder (NLR):   ", end="")
traverse_preorder(root)      # A B E F C D
print()

print("Postorder (LRN):  ", end="")
traverse_postorder(root)     # E F B C D A
print()

print("Level Order (BFS):", end="")
traverse_levelorder(root)    # A B C D E F
print()
```

### Basic Search

```python
# ═══════════════════════════════════════════════════════════════
# BASIC TREE SEARCH
# ═══════════════════════════════════════════════════════════════

def search_tree(root, target):
    """Search for a value in the tree (DFS).

    Args:
        root: Root node of the tree
        target: Value to search for

    Returns:
        TreeNode if found, None otherwise
    """
    if root is None:
        return None

    if root.value == target:
        return root

    # Search in children
    for child in root.children:
        result = search_tree(child, target)
        if result is not None:
            return result

    return None


def search_tree_bfs(root, target):
    """Search for a value using BFS (level-order).

    Args:
        root: Root node of the tree
        target: Value to search for

    Returns:
        TreeNode if found, None otherwise
    """
    if root is None:
        return None

    from collections import deque
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.value == target:
            return node

        for child in node.children:
            queue.append(child)

    return None


# Usage
found = search_tree(root, 'F')
if found:
    print(f"Found: {found.value}")  # Found: F
else:
    print("Not found")

found_bfs = search_tree_bfs(root, 'C')
print(f"Found via BFS: {found_bfs.value}")  # Found via BFS: C
```

---

## 💡 Common Use Cases

```
┌─────────────────────────────────────────────────────────────────┐
│                    TREE USE CASES                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. FILE SYSTEMS                                                │
│     Root: /                                                      │
│     ├── home/                                                    │
│     │   ├── user1/                                               │
│     │   │   ├── Documents/                                       │
│     │   │   └── Downloads/                                       │
│     │   └── user2/                                               │
│     └── var/                                                     │
│                                                                  │
│  2. ORGANIZATION CHARTS                                         │
│     CEO (Root)                                                   │
│     ├── VP Engineering                                           │
│     │   ├── Backend Team Lead                                    │
│     │   └── Frontend Team Lead                                   │
│     └── VP Marketing                                             │
│                                                                  │
│  3. DOM (Document Object Model)                                 │
│     <html>                                                       │
│     ├── <head>                                                   │
│     │   ├── <title>                                              │
│     │   └── <meta>                                               │
│     └── <body>                                                   │
│         ├── <div>                                                │
│         └── <p>                                                  │
│                                                                  │
│  4. EXPRESSION TREES                                            │
│            *                                                     │
│           / \                                                    │
│          +   3                                                   │
│         / \                                                      │
│        2   1  → represents: (2 + 1) * 3                         │
│                                                                  │
│  5. DIRECTORY TREES (Git commits, database indices)              │
│                                                                  │
│  6. GAME DEVELOPMENT (Scene graphs)                              │
│                                                                  │
│  7. COMPILER DESIGN (Abstract Syntax Trees - AST)                │
│                                                                  │
│  8. TAXONOMIES & CLASSIFICATIONS                                │
│     Animal (Root)                                                │
│     ├── Mammal                                                   │
│     │   ├── Dog                                                  │
│     │   └── Cat                                                  │
│     └── Reptile                                                  │
│         └── Snake                                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎓 Tree Representation Comparisons

```python
# ═══════════════════════════════════════════════════════════════
# DIFFERENT TREE REPRESENTATIONS
# ═══════════════════════════════════════════════════════════════

# 1. PARENT POINTER ARRAY (Implicit parent information)
parent = [-1, 0, 0, 1, 1]  # Index is node, value is parent
#        A(0)
#        / \
#       B(1) C(2)
#      / \
#    D(3) E(4)

# Pros: Simple, space-efficient
# Cons: Can't easily access children

# 2. CHILD POINTER ARRAY (Explicit children information)
children = [
    [1, 2],      # Node A: children B(1), C(2)
    [3, 4],      # Node B: children D(3), E(4)
    [],          # Node C: no children
    [],          # Node D: no children
    []           # Node E: no children
]

# Pros: Easy to access children
# Cons: Need to know max children count

# 3. LINKED STRUCTURE (Dynamic - TreeNode class)
# Already shown above - most flexible, OOP approach

# 4. ARRAY REPRESENTATION (Implicit structure for complete trees)
tree_array = [
    'A',        # Index 0 = root
    'B', 'C',   # Index 1, 2 = level 1
    'D', 'E',   # Index 3, 4 = level 2 (partial)
]
# For complete binary tree:
# Parent of index i: (i-1)//2
# Left child: 2*i + 1
# Right child: 2*i + 2

# Most flexible and OOP: Linked TreeNode structure
```

---

## 📊 Time Complexity Summary

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| **Search** | O(n) | O(h) | n = nodes, h = height (recursion stack) |
| **Insert** | O(n) | O(h) | Find parent then add child |
| **Delete** | O(n) | O(h) | Find node then remove |
| **Traversal** | O(n) | O(h) | Visit all nodes |
| **Find Height** | O(n) | O(h) | Must visit all nodes |
| **Space (n nodes)** | - | O(n) | Storage for all nodes |

**Key Insight:** In a balanced tree, h ≈ log(n), so operations are O(log n) on average. In an unbalanced tree, h can be n, making operations O(n).

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Forgetting to initialize children list
class BadTreeNode:
    def __init__(self, value):
        self.value = value
        # Missing: self.children = []

# ✅ RIGHT: Always initialize collection
class GoodTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


# ❌ WRONG: Modifying collection while iterating
for child in node.children:
    if child.value < 0:
        node.children.remove(child)  # Dangerous!

# ✅ RIGHT: Iterate over a copy
for child in list(node.children):
    if child.value < 0:
        node.children.remove(child)


# ❌ WRONG: Not handling circular references
node.children.append(node)  # Creates cycle!

# ✅ RIGHT: Trees have no cycles (acyclic property)
# Verify this when building the tree


# ❌ WRONG: Confusion between height and depth
def get_height_wrong(node):
    """This counts depth from current node."""
    return 0  # Wrong approach

# ✅ RIGHT: Height is distance to furthest leaf
def get_height(node):
    """Return height of subtree rooted at node."""
    if node is None:
        return -1

    max_child_height = -1
    for child in node.children:
        max_child_height = max(max_child_height, get_height(child))

    return max_child_height + 1


# ❌ WRONG: Recursive traversal without base case
def traverse_infinite(node):
    print(node.value)
    for child in node.children:
        traverse_infinite(child)  # Always recurses, no proper base case

# ✅ RIGHT: Always check for None
def traverse_correct(node):
    if node is None:
        return

    print(node.value)
    for child in node.children:
        traverse_correct(child)
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Use TreeNode class for clarity | Use raw nested lists/dicts |
| Understand height vs depth | Confuse the two concepts |
| Check for None/empty tree | Assume tree is non-empty |
| Use appropriate traversal | Wrong traversal for use case |
| Maintain acyclic property | Create cycles accidentally |
| Document parent-child relationships | Ambiguous structure |
| Use recursion for natural fit | Force iteration unnecessarily |
| Store references safely | Create multiple copies |

---

## 🎯 Exam Checklist

- [ ] Tree has exactly one root node
- [ ] Every non-root node has one parent
- [ ] Trees are acyclic (no cycles)
- [ ] Connected structure (all nodes reachable from root)
- [ ] Tree with n nodes has exactly n-1 edges
- [ ] Height = maximum distance from root to leaf
- [ ] Depth = distance of node from root
- [ ] Leaf node = node with no children
- [ ] Binary tree = max 2 children per node
- [ ] Complete tree = all levels full except possibly last level
- [ ] Perfect tree = all levels completely filled
- [ ] Full tree = every node has 0 or maximum children
- [ ] Preorder = process node before children (NLR)
- [ ] Postorder = process node after children (LRN)
- [ ] Level-order = breadth-first traversal
- [ ] TreeNode implementation with value and children list
- [ ] TreeNode must initialize children list in __init__
- [ ] Tree traversal requires base case (None check)
- [ ] Maximum nodes at level i = 2^i (for binary tree)
- [ ] Maximum total nodes with height h = 2^(h+1) - 1 (binary tree)

---

[[00_Index|← Index]] | [[05_Binary_Trees|Binary Trees →]]
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

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

draw_tree(root)

```
