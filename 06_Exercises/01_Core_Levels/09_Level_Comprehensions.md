# Level 9: Comprehensions & Lambda
Notebook: [[09_Level_Comprehensions.ipynb]]


> **Difficulty:** ⭐⭐⭐⭐ Advanced
> **Topics:** List/Dict/Set Comprehensions, Lambda Functions, map, filter, reduce
> **Prerequisites:** [[08_Level_Dictionaries|Level 8]], [[../../01_Python_Basics/07_Comprehensions|Comprehensions]], [[../../01_Python_Basics/09_Lambda_and_Built-ins|Lambda]]

---

## Exercise 9.1: Basic List Comprehension
**Task:** Create a list of squares from 1 to 10.

**Expected Output:**
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

> [!hint]- Hint
> Syntax: `[expression for item in iterable]`

> [!success]- Solution
> ```python
> squares = [x**2 for x in range(1, 11)]
> print(squares)
> ```

---

## Exercise 9.2: Conditional Comprehension
**Task:** Create a list of even numbers from 1 to 20.

**Expected Output:**
```
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

> [!hint]- Hint
> Add `if` condition: `[x for x in range if condition]`

> [!success]- Solution
> ```python
> evens = [x for x in range(1, 21) if x % 2 == 0]
> print(evens)
> ```

---

## Exercise 9.3: Transform with Condition
**Task:** From a list, keep only strings and convert them to uppercase.

**Given:** `mixed = [1, "hello", 2.5, "world", True, "python"]`

**Expected Output:**
```
['HELLO', 'WORLD', 'PYTHON']
```

> [!hint]- Hint
> Use `isinstance(x, str)` to filter strings.

> [!success]- Solution
> ```python
> mixed = [1, "hello", 2.5, "world", True, "python"]
> strings = [s.upper() for s in mixed if isinstance(s, str)]
> print(strings)
> ```

---

## Exercise 9.4: Nested List Comprehension
**Task:** Flatten a 2D matrix into a 1D list.

**Given:** `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

**Expected Output:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> [!hint]- Hint
> Use nested loops: `[item for row in matrix for item in row]`

> [!success]- Solution
> ```python
> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
> flat = [num for row in matrix for num in row]
> print(flat)
> ```

---

## Exercise 9.5: Dictionary Comprehension
**Task:** Create a dictionary mapping numbers 1-5 to their cubes.

**Expected Output:**
```
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```

> [!hint]- Hint
> Syntax: `{key: value for item in iterable}`

> [!success]- Solution
> ```python
> cubes = {x: x**3 for x in range(1, 6)}
> print(cubes)
> ```

---

## Exercise 9.6: Filter Dictionary
**Task:** Keep only items where value > 80.

**Given:** `scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65}`

**Expected Output:**
```
{'Alice': 85, 'Charlie': 90}
```

> [!hint]- Hint
> Use `.items()` with condition in comprehension.

> [!success]- Solution
> ```python
> scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65}
> passed = {k: v for k, v in scores.items() if v > 80}
> print(passed)
> ```

---

## Exercise 9.7: Set Comprehension
**Task:** Get unique first letters from a list of words.

**Given:** `words = ["apple", "banana", "avocado", "cherry", "apricot"]`

**Expected Output:**
```
{'a', 'b', 'c'}
```

> [!hint]- Hint
> Use `{expression for item in iterable}`.

> [!success]- Solution
> ```python
> words = ["apple", "banana", "avocado", "cherry", "apricot"]
> first_letters = {word[0] for word in words}
> print(first_letters)
> ```

---

## Exercise 9.8: Basic Lambda
**Task:** Create a lambda function to calculate the area of a rectangle.

**Expected Output:**
```
Area: 35
```

> [!hint]- Hint
> Syntax: `lambda param1, param2: expression`

> [!success]- Solution
> ```python
> area = lambda length, width: length * width
> print(f"Area: {area(5, 7)}")
> ```

---

## Exercise 9.9: Lambda with Sort
**Task:** Sort a list of tuples by the second element.

**Given:** `pairs = [(1, 'b'), (2, 'a'), (3, 'c')]`

**Expected Output:**
```
[(2, 'a'), (1, 'b'), (3, 'c')]
```

> [!hint]- Hint
> Use `sorted()` with `key=lambda x: x[1]`.

> [!success]- Solution
> ```python
> pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
> sorted_pairs = sorted(pairs, key=lambda x: x[1])
> print(sorted_pairs)
> ```

---

## Exercise 9.10: Map Function
**Task:** Double all numbers in a list using `map()`.

**Given:** `numbers = [1, 2, 3, 4, 5]`

**Expected Output:**
```
[2, 4, 6, 8, 10]
```

> [!hint]- Hint
> `map(function, iterable)` returns a map object.

> [!success]- Solution
> ```python
> numbers = [1, 2, 3, 4, 5]
> doubled = list(map(lambda x: x * 2, numbers))
> print(doubled)
> ```

---

## Exercise 9.11: Filter Function
**Task:** Filter out negative numbers using `filter()`.

**Given:** `numbers = [-2, -1, 0, 1, 2, 3]`

**Expected Output:**
```
[0, 1, 2, 3]
```

> [!hint]- Hint
> `filter(function, iterable)` keeps items where function returns True.

> [!success]- Solution
> ```python
> numbers = [-2, -1, 0, 1, 2, 3]
> non_negative = list(filter(lambda x: x >= 0, numbers))
> print(non_negative)
> ```

---

## Exercise 9.12: Reduce Function
**Task:** Calculate the product of all numbers using `reduce()`.

**Given:** `numbers = [1, 2, 3, 4, 5]`

**Expected Output:**
```
Product: 120
```

> [!hint]- Hint
> Import `reduce` from `functools`.

> [!success]- Solution
> ```python
> from functools import reduce
>
> numbers = [1, 2, 3, 4, 5]
> product = reduce(lambda x, y: x * y, numbers)
> print(f"Product: {product}")
> ```

---

## Exercise 9.13: Chained Operations
**Task:** Using a list of numbers, filter evens, square them, then sum the result.

**Given:** `numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

**Expected Output:**
```
Sum of squared evens: 220
```

> [!hint]- Hint
> Chain comprehension: filter first, then square in one expression.

> [!success]- Solution
> ```python
> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
> result = sum(x**2 for x in numbers if x % 2 == 0)
> print(f"Sum of squared evens: {result}")
> ```

---

## Exercise 9.14: Conditional Expression in Comprehension
**Task:** Create a list that replaces negative numbers with 0.

**Given:** `numbers = [-5, 3, -1, 7, -2, 8]`

**Expected Output:**
```
[0, 3, 0, 7, 0, 8]
```

> [!hint]- Hint
> Use ternary: `[a if condition else b for x in list]`

> [!success]- Solution
> ```python
> numbers = [-5, 3, -1, 7, -2, 8]
> result = [x if x >= 0 else 0 for x in numbers]
> print(result)
> ```

---

## Exercise 9.15: Complex Transformation
**Task:** Create a dictionary from two lists, filtering and transforming.

**Given:**
- `names = ["Alice", "Bob", "Charlie", "David"]`
- `scores = [85, 72, 90, 65]`
- Only include if score >= 75, value should be "Pass" or "Excellent"

**Expected Output:**
```
{'Alice': 'Pass', 'Charlie': 'Excellent'}
```

> [!hint]- Hint
> Combine zip(), filtering, and conditional expression.

> [!success]- Solution
> ```python
> names = ["Alice", "Bob", "Charlie", "David"]
> scores = [85, 72, 90, 65]
>
> result = {
>     name: ("Excellent" if score >= 90 else "Pass")
>     for name, score in zip(names, scores)
>     if score >= 75
> }
> print(result)
> ```

---

## 🎯 Level 9 Complete!

**Skills Practiced:**
- List comprehensions with conditions
- Dictionary and set comprehensions
- Nested comprehensions
- Lambda functions
- map(), filter(), reduce()
- Chaining operations
- Complex transformations

**Next Level:** [[10_Level_OOP_Exceptions|Level 10: OOP & Exceptions]]
