---
title: Tuples and Sets
category: fundamentals
tags: ['python', 'tuples', 'sets', 'data-structures', 'immutable']
created: 2026-01-27
type: topic
---

# Tuples and Sets

[[00_Index|← Back to Index]]

> **Tuples: Immutable sequences. Sets: Unique collections.**

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║    📦 TUPLES vs. SETS - Unveränderbar vs. Eindeutig          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   TUPLES (Geordnet, Unveränderbar):                          ║
║   ┌──────┬──────┬──────┬──────┬──────┐                       ║
║   │ "a"  │ "b"  │ "c"  │ "a"  │ "d"  │  ← Duplikate erlaubt ║
║   └──────┴──────┴──────┴──────┴──────┘                       ║
║   coords = (10, 20)                                           ║
║   ❌ Keine Änderungen möglich (immutable)                     ║
║   ✅ Kann als Dict-Schlüssel verwendet werden               ║
║                                                               ║
║   SETS (Ungeordnet, Eindeutig):                              ║
║      ╭─────────────────────────╮                             ║
║      │ "a"       "c"       "d" │  ← Nur eindeutige Werte    ║
║      │       "b"            │                                ║
║      ╰─────────────────────────╯                             ║
║   colors = {"red", "blue", "red"}  →  {"red", "blue"}       ║
║   ✅ Duplikate automatisch entfernt                          ║
║   ✅ Perfekt für Memberships-Tests                          ║
║                                                               ║
║   💡 Tuples = Sichere Listen, Sets = Eindeutige Elemente     ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📦 Tuples

### What is a Tuple?

A **tuple** is an ordered, **immutable** collection that allows duplicate values.

**Key Characteristics:**
- ✅ **Ordered** - maintains insertion order
- ❌ **Immutable** - cannot be changed after creation
- ✅ **Allows duplicates** - can have repeated values
- ✅ **Hashable** - can be dict keys or set elements
- ✅ **Faster** than lists (due to immutability)

### Creating Tuples

```python
# Empty tuple
empty = ()
empty = tuple()

# Single element (comma required!)
single = (42,)      # Correct
not_tuple = (42)    # This is just int 42!

# Multiple elements
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Without parentheses (tuple packing)
coords = 10, 20     # Same as (10, 20)

# From other types
from_list = tuple([1, 2, 3])
from_string = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')
```

### Accessing Tuple Items

```python
fruits = ('banana', 'orange', 'mango', 'lemon')

# Positive indexing
first = fruits[0]       # 'banana'
last = fruits[3]        # 'lemon'

# Negative indexing
last = fruits[-1]       # 'lemon'
first = fruits[-4]      # 'banana'

# Slicing
middle = fruits[1:3]    # ('orange', 'mango')
all_fruits = fruits[:]  # Copy entire tuple
```

### Tuple Operations

```python
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = (1, 2) * 3      # (1, 2, 1, 2, 1, 2)

# Length
length = len(tuple1)        # 3

# Check membership
exists = 2 in tuple1        # True

# Count occurrences
numbers = (1, 2, 2, 3, 2)
count = numbers.count(2)    # 3

# Find index
index = numbers.index(3)    # 3
```

### Tuple Unpacking

```python
# Basic unpacking
point = (10, 20)
x, y = point
print(x, y)  # 10 20

# Multiple values
person = ("Alice", 25, "NYC")
name, age, city = person

# With * (rest)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)    # 1
print(middle)   # [2, 3, 4]
print(last)     # 5
```

### Use Cases for Tuples

```python
# 1. Return multiple values
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

# 2. Dictionary keys
locations = {
    (0, 0): "origin",
    (1, 0): "right",
    (0, 1): "up"
}

# 3. Protect data from modification
constants = (3.14159, 2.71828, 1.41421)
# constants[0] = 3.14  # TypeError!

# 4. Named tuples (more readable)
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
```

---

## 🎲 Sets

### What is a Set?

A **set** is an **unordered** collection of **unique** items.

**Key Characteristics:**
- ❌ **Unordered** - no indexing or slicing
- ✅ **Mutable** - can add/remove items
- ❌ **No duplicates** - automatically removes duplicates
- ✅ **Fast lookups** - O(1) membership testing
- ✅ **Math operations** - union, intersection, difference

### Creating Sets

```python
# Empty set (note: {} creates empty dict!)
empty = set()

# With initial values
numbers = {1, 2, 3, 4, 5}
fruits = {'apple', 'banana', 'orange'}

# Duplicates automatically removed
with_dupes = {1, 2, 2, 3, 3, 3}
print(with_dupes)  # {1, 2, 3}

# From other types
from_list = set([1, 2, 2, 3])      # {1, 2, 3}
from_string = set("hello")          # {'h', 'e', 'l', 'o'}
```

### Adding Items

```python
fruits = {'apple', 'banana'}

# Add single item
fruits.add('orange')
print(fruits)  # {'apple', 'banana', 'orange'}

# Add multiple items
fruits.update(['mango', 'grape'])
print(fruits)  # {'apple', 'banana', 'orange', 'mango', 'grape'}

# Adding duplicate has no effect
fruits.add('apple')  # No error, just ignored
```

### Removing Items

```python
fruits = {'apple', 'banana', 'orange'}

# remove() - raises error if not found
fruits.remove('banana')
# fruits.remove('grape')  # KeyError!

# discard() - no error if not found
fruits.discard('orange')
fruits.discard('grape')  # No error

# pop() - removes and returns random item
item = fruits.pop()

# clear() - removes all items
fruits.clear()
```

### Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all items from both)
union = a | b
union = a.union(b)
print(union)  # {1, 2, 3, 4, 5, 6}

# Intersection (items in both)
inter = a & b
inter = a.intersection(b)
print(inter)  # {3, 4}

# Difference (in a, not in b)
diff = a - b
diff = a.difference(b)
print(diff)  # {1, 2}

# Symmetric difference (in either, not both)
sym_diff = a ^ b
sym_diff = a.symmetric_difference(b)
print(sym_diff)  # {1, 2, 5, 6}

# Subset check
small = {1, 2}
print(small.issubset(a))     # True
print(a.issuperset(small))   # True

# Disjoint check (no common elements)
c = {7, 8, 9}
print(a.isdisjoint(c))       # True
```

### Practical Examples

```python
# Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4, 5]

# Fast membership testing
large_set = set(range(1000000))
# Very fast O(1)
if 500000 in large_set:
    print("Found!")

# Find common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print(common)  # {3, 4}

# Find unique elements
unique_to_list1 = set(list1) - set(list2)
print(unique_to_list1)  # {1, 2}
```

---

## ⚖️ Comparison

| Feature | Tuple | Set |
|---------|-------|-----|
| **Ordered** | ✅ Yes | ❌ No |
| **Mutable** | ❌ No | ✅ Yes |
| **Duplicates** | ✅ Yes | ❌ No |
| **Indexing** | ✅ Yes | ❌ No |
| **Hashable** | ✅ Yes | ❌ No |
| **Syntax** | `(1, 2)` | `{1, 2}` |
| **Use case** | Fixed data, dict keys | Unique items, fast lookup |

---

## 💡 Best Practices

### Tuples

```python
# ✅ Use for fixed data
dimensions = (1920, 1080)

# ✅ Single element needs comma
single = (42,)

# ✅ Use as dict keys
grid = {(0, 0): "start", (10, 10): "end"}

# ✅ Multiple return values
def min_max(numbers):
    return (min(numbers), max(numbers))
```

### Sets

```python
# ✅ Remove duplicates efficiently
unique = set(my_list)

# ✅ Fast membership testing
valid_users = {'alice', 'bob', 'charlie'}
if username in valid_users:  # O(1)
    pass

# ✅ Math operations
all_users = active_users | inactive_users
premium = paid_users & verified_users

# ✅ Use {} only for non-empty sets
my_set = {1, 2, 3}  # Good
empty = set()        # Not {}
```

---

## 🎓 Summary

**Tuples:**
- Immutable sequences
- Use parentheses `()`
- Hashable (can be dict keys)
- Ordered and allow duplicates

**Sets:**
- Unique unordered collections
- Use curly braces `{}`
- Fast lookups O(1)
- Math operations (union, intersection, etc.)

**Key Takeaway:** Use tuples to protect data, sets for uniqueness and speed!

---

## 🔗 Related Topics

- [[02_Lists_Deep_Dive|Lists]]
- [[04_Dictionaries_Mastery|Dictionaries]]

---

[[00_Index|← Back to Index]]

*Immutability and uniqueness! 🔒*
