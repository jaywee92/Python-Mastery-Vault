---
title: Python Advanced - Cheatsheet
tags: [python, advanced, cheatsheet, reference]
created: 2026-02-01
---

# 🚀 Python Advanced - Cheatsheet

---

## 📦 Object-Oriented Programming

```python
class Animal:
    species = "Unknown"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

    def speak(self):
        return "..."

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def is_animal():
        return True

class Dog(Animal):  # Inheritance
    species = "Canine"

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):  # Override
        return "Woof!"

# Usage
dog = Dog("Buddy", "Labrador")
dog.speak()  # "Woof!"
```

---

## 🔮 Magic Methods (Dunder)

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):          # str(obj), print(obj)
        return f"({self.x}, {self.y})"

    def __repr__(self):         # repr(obj), debugging
        return f"Vector({self.x}, {self.y})"

    def __len__(self):          # len(obj)
        return 2

    def __add__(self, other):   # obj + other
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):    # obj == other
        return self.x == other.x and self.y == other.y

    def __getitem__(self, i):   # obj[i]
        return (self.x, self.y)[i]

    def __iter__(self):         # for x in obj
        yield self.x
        yield self.y
```

---

## 🎭 Decorators

```python
# Function decorator
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

# Built-in decorators
@property           # Getter
@setter             # Setter
@classmethod        # Class method
@staticmethod       # Static method
```

---

## 🔄 Iterators & Generators

```python
# Iterator
class Counter:
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.max:
            raise StopIteration
        self.n += 1
        return self.n

# Generator function
def count_up(max):
    n = 1
    while n <= max:
        yield n
        n += 1

# Generator expression
squares = (x**2 for x in range(10))

# Useful generator functions
import itertools
itertools.count(10)      # 10, 11, 12, ...
itertools.cycle([1,2,3]) # 1, 2, 3, 1, 2, 3, ...
itertools.chain([1,2], [3,4])  # 1, 2, 3, 4
```

---

## 📋 Comprehensions

```python
# List comprehension
[x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

[x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Dict comprehension
{x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
{x % 3 for x in range(10)}
# {0, 1, 2}

# Generator expression
(x**2 for x in range(5))
# <generator object>

# Nested comprehension
[[j for j in range(3)] for i in range(3)]
# [[0,1,2], [0,1,2], [0,1,2]]
```

---

## 🔗 Context Managers

```python
# Using with
with open("file.txt") as f:
    content = f.read()

# Custom context manager (class)
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        print(f"Elapsed: {time.time() - self.start:.2f}s")

with Timer():
    do_something()

# Using @contextmanager
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start:.2f}s")
```

---

## 📦 Modules & Packages

```python
# Import styles
import module
from module import func
from module import func as f
from module import *  # Avoid!

# Package structure
# mypackage/
#   __init__.py
#   module1.py
#   subpackage/
#     __init__.py
#     module2.py

# Relative imports
from . import module1
from ..subpackage import module2

# __name__ == "__main__"
if __name__ == "__main__":
    main()  # Only runs if executed directly
```

---

## 🧵 Lambda & Functional

```python
# Lambda
double = lambda x: x * 2
add = lambda x, y: x + y

# Map
list(map(lambda x: x**2, [1,2,3]))
# [1, 4, 9]

# Filter
list(filter(lambda x: x > 0, [-1,0,1,2]))
# [1, 2]

# Reduce
from functools import reduce
reduce(lambda a,b: a+b, [1,2,3,4])
# 10

# Sorted with key
sorted(words, key=lambda w: len(w))
sorted(items, key=lambda x: x[1], reverse=True)
```

---

## 🏷️ Type Hints

```python
# Basic types
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Collections
from typing import List, Dict, Tuple, Optional

def process(items: List[int]) -> Dict[str, int]:
    return {"sum": sum(items)}

def find(x: int) -> Optional[str]:
    return None if x < 0 else str(x)

# Union
from typing import Union
def handle(x: Union[int, str]) -> None:
    pass
```

---

## 🧪 Testing

```python
import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        # Runs before each test
        pass

    def test_add(self):
        self.assertEqual(1 + 1, 2)
        self.assertTrue(1 < 2)
        self.assertFalse(1 > 2)
        self.assertRaises(ValueError, int, "abc")

if __name__ == "__main__":
    unittest.main()

# pytest (simpler)
def test_add():
    assert 1 + 1 == 2
```

---

## 🎯 Quick Tips

| Concept | Key Point |
|---------|-----------|
| `super()` | Call parent class method |
| `@property` | Define getter as attribute |
| `yield` | Creates generator |
| `*args` | Tuple of positional args |
| `**kwargs` | Dict of keyword args |
| `__name__` | Current module name |
| `with` | Context manager |
| `typing` | Type hint module |

---

[[00_Index|← Back to Index]]
