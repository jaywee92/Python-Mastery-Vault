# Challenge: Array Problems 🏆
Notebook: [[11_Challenge_Arrays.ipynb]]


> **Difficulty:** ⭐⭐⭐ - ⭐⭐⭐⭐⭐
> **Style:** LeetCode / Codewars
> **Topics:** Lists, Loops, Conditionals, Sorting, Two Pointers

---

## C1: Two Sum ⭐⭐
**Task:** Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.

```python
def two_sum(nums: list, target: int) -> list:
    pass

# Example:
# two_sum([2, 7, 11, 15], 9) → [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9
# two_sum([3, 2, 4], 6) → [1, 2]
```

> [!hint]- 💡 Hint 1 (Low)
> You could use two nested loops to check every pair.

> [!hint]- 💡 Hint 2 (Mid)
> A dictionary can store numbers you've seen and their indices.

> [!hint]- 💡 Hint 3 (High)
> For each number, check if `target - num` exists in your dictionary.

> [!success]- Solution
> ```python
> def two_sum(nums: list, target: int) -> list:
>     seen = {}
>     for i, num in enumerate(nums):
>         complement = target - num
>         if complement in seen:
>             return [seen[complement], i]
>         seen[num] = i
>     return []
> ```
> **Complexity:** O(n) time, O(n) space

---

## C2: Maximum Subarray ⭐⭐⭐
**Task:** Find the contiguous subarray with the largest sum.

```python
def max_subarray(nums: list) -> int:
    pass

# Example:
# max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) → 6  # [4, -1, 2, 1]
# max_subarray([1]) → 1
# max_subarray([5, 4, -1, 7, 8]) → 23
```

> [!hint]- 💡 Hint 1 (Low)
> Think about when you should start a new subarray vs extend the current one.

> [!hint]- 💡 Hint 2 (Mid)
> Kadane's Algorithm: Keep track of current sum and max sum.

> [!hint]- 💡 Hint 3 (High)
> `current = max(num, current + num)` - decide to start fresh or continue.

> [!success]- Solution
> ```python
> def max_subarray(nums: list) -> int:
>     current_sum = max_sum = nums[0]
>     for num in nums[1:]:
>         current_sum = max(num, current_sum + num)
>         max_sum = max(max_sum, current_sum)
>     return max_sum
> ```
> **Complexity:** O(n) time, O(1) space

---

## C3: Move Zeroes ⭐⭐
**Task:** Move all zeroes to the end while maintaining the order of non-zero elements. Do this in-place.

```python
def move_zeroes(nums: list) -> None:
    pass

# Example:
# nums = [0, 1, 0, 3, 12]
# move_zeroes(nums)
# nums → [1, 3, 12, 0, 0]
```

> [!hint]- 💡 Hint 1 (Low)
> Use two pointers - one for the current position, one for placing non-zeros.

> [!hint]- 💡 Hint 2 (Mid)
> When you find a non-zero, swap it with the position of the slow pointer.

> [!hint]- 💡 Hint 3 (High)
> `slow` tracks where to place the next non-zero. Swap when `nums[fast] != 0`.

> [!success]- Solution
> ```python
> def move_zeroes(nums: list) -> None:
>     slow = 0
>     for fast in range(len(nums)):
>         if nums[fast] != 0:
>             nums[slow], nums[fast] = nums[fast], nums[slow]
>             slow += 1
> ```
> **Complexity:** O(n) time, O(1) space

---

## C4: Product Except Self ⭐⭐⭐
**Task:** Return an array where each element is the product of all elements except itself. No division allowed!

```python
def product_except_self(nums: list) -> list:
    pass

# Example:
# product_except_self([1, 2, 3, 4]) → [24, 12, 8, 6]
# product_except_self([-1, 1, 0, -3, 3]) → [0, 0, 9, 0, 0]
```

> [!hint]- 💡 Hint 1 (Low)
> For each position, you need the product of all elements to the left AND right.

> [!hint]- 💡 Hint 2 (Mid)
> First pass: calculate left products. Second pass: multiply by right products.

> [!hint]- 💡 Hint 3 (High)
> Build prefix products from left, then multiply in suffix products from right.

> [!success]- Solution
> ```python
> def product_except_self(nums: list) -> list:
>     n = len(nums)
>     result = [1] * n
>
>     # Left products
>     left = 1
>     for i in range(n):
>         result[i] = left
>         left *= nums[i]
>
>     # Right products
>     right = 1
>     for i in range(n - 1, -1, -1):
>         result[i] *= right
>         right *= nums[i]
>
>     return result
> ```
> **Complexity:** O(n) time, O(1) space (excluding output)

---

## C5: Container With Most Water ⭐⭐⭐
**Task:** Given heights, find two lines that together with the x-axis form a container with the most water.

```python
def max_area(height: list) -> int:
    pass

# Example:
# max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) → 49
# max_area([1, 1]) → 1
```

> [!hint]- 💡 Hint 1 (Low)
> Area = width × min(left_height, right_height). Start from the widest.

> [!hint]- 💡 Hint 2 (Mid)
> Use two pointers at the ends. Move the shorter one inward.

> [!hint]- 💡 Hint 3 (High)
> Moving the shorter line might find a taller one, improving area.

> [!success]- Solution
> ```python
> def max_area(height: list) -> int:
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
> ```
> **Complexity:** O(n) time, O(1) space

---

## C6: Rotate Array ⭐⭐
**Task:** Rotate an array to the right by `k` steps in-place.

```python
def rotate(nums: list, k: int) -> None:
    pass

# Example:
# nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# rotate(nums, 3)
# nums → [5, 6, 7, 1, 2, 3, 4]
```

> [!hint]- 💡 Hint 1 (Low)
> What if k is larger than the array length? Use modulo.

> [!hint]- 💡 Hint 2 (Mid)
> Reversing parts of the array can achieve rotation.

> [!hint]- 💡 Hint 3 (High)
> Reverse entire array, then reverse first k, then reverse rest.

> [!success]- Solution
> ```python
> def rotate(nums: list, k: int) -> None:
>     def reverse(start, end):
>         while start < end:
>             nums[start], nums[end] = nums[end], nums[start]
>             start += 1
>             end -= 1
>
>     n = len(nums)
>     k = k % n
>     reverse(0, n - 1)
>     reverse(0, k - 1)
>     reverse(k, n - 1)
> ```
> **Complexity:** O(n) time, O(1) space

---

## C7: Find Duplicate ⭐⭐⭐
**Task:** Find the duplicate number in an array of n+1 integers where each is in range [1, n].

```python
def find_duplicate(nums: list) -> int:
    pass

# Example:
# find_duplicate([1, 3, 4, 2, 2]) → 2
# find_duplicate([3, 1, 3, 4, 2]) → 3
```

> [!hint]- 💡 Hint 1 (Low)
> You could sort and check adjacent elements (but O(n log n)).

> [!hint]- 💡 Hint 2 (Mid)
> Think of the array as a linked list where value = next index.

> [!hint]- 💡 Hint 3 (High)
> Floyd's Cycle Detection (tortoise and hare) - find where cycles meet.

> [!success]- Solution
> ```python
> def find_duplicate(nums: list) -> int:
>     # Floyd's Cycle Detection
>     slow = fast = nums[0]
>
>     # Find meeting point
>     while True:
>         slow = nums[slow]
>         fast = nums[nums[fast]]
>         if slow == fast:
>             break
>
>     # Find cycle start
>     slow = nums[0]
>     while slow != fast:
>         slow = nums[slow]
>         fast = nums[fast]
>
>     return slow
> ```
> **Complexity:** O(n) time, O(1) space

---

## C8: Merge Sorted Arrays ⭐⭐
**Task:** Merge two sorted arrays in-place. nums1 has extra space at the end.

```python
def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    pass

# Example:
# nums1 = [1, 2, 3, 0, 0, 0], m = 3
# nums2 = [2, 5, 6], n = 3
# merge(nums1, m, nums2, n)
# nums1 → [1, 2, 2, 3, 5, 6]
```

> [!hint]- 💡 Hint 1 (Low)
> Start from the end to avoid overwriting elements we still need.

> [!hint]- 💡 Hint 2 (Mid)
> Use three pointers: one for each array and one for placement.

> [!hint]- 💡 Hint 3 (High)
> Compare from the back, place larger element at the end of nums1.

> [!success]- Solution
> ```python
> def merge(nums1: list, m: int, nums2: list, n: int) -> None:
>     p1, p2, p = m - 1, n - 1, m + n - 1
>
>     while p2 >= 0:
>         if p1 >= 0 and nums1[p1] > nums2[p2]:
>             nums1[p] = nums1[p1]
>             p1 -= 1
>         else:
>             nums1[p] = nums2[p2]
>             p2 -= 1
>         p -= 1
> ```
> **Complexity:** O(m + n) time, O(1) space

---

## C9: Best Time to Buy/Sell Stock ⭐⭐
**Task:** Find maximum profit from buying and selling a stock once.

```python
def max_profit(prices: list) -> int:
    pass

# Example:
# max_profit([7, 1, 5, 3, 6, 4]) → 5  # Buy at 1, sell at 6
# max_profit([7, 6, 4, 3, 1]) → 0  # No profit possible
```

> [!hint]- 💡 Hint 1 (Low)
> You must buy before you sell. Track the minimum price seen so far.

> [!hint]- 💡 Hint 2 (Mid)
> At each price, calculate potential profit if you sold now.

> [!hint]- 💡 Hint 3 (High)
> Update min_price and max_profit as you iterate through prices.

> [!success]- Solution
> ```python
> def max_profit(prices: list) -> int:
>     min_price = float('inf')
>     max_profit = 0
>
>     for price in prices:
>         min_price = min(min_price, price)
>         profit = price - min_price
>         max_profit = max(max_profit, profit)
>
>     return max_profit
> ```
> **Complexity:** O(n) time, O(1) space

---

## C10: 3Sum ⭐⭐⭐⭐
**Task:** Find all unique triplets that sum to zero.

```python
def three_sum(nums: list) -> list:
    pass

# Example:
# three_sum([-1, 0, 1, 2, -1, -4]) → [[-1, -1, 2], [-1, 0, 1]]
# three_sum([0, 1, 1]) → []
# three_sum([0, 0, 0]) → [[0, 0, 0]]
```

> [!hint]- 💡 Hint 1 (Low)
> Sort the array first to easily skip duplicates.

> [!hint]- 💡 Hint 2 (Mid)
> Fix one number, then use two pointers for the remaining two.

> [!hint]- 💡 Hint 3 (High)
> Skip duplicate values for all three positions to avoid duplicate triplets.

> [!success]- Solution
> ```python
> def three_sum(nums: list) -> list:
>     nums.sort()
>     result = []
>     n = len(nums)
>
>     for i in range(n - 2):
>         if i > 0 and nums[i] == nums[i-1]:
>             continue
>
>         left, right = i + 1, n - 1
>         while left < right:
>             total = nums[i] + nums[left] + nums[right]
>             if total < 0:
>                 left += 1
>             elif total > 0:
>                 right -= 1
>             else:
>                 result.append([nums[i], nums[left], nums[right]])
>                 while left < right and nums[left] == nums[left + 1]:
>                     left += 1
>                 while left < right and nums[right] == nums[right - 1]:
>                     right -= 1
>                 left += 1
>                 right -= 1
>
>     return result
> ```
> **Complexity:** O(n²) time, O(1) space

---

## 🎯 Array Challenges Complete!

**Skills Practiced:**
- Two Pointer Technique
- Sliding Window
- Prefix/Suffix Products
- Floyd's Cycle Detection
- Kadane's Algorithm
- In-place modifications

**Next Challenge:** [[12_Challenge_Strings|String Challenges]]
