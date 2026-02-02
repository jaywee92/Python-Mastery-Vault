---
title: Strings (HEAVILY TESTED!)
tags: [pcep, python, strings, methods, slicing]
created: 2026-01-30
exam_section: 3
exam_weight: 10%
---

# 📝 Strings - CRITICAL EXAM TOPIC!

[[00_Index|← Back to Index]] | [[08_Loops|← Loops]] | [[10_Lists|Lists →]]

> **"Strings are tested heavily - know every method!"**

---

## ⚠️ EXAM ALERT: Strings are one of the MOST TESTED topics!

---

## 🎯 String Basics

```python
# ═══════════════════════════════════════════════════════════════
# STRING CREATION
# ═══════════════════════════════════════════════════════════════

# Single or double quotes (identical)
s1 = 'Hello'
s2 = "Hello"
print(s1 == s2)  # True

# Triple quotes (multiline strings)
s3 = '''This is
a multiline
string'''

s4 = """Also
multiline"""

# Empty string
empty = ""
print(len(empty))  # 0
print(bool(empty))  # False (empty string is falsy!)

# Strings are IMMUTABLE!
s = "Hello"
# s[0] = 'J'  # TypeError: strings don't support item assignment
s = "Jello"   # This creates a NEW string (reassignment is OK)
```

---

## 🔢 String Indexing (EXAM FAVORITE!)

```
┌─────────────────────────────────────────────────────────────────┐
│                    STRING INDEXING                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  String:    P   Y   T   H   O   N                               │
│             ↓   ↓   ↓   ↓   ↓   ↓                               │
│  Index:     0   1   2   3   4   5                               │
│  Negative: -6  -5  -4  -3  -2  -1                               │
│                                                                  │
│  s = "PYTHON"                                                   │
│  s[0]  → 'P'     (first character)                             │
│  s[5]  → 'N'     (last character)                              │
│  s[-1] → 'N'     (last character)                              │
│  s[-6] → 'P'     (first character)                             │
│  s[6]  → IndexError!                                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
s = "PYTHON"
print(s[0])    # P
print(s[-1])   # N
print(s[2])    # T
print(s[-2])   # O
# print(s[10])  # IndexError: string index out of range
```

---

## ✂️ String Slicing (MUST KNOW!)

```
┌─────────────────────────────────────────────────────────────────┐
│              SLICING SYNTAX: s[start:stop:step]                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  start: Where to begin (inclusive, default 0)                   │
│  stop:  Where to end (EXCLUSIVE, default len(s))               │
│  step:  How many to skip (default 1)                           │
│                                                                  │
│  s = "PYTHON"                                                   │
│       0 1 2 3 4 5                                               │
│                                                                  │
│  s[0:3]   → "PYT"    (index 0, 1, 2 - NOT 3!)                  │
│  s[2:5]   → "THO"                                               │
│  s[:3]    → "PYT"    (from start)                              │
│  s[3:]    → "HON"    (to end)                                  │
│  s[:]     → "PYTHON" (copy entire string)                      │
│  s[::2]   → "PTO"    (every 2nd character)                     │
│  s[::-1]  → "NOHTYP" (REVERSE!)                                │
│  s[1:5:2] → "YH"     (index 1 and 3)                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
s = "PYTHON"

# Basic slicing
print(s[0:3])    # PYT (chars at 0, 1, 2)
print(s[1:4])    # YTH
print(s[:3])     # PYT (same as s[0:3])
print(s[3:])     # HON (same as s[3:6])
print(s[:])      # PYTHON (full copy)

# With step
print(s[::2])    # PTO (every 2nd char)
print(s[1::2])   # YHN (starting at 1, every 2nd)

# REVERSE STRING (very common exam question!)
print(s[::-1])   # NOHTYP

# Negative indices in slicing
print(s[-3:])    # HON (last 3 chars)
print(s[:-3])    # PYT (all except last 3)
print(s[-4:-1])  # THO

# Out of range slicing is OK (no error!)
print(s[0:100])  # PYTHON (just goes to end)
print(s[100:])   # "" (empty string)
```

---

## 🔧 String Methods (MEMORIZE THESE!)

### Case Methods

```python
s = "Hello World"

print(s.upper())       # HELLO WORLD
print(s.lower())       # hello world
print(s.capitalize())  # Hello world (only first char)
print(s.title())       # Hello World (each word)
print(s.swapcase())    # hELLO wORLD

# Check case
print("HELLO".isupper())  # True
print("hello".islower())  # True
print("Hello".istitle())  # True
```

### Search Methods

```python
s = "Hello World"

# Find (returns index or -1)
print(s.find("o"))      # 4 (first occurrence)
print(s.find("o", 5))   # 7 (search from index 5)
print(s.find("xyz"))    # -1 (not found)
print(s.rfind("o"))     # 7 (last occurrence)

# Index (returns index or raises ValueError)
print(s.index("o"))     # 4
# print(s.index("xyz"))  # ValueError!

# Count occurrences
print(s.count("o"))     # 2
print(s.count("l"))     # 3

# Check start/end
print(s.startswith("Hello"))  # True
print(s.endswith("World"))    # True
print(s.startswith("H"))      # True

# Check if contains (use 'in' operator)
print("World" in s)     # True
print("xyz" in s)       # False
```

### Modification Methods (return NEW string!)

```python
s = "  Hello World  "

# Strip whitespace
print(s.strip())        # "Hello World"
print(s.lstrip())       # "Hello World  "
print(s.rstrip())       # "  Hello World"

# Strip specific chars
print("xxHelloxx".strip("x"))  # "Hello"

# Replace
s = "Hello World"
print(s.replace("World", "Python"))  # Hello Python
print(s.replace("l", "L"))           # HeLLo WorLd
print(s.replace("l", "L", 1))        # HeLlo World (only first)

# Split and Join
s = "apple,banana,cherry"
print(s.split(","))        # ['apple', 'banana', 'cherry']
print("Hello World".split())  # ['Hello', 'World'] (splits on whitespace)

fruits = ['apple', 'banana', 'cherry']
print(",".join(fruits))    # apple,banana,cherry
print(" ".join(fruits))    # apple banana cherry
print("".join(fruits))     # applebananacherry
```

### Validation Methods (return True/False)

```python
# Check content type
print("abc".isalpha())     # True (only letters)
print("123".isdigit())     # True (only digits)
print("abc123".isalnum())  # True (letters or digits)
print("   ".isspace())     # True (only whitespace)

# More checks
print("abc".islower())     # True
print("ABC".isupper())     # True
print("Hello World".istitle())  # True

# IMPORTANT: Empty string returns False for most is* methods!
print("".isalpha())        # False
print("".isdigit())        # False
```

---

## 🎨 String Formatting (EXAM TOPIC!)

```python
# ═══════════════════════════════════════════════════════════════
# STRING FORMATTING METHODS
# ═══════════════════════════════════════════════════════════════

name = "Alice"
age = 25

# Method 1: f-strings (Python 3.6+, RECOMMENDED)
print(f"Name: {name}, Age: {age}")
print(f"Next year: {age + 1}")

# Method 2: .format()
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# Method 3: % operator (old style)
print("Name: %s, Age: %d" % (name, age))

# Formatting numbers
pi = 3.14159
print(f"{pi:.2f}")         # 3.14 (2 decimal places)
print(f"{1000:,}")         # 1,000 (with comma)
print(f"{42:05d}")         # 00042 (zero-padded)
```

---

## 🔗 String Operators

```python
# ═══════════════════════════════════════════════════════════════
# STRING OPERATORS
# ═══════════════════════════════════════════════════════════════

# Concatenation (+)
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Hello World

# Repetition (*)
print("Ha" * 3)        # HaHaHa
print("-" * 10)        # ----------

# Membership (in / not in)
print("H" in "Hello")      # True
print("x" not in "Hello")  # True

# Comparison (lexicographic)
print("apple" < "banana")  # True (a < b)
print("Apple" < "apple")   # True (uppercase < lowercase)
print("abc" == "abc")      # True

# Length
print(len("Hello"))    # 5
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: Strings are IMMUTABLE
s = "Hello"
# s[0] = 'J'  # TypeError!
s = "J" + s[1:]  # OK, creates new string

# TRAP 2: Slicing never raises IndexError
s = "Hi"
print(s[100:])   # "" (empty, no error)
print(s[100])    # IndexError!

# TRAP 3: find() vs index()
s = "Hello"
print(s.find("x"))   # -1 (not found)
# print(s.index("x"))  # ValueError!

# TRAP 4: split() with no argument
print("a  b  c".split())    # ['a', 'b', 'c'] (any whitespace)
print("a  b  c".split(" ")) # ['a', '', 'b', '', 'c']

# TRAP 5: Empty string is falsy
print(bool(""))      # False
print(bool(" "))     # True (space is a character!)
print(bool("False")) # True (non-empty string)

# TRAP 6: String multiplication with 0 or negative
print("Ha" * 0)   # "" (empty string)
print("Ha" * -1)  # "" (empty string)
```

---

## 📝 Quick Reference Table

| Method | Returns | Example |
|--------|---------|---------|
| `upper()` | Uppercase string | `"hi".upper()` → `"HI"` |
| `lower()` | Lowercase string | `"HI".lower()` → `"hi"` |
| `strip()` | Trimmed string | `" hi ".strip()` → `"hi"` |
| `split()` | List of strings | `"a,b".split(",")` → `['a','b']` |
| `join()` | Joined string | `",".join(['a','b'])` → `"a,b"` |
| `find()` | Index or -1 | `"hi".find("i")` → `1` |
| `replace()` | New string | `"hi".replace("i","o")` → `"ho"` |
| `count()` | Count of substring | `"hello".count("l")` → `2` |
| `startswith()` | Boolean | `"hi".startswith("h")` → `True` |
| `isdigit()` | Boolean | `"123".isdigit()` → `True` |

---

## 🎯 Exam Checklist

- [ ] Indexing: s[0], s[-1], IndexError on invalid index
- [ ] Slicing: s[start:stop:step], stop is EXCLUSIVE
- [ ] Reverse: s[::-1]
- [ ] Immutable: can't modify, only create new
- [ ] find() returns -1, index() raises ValueError
- [ ] split() vs split(" ") behavior
- [ ] join() is called ON the separator
- [ ] Empty string is False, space is True

---

[[08_Loops|← Loops]] | [[00_Index|Index]] | [[10_Lists|Lists →]]
