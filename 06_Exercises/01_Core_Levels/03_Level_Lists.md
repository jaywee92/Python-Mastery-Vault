# Level 3: Lists
Notebook: [[03_Level_Lists.ipynb]]


> **Difficulty:** ⭐⭐ Beginner-Intermediate
> **Topics:** List Creation, Indexing, Methods, Basic Operations
> **Prerequisites:** [[02_Level_Strings|Level 2]], [[../../01_Python_Basics/02_Lists_Deep_Dive|Lists Deep Dive]]

---

## Exercise 3.1: Create and Access
**Task:** Create a list with numbers 1-5 and print the third element.

**Expected Output:**
```
Third element: 3
```

> [!hint]- Hint
> Remember: indexing starts at 0, so third element is at index 2.

> [!success]- Solution
> ```python
> numbers = [1, 2, 3, 4, 5]
> print(f"Third element: {numbers[2]}")
> ```

---

## Exercise 3.2: List Length
**Task:** Given `fruits = ["apple", "banana", "cherry", "date", "elderberry"]`, print how many fruits there are.

**Expected Output:**
```
Number of fruits: 5
```

> [!hint]- Hint
> Use `len()` function.

> [!success]- Solution
> ```python
> fruits = ["apple", "banana", "cherry", "date", "elderberry"]
> print(f"Number of fruits: {len(fruits)}")
> ```

---

## Exercise 3.3: Append Element
**Task:** Start with `colors = ["red", "green"]` and add "blue" to the end.

**Expected Output:**
```
['red', 'green', 'blue']
```

> [!hint]- Hint
> Use the `.append()` method.

> [!success]- Solution
> ```python
> colors = ["red", "green"]
> colors.append("blue")
> print(colors)
> ```

---

## Exercise 3.4: Insert Element
**Task:** Given `numbers = [1, 2, 4, 5]`, insert 3 at the correct position.

**Expected Output:**
```
[1, 2, 3, 4, 5]
```

> [!hint]- Hint
> Use `.insert(index, element)` method.

> [!success]- Solution
> ```python
> numbers = [1, 2, 4, 5]
> numbers.insert(2, 3)
> print(numbers)
> ```

---

## Exercise 3.5: Remove Element
**Task:** Given `animals = ["cat", "dog", "bird", "dog", "fish"]`, remove the first "dog".

**Expected Output:**
```
['cat', 'bird', 'dog', 'fish']
```

> [!hint]- Hint
> Use `.remove()` method - it removes only the first occurrence.

> [!success]- Solution
> ```python
> animals = ["cat", "dog", "bird", "dog", "fish"]
> animals.remove("dog")
> print(animals)
> ```

---

## Exercise 3.6: Pop Element
**Task:** Given `stack = [1, 2, 3, 4, 5]`, remove and print the last element.

**Expected Output:**
```
Popped: 5
Remaining: [1, 2, 3, 4]
```

> [!hint]- Hint
> Use `.pop()` method - it removes and returns the last element.

> [!success]- Solution
> ```python
> stack = [1, 2, 3, 4, 5]
> popped = stack.pop()
> print(f"Popped: {popped}")
> print(f"Remaining: {stack}")
> ```

---

## Exercise 3.7: List Slicing
**Task:** Given `letters = ['a', 'b', 'c', 'd', 'e', 'f']`, extract elements from index 2 to 4.

**Expected Output:**
```
['c', 'd', 'e']
```

> [!hint]- Hint
> Use slicing: `list[start:end+1]`

> [!success]- Solution
> ```python
> letters = ['a', 'b', 'c', 'd', 'e', 'f']
> print(letters[2:5])
> ```

---

## Exercise 3.8: Reverse List
**Task:** Given `numbers = [1, 2, 3, 4, 5]`, reverse it in place.

**Expected Output:**
```
[5, 4, 3, 2, 1]
```

> [!hint]- Hint
> Use `.reverse()` method or slicing `[::-1]`.

> [!success]- Solution
> ```python
> numbers = [1, 2, 3, 4, 5]
> numbers.reverse()
> print(numbers)
> # Or: print(numbers[::-1])
> ```

---

## Exercise 3.9: Sort List
**Task:** Given `scores = [85, 92, 78, 95, 88]`, sort in ascending and descending order.

**Expected Output:**
```
Ascending: [78, 85, 88, 92, 95]
Descending: [95, 92, 88, 85, 78]
```

> [!hint]- Hint
> Use `.sort()` or `sorted()`. For descending, use `reverse=True`.

> [!success]- Solution
> ```python
> scores = [85, 92, 78, 95, 88]
> ascending = sorted(scores)
> descending = sorted(scores, reverse=True)
> print(f"Ascending: {ascending}")
> print(f"Descending: {descending}")
> ```

---

## Exercise 3.10: Find Element
**Task:** Given `names = ["Alice", "Bob", "Charlie", "David"]`, find the index of "Charlie".

**Expected Output:**
```
Index of Charlie: 2
```

> [!hint]- Hint
> Use the `.index()` method.

> [!success]- Solution
> ```python
> names = ["Alice", "Bob", "Charlie", "David"]
> print(f"Index of Charlie: {names.index('Charlie')}")
> ```

---

## Exercise 3.11: Count Occurrences
**Task:** Given `votes = ["A", "B", "A", "C", "A", "B", "A"]`, count how many times "A" appears.

**Expected Output:**
```
Votes for A: 4
```

> [!hint]- Hint
> Use the `.count()` method.

> [!success]- Solution
> ```python
> votes = ["A", "B", "A", "C", "A", "B", "A"]
> print(f"Votes for A: {votes.count('A')}")
> ```

---

## Exercise 3.12: Concatenate Lists
**Task:** Combine `list1 = [1, 2, 3]` and `list2 = [4, 5, 6]` into one list.

**Expected Output:**
```
[1, 2, 3, 4, 5, 6]
```

> [!hint]- Hint
> Use `+` operator or `.extend()` method.

> [!success]- Solution
> ```python
> list1 = [1, 2, 3]
> list2 = [4, 5, 6]
> combined = list1 + list2
> print(combined)
> ```

---

## Exercise 3.13: List Min/Max/Sum
**Task:** Given `numbers = [23, 45, 12, 67, 34]`, find the minimum, maximum, and sum.

**Expected Output:**
```
Min: 12
Max: 67
Sum: 181
```

> [!hint]- Hint
> Use `min()`, `max()`, and `sum()` functions.

> [!success]- Solution
> ```python
> numbers = [23, 45, 12, 67, 34]
> print(f"Min: {min(numbers)}")
> print(f"Max: {max(numbers)}")
> print(f"Sum: {sum(numbers)}")
> ```

---

## Exercise 3.14: Check Membership
**Task:** Given `fruits = ["apple", "banana", "cherry"]`, check if "banana" and "mango" are in the list.

**Expected Output:**
```
banana in list: True
mango in list: False
```

> [!hint]- Hint
> Use the `in` operator.

> [!success]- Solution
> ```python
> fruits = ["apple", "banana", "cherry"]
> print(f"banana in list: {'banana' in fruits}")
> print(f"mango in list: {'mango' in fruits}")
> ```

---

## Exercise 3.15: Copy List
**Task:** Create a copy of `original = [1, 2, 3]` and modify the copy without affecting the original.

**Expected Output:**
```
Original: [1, 2, 3]
Copy: [1, 2, 3, 4]
```

> [!hint]- Hint
> Use `.copy()` or slicing `[:]` to create a real copy.

> [!success]- Solution
> ```python
> original = [1, 2, 3]
> copy = original.copy()  # or: copy = original[:]
> copy.append(4)
> print(f"Original: {original}")
> print(f"Copy: {copy}")
> ```

---

## 🎯 Level 3 Complete!

**Skills Practiced:**
- List creation and indexing
- Adding elements (append, insert, extend)
- Removing elements (remove, pop)
- Slicing and reversing
- Sorting and searching
- List operations (min, max, sum, len)

**Next Level:** [[04_Level_Conditionals|Level 4: Conditionals]]
