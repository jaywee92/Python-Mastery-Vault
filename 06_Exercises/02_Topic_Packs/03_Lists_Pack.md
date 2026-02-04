# Lists Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** Lists and list processing

Notebook: [[03_Lists_Pack.ipynb]]

---

## L1: Double Each Number
**Task:** Return a new list with each value doubled.

```python
nums = [1, 2, 3]
# expected: [2, 4, 6]
```

> [!hint]- 💡 Hint 1 (Low)
> Use a loop and append doubled values.

> [!hint]- 💡 Hint 2 (Mid)
> A list comprehension can do this in one line.

> [!hint]- 💡 Hint 3 (High)
> `return [n * 2 for n in nums]`

> [!success]- ✅ Solution
> ```python
> def double(nums):
>     return [n * 2 for n in nums]
> 
> print(double([1, 2, 3]))  # [2, 4, 6]
> ```

---

---

## L2: Sum of Positives
**Task:** Sum only the positive numbers.

```python
nums = [-2, 5, -1, 3]
# expected: 8
```

> [!hint]- 💡 Hint 1 (Low)
> Check if a number is greater than 0.

> [!hint]- 💡 Hint 2 (Mid)
> Add to total only if positive.

> [!hint]- 💡 Hint 3 (High)
> Use a loop and `if n > 0`.

> [!success]- ✅ Solution
> ```python
> def sum_positives(nums):
>     total = 0
>     for n in nums:
>         if n > 0:
>             total += n
>     return total
> 
> print(sum_positives([-2, 5, -1, 3]))  # 8
> ```

---

---

## L3: Find Maximum
**Task:** Return the largest number in a list (without using `max`).

```python
nums = [5, 1, 9, 2]
# expected: 9
```

> [!hint]- 💡 Hint 1 (Low)
> Start with the first number as the current max.

> [!hint]- 💡 Hint 2 (Mid)
> Compare each number with the current max.

> [!hint]- 💡 Hint 3 (High)
> Update if `n > current_max`.

> [!success]- ✅ Solution
> ```python
> def find_max(nums):
>     current_max = nums[0]
>     for n in nums[1:]:
>         if n > current_max:
>             current_max = n
>     return current_max
> 
> print(find_max([5, 1, 9, 2]))  # 9
> ```

---

---

## L4: Count Occurrences
**Task:** Count how often each number appears.

```python
nums = [1, 2, 1, 3, 2, 1]
# expected: {1: 3, 2: 2, 3: 1}
```

> [!hint]- 💡 Hint 1 (Low)
> Use a dictionary to store counts.

> [!hint]- 💡 Hint 2 (Mid)
> Increment for each value.

> [!hint]- 💡 Hint 3 (High)
> `counts[n] = counts.get(n, 0) + 1`

> [!success]- ✅ Solution
> ```python
> def count_numbers(nums):
>     counts = {}
>     for n in nums:
>         counts[n] = counts.get(n, 0) + 1
>     return counts
> 
> print(count_numbers([1, 2, 1, 3, 2, 1]))
> # {1: 3, 2: 2, 3: 1}
> ```

---

---

## L5: Remove Negatives
**Task:** Return a new list without negative numbers.

```python
nums = [3, -1, 4, -2, 5]
# expected: [3, 4, 5]
```

> [!hint]- 💡 Hint 1 (Low)
> Filter values using a condition.

> [!hint]- 💡 Hint 2 (Mid)
> Use a list comprehension.

> [!hint]- 💡 Hint 3 (High)
> `return [n for n in nums if n >= 0]`

> [!success]- ✅ Solution
> ```python
> def remove_negatives(nums):
>     return [n for n in nums if n >= 0]
> 
> print(remove_negatives([3, -1, 4, -2, 5]))  # [3, 4, 5]
> ```

---

## L6: Append Item
**Task:** Append `3` to `items` and print the list.

```python
items = [1, 2]
# expected: [1,2,3]
```

> [!hint]- 💡 Hint 1 (Low)
> Use list methods.

> [!hint]- 💡 Hint 2 (Mid)
> Modify the list, then print it.

> [!hint]- 💡 Hint 3 (High)
> Most tasks are one line.

> [!success]- ✅ Solution
> ```python
> items = [1, 2]
> items.append(3)
> print(items)
> ```

---

---

## L7: Insert Item
**Task:** Insert `2` at index 1 in `items` and print the list.

```python
items = [1, 3]
# expected: [1,2,3]
```

> [!hint]- 💡 Hint 1 (Low)
> Use list methods.

> [!hint]- 💡 Hint 2 (Mid)
> Modify the list, then print it.

> [!hint]- 💡 Hint 3 (High)
> Most tasks are one line.

> [!success]- ✅ Solution
> ```python
> items = [1, 3]
> items.insert(1, 2)
> print(items)
> ```

---

---

## L8: Remove Item
**Task:** Remove the value `2` from `items` and print the list.

```python
items = [1, 2, 3]
# expected: [1,3]
```

> [!hint]- 💡 Hint 1 (Low)
> Use list methods.

> [!hint]- 💡 Hint 2 (Mid)
> Modify the list, then print it.

> [!hint]- 💡 Hint 3 (High)
> Most tasks are one line.

> [!success]- ✅ Solution
> ```python
> items = [1, 2, 3]
> items.remove(2)
> print(items)
> ```

---

---

## L9: Pop Last
**Task:** Pop the last item and print the popped value.

```python
items = [1, 2, 3]
# expected: 3
```

> [!hint]- 💡 Hint 1 (Low)
> Use list methods.

> [!hint]- 💡 Hint 2 (Mid)
> Modify the list, then print it.

> [!hint]- 💡 Hint 3 (High)
> Most tasks are one line.

> [!success]- ✅ Solution
> ```python
> items = [1, 2, 3]
> print(items.pop())
> ```

---

---

## L10: Slice Middle
**Task:** Slice out the middle items to get `[2, 3]`.

```python
items = [1, 2, 3, 4]
# expected: [2,3]
```

> [!hint]- 💡 Hint 1 (Low)
> Use list methods.

> [!hint]- 💡 Hint 2 (Mid)
> Modify the list, then print it.

> [!hint]- 💡 Hint 3 (High)
> Most tasks are one line.

> [!success]- ✅ Solution
> ```python
> items = [1, 2, 3, 4]
> print(items[1:3])
> ```

---

---

## L11: Length
**Task:** Get the length of `items` and print it.

```python
items = [1, 2, 3]
# expected: 3
```

> [!hint]- 💡 Hint 1 (Low)
> Use list methods.

> [!hint]- 💡 Hint 2 (Mid)
> Modify the list, then print it.

> [!hint]- 💡 Hint 3 (High)
> Most tasks are one line.

> [!success]- ✅ Solution
> ```python
> items = [1, 2, 3]
> print(len(items))
> ```

---

---

## L12: Sum
**Task:** Sum all numbers in `items` and print the result.

```python
items = [1, 2, 3]
# expected: 6
```

> [!hint]- 💡 Hint 1 (Low)
> Use list methods.

> [!hint]- 💡 Hint 2 (Mid)
> Modify the list, then print it.

> [!hint]- 💡 Hint 3 (High)
> Most tasks are one line.

> [!success]- ✅ Solution
> ```python
> items = [1, 2, 3]
> print(sum(items))
> ```

---

---

## L13: Max
**Task:** Find the maximum value in `items` and print it.

```python
items = [5, 2, 9]
# expected: 9
```

> [!hint]- 💡 Hint 1 (Low)
> Use list methods.

> [!hint]- 💡 Hint 2 (Mid)
> Modify the list, then print it.

> [!hint]- 💡 Hint 3 (High)
> Most tasks are one line.

> [!success]- ✅ Solution
> ```python
> items = [5, 2, 9]
> print(max(items))
> ```

---

---

## L14: Min
**Task:** Find the minimum value in `items` and print it.

```python
items = [5, 2, 9]
# expected: 2
```

> [!hint]- 💡 Hint 1 (Low)
> Use list methods.

> [!hint]- 💡 Hint 2 (Mid)
> Modify the list, then print it.

> [!hint]- 💡 Hint 3 (High)
> Most tasks are one line.

> [!success]- ✅ Solution
> ```python
> items = [5, 2, 9]
> print(min(items))
> ```

---

---

## L15: Sort
**Task:** Sort `items` in ascending order and print the list.

```python
items = [3, 1, 2]
# expected: [1,2,3]
```

> [!hint]- 💡 Hint 1 (Low)
> Use list methods.

> [!hint]- 💡 Hint 2 (Mid)
> Modify the list, then print it.

> [!hint]- 💡 Hint 3 (High)
> Most tasks are one line.

> [!success]- ✅ Solution
> ```python
> items = [3, 1, 2]
> items.sort()
> print(items)
> ```

---

---
