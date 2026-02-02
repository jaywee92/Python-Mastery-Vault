# Interview Classics (Beginner-Friendly)
Notebook: [[22_Interview_Classics_Easy.ipynb]]


> **Difficulty:** ⭐⭐ - ⭐⭐⭐
> **Focus:** Arrays, Hash Maps, Stacks
> **Note:** Inspired by common interview platforms (LeetCode-style)

---

## I1: Two Sum
**Task:** Return indices of two numbers that add up to `target`.

```python
nums = [2, 7, 11, 15]
target = 9
# expected: [0, 1]
```

> [!hint]- 💡 Hint 1 (Low)
> Try all pairs with two loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use a dictionary to store seen values and indices.

> [!hint]- 💡 Hint 3 (High)
> Check if `target - num` exists in the dictionary.

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

## I2: Contains Duplicate
**Task:** Return `True` if any value appears at least twice.

```python
nums = [1, 2, 3, 1]
# expected: True
```

> [!hint]- 💡 Hint 1 (Low)
> A set keeps only unique values.

> [!hint]- 💡 Hint 2 (Mid)
> If `len(set(nums))` is smaller, duplicates exist.

> [!hint]- 💡 Hint 3 (High)
> Compare length of list and set.

> [!success]- ✅ Solution
> ```python
> def contains_duplicate(nums):
>     return len(nums) != len(set(nums))
> 
> print(contains_duplicate([1, 2, 3, 1]))  # True
> ```

---

## I3: Valid Parentheses
**Task:** Check if parentheses are balanced.

```python
s = "()[]{}"
# expected: True
```

> [!hint]- 💡 Hint 1 (Low)
> Use a stack to track opening brackets.

> [!hint]- 💡 Hint 2 (Mid)
> When you see a closing bracket, it must match the top.

> [!hint]- 💡 Hint 3 (High)
> Use a dictionary: `pairs = {')': '(', ']': '[', '}': '{'}`.

> [!success]- ✅ Solution
> ```python
> def is_valid(s):
>     pairs = {')': '(', ']': '[', '}': '{'}
>     stack = []
>     for ch in s:
>         if ch in pairs.values():
>             stack.append(ch)
>         else:
>             if not stack or stack.pop() != pairs[ch]:
>                 return False
>     return not stack
> 
> print(is_valid("()[]{}"))  # True
> ```

---

## I4: Best Time to Buy and Sell Stock
**Task:** Return the maximum profit from one buy and one sell.

```python
prices = [7, 1, 5, 3, 6, 4]
# expected: 5  (buy at 1, sell at 6)
```

> [!hint]- 💡 Hint 1 (Low)
> Track the lowest price so far.

> [!hint]- 💡 Hint 2 (Mid)
> Compare current price with lowest and update max profit.

> [!hint]- 💡 Hint 3 (High)
> `profit = max(profit, price - min_price)`.

> [!success]- ✅ Solution
> ```python
> def max_profit(prices):
>     min_price = float("inf")
>     best = 0
>     for price in prices:
>         min_price = min(min_price, price)
>         best = max(best, price - min_price)
>     return best
> 
> print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
> ```

---

## I5: Valid Anagram
**Task:** Return `True` if two strings are anagrams.

```python
s = "anagram"
t = "nagaram"
# expected: True
```

> [!hint]- 💡 Hint 1 (Low)
> Count character frequency.

> [!hint]- 💡 Hint 2 (Mid)
> Sort both strings and compare.

> [!hint]- 💡 Hint 3 (High)
> `sorted(s) == sorted(t)` is simplest.

> [!success]- ✅ Solution
> ```python
> def is_anagram(s, t):
>     return sorted(s) == sorted(t)
> 
> print(is_anagram("anagram", "nagaram"))  # True
> ```

