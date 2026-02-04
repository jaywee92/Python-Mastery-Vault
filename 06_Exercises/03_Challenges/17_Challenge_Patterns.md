---
title: Algorithm Patterns Master
tags: [python, exercises, patterns, leetcode, interview]
created: 2026-02-04
difficulty: medium-hard
type: challenges
---

# 🎯 Algorithm Patterns Master

> **Learn Patterns, Not Just Problems**
> Based on [15 LeetCode Patterns](https://blog.algomaster.io/p/15-leetcode-patterns)
> Master these patterns and solve any variation!

---

## 📊 Pattern Overview

| Pattern | Use When | Time Complexity |
|---------|----------|-----------------|
| Two Pointers | Sorted arrays, pairs | O(n) |
| Sliding Window | Substrings, subarrays | O(n) |
| Fast & Slow Pointers | Cycles, middle element | O(n) |
| Binary Search | Sorted data, search space | O(log n) |
| BFS | Shortest path, level order | O(V + E) |
| DFS | Path finding, backtracking | O(V + E) |
| Merge Intervals | Overlapping ranges | O(n log n) |
| Monotonic Stack | Next greater/smaller | O(n) |
| Top K Elements | Frequency, ranking | O(n log k) |
| Backtracking | Combinations, permutations | O(2^n) |

---

## 🔷 Pattern 1: Two Pointers

> **When to use:** Sorted arrays, finding pairs, partitioning

### Template

```python
# Opposite direction (most common)
def two_pointers_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        if condition:
            left += 1
        else:
            right -= 1

# Same direction
def two_pointers_same(arr):
    slow = 0
    for fast in range(len(arr)):
        if condition:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
```

### Problem 1: Two Sum II (Sorted Array) ⭐⭐

Given a **sorted** array, find two numbers that add up to target.

```python
numbers = [2, 7, 11, 15]
target = 9
# Output: [1, 2] (1-indexed)
```

> 
> [!hint]- 💡 Hint
> Use two indices (left/right) and move them based on the condition.

> [!success]- ✅ Solution
> ```python
> def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
>     left, right = 0, len(numbers) - 1
>
>     while left < right:
>         total = numbers[left] + numbers[right]
>         if total == target:
>             return [left + 1, right + 1]  # 1-indexed
>         elif total < target:
>             left += 1
>         else:
>             right -= 1
>
>     return []
> ```

### Problem 2: Remove Duplicates from Sorted Array ⭐

Remove duplicates in-place, return new length.

```python
nums = [1, 1, 2]
# Output: 2, nums = [1, 2, ...]
```

> 
> [!hint]- 💡 Hint
> Use two indices (left/right) and move them based on the condition.

> [!success]- ✅ Solution
> ```python
> def remove_duplicates(nums: list[int]) -> int:
>     if not nums:
>         return 0
>
>     slow = 0
>     for fast in range(1, len(nums)):
>         if nums[fast] != nums[slow]:
>             slow += 1
>             nums[slow] = nums[fast]
>
>     return slow + 1
> ```

### Problem 3: Move Zeroes ⭐

Move all 0s to the end while maintaining relative order of non-zero elements.

```python
nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
```

> 
> [!hint]- 💡 Hint
> Use two indices (left/right) and move them based on the condition.

> [!success]- ✅ Solution
> ```python
> def move_zeroes(nums: list[int]) -> None:
>     slow = 0
>     for fast in range(len(nums)):
>         if nums[fast] != 0:
>             nums[slow], nums[fast] = nums[fast], nums[slow]
>             slow += 1
> ```

---

## 🔷 Pattern 2: Sliding Window

> **When to use:** Substrings, subarrays, contiguous sequences
> **Key insight:** Window expands (right++), shrinks (left++) based on condition

### Template

```python
# Variable size window
def sliding_window_variable(s):
    left = 0
    window = {}  # or set, counter
    result = 0

    for right in range(len(s)):
        # Expand: add s[right] to window

        while window_invalid():
            # Shrink: remove s[left] from window
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result

# Fixed size window
def sliding_window_fixed(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Problem 4: Maximum Sum Subarray of Size K ⭐⭐

Find maximum sum of any contiguous subarray of size k.

```python
arr = [2, 1, 5, 1, 3, 2]
k = 3
# Output: 9 (subarray [5, 1, 3])
```

> 
> [!hint]- 💡 Hint
> Keep a window and expand/contract it to satisfy the condition.

> [!success]- ✅ Solution
> ```python
> def max_sum_subarray(arr: list[int], k: int) -> int:
>     window_sum = sum(arr[:k])
>     max_sum = window_sum
>
>     for i in range(k, len(arr)):
>         window_sum += arr[i] - arr[i - k]
>         max_sum = max(max_sum, window_sum)
>
>     return max_sum
> ```

### Problem 5: Longest Substring with K Distinct Characters ⭐⭐⭐

Find length of longest substring with at most k distinct characters.

```python
s = "araaci"
k = 2
# Output: 4 ("araa")
```

> [!hint]- 💡 Hint
> Use a dict to count character frequencies. Shrink window when distinct > k.

> [!success]- ✅ Solution
> ```python
> def longest_substring_k_distinct(s: str, k: int) -> int:
>     char_count = {}
>     left = 0
>     max_length = 0
>
>     for right in range(len(s)):
>         char_count[s[right]] = char_count.get(s[right], 0) + 1
>
>         while len(char_count) > k:
>             char_count[s[left]] -= 1
>             if char_count[s[left]] == 0:
>                 del char_count[s[left]]
>             left += 1
>
>         max_length = max(max_length, right - left + 1)
>
>     return max_length
> ```

### Problem 6: Permutation in String ⭐⭐

Check if s2 contains a permutation of s1.

```python
s1 = "ab"
s2 = "eidbaooo"
# Output: True ("ba" is permutation of "ab")
```

> 
> [!hint]- 💡 Hint
> Keep a window and expand/contract it to satisfy the condition.

> [!success]- ✅ Solution
> ```python
> from collections import Counter
>
> def check_inclusion(s1: str, s2: str) -> bool:
>     if len(s1) > len(s2):
>         return False
>
>     s1_count = Counter(s1)
>     window = Counter(s2[:len(s1)])
>
>     if s1_count == window:
>         return True
>
>     for i in range(len(s1), len(s2)):
>         # Add new char
>         window[s2[i]] += 1
>         # Remove old char
>         old_char = s2[i - len(s1)]
>         window[old_char] -= 1
>         if window[old_char] == 0:
>             del window[old_char]
>
>         if s1_count == window:
>             return True
>
>     return False
> ```

---

## 🔷 Pattern 3: Fast & Slow Pointers (Floyd's)

> **When to use:** Cycle detection, finding middle, linked list problems

### Template

```python
def floyd_cycle_detection(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # Cycle found

    return False

def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # Middle node
```

### Problem 7: Happy Number ⭐⭐

A number is "happy" if repeatedly replacing it with the sum of squares of its digits eventually reaches 1.

```python
n = 19
# Output: True
# 1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1 ✓
```

> [!hint]- 💡 Hint
> Unhappy numbers form a cycle. Use Floyd's algorithm!

> [!success]- ✅ Solution
> ```python
> def is_happy(n: int) -> bool:
>     def get_next(num):
>         return sum(int(d) ** 2 for d in str(num))
>
>     slow = n
>     fast = get_next(n)
>
>     while fast != 1 and slow != fast:
>         slow = get_next(slow)
>         fast = get_next(get_next(fast))
>
>     return fast == 1
> ```

### Problem 8: Find the Duplicate Number ⭐⭐⭐

Array of n+1 integers where each integer is in [1, n]. Find the duplicate.

```python
nums = [1, 3, 4, 2, 2]
# Output: 2
```

> [!hint]- 💡 Hint
> Treat array as linked list: value at index i points to index nums[i]. Floyd's!

> [!success]- ✅ Solution
> ```python
> def find_duplicate(nums: list[int]) -> int:
>     # Phase 1: Find intersection
>     slow = fast = nums[0]
>     while True:
>         slow = nums[slow]
>         fast = nums[nums[fast]]
>         if slow == fast:
>             break
>
>     # Phase 2: Find cycle start
>     slow = nums[0]
>     while slow != fast:
>         slow = nums[slow]
>         fast = nums[fast]
>
>     return slow
> ```

---

## 🔷 Pattern 4: Merge Intervals

> **When to use:** Overlapping ranges, scheduling, time conflicts

### Template

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # Overlapping
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged
```

### Problem 9: Merge Intervals ⭐⭐

Merge all overlapping intervals.

```python
intervals = [[1,3], [2,6], [8,10], [15,18]]
# Output: [[1,6], [8,10], [15,18]]
```

> 
> [!hint]- 💡 Hint
> Sort intervals and merge or insert by comparing endpoints.

> [!success]- ✅ Solution
> ```python
> def merge(intervals: list[list[int]]) -> list[list[int]]:
>     intervals.sort(key=lambda x: x[0])
>     merged = [intervals[0]]
>
>     for start, end in intervals[1:]:
>         if start <= merged[-1][1]:
>             merged[-1][1] = max(merged[-1][1], end)
>         else:
>             merged.append([start, end])
>
>     return merged
> ```

### Problem 10: Insert Interval ⭐⭐

Insert a new interval into a sorted list of non-overlapping intervals.

```python
intervals = [[1,3], [6,9]]
newInterval = [2, 5]
# Output: [[1,5], [6,9]]
```

> 
> [!hint]- 💡 Hint
> Sort intervals and merge or insert by comparing endpoints.

> [!success]- ✅ Solution
> ```python
> def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
>     result = []
>     i = 0
>
>     # Add all intervals before newInterval
>     while i < len(intervals) and intervals[i][1] < newInterval[0]:
>         result.append(intervals[i])
>         i += 1
>
>     # Merge overlapping intervals
>     while i < len(intervals) and intervals[i][0] <= newInterval[1]:
>         newInterval[0] = min(newInterval[0], intervals[i][0])
>         newInterval[1] = max(newInterval[1], intervals[i][1])
>         i += 1
>     result.append(newInterval)
>
>     # Add remaining intervals
>     while i < len(intervals):
>         result.append(intervals[i])
>         i += 1
>
>     return result
> ```

### Problem 11: Meeting Rooms II ⭐⭐⭐

Find minimum number of meeting rooms required.

```python
intervals = [[0, 30], [5, 10], [15, 20]]
# Output: 2
```

> [!hint]- 💡 Hint
> Track start and end times separately. Count active meetings.

> [!success]- ✅ Solution
> ```python
> def min_meeting_rooms(intervals: list[list[int]]) -> int:
>     starts = sorted([i[0] for i in intervals])
>     ends = sorted([i[1] for i in intervals])
>
>     rooms = 0
>     max_rooms = 0
>     s, e = 0, 0
>
>     while s < len(starts):
>         if starts[s] < ends[e]:
>             rooms += 1
>             s += 1
>         else:
>             rooms -= 1
>             e += 1
>         max_rooms = max(max_rooms, rooms)
>
>     return max_rooms
> ```

---

## 🔷 Pattern 5: Monotonic Stack

> **When to use:** Next greater/smaller element, histogram problems

### Template

```python
def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []  # Indices of elements waiting for next greater

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)

    return result
```

### Problem 12: Next Greater Element I ⭐⭐

Find the next greater element for each element in nums1 within nums2.

```python
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
# Output: [-1, 3, -1]
```

> 
> [!hint]- 💡 Hint
> Push while iterating, pop when you match a condition.

> [!success]- ✅ Solution
> ```python
> def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
>     next_greater = {}
>     stack = []
>
>     for num in nums2:
>         while stack and stack[-1] < num:
>             next_greater[stack.pop()] = num
>         stack.append(num)
>
>     return [next_greater.get(num, -1) for num in nums1]
> ```

### Problem 13: Daily Temperatures ⭐⭐

Days until a warmer temperature (or 0 if never).

```python
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

> 
> [!hint]- 💡 Hint
> Push while iterating, pop when you match a condition.

> [!success]- ✅ Solution
> ```python
> def daily_temperatures(temperatures: list[int]) -> list[int]:
>     result = [0] * len(temperatures)
>     stack = []  # (index, temp) pairs
>
>     for i, temp in enumerate(temperatures):
>         while stack and stack[-1][1] < temp:
>             prev_idx, _ = stack.pop()
>             result[prev_idx] = i - prev_idx
>         stack.append((i, temp))
>
>     return result
> ```

### Problem 14: Largest Rectangle in Histogram ⭐⭐⭐⭐

Find the largest rectangular area in a histogram.

```python
heights = [2, 1, 5, 6, 2, 3]
# Output: 10
```

> [!hint]- 💡 Hint
> For each bar, find the left and right boundaries using monotonic stack.

> [!success]- ✅ Solution
> ```python
> def largest_rectangle_area(heights: list[int]) -> int:
>     stack = []  # (index, height)
>     max_area = 0
>
>     for i, h in enumerate(heights):
>         start = i
>         while stack and stack[-1][1] > h:
>             idx, height = stack.pop()
>             max_area = max(max_area, height * (i - idx))
>             start = idx
>         stack.append((start, h))
>
>     # Process remaining bars
>     for idx, height in stack:
>         max_area = max(max_area, height * (len(heights) - idx))
>
>     return max_area
> ```

---

## 🔷 Pattern 6: Top K Elements

> **When to use:** Finding k largest/smallest, frequency problems

### Template

```python
import heapq

def top_k_largest(nums, k):
    # Min heap of size k
    return heapq.nlargest(k, nums)

def top_k_smallest(nums, k):
    return heapq.nsmallest(k, nums)

def top_k_frequent(nums, k):
    from collections import Counter
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

### Problem 15: Kth Largest Element in Array ⭐⭐

Find the kth largest element.

```python
nums = [3, 2, 1, 5, 6, 4]
k = 2
# Output: 5
```

> 
> [!hint]- 💡 Hint
> Keep a heap of size k to track best elements.

> [!success]- ✅ Solution
> ```python
> import heapq
>
> def find_kth_largest(nums: list[int], k: int) -> int:
>     # Min heap of size k
>     heap = nums[:k]
>     heapq.heapify(heap)
>
>     for num in nums[k:]:
>         if num > heap[0]:
>             heapq.heapreplace(heap, num)
>
>     return heap[0]
>
> # Or simply:
> def find_kth_largest_v2(nums: list[int], k: int) -> int:
>     return heapq.nlargest(k, nums)[-1]
> ```

### Problem 16: K Closest Points to Origin ⭐⭐

Find k points closest to origin (0, 0).

```python
points = [[1, 3], [-2, 2]]
k = 1
# Output: [[-2, 2]]
```

> 
> [!hint]- 💡 Hint
> Keep a heap of size k to track best elements.

> [!success]- ✅ Solution
> ```python
> import heapq
>
> def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
>     # Use max heap (negate distance) of size k
>     heap = []
>
>     for x, y in points:
>         dist = -(x*x + y*y)  # Negate for max heap
>         if len(heap) < k:
>             heapq.heappush(heap, (dist, [x, y]))
>         elif dist > heap[0][0]:
>             heapq.heapreplace(heap, (dist, [x, y]))
>
>     return [point for _, point in heap]
> ```

---

## 🔷 Pattern 7: Backtracking

> **When to use:** Combinations, permutations, subsets, constraint satisfaction

### Template

```python
def backtrack(result, path, choices, start):
    if is_solution(path):
        result.append(path[:])
        return

    for i in range(start, len(choices)):
        # Skip duplicates if needed
        if i > start and choices[i] == choices[i-1]:
            continue

        path.append(choices[i])       # Make choice
        backtrack(result, path, choices, i + 1)  # Recurse
        path.pop()                    # Undo choice
```

### Problem 17: Subsets ⭐⭐

Generate all possible subsets of a list.

```python
nums = [1, 2, 3]
# Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

> 
> [!hint]- 💡 Hint
> Build a path step by step and backtrack on dead ends.

> [!success]- ✅ Solution
> ```python
> def subsets(nums: list[int]) -> list[list[int]]:
>     result = []
>
>     def backtrack(start, path):
>         result.append(path[:])
>         for i in range(start, len(nums)):
>             path.append(nums[i])
>             backtrack(i + 1, path)
>             path.pop()
>
>     backtrack(0, [])
>     return result
> ```

### Problem 18: Permutations ⭐⭐

Generate all permutations.

```python
nums = [1, 2, 3]
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
```

> 
> [!hint]- 💡 Hint
> Build a path step by step and backtrack on dead ends.

> [!success]- ✅ Solution
> ```python
> def permute(nums: list[int]) -> list[list[int]]:
>     result = []
>
>     def backtrack(path, remaining):
>         if not remaining:
>             result.append(path[:])
>             return
>
>         for i in range(len(remaining)):
>             path.append(remaining[i])
>             backtrack(path, remaining[:i] + remaining[i+1:])
>             path.pop()
>
>     backtrack([], nums)
>     return result
> ```

### Problem 19: Combination Sum ⭐⭐

Find all unique combinations that sum to target (can reuse elements).

```python
candidates = [2, 3, 6, 7]
target = 7
# Output: [[2, 2, 3], [7]]
```

> 
> [!hint]- 💡 Hint
> Build a path step by step and backtrack on dead ends.

> [!success]- ✅ Solution
> ```python
> def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
>     result = []
>
>     def backtrack(start, path, remaining):
>         if remaining == 0:
>             result.append(path[:])
>             return
>         if remaining < 0:
>             return
>
>         for i in range(start, len(candidates)):
>             path.append(candidates[i])
>             backtrack(i, path, remaining - candidates[i])  # i, not i+1 (reuse)
>             path.pop()
>
>     backtrack(0, [], target)
>     return result
> ```

### Problem 20: Word Search ⭐⭐⭐

Check if word exists in a grid (adjacent cells, no reuse).

```python
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# Output: True
```

> 
> [!hint]- 💡 Hint
> Build a path step by step and backtrack on dead ends.

> [!success]- ✅ Solution
> ```python
> def exist(board: list[list[str]], word: str) -> bool:
>     rows, cols = len(board), len(board[0])
>
>     def backtrack(r, c, idx):
>         if idx == len(word):
>             return True
>         if (r < 0 or r >= rows or c < 0 or c >= cols or
>             board[r][c] != word[idx]):
>             return False
>
>         temp = board[r][c]
>         board[r][c] = '#'  # Mark visited
>
>         found = (backtrack(r+1, c, idx+1) or
>                  backtrack(r-1, c, idx+1) or
>                  backtrack(r, c+1, idx+1) or
>                  backtrack(r, c-1, idx+1))
>
>         board[r][c] = temp  # Restore
>         return found
>
>     for r in range(rows):
>         for c in range(cols):
>             if backtrack(r, c, 0):
>                 return True
>     return False
> ```

---

## 📚 Pattern Cheat Sheet

```
┌─────────────────────────────────────────────────────────────┐
│                    PATTERN SELECTOR                          │
├─────────────────────────────────────────────────────────────┤
│ "Pair in sorted array"        → Two Pointers               │
│ "Substring/subarray"          → Sliding Window              │
│ "Cycle detection"             → Fast & Slow Pointers        │
│ "Sorted + search"             → Binary Search               │
│ "Shortest path"               → BFS                         │
│ "All paths/backtrack"         → DFS                         │
│ "Overlapping ranges"          → Merge Intervals             │
│ "Next greater/smaller"        → Monotonic Stack             │
│ "Top K / K-th element"        → Heap                        │
│ "All combinations"            → Backtracking                │
│ "Optimal substructure"        → Dynamic Programming         │
└─────────────────────────────────────────────────────────────┘
```

---

## 📚 Resources

| Resource | Link |
|----------|------|
| 15 LeetCode Patterns | [AlgoMaster](https://blog.algomaster.io/p/15-leetcode-patterns) |
| Pattern Explanations | [NeetCode](https://neetcode.io/) |
| GeeksforGeeks | [Two Pointers](https://www.geeksforgeeks.org/dsa/two-pointers-technique/) |

---

*Master patterns, and you can solve any problem!*
