---
title: Quick Reference Card
tags: [pcep, python, reference, cheatsheet]
created: 2026-01-30
---

# 📋 PCEP Quick Reference Card

[[00_Index|← Back to Index]] | [[19_Common_Mistakes|Common Mistakes →]]

> **"Print this and keep it handy for review!"**

---

## 🔢 Operators Precedence (High to Low)

```
()              Parentheses
**              Exponentiation (right-to-left!)
+x -x ~x        Unary
* / // %        Multiplication, Division
+ -             Addition, Subtraction
<< >>           Bitwise shifts
&               Bitwise AND
^               Bitwise XOR
|               Bitwise OR
== != < <= > >= is in    Comparisons
not             Logical NOT
and             Logical AND
or              Logical OR
```

---

## 📊 Data Types

| Type | Mutable | Example | Falsy Value |
|------|---------|---------|-------------|
| `int` | No | `42` | `0` |
| `float` | No | `3.14` | `0.0` |
| `str` | No | `"hello"` | `""` |
| `bool` | No | `True/False` | `False` |
| `list` | **Yes** | `[1, 2, 3]` | `[]` |
| `tuple` | No | `(1, 2, 3)` | `()` |
| `dict` | **Yes** | `{"a": 1}` | `{}` |
| `set` | **Yes** | `{1, 2, 3}` | `set()` |
| `NoneType` | No | `None` | `None` |

---

## 🔄 Type Conversions

```python
int("42")       # 42
int(3.7)        # 3 (truncates!)
float("3.14")   # 3.14
str(42)         # "42"
bool(0)         # False
bool("")        # False
bool([])        # False
bool("0")       # True (non-empty string!)
bool([0])       # True (has one element!)
list("abc")     # ['a', 'b', 'c']
tuple([1,2])    # (1, 2)
```

---

## 📝 String Methods (Most Common)

```python
s.upper()           # HELLO
s.lower()           # hello
s.strip()           # Remove whitespace
s.split(",")        # Split by delimiter → list
s.join(list)        # Join list → string
s.replace(a, b)     # Replace a with b
s.find(x)           # Index of x (-1 if not found)
s.index(x)          # Index of x (ValueError if not found!)
s.count(x)          # Count occurrences
s.startswith(x)     # True/False
s.endswith(x)       # True/False
s.isdigit()         # All digits?
s.isalpha()         # All letters?
s.isalnum()         # All alphanumeric?
len(s)              # Length
```

---

## 📋 List Methods

```python
lst.append(x)       # Add to end (one item)
lst.extend(iter)    # Add multiple items
lst.insert(i, x)    # Insert at index
lst.remove(x)       # Remove first x (ValueError if not found)
lst.pop()           # Remove & return last
lst.pop(i)          # Remove & return at index
lst.index(x)        # Find index of x
lst.count(x)        # Count occurrences
lst.sort()          # Sort in place (returns None!)
lst.reverse()       # Reverse in place
lst.copy()          # Shallow copy
lst.clear()         # Remove all
```

---

## 📖 Dictionary Methods

```python
d[key]              # Get value (KeyError if missing!)
d.get(key)          # Get value (None if missing)
d.get(key, default) # Get value (default if missing)
d.keys()            # All keys
d.values()          # All values
d.items()           # All (key, value) pairs
d.pop(key)          # Remove & return value
d.update(dict2)     # Merge dictionaries
d.setdefault(k, v)  # Get or set default
key in d            # Check if KEY exists
```

---

## 🔁 Loop Patterns

```python
# Range
range(5)            # 0, 1, 2, 3, 4
range(1, 6)         # 1, 2, 3, 4, 5
range(0, 10, 2)     # 0, 2, 4, 6, 8
range(5, 0, -1)     # 5, 4, 3, 2, 1

# Enumerate
for i, val in enumerate(lst):
    print(i, val)

# Zip
for a, b in zip(list1, list2):
    print(a, b)

# Loop else (runs if no break)
for x in items:
    if condition:
        break
else:
    print("No break occurred")
```

---

## 🔧 Functions

```python
# Definition
def func(a, b=10, *args, **kwargs):
    return result

# Lambda
lambda x: x * 2

# Parameter order:
# positional → *args → keyword → **kwargs

# Unpacking
func(*list)         # Unpack list as positional args
func(**dict)        # Unpack dict as keyword args
```

---

## ⚠️ Exception Handling

```python
try:
    risky_code()
except ValueError:
    handle_error()
except (TypeError, KeyError) as e:
    print(e)
else:
    runs_if_no_exception()
finally:
    always_runs()

raise ValueError("message")  # Raise exception
```

---

## 🎯 Critical Exam Facts

### Division
- `/` ALWAYS returns float: `10 / 2 = 5.0`
- `//` floor division: `7 // 2 = 3`, `-7 // 2 = -4`

### Slicing
- `s[start:stop:step]` - stop is EXCLUSIVE
- `s[::-1]` reverses
- Slicing never raises IndexError

### Booleans
- `True == 1`, `False == 0`
- `True + True = 2`

### Lists vs Tuples
- Lists: `[1, 2, 3]` - mutable
- Tuples: `(1, 2, 3)` - immutable
- Single tuple: `(1,)` - comma required!

### Copying
- `lst2 = lst1` - same object!
- `lst2 = lst1[:]` - shallow copy
- `lst2 = lst1.copy()` - shallow copy

### Strings
- Immutable!
- `s.find(x)` returns -1 if not found
- `s.index(x)` raises ValueError if not found

### Dictionaries
- `in` checks KEYS, not values
- `{}` creates empty dict, not set!
- Keys must be hashable (immutable)

---

## 📐 Common Built-in Functions

```python
len(x)              # Length
type(x)             # Type
isinstance(x, T)    # Type check
abs(x)              # Absolute value
round(x, n)         # Round (banker's rounding!)
min(), max(), sum() # Aggregates
sorted(iter)        # Returns NEW sorted list
reversed(iter)      # Returns iterator
list(), tuple()     # Convert to type
input()             # ALWAYS returns string!
print(sep, end)     # Output with options
```

---

[[00_Index|← Index]] | [[19_Common_Mistakes|Common Mistakes →]]
