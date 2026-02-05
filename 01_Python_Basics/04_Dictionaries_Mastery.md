---
title: Dictionaries Mastery
category: fundamentals
tags: ['python', 'dictionaries', 'data-structures', 'core', 'key-value']
created: 2026-01-27
type: topic
---

# Dictionaries Mastery

[[00_Index|← Back to Index]]

> **Master Python's powerful key-value data structure**

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║         📖 DICTIONARY - KEY:VALUE PAIRS                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   student = {"name": "Alice", "age": 25, "grade": "A"}       ║
║                                                               ║
║   ┌────────────┬──────────┬──────────────┬────────┬────────┐ ║
║   │   KEY      │  KEY     │    KEY       │  KEY   │ VALUE  │ ║
║   ├────────────┼──────────┼──────────────┼────────┼────────┤ ║
║   │   "name"   │  "age"   │   "grade"    │ VALUE  │        │ ║
║   │   ↓        │   ↓      │   ↓          │        │        │ ║
║   │  "Alice"   │  25      │   "A"        │        │        │ ║
║   └────────────┴──────────┴──────────────┴────────┴────────┘ ║
║                                                               ║
║   Access values (O(1) speed):                                ║
║   student["name"]  → "Alice"                                  ║
║   student["age"]   → 25                                       ║
║   student.get("grade")  → "A" (with fallback possible)       ║
║                                                               ║
║   Modifications:                                              ║
║   • student["gpa"] = 3.9  (New key)                          ║
║   • student["age"] = 26   (Update value)                     ║
║   • del student["grade"]  (Delete key)                       ║
║                                                               ║
║   💡 Dictionary = Fast access to values via keys             ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📖 What is a Dictionary?

A **dictionary** is an unordered collection of key-value pairs with fast O(1) lookup.

**Key Characteristics:**
- ✅ **Unordered** (but insertion order preserved in Python 3.7+)
- ✅ **Mutable** - can add/remove/modify items
- ✅ **Key-value pairs** - access values by keys
- ✅ **Keys must be unique** and hashable (immutable)
- ✅ **Values can be any type** (including other dicts)

**Syntax:**
```python
my_dict = {'key': 'value'}
```

---

## 🏗️ Creating Dictionaries

### Empty Dictionary

```python
# Method 1: Curly braces
empty_dict = {}

# Method 2: dict() constructor
empty_dict = dict()
```

### Dictionary with Values

```python
# Simple dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'country': 'USA'
}

# Complex dictionary with different types
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Using dict() constructor
person = dict(
    first_name='Jane',
    last_name='Smith',
    age=25
)
```

### Dictionary Length

```python
person = {
    'first_name': 'John',
    'age': 30,
    'country': 'USA'
}

length = len(person)
print(length)  # 3
```

---

## 🔍 Accessing Items

### Using Square Brackets

```python
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript'],
    'address': {
        'street': 'Main St',
        'zipcode': '12345'
    }
}

# Access values
print(person['first_name'])  # John
print(person['age'])         # 30

# Access nested values
print(person['skills'][0])          # Python
print(person['address']['street'])  # Main St

# KeyError if key doesn't exist
# print(person['city'])  # KeyError!
```

### Using get() Method (Safe)

```python
# get() returns None if key doesn't exist
print(person.get('first_name'))  # John
print(person.get('city'))        # None

# With default value
print(person.get('city', 'Unknown'))  # Unknown
```

---

## ➕ Adding Items

```python
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Add new key-value pair
person['email'] = 'john@example.com'
person['job_title'] = 'Developer'

print(person)
# {
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 30,
#     'email': 'john@example.com',
#     'job_title': 'Developer'
# }

# Add to nested list
person['skills'] = []
person['skills'].append('Python')
```

---

## ✏️ Modifying Items

```python
person = {
    'first_name': 'John',
    'age': 30
}

# Modify existing value
person['first_name'] = 'Jane'
person['age'] = 31

print(person)  # {'first_name': 'Jane', 'age': 31}

# Update multiple items
person.update({
    'age': 32,
    'city': 'NYC'
})
```

---

## 🗑️ Removing Items

### pop() - Remove and Return Value

```python
person = {
    'first_name': 'John',
    'age': 30,
    'city': 'NYC'
}

# Remove and get value
age = person.pop('age')
print(age)     # 30
print(person)  # {'first_name': 'John', 'city': 'NYC'}

# With default if key doesn't exist
email = person.pop('email', 'not found')
print(email)  # not found
```

### popitem() - Remove Last Item

```python
person = {'first_name': 'John', 'age': 30}

# Remove last item (returns key-value tuple)
item = person.popitem()
print(item)    # ('age', 30)
print(person)  # {'first_name': 'John'}
```

### del - Remove by Key

```python
person = {'first_name': 'John', 'age': 30, 'city': 'NYC'}

# Delete specific item
del person['age']
print(person)  # {'first_name': 'John', 'city': 'NYC'}

# Delete entire dictionary
# del person
```

### clear() - Remove All Items

```python
person = {'first_name': 'John', 'age': 30}

person.clear()
print(person)  # {}
```

---

## ✅ Checking Keys

```python
person = {
    'first_name': 'John',
    'age': 30
}

# Check if key exists
print('first_name' in person)  # True
print('email' in person)        # False

# Check before accessing
if 'email' in person:
    print(person['email'])
else:
    print('Email not found')
```

---

## 🔄 Iterating Dictionaries

### Iterate Keys

```python
person = {'first_name': 'John', 'age': 30, 'city': 'NYC'}

# Default: iterate keys
for key in person:
    print(key)
# first_name
# age
# city

# Explicit keys()
for key in person.keys():
    print(key)
```

### Iterate Values

```python
# Get all values
for value in person.values():
    print(value)
# John
# 30
# NYC
```

### Iterate Key-Value Pairs

```python
# items() returns tuples of (key, value)
for key, value in person.items():
    print(f"{key}: {value}")
# first_name: John
# age: 30
# city: NYC
```

---

## 📋 Dictionary Methods

### keys(), values(), items()

```python
person = {'name': 'John', 'age': 30, 'city': 'NYC'}

# Get all keys
keys = person.keys()
print(list(keys))  # ['name', 'age', 'city']

# Get all values
values = person.values()
print(list(values))  # ['John', 30, 'NYC']

# Get all items
items = person.items()
print(list(items))  
# [('name', 'John'), ('age', 30), ('city', 'NYC')]
```

### copy()

```python
person = {'name': 'John', 'age': 30}

# Shallow copy
person_copy = person.copy()

# Modify copy doesn't affect original
person_copy['age'] = 31
print(person['age'])       # 30
print(person_copy['age'])  # 31
```

### setdefault()

```python
person = {'name': 'John'}

# Get value or set default if key doesn't exist
age = person.setdefault('age', 30)
print(age)     # 30
print(person)  # {'name': 'John', 'age': 30}

# If key exists, return existing value
name = person.setdefault('name', 'Jane')
print(name)  # John (not Jane!)
```

---

## 🎨 Dictionary Comprehension

```python
# Create dict from range
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From lists
keys = ['name', 'age', 'city']
values = ['John', 30, 'NYC']
person = {k: v for k, v in zip(keys, values)}
print(person)  # {'name': 'John', 'age': 30, 'city': 'NYC'}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

## 🔗 Merging Dictionaries

### update() Method

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Overlapping keys: dict2 wins
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}
```

### Union Operator | (Python 3.9+)

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged = dict1 | dict2
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### Unpacking **

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

---

## 💡 Practical Examples

### Word Counter

```python
text = "hello world hello python world"
words = text.split()

# Count word occurrences
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# {'hello': 2, 'world': 2, 'python': 1}

# Using setdefault
word_count = {}
for word in words:
    word_count.setdefault(word, 0)
    word_count[word] += 1
```

### Group by Property

```python
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 25}
]

# Group by age
by_age = {}
for person in people:
    age = person['age']
    if age not in by_age:
        by_age[age] = []
    by_age[age].append(person['name'])

print(by_age)
# {25: ['Alice', 'Charlie'], 30: ['Bob']}
```

### Invert Dictionary

```python
original = {'a': 1, 'b': 2, 'c': 3}

# Swap keys and values
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

---

## ✅ Best Practices

### 1. Use get() for Safe Access

```python
# Bad
if 'key' in my_dict:
    value = my_dict['key']
else:
    value = 'default'

# Good
value = my_dict.get('key', 'default')
```

### 2. Use setdefault() for Initialization

```python
# Bad
if key not in my_dict:
    my_dict[key] = []
my_dict[key].append(value)

# Good
my_dict.setdefault(key, []).append(value)
```

### 3. Use items() for Key-Value Iteration

```python
# Bad
for key in my_dict:
    value = my_dict[key]
    print(key, value)

# Good
for key, value in my_dict.items():
    print(key, value)
```

### 4. Keys Must Be Hashable

```python
# ✅ Valid keys
valid_dict = {
    'string': 1,
    42: 2,
    (1, 2): 3,  # Tuple is hashable
    True: 4
}

# ❌ Invalid keys
# invalid = {[1, 2]: 'value'}  # TypeError: list not hashable
# invalid = {{}: 'value'}       # TypeError: dict not hashable
```

---

## 🎓 Summary

**Dictionaries:**
- Key-value pairs with O(1) lookup
- Keys must be unique and hashable
- Values can be any type
- Mutable (can add/remove/modify)

**Key Methods:**
- `get()` - safe access
- `pop()` - remove and return
- `update()` - merge dicts
- `items()` - iterate pairs

**Key Takeaway:** Dictionaries are Python's fastest lookup data structure!

---

## 🔗 Related Topics

- [[02_Lists_Deep_Dive|Lists]]
- [[03_Tuples_and_Sets|Tuples & Sets]]

---

[[00_Index|← Back to Index]]

*Key-value power! 🗝️*

✅ Use `.get()` instead of `[]` to avoid KeyError
✅ Check `if key in dict` before accessing
✅ Use dict comprehensions for transformations
✅ Use `.items()` to iterate over key-value pairs
✅ Remember: keys must be immutable (str, int, tuple)
❌ Don't use mutable objects (lists, dicts) as keys

---

## 🎓 Exam Practice

**Q: What's the output?**
```python
d = {"a": 1}
print(d.get("b", 0))
```
Answer: `0` (get returns default if key not found)

---

[[00_Index|← Back to Index]]
