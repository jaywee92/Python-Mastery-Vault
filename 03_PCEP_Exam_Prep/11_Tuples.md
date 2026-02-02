---
title: Tuples
tags: [pcep, python, tuples, immutable, sequences]
created: 2026-01-30
exam_section: 3
exam_weight: 5%
---

# 📦 Tuples

[[00_Index|← Back to Index]] | [[10_Lists|← Lists]] | [[12_Dictionaries|Dictionaries →]]

> **"Tuples are immutable lists - know the differences!"**

---

## 🎯 What is a Tuple?

```
┌─────────────────────────────────────────────────────────────────┐
│              TUPLE vs LIST                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  List: [1, 2, 3]   - MUTABLE (can change)                      │
│  Tuple: (1, 2, 3)  - IMMUTABLE (cannot change)                 │
│                                                                  │
│  Use tuples when:                                               │
│  • Data should not change                                       │
│  • Need hashable sequence (dict keys, set elements)            │
│  • Returning multiple values from function                     │
│  • Unpacking values                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Creating Tuples

```python
# ═══════════════════════════════════════════════════════════════
# TUPLE CREATION
# ═══════════════════════════════════════════════════════════════

# Empty tuple
empty = ()
empty2 = tuple()

# Single element tuple - NEEDS COMMA!
single = (42,)    # This is a tuple
not_tuple = (42)  # This is just an int!
print(type(single))     # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>

# Multiple elements
coords = (10, 20)
rgb = (255, 128, 0)
mixed = (1, "hello", 3.14, True)

# Parentheses are optional (tuple packing)
point = 10, 20, 30
print(type(point))  # <class 'tuple'>

# From other iterables
from_list = tuple([1, 2, 3])
from_string = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')
from_range = tuple(range(5))  # (0, 1, 2, 3, 4)

# Nested tuples
nested = ((1, 2), (3, 4), (5, 6))
```

---

## 🔢 Indexing and Slicing

```python
# ═══════════════════════════════════════════════════════════════
# INDEXING (Same as lists and strings!)
# ═══════════════════════════════════════════════════════════════

t = (10, 20, 30, 40, 50)

# Positive indexing
print(t[0])    # 10 (first)
print(t[2])    # 30
print(t[4])    # 50 (last)

# Negative indexing
print(t[-1])   # 50 (last)
print(t[-2])   # 40

# Slicing (returns NEW tuple)
print(t[1:4])   # (20, 30, 40)
print(t[:3])    # (10, 20, 30)
print(t[2:])    # (30, 40, 50)
print(t[::2])   # (10, 30, 50)
print(t[::-1])  # (50, 40, 30, 20, 10) - reversed!

# ═══════════════════════════════════════════════════════════════
# IMMUTABILITY - Cannot modify!
# ═══════════════════════════════════════════════════════════════

t = (1, 2, 3)
# t[0] = 10     # TypeError: tuple does not support item assignment
# t.append(4)   # AttributeError: tuple has no attribute 'append'

# But can reassign variable to new tuple
t = (10, 20, 30)  # This is OK - creates new tuple
```

---

## 🔄 Tuple Unpacking (IMPORTANT!)

```python
# ═══════════════════════════════════════════════════════════════
# TUPLE UNPACKING
# ═══════════════════════════════════════════════════════════════

# Basic unpacking
point = (10, 20)
x, y = point
print(x)  # 10
print(y)  # 20

# Must match number of elements!
coords = (1, 2, 3)
a, b, c = coords      # OK
# a, b = coords       # ValueError: too many values to unpack

# Swap values (Python magic!)
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10

# Extended unpacking with *
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5] - list, not tuple!

*start, last = (1, 2, 3, 4, 5)
print(start)  # [1, 2, 3, 4]
print(last)   # 5

first, *middle, last = (1, 2, 3, 4, 5)
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Ignore values with _
x, _, z = (1, 2, 3)
print(x, z)  # 1 3

# Function returns multiple values (as tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

low, high, total = get_stats([1, 2, 3, 4, 5])
print(low, high, total)  # 1 5 15
```

---

## 🔧 Tuple Methods

```python
# ═══════════════════════════════════════════════════════════════
# TUPLE METHODS (Only 2!)
# ═══════════════════════════════════════════════════════════════

t = (1, 2, 3, 2, 4, 2)

# count() - count occurrences
print(t.count(2))   # 3

# index() - find first occurrence (raises ValueError if not found)
print(t.index(2))   # 1 (first index of 2)
print(t.index(4))   # 4
# print(t.index(99))  # ValueError!

# That's it! No append, remove, sort, etc. (immutable!)
```

---

## 🔗 Tuple Operations

```python
# ═══════════════════════════════════════════════════════════════
# TUPLE OPERATIONS
# ═══════════════════════════════════════════════════════════════

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation (+) - creates NEW tuple
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4, 5, 6)

# Repetition (*)
t4 = t1 * 3
print(t4)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership (in)
print(2 in t1)      # True
print(9 not in t1)  # True

# Length
print(len(t1))  # 3

# Built-in functions
nums = (5, 2, 8, 1, 9)
print(min(nums))     # 1
print(max(nums))     # 9
print(sum(nums))     # 25
print(sorted(nums))  # [1, 2, 5, 8, 9] - returns list!

# Comparison
print((1, 2, 3) == (1, 2, 3))  # True
print((1, 2) < (1, 3))         # True (element by element)
print((1, 2) < (2, 0))         # True (first different element)
```

---

## 📊 Tuples as Dictionary Keys

```python
# ═══════════════════════════════════════════════════════════════
# TUPLES AS DICT KEYS (Lists can't do this!)
# ═══════════════════════════════════════════════════════════════

# Tuples are hashable (immutable), so they can be dict keys
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}

print(locations[(40.7128, -74.0060)])  # New York

# Lists CAN'T be dict keys!
# bad_dict = {[1, 2]: "value"}  # TypeError!

# Tuples can be set elements too
coords_set = {(0, 0), (1, 0), (0, 1)}
print((0, 0) in coords_set)  # True
```

---

## ⚠️ Mutable Objects Inside Tuples

```python
# ═══════════════════════════════════════════════════════════════
# TUPLE WITH MUTABLE ELEMENTS
# ═══════════════════════════════════════════════════════════════

# Tuple can contain mutable objects
t = ([1, 2], [3, 4])

# Can't reassign elements
# t[0] = [5, 6]  # TypeError!

# BUT can modify the mutable object inside!
t[0].append(100)
print(t)  # ([1, 2, 100], [3, 4])

# This is a subtle but important distinction!
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: Single element tuple needs comma
single = (42,)    # Tuple
not_tuple = (42)  # Just an int!
print(type(single))     # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>

# TRAP 2: Parentheses are optional for packing
t = 1, 2, 3       # This is a tuple!
print(type(t))    # <class 'tuple'>

# TRAP 3: Unpacking must match count
t = (1, 2, 3)
# a, b = t        # ValueError!
a, b, c = t       # OK

# TRAP 4: sorted() returns list, not tuple
t = (3, 1, 2)
result = sorted(t)
print(type(result))  # <class 'list'>

# TRAP 5: Extended unpacking gives list
first, *rest = (1, 2, 3)
print(type(rest))  # <class 'list'>

# TRAP 6: Can modify mutable contents
t = ([1, 2], 3)
t[0].append(99)   # OK! Modifies list inside
# t[1] = 4        # Error! Can't reassign element

# TRAP 7: tuple() on string
print(tuple("abc"))  # ('a', 'b', 'c') - characters!

# TRAP 8: Empty tuple vs single element
print(())       # () - empty tuple
print((1))      # 1 - NOT a tuple!
print((1,))     # (1,) - single element tuple
```

---

## 📝 Quick Reference

| Operation | Example | Result |
|-----------|---------|--------|
| Create | `(1, 2, 3)` | Tuple |
| Single element | `(1,)` | Tuple (comma required!) |
| Packing | `t = 1, 2, 3` | Tuple |
| Unpacking | `a, b = (1, 2)` | a=1, b=2 |
| Index | `t[0]`, `t[-1]` | Element |
| Slice | `t[1:3]` | New tuple |
| Concatenate | `t1 + t2` | New tuple |
| Repeat | `t * 3` | New tuple |
| Count | `t.count(x)` | Count of x |
| Index | `t.index(x)` | Position of x |

---

## 🎯 Exam Checklist

- [ ] Tuples are IMMUTABLE
- [ ] Single element tuple needs comma: (1,)
- [ ] Parentheses optional for packing: a, b = 1, 2
- [ ] Unpacking: x, y = (1, 2)
- [ ] Extended unpacking with *: first, *rest = tuple
- [ ] Only 2 methods: count() and index()
- [ ] Can be dict keys (lists can't!)
- [ ] sorted() returns list, not tuple
- [ ] Mutable objects inside can still be modified

---

[[10_Lists|← Lists]] | [[00_Index|Index]] | [[12_Dictionaries|Dictionaries →]]
