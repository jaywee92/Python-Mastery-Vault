# Challenge: Data Structure Problems 🏆
Notebook: [[14_Challenge_DataStructures.ipynb]]


> **Difficulty:** ⭐⭐⭐ - ⭐⭐⭐⭐⭐
> **Style:** LeetCode / Codewars
> **Topics:** Stacks, Queues, Hash Maps, Linked Lists, Trees

---

## C1: Implement Stack using Queues ⭐⭐
**Task:** Implement a LIFO stack using only two queues.

```python
class MyStack:
    def __init__(self):
        pass
    def push(self, x: int) -> None:
        pass
    def pop(self) -> int:
        pass
    def top(self) -> int:
        pass
    def empty(self) -> bool:
        pass

# Example:
# stack = MyStack()
# stack.push(1)
# stack.push(2)
# stack.top() → 2
# stack.pop() → 2
# stack.empty() → False
```

> [!hint]- 💡 Hint 1 (Low)
> Queue is FIFO, stack is LIFO. You need to reverse the order.

> [!hint]- 💡 Hint 2 (Mid)
> On push, rotate all existing elements after the new one.

> [!hint]- 💡 Hint 3 (High)
> Push to queue, then dequeue and re-enqueue n-1 elements.

> [!success]- Solution
> ```python
> from collections import deque
>
> class MyStack:
>     def __init__(self):
>         self.queue = deque()
>
>     def push(self, x: int) -> None:
>         self.queue.append(x)
>         # Rotate to put x at front
>         for _ in range(len(self.queue) - 1):
>             self.queue.append(self.queue.popleft())
>
>     def pop(self) -> int:
>         return self.queue.popleft()
>
>     def top(self) -> int:
>         return self.queue[0]
>
>     def empty(self) -> bool:
>         return len(self.queue) == 0
> ```
> **Complexity:** Push O(n), Pop O(1)

---

## C2: LRU Cache ⭐⭐⭐⭐
**Task:** Design a Least Recently Used cache with O(1) get and put.

```python
class LRUCache:
    def __init__(self, capacity: int):
        pass
    def get(self, key: int) -> int:
        pass
    def put(self, key: int, value: int) -> None:
        pass

# Example:
# cache = LRUCache(2)
# cache.put(1, 1)
# cache.put(2, 2)
# cache.get(1) → 1
# cache.put(3, 3)  # evicts key 2
# cache.get(2) → -1
```

> [!hint]- 💡 Hint 1 (Low)
> You need fast lookup AND order tracking.

> [!hint]- 💡 Hint 2 (Mid)
> Use a hash map for O(1) access + a doubly linked list for order.

> [!hint]- 💡 Hint 3 (High)
> Python's `OrderedDict` combines both functionalities!

> [!success]- Solution
> ```python
> from collections import OrderedDict
>
> class LRUCache:
>     def __init__(self, capacity: int):
>         self.cache = OrderedDict()
>         self.capacity = capacity
>
>     def get(self, key: int) -> int:
>         if key not in self.cache:
>             return -1
>         self.cache.move_to_end(key)
>         return self.cache[key]
>
>     def put(self, key: int, value: int) -> None:
>         if key in self.cache:
>             self.cache.move_to_end(key)
>         self.cache[key] = value
>         if len(self.cache) > self.capacity:
>             self.cache.popitem(last=False)
> ```
> **Complexity:** O(1) for both operations

---

## C3: Min Stack ⭐⭐
**Task:** Design a stack that supports push, pop, top, and retrieving the minimum element in O(1).

```python
class MinStack:
    def __init__(self):
        pass
    def push(self, val: int) -> None:
        pass
    def pop(self) -> None:
        pass
    def top(self) -> int:
        pass
    def getMin(self) -> int:
        pass

# Example:
# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# minStack.getMin() → -3
# minStack.pop()
# minStack.top() → 0
# minStack.getMin() → -2
```

> [!hint]- 💡 Hint 1 (Low)
> Store extra information with each element.

> [!hint]- 💡 Hint 2 (Mid)
> Keep track of the minimum at each stack level.

> [!hint]- 💡 Hint 3 (High)
> Store tuples of (value, current_minimum) on the stack.

> [!success]- Solution
> ```python
> class MinStack:
>     def __init__(self):
>         self.stack = []
>
>     def push(self, val: int) -> None:
>         if not self.stack:
>             self.stack.append((val, val))
>         else:
>             current_min = min(val, self.stack[-1][1])
>             self.stack.append((val, current_min))
>
>     def pop(self) -> None:
>         self.stack.pop()
>
>     def top(self) -> int:
>         return self.stack[-1][0]
>
>     def getMin(self) -> int:
>         return self.stack[-1][1]
> ```
> **Complexity:** O(1) for all operations

---

## C4: Reverse Linked List ⭐⭐
**Task:** Reverse a singly linked list.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    pass

# Example:
# 1 → 2 → 3 → 4 → 5 → None
# becomes
# 5 → 4 → 3 → 2 → 1 → None
```

> [!hint]- 💡 Hint 1 (Low)
> Keep track of three nodes: previous, current, next.

> [!hint]- 💡 Hint 2 (Mid)
> Reverse each pointer one at a time.

> [!hint]- 💡 Hint 3 (High)
> `curr.next = prev`, then move all three forward.

> [!success]- Solution
> ```python
> def reverse_list(head: ListNode) -> ListNode:
>     prev = None
>     curr = head
>
>     while curr:
>         next_temp = curr.next
>         curr.next = prev
>         prev = curr
>         curr = next_temp
>
>     return prev
>
> # Recursive:
> def reverse_list_recursive(head: ListNode) -> ListNode:
>     if not head or not head.next:
>         return head
>     new_head = reverse_list_recursive(head.next)
>     head.next.next = head
>     head.next = None
>     return new_head
> ```
> **Complexity:** O(n) time, O(1) space (iterative)

---

## C5: Merge Two Sorted Lists ⭐⭐
**Task:** Merge two sorted linked lists into one sorted list.

```python
def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    pass

# Example:
# l1: 1 → 2 → 4
# l2: 1 → 3 → 4
# Result: 1 → 1 → 2 → 3 → 4 → 4
```

> [!hint]- 💡 Hint 1 (Low)
> Compare heads and pick the smaller one.

> [!hint]- 💡 Hint 2 (Mid)
> Use a dummy node to simplify edge cases.

> [!hint]- 💡 Hint 3 (High)
> Keep moving pointers forward, attach remaining list at the end.

> [!success]- Solution
> ```python
> def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
>     dummy = ListNode()
>     current = dummy
>
>     while l1 and l2:
>         if l1.val <= l2.val:
>             current.next = l1
>             l1 = l1.next
>         else:
>             current.next = l2
>             l2 = l2.next
>         current = current.next
>
>     current.next = l1 or l2
>     return dummy.next
> ```
> **Complexity:** O(n + m) time, O(1) space

---

## C6: Linked List Cycle ⭐⭐
**Task:** Detect if a linked list has a cycle.

```python
def has_cycle(head: ListNode) -> bool:
    pass

# Example:
# 3 → 2 → 0 → -4 → (back to 2)  → True
# 1 → 2 → None  → False
```

> [!hint]- 💡 Hint 1 (Low)
> Use two pointers moving at different speeds.

> [!hint]- 💡 Hint 2 (Mid)
> If there's a cycle, the fast pointer will catch up to slow.

> [!hint]- 💡 Hint 3 (High)
> Floyd's algorithm: slow moves 1 step, fast moves 2 steps.

> [!success]- Solution
> ```python
> def has_cycle(head: ListNode) -> bool:
>     if not head or not head.next:
>         return False
>
>     slow = head
>     fast = head.next
>
>     while slow != fast:
>         if not fast or not fast.next:
>             return False
>         slow = slow.next
>         fast = fast.next.next
>
>     return True
> ```
> **Complexity:** O(n) time, O(1) space

---

## C7: Binary Tree Inorder Traversal ⭐⭐
**Task:** Return inorder traversal of a binary tree.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: TreeNode) -> list:
    pass

# Example:
#     1
#      \
#       2
#      /
#     3
# Output: [1, 3, 2]
```

> [!hint]- 💡 Hint 1 (Low)
> Inorder = Left, Root, Right.

> [!hint]- 💡 Hint 2 (Mid)
> Use recursion or a stack for iterative approach.

> [!hint]- 💡 Hint 3 (High)
> Go left as far as possible, then process, then go right.

> [!success]- Solution
> ```python
> def inorder_traversal(root: TreeNode) -> list:
>     result = []
>
>     def inorder(node):
>         if node:
>             inorder(node.left)
>             result.append(node.val)
>             inorder(node.right)
>
>     inorder(root)
>     return result
>
> # Iterative:
> def inorder_traversal_iterative(root: TreeNode) -> list:
>     result = []
>     stack = []
>     current = root
>
>     while current or stack:
>         while current:
>             stack.append(current)
>             current = current.left
>         current = stack.pop()
>         result.append(current.val)
>         current = current.right
>
>     return result
> ```
> **Complexity:** O(n) time, O(h) space

---

## C8: Maximum Depth of Binary Tree ⭐⭐
**Task:** Find the maximum depth of a binary tree.

```python
def max_depth(root: TreeNode) -> int:
    pass

# Example:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: 3
```

> [!hint]- 💡 Hint 1 (Low)
> Depth is 1 + max depth of subtrees.

> [!hint]- 💡 Hint 2 (Mid)
> Use recursion: base case is empty node = 0 depth.

> [!hint]- 💡 Hint 3 (High)
> `return 1 + max(max_depth(left), max_depth(right))`

> [!success]- Solution
> ```python
> def max_depth(root: TreeNode) -> int:
>     if not root:
>         return 0
>     return 1 + max(max_depth(root.left), max_depth(root.right))
>
> # Iterative with BFS:
> from collections import deque
> def max_depth_bfs(root: TreeNode) -> int:
>     if not root:
>         return 0
>     queue = deque([root])
>     depth = 0
>     while queue:
>         depth += 1
>         for _ in range(len(queue)):
>             node = queue.popleft()
>             if node.left:
>                 queue.append(node.left)
>             if node.right:
>                 queue.append(node.right)
>     return depth
> ```
> **Complexity:** O(n) time, O(h) space

---

## C9: Symmetric Tree ⭐⭐
**Task:** Check if a binary tree is symmetric (mirror of itself).

```python
def is_symmetric(root: TreeNode) -> bool:
    pass

# Example:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# Output: True
```

> [!hint]- 💡 Hint 1 (Low)
> Compare left subtree with right subtree.

> [!hint]- 💡 Hint 2 (Mid)
> Two trees are mirrors if roots equal and subtrees are mirrors.

> [!hint]- 💡 Hint 3 (High)
> Compare left.left with right.right and left.right with right.left.

> [!success]- Solution
> ```python
> def is_symmetric(root: TreeNode) -> bool:
>     def is_mirror(t1, t2):
>         if not t1 and not t2:
>             return True
>         if not t1 or not t2:
>             return False
>         return (t1.val == t2.val and
>                 is_mirror(t1.left, t2.right) and
>                 is_mirror(t1.right, t2.left))
>
>     return is_mirror(root, root)
> ```
> **Complexity:** O(n) time, O(h) space

---

## C10: Balanced Parentheses ⭐⭐
**Task:** Return `True` if the brackets are balanced and properly nested.

```python
def is_balanced(s: str) -> bool:
    pass

# Examples:
# is_balanced("()[]{}") -> True
# is_balanced("(]") -> False
# is_balanced("([{}])") -> True
```

> [!hint]- 💡 Hint 1 (Low)
> Use a stack to store opening brackets.

> [!hint]- 💡 Hint 2 (Mid)
> When you see a closing bracket, check the top of the stack.

> [!hint]- 💡 Hint 3 (High)
> Use a dict for matching pairs: `{')':'(', ']':'[', '}':'{'}`.

> [!success]- Solution
> ```python
> def is_balanced(s: str) -> bool:
>     stack = []
>     pairs = {')': '(', ']': '[', '}': '{'}
>     for ch in s:
>         if ch in "([{":
>             stack.append(ch)
>         elif ch in pairs:
>             if not stack or stack[-1] != pairs[ch]:
>                 return False
>             stack.pop()
>     return len(stack) == 0
> 
> print(is_balanced("()[]{}"))  # True
> print(is_balanced("(]"))      # False
> ```

---

## 🎯 Data Structure Challenges Complete!

**Skills Practiced:**
- Stack and Queue implementation
- Hash map design
- Linked list manipulation
- Tree traversals
- BST validation

**Next Challenge:** [[15_Challenge_Algorithms|Algorithm Challenges]]
