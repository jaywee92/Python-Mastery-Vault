---
title: Lists (MOST IMPORTANT!)
tags: [pcep, python, lists, mutable, sequences]
created: 2026-01-30
exam_section: 3
exam_weight: 12%
---

# 📋 Lists - THE MOST TESTED TOPIC!

[[00_Index|← Back to Index]] | [[09_Strings|← Strings]] | [[11_Tuples|Tuples →]]

> **"Lists are tested MORE than anything else - master them!"**

---

## ⚠️ EXAM ALERT: Lists appear in almost EVERY exam!

---

## 🎯 List Basics

```python
# ═══════════════════════════════════════════════════════════════
# LIST CREATION
# ═══════════════════════════════════════════════════════════════

# Empty list (two ways)
empty1 = []
empty2 = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Can mix types!
nested = [[1, 2], [3, 4], [5, 6]]  # List of lists

# List from other iterables
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(5))  # [0, 1, 2, 3, 4]

# Lists are MUTABLE (can be changed)!
nums = [1, 2, 3]
nums[0] = 10  # OK! [10, 2, 3]
```

---

## 🔢 Indexing (Same as Strings!)

```
┌─────────────────────────────────────────────────────────────────┐
│                    LIST INDEXING                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  List:      [10,  20,  30,  40,  50]                            │
│              ↓    ↓    ↓    ↓    ↓                              │
│  Index:      0    1    2    3    4                              │
│  Negative:  -5   -4   -3   -2   -1                              │
│                                                                  │
│  nums = [10, 20, 30, 40, 50]                                    │
│  nums[0]  → 10    (first)                                       │
│  nums[-1] → 50    (last)                                        │
│  nums[2]  → 30                                                  │
│  nums[5]  → IndexError!                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
nums = [10, 20, 30, 40, 50]

# Positive indexing
print(nums[0])    # 10 (first element)
print(nums[2])    # 30
print(nums[4])    # 50 (last element)

# Negative indexing
print(nums[-1])   # 50 (last element)
print(nums[-2])   # 40
print(nums[-5])   # 10 (first element)

# Modifying elements (lists are mutable!)
nums[0] = 100
print(nums)       # [100, 20, 30, 40, 50]
```

---

## ✂️ Slicing (MUST KNOW!)

```
┌─────────────────────────────────────────────────────────────────┐
│              SLICING SYNTAX: list[start:stop:step]              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  nums = [0, 1, 2, 3, 4, 5]                                      │
│                                                                  │
│  nums[1:4]   → [1, 2, 3]    (index 1, 2, 3 - NOT 4!)           │
│  nums[:3]    → [0, 1, 2]    (from start)                       │
│  nums[3:]    → [3, 4, 5]    (to end)                           │
│  nums[:]     → [0, 1, 2, 3, 4, 5]  (COPY!)                     │
│  nums[::2]   → [0, 2, 4]    (every 2nd)                        │
│  nums[::-1]  → [5, 4, 3, 2, 1, 0]  (REVERSE!)                  │
│                                                                  │
│  IMPORTANT: Slicing returns a NEW list!                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
nums = [0, 1, 2, 3, 4, 5]

# Basic slicing
print(nums[1:4])    # [1, 2, 3]
print(nums[:3])     # [0, 1, 2]
print(nums[3:])     # [3, 4, 5]
print(nums[:])      # [0, 1, 2, 3, 4, 5] (copy!)

# With step
print(nums[::2])    # [0, 2, 4]
print(nums[1::2])   # [1, 3, 5]

# REVERSE (common exam question!)
print(nums[::-1])   # [5, 4, 3, 2, 1, 0]

# Slice assignment (modifies list!)
nums[1:3] = [10, 20, 30]  # Replace with different length!
print(nums)  # [0, 10, 20, 30, 3, 4, 5]

# Delete with slicing
nums[1:4] = []
print(nums)  # [0, 3, 4, 5]
```

---

## 🔧 List Methods (MEMORIZE ALL!)

### Adding Elements

```python
# ═══════════════════════════════════════════════════════════════
# ADDING ELEMENTS
# ═══════════════════════════════════════════════════════════════

nums = [1, 2, 3]

# append() - add ONE element to end
nums.append(4)
print(nums)  # [1, 2, 3, 4]
nums.append([5, 6])  # Adds list AS one element!
print(nums)  # [1, 2, 3, 4, [5, 6]]

# extend() - add MULTIPLE elements (flattens iterable)
nums = [1, 2, 3]
nums.extend([4, 5, 6])
print(nums)  # [1, 2, 3, 4, 5, 6]
nums.extend("hi")  # Extends with each character!
print(nums)  # [1, 2, 3, 4, 5, 6, 'h', 'i']

# insert() - add at specific position
nums = [1, 2, 3]
nums.insert(0, 100)   # Insert at beginning
print(nums)  # [100, 1, 2, 3]
nums.insert(2, 200)   # Insert at index 2
print(nums)  # [100, 1, 200, 2, 3]
nums.insert(100, 999) # Beyond end → appends
print(nums)  # [100, 1, 200, 2, 3, 999]

# Concatenation (+) - creates NEW list
a = [1, 2]
b = [3, 4]
c = a + b
print(c)  # [1, 2, 3, 4]
print(a)  # [1, 2] (unchanged!)
```

### Removing Elements

```python
# ═══════════════════════════════════════════════════════════════
# REMOVING ELEMENTS
# ═══════════════════════════════════════════════════════════════

nums = [1, 2, 3, 2, 4, 2]

# remove() - removes FIRST occurrence by VALUE
nums.remove(2)
print(nums)  # [1, 3, 2, 4, 2]
# nums.remove(99)  # ValueError! Not in list

# pop() - removes by INDEX and RETURNS value
nums = [1, 2, 3, 4, 5]
last = nums.pop()      # Remove last (no argument)
print(last)  # 5
print(nums)  # [1, 2, 3, 4]

first = nums.pop(0)    # Remove at index 0
print(first)  # 1
print(nums)   # [2, 3, 4]

# pop() vs remove() - EXAM FAVORITE!
# pop(index) - by position, returns removed value
# remove(value) - by value, returns None

# del statement - removes by index or slice
nums = [1, 2, 3, 4, 5]
del nums[0]      # Delete first
print(nums)      # [2, 3, 4, 5]
del nums[1:3]    # Delete slice
print(nums)      # [2, 5]
del nums[:]      # Delete all (same as clear)

# clear() - remove all elements
nums = [1, 2, 3]
nums.clear()
print(nums)  # []
```

### Searching and Counting

```python
# ═══════════════════════════════════════════════════════════════
# SEARCHING AND COUNTING
# ═══════════════════════════════════════════════════════════════

nums = [1, 2, 3, 2, 4, 2]

# index() - find FIRST occurrence (raises ValueError if not found!)
print(nums.index(2))      # 1 (first occurrence)
print(nums.index(2, 2))   # 3 (search from index 2)
# print(nums.index(99))   # ValueError!

# count() - count occurrences
print(nums.count(2))   # 3
print(nums.count(99))  # 0 (no error!)

# in / not in - membership test (COMMON!)
print(2 in nums)       # True
print(99 in nums)      # False
print(99 not in nums)  # True
```

### Sorting and Reversing

```python
# ═══════════════════════════════════════════════════════════════
# SORTING AND REVERSING
# ═══════════════════════════════════════════════════════════════

nums = [3, 1, 4, 1, 5, 9, 2]

# sort() - sorts IN PLACE, returns None!
result = nums.sort()
print(result)  # None (!) - common trap!
print(nums)    # [1, 1, 2, 3, 4, 5, 9]

# sort() with reverse
nums.sort(reverse=True)
print(nums)    # [9, 5, 4, 3, 2, 1, 1]

# sorted() - returns NEW sorted list
nums = [3, 1, 4, 1, 5]
new_list = sorted(nums)
print(new_list)  # [1, 1, 3, 4, 5]
print(nums)      # [3, 1, 4, 1, 5] (unchanged!)

# reverse() - reverses IN PLACE
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)    # [5, 4, 3, 2, 1]

# reversed() - returns iterator
nums = [1, 2, 3]
rev = list(reversed(nums))
print(rev)     # [3, 2, 1]

# Slicing reverse (returns new list)
print(nums[::-1])  # [3, 2, 1]
```

---

## 📋 List Comprehensions (EXAM TOPIC!)

```python
# ═══════════════════════════════════════════════════════════════
# LIST COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════

# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition: [expr for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]
print(evens)    # [0, 2, 4, 6, 8]

# Transform strings
words = ["hello", "world"]
upper = [w.upper() for w in words]
print(upper)    # ['HELLO', 'WORLD']

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)   # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flatten a list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in nested for x in row]
print(flat)     # [1, 2, 3, 4, 5, 6]
```

---

## 🔄 Copying Lists (TRICKY!)

```
┌─────────────────────────────────────────────────────────────────┐
│              LIST COPYING - EXAM TRAP!                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ASSIGNMENT (=) creates a REFERENCE, not a copy!                │
│                                                                  │
│  a = [1, 2, 3]                                                  │
│  b = a           ← b points to SAME list!                       │
│  b[0] = 100                                                     │
│  print(a)        → [100, 2, 3]  MODIFIED!                       │
│                                                                  │
│  SHALLOW COPY - copies outer list only                          │
│  b = a[:]        or  b = a.copy()  or  b = list(a)             │
│                                                                  │
│  DEEP COPY - copies nested lists too                            │
│  import copy                                                     │
│  b = copy.deepcopy(a)                                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# COPYING LISTS
# ═══════════════════════════════════════════════════════════════

# ❌ WRONG: Assignment creates reference
a = [1, 2, 3]
b = a
b[0] = 100
print(a)  # [100, 2, 3] - BOTH changed!

# ✅ RIGHT: Shallow copy
a = [1, 2, 3]
b = a[:]       # Method 1: slicing
b = a.copy()   # Method 2: copy method
b = list(a)    # Method 3: list constructor
b[0] = 100
print(a)  # [1, 2, 3] - unchanged!

# ⚠️ SHALLOW COPY TRAP: Nested lists still reference same objects!
a = [[1, 2], [3, 4]]
b = a[:]
b[0][0] = 100
print(a)  # [[100, 2], [3, 4]] - NESTED list changed!

# ✅ DEEP COPY: For nested structures
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 100
print(a)  # [[1, 2], [3, 4]] - unchanged!
```

---

## 🔁 Iterating Over Lists

```python
# ═══════════════════════════════════════════════════════════════
# ITERATION METHODS
# ═══════════════════════════════════════════════════════════════

nums = [10, 20, 30]

# Method 1: Direct iteration
for num in nums:
    print(num)

# Method 2: Index iteration
for i in range(len(nums)):
    print(i, nums[i])

# Method 3: enumerate (INDEX + VALUE)
for i, num in enumerate(nums):
    print(f"Index {i}: {num}")
# Output:
# Index 0: 10
# Index 1: 20
# Index 2: 30

# Method 4: enumerate with start index
for i, num in enumerate(nums, start=1):
    print(f"Item {i}: {num}")
# Output:
# Item 1: 10
# Item 2: 20
# Item 3: 30

# Iterating two lists together: zip()
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

---

## 🔗 Built-in Functions with Lists

```python
# ═══════════════════════════════════════════════════════════════
# BUILT-IN FUNCTIONS
# ═══════════════════════════════════════════════════════════════

nums = [5, 2, 8, 1, 9]

print(len(nums))    # 5 (length)
print(min(nums))    # 1 (minimum)
print(max(nums))    # 9 (maximum)
print(sum(nums))    # 25 (sum)

# any() and all()
bools = [True, False, True]
print(any(bools))   # True (at least one True)
print(all(bools))   # False (not all True)

nums = [1, 2, 0, 4]
print(any(nums))    # True (non-zero = True)
print(all(nums))    # False (0 is False)

# Converting to/from lists
print(list("abc"))         # ['a', 'b', 'c']
print(list(range(3)))      # [0, 1, 2]
print(list((1, 2, 3)))     # [1, 2, 3] (from tuple)
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: append() vs extend()
a = [1, 2]
a.append([3, 4])   # Adds list as ONE element
print(a)  # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])   # Adds EACH element
print(b)  # [1, 2, 3, 4]

# TRAP 2: sort() returns None
nums = [3, 1, 2]
result = nums.sort()
print(result)  # None (!)
print(nums)    # [1, 2, 3]

# TRAP 3: Modifying while iterating
nums = [1, 2, 3, 4, 5]
# ❌ WRONG:
# for num in nums:
#     if num % 2 == 0:
#         nums.remove(num)  # Skips elements!

# ✅ RIGHT: Iterate over copy
for num in nums[:]:
    if num % 2 == 0:
        nums.remove(num)

# TRAP 4: List multiplication with nested lists
row = [[0] * 3] * 3  # WRONG!
row[0][0] = 1
print(row)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - ALL changed!

# ✅ RIGHT: Use comprehension
row = [[0] * 3 for _ in range(3)]
row[0][0] = 1
print(row)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

# TRAP 5: Empty list is falsy
print(bool([]))       # False
print(bool([0]))      # True (has one element!)
print(bool([False]))  # True (has one element!)

# TRAP 6: Index vs negative index
nums = [1, 2, 3]
# nums[3]   # IndexError!
print(nums[-1])  # 3 (last element)
```

---

## 📝 Quick Reference Table

| Method | Returns | Modifies List? | Example |
|--------|---------|----------------|---------|
| `append(x)` | None | ✅ Yes | `[1,2].append(3)` → `[1,2,3]` |
| `extend(it)` | None | ✅ Yes | `[1,2].extend([3,4])` → `[1,2,3,4]` |
| `insert(i,x)` | None | ✅ Yes | `[1,3].insert(1,2)` → `[1,2,3]` |
| `remove(x)` | None | ✅ Yes | `[1,2,3].remove(2)` → `[1,3]` |
| `pop([i])` | Element | ✅ Yes | `[1,2,3].pop()` → `3` |
| `sort()` | None | ✅ Yes | `[3,1,2].sort()` → `[1,2,3]` |
| `reverse()` | None | ✅ Yes | `[1,2,3].reverse()` → `[3,2,1]` |
| `index(x)` | Index | ❌ No | `[1,2,3].index(2)` → `1` |
| `count(x)` | Count | ❌ No | `[1,2,2,3].count(2)` → `2` |
| `copy()` | New list | ❌ No | `[1,2,3].copy()` → `[1,2,3]` |

---

## 🎯 Exam Checklist

- [ ] Lists are MUTABLE (can change elements)
- [ ] Indexing starts at 0, negative from -1
- [ ] Slicing: list[start:stop:step], stop is EXCLUSIVE
- [ ] append() adds ONE, extend() adds MANY
- [ ] sort() modifies list, returns None
- [ ] sorted() returns NEW list
- [ ] pop() removes by index, remove() by value
- [ ] Assignment (=) creates reference, not copy
- [ ] Empty list is falsy, [False] is truthy
- [ ] list[::-1] reverses the list

---

[[09_Strings|← Strings]] | [[00_Index|Index]] | [[11_Tuples|Tuples →]]
