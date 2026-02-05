---
title: Conditionals
category: control-flow
tags: ['python', 'conditionals', 'if-statements', 'logic', 'basics']
created: 2026-01-27
type: topic
---

# Conditionals

[[00_Index|← Back to Index]]

> **Control program flow with if/elif/else**

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║      🔀 CONDITIONALS - DECISION TREE FOR PYTHON               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║                    Is x > 0?                                 ║
║                        │                                      ║
║            ┌───────────┴───────────┐                          ║
║           YES                      NO                         ║
║            │                        │                        ║
║        Code A                Is x < 0?                        ║
║                                 │                             ║
║                     ┌───────────┴───────────┐                ║
║                   YES                       NO               ║
║                     │                        │               ║
║                  Code B                  Code C               ║
║                                                               ║
║   if x > 0:              # If true                           ║
║       print("Positive")  # This code runs                    ║
║   elif x < 0:            # Else if                           ║
║       print("Negative")  # This code runs                    ║
║   else:                  # Otherwise                          ║
║       print("Zero")      # This code runs                    ║
║                                                               ║
║   💡 Only one code block executes!                           ║
║   💡 Conditions checked from top to bottom                   ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 🔀 Basic if Statement

```python
a = 3
if a > 0:
    print('A is a positive number')
# Output: A is a positive number
```

## 🔀 if-else

```python
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
# Output: A is a positive number
```

## 🔀 if-elif-else

```python
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
# Output: A is zero
```

## 🎯 Ternary Operator

```python
a = 3
result = 'A is positive' if a > 0 else 'A is negative'
print(result)  # A is positive
```

## 📦 Nested Conditions

```python
a = 10
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive odd number')
```

## 💡 Practical Examples

```python
# Age check
age = 25
if age >= 18:
    status = 'adult'
elif age >= 13:
    status = 'teen'
else:
    status = 'child'

# Empty check
items = [1, 2, 3]
if items:  # Truthy if not empty
    print(f'First item: {items[0]}')

# Multiple conditions
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
```

---

[[00_Index|← Back to Index]]

*Make decisions! 🎯*
✅ Avoid nested ifs
✅ Use elif not multiple ifs

---

[[00_Index|← Back to Index]]
