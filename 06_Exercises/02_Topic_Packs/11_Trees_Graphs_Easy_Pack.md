# Trees & Graphs (Easy Pack)

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** Intro tree/graph practice

Notebook: [[11_Trees_Graphs_Easy_Pack.ipynb]]

---

## T1: Count Nodes (Binary Tree)
**Task:** Count how many nodes are in the tree.

```
    1
   / \
  2   3
```

Expected: `3`

> [!hint]- 💡 Hint 1 (Low)
> Use recursion.

> [!hint]- 💡 Hint 2 (Mid)
> Count current node + left + right.

> [!hint]- 💡 Hint 3 (High)
> Base case: `None` returns 0.

> [!success]- ✅ Solution
> ```python
> class Node:
>     def __init__(self, value, left=None, right=None):
>         self.value = value
>         self.left = left
>         self.right = right
> 
> def count_nodes(node):
>     if node is None:
>         return 0
>     return 1 + count_nodes(node.left) + count_nodes(node.right)
> 
> root = Node(1, Node(2), Node(3))
> print(count_nodes(root))  # 3
> ```

---

---

## T2: Tree Height
**Task:** Return the height of a binary tree (edges on longest path).

```
    1
   /
  2
 /
3
```

Expected: `2`

> [!hint]- 💡 Hint 1 (Low)
> Height = 1 + max(left, right).

> [!hint]- 💡 Hint 2 (Mid)
> Base case: empty tree has height -1.

> [!hint]- 💡 Hint 3 (High)
> Use recursion and `max`.

> [!success]- ✅ Solution
> ```python
> def height(node):
>     if node is None:
>         return -1
>     return 1 + max(height(node.left), height(node.right))
> 
> root = Node(1, Node(2, Node(3)))
> print(height(root))  # 2
> ```

---

---

## T3: Sum of Tree Values
**Task:** Return the sum of all values.

```
    5
   / \
  3   7
```

Expected: `15`

> [!hint]- 💡 Hint 1 (Low)
> Add root + left + right.

> [!hint]- 💡 Hint 2 (Mid)
> Use recursion.

> [!hint]- 💡 Hint 3 (High)
> Base case: empty tree returns 0.

> [!success]- ✅ Solution
> ```python
> def sum_tree(node):
>     if node is None:
>         return 0
>     return node.value + sum_tree(node.left) + sum_tree(node.right)
> 
> root = Node(5, Node(3), Node(7))
> print(sum_tree(root))  # 15
> ```

---

---

## G1: Graph Neighbors
**Task:** Return the neighbors of a node.

```python
graph = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"],
}
# neighbors of "A" -> ["B", "C"]
```

> [!hint]- 💡 Hint 1 (Low)
> Look up the key in the dictionary.

> [!hint]- 💡 Hint 2 (Mid)
> Use `graph.get(node, [])`.

> [!hint]- 💡 Hint 3 (High)
> Return the list directly.

> [!success]- ✅ Solution
> ```python
> def neighbors(graph, node):
>     return graph.get(node, [])
> 
> g = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
> print(neighbors(g, "A"))  # ['B', 'C']
> ```

---

---

## G2: BFS Order (Small Graph)
**Task:** Return BFS order from a starting node.

```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": [],
}
# expected from A: ['A', 'B', 'C', 'D']
```

> [!hint]- 💡 Hint 1 (Low)
> BFS uses a queue.

> [!hint]- 💡 Hint 2 (Mid)
> Add neighbors when you visit a node.

> [!hint]- 💡 Hint 3 (High)
> Use `deque` and `popleft()`.

> [!success]- ✅ Solution
> ```python
> from collections import deque
> 
> def bfs(graph, start):
>     visited = set([start])
>     order = []
>     queue = deque([start])
>     while queue:
>         node = queue.popleft()
>         order.append(node)
>         for neighbor in graph.get(node, []):
>             if neighbor not in visited:
>                 visited.add(neighbor)
>                 queue.append(neighbor)
>     return order
> 
> g = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
> print(bfs(g, "A"))  # ['A', 'B', 'C', 'D']
> ```

---

---

## G3: DFS Order (Small Graph)
**Task:** Return DFS order from a starting node.

```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": [],
}
# expected from A: ['A', 'B', 'D', 'C']
```

> [!hint]- 💡 Hint 1 (Low)
> DFS uses recursion or a stack.

> [!hint]- 💡 Hint 2 (Mid)
> Visit deep before going wide.

> [!hint]- 💡 Hint 3 (High)
> Use recursion with a visited set.

> [!success]- ✅ Solution
> ```python
> def dfs(graph, start, visited=None):
>     if visited is None:
>         visited = set()
>     visited.add(start)
>     order = [start]
>     for neighbor in graph.get(start, []):
>         if neighbor not in visited:
>             order.extend(dfs(graph, neighbor, visited))
>     return order
> 
> g = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}
> print(dfs(g, "A"))  # ['A', 'B', 'D', 'C']
> ```

---
