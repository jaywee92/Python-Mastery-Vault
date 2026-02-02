---
title: Literals & Variables
tags: [pcep, python, literals, variables, assignment]
created: 2026-01-30
exam_section: 1
exam_weight: 8%
---

# 📦 Literals & Variables

[[00_Index|← Back to Index]] | [[02_Python_Syntax|← Syntax]] | [[04_Operators|Operators →]]

> **"Know your literals - they appear in every exam question!"**

---

## 🎯 What are Literals?

```
┌─────────────────────────────────────────────────────────────────┐
│                    LITERALS                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A LITERAL is a fixed value written directly in code.           │
│                                                                  │
│  Examples:                                                       │
│    42         ← Integer literal                                 │
│    3.14       ← Float literal                                   │
│    "hello"    ← String literal                                  │
│    True       ← Boolean literal                                 │
│    None       ← None literal                                    │
│    [1, 2, 3]  ← List literal                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔢 Numeric Literals

### Integer Literals

```python
# ═══════════════════════════════════════════════════════════════
# INTEGER LITERALS
# ═══════════════════════════════════════════════════════════════

# Decimal (base 10) - default
x = 42
y = -17
z = 0

# Octal (base 8) - prefix 0o or 0O
octal = 0o17      # = 15 in decimal
print(octal)      # 15

# Hexadecimal (base 16) - prefix 0x or 0X
hexa = 0xFF       # = 255 in decimal
hexa2 = 0x1A      # = 26 in decimal
print(hexa)       # 255

# Binary (base 2) - prefix 0b or 0B
binary = 0b1010   # = 10 in decimal
print(binary)     # 10

# Underscores for readability (Python 3.6+)
million = 1_000_000
binary = 0b_1111_0000
hexa = 0xFF_FF
print(million)    # 1000000

# No size limit in Python!
big = 123456789012345678901234567890
```

### Float Literals

```python
# ═══════════════════════════════════════════════════════════════
# FLOAT LITERALS
# ═══════════════════════════════════════════════════════════════

# Standard notation
x = 3.14
y = -0.001
z = 4.0        # Still a float!

# Scientific notation (e or E)
a = 3e2        # = 300.0 (3 × 10²)
b = 3E2        # = 300.0 (same)
c = 1.5e-3     # = 0.0015 (1.5 × 10⁻³)
d = 2.5e10     # = 25000000000.0

print(type(3e2))  # <class 'float'>

# Special float values
import math
inf = float('inf')    # Positive infinity
neg_inf = float('-inf')  # Negative infinity
nan = float('nan')    # Not a Number

print(math.isinf(inf))  # True
print(math.isnan(nan))  # True
```

---

## 📝 String Literals

```python
# ═══════════════════════════════════════════════════════════════
# STRING LITERALS
# ═══════════════════════════════════════════════════════════════

# Single quotes
s1 = 'Hello'

# Double quotes (identical to single)
s2 = "Hello"

# Triple quotes (multiline)
s3 = '''This is
a multiline
string'''

s4 = """Also
multiline"""

# Escape sequences
tab = "Hello\tWorld"     # Tab
newline = "Hello\nWorld" # Newline
quote = "He said \"Hi\"" # Escaped quote
backslash = "C:\\folder" # Backslash
single = 'It\'s ok'      # Escaped single quote

# Raw strings (ignore escapes) - prefix r
path = r"C:\new\folder"  # \n not treated as newline
print(path)  # C:\new\folder

# Common escape sequences:
# \n  - newline
# \t  - tab
# \\  - backslash
# \'  - single quote
# \"  - double quote
# \r  - carriage return
```

---

## ✅ Boolean Literals

```python
# ═══════════════════════════════════════════════════════════════
# BOOLEAN LITERALS
# ═══════════════════════════════════════════════════════════════

# Only two values: True and False (capitalized!)
is_valid = True
is_empty = False

# Case matters!
# true   # NameError: name 'true' is not defined
# false  # NameError: name 'false' is not defined

# Booleans are actually integers!
print(True == 1)   # True
print(False == 0)  # True
print(True + True) # 2
print(True + False) # 1

# Boolean conversion (truthiness)
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False (empty string)
print(bool("hi"))   # True
print(bool([]))     # False (empty list)
print(bool([1]))    # True
print(bool(None))   # False
```

---

## ⬜ None Literal

```python
# ═══════════════════════════════════════════════════════════════
# NONE LITERAL
# ═══════════════════════════════════════════════════════════════

# None represents "nothing" or "no value"
x = None

# Check for None with 'is' (not ==)
if x is None:
    print("x is None")

if x is not None:
    print("x has a value")

# None is falsy
print(bool(None))  # False

# Functions return None by default
def no_return():
    pass

result = no_return()
print(result)  # None
print(result is None)  # True
```

---

## 📦 Variables

```
┌─────────────────────────────────────────────────────────────────┐
│                    VARIABLES                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A VARIABLE is a name that refers to a value in memory.         │
│                                                                  │
│  x = 42                                                         │
│    ↑   ↑                                                        │
│  name  value                                                    │
│                                                                  │
│  Variables in Python:                                           │
│  • Don't need to be declared                                    │
│  • Don't have fixed types (dynamic typing)                      │
│  • Are created when first assigned                              │
│  • Are references to objects                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# VARIABLE ASSIGNMENT
# ═══════════════════════════════════════════════════════════════

# Simple assignment
x = 10
name = "Alice"
pi = 3.14

# Multiple assignment (same value)
a = b = c = 0
print(a, b, c)  # 0 0 0

# Multiple assignment (different values)
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# Swap values (Python magic!)
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10

# Unpacking
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

*start, last = [1, 2, 3, 4, 5]
print(start)  # [1, 2, 3, 4]
print(last)   # 5

# Variables can change type
x = 10       # int
x = "hello"  # now str (dynamic typing!)
x = [1, 2]   # now list
```

---

## 🔗 Variable References

```python
# ═══════════════════════════════════════════════════════════════
# VARIABLES ARE REFERENCES
# ═══════════════════════════════════════════════════════════════

# With immutable types (int, str, tuple)
a = 10
b = a      # b points to same object
b = 20     # b now points to new object
print(a)   # 10 (unchanged)

# With mutable types (list, dict, set)
a = [1, 2, 3]
b = a      # b points to same list!
b.append(4)
print(a)   # [1, 2, 3, 4] - BOTH changed!

# Use copy to avoid this
a = [1, 2, 3]
b = a[:]   # or a.copy() or list(a)
b.append(4)
print(a)   # [1, 2, 3] (unchanged)

# Check identity with 'is'
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True (same object)
print(a is c)  # False (different objects)
print(a == c)  # True (same value)

# id() shows memory address
print(id(a))   # some number
print(id(b))   # same number
print(id(c))   # different number
```

---

## 🎨 Type Annotations (Optional)

```python
# ═══════════════════════════════════════════════════════════════
# TYPE HINTS (Python 3.5+)
# ═══════════════════════════════════════════════════════════════

# Type hints are optional annotations
name: str = "Alice"
age: int = 25
height: float = 1.75
is_student: bool = True

# Python doesn't enforce these - they're just hints!
name: str = 42  # No error! Python ignores type hints

# Function with type hints
def greet(name: str) -> str:
    return f"Hello, {name}"
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: Integer division
print(10 / 3)   # 3.333... (float!)
print(10 // 3)  # 3 (integer)

# TRAP 2: Octal/Hex/Binary output
x = 0o17
print(x)  # 15 (prints as decimal!)

# TRAP 3: Boolean as integer
print(True + True + False)  # 2

# TRAP 4: None comparison
x = None
# if x == None:  # Works but not preferred
if x is None:    # Correct way!
    pass

# TRAP 5: String escape
print("Hello\nWorld")  # Two lines
print(r"Hello\nWorld") # One line: Hello\nWorld

# TRAP 6: Float precision
print(0.1 + 0.2)  # 0.30000000000000004 (!)
print(0.1 + 0.2 == 0.3)  # False (!)

# TRAP 7: Assignment in condition
# if x = 5:  # SyntaxError! (not allowed in Python)
```

---

## 📝 Quick Reference

| Literal Type | Examples |
|--------------|----------|
| Integer | `42`, `-17`, `0`, `0xFF`, `0o17`, `0b1010` |
| Float | `3.14`, `1.5e-3`, `2.0` |
| String | `'hello'`, `"world"`, `'''multi'''` |
| Boolean | `True`, `False` |
| None | `None` |

---

## 🎯 Exam Checklist

- [ ] Integer prefixes: 0x (hex), 0o (octal), 0b (binary)
- [ ] Scientific notation: 3e2 = 300.0
- [ ] Escape sequences: \n, \t, \\, \', \"
- [ ] Raw strings: r"string"
- [ ] True/False are capitalized
- [ ] None checked with `is`, not `==`
- [ ] Variables are references to objects
- [ ] Dynamic typing - variables can change type

---

[[02_Python_Syntax|← Syntax]] | [[00_Index|Index]] | [[04_Operators|Operators →]]
