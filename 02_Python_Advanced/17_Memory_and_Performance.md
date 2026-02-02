---
title: Memory and Performance
tags: [python, performance, memory, optimization, profiling, exam-essential]
created: 2026-01-27
exam_weight: medium
difficulty: advanced
---

# 🚀 Memory and Performance

[[00_Index|← Back to Index]] | [[29_Context_Managers|← Context Managers]]

> **"Premature optimization is the root of all evil - but you should know it anyway!"**

---

## 🎯 The Concept: Efficient Python Code

```
┌─────────────────────────────────────────────────────────────────┐
│              PERFORMANCE OPTIMIZATION                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. MEASURE FIRST, THEN OPTIMIZE!                               │
│     └── Profiling shows where time is really lost               │
│                                                                  │
│  2. MEMORY VS SPEED                                             │
│     ├── More memory = often faster (caching)                    │
│     └── Less memory = often slower (recalculation)              │
│                                                                  │
│  3. CHOOSE THE RIGHT DATA STRUCTURE                             │
│     ├── List: O(n) search, O(1) append                          │
│     ├── Set: O(1) search, add, remove                           │
│     └── Dict: O(1) key lookup                                   │
│                                                                  │
│  4. USE PYTHON'S STRENGTHS                                      │
│     ├── Built-in functions (written in C)                       │
│     ├── List comprehensions                                      │
│     └── Generators for large data                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Measuring Memory with sys.getsizeof

```python
# ═══════════════════════════════════════════════════════════════
# MEASURING MEMORY CONSUMPTION
# ═══════════════════════════════════════════════════════════════
import sys

# Basic types
print(sys.getsizeof(0))           # 28 Bytes (int)
print(sys.getsizeof(1))           # 28 Bytes
print(sys.getsizeof(10**100))     # 72 Bytes (large int)
print(sys.getsizeof(3.14))        # 24 Bytes (float)
print(sys.getsizeof(""))          # 49 Bytes (empty str)
print(sys.getsizeof("a"))         # 50 Bytes
print(sys.getsizeof("hello"))     # 54 Bytes
print(sys.getsizeof([]))          # 56 Bytes (empty list)
print(sys.getsizeof({}))          # 64 Bytes (empty dict)
print(sys.getsizeof(set()))       # 216 Bytes (empty set)

# ═══════════════════════════════════════════════════════════════
# ATTENTION: getsizeof only shows shallow memory!
# ═══════════════════════════════════════════════════════════════

# Shallow memory (only container, not contents!)
lista = [1, 2, 3, 4, 5]
print(sys.getsizeof(lista))       # 104 Bytes (just the list itself)

# For deep measurement: Custom function or pympler
def deep_getsizeof(obj, seen=None):
    """Recursive memory measurement."""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum(deep_getsizeof(k, seen) + deep_getsizeof(v, seen)
                   for k, v in obj.items())
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
        size += sum(deep_getsizeof(i, seen) for i in obj)

    return size

print(deep_getsizeof(lista))      # ~244 Bytes (with all integers)
```

---

## 🆚 List vs Generator vs Tuple

```python
# ═══════════════════════════════════════════════════════════════
# MEMORY COMPARISON: LIST VS GENERATOR
# ═══════════════════════════════════════════════════════════════
import sys

n = 1_000_000

# List: All elements in memory
big_list = [x for x in range(n)]
print(f"List: {sys.getsizeof(big_list):,} Bytes")    # ~8.4 MB

# Generator: Only ~120 Bytes, no matter how large!
big_gen = (x for x in range(n))
print(f"Generator: {sys.getsizeof(big_gen)} Bytes")  # ~200 Bytes

# range: Also extremely memory efficient
big_range = range(n)
print(f"range: {sys.getsizeof(big_range)} Bytes")    # 48 Bytes

# ═══════════════════════════════════════════════════════════════
# WHEN TO USE WHAT?
# ═══════════════════════════════════════════════════════════════

# ✅ Generator when:
# - Large amounts of data
# - Only iterate once
# - Memory is scarce
# - Streaming processing

# ✅ List when:
# - Iterate multiple times
# - Index access needed
# - len() is needed
# - Small amounts of data

# ✅ Tuple when:
# - Immutable data
# - Must be hashable (for set/dict keys)
# - Slightly less memory than list
```

---

## 🎰 __slots__ - Save Memory in Classes

```python
# ═══════════════════════════════════════════════════════════════
# __SLOTS__ - MEMORY OPTIMIZATION FOR CLASSES
# ═══════════════════════════════════════════════════════════════
import sys

# Normal class - uses __dict__ for attributes
class PointNormal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# With __slots__ - fixed attributes, no __dict__
class PointSlots:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory comparison
p1 = PointNormal(1, 2)
p2 = PointSlots(1, 2)

print(sys.getsizeof(p1))          # 48 Bytes
print(sys.getsizeof(p1.__dict__)) # 104 Bytes (additional!)
print(sys.getsizeof(p2))          # 48 Bytes (no __dict__!)

# With many objects, this makes a HUGE difference:
# 1 Million points:
# - Normal: ~150 MB
# - Slots: ~48 MB

# ═══════════════════════════════════════════════════════════════
# LIMITATIONS OF __SLOTS__
# ═══════════════════════════════════════════════════════════════

class SlottedClass:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = SlottedClass(1, 2)
# obj.z = 3  # AttributeError! No new attributes allowed!
# obj.__dict__  # AttributeError! No __dict__ available!

# Inheritance with __slots__
class SlottedChild(SlottedClass):
    __slots__ = ['z']  # Only NEW attributes here!

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
```

---

## ⏱️ Measuring Time

```python
# ═══════════════════════════════════════════════════════════════
# MEASURING TIME
# ═══════════════════════════════════════════════════════════════
import time
import timeit

# ─────────────────────────────────────────────────────────────
# Simple time measurement with time
# ─────────────────────────────────────────────────────────────
start = time.time()
# ... Code here ...
result = sum(range(1_000_000))
end = time.time()
print(f"Duration: {end - start:.4f} seconds")

# More accurate with time.perf_counter()
start = time.perf_counter()
result = sum(range(1_000_000))
end = time.perf_counter()
print(f"Duration: {end - start:.6f} seconds")

# ─────────────────────────────────────────────────────────────
# timeit - For reliable measurements
# ─────────────────────────────────────────────────────────────

# Runs code multiple times and averages
t = timeit.timeit('sum(range(1000))', number=10000)
print(f"10000 runs: {t:.4f}s")

# With setup code
t = timeit.timeit(
    'sorted(data)',
    setup='import random; data = [random.random() for _ in range(1000)]',
    number=1000
)
print(f"1000 sorts: {t:.4f}s")

# Compare functions
def method1():
    return [x**2 for x in range(1000)]

def method2():
    return list(map(lambda x: x**2, range(1000)))

print(timeit.timeit(method1, number=10000))
print(timeit.timeit(method2, number=10000))
```

---

## 🔍 Profiling - Where is the Bottleneck?

```python
# ═══════════════════════════════════════════════════════════════
# CPROFILER - FUNCTION PROFILING
# ═══════════════════════════════════════════════════════════════
import cProfile
import pstats
from io import StringIO

def slow_function():
    total = 0
    for i in range(100000):
        total += i ** 2
    return total

def main():
    for _ in range(10):
        slow_function()

# Run profiling
cProfile.run('main()')

# Or with more control:
profiler = cProfile.Profile()
profiler.enable()

main()

profiler.disable()

# Format results
stream = StringIO()
stats = pstats.Stats(profiler, stream=stream)
stats.sort_stats('cumulative')  # Sort by cumulative time
stats.print_stats(10)           # Top 10 functions
print(stream.getvalue())

# ═══════════════════════════════════════════════════════════════
# LINE_PROFILER - LINE PROFILING (pip install line_profiler)
# ═══════════════════════════════════════════════════════════════

# Decorate functions with @profile
# @profile
# def my_function():
#     ...
#
# Then run with: kernprof -l -v script.py
```

### Memory Profiling

```python
# ═══════════════════════════════════════════════════════════════
# MEMORY PROFILER (pip install memory_profiler)
# ═══════════════════════════════════════════════════════════════

# @profile
# def memory_hungry():
#     a = [1] * 1000000
#     b = [2] * 1000000
#     del b
#     return a
#
# Run with: python -m memory_profiler script.py

# Or tracemalloc (built-in)
import tracemalloc

tracemalloc.start()

# Code that uses memory
big_list = [i for i in range(100000)]

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024:.2f} KB")
print(f"Peak: {peak / 1024:.2f} KB")

tracemalloc.stop()
```

---

## 🚄 Faster Data Structures

```python
# ═══════════════════════════════════════════════════════════════
# CHOOSE THE RIGHT DATA STRUCTURE
# ═══════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────
# List vs Set - Membership testing
# ─────────────────────────────────────────────────────────────
import timeit

data_list = list(range(10000))
data_set = set(range(10000))

# Search for element
print("List 'in':", timeit.timeit('5000 in data_list', globals=globals(), number=10000))
print("Set 'in':", timeit.timeit('5000 in data_set', globals=globals(), number=10000))
# Set is ~100x faster!

# ─────────────────────────────────────────────────────────────
# Dict vs list of tuples - Key lookup
# ─────────────────────────────────────────────────────────────
# Dict: O(1) lookup
users_dict = {'alice': 1, 'bob': 2, 'charlie': 3}
print(users_dict['bob'])  # Instant!

# List of tuples: O(n) lookup
users_list = [('alice', 1), ('bob', 2), ('charlie', 3)]
for name, id in users_list:
    if name == 'bob':
        print(id)
        break

# ─────────────────────────────────────────────────────────────
# collections.deque vs list - For queues
# ─────────────────────────────────────────────────────────────
from collections import deque

# List: append/pop right O(1), but left O(n)!
list_queue = []
list_queue.append(1)      # O(1)
list_queue.pop(0)         # O(n)! Shift all elements

# Deque: append/pop at both ends O(1)
deque_queue = deque()
deque_queue.append(1)     # O(1)
deque_queue.popleft()     # O(1)!

# ─────────────────────────────────────────────────────────────
# Array vs List - For numeric data
# ─────────────────────────────────────────────────────────────
from array import array
import sys

# List: Stores references to Python objects
int_list = [1, 2, 3, 4, 5]
print(sys.getsizeof(int_list))    # 104 Bytes

# Array: Stores raw values (like in C)
int_array = array('i', [1, 2, 3, 4, 5])  # 'i' = signed int
print(sys.getsizeof(int_array))   # 84 Bytes

# For numeric calculations: NumPy!
# import numpy as np
# np_array = np.array([1, 2, 3, 4, 5])
```

---

## ⚡ Optimization Techniques

### String Concatenation

```python
# ═══════════════════════════════════════════════════════════════
# STRING CONCATENATION
# ═══════════════════════════════════════════════════════════════
import timeit

n = 10000

# ❌ SLOW: += in loop
def concat_plus():
    result = ""
    for i in range(n):
        result += str(i)
    return result

# ✅ FAST: join()
def concat_join():
    return "".join(str(i) for i in range(n))

# ✅ FAST: list + join
def concat_list_join():
    parts = []
    for i in range(n):
        parts.append(str(i))
    return "".join(parts)

# Comparison
print("+=:", timeit.timeit(concat_plus, number=100))
print("join:", timeit.timeit(concat_join, number=100))
print("list+join:", timeit.timeit(concat_list_join, number=100))

# join is 5-10x faster than +=!
```

### List Comprehensions vs Loops

```python
# ═══════════════════════════════════════════════════════════════
# LIST COMPREHENSIONS ARE FASTER
# ═══════════════════════════════════════════════════════════════

# ❌ Slower: For-loop with append
def squares_loop():
    result = []
    for x in range(1000):
        result.append(x ** 2)
    return result

# ✅ Faster: List comprehension
def squares_comp():
    return [x ** 2 for x in range(1000)]

# ✅ Sometimes faster for simple operations: map
def squares_map():
    return list(map(lambda x: x ** 2, range(1000)))

# Benchmark
import timeit
print("Loop:", timeit.timeit(squares_loop, number=10000))
print("Comp:", timeit.timeit(squares_comp, number=10000))
print("Map:", timeit.timeit(squares_map, number=10000))

# List comprehension is usually 20-30% faster than loop!
```

### Local vs Global Variables

```python
# ═══════════════════════════════════════════════════════════════
# LOCAL VARIABLES ARE FASTER
# ═══════════════════════════════════════════════════════════════

# Global variable
global_var = 10

def with_global():
    total = 0
    for _ in range(1000000):
        total += global_var  # Global lookup each time
    return total

def with_local():
    local_var = 10           # Copy once
    total = 0
    for _ in range(1000000):
        total += local_var   # Local lookup (faster!)
    return total

# Also for built-ins:
def slow_loop():
    result = []
    for i in range(10000):
        result.append(len(str(i)))  # len and str looked up each time

def fast_loop():
    _len = len              # Cache locally
    _str = str
    result = []
    _append = result.append
    for i in range(10000):
        _append(_len(_str(i)))
```

### Caching with functools

```python
# ═══════════════════════════════════════════════════════════════
# CACHING WITH FUNCTOOLS
# ═══════════════════════════════════════════════════════════════
from functools import lru_cache, cache

# Fibonacci without cache: O(2^n) - EXTREMELY slow
def fib_slow(n):
    if n < 2:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

# With cache: O(n) - Lightning fast!
@lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2:
        return n
    return fib_fast(n-1) + fib_fast(n-2)

# Comparison
import timeit
# print(timeit.timeit('fib_slow(30)', globals=globals(), number=1))  # ~0.3s
print(timeit.timeit('fib_fast(30)', globals=globals(), number=1))    # ~0.00001s

# Cache info
print(fib_fast.cache_info())
# CacheInfo(hits=28, misses=31, maxsize=None, currsize=31)

# Clear cache
fib_fast.cache_clear()
```

---

## 📊 Big-O Complexity

```
┌─────────────────────────────────────────────────────────────────┐
│              BIG-O COMPLEXITY - OVERVIEW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Operation              List      Dict/Set    Deque             │
│  ─────────────────────────────────────────────────────────────  │
│  Index [i]              O(1)      O(1)*       O(n)              │
│  Search (in)            O(n)      O(1)        O(n)              │
│  Append (right)         O(1)      -           O(1)              │
│  Append (left)          O(n)      -           O(1)              │
│  Insert (middle)        O(n)      -           O(n)              │
│  Delete (index)         O(n)      O(1)        O(n)              │
│  Pop (right)            O(1)      -           O(1)              │
│  Pop (left)             O(n)      -           O(1)              │
│  Sort                   O(n log n) -          -                 │
│                                                                  │
│  * Dict: O(1) for key lookup                                    │
│                                                                  │
│  REMEMBER:                                                       │
│  - For search: Use set/dict!                                    │
│  - For queue (FIFO): Use deque!                                 │
│  - For stack (LIFO): list.append/pop is OK                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🧮 NumPy for Numeric Calculations

```python
# ═══════════════════════════════════════════════════════════════
# NUMPY - EXTREMELY FAST FOR NUMERIC OPERATIONS
# ═══════════════════════════════════════════════════════════════
# pip install numpy

import numpy as np
import timeit

n = 1_000_000

# Python list
py_list = list(range(n))

# NumPy array
np_array = np.arange(n)

# Square all elements
def python_squares():
    return [x**2 for x in py_list]

def numpy_squares():
    return np_array ** 2

print("Python:", timeit.timeit(python_squares, number=10))
print("NumPy:", timeit.timeit(numpy_squares, number=10))
# NumPy is 10-100x faster!

# Memory comparison
import sys
print(f"Python List: {sys.getsizeof(py_list) / 1024 / 1024:.2f} MB")
print(f"NumPy Array: {np_array.nbytes / 1024 / 1024:.2f} MB")
# NumPy needs ~8x less memory!
```

---

## 🎯 Checklist: Performance Optimization

```
┌─────────────────────────────────────────────────────────────────┐
│              OPTIMIZATION CHECKLIST                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  □ MEASURE FIRST!                                               │
│    └── cProfile, timeit, memory_profiler                        │
│                                                                  │
│  □ Right data structure?                                        │
│    ├── Many lookups → dict/set                                  │
│    ├── Queue → deque                                            │
│    └── Numeric → numpy                                          │
│                                                                  │
│  □ Generator instead of list?                                   │
│    └── Large data, iterate once                                 │
│                                                                  │
│  □ List comprehension instead of loop?                          │
│                                                                  │
│  □ join() instead of += for strings?                            │
│                                                                  │
│  □ Caching for expensive calculations?                          │
│    └── @lru_cache                                               │
│                                                                  │
│  □ Use built-ins?                                               │
│    └── sum(), min(), max(), sorted() - in C!                    │
│                                                                  │
│  □ __slots__ for many small objects?                            │
│                                                                  │
│  □ Local variables in hot loops?                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Premature optimization
def overly_optimized():
    # Spent hours on micro-optimization
    # of code that takes 0.001% of time
    pass

# ✅ CORRECT: Measure first, then optimize
# cProfile shows WHERE time is lost!

# ❌ WRONG: List for membership tests
if item in huge_list:      # O(n)
    pass

# ✅ CORRECT: Use set
if item in huge_set:       # O(1)
    pass

# ❌ WRONG: String concatenation in loop
result = ""
for s in strings:
    result += s            # New string object each time!

# ✅ CORRECT: join()
result = "".join(strings)  # Allocate once

# ❌ WRONG: Global variable in hot loop
CONSTANT = 10
def hot_loop():
    for i in range(1000000):
        x = i * CONSTANT   # Global lookup!

# ✅ CORRECT: Cache locally
def hot_loop_optimized():
    constant = CONSTANT    # Copy once
    for i in range(1000000):
        x = i * constant   # Local lookup

# ❌ WRONG: List as default argument
def bad_func(data=[]):     # List is shared!
    data.append(1)
    return data

# ✅ CORRECT: None as default
def good_func(data=None):
    if data is None:
        data = []
    data.append(1)
    return data
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Measure first (profiling) | Blind optimization |
| Use built-in functions | Custom implementation |
| Choose right data structure | Always use list |
| Generators for large data | Load everything into lists |
| `@lru_cache` for expensive functions | Manual caching |
| List comprehensions | Explicit loops |
| `"".join()` for strings | `+=` in loops |
| `__slots__` for many objects | Standard classes |

---

## 🎯 Exam Checklist

- [ ] `sys.getsizeof()` for memory measurement
- [ ] `timeit` for time measurement
- [ ] Generator vs list - memory differences
- [ ] `__slots__` for memory optimization
- [ ] Big-O complexity of data structures
- [ ] `@lru_cache` for memoization
- [ ] String concatenation with `join()`
- [ ] List comprehension faster than loop
- [ ] Set/dict for O(1) lookup

---

[[29_Context_Managers|← Context Managers]] | [[00_Index|Index]]
