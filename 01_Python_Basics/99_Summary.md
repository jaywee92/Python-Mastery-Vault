---
title: Python Basics - Summary
tags: [python, basics, summary, reference, cheatsheet]
created: 2026-02-05
type: summary
---

# Python Basics - Summary

## 📋 Overview

This document summarizes all essential Python fundamentals. From variables and data types through control flow mechanisms to functions, classes, and file operations - you'll find all important concepts in compact form here.

---

## 🔑 Quick Reference

### Data Types

| Type | Example | Mutable | Ordered | Hashable |
|-----|----------|---------|----------|----------|
| `int` | `42` | ❌ | - | ✅ |
| `float` | `3.14` | ❌ | - | ✅ |
| `str` | `"hello"` | ❌ | ✅ | ✅ |
| `bool` | `True` | ❌ | - | ✅ |
| `list` | `[1,2,3]` | ✅ | ✅ | ❌ |
| `tuple` | `(1,2,3)` | ❌ | ✅ | ✅ |
| `dict` | `{k: v}` | ✅ | ✅ | ❌ |
| `set` | `{1,2,3}` | ✅ | ❌ | ❌ |

### Collections Comparison

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| **Ordered** | ✅ | ✅ | ❌ | ✅ |
| **Mutable** | ✅ | ❌ | ✅ | ✅ |
| **Duplicates** | ✅ | ✅ | ❌ | Keys: ❌ |
| **Indexing** | ✅ | ✅ | ❌ | Key-based |
| **Hashable** | ❌ | ✅ | ❌ | ❌ |

### Syntax Essentials

```python
# Variables and Assignment
name = "Alice"
x, y, z = 1, 2, 3
a = b = c = 0

# String Operations
text = "Python"
text[0]         # "P" (Indexing)
text[0:3]       # "Pyt" (Slicing)
text[::-1]      # "nohtyP" (Reverse)
text.upper()    # "PYTHON"
f"{name} is {age} years old"  # F-strings

# Lists
numbers = [1, 2, 3]
numbers.append(4)
numbers.extend([5, 6])
numbers.insert(0, 0)
numbers.remove(2)
numbers.pop()
numbers[1:3]    # [2, 3]

# Dictionaries
person = {"name": "Alice", "age": 25}
person["age"]           # 25
person.get("city", "Unknown")
person.keys()
person.values()
person.items()

# Conditionals
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

result = "Even" if x % 2 == 0 else "Odd"

# Loops
for i in range(5):
    print(i)

for item in items:
    print(item)

while condition:
    # Code
    break       # Exit loop
    continue    # Skip iteration

# Comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
word_dict = {k: len(k) for k in words}
unique = {x for x in numbers}

# Functions
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda
square = lambda x: x ** 2
evens = list(filter(lambda x: x % 2 == 0, numbers))
sorted_by_length = sorted(words, key=len)

# Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

# File Operations
with open("file.txt", "r") as f:
    content = f.read()

with open("file.txt", "w") as f:
    f.write("Hello World")

# Exception Handling
try:
    risky_operation()
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print("Unexpected error")
finally:
    cleanup()
```

---

## 📝 Topic Summaries

### Variables and Strings Advanced

Variables store data under a name (dynamically typed). Strings are immutable text data types with extensive methods. F-strings offer the most modern formatting method with expression support.

**Key Concepts:**
- Variable naming conventions (snake_case)
- String indexing and slicing
- String methods (upper, lower, strip, split, replace)
- Type conversion (int, float, str, bool)

---

### Lists Deep Dive

Lists are mutable, ordered collections that can contain different data types. They support indexing, slicing, and many operations. List comprehensions offer an elegant and efficient way to create lists.

**Key Concepts:**
- Positive and negative indexing
- Slicing with start:stop:step syntax
- append vs extend (single element vs multiple)
- Shallow vs deep copy
- List comprehensions with if/else

---

### Tuples and Sets

Tuples are immutable sequences that can be used as dictionary keys. Sets are unordered collections with unique elements, perfect for membership tests and mathematical operations.

**Key Concepts:**
- Tuple unpacking
- Set operations (union, intersection, difference)
- Automatic duplicate removal in sets
- Sets for O(1) membership tests

---

### Dictionaries Mastery

Dictionaries are key-value collections with O(1) access time. Keys must be unique and hashable. They are the go-to data structure for structured data.

**Key Concepts:**
- get() vs [] access (error handling)
- pop(), update(), setdefault()
- Dictionary comprehensions
- Iteration over keys(), values(), items()

---

### Conditionals

If/elif/else statements control program flow based on conditions. Ternary operators offer compact if-else constructs. Some values are falsy (False, 0, "", [], None) and others truthy.

**Key Concepts:**
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Ternary expressions: `value_if_true if condition else value_if_false`
- Walrus operator (:=) in Python 3.8+

---

### Loops and Iteration

For loops iterate over sequences, while while loops are condition-based. Break exits the loop, continue skips to the next iteration. Enumerate and zip are powerful iteration tools.

**Key Concepts:**
- range() with start, stop, step
- enumerate() for index and value
- zip() for parallel iteration of multiple sequences
- Loop else (executes when completed without break)

---

### Comprehensions

List, dict, set, and generator comprehensions offer concise syntax for creating collections. They're often faster than loops and more Pythonic for simple transformations.

**Key Concepts:**
- Syntax: `[expression for item in iterable if condition]`
- Nested comprehensions
- If-else in comprehensions (ternary)
- Generator expressions with () are memory efficient

---

### Functions

Functions are reusable code blocks with parameters and return values. *args and **kwargs enable variable arguments. Default parameters, type hints, and docstrings are best practices.

**Key Concepts:**
- Parameters vs arguments
- Default parameters
- *args (tuple of positional arguments)
- **kwargs (dict of keyword arguments)
- Return values (single or multiple)

---

### Lambda and Built-ins

Lambda functions are anonymous, one-line functions for simple operations. map(), filter(), reduce(), and sorted() are powerful functional programming tools. any() and all() for condition checking.

**Key Concepts:**
- Lambda syntax: `lambda params: expression`
- map() - apply function to all elements
- filter() - filter elements
- sorted() with key parameter
- any()/all() for condition checking

---

### Scope and Closures

The LEGB rule determines variable lookup: Local → Enclosing → Global → Built-in. global and nonlocal keywords enable access to outer scopes. Closures are functions that access outer variables.

**Key Concepts:**
- LEGB rule for variable lookup
- global keyword for module variables
- nonlocal for enclosing-scope variables
- Closures for state management
- Late binding problem in loops

---

### Classes and OOP

Classes are blueprints for objects. __init__() is the constructor. self references the instance. Attributes store data, methods define behavior.

**Key Concepts:**
- class keyword and CamelCase naming convention
- __init__() constructor
- self parameter (mandatory)
- Instance vs class attributes
- Methods and their invocation

---

### File IO

The with statement (context manager) guarantees automatic closing. Modes: 'r' (read), 'w' (write/overwrite), 'a' (append). Encoding should always be specified explicitly.

**Key Concepts:**
- with open() for automatic close()
- File modes and their meaning
- read(), readline(), readlines() vs iteration
- write() vs writelines()
- CSV and JSON processing

---

### Exceptions

Try/except blocks catch errors and prevent program crashes. else runs only on success, finally always runs. raise creates custom exceptions. Specific exception handling is more important than generic.

**Key Concepts:**
- try/except/else/finally structure
- Specific vs generic exception handling
- raise for custom exceptions
- Custom exception classes
- EAFP vs LBYL philosophy

---

### Useful Imports

The standard library provides modules for common tasks. os and pathlib for filesystem, datetime for times, random for random values, json for data exchange.

**Important Modules:**
- os - filesystem and environment
- sys - interpreter parameters
- datetime - date and time
- json - JSON processing
- collections - Counter, defaultdict, namedtuple
- itertools - combinatorics and iterations
- re - regular expressions
- math - mathematical functions

---

## ✅ Self-Test Checklist

### Basics
- [ ] I can create and assign variables
- [ ] I know all primitive data types (int, float, str, bool)
- [ ] I can format strings with f-strings
- [ ] I understand true/false and truthy/falsy values

### Collections
- [ ] I can create, modify, and slice lists
- [ ] I can distinguish between append() and extend()
- [ ] I can create tuples and use unpacking
- [ ] I understand set operations (union, intersection)
- [ ] I can perform dictionary operations

### Control Flow
- [ ] I can write if/elif/else statements
- [ ] I can use for and while loops
- [ ] I understand break, continue, and else in loops
- [ ] I can write comprehensions (list, dict, set)
- [ ] I understand enumerate() and zip()

### Functions
- [ ] I can define functions with parameters
- [ ] I understand default parameters
- [ ] I can use *args and **kwargs
- [ ] I know lambda functions
- [ ] I can use map(), filter(), and sorted()

### Scope & OOP
- [ ] I understand the LEGB rule
- [ ] I can distinguish between global and nonlocal
- [ ] I understand closures
- [ ] I can write simple classes
- [ ] I understand __init__ and self

### Practical
- [ ] I can read and write files (with statement)
- [ ] I can handle exceptions with try/except
- [ ] I can process CSV and JSON
- [ ] I can import modules (os, json, datetime)
- [ ] I can use list comprehensions instead of loops

---

## 🛤️ Recommended Learning Path

### Beginner (Basics)
1. **Variables and Strings Advanced** - Foundation of all programs
2. **Data Types** - Understand different data types
3. **Lists Deep Dive** - Working with data
4. **Dictionaries Mastery** - Structured data
5. **Conditionals** - Making decisions

### Beginner-Intermediate (Control Flow)
6. **Loops and Iteration** - Repeat code
7. **Comprehensions** - Elegant list creation
8. **Functions** - Make code reusable
9. **Tuples and Sets** - More collection types

### Intermediate (Advanced Concepts)
10. **Lambda and Built-ins** - Functional programming
11. **Scope and Closures** - Understanding variable access
12. **File IO** - Working with files
13. **Exceptions** - Error handling

### Advanced
14. **Classes and OOP** - Object-oriented programming
15. **Useful Imports** - Using the standard library

---

## 🎯 Avoiding Common Beginner Mistakes

### 1. List Mutation vs String Immutability
```python
# ❌ WRONG - Strings are immutable
text = "hello"
text[0] = "H"  # TypeError!

# ✅ CORRECT
text = "hello".upper()  # "HELLO"
```

### 2. append vs extend
```python
# ❌ WRONG
list1 = [1, 2]
list1.append([3, 4])  # [1, 2, [3, 4]] - Nested!

# ✅ CORRECT
list1 = [1, 2]
list1.extend([3, 4])  # [1, 2, 3, 4]
```

### 3. Dict with [] vs get()
```python
# ❌ WRONG - KeyError if not present
value = my_dict["key"]

# ✅ CORRECT - Safe with default
value = my_dict.get("key", "default")
```

### 4. Mutable Default Parameters
```python
# ❌ WRONG - Unexpected behavior
def add_item(item, list_=[]):
    list_.append(item)
    return list_

# ✅ CORRECT - None as default
def add_item(item, list_=None):
    if list_ is None:
        list_ = []
    list_.append(item)
    return list_
```

### 5. Scope and UnboundLocalError
```python
# ❌ WRONG - UnboundLocalError
x = 10
def func():
    print(x)    # This line gives error!
    x = 5

# ✅ CORRECT
x = 10
def func():
    global x
    print(x)
    x = 5
```

### 6. Not using with statement
```python
# ❌ WRONG - File stays open
f = open("file.txt")
content = f.read()

# ✅ CORRECT
with open("file.txt") as f:
    content = f.read()
```

---

## 💡 Pro Tips

### Performance
- Use list comprehensions instead of append loops
- Use sets for membership tests (O(1) vs O(n))
- For large files: iterate instead of loading everything into RAM
- Learn the time complexity of common operations

### Code Quality
- Use descriptive variable names
- Keep functions small and focused
- Write docstrings for public functions
- Use type hints for better documentation

### Python Idioms
- Use f-strings instead of % or .format()
- EAFP (Easier to Ask Forgiveness) instead of LBYL
- List comprehensions over filter/map
- Context managers (with) for resource management

---

## 📚 Further Resources

After you master these basics, the next steps are:
- Python Advanced Topics (decorators, context managers, generators)
- Object-Oriented Programming (inheritance, polymorphism, design patterns)
- Standard Library (learn more modules)
- Testing (unittest, pytest)

---

## 🔍 Debugging Tips

```python
# 1. Print debugging
print(f"Debug: x = {x}, type = {type(x)}")

# 2. type() and isinstance()
print(type(variable))
print(isinstance(variable, int))

# 3. dir() for available methods
print(dir(object))

# 4. help() for documentation
help(function_name)

# 5. Syntax errors - check indentation!
# 6. NameError - variable not defined
# 7. TypeError - wrong data type
# 8. IndexError - index out of range
# 9. KeyError - key not in dict
# 10. ValueError - wrong value for type
```

---

**Learning Strategy:** Practice regularly with small projects, build functionality step by step, and test your code thoroughly!

*Master the basics, master Python! 🐍*
