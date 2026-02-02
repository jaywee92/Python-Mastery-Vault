---
title: Iterators and Generators
tags: [python, generators, iterators, yield, memory, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: advanced
---

# 🔄 Iterators and Generators

[[00_Index|← Back to Index]] | [[26_Working_with_Dates|← Working with Dates]] | [[28_Decorators|Decorators →]]

> **"Generators are lazy - and that's a good thing!"**

---

## 🎯 The Concept: Lazy Evaluation

```
┌─────────────────────────────────────────────────────────────────┐
│              LIST VS GENERATOR                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  LIST: [1, 2, 3, 4, 5]                                          │
│  ├── All elements in memory immediately                         │
│  ├── Can be iterated multiple times                             │
│  ├── Index access possible: list[2]                             │
│  └── len() works                                                 │
│                                                                  │
│  GENERATOR: (x for x in range(5))                               │
│  ├── Creates elements only on demand (lazy)                     │
│  ├── Only iterable once                                         │
│  ├── NO index access                                            │
│  └── NO len()                                                    │
│                                                                  │
│  ADVANTAGE: Extremely memory efficient with large datasets!     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔁 Iterator Protocol

Every iterable object implements the iterator protocol:

```python
# ═══════════════════════════════════════════════════════════════
# THE ITERATOR PROTOCOL
# ═══════════════════════════════════════════════════════════════

# __iter__() - Returns an iterator
# __next__() - Returns the next element, or StopIteration

# How a for-loop works internally:
numbers = [1, 2, 3]

# Manual:
iterator = iter(numbers)          # Calls numbers.__iter__()
print(next(iterator))             # 1 - Calls iterator.__next__()
print(next(iterator))             # 2
print(next(iterator))             # 3
# print(next(iterator))           # StopIteration!

# Create your own iterator
class Counter:
    """Counts from 0 to max-1."""

    def __init__(self, max_value):
        self.max = max_value

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.max:
            result = self.n
            self.n += 1
            return result
        raise StopIteration

# Usage
for i in Counter(3):
    print(i)                      # 0, 1, 2
```

---

## ⚡ Generator Functions

Functions with `yield` instead of `return`:

```python
# ═══════════════════════════════════════════════════════════════
# GENERATOR FUNCTION - WITH YIELD
# ═══════════════════════════════════════════════════════════════
def countdown(n):
    """Counts down from n to 1."""
    while n > 0:
        yield n                   # Pauses here and returns n
        n -= 1                    # Resumes at next next() call

# Calling creates generator object (doesn't execute yet!)
gen = countdown(3)
print(type(gen))                  # <class 'generator'>

# Iterate
print(next(gen))                  # 3
print(next(gen))                  # 2
print(next(gen))                  # 1
# print(next(gen))                # StopIteration

# Or with for-loop
for i in countdown(3):
    print(i)                      # 3, 2, 1
```

### yield vs return

```python
# ═══════════════════════════════════════════════════════════════
# DIFFERENCE: YIELD VS RETURN
# ═══════════════════════════════════════════════════════════════

# return - Function ends, value is returned
def get_squares_list(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result                 # All at once

# yield - Function "pauses", generates values on demand
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2              # One at a time

# Comparison
list_result = get_squares_list(1000000)  # 1M elements in memory!
gen_result = get_squares_gen(1000000)    # Almost no memory

# Memory comparison
import sys
print(sys.getsizeof(get_squares_list(1000)))  # ~8.5 KB
print(sys.getsizeof(get_squares_gen(1000)))   # ~120 Bytes!
```

---

## 📝 Generator Expressions

Like list comprehensions, but with parentheses:

```python
# ═══════════════════════════════════════════════════════════════
# GENERATOR EXPRESSION
# ═══════════════════════════════════════════════════════════════

# List comprehension (creates list)
squares_list = [x**2 for x in range(10)]

# Generator expression (creates generator)
squares_gen = (x**2 for x in range(10))

# In functions often directly without extra parentheses
total = sum(x**2 for x in range(10))        # ✅ Elegant
total = sum((x**2 for x in range(10)))      # ✅ Also OK

# Comparison
big_list = [x for x in range(10_000_000)]   # ~400 MB memory!
big_gen = (x for x in range(10_000_000))    # ~120 Bytes!

# ═══════════════════════════════════════════════════════════════
# WHEN LIST VS GENERATOR?
# ═══════════════════════════════════════════════════════════════

# ✅ GENERATOR when:
# - Large datasets
# - Only iterated once
# - Memory is important
# - Streaming data

# ✅ LIST when:
# - Iterated multiple times
# - Index access needed
# - len() needed
# - Small datasets
```

---

## 🔄 Practical Generator Examples

### Fibonacci Sequence (infinite)

```python
def fibonacci():
    """Infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:                   # Infinite!
        yield a
        a, b = b, a + b

# Limit with islice
from itertools import islice

fib = fibonacci()
first_10 = list(islice(fib, 10))
print(first_10)                   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Read file line by line

```python
def read_large_file(file_path):
    """Reads large file memory efficiently."""
    with open(file_path, 'r') as f:
        for line in f:
            yield line.strip()

# Process without loading everything into memory
for line in read_large_file('huge_log.txt'):
    if 'ERROR' in line:
        print(line)
```

### Pipeline with multiple generators

```python
def read_lines(filename):
    """Step 1: Read lines."""
    with open(filename) as f:
        for line in f:
            yield line.strip()

def filter_comments(lines):
    """Step 2: Filter comments."""
    for line in lines:
        if not line.startswith('#'):
            yield line

def parse_numbers(lines):
    """Step 3: Convert to numbers."""
    for line in lines:
        try:
            yield int(line)
        except ValueError:
            pass

# Assemble pipeline (lazy!)
numbers = parse_numbers(
    filter_comments(
        read_lines('data.txt')
    )
)

# Only now is it really processed
total = sum(numbers)
```

---

## 🔀 yield from

Delegates to another generator:

```python
# ═══════════════════════════════════════════════════════════════
# YIELD FROM - DELEGATION
# ═══════════════════════════════════════════════════════════════

# Without yield from
def chain_manual(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

# With yield from (more elegant!)
def chain(*iterables):
    for iterable in iterables:
        yield from iterable

# Usage
list(chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]

# Recursive generators
def flatten(nested):
    """Flattens nested lists."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # Recursive delegation
        else:
            yield item

list(flatten([1, [2, 3], [[4, 5], 6]]))  # [1, 2, 3, 4, 5, 6]
```

---

## 📨 Generator with .send()

Generators can also receive values:

```python
# ═══════════════════════════════════════════════════════════════
# BIDIRECTIONAL GENERATORS
# ═══════════════════════════════════════════════════════════════

def running_average():
    """Calculates running average."""
    total = 0
    count = 0
    average = None

    while True:
        value = yield average     # Returns average, receives value
        if value is not None:
            total += value
            count += 1
            average = total / count

# Usage
avg = running_average()
next(avg)                         # Initialize (None)
print(avg.send(10))               # 10.0
print(avg.send(20))               # 15.0
print(avg.send(30))               # 20.0
```

---

## 🛑 Close generator

```python
def counter():
    try:
        n = 0
        while True:
            yield n
            n += 1
    except GeneratorExit:
        print("Generator is closing")
    finally:
        print("Cleanup")

gen = counter()
print(next(gen))                  # 0
print(next(gen))                  # 1
gen.close()                       # "Generator is closing" + "Cleanup"
```

---

## 📊 Comparison: List vs Generator

| Aspect | List | Generator |
|--------|------|-----------|
| Syntax | `[x for x in ...]` | `(x for x in ...)` |
| Memory | All at once | Only current element |
| Iteration | Multiple | Only once |
| Index access | `list[i]` | Not possible |
| `len()` | ✅ Yes | ❌ No |
| Performance | Faster for small | Better for large |

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Use generator multiple times
gen = (x for x in range(3))
print(list(gen))                  # [0, 1, 2]
print(list(gen))                  # [] - Already exhausted!

# ✅ RIGHT: Use generator function
def get_gen():
    return (x for x in range(3))

print(list(get_gen()))            # [0, 1, 2]
print(list(get_gen()))            # [0, 1, 2]

# ❌ WRONG: len() on generator
gen = (x for x in range(3))
# len(gen)                        # TypeError!

# ✅ RIGHT: Convert to list first (if needed)
data = list(gen)
print(len(data))                  # 3

# ❌ WRONG: Generator expression instead of yield in function
def bad():
    numbers = (x for x in range(10))  # Local generator
    return numbers                     # Works, but unusual

# ✅ RIGHT: Use yield directly
def good():
    for x in range(10):
        yield x
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Generator for large datasets | List for millions of elements |
| `yield from` for delegation | Nested for-loops |
| Generator expression in `sum()`, `max()` etc. | Create list first |
| Generator for one-time iteration | Use generator multiple times |
| Pipeline with multiple generators | Everything in one function |

---

## 🎯 Exam Checklist

- [ ] Difference between Iterator vs Generator vs Iterable
- [ ] `yield` vs `return`
- [ ] Generator expression syntax `(x for x in ...)`
- [ ] `next()` and `StopIteration`
- [ ] `yield from` for delegation
- [ ] Memory efficiency of generators
- [ ] Iterator protocol: `__iter__()` and `__next__()`
- [ ] Generator can only be iterated once
- [ ] `islice()` for infinite generators

---

[[26_Working_with_Dates|← Working with Dates]] | [[00_Index|Index]] | [[28_Decorators|Decorators →]]
