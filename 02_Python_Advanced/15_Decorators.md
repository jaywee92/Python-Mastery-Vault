---
title: Decorators
tags: [python, decorators, metaprogramming, functools, exam-essential]
created: 2026-01-27
exam_weight: high
difficulty: advanced
---

# 🎀 Decorators

[[00_Index|← Back to Index]] | [[14_Iterators_and_Generators|← Iterators and Generators]] | [[16_Context_Managers|Context Managers →]]

> **"Decorators are Python's most elegant way to extend functions."**

---

## 🎯 The Concept: Functions as First-Class Objects

```
┌─────────────────────────────────────────────────────────────────┐
│              WHAT IS A DECORATOR?                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  WITHOUT DECORATOR:                                              │
│  ┌─────────────────┐                                            │
│  │   my_function   │ → Normal function                          │
│  └─────────────────┘                                            │
│                                                                  │
│  WITH DECORATOR:                                                 │
│  ┌─────────────────┐      ┌─────────────────┐                   │
│  │    @decorator   │  →   │   my_function   │                   │
│  └─────────────────┘      └─────────────────┘                   │
│          │                         │                             │
│          └─────────┬───────────────┘                            │
│                    ▼                                             │
│          ┌─────────────────┐                                    │
│          │ Extended Func   │ → Additional behavior!              │
│          └─────────────────┘                                    │
│                                                                  │
│  A decorator "wraps" a function and extends it.                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Functions are Objects

Before we understand decorators, we need to understand that functions in Python are objects:

```python
# ═══════════════════════════════════════════════════════════════
# FUNCTIONS ARE OBJECTS IN PYTHON
# ═══════════════════════════════════════════════════════════════

def greet(name):
    return f"Hello, {name}!"

# Assign function to variable
say_hello = greet
print(say_hello("World"))      # Hello, World!

# Pass function as argument
def call_twice(func, arg):
    return func(arg) + " " + func(arg)

print(call_twice(greet, "Python"))  # Hello, Python! Hello, Python!

# Define function inside a function
def outer():
    def inner():
        return "I am inside!"
    return inner

my_func = outer()
print(my_func())              # I am inside!

# Functions have attributes
print(greet.__name__)         # greet
print(greet.__doc__)          # None (or docstring)
```

---

## ⚡ The First Decorator

```python
# ═══════════════════════════════════════════════════════════════
# A SIMPLE DECORATOR
# ═══════════════════════════════════════════════════════════════

def my_decorator(func):
    """A decorator is a function that takes a function
    and returns an extended function."""

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

# Manual application (old method)
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
# Output:
# Before function
# Hello!
# After function

# With @ syntax (modern method - syntactic sugar!)
@my_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye()
# Output:
# Before function
# Goodbye!
# After function

# ═══════════════════════════════════════════════════════════════
# @decorator is identical to:
# function = decorator(function)
# ═══════════════════════════════════════════════════════════════
```

---

## 📝 Decorator with Function Arguments

```python
# ═══════════════════════════════════════════════════════════════
# WRAPPER WITH *ARGS AND **KWARGS
# ═══════════════════════════════════════════════════════════════

def logging_decorator(func):
    """Logs every function call."""

    def wrapper(*args, **kwargs):
        print(f"Call: {func.__name__}")
        print(f"  Args: {args}")
        print(f"  Kwargs: {kwargs}")

        result = func(*args, **kwargs)

        print(f"  Return: {result}")
        return result

    return wrapper

@logging_decorator
def add(a, b):
    return a + b

@logging_decorator
def greet(name, message="Welcome"):
    return f"{message}, {name}!"

# Usage
add(3, 5)
# Output:
# Call: add
#   Args: (3, 5)
#   Kwargs: {}
#   Return: 8

greet("Anna", message="Good day")
# Output:
# Call: greet
#   Args: ('Anna',)
#   Kwargs: {'message': 'Good day'}
#   Return: Good day, Anna!
```

---

## ⏱️ Practical Example: Timer Decorator

```python
# ═══════════════════════════════════════════════════════════════
# TIMER DECORATOR - MEASURES EXECUTION TIME
# ═══════════════════════════════════════════════════════════════
import time

def timer(func):
    """Measures execution time of a function."""

    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        duration = end_time - start_time
        print(f"{func.__name__} took {duration:.4f} seconds")

        return result

    return wrapper

@timer
def slow_function():
    """Simulates slow operation."""
    time.sleep(1)
    return "Done!"

@timer
def calculate_sum(n):
    """Calculates sum from 1 to n."""
    return sum(range(1, n + 1))

# Test
slow_function()           # slow_function took 1.0012 seconds
calculate_sum(1_000_000)    # calculate_sum took 0.0234 seconds
```

---

## 🔄 functools.wraps - Preserve Metadata

```python
# ═══════════════════════════════════════════════════════════════
# PROBLEM: LOST METADATA
# ═══════════════════════════════════════════════════════════════

def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def my_function():
    """This is my documentation."""
    pass

print(my_function.__name__)    # wrapper ❌ (should be my_function)
print(my_function.__doc__)     # None ❌ (should be docstring)

# ═══════════════════════════════════════════════════════════════
# SOLUTION: @functools.wraps
# ═══════════════════════════════════════════════════════════════
from functools import wraps

def good_decorator(func):
    @wraps(func)                   # ← Copies metadata!
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def my_function():
    """This is my documentation."""
    pass

print(my_function.__name__)    # my_function ✅
print(my_function.__doc__)     # This is my documentation. ✅
```

**Remember:** ALWAYS use `@wraps(func)` in your decorators!

---

## 🎯 Decorator WITH Arguments

```python
# ═══════════════════════════════════════════════════════════════
# DECORATOR THAT TAKES ITS OWN ARGUMENTS
# ═══════════════════════════════════════════════════════════════
from functools import wraps

# A decorator with arguments needs an additional level!
def repeat(times):
    """Executes the decorated function multiple times."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Hello!
# Hello!
# Hello!

# ═══════════════════════════════════════════════════════════════
# STRUCTURE: 3 NESTED LEVELS
# ═══════════════════════════════════════════════════════════════
#
# @repeat(3)          ← repeat(3) is called, returns decorator
# def func():         ← decorator(func) is called, returns wrapper
#     pass            ← wrapper is executed on each call
#
# Equivalent to: func = repeat(3)(func)
```

### Another Example: Rate Limiter

```python
from functools import wraps
import time

def rate_limit(max_calls, period):
    """Limits calls to max_calls per period seconds."""

    calls = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()

            # Remove old calls
            calls[:] = [c for c in calls if now - c < period]

            if len(calls) >= max_calls:
                raise Exception(f"Rate limit: max {max_calls} calls per {period}s")

            calls.append(now)
            return func(*args, **kwargs)

        return wrapper
    return decorator

@rate_limit(max_calls=3, period=10)
def api_call():
    print("API called!")

# Works 3x, then exception
```

---

## 🔗 Stack Multiple Decorators

```python
# ═══════════════════════════════════════════════════════════════
# DECORATOR STACKING
# ═══════════════════════════════════════════════════════════════
from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

def underline(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper

@bold
@italic
@underline
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
# <b><i><u>Hello, World!</u></i></b>

# ═══════════════════════════════════════════════════════════════
# ORDER: BOTTOM TO TOP!
# ═══════════════════════════════════════════════════════════════
#
# @bold              ← 3. Applied last (outermost)
# @italic            ← 2.
# @underline         ← 1. Applied first (innermost)
# def greet():
#
# Equivalent to: greet = bold(italic(underline(greet)))
```

---

## 🏛️ Class Decorators

### Decorator as Class

```python
# ═══════════════════════════════════════════════════════════════
# DECORATOR AS CLASS (WITH __call__)
# ═══════════════════════════════════════════════════════════════

class CountCalls:
    """Counts how many times a function was called."""

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} was called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()                  # say_hello was called 1 times
say_hello()                  # say_hello was called 2 times
print(say_hello.count)       # 2
```

### Decorate Classes

```python
# ═══════════════════════════════════════════════════════════════
# DECORATE A CLASS
# ═══════════════════════════════════════════════════════════════

def singleton(cls):
    """Ensures only one instance exists."""
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Database initialized")
        self.connection = "Connected"

# Test
db1 = Database()              # Database initialized
db2 = Database()              # Nothing! Same instance
print(db1 is db2)             # True
```

---

## 📚 Built-in Decorators

```python
# ═══════════════════════════════════════════════════════════════
# PYTHON'S BUILT-IN DECORATORS
# ═══════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────
# @staticmethod - Doesn't need self
# ─────────────────────────────────────────────────────────────
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

print(MathHelper.add(2, 3))   # 5 (without instance!)

# ─────────────────────────────────────────────────────────────
# @classmethod - Receives class instead of instance
# ─────────────────────────────────────────────────────────────
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def from_string(cls, data):
        name = data.split(",")[0]
        return cls(name)

p = Person.from_string("Anna,25")
print(Person.get_count())     # 1

# ─────────────────────────────────────────────────────────────
# @property - Getter/Setter/Deleter
# ─────────────────────────────────────────────────────────────
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter for radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for radius."""
        if value < 0:
            raise ValueError("Radius must be positive!")
        self._radius = value

    @property
    def area(self):
        """Calculated property (read-only)."""
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print(c.radius)               # 5
print(c.area)                 # 78.54...
c.radius = 10                 # Setter called
# c.area = 100                # AttributeError: can't set
```

---

## 🚀 functools Decorators

```python
# ═══════════════════════════════════════════════════════════════
# FUNCTOOLS DECORATORS
# ═══════════════════════════════════════════════════════════════
from functools import lru_cache, cache, cached_property

# ─────────────────────────────────────────────────────────────
# @lru_cache - Memoization (cache results)
# ─────────────────────────────────────────────────────────────
@lru_cache(maxsize=128)
def fibonacci(n):
    """Calculates n-th Fibonacci number with caching."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Without cache: extremely slow for large n
# With cache: lightning fast!
print(fibonacci(100))         # 354224848179261915075

# Show cache info
print(fibonacci.cache_info())
# CacheInfo(hits=98, misses=101, maxsize=128, currsize=101)

# Clear cache
fibonacci.cache_clear()

# ─────────────────────────────────────────────────────────────
# @cache (Python 3.9+) - Unlimited cache
# ─────────────────────────────────────────────────────────────
@cache
def expensive_operation(x):
    print(f"Calculating {x}...")
    return x ** 2

expensive_operation(5)        # Calculating 5...
expensive_operation(5)        # (nothing - from cache!)

# ─────────────────────────────────────────────────────────────
# @cached_property (Python 3.8+) - Lazy evaluation for properties
# ─────────────────────────────────────────────────────────────
class DataLoader:
    @cached_property
    def data(self):
        """Calculated only once."""
        print("Loading data...")
        return [1, 2, 3, 4, 5]

loader = DataLoader()
print(loader.data)            # Loading data... [1, 2, 3, 4, 5]
print(loader.data)            # [1, 2, 3, 4, 5] (not reloaded!)
```

---

## 🛡️ Practical Decorator Collection

```python
# ═══════════════════════════════════════════════════════════════
# USEFUL DECORATORS FOR DAILY USE
# ═══════════════════════════════════════════════════════════════
from functools import wraps
import time

# ─────────────────────────────────────────────────────────────
# Debug Decorator
# ─────────────────────────────────────────────────────────────
def debug(func):
    """Prints function call and result."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))

        print(f"→ {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"← {func.__name__} = {result!r}")

        return result
    return wrapper

# ─────────────────────────────────────────────────────────────
# Retry Decorator
# ─────────────────────────────────────────────────────────────
def retry(max_attempts=3, delay=1):
    """Retries function multiple times on error."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)

            raise last_exception

        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.5)
def unstable_api():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Server unreachable")
    return "Success!"

# ─────────────────────────────────────────────────────────────
# Type Check Decorator
# ─────────────────────────────────────────────────────────────
def enforce_types(func):
    """Checks types based on type hints."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        hints = func.__annotations__

        # Check arguments
        for name, value in kwargs.items():
            if name in hints:
                expected = hints[name]
                if not isinstance(value, expected):
                    raise TypeError(
                        f"{name} should be {expected.__name__}, "
                        f"but is {type(value).__name__}"
                    )

        return func(*args, **kwargs)

    return wrapper

@enforce_types
def greet(name: str, age: int):
    return f"{name} is {age} years old"

# greet(name="Anna", age="25")  # TypeError!
greet(name="Anna", age=25)      # OK
```

---

## 📊 Visualization: Decorator Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    DECORATOR FLOW                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  DEFINITION:                                                     │
│  @decorator                                                      │
│  def func():           →  func = decorator(func)                │
│      pass                                                        │
│                                                                  │
│  CALL:                                                           │
│                                                                  │
│  func()   ─────────────────┐                                    │
│                            ▼                                     │
│           ┌────────────────────────────────────┐                │
│           │         wrapper()                   │                │
│           │  ┌──────────────────────────────┐  │                │
│           │  │ 1. Before-logic (e.g. print) │  │                │
│           │  ├──────────────────────────────┤  │                │
│           │  │ 2. func(*args, **kwargs)     │ ←│── Original    │
│           │  ├──────────────────────────────┤  │                │
│           │  │ 3. After-logic (e.g. return) │  │                │
│           │  └──────────────────────────────┘  │                │
│           └────────────────────────────────────┘                │
│                            │                                     │
│                            ▼                                     │
│                     Result                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Forget @wraps
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
# Loses __name__, __doc__ etc.

# ✅ RIGHT: Always use @wraps
from functools import wraps
def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# ❌ WRONG: Decorator with arguments without extra level
def bad_repeat(times):     # Missing decorator level!
    @wraps(func)           # NameError: func not defined
    def wrapper(*args, **kwargs):
        pass
    return wrapper

# ✅ RIGHT: 3 levels for decorator with arguments
def good_repeat(times):
    def decorator(func):   # Extra level!
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# ❌ WRONG: Misunderstand decorator order
@A
@B
def func(): pass
# NOT A(func) then B(...)
# INSTEAD: A(B(func)) - B first!

# ❌ WRONG: Decorator on methods without self-handling
def class_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):  # args[0] is self!
        return func(*args, **kwargs)
    return wrapper
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Use `@wraps(func)` | Lose metadata |
| `*args, **kwargs` in wrapper | Fixed signature |
| Small, focused decorators | Huge all-purpose decorators |
| Docstrings for decorators | Undocumented decorators |
| `@lru_cache` for expensive calculations | Manual caching logic |
| Clear naming | Generic names |

---

## 🎯 Exam Checklist

- [ ] Decorator syntax: `@decorator` above function
- [ ] Decorator = function that takes function and returns function
- [ ] `@wraps(func)` from functools for metadata
- [ ] Decorator with arguments: 3 nested functions
- [ ] Order with multiple decorators: bottom to top
- [ ] Built-ins: `@staticmethod`, `@classmethod`, `@property`
- [ ] `@lru_cache` for memoization
- [ ] `*args, **kwargs` in wrapper

---

[[14_Iterators_and_Generators|← Iterators and Generators]] | [[00_Index|Index]] | [[16_Context_Managers|Context Managers →]]
