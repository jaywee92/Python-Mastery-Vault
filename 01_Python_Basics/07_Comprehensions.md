---
title: Comprehensions
category: control-flow
tags: ['python', 'comprehensions', 'list-comp', 'pythonic', 'advanced']
created: 2026-01-27
type: topic
---

# Comprehensions

[[00_Index|← Back to Index]]

> **Write elegant, concise Python with comprehensions**

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║      📋 LIST COMPREHENSION - COMPACT LIST CREATION            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   TRADITIONAL METHOD:                                         ║
║   ┌──────────────────────────┐                               ║
║   │ nums = []                │                               ║
║   │ for i in range(5):       │   4 lines of code            ║
║   │     nums.append(i * 2)   │   3 indentations             ║
║   │ # [0, 2, 4, 6, 8]        │                               ║
║   └──────────────────────────┘                               ║
║                                                               ║
║   COMPREHENSION (Pythonic):                                   ║
║   ┌──────────────────────────────────────┐                   ║
║   │ nums = [i * 2 for i in range(5)]     │  1 line!          ║
║   │ # [0, 2, 4, 6, 8]                    │                   ║
║   └──────────────────────────────────────┘                   ║
║                                                               ║
║   Structure: [EXPRESSION  for  VARIABLE  in  ITERABLE]       ║
║              │TRANSFORM │    │ELEMENT │      │SOURCE│        ║
║                                                               ║
║   Extended comprehension with filter:                         ║
║   [i for i in range(10) if i % 2 == 0]                       ║
║   # [0, 2, 4, 6, 8]  ← Only even numbers                    ║
║                                                               ║
║   💡 Faster, more readable and Pythonic than loops           ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📋 List Comprehension

### Basic Syntax

```python
# Syntax: [expression for item in iterable]

# Traditional way
language = 'Python'
lst = []
for i in language:
    lst.append(i)
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']

# List comprehension way
lst = [i for i in language]
print(lst)  # ['P', 'y', 't', 'h', 'o', 'n']
```

### Generating Numbers

```python
# Generate numbers 0-10
numbers = [i for i in range(11)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares
squares = [i * i for i in range(11)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)  # [(0, 0), (1, 1), (2, 4), (3, 9), ...]
```

### With Conditions

```python
# Even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filter with multiple conditions
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even)  # [4, 6, 8, 10]
```

### Nested Comprehensions

```python
# Flatten 2D list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in list_of_lists for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create matrix
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)
# [[0, 0, 0],
#  [0, 1, 2],
#  [0, 2, 4]]
```

### If-Else in Comprehension

```python
# Conditional expression
result = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(result)  # ['even', 'odd', 'even', 'odd', 'even']

# Transform based on condition
numbers = [1, 2, 3, 4, 5]
doubled_evens = [x * 2 if x % 2 == 0 else x for x in numbers]
print(doubled_evens)  # [1, 4, 3, 8, 5]
```

---

## 📖 Dictionary Comprehension

```python
# Basic dict comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# From two lists
keys = ['name', 'age', 'city']
values = ['John', 30, 'NYC']
person = {k: v for k, v in zip(keys, values)}
print(person)  # {'name': 'John', 'age': 30, 'city': 'NYC'}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Swap keys and values
original = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
```

---

## 🎲 Set Comprehension

```python
# Basic set comprehension
unique = {x % 3 for x in range(10)}
print(unique)  # {0, 1, 2}

# Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_nums = {x for x in numbers}
print(unique_nums)  # {1, 2, 3, 4, 5}

# With condition
even_set = {x for x in range(20) if x % 2 == 0}
print(even_set)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```

---

## 🔄 Generator Expression

```python
# Like list comprehension but with ()
# More memory efficient - generates values on demand
gen = (x**2 for x in range(10))
print(type(gen))  # <class 'generator'>

# Use in loop
for num in gen:
    print(num)

# Convert to list if needed
squares_list = list(x**2 for x in range(10))
```

---

## 💡 Practical Examples

### Filter and Transform

```python
# Get lengths of strings
words = ['hello', 'world', 'python', 'code']
lengths = [len(word) for word in words]
print(lengths)  # [5, 5, 6, 4]

# Uppercase specific items
words = ['hello', 'world', 'python']
result = [word.upper() if len(word) > 5 else word for word in words]
print(result)  # ['hello', 'world', 'PYTHON']

# Extract first letters
first_letters = [word[0] for word in words]
print(first_letters)  # ['h', 'w', 'p']
```

### Nested Data Processing

```python
# Extract from nested structure
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35}
]

# Get all names
names = [person['name'] for person in people]
print(names)  # ['Alice', 'Bob', 'Charlie']

# Filter by age
adults = [p['name'] for p in people if p['age'] >= 30]
print(adults)  # ['Bob', 'Charlie']
```

### Matrix Operations

```python
# Transpose matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
# [[1, 4, 7],
#  [2, 5, 8],
#  [3, 6, 9]]

# Diagonal elements
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(diagonal)  # [1, 5, 9]
```

---

## ✅ Best Practices

### 1. Keep It Simple

```python
# Good - readable
squares = [x**2 for x in range(10)]

# Bad - too complex
result = [x**2 if x % 2 == 0 else x**3 
          for x in range(20) 
          if x > 5 and x < 15 
          if x % 3 != 0]
```

### 2. Use Regular Loops for Complex Logic

```python
# Bad - hard to read comprehension
result = [process(x) if validate(x) and check(x) else default 
          for x in items if filter(x)]

# Good - use regular loop
result = []
for x in items:
    if filter(x) and validate(x) and check(x):
        result.append(process(x))
    else:
        result.append(default)
```

### 3. Limit Nesting

```python
# Acceptable - 2 levels
flattened = [num for row in matrix for num in row]

# Avoid - 3+ levels (hard to read)
result = [z for x in data for y in x for z in y]
```

### 4. Choose Right Tool

```python
# List comprehension - need list
numbers = [x for x in range(10)]

# Generator - large data, iterate once
numbers = (x for x in range(1000000))

# map/filter - simple transforms
numbers = list(map(lambda x: x**2, range(10)))
```

---

## 🎓 Summary

**Comprehensions:**
- List: `[x for x in items]`
- Dict: `{k: v for k, v in items}`
- Set: `{x for x in items}`
- Generator: `(x for x in items)`

**Key Benefits:**
- More concise than loops
- Often faster
- Pythonic and readable (when simple)

**Remember:** Use for simple transforms, regular loops for complex logic!

---

## 🔗 Related Topics

- [[02_Lists_Deep_Dive|Lists]]
- [[09_Lambda_and_Builtins|Lambda Functions]]

---

[[00_Index|← Back to Index]]

*Comprehend with comprehensions! 📋*
