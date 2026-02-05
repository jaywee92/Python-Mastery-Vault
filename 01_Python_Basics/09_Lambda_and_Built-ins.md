---
title: Lambda and Built-ins
category: functions
tags: ['python', 'lambda', 'functional', 'advanced', 'map-filter']
created: 2026-01-27
type: topic
---

# Lambda and Built-ins

[[00_Index|← Back to Index]]

> **Functional programming with lambda and built-in functions**

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║      ⚡ LAMBDA - ANONYME EINZEILIGE FUNKTIONEN                ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   TRADITIONELLE FUNKTION:                                     ║
║   def add(a, b):                                              ║
║       return a + b                                            ║
║   ↓                                                           ║
║   LAMBDA EQUIVALENT (Kompakt):                                ║
║   add = lambda a, b: a + b                                    ║
║                                                               ║
║   Struktur:  lambda PARAMETER: AUSDRUCK                       ║
║             │       │           │                             ║
║             │       │           └─ Was zurückgeben            ║
║             │       └─ Eingaben                               ║
║             └─ Schlüsselwort                                  ║
║                                                               ║
║   Häufige Verwendungen:                                        ║
║   • map():     Funktion auf jedes Element anwenden            ║
║     nums = [1,2,3,4]                                          ║
║     result = map(lambda x: x*2, nums)                         ║
║     # [2,4,6,8]                                               ║
║                                                               ║
║   • filter(): Nur Elemente mit Bedingung                      ║
║     nums = [1,2,3,4,5]                                        ║
║     result = filter(lambda x: x > 2, nums)                    ║
║     # [3,4,5]                                                 ║
║                                                               ║
║   • sorted(): Mit Custom-Schlüssel sortieren                 ║
║     words = ["apple", "pie", "a"]                             ║
║     result = sorted(words, key=lambda x: len(x))              ║
║     # ["a", "pie", "apple"]  (nach Länge)                    ║
║                                                               ║
║   💡 Lambda = Anonyme, einzeilige, schnelle Funktionen        ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 🎯 Lambda Functions

### Basic Lambda

```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2
print(square(5))  # 25

# Multiple parameters
add = lambda a, b: a + b
print(add(3, 7))  # 10

multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))  # 24
```

### Lambda in Action

```python
# Immediate execution
result = (lambda a, b: a + b)(2, 3)
print(result)  # 5

# With conditions
max_value = lambda a, b: a if a > b else b
print(max_value(10, 5))  # 10
```

---

## 🗺️ map() Function

```python
# Apply function to all items
numbers = [1, 2, 3, 4, 5]

# With lambda
squares = list(map(lambda x: x**2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# Multiple iterables
nums1 = [1, 2, 3]
nums2 = [10, 20, 30]
result = list(map(lambda x, y: x + y, nums1, nums2))
print(result)  # [11, 22, 33]

# With regular function
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
```

---

## 🔍 filter() Function

```python
# Filter items based on condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Get odd numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)  # [1, 3, 5, 7, 9]

# Filter strings
words = ['hello', 'world', 'python', 'code']
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)  # ['python']
```

---

## 📦 reduce() Function

```python
from functools import reduce

# Reduce to single value
numbers = [1, 2, 3, 4, 5]

# Sum all
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Product of all
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Max value
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5
```

---

## 🔢 sorted() Function

```python
# Sort with key
words = ['apple', 'pie', 'cherry', 'banana']

# Sort by length
by_length = sorted(words, key=len)
print(by_length)  # ['pie', 'apple', 'cherry', 'banana']

# Sort by last letter
by_last = sorted(words, key=lambda w: w[-1])
print(by_last)  # ['banana', 'apple', 'pie', 'cherry']

# Sort tuples
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
by_grade = sorted(students, key=lambda x: x[1], reverse=True)
print(by_grade)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]
```

---

## ✅ any() and all()

```python
# any() - True if ANY element is True
numbers = [0, 0, 1, 0]
print(any(numbers))  # True

numbers = [0, 0, 0]
print(any(numbers))  # False

# Check if any positive
nums = [-1, -2, 3, -4]
print(any(n > 0 for n in nums))  # True

# all() - True if ALL elements are True
numbers = [1, 2, 3, 4]
print(all(numbers))  # True

numbers = [1, 2, 0, 4]
print(all(numbers))  # False

# Check if all positive
nums = [1, 2, 3, 4]
print(all(n > 0 for n in nums))  # True
```

---

## 🎨 Higher Order Functions

### Function as Parameter

```python
def apply_twice(func, value):
    return func(func(value))

def add_five(x):
    return x + 5

result = apply_twice(add_five, 10)
print(result)  # 20 (10 + 5 + 5)
```

### Function as Return Value

```python
def get_operation(op):
    if op == 'square':
        return lambda x: x ** 2
    elif op == 'cube':
        return lambda x: x ** 3
    elif op == 'double':
        return lambda x: x * 2

square_func = get_operation('square')
print(square_func(5))  # 25

cube_func = get_operation('cube')
print(cube_func(3))  # 27
```

---

## 💡 Practical Examples

### Transform Data

```python
# Convert to uppercase
names = ['alice', 'bob', 'charlie']
upper_names = list(map(str.upper, names))
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# Extract ages
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30}
]
ages = list(map(lambda p: p['age'], people))
print(ages)  # [25, 30]
```

### Filter and Process

```python
# Get adult names
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 30}
]

adults = filter(lambda p: p['age'] >= 18, people)
adult_names = map(lambda p: p['name'], adults)
print(list(adult_names))  # ['Alice', 'Charlie']
```

### Chain Operations

```python
numbers = [1, 2, 3, 4, 5, 6]

# Filter evens, square them, sum
result = sum(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # 56 (4 + 16 + 36)
```

---

## ✅ Best Practices

### When to Use Lambda

```python
# Good - simple one-liners
squares = map(lambda x: x**2, numbers)
evens = filter(lambda x: x % 2 == 0, numbers)

# Bad - complex logic
# result = map(lambda x: x**2 if x > 0 else -x**2 if x < -10 else 0, numbers)

# Better - use regular function for complex logic
def complex_transform(x):
    if x > 0:
        return x**2
    elif x < -10:
        return -x**2
    return 0

result = map(complex_transform, numbers)
```

### Lambda vs Comprehension

```python
# Lambda with map
squares = list(map(lambda x: x**2, range(10)))

# List comprehension (often more Pythonic)
squares = [x**2 for x in range(10)]

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, range(10)))

# List comprehension (often clearer)
evens = [x for x in range(10) if x % 2 == 0]
```

---

## 🎓 Summary

**Lambda:** Anonymous functions  
**map():** Apply function to all items  
**filter():** Keep items that match condition  
**reduce():** Combine items to single value  
**sorted():** Sort with custom key  
**any()/all():** Check conditions

---

## 🔗 Related Topics

- [[08_Functions|Functions]]
- [[07_Comprehensions|Comprehensions]]

---

[[00_Index|← Back to Index]]

*Functional power! ⚡*
any(x > 4 for x in [1,2,3,4,5])
all(x > 0 for x in [1,2,3])
```

---

## ✅ Best Practices

✅ Use for simple functions
✅ Comprehensions often clearer
✅ sorted() very powerful

---

[[00_Index|← Back to Index]]
