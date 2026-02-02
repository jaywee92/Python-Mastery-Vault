---
title: Python Basics - Cheatsheet
tags: [python, basics, cheatsheet, reference]
created: 2026-02-01
---

# 🐍 Python Basics - Cheatsheet

---

## 📊 Data Types

| Type | Example | Mutable | Description |
|------|---------|---------|-------------|
| `int` | `42`, `-7` | ❌ | Whole numbers |
| `float` | `3.14`, `2.0` | ❌ | Decimal numbers |
| `str` | `"hello"` | ❌ | Text |
| `bool` | `True`, `False` | ❌ | Boolean |
| `list` | `[1, 2, 3]` | ✅ | Ordered, changeable |
| `tuple` | `(1, 2, 3)` | ❌ | Ordered, unchangeable |
| `dict` | `{"a": 1}` | ✅ | Key-value pairs |
| `set` | `{1, 2, 3}` | ✅ | Unique values |
| `None` | `None` | ❌ | No value |

---

## ➕ Operators

```python
# Arithmetic
+   # Addition
-   # Subtraction
*   # Multiplication
/   # Division (always float!)
//  # Floor division
%   # Modulo
**  # Power

# Comparison
==  # Equal
!=  # Not equal
<   # Less than
>   # Greater than
<=  # Less or equal
>=  # Greater or equal

# Logical
and  # Both true
or   # At least one true
not  # Invert

# Identity & Membership
is      # Same object
is not  # Different object
in      # In sequence
not in  # Not in sequence
```

---

## 🔄 Type Conversion

```python
int("42")      # → 42
int(3.7)       # → 3 (truncates!)
float("3.14")  # → 3.14
str(42)        # → "42"
bool(0)        # → False
bool("")       # → False
bool([])       # → False
list("abc")    # → ['a', 'b', 'c']
tuple([1,2])   # → (1, 2)
```

---

## 📝 Strings

```python
s = "Hello World"

# Indexing & Slicing
s[0]       # 'H' (first)
s[-1]      # 'd' (last)
s[0:5]     # 'Hello'
s[6:]      # 'World'
s[::-1]    # Reverse

# Common Methods
s.upper()         # 'HELLO WORLD'
s.lower()         # 'hello world'
s.strip()         # Remove whitespace
s.split(" ")      # ['Hello', 'World']
s.replace("l","L") # 'HeLLo WorLd'
s.find("o")       # 4 (-1 if not found)
s.count("l")      # 3
len(s)            # 11

# f-strings
name = "Alice"
f"Hello, {name}!"  # "Hello, Alice!"
```

---

## 📋 Lists

```python
lst = [1, 2, 3, 4, 5]

# Access
lst[0]       # 1
lst[-1]      # 5
lst[1:3]     # [2, 3]

# Modify
lst.append(6)       # Add to end
lst.extend([7,8])   # Add multiple
lst.insert(0, 0)    # Insert at index
lst.remove(3)       # Remove by value
lst.pop()           # Remove & return last
lst.pop(0)          # Remove & return at index

# Other
lst.sort()          # Sort in place (returns None!)
lst.reverse()       # Reverse in place
sorted(lst)         # Return new sorted list
len(lst)            # Length
lst.index(2)        # Find index
lst.count(2)        # Count occurrences
```

---

## 📖 Dictionaries

```python
d = {"name": "Alice", "age": 25}

# Access
d["name"]           # "Alice"
d.get("name")       # "Alice" (safe)
d.get("x", "N/A")   # "N/A" (default)

# Modify
d["city"] = "Berlin"  # Add/update
del d["age"]          # Delete
d.pop("name")         # Remove & return

# Iterate
d.keys()      # dict_keys(['name', 'age'])
d.values()    # dict_values(['Alice', 25])
d.items()     # dict_items([('name','Alice')...])

# Check
"name" in d   # True (checks keys!)
```

---

## 🔁 Control Flow

```python
# If-Elif-Else
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# For Loop
for i in range(5):     # 0,1,2,3,4
    print(i)

for item in [1,2,3]:
    print(item)

# While Loop
while condition:
    do_something()

# Loop Control
break      # Exit loop
continue   # Skip to next iteration
```

---

## 🔧 Functions

```python
# Definition
def greet(name, greeting="Hello"):
    """Docstring: explains function"""
    return f"{greeting}, {name}!"

# Call
greet("Alice")           # "Hello, Alice!"
greet("Bob", "Hi")       # "Hi, Bob!"
greet(greeting="Hey", name="Charlie")

# Lambda
double = lambda x: x * 2
double(5)  # 10

# Args & Kwargs
def func(*args, **kwargs):
    print(args)    # tuple
    print(kwargs)  # dict
```

---

## ⚠️ Exception Handling

```python
try:
    risky_code()
except ValueError:
    handle_value_error()
except (TypeError, KeyError) as e:
    print(f"Error: {e}")
except:
    handle_any_error()
else:
    runs_if_no_exception()
finally:
    always_runs()

# Raise
raise ValueError("message")
```

---

## 📂 File Operations

```python
# Read
with open("file.txt", "r") as f:
    content = f.read()

# Write
with open("file.txt", "w") as f:
    f.write("Hello")

# Append
with open("file.txt", "a") as f:
    f.write("More text")
```

---

## 🎯 Quick Tips

- `10 / 2 = 5.0` (division returns float!)
- `int(3.9) = 3` (truncates, doesn't round)
- `range(5)` → 0,1,2,3,4 (stop is exclusive)
- `in` for dicts checks keys, not values
- `sort()` returns None, modifies in place
- `sorted()` returns new list
- Strings are immutable!
- Empty collections are falsy: `[]`, `{}`, `""`, `()`

---

[[00_Index|← Back to Index]]
