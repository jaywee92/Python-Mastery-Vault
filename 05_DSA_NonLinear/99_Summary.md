---
title: DSA NonLinear - Summary
tags: [dsa, summary, trees, graphs, hash, non-linear]
created: 2026-02-05
---

# DSA NonLinear - Zusammenfassung

## 📋 Überblick

Nicht-lineare Datenstrukturen ermöglichen es, komplexe Beziehungen zwischen Daten effizient zu modellieren. Dieses Modul behandelt drei Hauptkategorien: Hash-basierte Strukturen (für schnelle Lookups), Bäume (für hierarchische Daten) und Graphen (für Netzwerk-Strukturen). Jede Kategorie bietet unterschiedliche Operationen und Komplexitäten.

---

## 📊 Komplexitäts-Übersicht

### Hash-basierte Strukturen

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
* Average case (bei guter Hash-Funktion)
```

### Bäume

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
│ Balance Factor       │ Keine Garantie   │ Keine Garantie   │ |h_l-h_r| ≤ 1 │
│ Rebalancing          │ Nein             │ Nein             │ Ja (Rotationen) │
└──────────────────────┴──────────────────┴──────────────────┴──────────┘
```

### Graphen

```
┌──────────────────────────┬──────────────┬──────────────┐
│ Algorithmus              │ Zeit         │ Space        │
├──────────────────────────┼──────────────┼──────────────┤
│ BFS/DFS                  │ O(V + E)     │ O(V)         │
│ Dijkstra (mit Heap)      │ O((V+E)logV) │ O(V)         │
│ Bellman-Ford             │ O(VE)        │ O(V)         │
│ Floyd-Warshall (all-pairs)│ O(V³)       │ O(V²)        │
│ Cycle Detection (DFS)    │ O(V + E)     │ O(V)         │
├──────────────────────────┼──────────────┼──────────────┤
│ Adjacency List Space     │ -            │ O(V + E)     │
│ Adjacency Matrix Space   │ -            │ O(V²)        │
└──────────────────────────┴──────────────┴──────────────┘
```

---

## 📝 Topic-Zusammenfassungen

### 1. Hash Tables
Hash Tables bilden Keys auf Values ab, indem eine Hash-Funktion den Key in einen Array-Index konvertiert. Sie ermöglichen durchschnittlich O(1) Operationen, erfordern aber Kollisionsbehandlung (Chaining oder Linear Probing). Der Load Factor bestimmt, wann eine Vergrößerung notwendig ist.

**Wichtige Konzepte:** Hash-Funktion, Collision Resolution, Load Factor, Chaining vs. Open Addressing

### 2. Hash Sets
Hash Sets speichern eindeutige Elemente und verwenden einen Hash-Table intern (nur Schlüssel, keine Werte). Sie bieten O(1) durchschnittliche Operationen für Add, Remove und Contains, mit automatischer Duplikat-Elimination. Perfekt für schnelle Membership-Tests und Duplicate-Detection.

**Wichtige Konzepte:** Eindeutigkeit, Set Operations (Union, Intersection, Difference), frozenset

### 3. Hash Maps
Hash Maps (Dictionaries) speichern Key-Value-Paare mit O(1) durchschnittlichen Lookups. Keys müssen unique und hashable sein, Values können beliebig sein. Sie unterstützen Operationen wie `.get()` mit Defaults, `defaultdict` für automatische Default-Werte und sind in Python 3.7+ ordered.

**Wichtige Konzepte:** Key-Value-Mapping, Safe Access, defaultdict, Counter

### 4. Trees (Allgemein)
Bäume sind hierarchische Strukturen mit einem Root-Node und Parent-Child-Beziehungen ohne Zyklen. Sie bestehen aus Knoten und Kanten, wobei jeder non-root Node genau einen Parent hat. Wichtige Messgrößen sind Höhe (max. Abstand zu Blatt) und Tiefe (Abstand von Root).

**Wichtige Konzepte:** Root, Leaves, Height vs. Depth, Traversals (Preorder, Postorder, Level-Order)

### 5. Binary Trees
Binary Trees begrenzen jeden Node auf maximal 2 Kinder (Left/Right). Sie können in Typen kategorisiert werden: Full, Complete, Perfect, Balanced. Das `TreeNode`-Muster speichert value, left und right Zeiger. Sie bilden die Grundlage für spezialisierte Strukturen wie BSTs.

**Wichtige Konzepte:** Left/Right Pointers, Tree Types, Traversals, Complete vs. Perfect

### 6. Tree Traversals (Preorder, Inorder, Postorder)
Traversierungen besuchen alle Nodes in unterschiedlichen Reihenfolgen. Preorder verarbeitet Node vor Kindern (N-L-R), Inorder verarbeitet zwischen Kindern (L-N-R, erzeugt sortierte Reihenfolge in BSTs), Postorder verarbeitet nach Kindern (L-R-N). Level-Order (BFS) besucht alle Nodes einer Ebene.

**Wichtige Konzepte:** DFS vs. BFS, Traversal Order, Recursive vs. Iterative Implementation

### 7. Binary Search Trees (BST)
BSTs ordnen Nodes so an, dass Left < Node < Right rekursiv erfüllt ist. Sie ermöglichen O(log n) Suche durch Elimination halber des Baums pro Vergleich. Das Problem: Unbalancierte BSTs degenerieren zu O(n). Inorder-Traversal erzeugt sortierte Reihenfolge.

**Wichtige Konzepte:** BST Property, Search/Insert/Delete, Unbalance Problem, Successor/Predecessor

### 8. AVL Trees
AVL Trees sind selbst-balancierende BSTs mit Balance Factor |h_left - h_right| ≤ 1. Sie garantieren O(log n) für alle Operationen durch automatische Rotationen (Left, Right, Left-Right, Right-Left). Sie sind strikter balanciert als Red-Black Trees, aber teurer in Wartung.

**Wichtige Konzepte:** Balance Factor, Rotations, Self-Balancing, Guaranteed O(log n)

### 9. Graphs - Basics
Graphen bestehen aus Vertices (Knoten) und Edges (Kanten), representiert als G = (V, E). Sie können directed (A→B), undirected (A-B), weighted (Kosten) oder unweighted sein. Zwei Hauptrepräsentationen: Adjacency List (sparsam) und Adjacency Matrix (dicht).

**Wichtige Konzepte:** Vertices, Edges, Directed/Undirected, Weighted/Unweighted, Representations

### 10. Graph Traversals (BFS & DFS)
BFS (Breadth-First) erkundet Level-by-Level mit einer Queue, gut für kürzeste Pfade in ungewichteten Graphen. DFS (Depth-First) erkundet tiefstmöglich mit Stack/Rekursion, gut für Cycle Detection und Topological Sorting. Beide haben Komplexität O(V + E).

**Wichtige Konzepte:** Queue vs. Stack, Visited Tracking, BFS Order vs. DFS Order, Anwendungen

### 11. Cycle Detection
Cycle Detection bestimmt, ob ein Graph Zyklen enthält. Undirected: Wenn während DFS ein Neighbor (außer Parent) besucht wird. Directed: 3-Color-Schema (White/Gray/Black) - wenn zu Gray-Node geleitet wird, ist es ein Cycle. O(V + E) Zeit.

**Wichtige Konzepte:** Cycle Definition, White-Gray-Black Marking, Undirected vs. Directed Detection

### 12. Shortest Path Algorithms
Shortest Path findet den Weg mit minimalem Gewicht zwischen zwei Knoten. Dijkstra (O((V+E)logV)) arbeitet mit nicht-negativen Gewichten mittels Greedy-Ansatz. Bellman-Ford (O(VE)) funktioniert auch mit negativen Gewichten. Floyd-Warshall (O(V³)) findet All-Pairs-Shortest-Paths.

**Wichtige Konzepte:** Weight/Cost, Dijkstra vs. Bellman-Ford, Negative Weights, All-Pairs

### 13. Dijkstra's Algorithm
Dijkstra's ist ein Greedy-Algorithmus, der immer den nächsten unbesuchten Knoten wählt. Er verwaltet dist[] array und besucht Knoten in aufsteigender Entfernung. Mit Min-Heap als Priority Queue: O((V+E)logV). Funktioniert nur mit nicht-negativen Kantengewichten.

**Wichtige Konzepte:** Greedy Choice, Distance Array, Priority Queue, Single-Source Shortest Path

### 14. Bellman-Ford Algorithm
Bellman-Ford relaxiert alle Edges V-1 Mal, wodurch kürzeste Pfade zu allen Knoten gefunden werden. O(VE) Zeit. Funktioniert mit negativen Gewichten und kann negative Zyklen erkennen. Langsamerer als Dijkstra, aber universeller einsetzbar.

**Wichtige Konzepte:** Edge Relaxation, Negative Weights, Negative Cycle Detection, All-Sources

---

## ✅ Selbsttest-Checkliste

### Hash Structures
- [ ] Ich kann Hash-Funktionen und deren Eigenschaften erklären
- [ ] Ich verstehe Collision Resolution (Chaining vs. Linear Probing)
- [ ] Ich kenne Load Factor und wann Resizing notwendig ist
- [ ] Ich kann O(1) durchschnittliche Zeit für Hash Operations begründen
- [ ] Ich kenne die Unterschiede zwischen Hash Table, Hash Set und Hash Map
- [ ] Ich kann set() und dict operations in Python korrekt nutzen
- [ ] Ich verstehe, warum nur hashable Objects als Keys/Set Elements fungieren

### Trees
- [ ] Ich kann die Definition eines Baums erklären (Root, Leaves, Acyclic)
- [ ] Ich unterscheide Height vs. Depth korrekt
- [ ] Ich kann alle Tree Traversals (Preorder, Inorder, Postorder, Level) implementieren
- [ ] Ich verstehe TreeNode mit value, left und right Pointern
- [ ] Ich kenne die Properties von Binary Trees (Full, Complete, Perfect, Balanced)
- [ ] Ich kann BST Property erklären und BST Operations implementieren
- [ ] Ich verstehe AVL Tree Balance Factor und Rotationen
- [ ] Ich weiß, warum AVL Trees O(log n) garantieren

### Graphs
- [ ] Ich unterscheide Vertices vs. Edges und directed vs. undirected Graphs
- [ ] Ich kann Adjacency List und Adjacency Matrix Representationen nutzen
- [ ] Ich kann BFS mit Queue und DFS mit Stack/Rekursion implementieren
- [ ] Ich verstehe Cycle Detection mit DFS und 3-Color-Schema
- [ ] Ich kann Dijkstra's Algorithm mit Priority Queue implementieren
- [ ] Ich verstehe Bellman-Ford und warum es negative Weights handhabt
- [ ] Ich weiß, wann welcher Shortest-Path-Algorithmus zu nutzen ist
- [ ] Ich kann Graph Traversal Results (Order, Distances) vorhersagen

### Implementierung & Praxis
- [ ] Ich kann eine einfache Hash Table mit Chaining implementieren
- [ ] Ich kann einen TreeNode mit Insert/Search/Delete implementieren
- [ ] Ich kann einen Graph mit Adjacency List darstellen
- [ ] Ich kann BFS und DFS auf einem gegebenen Graph durchführen
- [ ] Ich kann Probleme mit Hash Sets/Maps optimal lösen (Two Sum, etc.)
- [ ] Ich verstehe Time/Space Tradeoffs zwischen Hash vs. Tree vs. Graph Strukturen
- [ ] Ich kann zwischen Implementierungen basierend auf Anforderungen wählen

---

## 🛤️ Empfohlener Lernpfad

### Phase 1: Grundlagen verstehen (Tage 1-3)
```
Hash Tables
    ↓
Hash Sets
    ↓
Hash Maps
    ↓
Selbsttest: Dict/Set Operationen in Python üben
```

### Phase 2: Tree Foundations (Tage 4-7)
```
Trees (Allgemein)
    ↓
Binary Trees
    ↓
Tree Traversals (Pre/In/Post/Level)
    ↓
Praktikum: Traversal Implementations
```

### Phase 3: Specialized Trees (Tage 8-10)
```
Binary Search Trees
    ↓
AVL Trees & Rotations
    ↓
Praktikum: BST Insert/Delete, AVL Rebalancing
```

### Phase 4: Graphs Einleitung (Tage 11-13)
```
Graphs - Basics & Representations
    ↓
Graph Traversals (BFS & DFS)
    ↓
Praktikum: Graph Building, BFS/DFS Implementation
```

### Phase 5: Graph Algorithmen (Tage 14-18)
```
Cycle Detection
    ↓
Shortest Path Überblick
    ↓
Dijkstra's Algorithm
    ↓
Bellman-Ford Algorithm
    ↓
Praktikum: Alle Shortest-Path-Algorithmen implementieren
```

### Phase 6: Integration & Interview Prep (Tage 19-20)
```
Review Complexity Tables
    ↓
Interviewing Problems lösen (LeetCode Medium)
    ↓
Entscheidungslogik: Welche DS für welches Problem?
```

---

## 🎯 Häufige Interview-Fragen

### Hash-basierte Strukturen
- "Design a LRU Cache" → HashMap + Doubly Linked List
- "Two Sum" → HashSet/HashMap für O(n)
- "Group Anagrams" → HashMap mit Sorted String als Key
- "Valid Anagram" → Character Frequency mit Counter
- "Longest Substring Without Repeating" → Sliding Window + HashMap

### Bäume
- "Inorder Traversal" → Recursive oder Stack-based
- "Lowest Common Ancestor" → BST Properties nutzen
- "Validate BST" → Inorder sollte sortiert sein
- "Balance a BST" → In-place Balancing
- "Height Balanced Tree?" → Rekursives Checking mit Balance Factor

### Graphen
- "Clone a Graph" → DFS/BFS mit Visited Set
- "Course Schedule" → Cycle Detection (Topological Sort)
- "Number of Islands" → DFS/BFS auf 2D Grid
- "Network Delay Time" → Dijkstra oder BFS
- "Reorder Routes to Make All Paths Lead to Zero" → BFS mit Parent Tracking

---

## 💡 Performance-Vergleich Cheat Sheet

```
Operation               Hash Table    BST          AVL Tree     Graph (BFS/DFS)
─────────────────────────────────────────────────────────────────────────────
Search Unsorted Data   O(1)*         O(log n)**   O(log n)     O(V+E)***
Insert                 O(1)*         O(log n)**   O(log n)     O(1) add edge
Delete                 O(1)*         O(log n)**   O(log n)     O(V+E) removal
Min/Max                O(n)          O(log n)     O(log n)     O(V+E)
Sorted Traversal       O(n)          O(n)         O(n)         O(V+E)
Space                  O(n)          O(n)         O(n)         O(V+E)

* Average case (good hash function)
** If balanced; O(n) worst-case if degenerated
*** Depending on algorithm; O(V) to O(V²) typically

WHEN TO USE:
────────────────────────────────────────────────────────────────────────────
Hash Table/Set/Map:    Fast membership testing, Frequency counting, Caching
Binary Search Tree:    Sorted iteration needed, Range queries
AVL Tree:              Guaranteed O(log n), Strict balancing needed
Graph (BFS/DFS):       Connected components, Shortest paths, Dependency analysis
Dijkstra:              Single-source shortest path, Non-negative weights
Bellman-Ford:          Negative weights allowed, All-pairs analysis
```

---

## 🔑 Kritische Konzepte zusammengefasst

### Hash-basierte Strukturen
- Hash-Funktion konvertiert Key → Index (sollte uniform verteilen)
- Load Factor = entries / buckets (typisch: Resize bei α > 0.75)
- Collision Resolution durch Chaining (linked list) oder Probing
- Average O(1), Worst O(n) bei schlechter Distribution
- Python dict ist insertion-ordered seit 3.7+

### Bäume
- Height = längster Pfad zu Blatt (Leaf = Höhe 0)
- Depth = Abstand von Root (Root = Tiefe 0)
- Preorder (NLR): Node vor Kindern → Kopieren, Prefix-Expression
- Inorder (LNR): Node zwischen Kindern → Sortierer Output für BST
- Postorder (LRN): Node nach Kindern → Löschen, Postfix-Expression
- BST: Nur gültig wenn ALLE Left < Node < ALLE Right (rekursiv)
- AVL: Balance Factor jedes Nodes muss in [-1, 0, 1] sein
- Rotationen (Single/Double) rebalancieren AVL nach Insert/Delete

### Graphen
- V Vertices + E Edges; typisch: E = O(V²) dicht, O(V) sparsam
- Adjacency List: O(V+E) space, O(degree) access time
- Adjacency Matrix: O(V²) space, O(1) access time
- BFS: Queue, Level-by-Level, kürzeste ungewichtete Pfade
- DFS: Stack/Recursion, Depth-First, Cycle Detection, Topological Sort
- Dijkstra: Greedy, nur positive Weights, Single-Source
- Bellman-Ford: DP, negative Weights OK, Negative-Cycle Detection
- Cycle Detection: Directed = 3-Color (W/G/B), Undirected = Back Edges

---

## 📚 Verwandte Konzepte zur Vertiefung

1. **Heap / Priority Queue** - Effiziente Prioritäts-basierte Operationen (O(log n))
2. **Trie** - Prefix-basierte Suche für Strings
3. **Union-Find** - Disjunkte Mengen, Minimum Spanning Tree
4. **Topological Sorting** - DAG-Ordering via DFS
5. **Minimum Spanning Tree** - Kruskal's, Prim's Algorithms
6. **Red-Black Trees** - Alternate zu AVL (weniger strict balancing)
7. **B-Trees** - Multi-way trees für Disk-based searching
8. **Segment Trees / Fenwick Trees** - Range queries & updates

---

*Diese Zusammenfassung fasst die Kernkonzepte der nicht-linearen Datenstrukturen zusammen. Für tieferes Verständnis, siehe die individuellen Topic-Dateien.*
