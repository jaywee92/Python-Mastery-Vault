# Level 8: Dictionaries
Notebook: [[08_Level_Dictionaries.ipynb]]


> **Difficulty:** ⭐⭐⭐ Intermediate
> **Topics:** Dictionary Creation, Methods, Iteration, Nested Dictionaries
> **Prerequisites:** [[07_Level_Tuples_Sets|Level 7]], [[../../01_Python_Basics/04_Dictionaries_Mastery|Dictionaries Mastery]]

---

## Exercise 8.1: Create Dictionary
**Task:** Create a dictionary with three students and their scores, then print one score.

**Expected Output:**
```
Alice's score: 85
```

> [!hint]- Hint
> Use `{key: value}` syntax.

> [!success]- Solution
> ```python
> students = {"Alice": 85, "Bob": 92, "Charlie": 78}
> print(f"Alice's score: {students['Alice']}")
> ```

---

## Exercise 8.2: Safe Access
**Task:** Access a key that might not exist using `.get()` with a default value.

**Expected Output:**
```
David's score: Not found
```

> [!hint]- Hint
> Use `.get(key, default)` method.

> [!success]- Solution
> ```python
> students = {"Alice": 85, "Bob": 92}
> score = students.get("David", "Not found")
> print(f"David's score: {score}")
> ```

---

## Exercise 8.3: Add and Update
**Task:** Add a new student and update an existing score.

**Expected Output:**
```
{'Alice': 90, 'Bob': 92, 'David': 88}
```

> [!hint]- Hint
> Use `dict[key] = value` for both adding and updating.

> [!success]- Solution
> ```python
> students = {"Alice": 85, "Bob": 92}
> students["David"] = 88    # Add new
> students["Alice"] = 90    # Update existing
> print(students)
> ```

---

## Exercise 8.4: Remove Key
**Task:** Remove "Bob" from the dictionary and print the removed value.

**Expected Output:**
```
Removed: 92
Remaining: {'Alice': 85, 'Charlie': 78}
```

> [!hint]- Hint
> Use `.pop()` method to remove and return the value.

> [!success]- Solution
> ```python
> students = {"Alice": 85, "Bob": 92, "Charlie": 78}
> removed = students.pop("Bob")
> print(f"Removed: {removed}")
> print(f"Remaining: {students}")
> ```

---

## Exercise 8.5: Iterate Keys
**Task:** Print all student names (keys) from the dictionary.

**Expected Output:**
```
Alice
Bob
Charlie
```

> [!hint]- Hint
> Use `for key in dict:` or `dict.keys()`.

> [!success]- Solution
> ```python
> students = {"Alice": 85, "Bob": 92, "Charlie": 78}
> for name in students:
>     print(name)
> ```

---

## Exercise 8.6: Iterate Values
**Task:** Calculate the average of all scores.

**Expected Output:**
```
Average: 85.0
```

> [!hint]- Hint
> Use `.values()` and `sum()/len()`.

> [!success]- Solution
> ```python
> students = {"Alice": 85, "Bob": 92, "Charlie": 78}
> average = sum(students.values()) / len(students)
> print(f"Average: {average}")
> ```

---

## Exercise 8.7: Iterate Items
**Task:** Print each student with their score.

**Expected Output:**
```
Alice: 85
Bob: 92
Charlie: 78
```

> [!hint]- Hint
> Use `.items()` to get key-value pairs.

> [!success]- Solution
> ```python
> students = {"Alice": 85, "Bob": 92, "Charlie": 78}
> for name, score in students.items():
>     print(f"{name}: {score}")
> ```

---

## Exercise 8.8: Check Key Existence
**Task:** Check if "Alice" and "David" exist as keys.

**Expected Output:**
```
Alice exists: True
David exists: False
```

> [!hint]- Hint
> Use `in` operator.

> [!success]- Solution
> ```python
> students = {"Alice": 85, "Bob": 92}
> print(f"Alice exists: {'Alice' in students}")
> print(f"David exists: {'David' in students}")
> ```

---

## Exercise 8.9: Merge Dictionaries
**Task:** Merge two dictionaries using the `|` operator (Python 3.9+).

**Expected Output:**
```
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

> [!hint]- Hint
> Use `dict1 | dict2` or `{**dict1, **dict2}`.

> [!success]- Solution
> ```python
> dict1 = {"a": 1, "b": 2}
> dict2 = {"c": 3, "d": 4}
> merged = dict1 | dict2  # Python 3.9+
> # Alternative: merged = {**dict1, **dict2}
> print(merged)
> ```

---

## Exercise 8.10: Dictionary from Lists
**Task:** Create a dictionary from `keys = ["a", "b", "c"]` and `values = [1, 2, 3]`.

**Expected Output:**
```
{'a': 1, 'b': 2, 'c': 3}
```

> [!hint]- Hint
> Use `zip()` with `dict()`.

> [!success]- Solution
> ```python
> keys = ["a", "b", "c"]
> values = [1, 2, 3]
> result = dict(zip(keys, values))
> print(result)
> ```

---

## Exercise 8.11: Nested Dictionary
**Task:** Create a nested dictionary for students with multiple subjects.

**Expected Output:**
```
Alice's Math: 90
```

> [!hint]- Hint
> Use dictionary inside dictionary.

> [!success]- Solution
> ```python
> students = {
>     "Alice": {"Math": 90, "English": 85},
>     "Bob": {"Math": 78, "English": 92}
> }
> print(f"Alice's Math: {students['Alice']['Math']}")
> ```

---

## Exercise 8.12: Count Occurrences
**Task:** Count character occurrences in `text = "hello"`.

**Expected Output:**
```
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

> [!hint]- Hint
> Use `.get()` with default 0 or `collections.Counter`.

> [!success]- Solution
> ```python
> text = "hello"
> count = {}
> for char in text:
>     count[char] = count.get(char, 0) + 1
> print(count)
>
> # Alternative with Counter:
> # from collections import Counter
> # print(dict(Counter(text)))
> ```

---

## Exercise 8.13: Sort by Value
**Task:** Sort `scores = {"Alice": 85, "Bob": 92, "Charlie": 78}` by score descending.

**Expected Output:**
```
Bob: 92
Alice: 85
Charlie: 78
```

> [!hint]- Hint
> Use `sorted()` with `key` parameter.

> [!success]- Solution
> ```python
> scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
> sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
> for name, score in sorted_scores:
>     print(f"{name}: {score}")
> ```

---

## Exercise 8.14: Default Dictionary
**Task:** Group words by their first letter.

**Given:** `words = ["apple", "banana", "avocado", "blueberry", "cherry"]`

**Expected Output:**
```
{'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

> [!hint]- Hint
> Use `setdefault()` or `collections.defaultdict`.

> [!success]- Solution
> ```python
> words = ["apple", "banana", "avocado", "blueberry", "cherry"]
> grouped = {}
> for word in words:
>     grouped.setdefault(word[0], []).append(word)
> print(grouped)
>
> # Alternative with defaultdict:
> # from collections import defaultdict
> # grouped = defaultdict(list)
> # for word in words:
> #     grouped[word[0]].append(word)
> ```

---

## Exercise 8.15: Invert Dictionary
**Task:** Swap keys and values in `original = {"a": 1, "b": 2, "c": 3}`.

**Expected Output:**
```
{1: 'a', 2: 'b', 3: 'c'}
```

> [!hint]- Hint
> Use dictionary comprehension with `.items()`.

> [!success]- Solution
> ```python
> original = {"a": 1, "b": 2, "c": 3}
> inverted = {v: k for k, v in original.items()}
> print(inverted)
> ```

---

## 🎯 Level 8 Complete!

**Skills Practiced:**
- Dictionary CRUD operations
- Safe access with .get()
- Iterating keys, values, and items
- Merging dictionaries
- Nested dictionaries
- Counting and grouping
- Sorting dictionaries

**Next Level:** [[09_Level_Comprehensions|Level 9: Comprehensions & Lambda]]
