---
title: Scope and Closures
tags: [python, scope, closures, LEGB, functions, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# 🔭 Scope and Closures

[[00_Index|← Back to Index]] | [[10_A_Scope_LEGB_Visual_Guide|Visual Guide →]]

> **Understand how Python finds variables and how closures work**

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║        🔭 LEGB REGEL - WO FINDET PYTHON VARIABLEN?            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   LEGB = Local, Enclosing, Global, Built-in                  ║
║                                                               ║
║   ╔════════════════════════════════════════════════╗          ║
║   ║  BUILT-IN: print, len, str, int, range, etc.  ║          ║
║   ║  ╔══════════════════════════════════════════╗ ║          ║
║   ║  ║  GLOBAL: Top-Level Variablen des Moduls ║ ║          ║
║   ║  ║  x = 10                                  ║ ║          ║
║   ║  ║  ╔════════════════════════════════════╗ ║ ║          ║
║   ║  ║  ║  ENCLOSING: Äußere Funktion       ║ ║ ║          ║
║   ║  ║  ║  y = 20                            ║ ║ ║          ║
║   ║  ║  ║  ╔══════════════════════════════╗ ║ ║ ║          ║
║   ║  ║  ║  ║  LOCAL: Aktuelle Funktion    ║ ║ ║ ║          ║
║   ║  ║  ║  ║  z = 30                      ║ ║ ║ ║          ║
║   ║  ║  ║  ║  Suche: z → y → x → Built-in║ ║ ║ ║          ║
║   ║  ║  ║  ╚══════════════════════════════╝ ║ ║ ║          ║
║   ║  ║  ╚════════════════════════════════════╝ ║ ║          ║
║   ║  ╚══════════════════════════════════════════╝ ║          ║
║   ╚════════════════════════════════════════════════╝          ║
║                                                               ║
║   Suchrichtung: INNEN nach AUSSEN ←─────────────────         ║
║   Python stoppt, sobald es findet!                            ║
║                                                               ║
║   💡 LEGB wird von innen nach außen durchsucht               ║
║   💡 Zuerst Local, dann Enclosing, dann Global, zuletzt Built-in ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 🎯 What is Scope?

**Scope** determines where a variable is visible and accessible.

Python uses the **LEGB Rule** to find variables:

| Scope | Description | Example |
|-------|----------|---------|
| **L**ocal | Within the current function | `def func(): x = 1` |
| **E**nclosing | In enclosing functions | Nested functions |
| **G**lobal | At module level | Top-level in script |
| **B**uilt-in | Python's built-in names | `print`, `len`, `str` |

```
┌─────────────────────────────────────────────┐
│  Built-in (print, len, str, int, ...)       │
│  ┌───────────────────────────────────────┐  │
│  │  Global (Module Level)                │  │
│  │  ┌─────────────────────────────────┐  │  │
│  │  │  Enclosing (Outer Function)     │  │  │
│  │  │  ┌───────────────────────────┐  │  │  │
│  │  │  │  Local (Current Function) │  │  │  │
│  │  │  └───────────────────────────┘  │  │  │
│  │  └─────────────────────────────────┘  │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
     Python searches from INSIDE to OUTSIDE
```

---

## 📦 LEGB in Action

### Basic LEGB Demo

```python
# Global scope
x = "global"

def outer():
    # Enclosing scope
    x = "enclosing"

    def inner():
        # Local scope
        x = "local"
        print(f"Inner sees: {x}")  # "local"

    inner()
    print(f"Outer sees: {x}")  # "enclosing"

outer()
print(f"Global sees: {x}")  # "global"

# Output:
# Inner sees: local
# Outer sees: enclosing
# Global sees: global
```

### Scope Search Visualized

```python
name = "Global"  # Global scope

def greet():
    # No local 'name' → searches in Global
    print(f"Hello, {name}!")

greet()  # Hello, Global!

# With local name:
def greet_local():
    name = "Local"  # Local variable shadows Global
    print(f"Hello, {name}!")

greet_local()  # Hello, Local!
print(name)    # "Global" (unchanged!)
```

---

## 🌐 The `global` Keyword

With `global` you can **modify a global variable within a function**.

### Without global (creates new local object)

```python
counter = 0

def increment():
    counter = 1  # Creates NEW local variable!
    print(f"In function: {counter}")

increment()
print(f"Global: {counter}")  # Still 0!

# Output:
# In function: 1
# Global: 0
```

### With global (modifies Global)

```python
counter = 0

def increment():
    global counter  # References the global variable
    counter += 1
    print(f"In function: {counter}")

increment()  # In function: 1
increment()  # In function: 2
print(f"Global: {counter}")  # 2
```

### ⚠️ Warning: UnboundLocalError

```python
x = 10

def problematic():
    print(x)  # ❌ UnboundLocalError!
    x = 20    # This line makes x local for the ENTIRE function

# Python scans the function BEFORE execution
# and sees "x = 20" → x is local
# Then print(x) tries to read a local variable
# that doesn't exist yet → Error!

# Solution 1: global
def fixed_global():
    global x
    print(x)  # 10
    x = 20

# Solution 2: Use different name
def fixed_different():
    print(x)  # Reads global
    y = 20    # New local variable
```

---

## 🔗 The `nonlocal` Keyword

`nonlocal` allows access to variables from the **Enclosing Scope** (not Global!).

```python
def outer():
    count = 0  # Enclosing scope

    def inner():
        nonlocal count  # References count from outer()
        count += 1
        return count

    return inner

counter = outer()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

### global vs nonlocal

```python
x = "global"

def outer():
    x = "enclosing"

    def inner_global():
        global x
        x = "modified by inner_global"

    def inner_nonlocal():
        nonlocal x
        x = "modified by inner_nonlocal"

    inner_nonlocal()
    print(f"After nonlocal: {x}")  # "modified by inner_nonlocal"

    inner_global()
    print(f"After global: {x}")  # "modified by inner_nonlocal" (unchanged!)

outer()
print(f"Global x: {x}")  # "modified by inner_global"
```

**Comparison:**

| Keyword | Target | Usage |
|---------|--------|-------|
| `global` | Module-level variable | Rarely, mostly avoid |
| `nonlocal` | Enclosing Function Variable | For closures |

---

## 🎁 Closures

A **Closure** is a function that retains access to variables from its Enclosing Scope even after the outer function has finished executing.

### Basic Concept

```python
def make_multiplier(factor):
    """Factory function that returns a closure"""

    def multiplier(number):
        # 'factor' comes from enclosing scope
        return number * factor

    return multiplier  # Returns the inner function

# Create specialized functions
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
print(double(10))  # 20

# double "remembers" factor=2
# triple "remembers" factor=3
```

### Closure as Counter

```python
def create_counter(start=0):
    """Creates a counter with state"""
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

# Two independent counters
counter_a = create_counter(0)
counter_b = create_counter(100)

print(counter_a())  # 1
print(counter_a())  # 2
print(counter_b())  # 101
print(counter_a())  # 3
print(counter_b())  # 102
```

### Inspecting Closures

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

closure = outer(10)

# Display closure variables
print(closure.__closure__)  # (<cell at 0x...: int object at 0x...>,)
print(closure.__closure__[0].cell_contents)  # 10

# Free variables (from enclosing scope)
print(closure.__code__.co_freevars)  # ('x',)
```

---

## 🏭 Practical Closure Patterns

### 1. Function Factory

```python
def create_validator(min_val, max_val):
    """Creates validation function for range"""

    def validate(value):
        if min_val <= value <= max_val:
            return True
        raise ValueError(f"Value must be between {min_val} and {max_val}")

    return validate

# Specialized validators
validate_age = create_validator(0, 150)
validate_percentage = create_validator(0, 100)
validate_temperature = create_validator(-273.15, 1000)

print(validate_age(25))        # True
print(validate_percentage(75)) # True
# validate_age(200)            # ValueError!
```

### 2. Memoization (Caching)

```python
def memoize(func):
    """Closure for caching function results"""
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Without memoization: exponentially slow
# With memoization: linearly fast
print(fibonacci(100))  # 354224848179261915075 (instantly!)
```

### 3. Logger with Context

```python
def create_logger(prefix):
    """Logger with fixed prefix"""

    def log(message, level="INFO"):
        print(f"[{prefix}] {level}: {message}")

    return log

# Specialized loggers
db_log = create_logger("DATABASE")
api_log = create_logger("API")

db_log("Connection established")  # [DATABASE] INFO: Connection established
api_log("Request received")       # [API] INFO: Request received
db_log("Query failed", "ERROR")   # [DATABASE] ERROR: Query failed
```

---

## ⚠️ Common Pitfall: Late Binding

```python
# ❌ PROBLEM: Late Binding in Loops
functions = []
for i in range(3):
    functions.append(lambda: i)

for f in functions:
    print(f())  # 2, 2, 2 (not 0, 1, 2!)

# i is looked up only at CALL TIME,
# not at definition time!
# After the loop i = 2
```

**Solution: Default Argument**

```python
# ✅ SOLUTION: "Freeze" value at definition
functions = []
for i in range(3):
    functions.append(lambda i=i: i)  # Default arg captures value

for f in functions:
    print(f())  # 0, 1, 2 ✓
```

---

## 📋 Scope Rules Summary

```python
# 1. Reading: Python searches LEGB (Local → Enclosing → Global → Built-in)
# 2. Writing: ALWAYS creates local variable (except global/nonlocal)
# 3. global: Access module-level variable
# 4. nonlocal: Access Enclosing-Scope variable

# Memory aid:
# - Without keyword: Read from anywhere, write only locally
# - global: "I mean the outermost one"
# - nonlocal: "I mean the one level higher"
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Closures for state management | `global` for communication between functions |
| Use `nonlocal` in closures | Too many nested scopes |
| Factory functions for specialized functions | Mutable objects in closures without consideration |
| Keep functions small and focused | Ignore late binding in loops |

---

## 🎯 Exam Checklist

- [ ] Explain the LEGB rule
- [ ] Difference between `global` and `nonlocal`
- [ ] Define closure and give an example
- [ ] Explain UnboundLocalError
- [ ] Late binding problem and solution

---

[[09_Lambda_and_Built-ins|← Lambda]] | [[00_Index|Index]] | [[11_Classes_and_OOP|Classes →]]
