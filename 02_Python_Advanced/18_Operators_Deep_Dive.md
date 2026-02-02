---
title: Operators Deep Dive
tags: [python, operators, arithmetic, comparison, logical, advanced]
category: advanced
type: topic
---

# 31. Operators Deep Dive

[[00_Index|← Back to Index]]

> **Master all Python operators with practical examples**

---

## 📋 Table of Contents

- [Arithmetic Operators](#arithmetic-operators)
- [Comparison Operators](#comparison-operators)
- [Logical Operators](#logical-operators)
- [Bitwise Operators](#bitwise-operators)
- [Assignment Operators](#assignment-operators)
- [Identity Operators](#identity-operators)
- [Membership Operators](#membership-operators)
- [Operator Precedence](#operator-precedence)

---

## 🧮 Arithmetic Operators

### Basic Operations

Python supports all standard arithmetic operations:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor Division | `5 // 2` | `2` |
| `%` | Modulus | `5 % 2` | `1` |
| `**` | Exponentiation | `5 ** 2` | `25` |

### Integer Arithmetic

```python
# Basic integer operations
print('Addition:', 1 + 2)           # 3
print('Subtraction:', 2 - 1)        # 1
print('Multiplication:', 2 * 3)     # 6
print('Division:', 4 / 2)           # 2.0 (always returns float!)
print('Division:', 7 / 2)           # 3.5

# Floor division - removes decimal part
print('Floor Division:', 7 // 2)    # 3
print('Floor Division:', 7 // 3)    # 2

# Modulus - returns remainder
print('Modulus:', 3 % 2)            # 1
print('Modulus:', 10 % 3)           # 1

# Exponentiation - power
print('Exponentiation:', 2 ** 3)    # 8 (2 * 2 * 2)
print('Exponentiation:', 5 ** 2)    # 25
```

### Float Arithmetic

```python
# Floating point numbers
print('Pi:', 3.14)
print('Gravity:', 9.81)

# Mixed operations
print('Mixed:', 5 * 2.5)            # 12.5
print('Mixed:', 10 / 4)             # 2.5
```

### Complex Number Arithmetic

```python
# Complex numbers
print('Complex:', 1 + 1j)
print('Multiply:', (1 + 1j) * (1 - 1j))   # (2+0j)
```

### Practical Examples

```python
# Calculating area of a circle
radius = 10
area = 3.14 * radius ** 2
print(f'Area of circle: {area}')    # 314.0

# Calculating area of rectangle
length = 10
width = 20
area = length * width
print(f'Area of rectangle: {area}')  # 200

# Calculating weight
mass = 75  # kg
gravity = 9.81  # m/s²
weight = mass * gravity
print(f'Weight: {weight} N')        # 735.75 N

# Calculating density
mass = 75  # kg
volume = 0.075  # m³
density = mass / volume
print(f'Density: {density} kg/m³')  # 1000.0 kg/m³
```

---

## ⚖️ Comparison Operators

Compare two values and return boolean result.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal | `3 == 2` | `False` |
| `!=` | Not equal | `3 != 2` | `True` |
| `>` | Greater than | `3 > 2` | `True` |
| `<` | Less than | `3 < 2` | `False` |
| `>=` | Greater or equal | `3 >= 3` | `True` |
| `<=` | Less or equal | `2 <= 3` | `True` |

### Basic Comparisons

```python
# Number comparisons
print(3 > 2)      # True
print(3 >= 2)     # True
print(3 < 2)      # False
print(2 < 3)      # True
print(2 <= 3)     # True
print(3 == 2)     # False
print(3 != 2)     # True
```

### String Comparisons

```python
# Comparing string lengths
print(len('mango') == len('avocado'))   # False
print(len('mango') != len('avocado'))   # True
print(len('mango') < len('avocado'))    # True
print(len('milk') == len('meat'))       # True

# Lexicographic comparison
print('apple' < 'banana')               # True
print('zebra' > 'aardvark')            # True
```

### Practical Examples

```python
# Age verification
age = 25
is_adult = age >= 18
print(f'Is adult: {is_adult}')          # True

# Temperature check
temp = 22
is_comfortable = 18 <= temp <= 24
print(f'Comfortable: {is_comfortable}') # True

# Score comparison
score = 85
passed = score >= 60
print(f'Passed: {passed}')              # True
```

---

## 🔀 Logical Operators

Combine boolean expressions.

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | True if both true | `True and True` → `True` |
| `or` | True if one true | `True or False` → `True` |
| `not` | Inverts boolean | `not True` → `False` |

### AND Operator

```python
# Both must be True
print(True and True)     # True
print(True and False)    # False
print(False and False)   # False

# Practical example
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f'Can drive: {can_drive}')  # True
```

### OR Operator

```python
# At least one must be True
print(True or True)      # True
print(True or False)     # True
print(False or False)    # False

# Practical example
is_weekend = True
is_holiday = False
can_relax = is_weekend or is_holiday
print(f'Can relax: {can_relax}')  # True
```

### NOT Operator

```python
# Inverts the boolean value
print(not True)          # False
print(not False)         # True

# Practical example
is_raining = False
go_outside = not is_raining
print(f'Go outside: {go_outside}')  # True
```

### Combined Logic

```python
# Complex conditions
age = 20
has_ticket = True
has_id = True

can_enter = age >= 18 and (has_ticket or has_id)
print(f'Can enter: {can_enter}')    # True

# Eligibility check
score = 75
attendance = 85
passed = score >= 60 and attendance >= 80
print(f'Passed: {passed}')          # True
```

---

## 🔧 Assignment Operators

Assign and modify variables in one step.

| Operator | Example | Equivalent |
|----------|---------|------------|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

### Examples

```python
# Basic assignment
x = 10
print(f'x = {x}')               # 10

# Add and assign
x += 5  # x = x + 5
print(f'x += 5: {x}')           # 15

# Subtract and assign
x -= 3  # x = x - 3
print(f'x -= 3: {x}')           # 12

# Multiply and assign
x *= 2  # x = x * 2
print(f'x *= 2: {x}')           # 24

# Divide and assign
x /= 4  # x = x / 4
print(f'x /= 4: {x}')           # 6.0

# Power and assign
x = 2
x **= 3  # x = x ** 3
print(f'x **= 3: {x}')          # 8
```

---

## 🆔 Identity Operators

Check if two variables refer to the same object.

| Operator | Description |
|----------|-------------|
| `is` | True if same object |
| `is not` | True if different objects |

```python
# Identity check
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is z)           # True (same object)
print(x is y)           # False (different objects)
print(x == y)           # True (same value)

# With None
value = None
print(value is None)    # True (correct way)
print(value == None)    # True (works but 'is' preferred)
```

---

## 📦 Membership Operators

Check if value exists in sequence.

| Operator | Description |
|----------|-------------|
| `in` | True if found |
| `not in` | True if not found |

```python
# List membership
fruits = ['apple', 'banana', 'orange']
print('apple' in fruits)        # True
print('grape' in fruits)        # False
print('grape' not in fruits)    # True

# String membership
text = 'Hello World'
print('Hello' in text)          # True
print('hello' in text)          # False (case-sensitive)

# Dictionary membership (checks keys)
person = {'name': 'John', 'age': 30}
print('name' in person)         # True
print('John' in person)         # False (value, not key)
```

---

## 🎯 Operator Precedence

Order of operations (highest to lowest):

1. `()`  Parentheses
2. `**`  Exponentiation
3. `+x`, `-x`, `~x`  Unary plus, minus, NOT
4. `*`, `/`, `//`, `%`  Multiplication, Division
5. `+`, `-`  Addition, Subtraction
6. `<<`, `>>`  Bit shifts
7. `&`  Bitwise AND
8. `^`  Bitwise XOR
9. `|`  Bitwise OR
10. `==`, `!=`, `>`, `>=`, `<`, `<=`  Comparisons
11. `not`  Logical NOT
12. `and`  Logical AND
13. `or`  Logical OR

### Examples

```python
# Without parentheses
result = 2 + 3 * 4
print(result)           # 14 (not 20)

# With parentheses
result = (2 + 3) * 4
print(result)           # 20

# Complex expression
result = 2 ** 3 ** 2    # Right to left for **
print(result)           # 512 (not 64)

# With parentheses
result = (2 ** 3) ** 2
print(result)           # 64
```

---

## 💡 Best Practices

### 1. Use Parentheses for Clarity

```python
# Unclear
result = a + b * c

# Clear
result = a + (b * c)
```

### 2. Prefer `is` for None Checks

```python
# Good
if value is None:
    pass

# Avoid
if value == None:
    pass
```

### 3. Use Comparison Chaining

```python
# Instead of
if x >= 0 and x <= 100:
    pass

# Use
if 0 <= x <= 100:
    pass
```

### 4. Avoid Complex Expressions

```python
# Hard to read
result = (a + b) * (c - d) / (e + f) ** 2

# Better - break it down
sum_ab = a + b
diff_cd = c - d
sum_ef_squared = (e + f) ** 2
result = (sum_ab * diff_cd) / sum_ef_squared
```

---

## 🎓 Summary

**Arithmetic:** `+`, `-`, `*`, `/`, `//`, `%`, `**`  
**Comparison:** `==`, `!=`, `>`, `<`, `>=`, `<=`  
**Logical:** `and`, `or`, `not`  
**Assignment:** `=`, `+=`, `-=`, `*=`, etc.  
**Identity:** `is`, `is not`  
**Membership:** `in`, `not in`

**Key Takeaway:** Use operators to build powerful expressions while keeping code readable!

---

## 🔗 Related Topics

- [[01_Variables_and_Strings_Advanced|Variables & Strings]]
- [[05_Conditionals|Conditionals]]
- [[06_Loops_and_Iteration|Loops]]

---

[[00_Index|← Back to Index]]

*Master operators, master Python! 🎯*
