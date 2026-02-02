---
title: Loops and Iteration
category: control-flow
tags: ['python', 'loops', 'iteration', 'for', 'while', 'core']
created: 2026-01-27
type: topic
---

# Loops and Iteration

[[00_Index|← Back to Index]]

> **Repeat code with for and while loops**

---

## 🔄 While Loop

```python
# Basic while
count = 0
while count < 5:
    print(count)
    count += 1
# Prints: 0, 1, 2, 3, 4

# While with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(f'Final count: {count}')
# Prints: 0, 1, 2, 3, 4, Final count: 5

# Break in while
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
# Prints: 0, 1, 2

# Continue in while
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1
# Prints: 0, 1, 2, 4 (skips 3)
```

---

## 🔁 For Loop

### Loop over List

```python
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)
# Prints: 0, 1, 2, 3, 4, 5
```

### Loop over String

```python
language = 'Python'
for letter in language:
    print(letter)
# Prints: P, y, t, h, o, n

# With index
for i in range(len(language)):
    print(f"{i}: {language[i]}")
```

### Loop over Tuple

```python
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

### Loop over Dictionary

```python
person = {'name': 'John', 'age': 30, 'city': 'NYC'}

# Keys (default)
for key in person:
    print(key)

# Values
for value in person.values():
    print(value)

# Key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

### Range Function

```python
# range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 5):
    print(i)  # 2, 3, 4

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

---

## 🎯 Enumerate

```python
fruits = ['apple', 'banana', 'orange']

# Get index and value
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# Start index from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
```

---

## 🔗 Zip

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

# Combine two lists
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

---

## 🛑 Break and Continue

```python
# Break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i)
# Prints: 0, 1, 2, 3, 4

# Continue - skip iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Prints: 1, 3, 5, 7, 9
```

---

[[00_Index|← Back to Index]]

*Loop and conquer! 🔄*
        continue
    print(i)
```

---

## ✅ Best Practices

✅ Use enumerate for index
✅ Use zip for parallel iteration
✅ Prefer for over while

---

[[00_Index|← Back to Index]]
