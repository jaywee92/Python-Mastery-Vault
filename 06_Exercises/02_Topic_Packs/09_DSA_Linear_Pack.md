# DSA Linear Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** Arrays, stacks, queues, searching

Notebook: [[09_DSA_Linear_Pack.ipynb]]

---

## L1: Filter Evens
**Task:** Return a new list containing only the even numbers.

```python
nums = [1, 2, 3, 4, 5, 6]
# expected: [2, 4, 6]
```

> [!hint]- 💡 Hint 1 (Low)
> Use a loop and add items that match a condition.

> [!hint]- 💡 Hint 2 (Mid)
> Check each number with `num % 2 == 0`.

> [!hint]- 💡 Hint 3 (High)
> A list comprehension can do this in one line.

> [!success]- ✅ Solution
> ```python
> def evens(nums):
>     return [n for n in nums if n % 2 == 0]
> 
> print(evens([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
> ```

---

---

## L2: Stack Reverse
**Task:** Use a stack (list) to reverse a string.

```python
text = "python"
# expected: "nohtyp"
```

> [!hint]- 💡 Hint 1 (Low)
> Push characters onto a list and pop them.

> [!hint]- 💡 Hint 2 (Mid)
> Use `append` to push and `pop` to remove.

> [!hint]- 💡 Hint 3 (High)
> Build a result list and `"".join(...)` at the end.

> [!success]- ✅ Solution
> ```python
> def reverse_text(text):
>     stack = []
>     for ch in text:
>         stack.append(ch)
>     out = []
>     while stack:
>         out.append(stack.pop())
>     return "".join(out)
> 
> print(reverse_text("python"))  # nohtyp
> ```

---

---

## L3: Queue Processing
**Task:** Process names in a queue in the correct order.

```python
from collections import deque
queue = deque(["Ana", "Ben", "Cara"])
# expected order: Ana, Ben, Cara
```

> [!hint]- 💡 Hint 1 (Low)
> Remove items from the left side of the queue.

> [!hint]- 💡 Hint 2 (Mid)
> Use `popleft()` to dequeue.

> [!hint]- 💡 Hint 3 (High)
> Keep looping while the queue is not empty.

> [!success]- ✅ Solution
> ```python
> from collections import deque
> 
> def process(queue):
>     order = []
>     while queue:
>         order.append(queue.popleft())
>     return order
> 
> q = deque(["Ana", "Ben", "Cara"])
> print(process(q))  # ['Ana', 'Ben', 'Cara']
> ```

---

---

## L4: Linear Search
**Task:** Return the index of `target` or `-1` if not found.

```python
nums = [10, 20, 30, 40]
# target = 30 -> 2
```

> [!hint]- 💡 Hint 1 (Low)
> Scan the list from start to end.

> [!hint]- 💡 Hint 2 (Mid)
> Use `enumerate` to get index and value.

> [!hint]- 💡 Hint 3 (High)
> Return immediately when you find the target.

> [!success]- ✅ Solution
> ```python
> def linear_search(nums, target):
>     for i, v in enumerate(nums):
>         if v == target:
>             return i
>     return -1
> 
> print(linear_search([10, 20, 30, 40], 30))  # 2
> ```

---

---

## L5: Binary Search (Sorted List)
**Task:** Return the index of `target` in a sorted list or `-1`.

```python
nums = [1, 3, 5, 7, 9]
# target = 7 -> 3
```

> [!hint]- 💡 Hint 1 (Low)
> Keep `left` and `right` pointers.

> [!hint]- 💡 Hint 2 (Mid)
> Compare `target` with the middle value.

> [!hint]- 💡 Hint 3 (High)
> If target is bigger, move `left = mid + 1`.

> [!success]- ✅ Solution
> ```python
> def binary_search(nums, target):
>     left, right = 0, len(nums) - 1
>     while left <= right:
>         mid = (left + right) // 2
>         if nums[mid] == target:
>             return mid
>         if nums[mid] < target:
>             left = mid + 1
>         else:
>             right = mid - 1
>     return -1
> 
> print(binary_search([1, 3, 5, 7, 9], 7))  # 3
> ```

---

## L6: Remove Duplicates (Sorted)
**Task:** Given a **sorted** list, return a new list with duplicates removed.

```python
nums = [1, 1, 2, 2, 3, 3, 3]
# expected: [1, 2, 3]
```

> [!hint]- 💡 Hint 1 (Low)
> Keep the last unique value and skip duplicates.

> [!hint]- 💡 Hint 2 (Mid)
> If the list is sorted, duplicates are next to each other.

> [!hint]- 💡 Hint 3 (High)
> Compare each value to the last value in the result list.

> [!success]- ✅ Solution
> ```python
> def remove_duplicates(nums):
>     if not nums:
>         return []
>     result = [nums[0]]
>     for n in nums[1:]:
>         if n != result[-1]:
>             result.append(n)
>     return result
> 
> print(remove_duplicates([1, 1, 2, 2, 3, 3, 3]))  # [1, 2, 3]
> ```

---

---

## L7: Valid Parentheses (Stack)
**Task:** Check if a string has valid parentheses `()`.

```python
s = "(()())"  # True
s = "(()"     # False
```

> [!hint]- 💡 Hint 1 (Low)
> Use a stack to track open parentheses.

> [!hint]- 💡 Hint 2 (Mid)
> Push for `(`, pop for `)`.

> [!hint]- 💡 Hint 3 (High)
> If you try to pop an empty stack, it's invalid.

> [!success]- ✅ Solution
> ```python
> def is_valid(s):
>     stack = []
>     for ch in s:
>         if ch == '(':
>             stack.append(ch)
>         else:
>             if not stack:
>                 return False
>             stack.pop()
>     return len(stack) == 0
> 
> print(is_valid("(()())"))  # True
> print(is_valid("(()"))     # False
> ```

---

---

## L8: Queue From Two Stacks
**Task:** Implement a queue using two stacks.

> [!hint]- 💡 Hint 1 (Low)
> Use one stack for input, one for output.

> [!hint]- 💡 Hint 2 (Mid)
> When output stack is empty, move all items from input.

> [!hint]- 💡 Hint 3 (High)
> `enqueue` pushes to input; `dequeue` pops from output.

> [!success]- ✅ Solution
> ```python
> class TwoStackQueue:
>     def __init__(self):
>         self.in_stack = []
>         self.out_stack = []
> 
>     def enqueue(self, value):
>         self.in_stack.append(value)
> 
>     def dequeue(self):
>         if not self.out_stack:
>             while self.in_stack:
>                 self.out_stack.append(self.in_stack.pop())
>         return self.out_stack.pop() if self.out_stack else None
> 
> q = TwoStackQueue()
> q.enqueue(1)
> q.enqueue(2)
> print(q.dequeue())  # 1
> print(q.dequeue())  # 2
> ```

---

---

## L9: Merge Two Sorted Lists
**Task:** Merge two sorted lists into one sorted list.

```python
a = [1, 3, 5]
b = [2, 4, 6]
# expected: [1, 2, 3, 4, 5, 6]
```

> [!hint]- 💡 Hint 1 (Low)
> Use two pointers, one for each list.

> [!hint]- 💡 Hint 2 (Mid)
> Always append the smaller value and move that pointer.

> [!hint]- 💡 Hint 3 (High)
> After one list ends, append the rest of the other list.

> [!success]- ✅ Solution
> ```python
> def merge_sorted(a, b):
>     i = j = 0
>     result = []
>     while i < len(a) and j < len(b):
>         if a[i] <= b[j]:
>             result.append(a[i])
>             i += 1
>         else:
>             result.append(b[j])
>             j += 1
>     result.extend(a[i:])
>     result.extend(b[j:])
>     return result
> 
> print(merge_sorted([1,3,5],[2,4,6]))  # [1,2,3,4,5,6]
> ```

---

---

## L10: Find the Missing Number
**Task:** Given numbers from `0..n` with one missing, return the missing number.

```python
nums = [3, 0, 1]
# expected: 2
```

> [!hint]- 💡 Hint 1 (Low)
> The sum of 0..n can be computed with a formula.

> [!hint]- 💡 Hint 2 (Mid)
> Expected sum minus actual sum gives the missing value.

> [!hint]- 💡 Hint 3 (High)
> `total = n * (n + 1) // 2`

> [!success]- ✅ Solution
> ```python
> def missing_number(nums):
>     n = len(nums)
>     expected = n * (n + 1) // 2
>     return expected - sum(nums)
> 
> print(missing_number([3, 0, 1]))  # 2
> ```

---

## DL1: Linear Search
**Task:** Solve the task below.

```python
nums=[3,5,7]
# find 5 -> 1
```

> [!hint]- 💡 Hint 1 (Low)
> Use basic linear data structures.

> [!hint]- 💡 Hint 2 (Mid)
> Keep it O(n) where possible.

> [!hint]- 💡 Hint 3 (High)
> Use simple loops or helpers.

> [!success]- ✅ Solution
> ```python
> nums=[3,5,7]
> idx = -1
> for i,v in enumerate(nums):
>     if v==5:
>         idx=i
>         break
> print(idx)
> ```

---

---

## DL2: Binary Search
**Task:** Solve the task below.

```python
nums=[1,3,5,7,9]
# find 7 -> 3
```

> [!hint]- 💡 Hint 1 (Low)
> Use basic linear data structures.

> [!hint]- 💡 Hint 2 (Mid)
> Keep it O(n) where possible.

> [!hint]- 💡 Hint 3 (High)
> Use simple loops or helpers.

> [!success]- ✅ Solution
> ```python
> nums=[1,3,5,7,9]
> left,right=0,len(nums)-1
> idx=-1
> while left<=right:
>     mid=(left+right)//2
>     if nums[mid]==7:
>         idx=mid
>         break
>     if nums[mid]<7:
>         left=mid+1
>     else:
>         right=mid-1
> print(idx)
> ```

---

---

## DL3: Stack Push/Pop
**Task:** Solve the task below.

```python
# stack with 1,2 then pop
```

> [!hint]- 💡 Hint 1 (Low)
> Use basic linear data structures.

> [!hint]- 💡 Hint 2 (Mid)
> Keep it O(n) where possible.

> [!hint]- 💡 Hint 3 (High)
> Use simple loops or helpers.

> [!success]- ✅ Solution
> ```python
> stack=[]
> stack.append(1)
> stack.append(2)
> print(stack.pop())
> ```

---

---

## DL4: Queue Dequeue
**Task:** Solve the task below.

```python
# dequeue first
```

> [!hint]- 💡 Hint 1 (Low)
> Use basic linear data structures.

> [!hint]- 💡 Hint 2 (Mid)
> Keep it O(n) where possible.

> [!hint]- 💡 Hint 3 (High)
> Use simple loops or helpers.

> [!success]- ✅ Solution
> ```python
> from collections import deque
> q=deque([1,2,3])
> print(q.popleft())
> ```

---

---

## DL5: Reverse List
**Task:** Solve the task below.

```python
nums=[1,2,3]
# expected: [3,2,1]
```

> [!hint]- 💡 Hint 1 (Low)
> Use basic linear data structures.

> [!hint]- 💡 Hint 2 (Mid)
> Keep it O(n) where possible.

> [!hint]- 💡 Hint 3 (High)
> Use simple loops or helpers.

> [!success]- ✅ Solution
> ```python
> nums=[1,2,3]
> print(list(reversed(nums)))
> ```

---

---

## DL6: Remove Duplicates
**Task:** Solve the task below.

```python
nums=[1,1,2]
# expected: [1,2]
```

> [!hint]- 💡 Hint 1 (Low)
> Use basic linear data structures.

> [!hint]- 💡 Hint 2 (Mid)
> Keep it O(n) where possible.

> [!hint]- 💡 Hint 3 (High)
> Use simple loops or helpers.

> [!success]- ✅ Solution
> ```python
> nums=[1,1,2]
> res=[]
> for n in nums:
>     if n not in res:
>         res.append(n)
> print(res)
> ```

---

---

## DL7: Merge Sorted
**Task:** Solve the task below.

```python
a=[1,3]
b=[2,4]
# expected: [1,2,3,4]
```

> [!hint]- 💡 Hint 1 (Low)
> Use basic linear data structures.

> [!hint]- 💡 Hint 2 (Mid)
> Keep it O(n) where possible.

> [!hint]- 💡 Hint 3 (High)
> Use simple loops or helpers.

> [!success]- ✅ Solution
> ```python
> a=[1,3]
> b=[2,4]
> res=[]
> i=j=0
> while i<len(a) and j<len(b):
>     if a[i]<=b[j]:
>         res.append(a[i]); i+=1
>     else:
>         res.append(b[j]); j+=1
> res.extend(a[i:]); res.extend(b[j:])
> print(res)
> ```

---

---

## DL8: Max Subarray Sum
**Task:** Solve the task below.

```python
nums=[-2,1,-3,4]
# expected: 4
```

> [!hint]- 💡 Hint 1 (Low)
> Use basic linear data structures.

> [!hint]- 💡 Hint 2 (Mid)
> Keep it O(n) where possible.

> [!hint]- 💡 Hint 3 (High)
> Use simple loops or helpers.

> [!success]- ✅ Solution
> ```python
> nums=[-2,1,-3,4]
> best=curr=nums[0]
> for n in nums[1:]:
>     curr=max(n, curr+n)
>     best=max(best,curr)
> print(best)
> ```

---

---

## DL9: Move Zeros
**Task:** Solve the task below.

```python
nums=[0,1,0,3,12]
# expected: [1,3,12,0,0]
```

> [!hint]- 💡 Hint 1 (Low)
> Use basic linear data structures.

> [!hint]- 💡 Hint 2 (Mid)
> Keep it O(n) where possible.

> [!hint]- 💡 Hint 3 (High)
> Use simple loops or helpers.

> [!success]- ✅ Solution
> ```python
> nums=[0,1,0,3,12]
> res=[n for n in nums if n!=0]
> res += [0]*(len(nums)-len(res))
> print(res)
> ```

---

---

## DL10: Two Sum
**Task:** Solve the task below.

```python
nums=[2,7,11,15]
# target 9 -> [0,1]
```

> [!hint]- 💡 Hint 1 (Low)
> Use basic linear data structures.

> [!hint]- 💡 Hint 2 (Mid)
> Keep it O(n) where possible.

> [!hint]- 💡 Hint 3 (High)
> Use simple loops or helpers.

> [!success]- ✅ Solution
> ```python
> nums=[2,7,11,15]
> target=9
> seen={}
> ans=[]
> for i,n in enumerate(nums):
>     need=target-n
>     if need in seen:
>         ans=[seen[need], i]
>         break
>     seen[n]=i
> print(ans)
> ```

---

---
