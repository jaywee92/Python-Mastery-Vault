---
title: Python Syntax
tags: [pcep, python, syntax, indentation, comments]
created: 2026-01-30
exam_section: 1
exam_weight: 5%
---

# 📝 Python Syntax Fundamentals

[[00_Index|← Back to Index]] | [[01_Computer_Programming_Basics|← Basics]] | [[03_Literals_Variables|Literals & Variables →]]

> **"Python's syntax is simple but strict - indentation matters!"**

---

## 🎯 Python's Key Syntax Rules

```
┌─────────────────────────────────────────────────────────────────┐
│              PYTHON SYNTAX ESSENTIALS                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. INDENTATION is MANDATORY (not just style!)                  │
│  2. Colons (:) introduce code blocks                            │
│  3. No semicolons needed (but allowed)                          │
│  4. Case SENSITIVE (Name ≠ name ≠ NAME)                         │
│  5. Comments with # (single line)                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📏 Indentation (CRITICAL!)

```python
# ═══════════════════════════════════════════════════════════════
# INDENTATION RULES
# ═══════════════════════════════════════════════════════════════

# ✅ CORRECT: Consistent indentation (4 spaces recommended)
if True:
    print("Level 1")
    if True:
        print("Level 2")

# ❌ WRONG: Inconsistent indentation
# if True:
#     print("Four spaces")
#   print("Two spaces")  # IndentationError!

# ❌ WRONG: Missing indentation
# if True:
# print("No indent")  # IndentationError!

# Tabs vs Spaces: DON'T MIX!
# Python 3 doesn't allow mixing tabs and spaces
```

```
┌─────────────────────────────────────────────────────────────────┐
│              INDENTATION ERRORS                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  IndentationError: expected an indented block                   │
│    → Missing indentation after : (if, for, def, class, etc.)   │
│                                                                  │
│  IndentationError: unexpected indent                            │
│    → Extra indentation where not expected                       │
│                                                                  │
│  IndentationError: unindent does not match                      │
│    → Inconsistent indentation level                             │
│                                                                  │
│  TabError: inconsistent use of tabs and spaces                  │
│    → Mixed tabs and spaces in indentation                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💬 Comments

```python
# ═══════════════════════════════════════════════════════════════
# COMMENTS
# ═══════════════════════════════════════════════════════════════

# Single line comment
x = 5  # Inline comment

# Multi-line comments (consecutive single-line)
# This is line 1
# This is line 2
# This is line 3

"""
This is a multi-line string (docstring).
Often used as multi-line comment.
But it's actually a string literal!
"""

'''
Single quotes work too
for multi-line strings.
'''

# Comments are ignored by Python interpreter
# print("This won't print")  ← Won't execute
```

---

## 📝 Statements and Lines

```python
# ═══════════════════════════════════════════════════════════════
# STATEMENTS AND LINE CONTINUATION
# ═══════════════════════════════════════════════════════════════

# One statement per line (typical)
x = 5
y = 10
z = x + y

# Multiple statements on one line (with semicolon)
x = 5; y = 10; z = x + y  # Works but not recommended

# Line continuation with backslash (\)
total = 1 + 2 + 3 + \
        4 + 5 + 6
print(total)  # 21

# Implicit continuation inside brackets
numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

result = (1 + 2 + 3 +
          4 + 5 + 6)

person = {
    "name": "Alice",
    "age": 25
}
```

---

## 🔤 Identifiers (Names)

```
┌─────────────────────────────────────────────────────────────────┐
│              IDENTIFIER RULES                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  VALID identifiers must:                                        │
│  • Start with letter (a-z, A-Z) or underscore (_)              │
│  • Contain only letters, digits (0-9), and underscores         │
│  • NOT be a Python keyword                                      │
│  • Be case-sensitive                                            │
│                                                                  │
│  ✅ VALID:   name, Name, _name, name1, my_var, __init__        │
│  ❌ INVALID: 1name, my-var, my var, class, if, for            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# IDENTIFIER EXAMPLES
# ═══════════════════════════════════════════════════════════════

# Valid identifiers
name = "Alice"
Name = "Bob"       # Different from 'name'!
_private = 10      # Convention: "private" variable
__dunder__ = 20    # Special Python names
my_variable = 30
var123 = 40

# Invalid identifiers
# 1variable = 10   # SyntaxError: starts with digit
# my-var = 10      # SyntaxError: hyphen not allowed
# my var = 10      # SyntaxError: space not allowed
# class = 10       # SyntaxError: keyword

# Case sensitivity
age = 25
Age = 30
AGE = 35
print(age, Age, AGE)  # 25 30 35 - all different!
```

---

## 🚫 Python Keywords (Reserved Words)

```python
# ═══════════════════════════════════════════════════════════════
# PYTHON KEYWORDS (Cannot use as identifiers!)
# ═══════════════════════════════════════════════════════════════

import keyword
print(keyword.kwlist)

# Python 3.x keywords:
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

# Check if word is keyword
print(keyword.iskeyword("if"))      # True
print(keyword.iskeyword("hello"))   # False
```

---

## 🎨 Naming Conventions (PEP 8)

```python
# ═══════════════════════════════════════════════════════════════
# NAMING CONVENTIONS
# ═══════════════════════════════════════════════════════════════

# Variables and functions: lowercase_with_underscores
user_name = "Alice"
def calculate_total():
    pass

# Constants: UPPERCASE_WITH_UNDERSCORES
MAX_SIZE = 100
PI = 3.14159

# Classes: CamelCase (CapitalizedWords)
class MyClass:
    pass

# Private: starts with underscore
_internal_var = 10

# "Really private": starts with double underscore
__very_private = 20

# Magic/Dunder methods: __name__
__init__ = "special"

# Avoid: single letter names (except i, j, k for loops)
# Avoid: l, O, I (look like 1, 0)
```

---

## 📋 Code Blocks

```python
# ═══════════════════════════════════════════════════════════════
# CODE BLOCKS
# ═══════════════════════════════════════════════════════════════

# Code blocks are defined by indentation, not braces {}
# Colon (:) introduces a code block

# If statement
if condition:
    # This is the if block
    statement1
    statement2

# For loop
for item in items:
    # This is the for block
    process(item)

# Function definition
def my_function():
    # This is the function body
    return result

# Class definition
class MyClass:
    # This is the class body
    def method(self):
        pass

# While loop
while condition:
    # This is the while block
    do_something()

# Try-except
try:
    # Try block
    risky_operation()
except:
    # Except block
    handle_error()
```

---

## ⚠️ Common Syntax Errors

```python
# ═══════════════════════════════════════════════════════════════
# COMMON SYNTAX ERRORS
# ═══════════════════════════════════════════════════════════════

# Missing colon
# if True     # SyntaxError: expected ':'
#     print("hello")

# Missing indentation
# if True:
# print("hello")  # IndentationError

# Mismatched quotes
# print("hello')  # SyntaxError

# Mismatched brackets
# nums = [1, 2, 3  # SyntaxError: '[' was never closed

# Assignment vs comparison
# if x = 5:       # SyntaxError (use == for comparison)

# Invalid identifier
# 2fast = 10      # SyntaxError

# Using keyword as name
# class = "A"     # SyntaxError
```

---

## 🎯 Exam Checklist

- [ ] Indentation is mandatory (4 spaces recommended)
- [ ] Comments use # for single line
- [ ] Identifiers: letters, digits, underscores only
- [ ] Cannot start identifier with digit
- [ ] Python is case-sensitive
- [ ] Keywords cannot be used as identifiers
- [ ] Colon (:) introduces code blocks
- [ ] No mixing tabs and spaces

---

[[01_Computer_Programming_Basics|← Basics]] | [[00_Index|Index]] | [[03_Literals_Variables|Literals & Variables →]]
