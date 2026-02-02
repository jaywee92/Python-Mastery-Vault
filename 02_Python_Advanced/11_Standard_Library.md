---
title: Standard Library
tags: [python, stdlib, standard-library, modules, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# 📚 Standard Library

[[00_Index|← Back to Index]] | [[10_Common_Pitfalls|← Common Pitfalls]] | [[12_Regular_Expressions|Regular Expressions →]]

> **"Python comes with batteries - use them!"**

---

## 🎯 The Most Important Modules

```
┌─────────────────────────────────────────────────────────────────┐
│               STANDARD LIBRARY OVERVIEW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  📁 os, pathlib      │ File system operations                    │
│  🔧 sys              │ System-specific parameters                │
│  📊 collections      │ Advanced container types                  │
│  🔢 math             │ Mathematical functions                    │
│  🎲 random           │ Random numbers                            │
│  🔄 itertools        │ Iterator tools                            │
│  ⚡ functools        │ Higher-order functions                    │
│  📝 string           │ String constants and templates            │
│  📅 datetime         │ Date and time                             │
│  🔍 re               │ Regular expressions                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 os - Operating System Interface

```python
import os

# ═══════════════════════════════════════════════════════════════
# WORKING DIRECTORY
# ═══════════════════════════════════════════════════════════════
cwd = os.getcwd()                    # Current working directory
os.chdir('/path/to/dir')             # Change directory

# ═══════════════════════════════════════════════════════════════
# DIRECTORY OPERATIONS
# ═══════════════════════════════════════════════════════════════
os.listdir('.')                      # List files/folders
os.mkdir('new_folder')               # Create new folder
os.makedirs('path/to/nested')        # Create nested folders
os.rmdir('empty_folder')             # Delete empty folder
os.remove('file.txt')                # Delete file
os.rename('old.txt', 'new.txt')      # Rename

# ═══════════════════════════════════════════════════════════════
# PATH OPERATIONS (os.path)
# ═══════════════════════════════════════════════════════════════
os.path.exists('file.txt')           # Does it exist?
os.path.isfile('file.txt')           # Is it a file?
os.path.isdir('folder')              # Is it a folder?
os.path.join('dir', 'subdir', 'f')   # Join paths
os.path.split('/a/b/c.txt')          # ('/a/b', 'c.txt')
os.path.basename('/a/b/c.txt')       # 'c.txt'
os.path.dirname('/a/b/c.txt')        # '/a/b'
os.path.splitext('file.txt')         # ('file', '.txt')
os.path.abspath('.')                 # Absolute path
os.path.getsize('file.txt')          # File size in bytes

# ═══════════════════════════════════════════════════════════════
# ENVIRONMENT VARIABLES
# ═══════════════════════════════════════════════════════════════
home = os.environ.get('HOME')        # Read environment variable
os.environ['MY_VAR'] = 'value'       # Set

# ═══════════════════════════════════════════════════════════════
# EXECUTE PROCESS
# ═══════════════════════════════════════════════════════════════
os.system('echo Hello')              # Execute command (simple)
# Better: use subprocess.run()!
```

---

## 🔧 sys - System Parameters

```python
import sys

# ═══════════════════════════════════════════════════════════════
# SYSTEM INFORMATION
# ═══════════════════════════════════════════════════════════════
print(sys.version)                   # Python version
print(sys.platform)                  # 'linux', 'darwin', 'win32'
print(sys.executable)                # Python interpreter path

# ═══════════════════════════════════════════════════════════════
# COMMAND LINE ARGUMENTS
# ═══════════════════════════════════════════════════════════════
# python script.py arg1 arg2
print(sys.argv)                      # ['script.py', 'arg1', 'arg2']
print(sys.argv[0])                   # Script name
print(sys.argv[1:])                  # Arguments

# ═══════════════════════════════════════════════════════════════
# IMPORT SYSTEM
# ═══════════════════════════════════════════════════════════════
print(sys.path)                      # Module search paths
sys.path.append('/my/modules')       # Add path

# ═══════════════════════════════════════════════════════════════
# PROGRAM EXIT
# ═══════════════════════════════════════════════════════════════
sys.exit(0)                          # Exit with code 0 (success)
sys.exit(1)                          # Exit with error
sys.exit("Error message")            # With message

# ═══════════════════════════════════════════════════════════════
# STREAMS
# ═══════════════════════════════════════════════════════════════
sys.stdin                            # Standard input
sys.stdout                           # Standard output
sys.stderr                           # Standard error
sys.stdout.write("Hello")            # Write directly
```

---

## 📊 collections - Advanced Containers

```python
from collections import (
    Counter, defaultdict, OrderedDict,
    namedtuple, deque, ChainMap
)

# ═══════════════════════════════════════════════════════════════
# COUNTER - Counting
# ═══════════════════════════════════════════════════════════════
words = ['apple', 'banana', 'apple', 'cherry', 'apple']
counter = Counter(words)
print(counter)                       # Counter({'apple': 3, 'banana': 1, 'cherry': 1})
print(counter.most_common(2))        # [('apple', 3), ('banana', 1)]
print(counter['apple'])              # 3

text = "mississippi"
Counter(text)                        # Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Counter operations
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)                       # Counter({'a': 4, 'b': 3})
print(c1 - c2)                       # Counter({'a': 2})

# ═══════════════════════════════════════════════════════════════
# DEFAULTDICT - Dict with default value
# ═══════════════════════════════════════════════════════════════
# Group by first letter
words = ['apple', 'banana', 'avocado', 'blueberry']
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry']}

# Count
counts = defaultdict(int)
for char in "hello":
    counts[char] += 1
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Nested
nested = defaultdict(lambda: defaultdict(int))
nested['users']['alice'] += 1

# ═══════════════════════════════════════════════════════════════
# NAMEDTUPLE - Named tuples
# ═══════════════════════════════════════════════════════════════
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)                      # 10 20
print(p[0], p[1])                    # 10 20 (also index access)

Person = namedtuple('Person', 'name age city')  # String syntax
alice = Person('Alice', 30, 'Berlin')
print(alice.name)                    # 'Alice'

# Conversion
alice._asdict()                      # {'name': 'Alice', 'age': 30, 'city': 'Berlin'}

# ═══════════════════════════════════════════════════════════════
# DEQUE - Double-ended queue
# ═══════════════════════════════════════════════════════════════
from collections import deque

d = deque([1, 2, 3])
d.append(4)                          # Add right: [1, 2, 3, 4]
d.appendleft(0)                      # Add left: [0, 1, 2, 3, 4]
d.pop()                              # Remove right: 4
d.popleft()                          # Remove left: 0
d.rotate(1)                          # Rotate: [3, 1, 2]

# With maxlen (for fixed-size history)
history = deque(maxlen=5)
for i in range(10):
    history.append(i)
print(history)                       # deque([5, 6, 7, 8, 9], maxlen=5)
```

---

## 🔢 math - Mathematics

```python
import math

# ═══════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════
math.pi                              # 3.141592653589793
math.e                               # 2.718281828459045
math.inf                             # Infinity
math.nan                             # Not a number

# ═══════════════════════════════════════════════════════════════
# ROUNDING & ABSOLUTE VALUES
# ═══════════════════════════════════════════════════════════════
math.ceil(4.3)                       # 5 (round up)
math.floor(4.7)                      # 4 (round down)
math.trunc(4.7)                      # 4 (truncate)
math.fabs(-5)                        # 5.0 (absolute value as float)
abs(-5)                              # 5 (built-in, keeps type)

# ═══════════════════════════════════════════════════════════════
# POWERS & ROOTS
# ═══════════════════════════════════════════════════════════════
math.sqrt(16)                        # 4.0
math.pow(2, 3)                       # 8.0
2 ** 3                               # 8 (built-in, faster)
math.isqrt(17)                       # 4 (integer square root)

# ═══════════════════════════════════════════════════════════════
# LOGARITHMS
# ═══════════════════════════════════════════════════════════════
math.log(100)                        # Natural logarithm
math.log10(100)                      # 2.0 (base 10)
math.log2(8)                         # 3.0 (base 2)
math.log(100, 10)                    # 2.0 (arbitrary base)

# ═══════════════════════════════════════════════════════════════
# TRIGONOMETRY
# ═══════════════════════════════════════════════════════════════
math.sin(math.pi / 2)                # 1.0
math.cos(0)                          # 1.0
math.tan(math.pi / 4)                # ~1.0
math.radians(180)                    # π (degrees → radians)
math.degrees(math.pi)                # 180 (radians → degrees)

# ═══════════════════════════════════════════════════════════════
# OTHER
# ═══════════════════════════════════════════════════════════════
math.factorial(5)                    # 120
math.gcd(12, 18)                     # 6 (greatest common divisor)
math.lcm(4, 6)                       # 12 (least common multiple)
math.comb(5, 2)                      # 10 (combinations)
math.perm(5, 2)                      # 20 (permutations)
math.isclose(0.1 + 0.2, 0.3)        # True (float comparison!)
```

---

## 🎲 random - Random Numbers

```python
import random

# ═══════════════════════════════════════════════════════════════
# RANDOM NUMBERS
# ═══════════════════════════════════════════════════════════════
random.random()                      # Float in [0.0, 1.0)
random.uniform(1.0, 10.0)            # Float in [1.0, 10.0]
random.randint(1, 10)                # Integer in [1, 10] (inclusive)
random.randrange(1, 10)              # Integer in [1, 10) (exclusive 10)
random.randrange(0, 100, 5)          # 0, 5, 10, ..., 95

# ═══════════════════════════════════════════════════════════════
# SELECTION FROM SEQUENCES
# ═══════════════════════════════════════════════════════════════
items = ['a', 'b', 'c', 'd', 'e']
random.choice(items)                 # Random element
random.choices(items, k=3)           # 3 elements (with replacement)
random.sample(items, k=3)            # 3 elements (without replacement)

# With weights
random.choices(['A', 'B', 'C'], weights=[10, 1, 1], k=5)
# A will be chosen much more frequently

# ═══════════════════════════════════════════════════════════════
# SHUFFLE
# ═══════════════════════════════════════════════════════════════
deck = list(range(52))
random.shuffle(deck)                 # In-place shuffle
print(deck)

# ═══════════════════════════════════════════════════════════════
# REPRODUCIBILITY (Seed)
# ═══════════════════════════════════════════════════════════════
random.seed(42)                      # Fixed seed for reproducible results
print(random.random())               # Always same with same seed

# Important for tests!
random.seed(42)
result1 = [random.randint(1, 10) for _ in range(5)]
random.seed(42)
result2 = [random.randint(1, 10) for _ in range(5)]
assert result1 == result2            # Always True!
```

---

## 🔄 itertools - Iterator Tools

```python
from itertools import (
    count, cycle, repeat,            # Infinite iterators
    chain, zip_longest,              # Combining iterators
    combinations, permutations,      # Combinatorics
    product, groupby,                # Other
    islice, takewhile, dropwhile     # Filtering/slicing
)

# ═══════════════════════════════════════════════════════════════
# INFINITE ITERATORS (Be careful with list()!)
# ═══════════════════════════════════════════════════════════════
# count(start, step) - Count infinitely
for i in count(10, 2):
    if i > 20: break
    print(i)                         # 10, 12, 14, 16, 18, 20

# cycle(iterable) - Repeat endlessly
c = cycle(['A', 'B', 'C'])
[next(c) for _ in range(7)]          # ['A','B','C','A','B','C','A']

# repeat(value, times) - Repeat element
list(repeat('X', 5))                 # ['X', 'X', 'X', 'X', 'X']

# ═══════════════════════════════════════════════════════════════
# COMBINING
# ═══════════════════════════════════════════════════════════════
# chain - Chain iterables
list(chain([1, 2], [3, 4], [5]))     # [1, 2, 3, 4, 5]
list(chain.from_iterable([[1,2],[3,4]])) # [1, 2, 3, 4]

# zip_longest - zip with padding
list(zip_longest([1, 2], [3, 4, 5], fillvalue=0))
# [(1, 3), (2, 4), (0, 5)]

# ═══════════════════════════════════════════════════════════════
# COMBINATORICS
# ═══════════════════════════════════════════════════════════════
# combinations - No order, no repetition
list(combinations('ABC', 2))         # [('A','B'), ('A','C'), ('B','C')]

# permutations - With order, no repetition
list(permutations('AB', 2))          # [('A','B'), ('B','A')]

# product - Cartesian product
list(product('AB', '12'))            # [('A','1'),('A','2'),('B','1'),('B','2')]
list(product(range(2), repeat=3))    # All 3-bit combinations

# ═══════════════════════════════════════════════════════════════
# SLICING & FILTERING
# ═══════════════════════════════════════════════════════════════
# islice - Slicing for iterators
list(islice(count(), 5))             # [0, 1, 2, 3, 4]
list(islice(count(), 2, 6))          # [2, 3, 4, 5]

# takewhile - Take while condition is True
list(takewhile(lambda x: x < 5, [1,3,5,2,1]))  # [1, 3]

# dropwhile - Skip while condition is True
list(dropwhile(lambda x: x < 5, [1,3,5,2,1]))  # [5, 2, 1]

# ═══════════════════════════════════════════════════════════════
# GROUPBY - Group (MUST be sorted!)
# ═══════════════════════════════════════════════════════════════
data = [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# A [('A', 1), ('A', 2)]
# B [('B', 1), ('B', 2)]
```

---

## ⚡ functools - Function Tools

```python
from functools import (
    reduce, partial, lru_cache, wraps, total_ordering
)

# ═══════════════════════════════════════════════════════════════
# REDUCE - Reduce list to single value
# ═══════════════════════════════════════════════════════════════
from functools import reduce
from operator import add, mul

numbers = [1, 2, 3, 4, 5]
reduce(add, numbers)                 # 15 (sum)
reduce(mul, numbers)                 # 120 (product)
reduce(lambda a, b: a if a > b else b, numbers)  # 5 (maximum)

# With initial value
reduce(add, [], 0)                   # 0 (without initial: error on empty list)

# ═══════════════════════════════════════════════════════════════
# PARTIAL - Pre-set arguments
# ═══════════════════════════════════════════════════════════════
from functools import partial

def greet(greeting, name):
    return f"{greeting}, {name}!"

say_hello = partial(greet, "Hello")
say_hi = partial(greet, "Hi")

print(say_hello("Alice"))            # "Hello, Alice!"
print(say_hi("Bob"))                 # "Hi, Bob!"

# With keyword arguments
int_from_binary = partial(int, base=2)
print(int_from_binary("1010"))       # 10

# ═══════════════════════════════════════════════════════════════
# LRU_CACHE - Memoization
# ═══════════════════════════════════════════════════════════════
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))                # Fast thanks to cache!
print(fibonacci.cache_info())        # Statistics

# Clear cache
fibonacci.cache_clear()

# ═══════════════════════════════════════════════════════════════
# WRAPS - Preserve decorator metadata
# ═══════════════════════════════════════════════════════════════
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """My docstring."""
    pass

print(my_function.__name__)          # 'my_function' (not 'wrapper')
print(my_function.__doc__)           # 'My docstring.'
```

---

## 📝 string - String Helpers

```python
import string

# ═══════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════
string.ascii_letters                 # 'abcdefghijklmnopqrstuvwxyzABCDEF...'
string.ascii_lowercase               # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase               # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits                        # '0123456789'
string.hexdigits                     # '0123456789abcdefABCDEF'
string.punctuation                   # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
string.whitespace                    # ' \t\n\r\x0b\x0c'

# Useful for password generation
import random
chars = string.ascii_letters + string.digits
password = ''.join(random.choices(chars, k=16))
```

---

## ✅ Module Overview

| Module | Main Purpose | Important Functions |
|--------|------------|----------------------|
| `os` | File system & system | `getcwd`, `listdir`, `path.join` |
| `sys` | Python runtime | `argv`, `exit`, `path` |
| `collections` | Advanced containers | `Counter`, `defaultdict`, `namedtuple` |
| `math` | Mathematics | `sqrt`, `ceil`, `floor`, `factorial` |
| `random` | Random | `randint`, `choice`, `shuffle` |
| `itertools` | Iterators | `chain`, `combinations`, `groupby` |
| `functools` | Functions | `reduce`, `partial`, `lru_cache` |

---

## 🎯 Exam Checklist

- [ ] `os.path.join()`, `exists()`, `isfile()`, `isdir()`
- [ ] `sys.argv` for command line arguments
- [ ] `Counter` for counting, `most_common()`
- [ ] `defaultdict(list)` and `defaultdict(int)`
- [ ] `namedtuple` for structured data
- [ ] `random.seed()` for reproducibility
- [ ] `itertools.combinations` vs `permutations`
- [ ] `functools.lru_cache` for memoization
- [ ] `functools.partial` for pre-setting arguments

---

[[10_Common_Pitfalls|← Common Pitfalls]] | [[00_Index|Index]] | [[12_Regular_Expressions|Regular Expressions →]]
