---
title: Hash Maps
tags: [dsa, hash-map, dictionary, key-value, data-structure]
created: 2026-01-30
difficulty: intermediate
time_complexity: O(1) average
space_complexity: O(n)
---

# 🗺️ Hash Maps

[[00_Index|← Back to Index]] | [[02_Hash_Sets|← Hash Sets]] | [[04_Trees|Trees →]]

> **"Hash maps: The Swiss Army knife of data structures"**

---

## 🎯 The Concept

```
┌─────────────────────────────────────────────────────────────────┐
│                    WHAT IS A HASH MAP?                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A Hash Map (Dictionary) stores KEY-VALUE pairs.                │
│  Keys are unique, values can be anything.                       │
│                                                                  │
│  Hash Set:  stores values only                                  │
│  Hash Map:  stores key → value pairs                            │
│                                                                  │
│  ┌─────────────────────────────────────────┐                    │
│  │     KEY        │      VALUE             │                    │
│  ├────────────────┼────────────────────────┤                    │
│  │  "name"        │  "Alice"               │                    │
│  │  "age"         │  25                    │                    │
│  │  "email"       │  "alice@example.com"   │                    │
│  │  "scores"      │  [95, 87, 92]          │                    │
│  └─────────────────────────────────────────┘                    │
│                                                                  │
│  Keys must be UNIQUE and HASHABLE                               │
│  Values can be ANYTHING (including other hash maps!)            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✅ Beginner-Friendly Python Way

Python dictionaries are hash maps.

```python
ages = {"Ana": 30, "Ben": 25}

# Insert
ages["Cara"] = 28

# Update
ages["Ben"] = 26

# Iterate
for name, age in ages.items():
    print(name, age)
```

---

## 🏗️ Hash Map Implementation

```python
# ═══════════════════════════════════════════════════════════════
# COMPLETE HASH MAP IMPLEMENTATION
# ═══════════════════════════════════════════════════════════════

class HashMap:
    def __init__(self, initial_capacity=16, load_factor=0.75):
        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        """Hash function - converts key to bucket index."""
        return hash(key) % self.capacity

    def _resize(self):
        """Double capacity when load factor exceeded."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key, value):
        """Insert or update key-value pair."""
        # Check load factor
        if self.size >= self.capacity * self.load_factor:
            self._resize()

        index = self._hash(key)
        bucket = self.buckets[index]

        # Update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Insert new key-value pair
        bucket.append((key, value))
        self.size += 1

    def get(self, key, default=None):
        """Get value by key, return default if not found."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return default

    def remove(self, key):
        """Remove key-value pair, return value."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return v

        raise KeyError(key)

    def __getitem__(self, key):
        """Enable map[key] syntax."""
        result = self.get(key)
        if result is None and key not in self:
            raise KeyError(key)
        return result

    def __setitem__(self, key, value):
        """Enable map[key] = value syntax."""
        self.put(key, value)

    def __delitem__(self, key):
        """Enable del map[key] syntax."""
        self.remove(key)

    def __contains__(self, key):
        """Enable 'key in map' syntax."""
        index = self._hash(key)
        return any(k == key for k, v in self.buckets[index])

    def __len__(self):
        return self.size

    def keys(self):
        """Return all keys."""
        for bucket in self.buckets:
            for k, v in bucket:
                yield k

    def values(self):
        """Return all values."""
        for bucket in self.buckets:
            for k, v in bucket:
                yield v

    def items(self):
        """Return all key-value pairs."""
        for bucket in self.buckets:
            for k, v in bucket:
                yield (k, v)

    def __str__(self):
        items = [f"{k!r}: {v!r}" for k, v in self.items()]
        return "{" + ", ".join(items) + "}"


# Usage
hm = HashMap()
hm["name"] = "Alice"
hm["age"] = 25
hm["city"] = "Berlin"

print(hm["name"])      # Alice
print(hm.get("phone", "N/A"))  # N/A
print("age" in hm)     # True
print(len(hm))         # 3
print(hm)              # {'name': 'Alice', 'age': 25, 'city': 'Berlin'}
```

---

## 🐍 Python dict - The Ultimate Hash Map

```python
# ═══════════════════════════════════════════════════════════════
# PYTHON DICTIONARY OPERATIONS
# ═══════════════════════════════════════════════════════════════

# Creating dictionaries
empty = {}
person = {"name": "Alice", "age": 25}
from_pairs = dict([("a", 1), ("b", 2)])
from_kwargs = dict(x=1, y=2, z=3)

# Basic operations - O(1) average
person["email"] = "alice@example.com"  # Insert
print(person["name"])                   # Access
del person["age"]                       # Delete
print("email" in person)                # Contains

# Safe access
print(person.get("phone"))              # None (no error)
print(person.get("phone", "Unknown"))   # "Unknown" (default)

# Iteration
for key in person:                      # Keys only
    print(key)

for key, value in person.items():       # Key-value pairs
    print(f"{key}: {value}")

for value in person.values():           # Values only
    print(value)

# ═══════════════════════════════════════════════════════════════
# USEFUL DICT METHODS
# ═══════════════════════════════════════════════════════════════

d = {"a": 1, "b": 2}

# setdefault - get value or set default if missing
d.setdefault("c", 3)  # Sets d["c"] = 3 and returns 3
d.setdefault("a", 99) # Returns 1 (already exists)

# update - merge dictionaries
d.update({"d": 4, "e": 5})
d |= {"f": 6}  # Python 3.9+ merge operator

# pop - remove and return value
value = d.pop("a")        # Returns 1, removes key
value = d.pop("z", None)  # Returns None, no error

# popitem - remove and return last inserted
key, val = d.popitem()

# clear - remove all
d.clear()
```

---

## 🔧 Advanced Patterns

### Counter Pattern

```python
# ═══════════════════════════════════════════════════════════════
# COUNTING FREQUENCIES
# ═══════════════════════════════════════════════════════════════

# Manual counting
def count_chars(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(count_chars("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Using collections.Counter
from collections import Counter

freq = Counter("hello")
print(freq)                  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
print(freq.most_common(2))   # [('l', 2), ('h', 1)]
```

### Default Dict Pattern

```python
# ═══════════════════════════════════════════════════════════════
# GROUPING WITH DEFAULT VALUES
# ═══════════════════════════════════════════════════════════════
from collections import defaultdict

# Group words by first letter
words = ["apple", "banana", "apricot", "berry", "avocado"]

# Manual approach
grouped = {}
for word in words:
    key = word[0]
    if key not in grouped:
        grouped[key] = []
    grouped[key].append(word)

# Using defaultdict (cleaner)
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)

print(dict(grouped))
# {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'berry']}

# defaultdict with int (for counting)
counter = defaultdict(int)
for word in words:
    counter[word[0]] += 1

print(dict(counter))  # {'a': 3, 'b': 2}
```

### Two-Way Mapping

```python
# ═══════════════════════════════════════════════════════════════
# BIDIRECTIONAL MAPPING
# ═══════════════════════════════════════════════════════════════

class BiDict:
    """Two-way dictionary."""
    def __init__(self):
        self.forward = {}
        self.backward = {}

    def put(self, key, value):
        self.forward[key] = value
        self.backward[value] = key

    def get_by_key(self, key):
        return self.forward.get(key)

    def get_by_value(self, value):
        return self.backward.get(value)


# Usage
countries = BiDict()
countries.put("DE", "Germany")
countries.put("FR", "France")

print(countries.get_by_key("DE"))      # Germany
print(countries.get_by_value("France")) # FR
```

---

## 🎯 Common Interview Problems

```python
# ═══════════════════════════════════════════════════════════════
# CLASSIC HASH MAP PROBLEMS
# ═══════════════════════════════════════════════════════════════

# 1. Two Sum - O(n)
def two_sum(nums, target):
    """Find indices of two numbers that add to target."""
    seen = {}  # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

# 2. First Unique Character - O(n)
def first_unique_char(s):
    """Find index of first non-repeating character."""
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

print(first_unique_char("leetcode"))  # 0 ('l')

# 3. Group Anagrams - O(n * k log k)
def group_anagrams(strs):
    """Group words that are anagrams of each other."""
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # Sorted chars as key
        groups[key].append(s)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# 4. Longest Consecutive Sequence - O(n)
def longest_consecutive(nums):
    """Find length of longest consecutive sequence."""
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting from sequence start
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            max_length = max(max_length, length)

    return max_length

print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4 (1,2,3,4)
```

---

## 📊 Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| put/insert | O(1) | O(n) |
| get/access | O(1) | O(n) |
| delete | O(1) | O(n) |
| contains | O(1) | O(n) |
| keys/values/items | O(n) | O(n) |

**Space Complexity:** O(n)

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Accessing missing key directly
d = {"a": 1}
# print(d["b"])  # KeyError!

# ✅ RIGHT: Use get() or check first
print(d.get("b", "default"))
if "b" in d:
    print(d["b"])

# ❌ WRONG: Mutable default argument
def add_item(item, items={}):  # DANGER!
    items[item] = True
    return items

# ✅ RIGHT: Use None as default
def add_item(item, items=None):
    if items is None:
        items = {}
    items[item] = True
    return items

# ❌ WRONG: Using mutable objects as keys
# d = {[1, 2]: "value"}  # TypeError!

# ✅ RIGHT: Use tuples (immutable)
d = {(1, 2): "value"}

# ❌ WRONG: Modifying dict while iterating
d = {"a": 1, "b": 2, "c": 3}
# for key in d:
#     if d[key] < 2:
#         del d[key]  # RuntimeError!

# ✅ RIGHT: Iterate over a copy
for key in list(d.keys()):
    if d[key] < 2:
        del d[key]
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Use `.get()` for safe access | Access keys that might not exist |
| Use `defaultdict` for grouping | Manual key existence checks |
| Use `Counter` for frequency | Manual counting |
| Use comprehensions | Verbose loops |
| Check membership with `in` | Try/except for membership |

---

## 🎯 Exam Checklist

- [ ] Hash map stores key-value pairs
- [ ] Keys must be unique and hashable
- [ ] O(1) average for all operations
- [ ] Python `dict` is a hash map
- [ ] `.get()` for safe access with default
- [ ] `defaultdict` for automatic default values
- [ ] `Counter` for frequency counting
- [ ] Keys are iterated in insertion order (3.7+)

---

[[02_Hash_Sets|← Hash Sets]] | [[00_Index|Index]] | [[04_Trees|Trees →]]
---

## 🎨 Visualization (Optional)

```python
import sys
import site
from pathlib import Path

# Ensure user site-packages are visible (Obsidian runner)
user_site = site.getusersitepackages()
if user_site and user_site not in sys.path:
    sys.path.append(user_site)

# Add vault root to sys.path (Obsidian runner)
# Tries current dir, parent dirs, then a known vault path fallback.
added = False
for p in [Path.cwd(), *Path.cwd().parents]:
    if (p / "DSA_Utils").exists():
        sys.path.append(str(p))
        added = True
        break

if not added:
    fallback = Path("/Users/jochenwahl/Library/CloudStorage/OneDrive-Persönlich/z99_Obsidian_Vault/Codex_Coding")
    if fallback.exists():
        sys.path.append(str(fallback))

from DSA_Utils.utils import draw_array

keys = [1, 2, 3, 4]
draw_array(keys, title="Map Keys")
```
