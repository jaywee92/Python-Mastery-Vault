---
title: Functions - Advanced
tags: [pcep, python, functions, args, kwargs, lambda]
created: 2026-01-30
exam_section: 4
exam_weight: 10%
---

# 🚀 Functions - Advanced

[[00_Index|← Back to Index]] | [[13_Functions_Basics|← Functions Basics]] | [[15_Builtin_Functions|Built-ins →]]

> **"Master *args, **kwargs, and lambda for the exam!"**

---

## 📦 *args - Variable Positional Arguments

```python
# ═══════════════════════════════════════════════════════════════
# *args - Accept any number of positional arguments
# ═══════════════════════════════════════════════════════════════

def sum_all(*args):
    """args is a TUPLE of all positional arguments."""
    print(f"args = {args}")
    print(f"type = {type(args)}")
    return sum(args)

print(sum_all(1, 2))           # args = (1, 2), returns 3
print(sum_all(1, 2, 3, 4, 5))  # args = (1, 2, 3, 4, 5), returns 15
print(sum_all())               # args = (), returns 0

# Combine with regular parameters
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!

# *args must come AFTER regular positional parameters
def func(a, b, *args):   # OK
    pass

# def func(*args, a, b):  # a, b become keyword-only!
```

---

## 📖 **kwargs - Variable Keyword Arguments

```python
# ═══════════════════════════════════════════════════════════════
# **kwargs - Accept any number of keyword arguments
# ═══════════════════════════════════════════════════════════════

def print_info(**kwargs):
    """kwargs is a DICT of keyword arguments."""
    print(f"kwargs = {kwargs}")
    print(f"type = {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Berlin")
# kwargs = {'name': 'Alice', 'age': 25, 'city': 'Berlin'}
# type = <class 'dict'>
# name: Alice
# age: 25
# city: Berlin

# Combine with regular parameters
def create_profile(username, **details):
    profile = {"username": username}
    profile.update(details)
    return profile

print(create_profile("alice123", email="a@b.com", age=25))
# {'username': 'alice123', 'email': 'a@b.com', 'age': 25}
```

---

## 🔀 Combining *args and **kwargs

```python
# ═══════════════════════════════════════════════════════════════
# PARAMETER ORDER (MUST FOLLOW!)
# ═══════════════════════════════════════════════════════════════

# Order: positional → *args → keyword → **kwargs
def func(a, b, *args, c=10, d=20, **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"c={c}, d={d}")
    print(f"kwargs={kwargs}")

func(1, 2, 3, 4, 5, c=100, x="extra", y="more")
# a=1, b=2
# args=(3, 4, 5)
# c=100, d=20
# kwargs={'x': 'extra', 'y': 'more'}

# "Accepts anything" function
def universal(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

universal(1, 2, 3, name="Alice", age=25)
# args: (1, 2, 3)
# kwargs: {'name': 'Alice', 'age': 25}
```

---

## 📤 Unpacking Arguments

```python
# ═══════════════════════════════════════════════════════════════
# UNPACKING WHEN CALLING FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def add(a, b, c):
    return a + b + c

# Unpack list/tuple with *
numbers = [1, 2, 3]
print(add(*numbers))  # Same as add(1, 2, 3) → 6

# Unpack dict with **
params = {"a": 1, "b": 2, "c": 3}
print(add(**params))  # Same as add(a=1, b=2, c=3) → 6

# Mix unpacking
def greet(greeting, name, punctuation):
    return f"{greeting}, {name}{punctuation}"

args = ("Hello", "Alice")
kwargs = {"punctuation": "!"}
print(greet(*args, **kwargs))  # Hello, Alice!
```

---

## λ Lambda Functions

```
┌─────────────────────────────────────────────────────────────────┐
│              LAMBDA FUNCTIONS                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Lambda = anonymous (unnamed) function                          │
│                                                                  │
│  Syntax: lambda parameters: expression                          │
│                                                                  │
│  • Single expression only (no statements!)                      │
│  • Returns result automatically                                 │
│  • No return keyword needed                                     │
│  • Useful for short, simple functions                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# LAMBDA FUNCTIONS
# ═══════════════════════════════════════════════════════════════

# Basic lambda
double = lambda x: x * 2
print(double(5))  # 10

# Equivalent to:
def double(x):
    return x * 2

# Multiple parameters
add = lambda a, b: a + b
print(add(3, 5))  # 8

# No parameters
greet = lambda: "Hello!"
print(greet())  # Hello!

# With default parameters
power = lambda x, n=2: x ** n
print(power(3))      # 9
print(power(3, 3))   # 27

# Lambda with conditionals (ternary)
classify = lambda x: "positive" if x > 0 else "non-positive"
print(classify(5))   # positive
print(classify(-3))  # non-positive
```

---

## 🔧 Lambda with Built-in Functions

```python
# ═══════════════════════════════════════════════════════════════
# LAMBDA WITH sorted(), map(), filter()
# ═══════════════════════════════════════════════════════════════

# sorted() with key
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
by_grade = sorted(students, key=lambda s: s["grade"])
print([s["name"] for s in by_grade])  # ['Charlie', 'Alice', 'Bob']

# Sort by name
by_name = sorted(students, key=lambda s: s["name"])

# Sort strings by length
words = ["apple", "pie", "banana", "cat"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)  # ['pie', 'cat', 'apple', 'banana']

# map() - apply function to each element
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# filter() - keep elements where function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Combine map and filter
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10))))
print(result)  # [0, 4, 16, 36, 64]
```

---

## 🔄 Closures

```python
# ═══════════════════════════════════════════════════════════════
# CLOSURES - Functions that "remember" their environment
# ═══════════════════════════════════════════════════════════════

def make_multiplier(n):
    """Returns a function that multiplies by n."""
    def multiplier(x):
        return x * n  # n is "remembered" from outer function
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# Each closure has its own "n"
print(double(10))  # 20
print(triple(10))  # 30
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: *args is a TUPLE, **kwargs is a DICT
def show(*args, **kwargs):
    print(type(args))    # <class 'tuple'>
    print(type(kwargs))  # <class 'dict'>

# TRAP 2: Parameter order matters!
# def wrong(a, *args, b, **kwargs, c):  # SyntaxError!
def right(a, *args, b=10, **kwargs):     # OK
    pass

# TRAP 3: Lambda can only have ONE expression
# lambda x: if x > 0: return x  # SyntaxError!
lambda x: x if x > 0 else 0     # OK (ternary)

# TRAP 4: Lambda with no return keyword
double = lambda x: x * 2  # Returns automatically
# double = lambda x: return x * 2  # SyntaxError!

# TRAP 5: Unpacking syntax
def func(a, b, c):
    pass

lst = [1, 2, 3]
func(*lst)     # Unpack list: func(1, 2, 3)
# func(lst)    # Error: func([1,2,3]) - passes list as 'a'

dct = {"a": 1, "b": 2, "c": 3}
func(**dct)    # Unpack dict: func(a=1, b=2, c=3)

# TRAP 6: *args after regular params
def func(a, b, *args):
    print(a, b, args)

func(1, 2, 3, 4)  # a=1, b=2, args=(3, 4)

# TRAP 7: Keyword-only parameters after *args
def func(*args, required_keyword):
    print(args, required_keyword)

# func(1, 2, 3)  # TypeError! missing required keyword
func(1, 2, 3, required_keyword="value")  # OK

# TRAP 8: Default value shared across calls (mutable default)
def bad_append(item, lst=[]):  # DANGER!
    lst.append(item)
    return lst

print(bad_append(1))  # [1]
print(bad_append(2))  # [1, 2] - Surprise!
```

---

## 📝 Quick Reference

| Syntax | Description | Example |
|--------|-------------|---------|
| `*args` | Variable positional args | `def f(*args):` |
| `**kwargs` | Variable keyword args | `def f(**kwargs):` |
| `*list` | Unpack list when calling | `f(*[1,2,3])` |
| `**dict` | Unpack dict when calling | `f(**{"a":1})` |
| `lambda x: expr` | Anonymous function | `lambda x: x*2` |
| `key=lambda` | Sort key function | `sorted(l, key=lambda x: x[1])` |

---

## 🎯 Exam Checklist

- [ ] *args creates a TUPLE
- [ ] **kwargs creates a DICT
- [ ] Parameter order: positional, *args, keyword, **kwargs
- [ ] Lambda: single expression, auto-returns
- [ ] Lambda cannot have statements (if/for/while)
- [ ] Use ternary in lambda for conditionals
- [ ] * unpacks sequences when calling
- [ ] ** unpacks dicts when calling
- [ ] map() and filter() work with lambda

---

[[13_Functions_Basics|← Functions Basics]] | [[00_Index|Index]] | [[15_Builtin_Functions|Built-ins →]]
