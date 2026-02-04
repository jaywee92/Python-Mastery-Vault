---
title: Blind 75 Essentials
tags: [python, exercises, blind75, leetcode, interview]
created: 2026-02-04
difficulty: medium-hard
type: challenges
---

# 🏆 Blind 75 Essentials

> **The Most Important Interview Problems**
> Curated by [Tech Interview Handbook](https://www.techinterviewhandbook.org/best-practice-questions/)
> These 25 problems cover the core patterns from the famous Blind 75 list.

---

## 📊 Categories Overview

| Category | Problems | Key Patterns |
|----------|----------|--------------|
| Arrays & Hashing | 5 | Hash Maps, Frequency Count |
| Two Pointers | 4 | Sorted Arrays, Palindromes |
| Sliding Window | 3 | Substrings, Subarrays |
| Binary Search | 3 | Rotated Arrays, Search |
| Linked Lists | 3 | Reversal, Cycle Detection |
| Trees | 4 | DFS, BFS, Recursion |
| Dynamic Programming | 3 | Memoization, Tabulation |

---

## 🔷 Arrays & Hashing

### Problem 1: Two Sum ⭐⭐
> **LeetCode #1** | Most Asked Interview Question

Given an array of integers `nums` and an integer `target`, return indices of the two numbers that add up to `target`.

```python
# Example
nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1] (because nums[0] + nums[1] = 9)
```

> [!hint]- 💡 Hint 1 (Low)
> A brute force approach checks every pair - O(n²). Can you do better with a hash map?

> [!hint]- 💡 Hint 2 (Mid)
> For each number, calculate what complement you need: `target - num`. Store seen numbers in a dict.

> [!hint]- 💡 Hint 3 (High)
> ```python
> def two_sum(nums, target):
>     seen = {}
>     for i, num in enumerate(nums):
>         complement = target - num
>         if complement in seen:
>             return [seen[complement], i]
>         seen[num] = i
> ```

> [!success]- ✅ Solution
> ```python
> def two_sum(nums: list[int], target: int) -> list[int]:
>     seen = {}
>     for i, num in enumerate(nums):
>         complement = target - num
>         if complement in seen:
>             return [seen[complement], i]
>         seen[num] = i
>     return []
>
> # Test
> print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
> print(two_sum([3, 2, 4], 6))       # [1, 2]
> ```
> **Time:** O(n) | **Space:** O(n)

---

### Problem 2: Contains Duplicate ⭐
> **LeetCode #217**

Given an integer array `nums`, return `True` if any value appears at least twice.

```python
# Example
nums = [1, 2, 3, 1]
# Output: True
```

> [!hint]- 💡 Hint 1 (Low)
> Sets only store unique values...

> [!hint]- 💡 Hint 2 (Mid)
> Compare the length of the list with the length of a set created from it.

> [!success]- ✅ Solution
> ```python
> def contains_duplicate(nums: list[int]) -> bool:
>     return len(nums) != len(set(nums))
>
> # Alternative with early exit
> def contains_duplicate_v2(nums: list[int]) -> bool:
>     seen = set()
>     for num in nums:
>         if num in seen:
>             return True
>         seen.add(num)
>     return False
> ```
> **Time:** O(n) | **Space:** O(n)

---

### Problem 3: Valid Anagram ⭐
> **LeetCode #242**

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`.

```python
# Example
s = "anagram"
t = "nagaram"
# Output: True
```

> [!hint]- 💡 Hint 1 (Low)
> Anagrams have the same character frequencies.

> [!hint]- 💡 Hint 2 (Mid)
> Use `collections.Counter` or sort both strings.

> [!success]- ✅ Solution
> ```python
> from collections import Counter
>
> def is_anagram(s: str, t: str) -> bool:
>     return Counter(s) == Counter(t)
>
> # Alternative: Sorting
> def is_anagram_v2(s: str, t: str) -> bool:
>     return sorted(s) == sorted(t)
>
> print(is_anagram("anagram", "nagaram"))  # True
> print(is_anagram("rat", "car"))          # False
> ```
> **Time:** O(n) | **Space:** O(n)

---

### Problem 4: Group Anagrams ⭐⭐
> **LeetCode #49**

Given an array of strings, group the anagrams together.

```python
# Example
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
```

> [!hint]- 💡 Hint 1 (Low)
> Anagrams, when sorted, produce the same string.

> [!hint]- 💡 Hint 2 (Mid)
> Use a dictionary where the key is the sorted string.

> [!hint]- 💡 Hint 3 (High)
> ```python
> from collections import defaultdict
> groups = defaultdict(list)
> for s in strs:
>     key = tuple(sorted(s))
>     groups[key].append(s)
> ```

> [!success]- ✅ Solution
> ```python
> from collections import defaultdict
>
> def group_anagrams(strs: list[str]) -> list[list[str]]:
>     groups = defaultdict(list)
>     for s in strs:
>         key = tuple(sorted(s))
>         groups[key].append(s)
>     return list(groups.values())
>
> print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
> ```
> **Time:** O(n * k log k) where k = max string length | **Space:** O(n * k)

---

### Problem 5: Top K Frequent Elements ⭐⭐
> **LeetCode #347**

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

```python
# Example
nums = [1, 1, 1, 2, 2, 3]
k = 2
# Output: [1, 2]
```

> [!hint]- 💡 Hint 1 (Low)
> Count frequencies first, then find the top k.

> [!hint]- 💡 Hint 2 (Mid)
> Use `Counter.most_common(k)` or a heap.

> [!success]- ✅ Solution
> ```python
> from collections import Counter
>
> def top_k_frequent(nums: list[int], k: int) -> list[int]:
>     count = Counter(nums)
>     return [num for num, freq in count.most_common(k)]
>
> # Alternative: Bucket Sort O(n)
> def top_k_frequent_v2(nums: list[int], k: int) -> list[int]:
>     count = Counter(nums)
>     buckets = [[] for _ in range(len(nums) + 1)]
>
>     for num, freq in count.items():
>         buckets[freq].append(num)
>
>     result = []
>     for i in range(len(buckets) - 1, -1, -1):
>         result.extend(buckets[i])
>         if len(result) >= k:
>             return result[:k]
>     return result
> ```
> **Time:** O(n) with bucket sort | **Space:** O(n)

---

## 🔷 Two Pointers

### Problem 6: Valid Palindrome ⭐
> **LeetCode #125**

Given a string `s`, return `True` if it's a palindrome (considering only alphanumeric characters, ignoring case).

```python
# Example
s = "A man, a plan, a canal: Panama"
# Output: True
```

> [!hint]- 💡 Hint 1 (Low)
> Use two pointers from both ends moving inward.

> [!hint]- 💡 Hint 2 (Mid)
> Skip non-alphanumeric characters with `isalnum()`.

> [!success]- ✅ Solution
> ```python
> def is_palindrome(s: str) -> bool:
>     left, right = 0, len(s) - 1
>
>     while left < right:
>         while left < right and not s[left].isalnum():
>             left += 1
>         while left < right and not s[right].isalnum():
>             right -= 1
>
>         if s[left].lower() != s[right].lower():
>             return False
>
>         left += 1
>         right -= 1
>
>     return True
>
> print(is_palindrome("A man, a plan, a canal: Panama"))  # True
> ```
> **Time:** O(n) | **Space:** O(1)

---

### Problem 7: 3Sum ⭐⭐⭐
> **LeetCode #15** | Classic Interview Problem

Given an integer array `nums`, return all triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`.

```python
# Example
nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
```

> [!hint]- 💡 Hint 1 (Low)
> Sort the array first. This enables the two-pointer technique.

> [!hint]- 💡 Hint 2 (Mid)
> Fix one number, then use two pointers to find pairs that sum to its negative.

> [!hint]- 💡 Hint 3 (High)
> Skip duplicates to avoid duplicate triplets in the result.

> [!success]- ✅ Solution
> ```python
> def three_sum(nums: list[int]) -> list[list[int]]:
>     nums.sort()
>     result = []
>
>     for i in range(len(nums) - 2):
>         # Skip duplicates for first number
>         if i > 0 and nums[i] == nums[i - 1]:
>             continue
>
>         left, right = i + 1, len(nums) - 1
>
>         while left < right:
>             total = nums[i] + nums[left] + nums[right]
>
>             if total < 0:
>                 left += 1
>             elif total > 0:
>                 right -= 1
>             else:
>                 result.append([nums[i], nums[left], nums[right]])
>                 # Skip duplicates
>                 while left < right and nums[left] == nums[left + 1]:
>                     left += 1
>                 while left < right and nums[right] == nums[right - 1]:
>                     right -= 1
>                 left += 1
>                 right -= 1
>
>     return result
>
> print(three_sum([-1, 0, 1, 2, -1, -4]))
> ```
> **Time:** O(n²) | **Space:** O(1) excluding output

---

### Problem 8: Container With Most Water ⭐⭐
> **LeetCode #11**

Given `n` non-negative integers representing heights of vertical lines, find two lines that together with the x-axis form a container that holds the most water.

```python
# Example
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
```

> [!hint]- 💡 Hint 1 (Low)
> Area = min(height[left], height[right]) * (right - left)

> [!hint]- 💡 Hint 2 (Mid)
> Start with the widest container (left=0, right=n-1). Move the pointer with the shorter height inward.

> [!success]- ✅ Solution
> ```python
> def max_area(height: list[int]) -> int:
>     left, right = 0, len(height) - 1
>     max_water = 0
>
>     while left < right:
>         width = right - left
>         h = min(height[left], height[right])
>         max_water = max(max_water, width * h)
>
>         if height[left] < height[right]:
>             left += 1
>         else:
>             right -= 1
>
>     return max_water
>
> print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
> ```
> **Time:** O(n) | **Space:** O(1)

---

### Problem 9: Trapping Rain Water ⭐⭐⭐⭐
> **LeetCode #42** | Hard Classic

Given `n` non-negative integers representing elevation map, compute how much water it can trap after raining.

```python
# Example
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
```

> [!hint]- 💡 Hint 1 (Low)
> Water at each position = min(max_left, max_right) - height[i]

> [!hint]- 💡 Hint 2 (Mid)
> Use two pointers with running max from left and right.

> [!hint]- 💡 Hint 3 (High)
> Move the pointer with the smaller max inward, accumulating water.

> [!success]- ✅ Solution
> ```python
> def trap(height: list[int]) -> int:
>     if not height:
>         return 0
>
>     left, right = 0, len(height) - 1
>     left_max, right_max = height[left], height[right]
>     water = 0
>
>     while left < right:
>         if left_max < right_max:
>             left += 1
>             left_max = max(left_max, height[left])
>             water += left_max - height[left]
>         else:
>             right -= 1
>             right_max = max(right_max, height[right])
>             water += right_max - height[right]
>
>     return water
>
> print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
> ```
> **Time:** O(n) | **Space:** O(1)

---

## 🔷 Sliding Window

### Problem 10: Best Time to Buy and Sell Stock ⭐
> **LeetCode #121** | Most Popular Easy Problem

Given an array `prices` where `prices[i]` is the price on day `i`, find the maximum profit from one transaction.

```python
# Example
prices = [7, 1, 5, 3, 6, 4]
# Output: 5 (buy at 1, sell at 6)
```

> [!hint]- 💡 Hint 1 (Low)
> Track the minimum price seen so far.

> [!hint]- 💡 Hint 2 (Mid)
> At each price, calculate profit if selling today. Update max profit.

> [!success]- ✅ Solution
> ```python
> def max_profit(prices: list[int]) -> int:
>     min_price = float('inf')
>     max_profit = 0
>
>     for price in prices:
>         min_price = min(min_price, price)
>         max_profit = max(max_profit, price - min_price)
>
>     return max_profit
>
> print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
> ```
> **Time:** O(n) | **Space:** O(1)

---

### Problem 11: Longest Substring Without Repeating Characters ⭐⭐
> **LeetCode #3** | Classic Sliding Window

Given a string `s`, find the length of the longest substring without repeating characters.

```python
# Example
s = "abcabcbb"
# Output: 3 ("abc")
```

> [!hint]- 💡 Hint 1 (Low)
> Use a sliding window that expands until a duplicate is found.

> [!hint]- 💡 Hint 2 (Mid)
> Use a set to track characters in the current window. Shrink from left when duplicate found.

> [!hint]- 💡 Hint 3 (High)
> Use a dict to store the last index of each character for O(1) window shrinking.

> [!success]- ✅ Solution
> ```python
> def length_of_longest_substring(s: str) -> int:
>     char_index = {}
>     left = 0
>     max_length = 0
>
>     for right, char in enumerate(s):
>         if char in char_index and char_index[char] >= left:
>             left = char_index[char] + 1
>
>         char_index[char] = right
>         max_length = max(max_length, right - left + 1)
>
>     return max_length
>
> print(length_of_longest_substring("abcabcbb"))  # 3
> print(length_of_longest_substring("pwwkew"))    # 3
> ```
> **Time:** O(n) | **Space:** O(min(n, alphabet_size))

---

### Problem 12: Minimum Window Substring ⭐⭐⭐⭐
> **LeetCode #76** | Hard Sliding Window

Given strings `s` and `t`, return the minimum window in `s` that contains all characters in `t`.

```python
# Example
s = "ADOBECODEBANC"
t = "ABC"
# Output: "BANC"
```

> [!hint]- 💡 Hint 1 (Low)
> Use a sliding window. Expand right until all chars found, then shrink left.

> [!hint]- 💡 Hint 2 (Mid)
> Track character counts needed vs. in window. Use a "formed" counter.

> [!success]- ✅ Solution
> ```python
> from collections import Counter
>
> def min_window(s: str, t: str) -> str:
>     if not t or not s:
>         return ""
>
>     need = Counter(t)
>     have = {}
>     required = len(need)
>     formed = 0
>
>     left = 0
>     min_len = float('inf')
>     result = (0, 0)
>
>     for right, char in enumerate(s):
>         have[char] = have.get(char, 0) + 1
>
>         if char in need and have[char] == need[char]:
>             formed += 1
>
>         while formed == required:
>             if right - left + 1 < min_len:
>                 min_len = right - left + 1
>                 result = (left, right + 1)
>
>             left_char = s[left]
>             have[left_char] -= 1
>             if left_char in need and have[left_char] < need[left_char]:
>                 formed -= 1
>             left += 1
>
>     return s[result[0]:result[1]] if min_len != float('inf') else ""
>
> print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
> ```
> **Time:** O(n + m) | **Space:** O(n + m)

---

## 🔷 Binary Search

### Problem 13: Binary Search ⭐
> **LeetCode #704**

Given a sorted array `nums` and a `target`, return its index or -1 if not found.

```python
# Example
nums = [-1, 0, 3, 5, 9, 12]
target = 9
# Output: 4
```

> 
> [!hint]- 💡 Hint
> Use low/high pointers and cut the search space in half.

> [!success]- ✅ Solution
> ```python
> def binary_search(nums: list[int], target: int) -> int:
>     left, right = 0, len(nums) - 1
>
>     while left <= right:
>         mid = (left + right) // 2
>         if nums[mid] == target:
>             return mid
>         elif nums[mid] < target:
>             left = mid + 1
>         else:
>             right = mid - 1
>
>     return -1
> ```
> **Time:** O(log n) | **Space:** O(1)

---

### Problem 14: Search in Rotated Sorted Array ⭐⭐⭐
> **LeetCode #33**

Given a rotated sorted array `nums` and a `target`, return its index or -1.

```python
# Example
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
# Output: 4
```

> [!hint]- 💡 Hint 1 (Low)
> One half of the array is always sorted.

> [!hint]- 💡 Hint 2 (Mid)
> Determine which half is sorted, then check if target is in that range.

> [!success]- ✅ Solution
> ```python
> def search_rotated(nums: list[int], target: int) -> int:
>     left, right = 0, len(nums) - 1
>
>     while left <= right:
>         mid = (left + right) // 2
>
>         if nums[mid] == target:
>             return mid
>
>         # Left half is sorted
>         if nums[left] <= nums[mid]:
>             if nums[left] <= target < nums[mid]:
>                 right = mid - 1
>             else:
>                 left = mid + 1
>         # Right half is sorted
>         else:
>             if nums[mid] < target <= nums[right]:
>                 left = mid + 1
>             else:
>                 right = mid - 1
>
>     return -1
>
> print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # 4
> ```
> **Time:** O(log n) | **Space:** O(1)

---

### Problem 15: Find Minimum in Rotated Sorted Array ⭐⭐
> **LeetCode #153**

Find the minimum element in a rotated sorted array with unique elements.

```python
# Example
nums = [3, 4, 5, 1, 2]
# Output: 1
```

> [!hint]- 💡 Hint 1 (Low)
> The minimum is at the rotation point.

> [!hint]- 💡 Hint 2 (Mid)
> Compare mid with right. If `nums[mid] > nums[right]`, minimum is in right half.

> [!success]- ✅ Solution
> ```python
> def find_min(nums: list[int]) -> int:
>     left, right = 0, len(nums) - 1
>
>     while left < right:
>         mid = (left + right) // 2
>
>         if nums[mid] > nums[right]:
>             left = mid + 1
>         else:
>             right = mid
>
>     return nums[left]
>
> print(find_min([3, 4, 5, 1, 2]))  # 1
> ```
> **Time:** O(log n) | **Space:** O(1)

---

## 🔷 Linked Lists

### Problem 16: Reverse Linked List ⭐
> **LeetCode #206** | Fundamental Problem

Reverse a singly linked list.

> [!hint]- 💡 Hint 1 (Low)
> Use three pointers: prev, curr, next.

> [!success]- ✅ Solution
> ```python
> class ListNode:
>     def __init__(self, val=0, next=None):
>         self.val = val
>         self.next = next
>
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
> ```
> **Time:** O(n) | **Space:** O(1)

---

### Problem 17: Linked List Cycle ⭐
> **LeetCode #141** | Floyd's Algorithm

Detect if a linked list has a cycle.

> [!hint]- 💡 Hint 1 (Low)
> Use slow and fast pointers (Floyd's Tortoise and Hare).

> [!success]- ✅ Solution
> ```python
> def has_cycle(head: ListNode) -> bool:
>     slow = fast = head
>
>     while fast and fast.next:
>         slow = slow.next
>         fast = fast.next.next
>         if slow == fast:
>             return True
>
>     return False
> ```
> **Time:** O(n) | **Space:** O(1)

---

### Problem 18: Merge Two Sorted Lists ⭐
> **LeetCode #21**

Merge two sorted linked lists into one sorted list.

> 
> [!hint]- 💡 Hint
> Use fast/slow or previous/current pointers to traverse.

> [!success]- ✅ Solution
> ```python
> def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
>     dummy = ListNode(0)
>     curr = dummy
>
>     while l1 and l2:
>         if l1.val <= l2.val:
>             curr.next = l1
>             l1 = l1.next
>         else:
>             curr.next = l2
>             l2 = l2.next
>         curr = curr.next
>
>     curr.next = l1 or l2
>     return dummy.next
> ```
> **Time:** O(n + m) | **Space:** O(1)

---

## 🔷 Trees

### Problem 19: Invert Binary Tree ⭐
> **LeetCode #226** | Famous Google Interview Question

Invert a binary tree (mirror image).

> 
> [!hint]- 💡 Hint
> Use recursion or a stack/queue for traversal.

> [!success]- ✅ Solution
> ```python
> class TreeNode:
>     def __init__(self, val=0, left=None, right=None):
>         self.val = val
>         self.left = left
>         self.right = right
>
> def invert_tree(root: TreeNode) -> TreeNode:
>     if not root:
>         return None
>
>     root.left, root.right = root.right, root.left
>     invert_tree(root.left)
>     invert_tree(root.right)
>
>     return root
> ```
> **Time:** O(n) | **Space:** O(h) where h = height

---

### Problem 20: Maximum Depth of Binary Tree ⭐
> **LeetCode #104**

Find the maximum depth (number of nodes along the longest path from root to leaf).

> 
> [!hint]- 💡 Hint
> Use recursion or a stack/queue for traversal.

> [!success]- ✅ Solution
> ```python
> def max_depth(root: TreeNode) -> int:
>     if not root:
>         return 0
>     return 1 + max(max_depth(root.left), max_depth(root.right))
> ```
> **Time:** O(n) | **Space:** O(h)

---

### Problem 21: Validate Binary Search Tree ⭐⭐
> **LeetCode #98**

Determine if a binary tree is a valid BST.

> [!hint]- 💡 Hint 1 (Low)
> Each node must be within a valid range (min, max).

> [!success]- ✅ Solution
> ```python
> def is_valid_bst(root: TreeNode) -> bool:
>     def validate(node, min_val, max_val):
>         if not node:
>             return True
>         if node.val <= min_val or node.val >= max_val:
>             return False
>         return (validate(node.left, min_val, node.val) and
>                 validate(node.right, node.val, max_val))
>
>     return validate(root, float('-inf'), float('inf'))
> ```
> **Time:** O(n) | **Space:** O(h)

---

### Problem 22: Lowest Common Ancestor ⭐⭐
> **LeetCode #236**

Find the lowest common ancestor of two nodes in a binary tree.

> [!hint]- 💡 Hint 1 (Low)
> If both nodes are in one subtree, LCA is in that subtree.

> [!success]- ✅ Solution
> ```python
> def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
>     if not root or root == p or root == q:
>         return root
>
>     left = lowest_common_ancestor(root.left, p, q)
>     right = lowest_common_ancestor(root.right, p, q)
>
>     if left and right:
>         return root
>     return left or right
> ```
> **Time:** O(n) | **Space:** O(h)

---

## 🔷 Dynamic Programming

### Problem 23: Climbing Stairs ⭐
> **LeetCode #70** | Classic DP Introduction

You can climb 1 or 2 steps. How many distinct ways to reach step `n`?

```python
# Example
n = 3
# Output: 3 (1+1+1, 1+2, 2+1)
```

> [!hint]- 💡 Hint 1 (Low)
> This is the Fibonacci sequence!

> [!success]- ✅ Solution
> ```python
> def climb_stairs(n: int) -> int:
>     if n <= 2:
>         return n
>
>     a, b = 1, 2
>     for _ in range(3, n + 1):
>         a, b = b, a + b
>     return b
> ```
> **Time:** O(n) | **Space:** O(1)

---

### Problem 24: House Robber ⭐⭐
> **LeetCode #198**

You can't rob two adjacent houses. Find the maximum amount you can rob.

```python
# Example
nums = [2, 7, 9, 3, 1]
# Output: 12 (2 + 9 + 1)
```

> [!hint]- 💡 Hint 1 (Low)
> At each house: rob it (+ value 2 houses ago) or skip it (keep previous max).

> [!success]- ✅ Solution
> ```python
> def rob(nums: list[int]) -> int:
>     if not nums:
>         return 0
>     if len(nums) == 1:
>         return nums[0]
>
>     prev2, prev1 = 0, 0
>     for num in nums:
>         curr = max(prev2 + num, prev1)
>         prev2, prev1 = prev1, curr
>     return prev1
>
> print(rob([2, 7, 9, 3, 1]))  # 12
> ```
> **Time:** O(n) | **Space:** O(1)

---

### Problem 25: Longest Increasing Subsequence ⭐⭐⭐
> **LeetCode #300**

Find the length of the longest strictly increasing subsequence.

```python
# Example
nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4 ([2, 3, 7, 101])
```

> [!hint]- 💡 Hint 1 (Low)
> DP: `dp[i]` = length of LIS ending at index `i`.

> [!hint]- 💡 Hint 2 (Mid)
> For each element, check all previous elements that are smaller.

> [!hint]- 💡 Hint 3 (High)
> Optimize to O(n log n) with binary search on a "tails" array.

> [!success]- ✅ Solution
> ```python
> # O(n²) DP Solution
> def length_of_lis(nums: list[int]) -> int:
>     if not nums:
>         return 0
>
>     dp = [1] * len(nums)
>
>     for i in range(1, len(nums)):
>         for j in range(i):
>             if nums[j] < nums[i]:
>                 dp[i] = max(dp[i], dp[j] + 1)
>
>     return max(dp)
>
> # O(n log n) Binary Search Solution
> import bisect
>
> def length_of_lis_optimized(nums: list[int]) -> int:
>     tails = []
>     for num in nums:
>         pos = bisect.bisect_left(tails, num)
>         if pos == len(tails):
>             tails.append(num)
>         else:
>             tails[pos] = num
>     return len(tails)
>
> print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
> ```
> **Time:** O(n²) or O(n log n) | **Space:** O(n)

---

## 📚 Resources

| Resource | Description |
|----------|-------------|
| [NeetCode Blind 75](https://neetcode.io/practice/practice/blind75) | Video solutions for all problems |
| [Tech Interview Handbook](https://www.techinterviewhandbook.org/best-practice-questions/) | Original Blind 75 author |
| [LeetCode Patterns](https://blog.algomaster.io/p/15-leetcode-patterns) | 15 essential patterns |

---

*Master these 25 problems, and you'll have a solid foundation for coding interviews!*
