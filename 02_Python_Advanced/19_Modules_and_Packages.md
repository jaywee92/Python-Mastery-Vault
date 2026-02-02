---
title: Modules and Packages
tags: [python, modules, packages, import, organization, advanced]
category: advanced
type: topic
---

# 32. Modules and Packages

[[00_Index|← Back to Index]]

> **Organize and reuse code with modules and packages**

---

## 📋 What is a Module?

A **module** is a file containing Python code (functions, classes, variables) that can be imported and reused in other programs.

**Benefits:**
- ✓ Code reusability
- ✓ Better organization
- ✓ Namespace management
- ✓ Easier maintenance

---

## 📝 Creating Your Own Module

### Simple Module

Create a file named `mymodule.py`:

```python
# mymodule.py

def generate_full_name(firstname, lastname):
    """Combine first and last name"""
    return f"{firstname} {lastname}"

def sum_two_nums(a, b):
    """Add two numbers"""
    return a + b

# Module-level variables
PI = 3.14159
gravity = 9.81

# Module-level dictionary
person = {
    'firstname': 'John',
    'lastname': 'Doe',
    'age': 30
}
```

### Using Your Module

Create `main.py` in the same directory:

```python
# main.py

# Import the entire module
import mymodule

# Use functions from module
name = mymodule.generate_full_name('Alice', 'Smith')
print(name)  # Alice Smith

# Use variables from module
print(mymodule.PI)  # 3.14159

mass = 75
weight = mass * mymodule.gravity
print(f'Weight: {weight} N')  # Weight: 735.75 N
```

---

## 📦 Different Import Styles

### 1. Import Entire Module

```python
import mymodule

# Access with module name prefix
result = mymodule.sum_two_nums(5, 10)
```

**Pros:** Clear where functions come from  
**Cons:** More typing

### 2. Import Specific Items

```python
from mymodule import generate_full_name, sum_two_nums, PI

# Use directly without module prefix
name = generate_full_name('Bob', 'Jones')
total = sum_two_nums(3, 7)
circle_area = PI * 5 ** 2
```

**Pros:** Less typing  
**Cons:** Less clear where items come from

### 3. Import Everything (⚠️ Not Recommended)

```python
from mymodule import *

# All items available directly
name = generate_full_name('Charlie', 'Brown')
```

**⚠️ Warning:** Can cause naming conflicts!

### 4. Import with Alias

```python
import mymodule as mm

# Use short alias
name = mm.generate_full_name('David', 'Wilson')
```

**Pros:** Shorter, still clear

### 5. Import Function with Alias

```python
from mymodule import generate_full_name as fullname

# Use renamed function
name = fullname('Eve', 'Davis')
```

---

## 🛠️ Built-in Modules

Python comes with many useful built-in modules!

### OS Module - Operating System Interface

```python
import os

# Get current working directory
current_dir = os.getcwd()
print(f'Current directory: {current_dir}')

# List directory contents
files = os.listdir('.')
print(f'Files: {files}')

# Create directory
# os.mkdir('new_folder')

# Check if path exists
exists = os.path.exists('myfile.txt')
print(f'File exists: {exists}')

# Join paths (platform-independent)
full_path = os.path.join('folder', 'subfolder', 'file.txt')
print(full_path)

# Get file extension
filename = 'document.pdf'
name, ext = os.path.splitext(filename)
print(f'Name: {name}, Extension: {ext}')
```

### Sys Module - System Parameters

```python
import sys

# Get Python version
print(f'Python version: {sys.version}')

# Get command line arguments
print(f'Script name: {sys.argv[0]}')
# If you run: python script.py arg1 arg2
# sys.argv[1] would be 'arg1'
# sys.argv[2] would be 'arg2'

# Exit program
# sys.exit()  # Exits with code 0 (success)
# sys.exit(1)  # Exits with error code 1

# Python path (where modules are searched)
print(f'Module search paths: {sys.path[:3]}')
```

### Math Module - Mathematical Functions

```python
import math

# Constants
print(f'Pi: {math.pi}')        # 3.141592...
print(f'e: {math.e}')          # 2.718281...

# Basic functions
print(math.sqrt(16))           # 4.0
print(math.pow(2, 3))          # 8.0
print(math.floor(3.7))         # 3
print(math.ceil(3.2))          # 4
print(math.fabs(-5))           # 5.0

# Trigonometry
print(math.sin(math.pi / 2))   # 1.0
print(math.cos(0))             # 1.0
print(math.tan(math.pi / 4))   # 1.0

# Logarithms
print(math.log(10))            # Natural log
print(math.log10(100))         # Base 10: 2.0
print(math.log2(8))            # Base 2: 3.0

# Factorial
print(math.factorial(5))       # 120
```

### Random Module - Random Numbers

```python
import random

# Random integer in range
num = random.randint(1, 10)
print(f'Random number (1-10): {num}')

# Random float between 0 and 1
decimal = random.random()
print(f'Random decimal: {decimal}')

# Random float in range
price = random.uniform(10.5, 99.9)
print(f'Random price: ${price:.2f}')

# Random choice from list
fruits = ['apple', 'banana', 'orange', 'grape']
fruit = random.choice(fruits)
print(f'Random fruit: {fruit}')

# Shuffle list in place
cards = ['A', 'K', 'Q', 'J', '10']
random.shuffle(cards)
print(f'Shuffled: {cards}')

# Random sample (multiple items)
winners = random.sample(fruits, 2)
print(f'Winners: {winners}')
```

### Statistics Module - Statistical Functions

```python
import statistics

data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

# Mean (average)
mean = statistics.mean(data)
print(f'Mean: {mean}')              # 5.0

# Median (middle value)
median = statistics.median(data)
print(f'Median: {median}')          # 5

# Mode (most common)
mode = statistics.mode(data)
print(f'Mode: {mode}')              # 5

# Standard deviation
stdev = statistics.stdev(data)
print(f'Std Dev: {stdev:.2f}')      # 2.67

# Variance
variance = statistics.variance(data)
print(f'Variance: {variance:.2f}')  # 7.11
```

### Datetime Module - Date and Time

```python
from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(f'Now: {now}')

# Current date only
today = date.today()
print(f'Today: {today}')

# Formatted output
formatted = now.strftime('%Y-%m-%d %H:%M:%S')
print(f'Formatted: {formatted}')

# Create specific date
birthday = date(1990, 5, 15)
print(f'Birthday: {birthday}')

# Date arithmetic
tomorrow = today + timedelta(days=1)
print(f'Tomorrow: {tomorrow}')

next_week = today + timedelta(weeks=1)
print(f'Next week: {next_week}')

# Time difference
age_days = (today - birthday).days
print(f'Age in days: {age_days}')
```

### String Module - String Constants

```python
import string

# Useful constants
print(f'Lowercase: {string.ascii_lowercase}')
print(f'Uppercase: {string.ascii_uppercase}')
print(f'Digits: {string.digits}')
print(f'Punctuation: {string.punctuation}')

# All printable characters
print(f'Printable chars: {string.printable[:20]}...')
```

---

## 📦 Creating Packages

A **package** is a directory containing multiple modules and a special `__init__.py` file.

### Package Structure

```
mypackage/
│
├── __init__.py          # Makes it a package
├── module1.py           # Module 1
├── module2.py           # Module 2
└── subpackage/
    ├── __init__.py      # Subpackage
    └── module3.py       # Module 3
```

### Example Package

**mypackage/__init__.py:**
```python
# Can be empty, or contain package initialization code
print("mypackage initialized")
```

**mypackage/module1.py:**
```python
def function1():
    return "Function from module1"
```

**mypackage/module2.py:**
```python
def function2():
    return "Function from module2"
```

### Using a Package

```python
# Import from package
from mypackage import module1, module2

result1 = module1.function1()
result2 = module2.function2()

# Or import specific functions
from mypackage.module1 import function1
```

---

## 🔍 Module Search Path

Python searches for modules in this order:

1. **Current directory**
2. **PYTHONPATH** environment variable
3. **Standard library directories**
4. **Site-packages** (installed packages)

View search path:

```python
import sys
print(sys.path)
```

---

## 💡 Best Practices

### 1. Use Descriptive Module Names

```python
# Good
import user_authentication
import data_processing

# Avoid
import utils
import helpers
```

### 2. Organize Related Code

```python
# Group related functionality
myapp/
├── database/
│   ├── __init__.py
│   ├── models.py
│   └── queries.py
├── api/
│   ├── __init__.py
│   ├── routes.py
│   └── handlers.py
└── utils/
    ├── __init__.py
    ├── validators.py
    └── formatters.py
```

### 3. Avoid Circular Imports

```python
# BAD: module_a imports module_b, module_b imports module_a

# GOOD: Use a third module or restructure code
```

### 4. Use `if __name__ == "__main__":`

```python
# mymodule.py

def my_function():
    return "Hello"

# This only runs when file is executed directly
if __name__ == "__main__":
    print("Testing module")
    print(my_function())
```

---

## 🎓 Summary

- **Modules** = Python files with reusable code
- **Packages** = Directories with multiple modules
- **Import** = Use code from modules
- **Built-in modules** = Ready-to-use functionality
- **Custom modules** = Organize your own code

**Key Takeaway:** Modules make code reusable, organized, and maintainable!

---

## 🔗 Related Topics

- [[33_Package_Manager|Package Manager (pip)]]
- [[08_Functions|Functions]]
- [[11_Classes_and_OOP|Classes & OOP]]

---

[[00_Index|← Back to Index]]

*Modular code is maintainable code! 📦*
