---
title: Useful Imports & Built-in Functions
tags: [python, imports, stdlib, functions, practical]
created: 2026-02-01
type: topic
difficulty: beginner-intermediate
---

# 🧰 Useful Imports & Built-in Functions

[[00_Index|← Back to Index]]

> **The most important modules and functions for everyday coding**

---

## 📦 Essential Standard Library Imports

### 1. `os` - Operating System Interaction

```python
import os

# Current directory
print(os.getcwd())  # /Users/vito/projects

# Change directory
os.chdir('/path/to/folder')

# List files
files = os.listdir('.')  # ['file1.py', 'file2.txt']

# Create directory
os.makedirs('new_folder/subfolder', exist_ok=True)

# Delete file / folder
os.remove('file.txt')
os.rmdir('empty_folder')

# Environment variables
api_key = os.getenv('API_KEY', 'default_value')
os.environ['MY_VAR'] = 'value'

# Path operations
path = os.path.join('folder', 'subfolder', 'file.txt')
# → 'folder/subfolder/file.txt'

os.path.exists('file.txt')      # True/False
os.path.isfile('file.txt')      # Is it a file?
os.path.isdir('folder')         # Is it a directory?
os.path.basename('/a/b/c.txt')  # 'c.txt'
os.path.dirname('/a/b/c.txt')   # '/a/b'
os.path.splitext('file.txt')    # ('file', '.txt')
```

---

### 2. `sys` - System Parameters

```python
import sys

# Command line arguments
print(sys.argv)  # ['script.py', 'arg1', 'arg2']

# Python version
print(sys.version)  # '3.11.0 ...'

# Exit program
sys.exit(0)  # 0 = success, 1+ = error

# Module search paths
print(sys.path)

# Maximum recursion depth
sys.setrecursionlimit(2000)
```

---

### 3. `datetime` - Date & Time

```python
from datetime import datetime, date, timedelta

# Current date/time
now = datetime.now()
today = date.today()

print(now)    # 2026-02-01 14:30:45.123456
print(today)  # 2026-02-01

# Formatting
formatted = now.strftime('%d.%m.%Y %H:%M')  # '01.02.2026 14:30'
formatted = now.strftime('%Y-%m-%d')         # '2026-02-01'

# Parse string to date
date_str = '25.12.2026'
parsed = datetime.strptime(date_str, '%d.%m.%Y')

# Time differences
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
two_hours_ago = now - timedelta(hours=2)

# Calculate difference
diff = datetime(2026, 12, 31) - datetime.now()
print(diff.days)  # Days until New Year's Eve

# Individual components
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)
print(now.weekday())  # 0=Monday, 6=Sunday
```

**Important Format Codes:**
```
%Y = Year (4-digit)      %y = Year (2-digit)
%m = Month (01-12)       %d = Day (01-31)
%H = Hour (00-23)        %M = Minute (00-59)
%S = Second (00-59)      %A = Weekday (Monday)
%B = Month name (January)
```

---

### 4. `random` - Random Numbers

```python
import random

# Random integer
num = random.randint(1, 100)  # 1 to 100 (inclusive)

# Random float
num = random.random()      # 0.0 to 1.0
num = random.uniform(1, 10)  # 1.0 to 10.0

# Random element from list
items = ['a', 'b', 'c', 'd']
choice = random.choice(items)  # e.g. 'c'

# Multiple random elements (without replacement)
sample = random.sample(items, 2)  # e.g. ['b', 'd']

# Shuffle list (in-place)
random.shuffle(items)

# Reproducible random numbers (for testing)
random.seed(42)
print(random.randint(1, 100))  # Always the same
```

---

### 5. `math` - Mathematical Functions

```python
import math

# Basic operations
math.sqrt(16)      # 4.0 - Square root
math.pow(2, 3)     # 8.0 - Power
math.factorial(5)  # 120 - Factorial

# Rounding
math.floor(3.7)    # 3 - Round down
math.ceil(3.2)     # 4 - Round up
math.trunc(-3.7)   # -3 - Toward zero

# Trigonometry (radians!)
math.sin(math.pi / 2)  # 1.0
math.cos(0)            # 1.0
math.radians(180)      # π - Degrees to radians
math.degrees(math.pi)  # 180 - Radians to degrees

# Logarithms
math.log(100)      # 4.605... (natural log)
math.log10(100)    # 2.0
math.log2(8)       # 3.0

# Constants
math.pi    # 3.14159...
math.e     # 2.71828...
math.inf   # Infinity
math.nan   # Not a Number

# Practical
math.gcd(12, 18)   # 6 - Greatest common divisor
math.isnan(x)      # Check for NaN
math.isinf(x)      # Check for infinity
```

---

### 6. `collections` - Extended Data Structures

```python
from collections import Counter, defaultdict, namedtuple, deque

# Counter - Count elements
words = ['apple', 'banana', 'apple', 'cherry', 'apple']
count = Counter(words)
print(count)  # Counter({'apple': 3, 'banana': 1, 'cherry': 1})
print(count.most_common(2))  # [('apple', 3), ('banana', 1)]

# Count letters
letter_count = Counter('mississippi')
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# defaultdict - Dict with default value
word_groups = defaultdict(list)
words = [('fruit', 'apple'), ('fruit', 'banana'), ('veggie', 'carrot')]
for category, item in words:
    word_groups[category].append(item)
# {'fruit': ['apple', 'banana'], 'veggie': ['carrot']}

# With int as default (counting)
letter_count = defaultdict(int)
for char in 'hello':
    letter_count[char] += 1

# namedtuple - Tuple with names
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)  # 3 4
print(p[0])      # 3 (index also works)

Person = namedtuple('Person', 'name age city')
bob = Person('Bob', 30, 'Berlin')
print(bob.name)  # 'Bob'

# deque - Double-ended queue (fast at both ends)
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)   # [0, 1, 2, 3]
d.append(4)       # [0, 1, 2, 3, 4]
d.popleft()       # 0, deque is [1, 2, 3, 4]
d.pop()           # 4
d.rotate(1)       # Rotate right
```

---

### 7. `itertools` - Iterator Tools

```python
from itertools import count, cycle, repeat, chain, combinations, permutations

# Infinite iterators
for i in count(10, 2):  # 10, 12, 14, 16, ...
    if i > 20:
        break
    print(i)

# Cycle repeatedly
colors = cycle(['red', 'green', 'blue'])
for _ in range(5):
    print(next(colors))  # red, green, blue, red, green

# Chain lists together
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list(chain(list1, list2))  # [1, 2, 3, 4, 5, 6]

# Combinations (without order)
items = ['A', 'B', 'C']
combs = list(combinations(items, 2))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Permutations (with order)
perms = list(permutations(items, 2))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# Product (Cartesian product)
from itertools import product
list(product([1, 2], ['a', 'b']))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# Grouping
from itertools import groupby
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# A [('A', 1), ('A', 2)]
# B [('B', 3), ('B', 4)]
```

---

### 8. `json` - JSON Processing

```python
import json

# Python → JSON String
data = {'name': 'Max', 'age': 25, 'cities': ['Berlin', 'Hamburg']}
json_str = json.dumps(data)
# '{"name": "Max", "age": 25, "cities": ["Berlin", "Hamburg"]}'

# Pretty formatted
json_str = json.dumps(data, indent=2, ensure_ascii=False)

# JSON String → Python
parsed = json.loads(json_str)
print(parsed['name'])  # 'Max'

# Read JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Write JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
```

---

### 9. `re` - Regular Expressions (Basics)

```python
import re

text = "My email is max@example.com and test@gmail.com"

# Search (first match)
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print(match.group())  # 'max@example.com'

# Find all
emails = re.findall(r'\w+@\w+\.\w+', text)
# ['max@example.com', 'test@gmail.com']

# Replace
new_text = re.sub(r'\d+', 'X', 'Price: 100 Euro')
# 'Price: X Euro'

# Split
parts = re.split(r'[,;]', 'a,b;c,d')
# ['a', 'b', 'c', 'd']

# Common patterns
r'\d+'      # Numbers
r'\w+'      # Words (letters, numbers, _)
r'\s+'      # Whitespace
r'[A-Z]+'   # Uppercase letters
r'^Start'   # Line start
r'End$'     # Line end
r'\b\w+\b'  # Whole words
```

---

## ⚡ Important Built-in Functions

### Data Transformation

```python
# map() - Apply function to all elements
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16]

# filter() - Filter elements
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# zip() - Combine lists
names = ['Alice', 'Bob']
ages = [25, 30]
combined = list(zip(names, ages))  # [('Alice', 25), ('Bob', 30)]

# enumerate() - Index + value
for i, name in enumerate(['a', 'b', 'c']):
    print(i, name)  # 0 a, 1 b, 2 c

# sorted() - Sort (new list)
sorted([3, 1, 2])                    # [1, 2, 3]
sorted(['b', 'a'], reverse=True)     # ['b', 'a']
sorted(users, key=lambda u: u.age)   # By attribute

# reversed() - Reverse
list(reversed([1, 2, 3]))  # [3, 2, 1]
```

### Aggregation

```python
numbers = [1, 2, 3, 4, 5]

sum(numbers)      # 15
min(numbers)      # 1
max(numbers)      # 5
len(numbers)      # 5

# With key function
users = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
youngest = min(users, key=lambda u: u['age'])  # Bob

# any() / all()
any([False, True, False])   # True (at least one)
all([True, True, True])     # True (all)

# Practical for checks
numbers = [2, 4, 6, 8]
all(n % 2 == 0 for n in numbers)  # True - all even?
any(n > 5 for n in numbers)       # True - any > 5?
```

### Type Conversion

```python
# Numbers
int('42')        # 42
float('3.14')    # 3.14
str(42)          # '42'

# Bool
bool(0)          # False
bool('')         # False
bool([])         # False
bool(1)          # True
bool('text')     # True

# Lists/Tuples/Sets
list((1, 2, 3))      # [1, 2, 3]
tuple([1, 2, 3])     # (1, 2, 3)
set([1, 2, 2, 3])    # {1, 2, 3}
dict([('a', 1)])     # {'a': 1}

# ASCII
ord('A')         # 65
chr(65)          # 'A'
```

### Object Inspection

```python
# Check type
type(42)                    # <class 'int'>
isinstance(42, int)         # True
isinstance(42, (int, str))  # True (one of multiple)

# List attributes
dir(object)                 # All attributes/methods

# Help
help(len)                   # Show documentation

# ID (memory address)
id(object)                  # Unique ID

# Dynamic attributes
hasattr(obj, 'name')        # Has attribute?
getattr(obj, 'name', None)  # Get attribute
setattr(obj, 'name', 'Max') # Set attribute
```

---

## 🎯 Practical Code Snippets

### File Operations

```python
# Find all .txt files in directory
import os
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

# Read file line by line
with open('file.txt') as f:
    for line in f:
        print(line.strip())

# Read entire content
content = open('file.txt').read()

# Quick write to file
with open('output.txt', 'w') as f:
    f.write('Hello World\n')
```

### String Processing

```python
# Common string operations
text = "  Hello World  "
text.strip()           # 'Hello World'
text.lower()           # '  hello world  '
text.upper()           # '  HELLO WORLD  '
text.replace('o', '0') # '  Hell0 W0rld  '
text.split()           # ['Hello', 'World']
'-'.join(['a','b'])    # 'a-b'

# Checks
'hello'.startswith('he')  # True
'hello'.endswith('lo')    # True
'hello'.isalpha()         # True
'123'.isdigit()           # True
```

### List Tricks

```python
# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
# [1, 2, 3, 4, 5, 6]

# Remove duplicates (preserve order)
items = [1, 2, 2, 3, 1, 4]
unique = list(dict.fromkeys(items))  # [1, 2, 3, 4]

# Split list into chunks
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

list(chunks([1,2,3,4,5,6], 2))  # [[1,2], [3,4], [5,6]]
```

---

## 📝 Import Best Practices

```python
# ✅ Good - Specific imports
from datetime import datetime, timedelta
from collections import Counter, defaultdict

# ✅ Good - Import module
import os
import json

# ❌ Avoid - Wildcard imports
from os import *  # May overwrite names

# ✅ Alias for long names
import numpy as np
import pandas as pd

# ✅ Grouping (Standard Library → Third Party → Local)
import os
import sys
from datetime import datetime

import requests
import numpy as np

from myproject import utils
```

---

## 🔗 Related Topics

- [[09_Lambda_and_Built-ins|Lambda & Built-ins]]
- [[12_File_IO|File I/O]]
- [[../02_Python_Advanced/11_Standard_Library|Standard Library (Advanced)]]
- [[../02_Python_Advanced/12_Regular_Expressions|Regex (Advanced)]]

---

[[00_Index|← Back to Index]]

*These imports will be your daily toolkit! 🛠️*
