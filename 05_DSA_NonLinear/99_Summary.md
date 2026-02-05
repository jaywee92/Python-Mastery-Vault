---
title: DSA NonLinear - Summary
tags: [dsa, summary, trees, graphs, hash, non-linear]
created: 2026-02-05
---

# DSA NonLinear - Summary

## 📋 Overview

Non-linear data structures enable efficient modeling of complex relationships between data. This module covers three main categories: hash-based structures (for fast lookups), trees (for hierarchical data), and graphs (for network structures). Each category offers different operations and complexities.

---

## 📊 Complexity Overview

### Hash-Based Structures

```
┌────────────────────┬──────────────┬──────────────┬─────────────┐
│ Operation          │ Hash Table   │ Hash Set     │ Hash Map    │
├────────────────────┼──────────────┼──────────────┼─────────────┤
│ Insert/Put         │ O(1)*        │ O(1)*        │ O(1)*       │
│ Delete/Remove      │ O(1)*        │ O(1)*        │ O(1)*       │
│ Search/Contains    │ O(1)*        │ O(1)*        │ O(1)*       │
│ Iteration          │ O(n)         │ O(n)         │ O(n)        │
│ Space              │ O(n)         │ O(n)         │ O(n)        │
├────────────────────┼──────────────┼──────────────┼─────────────┤
│ Worst Case         │ O(n)         │ O(n)         │ O(n)        │
│ Load Factor        │ α < 0.75     │ α < 0.75     │ α < 0.75    │
└────────────────────┴──────────────┴──────────────┴─────────────┘
* Average case (with good hash function)
```

### Trees

```
┌──────────────────────┬──────────────────┬──────────────────┬──────────┐
│ Operation            │ BST Average      │ BST Worst        │ AVL Tree │
├──────────────────────┼──────────────────┼──────────────────┼──────────┤
│ Search               │ O(log n)         │ O(n)             │ O(log n) │
│ Insert               │ O(log n)         │ O(n)             │ O(log n) │
│ Delete               │ O(log n)         │ O(n)             │ O(log n) │
│ Space                │ O(n)             │ O(n)             │ O(n)     │
│ Find Min/Max         │ O(log n)         │ O(n)             │ O(log n) │
├──────────────────────┼──────────────────┼──────────────────┼──────────┤
│ Balance Factor       │ No guarantee     │ No guarantee     │ |h_l-h_r| ≤ 1 │
│ Rebalancing          │ No               │ No               │ Yes (rotations) │
└──────────────────────┴──────────────────┴──────────────────┴──────────┘
```

### Graphs

```
┌──────────────────────────┬──────────────┬──────────────┐
│ Algorithm                │ Time         │ Space        │
├──────────────────────────┼──────────────┼──────────────┤
│ BFS/DFS                  │ O(V + E)     │ O(V)         │
│ Dijkstra (with heap)     │ O((V+E)logV) │ O(V)         │
│ Bellman-Ford             │ O(VE)        │ O(V)         │
│ Floyd-Warshall (all-pairs)│ O(V³)       │ O(V²)        │
│ Cycle detection (DFS)    │ O(V + E)     │ O(V)         │
├──────────────────────────┼──────────────┼──────────────┤
│ Adjacency list space     │ -            │ O(V + E)     │
│ Adjacency matrix space   │ -            │ O(V²)        │
└──────────────────────────┴──────────────┴──────────────┘
```

---

## 📝 Topic Summaries

### 1. Hash Tables
Hash tables map keys to values by converting the key to an array index using a hash function. They enable average O(1) operations but require collision handling (chaining or linear probing). The load factor determines when resizing is necessary.

**Key Concepts:** Hash function, collision resolution, load factor, chaining vs. open addressing

### 2. Hash Sets
Hash sets store unique elements and use a hash table internally (keys only, no values). They offer O(1) average operations for add, remove, and contains, with automatic duplicate elimination. Perfect for fast membership tests and duplicate detection.

**Key Concepts:** Uniqueness, set operations (union, intersection, difference), frozenset

### 3. Hash Maps
Hash maps (dictionaries) store key-value pairs with O(1) average lookups. Keys must be unique and hashable, values can be anything. They support operations like `.get()` with defaults, `defaultdict` for automatic defaults, and are ordered in Python 3.7+.

**Key Concepts:** Key-value mapping, safe access, defaultdict, counter

### 4. Trees (General)
Trees are hierarchical structures with a root node and parent-child relationships without cycles. They consist of nodes and edges, where each non-root node has exactly one parent. Important measures are height (max. distance to leaf) and depth (distance from root).

**Key Concepts:** Root, leaves, height vs. depth, traversals (preorder, postorder, level-order)

### 5. Binary Trees
Binary trees limit each node to at most 2 children (left/right). They can be categorized: full, complete, perfect, balanced. The `TreeNode` pattern stores value, left, and right pointers. They form the basis for specialized structures like BSTs.

**Key Concepts:** Left/right pointers, tree types, traversals, complete vs. perfect

### 6. Tree Traversals (Preorder, Inorder, Postorder)
Traversals visit all nodes in different orders. Preorder processes node before children (N-L-R), inorder processes between children (L-N-R, produces sorted order in BSTs), postorder processes after children (L-R-N). Level-order (BFS) visits all nodes at each level.

**Key Concepts:** DFS vs. BFS, traversal order, recursive vs. iterative implementation

### 7. Binary Search Trees (BST)
BSTs arrange nodes so that left < node < right recursively. They enable O(log n) search by eliminating half the tree per comparison. Problem: unbalanced BSTs degenerate to O(n). Inorder traversal produces sorted order.

**Key Concepts:** BST property, search/insert/delete, unbalance problem, successor/predecessor

### 8. AVL Trees
AVL trees are self-balancing BSTs with balance factor |h_left - h_right| ≤ 1. They guarantee O(log n) for all operations through automatic rotations (left, right, left-right, right-left). They're more strictly balanced than red-black trees but costlier to maintain.

**Key Concepts:** Balance factor, rotations, self-balancing, guaranteed O(log n)

### 9. Graphs - Basics
Graphs consist of vertices (nodes) and edges (links), represented as G = (V, E). They can be directed (A→B), undirected (A-B), weighted (cost) or unweighted. Two main representations: adjacency list (sparse) and adjacency matrix (dense).

**Key Concepts:** Vertices, edges, directed/undirected, weighted/unweighted, representations

### 10. Graph Traversals (BFS & DFS)
BFS (breadth-first) explores level-by-level with a queue, good for shortest paths in unweighted graphs. DFS (depth-first) explores as deeply as possible with stack/recursion, good for cycle detection and topological sorting. Both have complexity O(V + E).

**Key Concepts:** Queue vs. stack, visited tracking, BFS order vs. DFS order, applications

### 11. Cycle Detection
Cycle detection determines if a graph contains cycles. Undirected: if during DFS a neighbor (except parent) is visited. Directed: 3-color schema (white/gray/black) - if redirected to gray node, it's a cycle. O(V + E) time.

**Key Concepts:** Cycle definition, white-gray-black marking, undirected vs. directed detection

### 12. Shortest Path Algorithms
Shortest path finds the path with minimum weight between two nodes. Dijkstra (O((V+E)logV)) works with non-negative weights using greedy approach. Bellman-Ford (O(VE)) also works with negative weights. Floyd-Warshall (O(V³)) finds all-pairs shortest paths.

**Key Concepts:** Weight/cost, Dijkstra vs. Bellman-Ford, negative weights, all-pairs

### 13. Dijkstra's Algorithm
Dijkstra's is a greedy algorithm that always chooses the next unvisited node. It maintains dist[] array and visits nodes in ascending distance order. With min-heap as priority queue: O((V+E)logV). Works only with non-negative edge weights.

**Key Concepts:** Greedy choice, distance array, priority queue, single-source shortest path

### 14. Bellman-Ford Algorithm
Bellman-Ford relaxes all edges V-1 times, finding shortest paths to all nodes. O(VE) time. Works with negative weights and can detect negative cycles. Slower than Dijkstra but more universally applicable.

**Key Concepts:** Edge relaxation, negative weights, negative cycle detection, all-sources

---

## ✅ Self-Test Checklist

### Hash Structures
- [ ] I can explain hash functions and their properties
- [ ] I understand collision resolution (chaining vs. linear probing)
- [ ] I know load factor and when resizing is necessary
- [ ] I can justify O(1) average time for hash operations
- [ ] I know differences between hash table, hash set, and hash map
- [ ] I can correctly use set() and dict operations in Python
- [ ] I understand why only hashable objects can be keys/set elements

### Trees
- [ ] I can explain tree definition (root, leaves, acyclic)
- [ ] I correctly distinguish height vs. depth
- [ ] I can implement all tree traversals (preorder, inorder, postorder, level)
- [ ] I understand TreeNode with value, left, and right pointers
- [ ] I know properties of binary trees (full, complete, perfect, balanced)
- [ ] I can explain BST property and implement BST operations
- [ ] I understand AVL tree balance factor and rotations
- [ ] I know why AVL trees guarantee O(log n)

### Graphs
- [ ] I distinguish vertices vs. edges and directed vs. undirected graphs
- [ ] I can use adjacency list and adjacency matrix representations
- [ ] I can implement BFS with queue and DFS with stack/recursion
- [ ] I understand cycle detection with DFS and 3-color schema
- [ ] I can implement Dijkstra's algorithm with priority queue
- [ ] I understand Bellman-Ford and why it handles negative weights
- [ ] I know when to use which shortest-path algorithm
- [ ] I can predict graph traversal results (order, distances)

### Implementation & Practice
- [ ] I can implement a simple hash table with chaining
- [ ] I can implement TreeNode with insert/search/delete
- [ ] I can represent a graph with adjacency list
- [ ] I can perform BFS and DFS on a given graph
- [ ] I can optimally solve problems with hash sets/maps (two sum, etc.)
- [ ] I understand time/space tradeoffs between hash vs. tree vs. graph structures
- [ ] I can choose between implementations based on requirements

---

## 🛤️ Recommended Learning Path

### Phase 1: Understanding Basics (Days 1-3)
```
Hash Tables
    ↓
Hash Sets
    ↓
Hash Maps
    ↓
Self-test: Practice dict/set operations in Python
```

### Phase 2: Tree Foundations (Days 4-7)
```
Trees (General)
    ↓
Binary Trees
    ↓
Tree Traversals (Pre/In/Post/Level)
    ↓
Lab: Traversal implementations
```

### Phase 3: Specialized Trees (Days 8-10)
```
Binary Search Trees
    ↓
AVL Trees & Rotations
    ↓
Lab: BST insert/delete, AVL rebalancing
```

### Phase 4: Graph Introduction (Days 11-13)
```
Graphs - Basics & Representations
    ↓
Graph Traversals (BFS & DFS)
    ↓
Lab: Graph building, BFS/DFS implementation
```

### Phase 5: Graph Algorithms (Days 14-18)
```
Cycle Detection
    ↓
Shortest Path Overview
    ↓
Dijkstra's Algorithm
    ↓
Bellman-Ford Algorithm
    ↓
Lab: Implement all shortest-path algorithms
```

### Phase 6: Integration & Interview Prep (Days 19-20)
```
Review complexity tables
    ↓
Solve interview problems (LeetCode medium)
    ↓
Decision logic: Which DS for which problem?
```

---

## 🎯 Common Interview Questions

### Hash-Based Structures
- "Design a LRU cache" → HashMap + doubly linked list
- "Two sum" → HashSet/HashMap for O(n)
- "Group anagrams" → HashMap with sorted string as key
- "Valid anagram" → Character frequency with counter
- "Longest substring without repeating" → Sliding window + HashMap

### Trees
- "Inorder traversal" → Recursive or stack-based
- "Lowest common ancestor" → Use BST properties
- "Validate BST" → Inorder should be sorted
- "Balance a BST" → In-place balancing
- "Height balanced tree?" → Recursive checking with balance factor

### Graphs
- "Clone a graph" → DFS/BFS with visited set
- "Course schedule" → Cycle detection (topological sort)
- "Number of islands" → DFS/BFS on 2D grid
- "Network delay time" → Dijkstra or BFS
- "Reorder routes to make all paths lead to zero" → BFS with parent tracking

---

## 💡 Performance Comparison Cheat Sheet

```
Operation               Hash Table    BST          AVL Tree     Graph (BFS/DFS)
─────────────────────────────────────────────────────────────────────────────
Search unsorted data   O(1)*         O(log n)**   O(log n)     O(V+E)***
Insert                 O(1)*         O(log n)**   O(log n)     O(1) add edge
Delete                 O(1)*         O(log n)**   O(log n)     O(V+E) removal
Min/Max                O(n)          O(log n)     O(log n)     O(V+E)
Sorted traversal       O(n)          O(n)         O(n)         O(V+E)
Space                  O(n)          O(n)         O(n)         O(V+E)

* Average case (good hash function)
** If balanced; O(n) worst-case if degenerated
*** Depending on algorithm; O(V) to O(V²) typically

WHEN TO USE:
────────────────────────────────────────────────────────────────────────────
Hash table/set/map:    Fast membership testing, frequency counting, caching
Binary search tree:    Sorted iteration needed, range queries
AVL tree:              Guaranteed O(log n), strict balancing needed
Graph (BFS/DFS):       Connected components, shortest paths, dependency analysis
Dijkstra:              Single-source shortest path, non-negative weights
Bellman-Ford:          Negative weights allowed, all-pairs analysis
```

---

## 🔑 Critical Concepts Summary

### Hash-Based Structures
- Hash function converts key → index (should distribute uniformly)
- Load factor = entries / buckets (typical: resize at α > 0.75)
- Collision resolution through chaining (linked list) or probing
- Average O(1), worst O(n) with poor distribution
- Python dict is insertion-ordered since 3.7+

### Trees
- Height = longest path to leaf (leaf = height 0)
- Depth = distance from root (root = depth 0)
- Preorder (NLR): node before children → copying, prefix expression
- Inorder (LNR): node between children → sorted output for BST
- Postorder (LRN): node after children → deletion, postfix expression
- BST: Valid only if ALL left < node < ALL right (recursively)
- AVL: Balance factor of each node must be in [-1, 0, 1]
- Rotations (single/double) rebalance AVL after insert/delete

### Graphs
- V vertices + E edges; typical: E = O(V²) dense, O(V) sparse
- Adjacency list: O(V+E) space, O(degree) access time
- Adjacency matrix: O(V²) space, O(1) access time
- BFS: queue, level-by-level, shortest unweighted paths
- DFS: stack/recursion, depth-first, cycle detection, topological sort
- Dijkstra: greedy, positive weights only, single-source
- Bellman-Ford: DP, negative weights OK, negative-cycle detection
- Cycle detection: directed = 3-color (W/G/B), undirected = back edges

---

## 📚 Related Concepts for Deepening

1. **Heap / Priority Queue** - Efficient priority-based operations (O(log n))
2. **Trie** - Prefix-based search for strings
3. **Union-Find** - Disjoint sets, minimum spanning tree
4. **Topological Sorting** - DAG ordering via DFS
5. **Minimum Spanning Tree** - Kruskal's, Prim's algorithms
6. **Red-Black Trees** - Alternative to AVL (less strict balancing)
7. **B-Trees** - Multi-way trees for disk-based searching
8. **Segment Trees / Fenwick Trees** - Range queries & updates

---

*This summary covers core concepts of non-linear data structures. For deeper understanding, see individual topic files.*
