---
title: Hash Tables
tags: [dsa, hash-table, hashing, collision, data-structure]
created: 2026-01-30
difficulty: intermediate
time_complexity: O(1) average
space_complexity: O(n)
---

# #️⃣ Hash Tables

[[00_Index|← Back to Index]] | [[02_Hash_Sets|Hash Sets →]]

> **"Hash tables: Trading space for time since 1953"**

---

## 🎯 The Concept

```
┌─────────────────────────────────────────────────────────────────┐
│                    WHAT IS A HASH TABLE?                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A Hash Table is a data structure that maps KEYS to VALUES      │
│  using a HASH FUNCTION for near-constant time operations.       │
│                                                                  │
│  KEY ──→ [HASH FUNCTION] ──→ INDEX ──→ VALUE                    │
│                                                                  │
│  Example:                                                        │
│  "apple" ──→ hash("apple") ──→ 3 ──→ bucket[3] ──→ "red"       │
│                                                                  │
│  ┌─────────────────────────────────────────┐                    │
│  │  Index │ Key      │ Value               │                    │
│  ├────────┼──────────┼─────────────────────┤                    │
│  │   0    │ "banana" │ "yellow"            │                    │
│  │   1    │  empty   │                     │                    │
│  │   2    │ "grape"  │ "purple"            │                    │
│  │   3    │ "apple"  │ "red"               │                    │
│  │   4    │  empty   │                     │                    │
│  └─────────────────────────────────────────┘                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✅ Beginner-Friendly Python Way

Python already provides hash tables with `dict`.

```python
colors = {
    "apple": "red",
    "banana": "yellow",
}

# Insert or update
colors["grape"] = "purple"

# Lookup
print(colors["apple"])  # red

# Safe lookup
print(colors.get("pear", "not found"))  # not found
```

Use `dict` unless you are studying how hash tables work internally.

---

## 🔧 How Hashing Works

```python
# ═══════════════════════════════════════════════════════════════
# SIMPLE HASH FUNCTION EXAMPLE
# ═══════════════════════════════════════════════════════════════

def simple_hash(key, table_size):
    """Convert key to an index."""
    # Sum of ASCII values modulo table size
    hash_value = sum(ord(char) for char in str(key))
    return hash_value % table_size

# Example
table_size = 10
print(simple_hash("apple", table_size))   # 0
print(simple_hash("banana", table_size))  # 5
print(simple_hash("cherry", table_size))  # 3

# Python's built-in hash function
print(hash("apple"))      # Large integer (varies)
print(hash("apple") % 10) # Index between 0-9
```

---

## 🏗️ Basic Hash Table Implementation

```python
# ═══════════════════════════════════════════════════════════════
# HASH TABLE WITH CHAINING (Collision Resolution)
# ═══════════════════════════════════════════════════════════════

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of buckets
        self.count = 0

    def _hash(self, key):
        """Hash function - converts key to index."""
        return hash(key) % self.size

    def put(self, key, value):
        """Insert or update a key-value pair."""
        index = self._hash(key)
        bucket = self.table[index]

        # Check if key exists, update if so
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Key doesn't exist, append
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        """Retrieve value by key."""
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        """Remove a key-value pair."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return v

        raise KeyError(f"Key '{key}' not found")

    def __contains__(self, key):
        """Check if key exists."""
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        return self.count

    def __str__(self):
        items = []
        for bucket in self.table:
            for k, v in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"


# Usage
ht = HashTable()
ht.put("name", "Alice")
ht.put("age", 25)
ht.put("city", "Berlin")

print(ht.get("name"))     # Alice
print("age" in ht)        # True
print(len(ht))            # 3
print(ht)                 # {name: Alice, age: 25, city: Berlin}
```

---

## 💥 Collision Resolution

When two keys hash to the same index, we have a **collision**.

```
┌─────────────────────────────────────────────────────────────────┐
│                    COLLISION EXAMPLE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  hash("apple") % 5 = 2                                          │
│  hash("melon") % 5 = 2    ← COLLISION! Same index!             │
│                                                                  │
│  SOLUTION 1: CHAINING (Linked List at each bucket)              │
│  ┌───┬───────────────────────────────────┐                      │
│  │ 0 │ → empty                           │                      │
│  │ 1 │ → empty                           │                      │
│  │ 2 │ → [apple,red] → [melon,green]     │  ← Chain!           │
│  │ 3 │ → empty                           │                      │
│  │ 4 │ → [grape,purple]                  │                      │
│  └───┴───────────────────────────────────┘                      │
│                                                                  │
│  SOLUTION 2: OPEN ADDRESSING (Linear Probing)                   │
│  ┌───┬──────────────────┐                                       │
│  │ 0 │ empty            │                                       │
│  │ 1 │ empty            │                                       │
│  │ 2 │ [apple, red]     │  ← First key                         │
│  │ 3 │ [melon, green]   │  ← Probe next slot!                  │
│  │ 4 │ [grape, purple]  │                                       │
│  └───┴──────────────────┘                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Chaining Implementation (shown above)

### Open Addressing (Linear Probing)

```python
# ═══════════════════════════════════════════════════════════════
# HASH TABLE WITH LINEAR PROBING
# ═══════════════════════════════════════════════════════════════

class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def _probe(self, index):
        """Find next available slot (linear probing)."""
        return (index + 1) % self.size

    def put(self, key, value):
        if self.count >= self.size * 0.7:  # Load factor check
            self._resize()

        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value  # Update
                return
            index = self._probe(index)

        self.keys[index] = key
        self.values[index] = value
        self.count += 1

    def get(self, key):
        index = self._hash(key)
        start = index

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._probe(index)
            if index == start:
                break

        raise KeyError(f"Key '{key}' not found")

    def _resize(self):
        """Double the table size when load factor exceeds threshold."""
        old_keys = self.keys
        old_values = self.values

        self.size *= 2
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.count = 0

        for i, key in enumerate(old_keys):
            if key is not None:
                self.put(key, old_values[i])
```

---

## 📊 Load Factor

```
┌─────────────────────────────────────────────────────────────────┐
│                      LOAD FACTOR                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Load Factor (α) = n / m                                        │
│                                                                  │
│  Where:                                                          │
│    n = number of entries                                        │
│    m = number of buckets                                        │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │  Load Factor  │  Performance  │  Action                │     │
│  ├───────────────┼───────────────┼────────────────────────┤     │
│  │  α < 0.5      │  Excellent    │  Space wasted          │     │
│  │  0.5 ≤ α ≤ 0.7│  Good         │  Optimal range         │     │
│  │  α > 0.7      │  Degrading    │  Consider resize       │     │
│  │  α > 1.0      │  Poor         │  Must resize (chain)   │     │
│  └────────────────────────────────────────────────────────┘     │
│                                                                  │
│  When α exceeds threshold → RESIZE (usually double)             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🐍 Python's Built-in dict

```python
# ═══════════════════════════════════════════════════════════════
# PYTHON DICT IS A HASH TABLE!
# ═══════════════════════════════════════════════════════════════

# Creating a dictionary (hash table)
person = {
    "name": "Alice",
    "age": 25,
    "city": "Berlin"
}

# O(1) average operations
person["email"] = "alice@example.com"  # Insert
print(person["name"])                   # Lookup
del person["city"]                      # Delete
print("age" in person)                  # Contains

# Dict methods
print(person.keys())      # dict_keys(['name', 'age', 'email'])
print(person.values())    # dict_values(['Alice', 25, 'alice@...'])
print(person.items())     # dict_items([('name', 'Alice'), ...])

# Safe access
print(person.get("phone", "N/A"))  # N/A (default if missing)

# Iteration
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## ⚡ Hash Functions

```python
# ═══════════════════════════════════════════════════════════════
# GOOD VS BAD HASH FUNCTIONS
# ═══════════════════════════════════════════════════════════════

# ❌ BAD: Always returns same value (all collisions!)
def bad_hash(key):
    return 0

# ❌ BAD: Only uses first character
def bad_hash_2(key):
    return ord(str(key)[0]) % 10

# ✅ GOOD: Uses all characters
def good_hash(key, size):
    hash_val = 0
    for i, char in enumerate(str(key)):
        hash_val += ord(char) * (31 ** i)
    return hash_val % size

# ✅ BETTER: Python's built-in
hash("hello")  # Uses sophisticated algorithm

# Properties of a good hash function:
# 1. Deterministic - same input → same output
# 2. Uniform distribution - spreads keys evenly
# 3. Fast to compute
# 4. Minimizes collisions
```

---

## 📊 Time Complexity

| Operation | Average | Worst Case |
|-----------|---------|------------|
| Search | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Space | O(n) | O(n) |

**Worst case** occurs when all keys hash to the same index (all collisions).

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Using mutable objects as keys
my_dict = {}
# my_dict[[1, 2, 3]] = "value"  # TypeError! Lists are mutable

# ✅ RIGHT: Use immutable objects as keys
my_dict[(1, 2, 3)] = "value"   # Tuples are OK
my_dict["string"] = "value"    # Strings are OK
my_dict[42] = "value"          # Numbers are OK

# ❌ WRONG: Modifying dict while iterating
data = {"a": 1, "b": 2, "c": 3}
# for key in data:
#     if data[key] < 2:
#         del data[key]  # RuntimeError!

# ✅ RIGHT: Iterate over a copy
for key in list(data.keys()):
    if data[key] < 2:
        del data[key]

# ❌ WRONG: Assuming insertion order (Python < 3.7)
# ✅ RIGHT: Python 3.7+ guarantees insertion order
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Use immutable keys | Use mutable objects as keys |
| Check load factor | Let table get too full |
| Use built-in dict | Implement from scratch (usually) |
| Handle missing keys | Assume key exists |
| Consider defaultdict | Manual default handling |

---

## 🎯 Exam Checklist

- [ ] Hash function converts key to index
- [ ] Collision: two keys → same index
- [ ] Chaining: linked list at each bucket
- [ ] Open addressing: probe for next slot
- [ ] Load factor = entries / buckets
- [ ] Average O(1), worst O(n)
- [ ] Python dict is a hash table
- [ ] Keys must be hashable (immutable)

---

[[00_Index|← Index]] | [[02_Hash_Sets|Hash Sets →]]
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

# simple view of buckets (values as lengths)
buckets = [2, 0, 1, 3, 0]
draw_array(buckets, title="Hash Table Buckets")
```
