---
title: Functions - Basics
tags: [pcep, python, functions, def, return, parameters]
created: 2026-01-30
exam_section: 4
exam_weight: 15%
---

# 🔧 Functions - Basics

[[00_Index|← Back to Index]] | [[12_Dictionaries|← Dictionaries]] | [[14_Functions_Advanced|Functions Advanced →]]

> **"Section 4 is 35% of the exam - functions are critical!"**

---

## ⚠️ EXAM ALERT: Functions = 35% of exam weight!

---

## 🎯 What is a Function?

```
┌─────────────────────────────────────────────────────────────────┐
│                    FUNCTION ANATOMY                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  def function_name(parameter1, parameter2):                     │
│      """Docstring - explains what function does"""              │
│      # Function body                                            │
│      result = parameter1 + parameter2                           │
│      return result                                              │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  def      - keyword to define a function                │   │
│  │  name     - function identifier (follows naming rules)  │   │
│  │  ()       - parentheses contain parameters              │   │
│  │  :        - colon ends the function header              │   │
│  │  body     - indented code block                         │   │
│  │  return   - (optional) sends value back to caller       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# BASIC FUNCTION EXAMPLES
# ═══════════════════════════════════════════════════════════════

# Simple function with no parameters
def greet():
    print("Hello, World!")

greet()  # Call the function → Hello, World!

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Hello, Alice!

# Function with return value
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# Function with multiple return values (returns tuple)
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

low, high, total = get_stats([1, 2, 3, 4, 5])
print(low, high, total)  # 1 5 15
```

---

## 📥 Parameters vs Arguments

```
┌─────────────────────────────────────────────────────────────────┐
│              PARAMETERS vs ARGUMENTS                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PARAMETERS: Variables in function DEFINITION                   │
│  ARGUMENTS:  Values passed in function CALL                     │
│                                                                  │
│  def greet(name):     ← name is a PARAMETER                    │
│      print(name)                                                │
│                                                                  │
│  greet("Alice")       ← "Alice" is an ARGUMENT                 │
│                                                                  │
│  Think of it as:                                                │
│    Parameter = placeholder (in definition)                      │
│    Argument = actual value (in call)                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔢 Types of Arguments

### Positional Arguments

```python
# ═══════════════════════════════════════════════════════════════
# POSITIONAL ARGUMENTS - order matters!
# ═══════════════════════════════════════════════════════════════

def describe(name, age, city):
    print(f"{name} is {age} years old from {city}")

# Positional: matched by order
describe("Alice", 25, "Berlin")  # Alice is 25 years old from Berlin
describe("Berlin", "Alice", 25)  # Berlin is Alice years old from 25 (wrong!)
```

### Keyword Arguments

```python
# ═══════════════════════════════════════════════════════════════
# KEYWORD ARGUMENTS - order doesn't matter!
# ═══════════════════════════════════════════════════════════════

def describe(name, age, city):
    print(f"{name} is {age} years old from {city}")

# Keyword: matched by name, order doesn't matter
describe(name="Alice", age=25, city="Berlin")
describe(city="Berlin", name="Alice", age=25)  # Same result!

# Mixed: positional MUST come before keyword
describe("Alice", city="Berlin", age=25)  # OK
# describe(name="Alice", 25, "Berlin")  # SyntaxError!
```

### Default Parameters

```python
# ═══════════════════════════════════════════════════════════════
# DEFAULT PARAMETERS
# ═══════════════════════════════════════════════════════════════

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Alice", "Hi")        # Hi, Alice!
greet("Alice", greeting="Hey")  # Hey, Alice!

# IMPORTANT: Default parameters must come AFTER non-default!
def func(a, b=10, c=20):   # OK
    pass

# def func(a=10, b, c):    # SyntaxError! Non-default after default
```

### EXAM TRAP: Mutable Default Arguments

```python
# ═══════════════════════════════════════════════════════════════
# MUTABLE DEFAULT ARGUMENT TRAP!
# ═══════════════════════════════════════════════════════════════

# ❌ WRONG: Mutable default argument
def add_item(item, items=[]):  # DANGER!
    items.append(item)
    return items

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b']  ← SURPRISE! List persists!
print(add_item("c"))  # ['a', 'b', 'c']

# ✅ RIGHT: Use None as default
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['b']  ← Fresh list each time!
```

---

## 📤 Return Statement

```python
# ═══════════════════════════════════════════════════════════════
# RETURN STATEMENT
# ═══════════════════════════════════════════════════════════════

# Return a value
def double(x):
    return x * 2

print(double(5))  # 10

# Return ends function execution
def check_positive(x):
    if x > 0:
        return "Positive"
    return "Not positive"  # Only reached if x <= 0

# No return = returns None
def no_return():
    print("Hello")
    # No return statement

result = no_return()  # Prints "Hello"
print(result)         # None

# Empty return = returns None
def empty_return():
    return

result = empty_return()
print(result)  # None

# Multiple return values (actually returns a tuple)
def get_coordinates():
    return 10, 20  # Returns (10, 20)

x, y = get_coordinates()
print(x, y)  # 10 20

coords = get_coordinates()
print(coords)  # (10, 20)
```

---

## 🔄 Variable Scope (EXAM FAVORITE!)

```
┌─────────────────────────────────────────────────────────────────┐
│                    VARIABLE SCOPE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  GLOBAL: Defined outside any function                           │
│  LOCAL:  Defined inside a function                              │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  global_var = 10       ← GLOBAL scope                   │   │
│  │                                                          │   │
│  │  def my_function():                                      │   │
│  │      local_var = 20    ← LOCAL scope (only inside func) │   │
│  │      print(global_var) ← Can READ global                │   │
│  │      print(local_var)                                    │   │
│  │                                                          │   │
│  │  print(global_var)     ← OK, global accessible          │   │
│  │  print(local_var)      ← ERROR! local not accessible    │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# SCOPE EXAMPLES
# ═══════════════════════════════════════════════════════════════

# Global variable
x = 10

def read_global():
    print(x)  # Can READ global variable

read_global()  # 10

# Local variable shadows global
x = 10

def shadow_global():
    x = 20  # This is a NEW local variable, not the global!
    print(x)

shadow_global()  # 20
print(x)         # 10 (global unchanged)

# Modifying global with 'global' keyword
x = 10

def modify_global():
    global x  # Declare we want to use the global x
    x = 20

modify_global()
print(x)  # 20 (global was modified)

# ═══════════════════════════════════════════════════════════════
# COMMON EXAM TRAP: UnboundLocalError
# ═══════════════════════════════════════════════════════════════

x = 10

def trap():
    # print(x)  # UnboundLocalError! Python sees assignment below
    x = 20      # and thinks x is local, but it's not defined yet
    print(x)

# ✅ FIX: Either use 'global' or don't reassign
def fixed():
    global x
    print(x)  # OK now
    x = 20
```

---

## 📋 Docstrings

```python
# ═══════════════════════════════════════════════════════════════
# DOCSTRINGS - Documentation for functions
# ═══════════════════════════════════════════════════════════════

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length: The length of the rectangle
        width: The width of the rectangle

    Returns:
        The area (length * width)
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)

# Use help()
help(calculate_area)
```

---

## 🔧 Built-in Functions (MUST KNOW!)

```python
# ═══════════════════════════════════════════════════════════════
# ESSENTIAL BUILT-IN FUNCTIONS
# ═══════════════════════════════════════════════════════════════

# Type conversion
int("42")       # 42
float("3.14")   # 3.14
str(42)         # "42"
bool(1)         # True
list("abc")     # ['a', 'b', 'c']
tuple([1,2,3])  # (1, 2, 3)

# Math functions
abs(-5)         # 5
pow(2, 3)       # 8 (same as 2**3)
round(3.7)      # 4
round(3.14159, 2)  # 3.14
min(1, 2, 3)    # 1
max(1, 2, 3)    # 3
sum([1,2,3])    # 6

# Sequence functions
len("hello")    # 5
sorted([3,1,2]) # [1, 2, 3]
reversed([1,2,3])  # iterator

# Input/Output
print("Hello")      # Output
input("Enter: ")    # Input (returns string!)

# Type checking
type(42)            # <class 'int'>
isinstance(42, int) # True

# Range
range(5)            # 0, 1, 2, 3, 4
range(1, 6)         # 1, 2, 3, 4, 5
range(0, 10, 2)     # 0, 2, 4, 6, 8

# Enumerate
list(enumerate(['a','b','c']))  # [(0,'a'), (1,'b'), (2,'c')]

# Zip
list(zip([1,2], ['a','b']))  # [(1,'a'), (2,'b')]
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: print() vs return
def add(a, b):
    print(a + b)  # Just displays, returns None!

result = add(2, 3)  # Prints 5
print(result)       # None!

# TRAP 2: Forgetting parentheses when calling
def greet():
    return "Hello"

print(greet)    # <function greet at 0x...>
print(greet())  # Hello

# TRAP 3: Modifying mutable argument
def modify(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify(my_list)
print(my_list)  # [1, 2, 3, 4] - MODIFIED!

# TRAP 4: Parameter order
def func(a, b=10, c=20):
    print(a, b, c)

func(1)           # 1 10 20
func(1, 2)        # 1 2 20
func(1, c=30)     # 1 10 30
# func(b=5, 1)    # SyntaxError! Positional after keyword

# TRAP 5: Multiple return statements
def check(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    # No return for x == 0, returns None!

print(check(0))  # None
```

---

## 📝 Quick Reference

| Concept | Example | Description |
|---------|---------|-------------|
| Define | `def func():` | Create a function |
| Call | `func()` | Execute the function |
| Return | `return value` | Send value back |
| Default | `def f(x=10):` | Default parameter |
| Keyword | `f(x=5)` | Named argument |
| Global | `global x` | Access global variable |
| Docstring | `"""Doc"""` | Function documentation |

---

## 🎯 Exam Checklist

- [ ] `def` keyword creates functions
- [ ] Parameters in definition, arguments in call
- [ ] Default parameters must come AFTER non-defaults
- [ ] Mutable default arguments are dangerous (use None)
- [ ] No return or empty return → returns None
- [ ] Local variables shadow global variables
- [ ] Use `global` keyword to modify global variables
- [ ] Positional arguments must come before keyword arguments
- [ ] Functions are objects (can be passed around)

---

[[12_Dictionaries|← Dictionaries]] | [[00_Index|Index]] | [[14_Functions_Advanced|Functions Advanced →]]
