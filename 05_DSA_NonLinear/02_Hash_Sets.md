---
title: Hash Sets
tags: [dsa, hash-set, set, unique, data-structure]
created: 2026-01-30
difficulty: intermediate
time_complexity: O(1) average
space_complexity: O(n)
---

# 🎯 Hash Sets

[[00_Index|← Back to Index]] | [[01_Hash_Tables|← Hash Tables]] | [[03_Hash_Maps|Hash Maps →]]

> **"A set is just a hash table where we only care about keys"**

---

## 🎯 The Concept

```
┌─────────────────────────────────────────────────────────────────┐
│                    WHAT IS A HASH SET?                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A Hash Set stores UNIQUE elements using hashing.               │
│  No duplicates allowed! No key-value pairs, just values.        │
│                                                                  │
│  Hash Table:  key → value                                       │
│  Hash Set:    value (key = value, no separate value)            │
│                                                                  │
│  Example Set: {1, 5, 3, 8, 2}                                   │
│                                                                  │
│  ┌─────────────────────────────────────────┐                    │
│  │  Index │ Element                        │                    │
│  ├────────┼────────────────────────────────┤                    │
│  │   0    │ empty                          │                    │
│  │   1    │ 1                              │                    │
│  │   2    │ 2                              │                    │
│  │   3    │ 3, 8 (collision → chain)       │                    │
│  │   4    │ empty                          │                    │
│  │   5    │ 5                              │                    │
│  └─────────────────────────────────────────┘                    │
│                                                                  │
│  Key Property: No duplicate elements!                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✅ Beginner-Friendly Python Way

Python sets store **unique** values.

```python
numbers = {1, 2, 2, 3}
print(numbers)  # {1, 2, 3}

numbers.add(4)
numbers.discard(2)
print(3 in numbers)  # True
```

Use `set` for fast membership checks.

---

## 🏗️ Hash Set Implementation

```python
# ═══════════════════════════════════════════════════════════════
# HASH SET IMPLEMENTATION
# ═══════════════════════════════════════════════════════════════

class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, value):
        """Hash function."""
        return hash(value) % self.size

    def add(self, value):
        """Add element to set (no duplicates)."""
        if value in self:
            return  # Already exists

        index = self._hash(value)
        self.buckets[index].append(value)
        self.count += 1

    def remove(self, value):
        """Remove element from set."""
        index = self._hash(value)
        bucket = self.buckets[index]

        if value in bucket:
            bucket.remove(value)
            self.count -= 1
        else:
            raise KeyError(f"Element '{value}' not found")

    def discard(self, value):
        """Remove if exists, don't raise error if not."""
        try:
            self.remove(value)
        except KeyError:
            pass

    def __contains__(self, value):
        """Check if element exists (O(1) average)."""
        index = self._hash(value)
        return value in self.buckets[index]

    def __len__(self):
        return self.count

    def __iter__(self):
        for bucket in self.buckets:
            for value in bucket:
                yield value

    def __str__(self):
        elements = list(self)
        return "{" + ", ".join(map(str, elements)) + "}"


# Usage
s = HashSet()
s.add(1)
s.add(2)
s.add(3)
s.add(2)  # Duplicate - ignored!

print(s)          # {1, 2, 3}
print(2 in s)     # True
print(len(s))     # 3
```

---

## 🔄 Set Operations

```
┌─────────────────────────────────────────────────────────────────┐
│                    SET OPERATIONS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A = {1, 2, 3, 4}                                               │
│  B = {3, 4, 5, 6}                                               │
│                                                                  │
│  UNION (A ∪ B):        {1, 2, 3, 4, 5, 6}                       │
│  ┌───────────────────┐                                          │
│  │   ┌─────┬─────┐   │                                          │
│  │   │ A   │   B │   │  All elements from both                  │
│  │   └─────┴─────┘   │                                          │
│  └───────────────────┘                                          │
│                                                                  │
│  INTERSECTION (A ∩ B): {3, 4}                                   │
│  ┌───────────────────┐                                          │
│  │   ┌─────┬─────┐   │                                          │
│  │   │     │█████│   │  Elements in both                        │
│  │   └─────┴─────┘   │                                          │
│  └───────────────────┘                                          │
│                                                                  │
│  DIFFERENCE (A - B):   {1, 2}                                   │
│  ┌───────────────────┐                                          │
│  │   ┌─────┬─────┐   │                                          │
│  │   │█████│     │   │  Elements in A but not B                 │
│  │   └─────┴─────┘   │                                          │
│  └───────────────────┘                                          │
│                                                                  │
│  SYMMETRIC DIFF (A △ B): {1, 2, 5, 6}                           │
│  ┌───────────────────┐                                          │
│  │   ┌─────┬─────┐   │                                          │
│  │   │█████│█████│   │  Elements in A or B, but not both        │
│  │   └─────┴─────┘   │                                          │
│  └───────────────────┘                                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Implementation

```python
# ═══════════════════════════════════════════════════════════════
# SET OPERATIONS IMPLEMENTATION
# ═══════════════════════════════════════════════════════════════

class HashSet:
    # ... (previous methods) ...

    def union(self, other):
        """Return new set with elements from both sets."""
        result = HashSet(self.size)
        for elem in self:
            result.add(elem)
        for elem in other:
            result.add(elem)
        return result

    def intersection(self, other):
        """Return new set with common elements."""
        result = HashSet(self.size)
        for elem in self:
            if elem in other:
                result.add(elem)
        return result

    def difference(self, other):
        """Return new set with elements in self but not in other."""
        result = HashSet(self.size)
        for elem in self:
            if elem not in other:
                result.add(elem)
        return result

    def symmetric_difference(self, other):
        """Return new set with elements in either but not both."""
        result = HashSet(self.size)
        for elem in self:
            if elem not in other:
                result.add(elem)
        for elem in other:
            if elem not in self:
                result.add(elem)
        return result

    def issubset(self, other):
        """Check if all elements are in other."""
        for elem in self:
            if elem not in other:
                return False
        return True

    def issuperset(self, other):
        """Check if contains all elements of other."""
        return other.issubset(self)
```

---

## 🐍 Python's Built-in set

```python
# ═══════════════════════════════════════════════════════════════
# PYTHON SET OPERATIONS
# ═══════════════════════════════════════════════════════════════

# Creating sets
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
empty = set()  # NOT {} - that's an empty dict!

# Basic operations - O(1) average
a.add(5)           # Add element
a.remove(1)        # Remove (raises KeyError if missing)
a.discard(99)      # Remove (no error if missing)
print(3 in a)      # Membership test

# Set operations
print(a | b)       # Union:              {2, 3, 4, 5, 6}
print(a & b)       # Intersection:       {3, 4, 5}
print(a - b)       # Difference:         {2}
print(a ^ b)       # Symmetric diff:     {2, 6}

# Method equivalents
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# Subset/superset
print({1, 2}.issubset({1, 2, 3}))     # True
print({1, 2, 3}.issuperset({1, 2}))   # True

# Frozen set (immutable)
fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError - immutable!
```

---

## 🎯 Common Use Cases

```python
# ═══════════════════════════════════════════════════════════════
# PRACTICAL APPLICATIONS
# ═══════════════════════════════════════════════════════════════

# 1. Remove duplicates from a list
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
print(unique)  # [1, 2, 3, 4]

# 2. Fast membership testing
valid_users = {"alice", "bob", "charlie"}
if "alice" in valid_users:  # O(1) instead of O(n)
    print("Valid user")

# 3. Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(common)  # {4, 5}

# 4. Find unique elements
all_items = set(list1) | set(list2)
print(all_items)  # {1, 2, 3, 4, 5, 6, 7, 8}

# 5. Check for duplicates
def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates([1, 2, 3]))     # False
print(has_duplicates([1, 2, 2, 3]))  # True

# 6. Two Sum problem (using set)
def two_sum_exists(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

print(two_sum_exists([2, 7, 11, 15], 9))  # True (2 + 7)
```

---

## 📊 Time Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| add() | O(1) | O(n) |
| remove() | O(1) | O(n) |
| contains (in) | O(1) | O(n) |
| union | O(n+m) | O(n+m) |
| intersection | O(min(n,m)) | O(n*m) |
| difference | O(n) | O(n) |

---

## 🆚 Set vs List for Membership

```python
# ═══════════════════════════════════════════════════════════════
# PERFORMANCE COMPARISON
# ═══════════════════════════════════════════════════════════════
import time

n = 100000
data_list = list(range(n))
data_set = set(range(n))

# List membership - O(n)
start = time.time()
for _ in range(1000):
    99999 in data_list
print(f"List: {time.time() - start:.4f}s")

# Set membership - O(1)
start = time.time()
for _ in range(1000):
    99999 in data_set
print(f"Set:  {time.time() - start:.4f}s")

# Result: Set is ~1000x faster for large data!
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Empty set with {}
empty = {}        # This is a DICT!
print(type(empty))  # <class 'dict'>

# ✅ RIGHT: Use set()
empty = set()
print(type(empty))  # <class 'set'>

# ❌ WRONG: Mutable elements
# s = {[1, 2, 3]}  # TypeError! Lists are mutable

# ✅ RIGHT: Use tuples for immutable sequences
s = {(1, 2, 3)}   # OK

# ❌ WRONG: Assuming order
s = {3, 1, 2}
# Order is NOT guaranteed (though Python 3.7+ maintains insertion order for dict)

# ❌ WRONG: Modifying set while iterating
s = {1, 2, 3, 4, 5}
# for item in s:
#     if item % 2 == 0:
#         s.remove(item)  # RuntimeError!

# ✅ RIGHT: Iterate over a copy
for item in list(s):
    if item % 2 == 0:
        s.remove(item)
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Use set for membership tests | Use list for large lookups |
| Use set() for empty set | Use {} for empty set |
| Use frozenset for immutable | Modify sets being iterated |
| Use set operations | Write manual loops |
| Use hashable elements only | Try to add mutable objects |

---

## 🎯 Exam Checklist

- [ ] Set stores unique elements only
- [ ] Uses hashing internally (like hash table)
- [ ] O(1) average for add, remove, contains
- [ ] Union (|), Intersection (&), Difference (-)
- [ ] Elements must be hashable (immutable)
- [ ] `set()` for empty set, NOT `{}`
- [ ] `frozenset` for immutable sets

---

[[01_Hash_Tables|← Hash Tables]] | [[00_Index|Index]] | [[03_Hash_Maps|Hash Maps →]]
