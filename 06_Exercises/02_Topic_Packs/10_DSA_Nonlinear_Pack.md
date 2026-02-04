# DSA Non-Linear Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** Hash tables, trees, graphs

Notebook: [[10_DSA_Nonlinear_Pack.ipynb]]

---

## N1: Anagram Check (Hash Map)
**Task:** Return `True` if two words are anagrams (same letters, different order).

```python
word1 = "listen"
word2 = "silent"
# expected: True
```

> [!hint]- 💡 Hint 1 (Low)
> Count how many times each letter appears.

> [!hint]- 💡 Hint 2 (Mid)
> Use a dictionary for counts.

> [!hint]- 💡 Hint 3 (High)
> Compare the two dictionaries.

> [!success]- ✅ Solution
> ```python
> def letter_counts(word):
>     counts = {}
>     for ch in word:
>         counts[ch] = counts.get(ch, 0) + 1
>     return counts
> 
> def is_anagram(a, b):
>     return letter_counts(a) == letter_counts(b)
> 
> print(is_anagram("listen", "silent"))  # True
> ```

---

---

## N2: Simple Tree (Preorder)
**Task:** Return preorder traversal for this tree.

```
    A
   / \
  B   C
```

Expected: `A B C`

> [!hint]- 💡 Hint 1 (Low)
> Preorder means: Root, Left, Right.

> [!hint]- 💡 Hint 2 (Mid)
> Visit `A`, then `B`, then `C`.

> [!hint]- 💡 Hint 3 (High)
> Use a simple recursive function.

> [!success]- ✅ Solution
> ```python
> class Node:
>     def __init__(self, value, left=None, right=None):
>         self.value = value
>         self.left = left
>         self.right = right
> 
> def preorder(node, out):
>     if node is None:
>         return
>     # 1) Visit root
>     out.append(node.value)
>     # 2) Visit left subtree
>     preorder(node.left, out)
>     # 3) Visit right subtree
>     preorder(node.right, out)
> 
> root = Node("A", Node("B"), Node("C"))
> result = []
> preorder(root, result)
> print(" ".join(result))  # A B C
> ```

---

---

## N3: Graph Neighbors
**Task:** Print all neighbors of node `"B"`.

```python
graph = {
    "A": ["B", "D"],
    "B": ["A", "C", "E"],
    "C": ["B"],
    "D": ["A", "E"],
    "E": ["B", "D"],
}
```

> [!hint]- 💡 Hint 1 (Low)
> Look up the key `"B"` in the dictionary.

> [!hint]- 💡 Hint 2 (Mid)
> The neighbors are already stored in a list.

> [!hint]- 💡 Hint 3 (High)
> `graph["B"]` is the answer.

> [!success]- ✅ Solution
> ```python
> print(graph["B"])  # ['A', 'C', 'E']
> ```

---

---

## N4: BFS Order
**Task:** Return BFS order starting at `"A"`.

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}
# expected: ['A', 'B', 'C', 'D']
```

> [!hint]- 💡 Hint 1 (Low)
> BFS uses a queue.

> [!hint]- 💡 Hint 2 (Mid)
> Add neighbors when you visit a node.

> [!hint]- 💡 Hint 3 (High)
> Use `collections.deque` and `popleft()`.

> [!success]- ✅ Solution
> ```python
> from collections import deque
> 
> def bfs(graph, start):
>     visited = set([start])
>     order = []
>     queue = deque([start])
> 
>     while queue:
>         node = queue.popleft()
>         order.append(node)
>         for neighbor in graph.get(node, []):
>             if neighbor not in visited:
>                 visited.add(neighbor)
>                 queue.append(neighbor)
> 
>     return order
> 
> print(bfs(graph, "A"))  # ['A', 'B', 'C', 'D']
> ```

---

---

## N5: BST Search
**Task:** Search for a value in a BST. Return `True` if found.

```python
# Tree values: 10, 5, 15, 3, 7
# Search for 7 -> True
```

> [!hint]- 💡 Hint 1 (Low)
> Compare the target with the current node.

> [!hint]- 💡 Hint 2 (Mid)
> If target is smaller, go left; if bigger, go right.

> [!hint]- 💡 Hint 3 (High)
> Use recursion to move down the tree.

> [!success]- ✅ Solution
> ```python
> class Node:
>     def __init__(self, value):
>         self.value = value
>         self.left = None
>         self.right = None
> 
> def insert(root, value):
>     if root is None:
>         return Node(value)
>     if value < root.value:
>         root.left = insert(root.left, value)
>     elif value > root.value:
>         root.right = insert(root.right, value)
>     return root
> 
> def search(root, value):
>     if root is None:
>         return False
>     if value == root.value:
>         return True
>     if value < root.value:
>         return search(root.left, value)
>     return search(root.right, value)
> 
> root = None
> for v in [10, 5, 15, 3, 7]:
>     root = insert(root, v)
> 
> print(search(root, 7))  # True
> ```

---

## N6: First Unique Character
**Task:** Return the index of the first non-repeating character, or `-1`.

```python
text = "leetcode"
# expected: 0 ("l")
```

> [!hint]- 💡 Hint 1 (Low)
> Count how often each character appears.

> [!hint]- 💡 Hint 2 (Mid)
> Use a dictionary or `collections.Counter`.

> [!hint]- 💡 Hint 3 (High)
> After counting, scan the string again to find the first count == 1.

> [!success]- ✅ Solution
> ```python
> def first_unique_index(text):
>     counts = {}
>     for ch in text:
>         counts[ch] = counts.get(ch, 0) + 1
>     for i, ch in enumerate(text):
>         if counts[ch] == 1:
>             return i
>     return -1
> 
> print(first_unique_index("leetcode"))  # 0
> ```

---

---

## N7: Level Order Traversal (Tree)
**Task:** Return the values level by level.

```
    1
   / \
  2   3
```

Expected: `[[1], [2, 3]]`

> [!hint]- 💡 Hint 1 (Low)
> Use a queue to process nodes level by level.

> [!hint]- 💡 Hint 2 (Mid)
> Process all nodes currently in the queue for each level.

> [!hint]- 💡 Hint 3 (High)
> Use `len(queue)` to know how many nodes are in the current level.

> [!success]- ✅ Solution
> ```python
> from collections import deque
> 
> class Node:
>     def __init__(self, value, left=None, right=None):
>         self.value = value
>         self.left = left
>         self.right = right
> 
> def level_order(root):
>     if root is None:
>         return []
>     result = []
>     queue = deque([root])
>     while queue:
>         level = []
>         for _ in range(len(queue)):
>             node = queue.popleft()
>             level.append(node.value)
>             if node.left:
>                 queue.append(node.left)
>             if node.right:
>                 queue.append(node.right)
>         result.append(level)
>     return result
> 
> root = Node(1, Node(2), Node(3))
> print(level_order(root))  # [[1], [2, 3]]
> ```

---

---

## N8: Graph Path Exists
**Task:** Return `True` if there is a path from `start` to `target`.

```python
graph = {
    "A": ["B"],
    "B": ["C"],
    "C": [],
}
# start = "A", target = "C" -> True
```

> [!hint]- 💡 Hint 1 (Low)
> Use BFS or DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a set of visited nodes.

> [!hint]- 💡 Hint 3 (High)
> If you reach target, return True.

> [!success]- ✅ Solution
> ```python
> def path_exists(graph, start, target):
>     stack = [start]
>     visited = set()
>     while stack:
>         node = stack.pop()
>         if node == target:
>             return True
>         if node in visited:
>             continue
>         visited.add(node)
>         for neighbor in graph.get(node, []):
>             stack.append(neighbor)
>     return False
> 
> g = {"A": ["B"], "B": ["C"], "C": []}
> print(path_exists(g, "A", "C"))  # True
> ```

---

---

## N9: Valid BST
**Task:** Check if a binary tree is a valid BST.

> [!hint]- 💡 Hint 1 (Low)
> Every node must be in a valid min/max range.

> [!hint]- 💡 Hint 2 (Mid)
> Recurse with updated bounds for left and right.

> [!hint]- 💡 Hint 3 (High)
> Left nodes < current, right nodes > current.

> [!success]- ✅ Solution
> ```python
> class Node:
>     def __init__(self, value, left=None, right=None):
>         self.value = value
>         self.left = left
>         self.right = right
> 
> def is_bst(node, low=float("-inf"), high=float("inf")):
>     if node is None:
>         return True
>     if not (low < node.value < high):
>         return False
>     return is_bst(node.left, low, node.value) and is_bst(node.right, node.value, high)
> 
> root = Node(2, Node(1), Node(3))
> print(is_bst(root))  # True
> ```

---

---

## N10: Contains Duplicate (Set)
**Task:** Return `True` if the list contains any duplicate value.

```python
nums = [1, 2, 3, 1]
# expected: True
```

> [!hint]- 💡 Hint 1 (Low)
> A set keeps only unique values.

> [!hint]- 💡 Hint 2 (Mid)
> Compare the length of the list and the set.

> [!hint]- 💡 Hint 3 (High)
> If lengths differ, there is a duplicate.

> [!success]- ✅ Solution
> ```python
> def has_duplicate(nums):
>     return len(nums) != len(set(nums))
> 
> print(has_duplicate([1, 2, 3, 1]))  # True
> ```
