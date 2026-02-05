---
title: Variables and Strings Advanced
category: fundamentals
tags: ['python', 'strings', 'variables', 'basics', 'fundamentals']
created: 2026-01-27
type: topic
---

# Variables and Strings Advanced

[[00_Index|← Back to Index]]

> **Master variables and strings - the foundation of Python**

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║          📦 VARIABLES & STRINGS - LABELED DATA BOXES          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   name = "Alice"        age = 25         text = "Python"     ║
║                                                               ║
║   ┌──────────────┐     ┌──────────┐     ┌──────────────┐    ║
║   │ "Alice"      │     │   25     │     │ "Python"     │    ║
║   └──────┬───────┘     └────┬─────┘     └──────┬───────┘    ║
║          │ name             │ age              │ text        ║
║          │ (variablenname)  │                  │             ║
║                                                               ║
║   🔤 Strings sind unveränderbar (immutable)                   ║
║   • "Python"[0] → "P"                                         ║
║   • "Python"[:2] → "Py"  (Slicing)                           ║
║   • "python".upper() → "PYTHON"  (Methoden)                  ║
║                                                               ║
║   💡 Variable = Name + Wert (wie eine beschriftete Box!)      ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📋 Table of Contents

- [Variables](#variables)
- [Variable Naming](#variable-naming)
- [Data Types](#data-types)
- [Strings](#strings)
- [String Methods](#string-methods)
- [String Formatting](#string-formatting)
- [Type Conversion](#type-conversion)

---

## 📦 Variables

### What is a Variable?

A **variable** is a named storage location in memory that holds data.

```python
# Simple assignment
name = "Alice"
age = 25
height = 1.75
is_student = True

# Multiple assignment
x, y, z = 1, 2, 3

# Same value to multiple variables
a = b = c = 0

print(name)    # Alice
print(age)     # 25
```

### Variable Naming Rules

**✅ Valid names:**
```python
firstname = "John"
last_name = "Doe"
age = 30
_private = "hidden"
year2024 = 2024
CONSTANT = 3.14
```

**❌ Invalid names:**
```python
# first-name = "John"    # No hyphens
# first@name = "John"    # No special chars
# 1name = "John"         # Can't start with number
# first name = "John"    # No spaces
```

### Best Practices

```python
# Use descriptive names
✅ user_age = 25
❌ x = 25

# Use snake_case for variables
✅ first_name = "Alice"
❌ firstName = "Alice"  # camelCase (used in other languages)

# Use UPPERCASE for constants
✅ MAX_SIZE = 100
✅ PI = 3.14159

# Avoid built-in names
❌ list = [1, 2, 3]    # Shadows built-in
✅ my_list = [1, 2, 3]
```

---

## 🔢 Data Types

Python has several built-in data types:

```python
# Numbers
integer = 42                    # int
floating = 3.14                 # float
complex_num = 1 + 2j           # complex

# Text
text = "Hello World"           # str

# Boolean
is_valid = True                # bool
is_empty = False

# Check type
print(type(integer))           # <class 'int'>
print(type(text))              # <class 'str'>
print(type(is_valid))          # <class 'bool'>
```

### Type Checking

```python
# Check if variable is of certain type
age = 25
print(isinstance(age, int))     # True
print(isinstance(age, str))     # False

name = "Alice"
print(isinstance(name, str))    # True
```

---

## 📝 Strings

### Creating Strings

```python
# Single quotes
single = 'Hello'

# Double quotes
double = "World"

# Triple quotes (multiline)
multiline = '''This is
a multiline
string'''

paragraph = """
Line 1
Line 2
Line 3
"""

print(multiline)
print(paragraph)
```

### String Concatenation

```python
# Using +
first = "Hello"
second = "World"
result = first + " " + second
print(result)  # Hello World

# Using multiple strings
greeting = "Hello" " " "World"
print(greeting)  # Hello World

# Repeat strings
stars = "*" * 10
print(stars)  # **********
```

### String Indexing

```python
text = "Python"

# Positive indexing (0-based)
print(text[0])    # P
print(text[1])    # y
print(text[5])    # n

# Negative indexing (from end)
print(text[-1])   # n
print(text[-2])   # o
print(text[-6])   # P
```

### String Slicing

```python
text = "Python Programming"

# Basic slicing [start:end]
print(text[0:6])      # Python
print(text[7:18])     # Programming

# Omit start (from beginning)
print(text[:6])       # Python

# Omit end (to end)
print(text[7:])       # Programming

# Negative indices
print(text[-11:])     # Programming

# Step (every nth character)
print(text[::2])      # Pto rgamn
print(text[::-1])     # gnimmargorP nohtyP (reverse!)
```

---

## 🛠️ String Methods

### Case Methods

```python
text = "Hello World"

print(text.upper())        # HELLO WORLD
print(text.lower())        # hello world
print(text.capitalize())   # Hello world
print(text.title())        # Hello World
print(text.swapcase())     # hELLO wORLD

# Check case
print(text.isupper())      # False
print(text.islower())      # False
print("HELLO".isupper())   # True
```

### Whitespace Methods

```python
text = "   Hello World   "

print(text.strip())        # "Hello World"
print(text.lstrip())       # "Hello World   "
print(text.rstrip())       # "   Hello World"

# Remove specific characters
text2 = "***Hello***"
print(text2.strip("*"))    # Hello
```

### Search Methods

```python
text = "Hello World"

print(text.find("World"))      # 6 (index)
print(text.find("Python"))     # -1 (not found)

print(text.index("World"))     # 6
# print(text.index("Python"))  # Raises ValueError

print(text.count("l"))         # 3
print(text.count("World"))     # 1

print(text.startswith("Hello"))  # True
print(text.endswith("World"))    # True
```

### Replace and Split

```python
text = "Hello World"

# Replace
new_text = text.replace("World", "Python")
print(new_text)  # Hello Python

# Replace all occurrences
text2 = "one two one three one"
print(text2.replace("one", "1"))  # 1 two 1 three 1

# Replace limited times
print(text2.replace("one", "1", 2))  # 1 two 1 three one

# Split
words = text.split()
print(words)  # ['Hello', 'World']

csv = "apple,banana,orange"
fruits = csv.split(",")
print(fruits)  # ['apple', 'banana', 'orange']

# Join
words = ["Hello", "World"]
sentence = " ".join(words)
print(sentence)  # Hello World
```

### Validation Methods

```python
# Check if string contains only...
print("hello".isalpha())       # True (letters only)
print("hello123".isalpha())    # False

print("12345".isdigit())       # True (digits only)
print("123.45".isdigit())      # False

print("hello123".isalnum())    # True (letters + digits)
print("hello 123".isalnum())   # False (has space)

print("   ".isspace())         # True (whitespace only)
print("  a  ".isspace())       # False
```

---

## 🎨 String Formatting

### F-Strings (Modern - Python 3.6+)

```python
name = "Alice"
age = 25
height = 1.75

# Basic
print(f"My name is {name}")
print(f"I am {age} years old")

# Expressions
print(f"Next year I'll be {age + 1}")
print(f"2 + 2 = {2 + 2}")

# Method calls
text = "python"
print(f"{text.upper()}")  # PYTHON

# Formatting numbers
price = 49.99
print(f"Price: ${price:.2f}")  # Price: $49.99

pi = 3.14159265359
print(f"Pi: {pi:.2f}")         # Pi: 3.14
print(f"Pi: {pi:.4f}")         # Pi: 3.1416
```

### Format Method

```python
# Positional
print("Hello, {}!".format("World"))
print("{} + {} = {}".format(2, 3, 5))

# Named
print("Name: {name}, Age: {age}".format(name="Bob", age=30))

# Mixed
print("{0} {1} {0}".format("Hello", "World"))  # Hello World Hello
```

### Old Style (%)

```python
name = "Alice"
age = 25

print("Name: %s" % name)
print("Age: %d" % age)
print("%s is %d years old" % (name, age))
```

---

## 🔄 Type Conversion (Casting)

### To String

```python
num = 42
float_num = 3.14
bool_val = True

str_num = str(num)
str_float = str(float_num)
str_bool = str(bool_val)

print(str_num)      # "42"
print(str_float)    # "3.14"
print(str_bool)     # "True"
```

### To Integer

```python
text_num = "42"
float_num = 3.9

int_text = int(text_num)
int_float = int(float_num)  # Truncates to 3

print(int_text)     # 42
print(int_float)    # 3

# Be careful
# int("3.14")  # ValueError
# int("hello") # ValueError
```

### To Float

```python
text_num = "3.14"
int_num = 42

float_text = float(text_num)
float_int = float(int_num)

print(float_text)   # 3.14
print(float_int)    # 42.0
```

### To Boolean

```python
# True if non-empty/non-zero
print(bool("Hello"))    # True
print(bool(""))         # False
print(bool(42))         # True
print(bool(0))          # False
print(bool([1, 2]))     # True
print(bool([]))         # False
```

---

## 💡 Practical Examples

### User Input

```python
# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello {name}!")
print(f"You are {age} years old")

# Convert input to number
age_num = int(age)
print(f"Next year you'll be {age_num + 1}")
```

### String Manipulation

```python
# Clean user input
user_input = "  hello world  "
cleaned = user_input.strip().title()
print(cleaned)  # Hello World

# Validate email (simple)
email = "user@example.com"
is_valid = "@" in email and "." in email
print(f"Email valid: {is_valid}")

# Extract extension
filename = "document.pdf"
extension = filename.split(".")[-1]
print(f"Extension: {extension}")  # pdf
```

### Text Processing

```python
# Count words
text = "Python is awesome and Python is powerful"
words = text.split()
print(f"Word count: {len(words)}")

# Find and replace
new_text = text.replace("Python", "JavaScript")
print(new_text)

# Count occurrences
python_count = text.count("Python")
print(f"'Python' appears {python_count} times")
```

---

## 🎓 Summary

**Variables:**
- Store data with descriptive names
- Use snake_case naming
- Python is dynamically typed

**Strings:**
- Immutable text data
- Triple quotes for multiline
- Rich set of methods

**Key Operations:**
- Indexing and slicing
- String methods (upper, lower, strip, etc.)
- F-strings for formatting
- Type conversion

**Best Practices:**
- Use f-strings (modern)
- Use descriptive variable names
- Validate and clean user input

---

## 🔗 Related Topics

- [[02_Lists_Deep_Dive|Lists]]
- [[04_Dictionaries_Mastery|Dictionaries]]
- [[25_Regular_Expressions|Regex]]

---

[[00_Index|← Back to Index]]

*Master the basics, master Python! 🐍*

# Slicing
text[0]       # "H"
text[-1]      # "d"
text[0:5]     # "Hello"
text[::-1]    # Reverse
```

---

## ✅ Best Practices

✅ Use f-strings for formatting
✅ Strings are immutable
✅ Triple quotes for multiline
✅ Use .join() for concatenating many strings

---

[[00_Index|← Back to Index]]
