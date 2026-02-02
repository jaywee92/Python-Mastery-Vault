---
title: Input & Output
tags: [pcep, python, input, print, output]
created: 2026-01-30
exam_section: 1
exam_weight: 5%
---

# 📥📤 Input & Output

[[00_Index|← Back to Index]] | [[05_Data_Types|← Data Types]] | [[07_Conditionals|Conditionals →]]

> **"Remember: input() ALWAYS returns a string!"**

---

## 📤 The print() Function

```python
# ═══════════════════════════════════════════════════════════════
# BASIC PRINT
# ═══════════════════════════════════════════════════════════════

print("Hello, World!")
print(42)
print(3.14)
print(True)
print([1, 2, 3])

# Multiple arguments
print("Hello", "World")      # Hello World
print(1, 2, 3)               # 1 2 3

# ═══════════════════════════════════════════════════════════════
# PRINT PARAMETERS
# ═══════════════════════════════════════════════════════════════

# sep - separator between arguments (default: space)
print("a", "b", "c")              # a b c
print("a", "b", "c", sep="")      # abc
print("a", "b", "c", sep="-")     # a-b-c
print("a", "b", "c", sep="\n")    # a (newline) b (newline) c

# end - what to print at end (default: newline)
print("Hello", end="")
print(" World")           # Hello World (same line)

print("Line 1", end="---")
print("Line 2")           # Line 1---Line 2

# Combining sep and end
print(1, 2, 3, sep=",", end="!\n")  # 1,2,3!

# ═══════════════════════════════════════════════════════════════
# PRINT TO FILE
# ═══════════════════════════════════════════════════════════════

# file parameter (default: sys.stdout)
import sys
print("Error!", file=sys.stderr)

# Write to a file
with open("output.txt", "w") as f:
    print("Hello", file=f)
```

---

## 📥 The input() Function

```
┌─────────────────────────────────────────────────────────────────┐
│              input() ALWAYS RETURNS A STRING!                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  name = input("Enter name: ")                                   │
│  # User types: Alice                                            │
│  # name = "Alice" (string!)                                     │
│                                                                  │
│  age = input("Enter age: ")                                     │
│  # User types: 25                                               │
│  # age = "25" (string, NOT int!)                               │
│                                                                  │
│  To get a number: int(input("Enter age: "))                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# BASIC INPUT
# ═══════════════════════════════════════════════════════════════

# Simple input
name = input()  # Waits for user input

# Input with prompt
name = input("Enter your name: ")
print(f"Hello, {name}!")

# input() ALWAYS returns string!
age = input("Enter your age: ")
print(type(age))  # <class 'str'>
print(age + 10)   # TypeError! Can't add str and int

# Convert input to numbers
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

# ═══════════════════════════════════════════════════════════════
# INPUT PATTERNS
# ═══════════════════════════════════════════════════════════════

# Get integer input
number = int(input("Enter a number: "))

# Get float input
decimal = float(input("Enter a decimal: "))

# Get multiple values on one line
x, y = input("Enter x y: ").split()  # Returns list of strings
x, y = int(x), int(y)

# Or in one line
x, y = map(int, input("Enter x y: ").split())

# Get a list of numbers
numbers = list(map(int, input("Enter numbers: ").split()))
# User types: 1 2 3 4 5
# numbers = [1, 2, 3, 4, 5]
```

---

## 🎨 String Formatting

```python
# ═══════════════════════════════════════════════════════════════
# STRING FORMATTING METHODS
# ═══════════════════════════════════════════════════════════════

name = "Alice"
age = 25
height = 1.756

# Method 1: f-strings (Python 3.6+) - RECOMMENDED
print(f"Name: {name}, Age: {age}")
print(f"Height: {height:.2f}")     # 1.76 (2 decimal places)
print(f"Age in 10 years: {age + 10}")

# Method 2: .format()
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# Method 3: % operator (old style)
print("Name: %s, Age: %d" % (name, age))
print("Height: %.2f" % height)

# ═══════════════════════════════════════════════════════════════
# FORMAT SPECIFIERS
# ═══════════════════════════════════════════════════════════════

# Number formatting
num = 42
pi = 3.14159

print(f"{num:5d}")     # "   42" (width 5, right-aligned)
print(f"{num:05d}")    # "00042" (zero-padded)
print(f"{num:<5d}")    # "42   " (left-aligned)
print(f"{num:^5d}")    # " 42  " (centered)

print(f"{pi:.2f}")     # "3.14" (2 decimal places)
print(f"{pi:8.2f}")    # "    3.14" (width 8, 2 decimals)

# Large numbers with comma separator
big = 1000000
print(f"{big:,}")      # "1,000,000"

# Percentage
ratio = 0.75
print(f"{ratio:.1%}")  # "75.0%"

# Binary, hex, octal
num = 255
print(f"{num:b}")      # "11111111" (binary)
print(f"{num:x}")      # "ff" (hex)
print(f"{num:o}")      # "377" (octal)
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: input() always returns string
x = input("Enter number: ")  # User enters: 5
print(x + 5)  # TypeError! "5" + 5 doesn't work

# FIX:
x = int(input("Enter number: "))
print(x + 5)  # 10

# TRAP 2: Empty input
x = input("Enter: ")  # User just presses Enter
print(x)      # "" (empty string)
print(bool(x))  # False

# TRAP 3: print() returns None
result = print("Hello")
print(result)  # None

# TRAP 4: sep and end defaults
print("a", "b")       # a b (space between, newline at end)
print("a", "b", sep="")  # ab
print("a", "b", end="")  # a b (no newline)

# TRAP 5: Multiple inputs on same line
# For "5 10 15":
a, b, c = input().split()  # a="5", b="10", c="15" (all strings!)

# TRAP 6: Float formatting
print(f"{3.1:.0f}")  # "3" (no decimal places)
print(f"{3.5:.0f}")  # "4" (rounds!)
print(f"{3.14159:.3f}")  # "3.142" (rounds!)

# TRAP 7: Escape characters in print
print("Hello\nWorld")   # Two lines
print(r"Hello\nWorld")  # Hello\nWorld (raw string)
print("Hello\\nWorld")  # Hello\nWorld (escaped backslash)
```

---

## 📝 Quick Reference

| Function/Format | Description | Example |
|-----------------|-------------|---------|
| `print(x)` | Print x | `print("Hi")` → `Hi` |
| `print(x, y, sep="-")` | Custom separator | `print(1,2,sep="-")` → `1-2` |
| `print(x, end="")` | No newline | Continues on same line |
| `input()` | Get user input (string!) | `x = input()` |
| `f"{x}"` | f-string | `f"Age: {age}"` |
| `f"{x:.2f}"` | 2 decimal places | `f"{3.14159:.2f}"` → `"3.14"` |
| `f"{x:05d}"` | Zero-padded | `f"{42:05d}"` → `"00042"` |

---

## 🎯 Exam Checklist

- [ ] input() ALWAYS returns string
- [ ] Convert input: int(), float()
- [ ] print() with multiple args uses space separator
- [ ] sep="" removes spaces between args
- [ ] end="" prevents newline
- [ ] f-strings: f"text {variable}"
- [ ] Format specifiers: .2f, 05d, etc.
- [ ] print() returns None

---

[[05_Data_Types|← Data Types]] | [[00_Index|Index]] | [[07_Conditionals|Conditionals →]]
