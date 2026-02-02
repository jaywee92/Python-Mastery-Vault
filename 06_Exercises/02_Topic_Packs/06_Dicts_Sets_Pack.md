# Dictionaries & Sets Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** Counting and membership

Notebook: [[06_Dicts_Sets_Pack.ipynb]]

---

## D1: Word Frequency
**Task:** Count word frequency in a sentence.

```python
text = "to be or not to be"
# expected: {"to": 2, "be": 2, "or": 1, "not": 1}
```

> [!hint]- 💡 Hint 1 (Low)
> Split into words, then count.

> [!hint]- 💡 Hint 2 (Mid)
> Use `dict.get(word, 0)`.

> [!hint]- 💡 Hint 3 (High)
> `counts[word] = counts.get(word, 0) + 1`

> [!success]- ✅ Solution
> ```python
> def word_count(text):
>     counts = {}
>     for word in text.split():
>         counts[word] = counts.get(word, 0) + 1
>     return counts
> 
> print(word_count("to be or not to be"))
> ```

---

---

## D2: Unique Items
**Task:** Return the unique values from a list.

```python
nums = [1, 2, 2, 3, 3]
# expected: {1, 2, 3}
```

> [!hint]- 💡 Hint 1 (Low)
> A set stores unique items.

> [!hint]- 💡 Hint 2 (Mid)
> Use `set(nums)`.

> [!hint]- 💡 Hint 3 (High)
> Return a set, not a list.

> [!success]- ✅ Solution
> ```python
> def unique_values(nums):
>     return set(nums)
> 
> print(unique_values([1, 2, 2, 3, 3]))  # {1, 2, 3}
> ```

---

---

## D3: Phonebook Lookup
**Task:** Build a phonebook and lookup a name.

```python
contacts = {"Ana": "123", "Ben": "456"}
# lookup "Ben" -> "456"
```

> [!hint]- 💡 Hint 1 (Low)
> Use dictionary indexing.

> [!hint]- 💡 Hint 2 (Mid)
> Use `.get(name, "not found")`.

> [!hint]- 💡 Hint 3 (High)
> Return "not found" if missing.

> [!success]- ✅ Solution
> ```python
> def lookup(phonebook, name):
>     return phonebook.get(name, "not found")
> 
> book = {"Ana": "123", "Ben": "456"}
> print(lookup(book, "Ben"))  # 456
> print(lookup(book, "Cara")) # not found
> ```

---

---

## D4: Common Items
**Task:** Return common items between two lists.

```python
a = [1, 2, 3]
b = [2, 3, 4]
# expected: {2, 3}
```

> [!hint]- 💡 Hint 1 (Low)
> Convert both to sets.

> [!hint]- 💡 Hint 2 (Mid)
> Use set intersection.

> [!hint]- 💡 Hint 3 (High)
> `set(a) & set(b)`

> [!success]- ✅ Solution
> ```python
> def common(a, b):
>     return set(a) & set(b)
> 
> print(common([1, 2, 3], [2, 3, 4]))  # {2, 3}
> ```

---

---

## D5: Merge Dictionaries
**Task:** Merge two dictionaries (second overwrites first).

```python
a = {"x": 1, "y": 2}
b = {"y": 9, "z": 3}
# expected: {"x": 1, "y": 9, "z": 3}
```

> [!hint]- 💡 Hint 1 (Low)
> Python can merge with `{**a, **b}`.

> [!hint]- 💡 Hint 2 (Mid)
> Values in `b` overwrite values in `a`.

> [!hint]- 💡 Hint 3 (High)
> Use `result = {**a, **b}`.

> [!success]- ✅ Solution
> ```python
> def merge_dicts(a, b):
>     return {**a, **b}
> 
> print(merge_dicts({"x": 1, "y": 2}, {"y": 9, "z": 3}))
> # {'x': 1, 'y': 9, 'z': 3}
> ```

---

## D1: Count Words
**Task:** Solve the task below.

```python
text='a a b'
# expected: {'a':2,'b':1}
```

> [!hint]- 💡 Hint 1 (Low)
> Use dictionaries or sets.

> [!hint]- 💡 Hint 2 (Mid)
> Use .get() or set operators.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> text='a a b'
> counts = {}
> for w in text.split():
>     counts[w] = counts.get(w,0)+1
> print(counts)
> ```

---

---

## D3: Get with Default
**Task:** Solve the task below.

```python
d={'a':1}
# expected: 0
```

> [!hint]- 💡 Hint 1 (Low)
> Use dictionaries or sets.

> [!hint]- 💡 Hint 2 (Mid)
> Use .get() or set operators.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> d={'a':1}
> print(d.get('b',0))
> ```

---

---

## D4: Merge Dicts
**Task:** Solve the task below.

```python
a={'x':1}
b={'x':2,'y':3}
# expected: {'x':2,'y':3}
```

> [!hint]- 💡 Hint 1 (Low)
> Use dictionaries or sets.

> [!hint]- 💡 Hint 2 (Mid)
> Use .get() or set operators.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> a={'x':1}
> b={'x':2,'y':3}
> print({**a, **b})
> ```

---

---

## D5: Keys List
**Task:** Solve the task below.

```python
d={'a':1,'b':2}
# expected: ['a','b']
```

> [!hint]- 💡 Hint 1 (Low)
> Use dictionaries or sets.

> [!hint]- 💡 Hint 2 (Mid)
> Use .get() or set operators.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> d={'a':1,'b':2}
> print(list(d.keys()))
> ```

---

---

## D6: Values List
**Task:** Solve the task below.

```python
d={'a':1,'b':2}
# expected: [1,2]
```

> [!hint]- 💡 Hint 1 (Low)
> Use dictionaries or sets.

> [!hint]- 💡 Hint 2 (Mid)
> Use .get() or set operators.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> d={'a':1,'b':2}
> print(list(d.values()))
> ```

---

---

## D7: Invert Dict
**Task:** Solve the task below.

```python
d={'a':1,'b':2}
# expected: {1:'a',2:'b'}
```

> [!hint]- 💡 Hint 1 (Low)
> Use dictionaries or sets.

> [!hint]- 💡 Hint 2 (Mid)
> Use .get() or set operators.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> d={'a':1,'b':2}
> inv = {v:k for k,v in d.items()}
> print(inv)
> ```

---

---

## D8: Set Intersection
**Task:** Solve the task below.

```python
a={1,2,3}
b={2,3,4}
# expected: {2,3}
```

> [!hint]- 💡 Hint 1 (Low)
> Use dictionaries or sets.

> [!hint]- 💡 Hint 2 (Mid)
> Use .get() or set operators.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> a={1,2,3}
> b={2,3,4}
> print(a & b)
> ```

---

---

## D9: Set Union
**Task:** Solve the task below.

```python
a={1,2}
b={2,3}
# expected: {1,2,3}
```

> [!hint]- 💡 Hint 1 (Low)
> Use dictionaries or sets.

> [!hint]- 💡 Hint 2 (Mid)
> Use .get() or set operators.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> a={1,2}
> b={2,3}
> print(a | b)
> ```

---

---

## D10: Membership
**Task:** Solve the task below.

```python
d={'x':1}
# expected: True
```

> [!hint]- 💡 Hint 1 (Low)
> Use dictionaries or sets.

> [!hint]- 💡 Hint 2 (Mid)
> Use .get() or set operators.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> d={'x':1}
> print('x' in d)
> ```

---

---
