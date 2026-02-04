---
title: NeetCode 150 Essentials
tags: [python, exercises, neetcode, leetcode, interview, advanced]
created: 2026-02-04
difficulty: medium-hard
type: challenges
---

# 🚀 NeetCode 150 Essentials

> **Beyond Blind 75 - Advanced Problems**
> Source: [NeetCode 150](https://neetcode.io/practice?tab=neetcode150)
> These 25 problems cover advanced patterns not in Blind 75.

---

## 📊 Advanced Categories

| Category | Problems | Key Patterns |
|----------|----------|--------------|
| Stack | 4 | Evaluation, Parsing |
| Graphs | 5 | BFS, DFS, Topological |
| 1D Dynamic Programming | 4 | Memoization, Optimization |
| 2D Dynamic Programming | 4 | Grid, LCS, Edit Distance |
| Tries | 3 | Prefix Trees, Word Search |
| Heap / Priority Queue | 3 | Scheduling, Merging |
| Greedy | 2 | Intervals, Optimization |

---

## 🔷 Stack (Advanced)

### Problem 1: Evaluate Reverse Polish Notation ⭐⭐

Evaluate an expression in Reverse Polish Notation (postfix).

```python
tokens = ["2", "1", "+", "3", "*"]
# Output: 9 ((2 + 1) * 3)
```

> [!hint]- 💡 Hint
> Stack stores operands. When operator appears, pop two operands, compute, push result.

> [!success]- ✅ Solution
> ```python
> def eval_rpn(tokens: list[str]) -> int:
>     stack = []
>     ops = {
>         '+': lambda a, b: a + b,
>         '-': lambda a, b: a - b,
>         '*': lambda a, b: a * b,
>         '/': lambda a, b: int(a / b)  # Truncate toward zero
>     }
>
>     for token in tokens:
>         if token in ops:
>             b, a = stack.pop(), stack.pop()
>             stack.append(ops[token](a, b))
>         else:
>             stack.append(int(token))
>
>     return stack[0]
>
> print(eval_rpn(["2", "1", "+", "3", "*"]))  # 9
> ```
> **Time:** O(n) | **Space:** O(n)

---

### Problem 2: Generate Parentheses ⭐⭐

Generate all valid combinations of n pairs of parentheses.

```python
n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
```

> [!hint]- 💡 Hint
> Backtracking: only add '(' if open < n, only add ')' if close < open.

> [!success]- ✅ Solution
> ```python
> def generate_parenthesis(n: int) -> list[str]:
>     result = []
>
>     def backtrack(s, open_count, close_count):
>         if len(s) == 2 * n:
>             result.append(s)
>             return
>
>         if open_count < n:
>             backtrack(s + '(', open_count + 1, close_count)
>         if close_count < open_count:
>             backtrack(s + ')', open_count, close_count + 1)
>
>     backtrack('', 0, 0)
>     return result
>
> print(generate_parenthesis(3))
> ```
> **Time:** O(4^n / √n) | **Space:** O(n)

---

### Problem 3: Min Stack ⭐⭐

Design a stack that supports push, pop, top, and getMin in O(1).

> 
> [!hint]- 💡 Hint
> Push while iterating, pop when you match a condition.

> [!success]- ✅ Solution
> ```python
> class MinStack:
>     def __init__(self):
>         self.stack = []
>         self.min_stack = []
>
>     def push(self, val: int) -> None:
>         self.stack.append(val)
>         min_val = min(val, self.min_stack[-1] if self.min_stack else val)
>         self.min_stack.append(min_val)
>
>     def pop(self) -> None:
>         self.stack.pop()
>         self.min_stack.pop()
>
>     def top(self) -> int:
>         return self.stack[-1]
>
>     def getMin(self) -> int:
>         return self.min_stack[-1]
> ```

---

### Problem 4: Decode String ⭐⭐

Decode an encoded string like "3[a2[c]]" → "accaccacc".

```python
s = "3[a2[c]]"
# Output: "accaccacc"
```

> [!hint]- 💡 Hint
> Use stack to handle nested brackets. Push current string and count on '[', build on ']'.

> [!success]- ✅ Solution
> ```python
> def decode_string(s: str) -> str:
>     stack = []
>     curr_str = ""
>     curr_num = 0
>
>     for char in s:
>         if char.isdigit():
>             curr_num = curr_num * 10 + int(char)
>         elif char == '[':
>             stack.append((curr_str, curr_num))
>             curr_str = ""
>             curr_num = 0
>         elif char == ']':
>             prev_str, num = stack.pop()
>             curr_str = prev_str + curr_str * num
>         else:
>             curr_str += char
>
>     return curr_str
>
> print(decode_string("3[a2[c]]"))  # "accaccacc"
> ```

---

## 🔷 Graphs

### Problem 5: Number of Islands ⭐⭐

Count the number of islands (connected '1's) in a 2D grid.

```python
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
# Output: 3
```

> 
> [!hint]- 💡 Hint
> BFS for shortest path, DFS for exploring paths.

> [!success]- ✅ Solution
> ```python
> def num_islands(grid: list[list[str]]) -> int:
>     if not grid:
>         return 0
>
>     rows, cols = len(grid), len(grid[0])
>     count = 0
>
>     def dfs(r, c):
>         if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
>             return
>         grid[r][c] = '0'  # Mark visited
>         dfs(r + 1, c)
>         dfs(r - 1, c)
>         dfs(r, c + 1)
>         dfs(r, c - 1)
>
>     for r in range(rows):
>         for c in range(cols):
>             if grid[r][c] == '1':
>                 dfs(r, c)
>                 count += 1
>
>     return count
> ```
> **Time:** O(m × n) | **Space:** O(m × n)

---

### Problem 6: Clone Graph ⭐⭐

Deep copy a connected undirected graph.

> 
> [!hint]- 💡 Hint
> BFS for shortest path, DFS for exploring paths.

> [!success]- ✅ Solution
> ```python
> class Node:
>     def __init__(self, val=0, neighbors=None):
>         self.val = val
>         self.neighbors = neighbors if neighbors else []
>
> def clone_graph(node: Node) -> Node:
>     if not node:
>         return None
>
>     cloned = {}
>
>     def dfs(n):
>         if n in cloned:
>             return cloned[n]
>
>         copy = Node(n.val)
>         cloned[n] = copy
>
>         for neighbor in n.neighbors:
>             copy.neighbors.append(dfs(neighbor))
>
>         return copy
>
>     return dfs(node)
> ```

---

### Problem 7: Course Schedule ⭐⭐

Check if you can finish all courses (detect cycle in directed graph).

```python
numCourses = 2
prerequisites = [[1, 0]]
# Output: True (Take course 0 first, then course 1)
```

> [!hint]- 💡 Hint
> Detect cycle using DFS with three states: unvisited, visiting, visited.

> [!success]- ✅ Solution
> ```python
> def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
>     graph = {i: [] for i in range(numCourses)}
>     for course, prereq in prerequisites:
>         graph[course].append(prereq)
>
>     # 0: unvisited, 1: visiting, 2: visited
>     state = [0] * numCourses
>
>     def has_cycle(course):
>         if state[course] == 1:  # Cycle detected
>             return True
>         if state[course] == 2:  # Already processed
>             return False
>
>         state[course] = 1  # Mark visiting
>
>         for prereq in graph[course]:
>             if has_cycle(prereq):
>                 return True
>
>         state[course] = 2  # Mark visited
>         return False
>
>     for course in range(numCourses):
>         if has_cycle(course):
>             return False
>
>     return True
> ```

---

### Problem 8: Course Schedule II (Topological Sort) ⭐⭐

Return the order to take all courses.

```python
numCourses = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]
# Output: [0, 1, 2, 3] or [0, 2, 1, 3]
```

> 
> [!hint]- 💡 Hint
> BFS for shortest path, DFS for exploring paths.

> [!success]- ✅ Solution
> ```python
> from collections import deque
>
> def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
>     graph = {i: [] for i in range(numCourses)}
>     in_degree = [0] * numCourses
>
>     for course, prereq in prerequisites:
>         graph[prereq].append(course)
>         in_degree[course] += 1
>
>     # Start with courses having no prerequisites
>     queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
>     order = []
>
>     while queue:
>         course = queue.popleft()
>         order.append(course)
>
>         for next_course in graph[course]:
>             in_degree[next_course] -= 1
>             if in_degree[next_course] == 0:
>                 queue.append(next_course)
>
>     return order if len(order) == numCourses else []
> ```

---

### Problem 9: Word Ladder ⭐⭐⭐

Shortest transformation sequence from beginWord to endWord.

```python
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5 (hit → hot → dot → dog → cog)
```

> [!hint]- 💡 Hint
> BFS for shortest path. Generate all possible one-letter changes.

> [!success]- ✅ Solution
> ```python
> from collections import deque
>
> def ladder_length(beginWord: str, endWord: str, wordList: list[str]) -> int:
>     word_set = set(wordList)
>     if endWord not in word_set:
>         return 0
>
>     queue = deque([(beginWord, 1)])
>     visited = {beginWord}
>
>     while queue:
>         word, length = queue.popleft()
>
>         if word == endWord:
>             return length
>
>         for i in range(len(word)):
>             for c in 'abcdefghijklmnopqrstuvwxyz':
>                 next_word = word[:i] + c + word[i+1:]
>                 if next_word in word_set and next_word not in visited:
>                     visited.add(next_word)
>                     queue.append((next_word, length + 1))
>
>     return 0
> ```

---

## 🔷 1D Dynamic Programming

### Problem 10: Coin Change ⭐⭐

Minimum coins to make up amount.

```python
coins = [1, 2, 5]
amount = 11
# Output: 3 (5 + 5 + 1)
```

> [!hint]- 💡 Hint
> dp[i] = minimum coins to make amount i. dp[i] = min(dp[i], dp[i - coin] + 1)

> [!success]- ✅ Solution
> ```python
> def coin_change(coins: list[int], amount: int) -> int:
>     dp = [float('inf')] * (amount + 1)
>     dp[0] = 0
>
>     for i in range(1, amount + 1):
>         for coin in coins:
>             if coin <= i:
>                 dp[i] = min(dp[i], dp[i - coin] + 1)
>
>     return dp[amount] if dp[amount] != float('inf') else -1
>
> print(coin_change([1, 2, 5], 11))  # 3
> ```
> **Time:** O(amount × coins) | **Space:** O(amount)

---

### Problem 11: Word Break ⭐⭐

Check if string can be segmented into dictionary words.

```python
s = "leetcode"
wordDict = ["leet", "code"]
# Output: True
```

> 
> [!hint]- 💡 Hint
> Break into subproblems and store results.

> [!success]- ✅ Solution
> ```python
> def word_break(s: str, wordDict: list[str]) -> bool:
>     word_set = set(wordDict)
>     dp = [False] * (len(s) + 1)
>     dp[0] = True
>
>     for i in range(1, len(s) + 1):
>         for j in range(i):
>             if dp[j] and s[j:i] in word_set:
>                 dp[i] = True
>                 break
>
>     return dp[len(s)]
> ```

---

### Problem 12: Decode Ways ⭐⭐

Count ways to decode a digit string (A=1, B=2, ..., Z=26).

```python
s = "226"
# Output: 3 ("BZ", "VF", "BBF")
```

> [!hint]- 💡 Hint
> Similar to climbing stairs but with validity checks.

> [!success]- ✅ Solution
> ```python
> def num_decodings(s: str) -> int:
>     if not s or s[0] == '0':
>         return 0
>
>     n = len(s)
>     dp = [0] * (n + 1)
>     dp[0] = 1
>     dp[1] = 1
>
>     for i in range(2, n + 1):
>         # Single digit
>         if s[i-1] != '0':
>             dp[i] += dp[i-1]
>         # Two digits
>         two_digit = int(s[i-2:i])
>         if 10 <= two_digit <= 26:
>             dp[i] += dp[i-2]
>
>     return dp[n]
> ```

---

### Problem 13: Maximum Product Subarray ⭐⭐

Find contiguous subarray with largest product.

```python
nums = [2, 3, -2, 4]
# Output: 6 ([2, 3])
```

> [!hint]- 💡 Hint
> Track both max and min at each position (negative × negative = positive).

> [!success]- ✅ Solution
> ```python
> def max_product(nums: list[int]) -> int:
>     result = max(nums)
>     curr_min = curr_max = 1
>
>     for n in nums:
>         if n == 0:
>             curr_min = curr_max = 1
>             continue
>
>         temp = curr_max * n
>         curr_max = max(n * curr_max, n * curr_min, n)
>         curr_min = min(temp, n * curr_min, n)
>
>         result = max(result, curr_max)
>
>     return result
> ```

---

## 🔷 2D Dynamic Programming

### Problem 14: Unique Paths ⭐⭐

Count paths from top-left to bottom-right (only right or down).

```python
m, n = 3, 7
# Output: 28
```

> 
> [!hint]- 💡 Hint
> Break into subproblems and store results.

> [!success]- ✅ Solution
> ```python
> def unique_paths(m: int, n: int) -> int:
>     dp = [[1] * n for _ in range(m)]
>
>     for i in range(1, m):
>         for j in range(1, n):
>             dp[i][j] = dp[i-1][j] + dp[i][j-1]
>
>     return dp[m-1][n-1]
>
> # Space optimized O(n)
> def unique_paths_v2(m: int, n: int) -> int:
>     dp = [1] * n
>     for _ in range(1, m):
>         for j in range(1, n):
>             dp[j] += dp[j-1]
>     return dp[-1]
> ```

---

### Problem 15: Longest Common Subsequence ⭐⭐

Find length of LCS of two strings.

```python
text1 = "abcde"
text2 = "ace"
# Output: 3 ("ace")
```

> [!hint]- 💡 Hint
> dp[i][j] = LCS of text1[:i] and text2[:j]. If chars match, dp[i-1][j-1] + 1.

> [!success]- ✅ Solution
> ```python
> def longest_common_subsequence(text1: str, text2: str) -> int:
>     m, n = len(text1), len(text2)
>     dp = [[0] * (n + 1) for _ in range(m + 1)]
>
>     for i in range(1, m + 1):
>         for j in range(1, n + 1):
>             if text1[i-1] == text2[j-1]:
>                 dp[i][j] = dp[i-1][j-1] + 1
>             else:
>                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
>
>     return dp[m][n]
> ```

---

### Problem 16: Edit Distance ⭐⭐⭐

Minimum operations (insert, delete, replace) to convert word1 to word2.

```python
word1 = "horse"
word2 = "ros"
# Output: 3
```

> 
> [!hint]- 💡 Hint
> Break into subproblems and store results.

> [!success]- ✅ Solution
> ```python
> def min_distance(word1: str, word2: str) -> int:
>     m, n = len(word1), len(word2)
>     dp = [[0] * (n + 1) for _ in range(m + 1)]
>
>     # Base cases
>     for i in range(m + 1):
>         dp[i][0] = i
>     for j in range(n + 1):
>         dp[0][j] = j
>
>     for i in range(1, m + 1):
>         for j in range(1, n + 1):
>             if word1[i-1] == word2[j-1]:
>                 dp[i][j] = dp[i-1][j-1]
>             else:
>                 dp[i][j] = 1 + min(
>                     dp[i-1][j],      # Delete
>                     dp[i][j-1],      # Insert
>                     dp[i-1][j-1]     # Replace
>                 )
>
>     return dp[m][n]
> ```

---

### Problem 17: Interleaving String ⭐⭐⭐

Check if s3 is formed by interleaving s1 and s2.

```python
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
# Output: True
```

> 
> [!hint]- 💡 Hint
> Break into subproblems and store results.

> [!success]- ✅ Solution
> ```python
> def is_interleave(s1: str, s2: str, s3: str) -> bool:
>     m, n = len(s1), len(s2)
>     if m + n != len(s3):
>         return False
>
>     dp = [[False] * (n + 1) for _ in range(m + 1)]
>     dp[0][0] = True
>
>     # Initialize first row and column
>     for i in range(1, m + 1):
>         dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
>     for j in range(1, n + 1):
>         dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
>
>     for i in range(1, m + 1):
>         for j in range(1, n + 1):
>             dp[i][j] = (
>                 (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or
>                 (dp[i][j-1] and s2[j-1] == s3[i+j-1])
>             )
>
>     return dp[m][n]
> ```

---

## 🔷 Tries

### Problem 18: Implement Trie (Prefix Tree) ⭐⭐

Implement a trie with insert, search, and startsWith.

> 
> [!hint]- 💡 Hint
> Store prefixes in a tree of characters.

> [!success]- ✅ Solution
> ```python
> class TrieNode:
>     def __init__(self):
>         self.children = {}
>         self.is_end = False
>
> class Trie:
>     def __init__(self):
>         self.root = TrieNode()
>
>     def insert(self, word: str) -> None:
>         node = self.root
>         for char in word:
>             if char not in node.children:
>                 node.children[char] = TrieNode()
>             node = node.children[char]
>         node.is_end = True
>
>     def search(self, word: str) -> bool:
>         node = self._find_node(word)
>         return node is not None and node.is_end
>
>     def startsWith(self, prefix: str) -> bool:
>         return self._find_node(prefix) is not None
>
>     def _find_node(self, prefix: str) -> TrieNode:
>         node = self.root
>         for char in prefix:
>             if char not in node.children:
>                 return None
>             node = node.children[char]
>         return node
> ```

---

### Problem 19: Design Add and Search Words ⭐⭐⭐

Support adding words and searching with '.' wildcard.

> 
> [!hint]- 💡 Hint
> Store prefixes in a tree of characters.

> [!success]- ✅ Solution
> ```python
> class WordDictionary:
>     def __init__(self):
>         self.root = {}
>
>     def addWord(self, word: str) -> None:
>         node = self.root
>         for char in word:
>             node = node.setdefault(char, {})
>         node['$'] = True
>
>     def search(self, word: str) -> bool:
>         def dfs(node, i):
>             if i == len(word):
>                 return '$' in node
>
>             char = word[i]
>             if char == '.':
>                 return any(
>                     dfs(child, i + 1)
>                     for key, child in node.items()
>                     if key != '$'
>                 )
>             if char in node:
>                 return dfs(node[char], i + 1)
>             return False
>
>         return dfs(self.root, 0)
> ```

---

### Problem 20: Word Search II ⭐⭐⭐⭐

Find all words from dictionary that exist in the board.

```python
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
```

> 
> [!hint]- 💡 Hint
> Store prefixes in a tree of characters.

> [!success]- ✅ Solution
> ```python
> def find_words(board: list[list[str]], words: list[str]) -> list[str]:
>     # Build trie
>     trie = {}
>     for word in words:
>         node = trie
>         for char in word:
>             node = node.setdefault(char, {})
>         node['$'] = word
>
>     rows, cols = len(board), len(board[0])
>     result = []
>
>     def dfs(r, c, node):
>         char = board[r][c]
>         if char not in node:
>             return
>
>         next_node = node[char]
>         if '$' in next_node:
>             result.append(next_node['$'])
>             del next_node['$']  # Avoid duplicates
>
>         board[r][c] = '#'  # Mark visited
>
>         for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
>             nr, nc = r + dr, c + dc
>             if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
>                 dfs(nr, nc, next_node)
>
>         board[r][c] = char  # Restore
>
>     for r in range(rows):
>         for c in range(cols):
>             dfs(r, c, trie)
>
>     return result
> ```

---

## 🔷 Heap / Priority Queue

### Problem 21: Task Scheduler ⭐⭐⭐

Find minimum time to execute tasks with cooldown period.

```python
tasks = ["A","A","A","B","B","B"]
n = 2
# Output: 8 (A -> B -> idle -> A -> B -> idle -> A -> B)
```

> 
> [!hint]- 💡 Hint
> Use FIFO order with a queue (e.g., deque).

> [!success]- ✅ Solution
> ```python
> from collections import Counter
> import heapq
>
> def least_interval(tasks: list[str], n: int) -> int:
>     count = Counter(tasks)
>     max_heap = [-c for c in count.values()]
>     heapq.heapify(max_heap)
>
>     time = 0
>     queue = []  # (available_time, count)
>
>     while max_heap or queue:
>         time += 1
>
>         if max_heap:
>             cnt = heapq.heappop(max_heap) + 1
>             if cnt != 0:
>                 queue.append((time + n, cnt))
>
>         if queue and queue[0][0] == time:
>             heapq.heappush(max_heap, queue.pop(0)[1])
>
>     return time
> ```

---

### Problem 22: Merge K Sorted Lists ⭐⭐⭐

Merge k sorted linked lists into one sorted list.

> 
> [!hint]- 💡 Hint
> Use FIFO order with a queue (e.g., deque).

> [!success]- ✅ Solution
> ```python
> import heapq
>
> def merge_k_lists(lists: list[ListNode]) -> ListNode:
>     # Handle comparison for ListNode
>     ListNode.__lt__ = lambda self, other: self.val < other.val
>
>     heap = []
>     for l in lists:
>         if l:
>             heapq.heappush(heap, l)
>
>     dummy = ListNode(0)
>     curr = dummy
>
>     while heap:
>         node = heapq.heappop(heap)
>         curr.next = node
>         curr = curr.next
>
>         if node.next:
>             heapq.heappush(heap, node.next)
>
>     return dummy.next
> ```

---

### Problem 23: Find Median from Data Stream ⭐⭐⭐

Design a data structure that supports addNum and findMedian.

> 
> [!hint]- 💡 Hint
> Use FIFO order with a queue (e.g., deque).

> [!success]- ✅ Solution
> ```python
> import heapq
>
> class MedianFinder:
>     def __init__(self):
>         self.small = []  # Max heap (negated)
>         self.large = []  # Min heap
>
>     def addNum(self, num: int) -> None:
>         heapq.heappush(self.small, -num)
>         heapq.heappush(self.large, -heapq.heappop(self.small))
>
>         if len(self.large) > len(self.small):
>             heapq.heappush(self.small, -heapq.heappop(self.large))
>
>     def findMedian(self) -> float:
>         if len(self.small) > len(self.large):
>             return -self.small[0]
>         return (-self.small[0] + self.large[0]) / 2
> ```

---

## 🔷 Greedy

### Problem 24: Jump Game ⭐⭐

Check if you can reach the last index.

```python
nums = [2, 3, 1, 1, 4]
# Output: True
```

> 
> [!hint]- 💡 Hint
> Make the best local choice at each step.

> [!success]- ✅ Solution
> ```python
> def can_jump(nums: list[int]) -> bool:
>     max_reach = 0
>
>     for i, jump in enumerate(nums):
>         if i > max_reach:
>             return False
>         max_reach = max(max_reach, i + jump)
>
>     return True
> ```

---

### Problem 25: Jump Game II ⭐⭐⭐

Minimum jumps to reach the last index.

```python
nums = [2, 3, 1, 1, 4]
# Output: 2 (1 → 2 → 5)
```

> 
> [!hint]- 💡 Hint
> Make the best local choice at each step.

> [!success]- ✅ Solution
> ```python
> def jump(nums: list[int]) -> int:
>     jumps = 0
>     curr_end = 0
>     farthest = 0
>
>     for i in range(len(nums) - 1):
>         farthest = max(farthest, i + nums[i])
>
>         if i == curr_end:
>             jumps += 1
>             curr_end = farthest
>
>     return jumps
> ```

---

## 📚 Resources

| Resource | Link |
|----------|------|
| NeetCode 150 | [neetcode.io](https://neetcode.io/practice?tab=neetcode150) |
| Video Solutions | [NeetCode YouTube](https://www.youtube.com/c/NeetCode) |
| LeetCode Discuss | [leetcode.com/discuss](https://leetcode.com/discuss/) |

---

*These advanced problems will prepare you for FAANG interviews!*
