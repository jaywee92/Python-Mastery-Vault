---
title: Data Types
tags: [pcep, python, types, int, float, str, bool, conversion]
created: 2026-01-30
exam_section: 1
exam_weight: 8%
---

# 📊 Data Types

[[00_Index|← Back to Index]] | [[04_Operators|← Operators]] | [[06_Input_Output|I/O →]]

> **"Know type conversions - they're tested frequently!"**

---

## 🎯 Python's Built-in Types

```
┌─────────────────────────────────────────────────────────────────┐
│              PYTHON DATA TYPES                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  NUMERIC TYPES:                                                 │
│    int    - Integer (whole numbers)                            │
│    float  - Floating point (decimals)                          │
│    complex - Complex numbers (rarely tested)                   │
│                                                                  │
│  SEQUENCE TYPES:                                                │
│    str    - String (immutable)                                 │
│    list   - List (mutable)                                     │
│    tuple  - Tuple (immutable)                                  │
│                                                                  │
│  MAPPING TYPE:                                                  │
│    dict   - Dictionary (key-value pairs)                       │
│                                                                  │
│  SET TYPES:                                                     │
│    set    - Set (mutable, unique elements)                     │
│    frozenset - Frozen set (immutable)                          │
│                                                                  │
│  BOOLEAN TYPE:                                                  │
│    bool   - Boolean (True/False)                               │
│                                                                  │
│  NONE TYPE:                                                     │
│    NoneType - Represents absence of value                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔢 Numeric Types

```python
# ═══════════════════════════════════════════════════════════════
# INTEGER (int)
# ═══════════════════════════════════════════════════════════════

x = 42
y = -17
z = 0

# No size limit!
big = 12345678901234567890123456789

print(type(x))  # <class 'int'>

# Integer operations
print(10 + 3)   # 13 (int)
print(10 - 3)   # 7 (int)
print(10 * 3)   # 30 (int)
print(10 // 3)  # 3 (int) - floor division
print(10 % 3)   # 1 (int) - modulo
print(10 ** 3)  # 1000 (int) - power

# Division ALWAYS returns float!
print(10 / 2)   # 5.0 (float!)

# ═══════════════════════════════════════════════════════════════
# FLOAT
# ═══════════════════════════════════════════════════════════════

a = 3.14
b = -0.001
c = 2.0        # Still float!
d = 3e2        # 300.0 (scientific notation)

print(type(a))  # <class 'float'>

# Float precision issues!
print(0.1 + 0.2)        # 0.30000000000000004
print(0.1 + 0.2 == 0.3) # False!

# ═══════════════════════════════════════════════════════════════
# BOOLEAN (bool)
# ═══════════════════════════════════════════════════════════════

t = True
f = False

print(type(t))  # <class 'bool'>

# Bool is subclass of int!
print(True + True)   # 2
print(True * 10)     # 10
print(False + 5)     # 5
print(isinstance(True, int))  # True
```

---

## 📝 String Type

```python
# ═══════════════════════════════════════════════════════════════
# STRING (str)
# ═══════════════════════════════════════════════════════════════

s1 = 'hello'
s2 = "hello"
s3 = '''multi
line'''

print(type(s1))  # <class 'str'>

# Strings are IMMUTABLE
s = "hello"
# s[0] = "H"  # TypeError!
s = "Hello"   # Creates new string (ok)

# String operations
print(len("hello"))      # 5
print("hello"[0])        # h
print("hello"[-1])       # o
print("hello"[1:4])      # ell
print("hello" + "world") # helloworld
print("ha" * 3)          # hahaha

# String methods
print("hello".upper())      # HELLO
print("HELLO".lower())      # hello
print("  hi  ".strip())     # hi
print("hello".replace("l", "L"))  # heLLo
print("a,b,c".split(","))   # ['a', 'b', 'c']
```

---

## 🔄 Type Conversion (CRITICAL!)

```
┌─────────────────────────────────────────────────────────────────┐
│              TYPE CONVERSION                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  EXPLICIT CONVERSION (Casting):                                 │
│    int()   - Convert to integer                                │
│    float() - Convert to float                                  │
│    str()   - Convert to string                                 │
│    bool()  - Convert to boolean                                │
│    list()  - Convert to list                                   │
│    tuple() - Convert to tuple                                  │
│                                                                  │
│  IMPLICIT CONVERSION (Automatic):                               │
│    int + float → float                                         │
│    bool + int → int                                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# int() CONVERSION
# ═══════════════════════════════════════════════════════════════

print(int(3.7))      # 3 (truncates, not rounds!)
print(int(3.2))      # 3
print(int(-3.7))     # -3 (toward zero)
print(int("42"))     # 42
print(int("  42  ")) # 42 (strips whitespace)
print(int(True))     # 1
print(int(False))    # 0

# int() with base
print(int("FF", 16))  # 255 (hexadecimal)
print(int("17", 8))   # 15 (octal)
print(int("1010", 2)) # 10 (binary)

# Errors:
# int("3.14")      # ValueError! (float string)
# int("hello")     # ValueError!
# int("")          # ValueError!

# ═══════════════════════════════════════════════════════════════
# float() CONVERSION
# ═══════════════════════════════════════════════════════════════

print(float(42))      # 42.0
print(float("3.14"))  # 3.14
print(float("42"))    # 42.0
print(float("3e2"))   # 300.0
print(float(True))    # 1.0
print(float(False))   # 0.0

# Special values
print(float("inf"))   # inf
print(float("-inf"))  # -inf

# Errors:
# float("hello")    # ValueError!

# ═══════════════════════════════════════════════════════════════
# str() CONVERSION
# ═══════════════════════════════════════════════════════════════

print(str(42))        # "42"
print(str(3.14))      # "3.14"
print(str(True))      # "True"
print(str(False))     # "False"
print(str(None))      # "None"
print(str([1,2,3]))   # "[1, 2, 3]"

# ═══════════════════════════════════════════════════════════════
# bool() CONVERSION (Truthiness)
# ═══════════════════════════════════════════════════════════════

# FALSY values (evaluate to False):
print(bool(0))        # False
print(bool(0.0))      # False
print(bool(""))       # False (empty string)
print(bool([]))       # False (empty list)
print(bool(()))       # False (empty tuple)
print(bool({}))       # False (empty dict)
print(bool(None))     # False

# TRUTHY values (evaluate to True):
print(bool(1))        # True
print(bool(-1))       # True (any non-zero!)
print(bool(3.14))     # True
print(bool("hello"))  # True
print(bool(" "))      # True (space is a character!)
print(bool([0]))      # True (has one element!)
print(bool("False"))  # True (non-empty string!)
```

---

## 📊 type() and isinstance()

```python
# ═══════════════════════════════════════════════════════════════
# CHECKING TYPES
# ═══════════════════════════════════════════════════════════════

x = 42
print(type(x))              # <class 'int'>
print(type(x) == int)       # True

# isinstance() is more flexible (checks inheritance)
print(isinstance(42, int))       # True
print(isinstance(3.14, float))   # True
print(isinstance("hi", str))     # True
print(isinstance(True, int))     # True! (bool is subclass of int)
print(isinstance(True, bool))    # True

# Check multiple types
print(isinstance(42, (int, float)))  # True
print(isinstance(3.14, (int, float)))  # True
```

---

## 🔀 Implicit Type Conversion

```python
# ═══════════════════════════════════════════════════════════════
# IMPLICIT (AUTOMATIC) CONVERSION
# ═══════════════════════════════════════════════════════════════

# int + float → float
print(5 + 3.0)     # 8.0 (float)
print(type(5 + 3.0))  # <class 'float'>

# bool + int → int
print(True + 5)    # 6 (int)
print(False + 5)   # 5 (int)

# bool + float → float
print(True + 3.14) # 4.14 (float)

# NO implicit conversion with strings!
# print("5" + 3)   # TypeError!
# print(5 + "3")   # TypeError!
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: int() truncates, doesn't round
print(int(3.9))   # 3 (not 4!)
print(int(-3.9))  # -3 (not -4!)

# TRAP 2: Can't convert float string to int directly
# print(int("3.14"))  # ValueError!
print(int(float("3.14")))  # 3 (convert to float first)

# TRAP 3: Empty string is falsy, but "0" is truthy
print(bool(""))    # False
print(bool("0"))   # True (non-empty string!)
print(bool("False"))  # True!

# TRAP 4: [0] is truthy (has one element)
print(bool([0]))   # True
print(bool([]))    # False

# TRAP 5: True is 1, False is 0
print(True == 1)   # True
print(False == 0)  # True
print(True + True + True)  # 3

# TRAP 6: Division always returns float
print(10 / 2)      # 5.0 (not 5!)
print(type(10/2))  # <class 'float'>

# TRAP 7: type() vs isinstance() with bools
print(type(True) == int)      # False (type is bool)
print(isinstance(True, int))  # True (bool is subclass of int)
```

---

## 📝 Quick Reference

| Function | Description | Example |
|----------|-------------|---------|
| `int(x)` | Convert to integer | `int("42")` → `42` |
| `float(x)` | Convert to float | `float("3.14")` → `3.14` |
| `str(x)` | Convert to string | `str(42)` → `"42"` |
| `bool(x)` | Convert to boolean | `bool(0)` → `False` |
| `type(x)` | Get type | `type(42)` → `<class 'int'>` |
| `isinstance(x, T)` | Check type | `isinstance(42, int)` → `True` |

---

## 🎯 Exam Checklist

- [ ] int() truncates (toward zero)
- [ ] float() always creates float
- [ ] str() works on everything
- [ ] Falsy: 0, 0.0, "", [], {}, (), None
- [ ] Truthy: non-zero, non-empty
- [ ] "False" and "0" are truthy (non-empty strings!)
- [ ] Division (/) always returns float
- [ ] bool is subclass of int (True=1, False=0)
- [ ] type() returns exact type
- [ ] isinstance() checks inheritance

---

[[04_Operators|← Operators]] | [[00_Index|Index]] | [[06_Input_Output|I/O →]]
