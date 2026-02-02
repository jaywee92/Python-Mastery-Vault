# Level 7: Tuples & Sets
Notebook: [[07_Level_Tuples_Sets.ipynb]]


> **Difficulty:** ⭐⭐⭐ Intermediate
> **Topics:** Tuple Operations, Set Operations, Immutability, Set Methods
> **Prerequisites:** [[06_Level_Functions|Level 6]], [[../../01_Python_Basics/03_Tuples_and_Sets|Tuples and Sets]]

---

## Exercise 7.1: Create Tuple
**Task:** Create a tuple with the coordinates `(10, 20, 30)` and print each value.

**Expected Output:**
```
x: 10, y: 20, z: 30
```

> [!hint]- Hint
> Unpack the tuple: `x, y, z = coordinates`.

> [!success]- Solution
> ```python
> coordinates = (10, 20, 30)
> x, y, z = coordinates
> print(f"x: {x}, y: {y}, z: {z}")
> ```

---

## Exercise 7.2: Tuple Unpacking
**Task:** Swap two variables using tuple unpacking without a temp variable.

**Expected Output:**
```
Before: a=5, b=10
After: a=10, b=5
```

> [!hint]- Hint
> Use `a, b = b, a`.

> [!success]- Solution
> ```python
> a, b = 5, 10
> print(f"Before: a={a}, b={b}")
> a, b = b, a
> print(f"After: a={a}, b={b}")
> ```

---

## Exercise 7.3: Named Tuple
**Task:** Use tuple unpacking with `*rest` to get first element and remaining elements.

**Given:** `numbers = (1, 2, 3, 4, 5)`

**Expected Output:**
```
First: 1
Rest: [2, 3, 4, 5]
```

> [!hint]- Hint
> Use `first, *rest = numbers`.

> [!success]- Solution
> ```python
> numbers = (1, 2, 3, 4, 5)
> first, *rest = numbers
> print(f"First: {first}")
> print(f"Rest: {rest}")
> ```

---

## Exercise 7.4: Tuple as Dictionary Key
**Task:** Create a dictionary where tuple coordinates are keys with city names as values.

**Expected Output:**
```
City at (40.7128, -74.0060): New York
```

> [!hint]- Hint
> Tuples are hashable and can be used as dictionary keys.

> [!success]- Solution
> ```python
> cities = {
>     (40.7128, -74.0060): "New York",
>     (51.5074, -0.1278): "London",
>     (48.8566, 2.3522): "Paris"
> }
>
> print(f"City at (40.7128, -74.0060): {cities[(40.7128, -74.0060)]}")
> ```

---

## Exercise 7.5: Create Set
**Task:** Create a set from `numbers = [1, 2, 2, 3, 3, 3, 4]` and print unique values.

**Expected Output:**
```
Unique: {1, 2, 3, 4}
Count: 4
```

> [!hint]- Hint
> Use `set()` to create a set from a list.

> [!success]- Solution
> ```python
> numbers = [1, 2, 2, 3, 3, 3, 4]
> unique = set(numbers)
> print(f"Unique: {unique}")
> print(f"Count: {len(unique)}")
> ```

---

## Exercise 7.6: Set Union
**Task:** Find the union of `set_a = {1, 2, 3}` and `set_b = {3, 4, 5}`.

**Expected Output:**
```
Union: {1, 2, 3, 4, 5}
```

> [!hint]- Hint
> Use `|` operator or `.union()` method.

> [!success]- Solution
> ```python
> set_a = {1, 2, 3}
> set_b = {3, 4, 5}
> union = set_a | set_b  # or set_a.union(set_b)
> print(f"Union: {union}")
> ```

---

## Exercise 7.7: Set Intersection
**Task:** Find common elements between `set_a = {1, 2, 3, 4}` and `set_b = {3, 4, 5, 6}`.

**Expected Output:**
```
Common: {3, 4}
```

> [!hint]- Hint
> Use `&` operator or `.intersection()` method.

> [!success]- Solution
> ```python
> set_a = {1, 2, 3, 4}
> set_b = {3, 4, 5, 6}
> common = set_a & set_b  # or set_a.intersection(set_b)
> print(f"Common: {common}")
> ```

---

## Exercise 7.8: Set Difference
**Task:** Find elements in `set_a = {1, 2, 3, 4}` that are NOT in `set_b = {3, 4, 5}`.

**Expected Output:**
```
Difference: {1, 2}
```

> [!hint]- Hint
> Use `-` operator or `.difference()` method.

> [!success]- Solution
> ```python
> set_a = {1, 2, 3, 4}
> set_b = {3, 4, 5}
> diff = set_a - set_b  # or set_a.difference(set_b)
> print(f"Difference: {diff}")
> ```

---

## Exercise 7.9: Symmetric Difference
**Task:** Find elements that are in either set but NOT in both.

**Given:** `set_a = {1, 2, 3}`, `set_b = {2, 3, 4}`

**Expected Output:**
```
Symmetric Difference: {1, 4}
```

> [!hint]- Hint
> Use `^` operator or `.symmetric_difference()` method.

> [!success]- Solution
> ```python
> set_a = {1, 2, 3}
> set_b = {2, 3, 4}
> sym_diff = set_a ^ set_b
> print(f"Symmetric Difference: {sym_diff}")
> ```

---

## Exercise 7.10: Check Subset
**Task:** Check if `{1, 2}` is a subset of `{1, 2, 3, 4, 5}`.

**Expected Output:**
```
Is subset: True
```

> [!hint]- Hint
> Use `<=` operator or `.issubset()` method.

> [!success]- Solution
> ```python
> small_set = {1, 2}
> large_set = {1, 2, 3, 4, 5}
> is_subset = small_set <= large_set  # or small_set.issubset(large_set)
> print(f"Is subset: {is_subset}")
> ```

---

## Exercise 7.11: Remove Duplicates
**Task:** Remove duplicates from `words = ["apple", "banana", "apple", "cherry", "banana"]` while preserving order.

**Expected Output:**
```
['apple', 'banana', 'cherry']
```

> [!hint]- Hint
> Use `dict.fromkeys()` to preserve order.

> [!success]- Solution
> ```python
> words = ["apple", "banana", "apple", "cherry", "banana"]
> unique = list(dict.fromkeys(words))
> print(unique)
> ```

---

## Exercise 7.12: Set Membership
**Task:** Check if various elements exist in `valid = {"python", "java", "javascript"}`.

**Expected Output:**
```
python: True
ruby: False
```

> [!hint]- Hint
> Use `in` operator for fast membership testing.

> [!success]- Solution
> ```python
> valid = {"python", "java", "javascript"}
> print(f"python: {'python' in valid}")
> print(f"ruby: {'ruby' in valid}")
> ```

---

## Exercise 7.13: Frozen Set
**Task:** Create an immutable set and try to add an element (show it fails).

**Expected Output:**
```
Frozen: frozenset({1, 2, 3})
Cannot modify frozen set!
```

> [!hint]- Hint
> Use `frozenset()` to create an immutable set.

> [!success]- Solution
> ```python
> frozen = frozenset({1, 2, 3})
> print(f"Frozen: {frozen}")
>
> try:
>     frozen.add(4)
> except AttributeError:
>     print("Cannot modify frozen set!")
> ```

---

## Exercise 7.14: Count Unique Characters
**Task:** Count unique characters in `text = "mississippi"`.

**Expected Output:**
```
Unique characters: {'i', 'm', 'p', 's'}
Count: 4
```

> [!hint]- Hint
> Convert string to set.

> [!success]- Solution
> ```python
> text = "mississippi"
> unique = set(text)
> print(f"Unique characters: {unique}")
> print(f"Count: {len(unique)}")
> ```

---

## Exercise 7.15: Tuple vs List Performance
**Task:** Demonstrate that tuples are faster to create than lists by timing both.

**Expected Output:**
```
Tuple creation is generally faster than list creation
```

> [!hint]- Hint
> Use `timeit` module or simple timing.

> [!success]- Solution
> ```python
> import time
>
> # Time tuple creation
> start = time.perf_counter()
> for _ in range(1000000):
>     t = (1, 2, 3, 4, 5)
> tuple_time = time.perf_counter() - start
>
> # Time list creation
> start = time.perf_counter()
> for _ in range(1000000):
>     l = [1, 2, 3, 4, 5]
> list_time = time.perf_counter() - start
>
> print(f"Tuple: {tuple_time:.4f}s")
> print(f"List: {list_time:.4f}s")
> print("Tuple creation is generally faster than list creation")
> ```

---

## 🎯 Level 7 Complete!

**Skills Practiced:**
- Tuple creation and unpacking
- Tuple as immutable sequence
- Set operations (union, intersection, difference)
- Set membership testing
- Removing duplicates
- Frozen sets

**Next Level:** [[08_Level_Dictionaries|Level 8: Dictionaries]]
