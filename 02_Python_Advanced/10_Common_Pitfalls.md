---
title: Common Pitfalls
tags: [python, pitfalls, common-mistakes, gotchas, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# ⚠️ Common Pitfalls

[[00_Index|← Back to Index]] | [[22_Code_Quality|← Code Quality]] | [[24_Standard_Library|Standard Library →]]

> **"Learn from the mistakes of others - you don't have enough time to make them all yourself!"**

---

## 🎯 The Most Important Python Pitfalls

These pitfalls catch even experienced developers. Know them before they know you!

```
┌─────────────────────────────────────────────────────────────────┐
│                    TOP 10 PYTHON PITFALLS                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Mutable Default Arguments                                    │
│  2. Late Binding in Closures                                     │
│  3. Modifying While Iterating                                    │
│  4. == vs is for None                                            │
│  5. Forgotten return                                             │
│  6. Integer Caching                                              │
│  7. List as Class Attribute                                      │
│  8. Shallow vs Deep Copy                                         │
│  9. Variable Scope in Loops                                      │
│  10. String Immutability                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1️⃣ Mutable Default Arguments

**The CLASSIC problem in Python!**

```python
# ═══════════════════════════════════════════════════════════════
# ❌ WRONG: Mutable as default value
# ═══════════════════════════════════════════════════════════════
def add_item(item, shopping_list=[]):
    shopping_list.append(item)
    return shopping_list

# Expectation vs Reality:
print(add_item("Milk"))    # ['Milk']          ← OK
print(add_item("Bread"))     # ['Milk', 'Bread']  ← SURPRISE!
print(add_item("Eggs"))     # ['Milk', 'Bread', 'Eggs'] ← WTF?!

# The empty list is created ONCE and then reused!

# ═══════════════════════════════════════════════════════════════
# ✅ CORRECT: None as default, create in body
# ═══════════════════════════════════════════════════════════════
def add_item(item, shopping_list=None):
    if shopping_list is None:
        shopping_list = []
    shopping_list.append(item)
    return shopping_list

print(add_item("Milk"))    # ['Milk']
print(add_item("Bread"))     # ['Bread']  ← Now correct!
```

```
⚠️ REMEMBER: NEVER use as default value:
   - []     (list)
   - {}     (dictionary)
   - set()  (set)
   - Any other mutable object

✅ INSTEAD: None as default, create in function body
```

---

## 2️⃣ Late Binding in Closures

```python
# ═══════════════════════════════════════════════════════════════
# ❌ WRONG: Closures bind late!
# ═══════════════════════════════════════════════════════════════
def create_multipliers():
    multipliers = []
    for i in range(5):
        multipliers.append(lambda x: x * i)
    return multipliers

mults = create_multipliers()
print(mults[0](10))  # Expectation: 0  → Reality: 40
print(mults[1](10))  # Expectation: 10 → Reality: 40
print(mults[2](10))  # Expectation: 20 → Reality: 40
# All return 40! i is 4 at the end

# ═══════════════════════════════════════════════════════════════
# ✅ SOLUTION 1: Default argument binds immediately
# ═══════════════════════════════════════════════════════════════
def create_multipliers():
    multipliers = []
    for i in range(5):
        multipliers.append(lambda x, i=i: x * i)  # i=i binds immediately!
    return multipliers

mults = create_multipliers()
print(mults[0](10))  # 0  ✓
print(mults[1](10))  # 10 ✓
print(mults[2](10))  # 20 ✓

# ═══════════════════════════════════════════════════════════════
# ✅ SOLUTION 2: functools.partial
# ═══════════════════════════════════════════════════════════════
from functools import partial

def multiply(i, x):
    return x * i

def create_multipliers():
    return [partial(multiply, i) for i in range(5)]
```

```
┌─────────────────────────────────────────────────────────────────┐
│                    LATE BINDING EXPLAINED                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   for i in range(5):                                            │
│       funcs.append(lambda: i)                                   │
│                                                                  │
│   i = 0 → lambda: i  (references i, not value 0)               │
│   i = 1 → lambda: i  (references i, not value 1)               │
│   i = 2 → lambda: i  ...                                        │
│   i = 3 → lambda: i  ...                                        │
│   i = 4 → lambda: i  (i is 4 at the end)                        │
│                                                                  │
│   All lambdas see the CURRENT value of i (4)                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3️⃣ Modifying While Iterating

```python
# ═══════════════════════════════════════════════════════════════
# ❌ WRONG: Modify list during iteration
# ═══════════════════════════════════════════════════════════════
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # DANGEROUS!

print(numbers)  # [1, 3, 5, 7, 9]? NO! → [1, 3, 5, 7, 9] (luck) or error

# The problem: The iterator loses its position!

# ═══════════════════════════════════════════════════════════════
# ✅ SOLUTION 1: List comprehension (new list)
# ═══════════════════════════════════════════════════════════════
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [n for n in numbers if n % 2 != 0]
print(numbers)  # [1, 3, 5, 7, 9] ✓

# ═══════════════════════════════════════════════════════════════
# ✅ SOLUTION 2: Iterate over copy
# ═══════════════════════════════════════════════════════════════
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers[:]:  # [:] creates copy
    if num % 2 == 0:
        numbers.remove(num)

# ═══════════════════════════════════════════════════════════════
# ✅ SOLUTION 3: Iterate backwards (for index-based)
# ═══════════════════════════════════════════════════════════════
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        del numbers[i]

# Same applies to dictionaries!
# ❌
for key in my_dict:
    del my_dict[key]  # RuntimeError!

# ✅
for key in list(my_dict.keys()):
    del my_dict[key]  # OK
```

---

## 4️⃣ == vs is for None

```python
# ═══════════════════════════════════════════════════════════════
# ❌ WRONG: == for None comparison
# ═══════════════════════════════════════════════════════════════
value = None

if value == None:  # Works, but poor style
    print("Is None")

# The problem: == can be overridden!
class Tricky:
    def __eq__(self, other):
        return True  # Always True!

t = Tricky()
print(t == None)  # True, even though t is not None!

# ═══════════════════════════════════════════════════════════════
# ✅ CORRECT: is for None
# ═══════════════════════════════════════════════════════════════
value = None

if value is None:  # Checks identity, not equality
    print("Is None")

if value is not None:  # Not "if not value is None"
    print("Has value")

# is checks: Are they the SAME object?
# == checks: Are the VALUES equal?
```

```
┌─────────────────────────────────────────────────────────────────┐
│                     is vs == OVERVIEW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  is       → Identity (same object in memory)                    │
│  ==       → Equality (values are equal)                         │
│                                                                  │
│  Use is for:                                                    │
│  - None                                                          │
│  - True/False (explicitly)                                      │
│  - Singleton objects                                             │
│                                                                  │
│  Use == for:                                                    │
│  - Numbers, strings, lists (value comparison)                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5️⃣ Forgotten return

```python
# ═══════════════════════════════════════════════════════════════
# ❌ WRONG: return forgotten
# ═══════════════════════════════════════════════════════════════
def add(a, b):
    result = a + b
    # No return! Returns None implicitly

x = add(2, 3)
print(x)  # None (not 5!)

# ═══════════════════════════════════════════════════════════════
# ✅ CORRECT: Explicit return
# ═══════════════════════════════════════════════════════════════
def add(a, b):
    return a + b

# Especially tricky with conditional returns:
# ❌ WRONG
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    # What happens with score < 80? → None!

# ✅ CORRECT
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"  # Always a return!
```

---

## 6️⃣ Integer Caching

```python
# Python caches small integers (-5 to 256)

a = 256
b = 256
print(a is b)  # True - same cached integer

a = 257
b = 257
print(a is b)  # False - different objects!

# This is NOT a bug, but shows why "is" is wrong for number comparison

# ═══════════════════════════════════════════════════════════════
# ❌ WRONG: is for number comparison
# ═══════════════════════════════════════════════════════════════
def check_value(x):
    if x is 100:  # WARNING: Can fail!
        return True

# ═══════════════════════════════════════════════════════════════
# ✅ CORRECT: == for number comparison
# ═══════════════════════════════════════════════════════════════
def check_value(x):
    if x == 100:  # Always correct
        return True
```

---

## 7️⃣ List as Class Attribute

```python
# ═══════════════════════════════════════════════════════════════
# ❌ WRONG: Mutable class attribute
# ═══════════════════════════════════════════════════════════════
class Student:
    grades = []  # Class attribute - shared between ALL instances!

    def __init__(self, name):
        self.name = name

alice = Student("Alice")
bob = Student("Bob")

alice.grades.append(95)
print(bob.grades)  # [95] - Bob has Alice's grade?!

# ═══════════════════════════════════════════════════════════════
# ✅ CORRECT: Instance attribute in __init__
# ═══════════════════════════════════════════════════════════════
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # Each instance gets its own list

alice = Student("Alice")
bob = Student("Bob")

alice.grades.append(95)
print(bob.grades)  # [] - Correct!
```

---

## 8️⃣ Shallow vs Deep Copy

```python
import copy

# ═══════════════════════════════════════════════════════════════
# The problem: Nested structures
# ═══════════════════════════════════════════════════════════════
original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy - copies only outer list
shallow = original.copy()  # or list(original) or original[:]
shallow[0][0] = 999

print(original)  # [[999, 2, 3], [4, 5, 6]] - ALSO changed!

# ═══════════════════════════════════════════════════════════════
# ✅ Deep copy - copies everything recursively
# ═══════════════════════════════════════════════════════════════
original = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(original)
deep[0][0] = 999

print(original)  # [[1, 2, 3], [4, 5, 6]] - Unchanged!
```

```
┌─────────────────────────────────────────────────────────────────┐
│               SHALLOW VS DEEP COPY                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ORIGINAL         SHALLOW COPY       DEEP COPY                  │
│  ┌─────┐          ┌─────┐            ┌─────┐                    │
│  │ [1] │────┐     │ [1] │────┐       │ [1] │                    │
│  │ [2] │    │     │ [2] │    │       │ [2] │                    │
│  └─────┘    │     └─────┘    │       └─────┘                    │
│             ▼                ▼             ▼                     │
│         ┌───────┐       ┌───────┐    ┌───────┐                  │
│         │ a b c │       │ a b c │    │ a b c │                  │
│         └───────┘       └───────┘    └───────┘                  │
│              ↑               ↑            (Copy)                │
│              └───────────────┘                                  │
│               SAME inner list!                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9️⃣ Variable Scope in Loops

```python
# ═══════════════════════════════════════════════════════════════
# Python: Loop variables "leak" out of the loop!
# ═══════════════════════════════════════════════════════════════
for i in range(5):
    pass

print(i)  # 4 - i still exists!

# ═══════════════════════════════════════════════════════════════
# Even more problematic in list comprehensions (Python 2)
# Fixed in Python 3!
# ═══════════════════════════════════════════════════════════════

# Python 3: List comprehension has its own scope
x = 10
result = [x for x in range(5)]
print(x)  # 10 - x is still 10 ✓

# But normal loops don't:
x = 10
for x in range(5):
    pass
print(x)  # 4 - x was overwritten!

# ═══════════════════════════════════════════════════════════════
# ✅ SOLUTION: Use different variable names
# ═══════════════════════════════════════════════════════════════
important_value = 10
for index in range(5):  # Not "i" if important
    pass
print(important_value)  # 10 - safe
```

---

## 🔟 String Immutability

```python
# ═══════════════════════════════════════════════════════════════
# ❌ WRONG: Concatenate string in loop
# ═══════════════════════════════════════════════════════════════
result = ""
for i in range(10000):
    result += str(i)  # Creates NEW string EVERY time!

# This is O(n²) - extremely slow!

# ═══════════════════════════════════════════════════════════════
# ✅ CORRECT: List + join
# ═══════════════════════════════════════════════════════════════
parts = []
for i in range(10000):
    parts.append(str(i))
result = "".join(parts)  # O(n) - much faster!

# Or directly:
result = "".join(str(i) for i in range(10000))
```

---

## 🎁 Bonus Pitfalls

### Chained Comparison Confusion

```python
# Python allows: a < b < c
# But be careful:

x = 5
print(1 < x < 10)  # True ✓
print(1 < x > 3)   # True (1 < 5 AND 5 > 3)

# Confusing:
print(5 == 5 == True)  # False! (5 == 5) is True, but (5 == True) is False
```

### except without type

```python
# ❌ WRONG: Catch all exceptions
try:
    do_something()
except:  # Catches EVERYTHING, including KeyboardInterrupt!
    pass

# ✅ CORRECT: Specific exceptions
try:
    do_something()
except ValueError as e:
    handle_error(e)
except Exception as e:  # Only if really needed
    log_error(e)
    raise  # Re-raise!
```

### Default dict without factory

```python
from collections import defaultdict

# ❌ WRONG: defaultdict used incorrectly
d = defaultdict(0)  # TypeError! 0 is not a function

# ✅ CORRECT: Factory function
d = defaultdict(int)  # int() returns 0
d = defaultdict(list)  # list() returns []
d = defaultdict(lambda: "default")  # Lambda for custom default
```

---

## ✅ Summary

| Pitfall | Problem | Solution |
|---------|---------|--------|
| Mutable Default | List is shared | `=None` in signature |
| Late Binding | All lambdas same | `i=i` as default arg |
| Modify While Iterate | Elements skipped | List comprehension/copy |
| == for None | Can be overridden | Use `is None` |
| Forgotten return | Function returns None | Always explicit return |
| Integer Caching | is fails | == for numbers |
| Class Attribute List | All instances share | Create in __init__ |
| Shallow Copy | Nested objects shared | Use deepcopy() |
| Loop Variable Leak | Variable persists | Use unique names |
| String += in loop | O(n²) performance | Use join() |

---

## 🎯 Exam Checklist

- [ ] Mutable Default Arguments: `=None` pattern
- [ ] Late Binding in Closures: `i=i` fix
- [ ] Modifying While Iterating: copy or comprehension
- [ ] `is None` instead of `== None`
- [ ] Always explicit `return`
- [ ] Class attributes vs instance attributes
- [ ] `copy.deepcopy()` for nested structures
- [ ] `"".join()` instead of `+=` for strings

---

[[22_Code_Quality|← Code Quality]] | [[00_Index|Index]] | [[24_Standard_Library|Standard Library →]]
