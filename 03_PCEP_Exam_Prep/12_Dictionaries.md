---
title: Dictionaries
tags: [pcep, python, dictionaries, dict, key-value]
created: 2026-01-30
exam_section: 3
exam_weight: 8%
---

# 📖 Dictionaries

[[00_Index|← Back to Index]] | [[11_Tuples|← Tuples]] | [[13_Functions_Basics|Functions →]]

> **"Key-value pairs - know the methods and traps!"**

---

## 🎯 What is a Dictionary?

```
┌─────────────────────────────────────────────────────────────────┐
│              DICTIONARY                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A dictionary stores KEY-VALUE pairs.                           │
│                                                                  │
│  {                                                               │
│      "name": "Alice",      ← key: value                         │
│      "age": 25,            ← key: value                         │
│      "city": "Berlin"      ← key: value                         │
│  }                                                               │
│                                                                  │
│  • Keys must be UNIQUE and HASHABLE (immutable)                 │
│  • Values can be ANYTHING                                       │
│  • Ordered since Python 3.7 (insertion order preserved)         │
│  • Mutable (can add, modify, delete)                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Creating Dictionaries

```python
# ═══════════════════════════════════════════════════════════════
# DICTIONARY CREATION
# ═══════════════════════════════════════════════════════════════

# Empty dictionary
empty = {}
empty2 = dict()

# With initial values
person = {"name": "Alice", "age": 25, "city": "Berlin"}

# From list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# Using keyword arguments
d = dict(name="Alice", age=25)
print(d)  # {'name': 'Alice', 'age': 25}

# Dict comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists with zip
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)  # {'a': 1, 'b': 2, 'c': 3}

# Keys must be hashable (immutable)
valid = {
    "string": 1,     # OK
    42: 2,           # OK
    (1, 2): 3,       # OK (tuple)
    3.14: 4          # OK
}
# invalid = {[1, 2]: 5}  # TypeError! Lists not hashable
```

---

## 🔑 Accessing Values

```python
# ═══════════════════════════════════════════════════════════════
# ACCESSING DICTIONARY VALUES
# ═══════════════════════════════════════════════════════════════

person = {"name": "Alice", "age": 25, "city": "Berlin"}

# Direct access with []
print(person["name"])   # Alice
print(person["age"])    # 25
# print(person["phone"])  # KeyError! Key doesn't exist

# Safe access with get() - returns None or default
print(person.get("name"))         # Alice
print(person.get("phone"))        # None (no error!)
print(person.get("phone", "N/A")) # N/A (custom default)

# Check if key exists
print("name" in person)    # True
print("phone" in person)   # False
print("Alice" in person)   # False! (checks keys, not values!)

# Check if value exists
print("Alice" in person.values())  # True
```

---

## ✏️ Modifying Dictionaries

```python
# ═══════════════════════════════════════════════════════════════
# ADDING AND UPDATING
# ═══════════════════════════════════════════════════════════════

person = {"name": "Alice", "age": 25}

# Add new key-value pair
person["city"] = "Berlin"
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'Berlin'}

# Update existing value
person["age"] = 26
print(person)  # {'name': 'Alice', 'age': 26, 'city': 'Berlin'}

# update() - merge dictionaries
person.update({"phone": "123", "email": "a@b.com"})
# Also: person |= {"phone": "123"}  (Python 3.9+)

# setdefault() - add only if key doesn't exist
person.setdefault("age", 100)   # Returns 26 (already exists)
person.setdefault("country", "Germany")  # Adds new key

# ═══════════════════════════════════════════════════════════════
# REMOVING
# ═══════════════════════════════════════════════════════════════

person = {"name": "Alice", "age": 25, "city": "Berlin"}

# del - remove by key
del person["city"]
print(person)  # {'name': 'Alice', 'age': 25}
# del person["xyz"]  # KeyError!

# pop() - remove and return value
age = person.pop("age")
print(age)     # 25
print(person)  # {'name': 'Alice'}

# pop() with default (no error if missing)
phone = person.pop("phone", "N/A")
print(phone)   # N/A

# popitem() - remove and return last inserted pair
person = {"a": 1, "b": 2, "c": 3}
item = person.popitem()
print(item)    # ('c', 3)
print(person)  # {'a': 1, 'b': 2}

# clear() - remove all
person.clear()
print(person)  # {}
```

---

## 🔄 Iterating Over Dictionaries

```python
# ═══════════════════════════════════════════════════════════════
# DICTIONARY ITERATION
# ═══════════════════════════════════════════════════════════════

person = {"name": "Alice", "age": 25, "city": "Berlin"}

# Iterate over keys (default)
for key in person:
    print(key)
# name, age, city

# Explicit keys()
for key in person.keys():
    print(key)

# Iterate over values
for value in person.values():
    print(value)
# Alice, 25, Berlin

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
# name: Alice
# age: 25
# city: Berlin

# Get all as lists
print(list(person.keys()))    # ['name', 'age', 'city']
print(list(person.values()))  # ['Alice', 25, 'Berlin']
print(list(person.items()))   # [('name', 'Alice'), ...]
```

---

## 🔧 Dictionary Methods

```python
# ═══════════════════════════════════════════════════════════════
# DICTIONARY METHODS
# ═══════════════════════════════════════════════════════════════

d = {"a": 1, "b": 2, "c": 3}

# get(key, default) - safe access
print(d.get("a"))           # 1
print(d.get("z"))           # None
print(d.get("z", 0))        # 0

# keys(), values(), items()
print(d.keys())    # dict_keys(['a', 'b', 'c'])
print(d.values())  # dict_values([1, 2, 3])
print(d.items())   # dict_items([('a', 1), ('b', 2), ('c', 3)])

# setdefault(key, default) - get or set
d.setdefault("d", 4)  # Adds d:4, returns 4
d.setdefault("a", 99) # Returns 1 (already exists)

# update(dict/pairs) - merge
d.update({"e": 5, "f": 6})
d.update([("g", 7)])  # From pairs

# pop(key, default) - remove and return
val = d.pop("a")       # Returns 1, removes key
val = d.pop("z", 0)    # Returns 0 (default)

# popitem() - remove last item
key, val = d.popitem()

# clear() - remove all
d.clear()

# copy() - shallow copy
d = {"a": 1, "b": 2}
d2 = d.copy()
```

---

## 📊 Dictionary Comprehensions

```python
# ═══════════════════════════════════════════════════════════════
# DICTIONARY COMPREHENSIONS
# ═══════════════════════════════════════════════════════════════

# Basic: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}

# Swap keys and values
original = {"a": 1, "b": 2}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b'}

# Transform keys/values
d = {"Name": "ALICE", "City": "BERLIN"}
lower = {k.lower(): v.lower() for k, v in d.items()}
print(lower)  # {'name': 'alice', 'city': 'berlin'}
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: {} creates empty dict, not set!
empty = {}
print(type(empty))  # <class 'dict'>
# Use set() for empty set

# TRAP 2: in checks KEYS, not values!
d = {"name": "Alice", "age": 25}
print("name" in d)   # True (key)
print("Alice" in d)  # False! (value, not key)
print("Alice" in d.values())  # True

# TRAP 3: KeyError when accessing missing key
d = {"a": 1}
# print(d["b"])  # KeyError!
print(d.get("b"))  # None (safe)

# TRAP 4: Modifying while iterating
d = {"a": 1, "b": 2, "c": 3}
# for key in d:
#     del d[key]  # RuntimeError!

# FIX: Iterate over copy
for key in list(d.keys()):
    del d[key]

# TRAP 5: Keys must be hashable
# d = {[1, 2]: "value"}  # TypeError! List not hashable
d = {(1, 2): "value"}    # OK - tuple is hashable

# TRAP 6: pop() vs get()
d = {"a": 1}
d.get("b")      # Returns None, doesn't modify dict
d.pop("b", None)  # Returns None, doesn't modify dict
# d.pop("b")    # KeyError! (no default)

# TRAP 7: dict ordering
# Python 3.7+: dictionaries maintain insertion order
d = {"c": 3, "a": 1, "b": 2}
print(list(d.keys()))  # ['c', 'a', 'b'] (insertion order)

# TRAP 8: copy() is shallow
d = {"a": [1, 2, 3]}
d2 = d.copy()
d2["a"].append(4)
print(d)  # {'a': [1, 2, 3, 4]} - original modified!
```

---

## 📝 Quick Reference

| Method | Description | Example |
|--------|-------------|---------|
| `d[key]` | Get value (KeyError if missing) | `d["name"]` |
| `d.get(key, default)` | Safe get | `d.get("x", 0)` |
| `d[key] = value` | Set value | `d["age"] = 25` |
| `del d[key]` | Delete key | `del d["age"]` |
| `d.pop(key, default)` | Remove & return | `d.pop("age")` |
| `d.keys()` | All keys | `list(d.keys())` |
| `d.values()` | All values | `list(d.values())` |
| `d.items()` | All pairs | `list(d.items())` |
| `key in d` | Check key exists | `"name" in d` |
| `d.update(dict2)` | Merge | `d.update({"x": 1})` |
| `d.setdefault(k, v)` | Get or set | `d.setdefault("x", 0)` |

---

## 🎯 Exam Checklist

- [ ] Dictionaries store key-value pairs
- [ ] Keys must be unique and hashable (immutable)
- [ ] {} creates empty dict (not set!)
- [ ] `in` checks keys, not values
- [ ] Use get() for safe access
- [ ] KeyError if accessing missing key with []
- [ ] Python 3.7+ maintains insertion order
- [ ] Don't modify dict while iterating
- [ ] copy() creates shallow copy

---

[[11_Tuples|← Tuples]] | [[00_Index|Index]] | [[13_Functions_Basics|Functions →]]
