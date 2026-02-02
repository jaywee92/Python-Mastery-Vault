# DSA Non-Linear Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** Hash tables, trees, graphs

Notebook: [[10_DSA_Nonlinear_Pack.ipynb]]

---

## N1: Word Frequency (Hash Map)
**Task:** Count word frequency in a sentence.

```python
text = "hello hello world"
# expected: {"hello": 2, "world": 1}
```

> [!hint]- 💡 Hint 1 (Low)
> Use a dictionary to store counts.

> [!hint]- 💡 Hint 2 (Mid)
> Split the text into words using `split()`.

> [!hint]- 💡 Hint 3 (High)
> `counts[word] = counts.get(word, 0) + 1`

> [!success]- ✅ Solution
> ```python
> def word_count(text):
>     counts = {}
>     for word in text.split():
>         counts[word] = counts.get(word, 0) + 1
>     return counts
> 
> print(word_count("hello hello world"))
> # {'hello': 2, 'world': 1}
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
> The output is `A B C`.

> [!success]- ✅ Solution
> ```python
> # Preorder: Root, Left, Right
> # A B C
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

## N10: Two Sum (Hash Map)
**Task:** Return indices of two values that sum to target.

```python
nums = [2, 7, 11, 15]
target = 9
# expected: [0, 1]
```

> [!hint]- 💡 Hint 1 (Low)
> Store numbers you have already seen.

> [!hint]- 💡 Hint 2 (Mid)
> Check if `target - num` is in the dictionary.

> [!hint]- 💡 Hint 3 (High)
> Store value → index for fast lookup.

> [!success]- ✅ Solution
> ```python
> def two_sum(nums, target):
>     seen = {}
>     for i, num in enumerate(nums):
>         need = target - num
>         if need in seen:
>             return [seen[need], i]
>         seen[num] = i
>     return []
> 
> print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
> ```

---

## DN1: Count Tree Nodes
**Task:** Solve the task below.

```python
# count nodes in tree
```

> [!hint]- 💡 Hint 1 (Low)
> Use recursion or BFS/DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a visited set for graphs.

> [!hint]- 💡 Hint 3 (High)
> Use small helper functions.

> [!success]- ✅ Solution
> ```python
> class Node:
>     def __init__(self,v,l=None,r=None):
>         self.v=v; self.l=l; self.r=r
>
> def count(n):
>     if n is None: return 0
>     return 1+count(n.l)+count(n.r)
>
> root=Node(1,Node(2),Node(3))
> print(count(root))
> ```

---

---

## DN2: Tree Sum
**Task:** Solve the task below.

```python
# sum nodes
```

> [!hint]- 💡 Hint 1 (Low)
> Use recursion or BFS/DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a visited set for graphs.

> [!hint]- 💡 Hint 3 (High)
> Use small helper functions.

> [!success]- ✅ Solution
> ```python
> def sum_tree(n):
>     if n is None: return 0
>     return n.v + sum_tree(n.l)+sum_tree(n.r)
>
> print(sum_tree(root))
> ```

---

---

## DN3: BST Search
**Task:** Solve the task below.

```python
# search 7
```

> [!hint]- 💡 Hint 1 (Low)
> Use recursion or BFS/DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a visited set for graphs.

> [!hint]- 💡 Hint 3 (High)
> Use small helper functions.

> [!success]- ✅ Solution
> ```python
> class Node:
>     def __init__(self,v,l=None,r=None):
>         self.v=v; self.l=l; self.r=r
>
> def search(n,x):
>     if n is None: return False
>     if n.v==x: return True
>     return search(n.l,x) if x<n.v else search(n.r,x)
>
> root=Node(10,Node(5),Node(15))
> print(search(root, 15))
> ```

---

---

## DN4: Graph Neighbors
**Task:** Solve the task below.

```python
graph={'A':['B','C']}
# expected: ['B','C']
```

> [!hint]- 💡 Hint 1 (Low)
> Use recursion or BFS/DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a visited set for graphs.

> [!hint]- 💡 Hint 3 (High)
> Use small helper functions.

> [!success]- ✅ Solution
> ```python
> graph={'A':['B','C']}
> print(graph.get('A',[]))
> ```

---

---

## DN5: BFS Order
**Task:** Solve the task below.

```python
graph={'A':['B'], 'B':['C'], 'C':[]}
# from A
```

> [!hint]- 💡 Hint 1 (Low)
> Use recursion or BFS/DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a visited set for graphs.

> [!hint]- 💡 Hint 3 (High)
> Use small helper functions.

> [!success]- ✅ Solution
> ```python
> from collections import deque
>
> def bfs(g,s):
>     q=deque([s]); seen={s}; out=[]
>     while q:
>         n=q.popleft(); out.append(n)
>         for nb in g.get(n,[]):
>             if nb not in seen:
>                 seen.add(nb); q.append(nb)
>     return out
>
> print(bfs({'A':['B'], 'B':['C'], 'C':[]}, 'A'))
> ```

---

---

## DN6: DFS Order
**Task:** Solve the task below.

```python
graph={'A':['B','C'],'B':[],'C':[]}
# from A
```

> [!hint]- 💡 Hint 1 (Low)
> Use recursion or BFS/DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a visited set for graphs.

> [!hint]- 💡 Hint 3 (High)
> Use small helper functions.

> [!success]- ✅ Solution
> ```python
> def dfs(g,s,seen=None):
>     if seen is None: seen=set()
>     seen.add(s); out=[s]
>     for nb in g.get(s,[]):
>         if nb not in seen:
>             out.extend(dfs(g,nb,seen))
>     return out
>
> print(dfs({'A':['B','C'],'B':[],'C':[]}, 'A'))
> ```

---

---

## DN7: First Unique
**Task:** Solve the task below.

```python
text='aabcc'
# expected: 'b'
```

> [!hint]- 💡 Hint 1 (Low)
> Use recursion or BFS/DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a visited set for graphs.

> [!hint]- 💡 Hint 3 (High)
> Use small helper functions.

> [!success]- ✅ Solution
> ```python
> text='aabcc'
> counts={}
> for ch in text:
>     counts[ch]=counts.get(ch,0)+1
> res=''
> for ch in text:
>     if counts[ch]==1:
>         res=ch
>         break
> print(res)
> ```

---

---

## DN8: Level Order
**Task:** Solve the task below.

```python
# tree level order
```

> [!hint]- 💡 Hint 1 (Low)
> Use recursion or BFS/DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a visited set for graphs.

> [!hint]- 💡 Hint 3 (High)
> Use small helper functions.

> [!success]- ✅ Solution
> ```python
> from collections import deque
>
> def level_order(root):
>     if root is None: return []
>     q=deque([root]); res=[]
>     while q:
>         level=[]
>         for _ in range(len(q)):
>             n=q.popleft(); level.append(n.v)
>             if n.l: q.append(n.l)
>             if n.r: q.append(n.r)
>         res.append(level)
>     return res
>
> print(level_order(root))
> ```

---

---

## DN9: Valid BST
**Task:** Solve the task below.

```python
# check BST
```

> [!hint]- 💡 Hint 1 (Low)
> Use recursion or BFS/DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a visited set for graphs.

> [!hint]- 💡 Hint 3 (High)
> Use small helper functions.

> [!success]- ✅ Solution
> ```python
> def is_bst(n,low=float('-inf'),high=float('inf')):
>     if n is None: return True
>     if not (low < n.v < high): return False
>     return is_bst(n.l,low,n.v) and is_bst(n.r,n.v,high)
>
> print(is_bst(root))
> ```

---

---

## DN10: Graph Path Exists
**Task:** Solve the task below.

```python
# path from A to C
```

> [!hint]- 💡 Hint 1 (Low)
> Use recursion or BFS/DFS.

> [!hint]- 💡 Hint 2 (Mid)
> Keep a visited set for graphs.

> [!hint]- 💡 Hint 3 (High)
> Use small helper functions.

> [!success]- ✅ Solution
> ```python
> def path_exists(g,s,t):
>     stack=[s]; seen=set()
>     while stack:
>         n=stack.pop()
>         if n==t: return True
>         if n in seen: continue
>         seen.add(n)
>         for nb in g.get(n,[]):
>             stack.append(nb)
>     return False
>
> print(path_exists({'A':['B'], 'B':['C'], 'C':[]}, 'A','C'))
> ```

---

---
