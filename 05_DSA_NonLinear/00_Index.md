---
title: Non-Linear Data Structures - Index
tags: [dsa, data-structures, hash-tables, trees, graphs, index]
created: 2026-01-30
type: index
---

# 🌳 Non-Linear Data Structures

> **Beyond arrays and lists - where data gets interesting!**

---

## ✅ Beginner Tips

- Start with **Hash Tables** and compare them to Python `dict`.
- Learn Trees before Graphs.
- Draw small examples on paper as you read.

---

## 📚 Learning Path

### #️⃣ Hash Tables (Chapter 1-3)

| # | Topic | Description | Complexity |
|---|-------|-------------|------------|
| 01 | [[01_Hash_Tables\|Hash Tables]] | Hashing, collisions, load factor | O(1) avg |
| 02 | [[02_Hash_Sets\|Hash Sets]] | Unique elements, set operations | O(1) avg |
| 03 | [[03_Hash_Maps\|Hash Maps]] | Key-value pairs, dictionaries | O(1) avg |

### 🌲 Trees (Chapter 4-10)

| # | Topic | Description | Complexity |
|---|-------|-------------|------------|
| 04 | [[04_Trees\|Trees]] | Tree basics, terminology, types | - |
| 05 | [[05_Binary_Trees\|Binary Trees]] | Binary tree structure, properties | - |
| 06 | [[06_Preorder_Traversal\|Pre-order Traversal]] | Root → Left → Right | O(n) |
| 07 | [[07_Inorder_Traversal\|In-order Traversal]] | Left → Root → Right | O(n) |
| 08 | [[08_Postorder_Traversal\|Post-order Traversal]] | Left → Right → Root | O(n) |
| 09 | [[09_Binary_Search_Trees\|Binary Search Trees]] | BST operations, search, insert | O(log n) avg |
| 10 | [[10_AVL_Trees\|AVL Trees]] | Self-balancing BST, rotations | O(log n) |

### 🕸️ Graphs (Chapter 11-17)

| # | Topic | Description | Complexity |
|---|-------|-------------|------------|
| 11 | [[11_Graphs_I\|Graphs I]] | Graph basics, representations | - |
| 12 | [[12_Graphs_II\|Graphs II]] | Weighted, directed graphs | - |
| 13 | [[13_Graph_Traversals\|Graph Traversals]] | BFS, DFS | O(V+E) |
| 14 | [[14_Cycle_Detection\|Cycle Detection]] | Finding cycles in graphs | O(V+E) |
| 15 | [[15_Shortest_Path\|Shortest Path]] | Path finding algorithms | varies |
| 16 | [[16_Dijkstras\|Dijkstra's Algorithm]] | Single-source shortest path | O((V+E)log V) |
| 17 | [[17_Bellman_Ford\|Bellman-Ford Algorithm]] | Handles negative weights | O(VE) |

---

## ✅ Practice (Beginner-Friendly)

- [[../06_Exercises/02_Topic_Packs/10_DSA_Nonlinear_Pack|DSA Non-Linear Pack]]
- [[../06_Exercises/02_Topic_Packs/11_Trees_Graphs_Easy_Pack|Trees & Graphs (Easy Pack)]]

---

## 🎯 Quick Reference

### Time Complexity Overview

```
┌─────────────────────────────────────────────────────────────┐
│                  TIME COMPLEXITY                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  HASH TABLES          Average    Worst                      │
│  ─────────────────────────────────────                      │
│  Search               O(1)       O(n)                       │
│  Insert               O(1)       O(n)                       │
│  Delete               O(1)       O(n)                       │
│                                                             │
│  BINARY SEARCH TREE   Average    Worst (unbalanced)        │
│  ─────────────────────────────────────                      │
│  Search               O(log n)   O(n)                       │
│  Insert               O(log n)   O(n)                       │
│  Delete               O(log n)   O(n)                       │
│                                                             │
│  AVL TREE             All Cases                             │
│  ─────────────────────────────────────                      │
│  Search               O(log n)                              │
│  Insert               O(log n)                              │
│  Delete               O(log n)                              │
│                                                             │
│  GRAPHS               Time          Space                   │
│  ─────────────────────────────────────                      │
│  BFS/DFS              O(V + E)      O(V)                    │
│  Dijkstra             O((V+E)log V) O(V)                    │
│  Bellman-Ford         O(V * E)      O(V)                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔗 Related Resources

| Resource | Description |
|----------|-------------|
| [[00_Cheatsheet\|🎯 Quick Cheatsheet]] | All algorithms at a glance |
| [[../04_DSA_Linear/00_Index\|📚 Linear Structures]] | Arrays, Lists, Stacks, Queues |
| [[../02_Python_Advanced/00_Index\|🐍 Python Advanced]] | Python implementation details |

---

## 📊 Statistics

```
Non-Linear Data Structures Vault
├── 17 Main chapters
├── 3 Sections (Hash, Trees, Graphs)
├── ~200 Code examples
├── ASCII visualizations
└── Complexity analysis
```

---

*Created for DSA exam preparation* 🎓
