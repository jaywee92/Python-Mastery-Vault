---
title: Recursion & Generators
tags: [pcep, python, recursion, generators, yield]
created: 2026-01-30
exam_section: 4
exam_weight: 5%
---

# 🔄 Recursion & Generators

[[00_Index|← Back to Index]] | [[16_Exceptions|← Exceptions]] | [[18_Quick_Reference|Quick Reference →]]

> **"Understand the basics - these appear occasionally!"**

---

## 🔁 Recursion Basics

```
┌─────────────────────────────────────────────────────────────────┐
│              RECURSION                                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A function that CALLS ITSELF.                                  │
│                                                                  │
│  Every recursive function needs:                                │
│  1. BASE CASE - condition to stop recursion                    │
│  2. RECURSIVE CASE - calls itself with smaller problem         │
│                                                                  │
│  Without base case → infinite recursion → RecursionError!      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# FACTORIAL EXAMPLE
# ═══════════════════════════════════════════════════════════════

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # 120 (5 * 4 * 3 * 2 * 1)

# How it works:
# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1
# = 120
```

---

## 📊 Common Recursive Examples

```python
# ═══════════════════════════════════════════════════════════════
# FIBONACCI
# ═══════════════════════════════════════════════════════════════

def fibonacci(n):
    if n <= 1:  # Base cases
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8 (0, 1, 1, 2, 3, 5, 8)

# ═══════════════════════════════════════════════════════════════
# SUM OF LIST
# ═══════════════════════════════════════════════════════════════

def sum_list(lst):
    if len(lst) == 0:  # Base case
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15

# ═══════════════════════════════════════════════════════════════
# COUNTDOWN
# ═══════════════════════════════════════════════════════════════

def countdown(n):
    if n <= 0:  # Base case
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)

countdown(3)  # 3, 2, 1, Blast off!

# ═══════════════════════════════════════════════════════════════
# POWER (Exponentiation)
# ═══════════════════════════════════════════════════════════════

def power(base, exp):
    if exp == 0:  # Base case
        return 1
    return base * power(base, exp - 1)

print(power(2, 3))  # 8
```

---

## ⚠️ Recursion Limits

```python
# ═══════════════════════════════════════════════════════════════
# RECURSION LIMIT
# ═══════════════════════════════════════════════════════════════

import sys

# Python has a recursion limit (default ~1000)
print(sys.getrecursionlimit())  # 1000 (default)

# Exceeding limit raises RecursionError
def infinite():
    return infinite()  # No base case!

# infinite()  # RecursionError: maximum recursion depth exceeded

# Can increase limit (not recommended)
# sys.setrecursionlimit(2000)
```

---

## 🌿 Generators Basics

```
┌─────────────────────────────────────────────────────────────────┐
│              GENERATORS                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  A generator is a function that uses YIELD instead of RETURN.  │
│                                                                  │
│  • Produces values ONE AT A TIME (lazy evaluation)             │
│  • Saves memory for large sequences                            │
│  • Can only iterate once                                        │
│  • Returns a generator object                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# GENERATOR FUNCTION
# ═══════════════════════════════════════════════════════════════

def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Pauses and returns value
        count += 1

# Creates a generator object
gen = count_up_to(3)
print(type(gen))  # <class 'generator'>

# Get values one at a time
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # StopIteration error!

# Or iterate with for loop
for num in count_up_to(3):
    print(num)  # 1, 2, 3

# ═══════════════════════════════════════════════════════════════
# GENERATOR EXPRESSION
# ═══════════════════════════════════════════════════════════════

# Like list comprehension, but with ()
squares_gen = (x**2 for x in range(5))
print(type(squares_gen))  # <class 'generator'>

# Convert to list
print(list(squares_gen))  # [0, 1, 4, 9, 16]

# Compare memory usage:
# List: stores all values in memory
squares_list = [x**2 for x in range(1000000)]

# Generator: computes values on demand
squares_gen = (x**2 for x in range(1000000))
```

---

## 🔧 Generator Examples

```python
# ═══════════════════════════════════════════════════════════════
# FIBONACCI GENERATOR
# ═══════════════════════════════════════════════════════════════

def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
fib = fib_generator()
for _ in range(10):
    print(next(fib), end=" ")
# 0 1 1 2 3 5 8 13 21 34

# ═══════════════════════════════════════════════════════════════
# READING LARGE FILES
# ═══════════════════════════════════════════════════════════════

def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# Memory efficient - only one line in memory at a time
# for line in read_lines("huge_file.txt"):
#     process(line)
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: No base case = RecursionError
def bad_recursion(n):
    return bad_recursion(n - 1)  # No base case!

# TRAP 2: Base case never reached
def still_bad(n):
    if n == 0:
        return 0
    return still_bad(n + 1)  # n increases, never reaches 0!

# TRAP 3: Generator exhaustion
gen = (x for x in range(3))
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [] - already exhausted!

# TRAP 4: Generator vs list comprehension
gen = (x for x in range(3))   # Generator (parentheses)
lst = [x for x in range(3)]   # List (brackets)

# TRAP 5: next() on exhausted generator
gen = (x for x in range(2))
print(next(gen))  # 0
print(next(gen))  # 1
# print(next(gen))  # StopIteration!

# Safe way:
print(next(gen, "default"))  # "default" if exhausted

# TRAP 6: yield vs return
def with_return():
    return [1, 2, 3]  # Returns list immediately

def with_yield():
    yield 1
    yield 2
    yield 3  # Returns generator

print(type(with_return()))  # <class 'list'>
print(type(with_yield()))   # <class 'generator'>
```

---

## 📝 Quick Reference

| Concept | Description | Example |
|---------|-------------|---------|
| Recursion | Function calls itself | `def f(n): return f(n-1)` |
| Base case | Condition to stop | `if n == 0: return 1` |
| yield | Produce value, pause | `yield x` |
| Generator | Function with yield | `def gen(): yield 1` |
| Gen expression | `(expr for x in iter)` | `(x**2 for x in range(5))` |
| next() | Get next value | `next(gen)` |

---

## 🎯 Exam Checklist

- [ ] Recursion needs a BASE CASE
- [ ] RecursionError if too many calls
- [ ] yield creates a generator
- [ ] Generators produce values lazily
- [ ] Generators can only iterate once
- [ ] (x for x in ...) = generator expression
- [ ] [x for x in ...] = list comprehension
- [ ] next() gets next value from generator

---

[[16_Exceptions|← Exceptions]] | [[00_Index|Index]] | [[18_Quick_Reference|Quick Reference →]]
