---
title: Operators (HEAVILY TESTED!)
tags: [pcep, python, operators, arithmetic, comparison, logical]
created: 2026-01-30
exam_section: 1
exam_weight: 12%
---

# ➕ Operators

[[00_Index|← Back to Index]] | [[03_Literals_Variables|← Literals]] | [[05_Data_Types|Data Types →]]

> **"Know operator precedence - it appears in MANY questions!"**

---

## ⚠️ EXAM ALERT: Operators are heavily tested!

---

## 🔢 Arithmetic Operators

```python
# ═══════════════════════════════════════════════════════════════
# ARITHMETIC OPERATORS
# ═══════════════════════════════════════════════════════════════

a, b = 10, 3

print(a + b)   # 13  Addition
print(a - b)   # 7   Subtraction
print(a * b)   # 30  Multiplication
print(a / b)   # 3.333...  Division (ALWAYS returns float!)
print(a // b)  # 3   Floor division (integer division)
print(a % b)   # 1   Modulo (remainder)
print(a ** b)  # 1000  Exponentiation (10³)

# IMPORTANT: Division (/) always returns float!
print(10 / 2)     # 5.0 (not 5!)
print(type(10/2)) # <class 'float'>

# Floor division (//) rounds DOWN
print(7 // 2)     # 3
print(-7 // 2)    # -4 (rounds toward negative infinity!)

# Modulo with negative numbers
print(7 % 3)      # 1
print(-7 % 3)     # 2 (result has sign of divisor)
print(7 % -3)     # -2

# Exponentiation is right-associative
print(2 ** 3 ** 2)   # 512 (= 2^9, not 8^2)
print(2 ** (3 ** 2)) # 512
print((2 ** 3) ** 2) # 64
```

---

## 🔍 Comparison Operators

```python
# ═══════════════════════════════════════════════════════════════
# COMPARISON OPERATORS (return True/False)
# ═══════════════════════════════════════════════════════════════

a, b = 10, 5

print(a == b)  # False  Equal
print(a != b)  # True   Not equal
print(a > b)   # True   Greater than
print(a < b)   # False  Less than
print(a >= b)  # True   Greater than or equal
print(a <= b)  # False  Less than or equal

# Chained comparisons (Python special!)
x = 5
print(1 < x < 10)      # True (1 < 5 AND 5 < 10)
print(1 < x < 3)       # False
print(1 < x <= 5 < 10) # True

# Comparing different types
print(5 == 5.0)    # True (values equal)
print(5 == "5")    # False (different types)
print(True == 1)   # True (bool is subclass of int)
print(False == 0)  # True

# String comparison (lexicographic/alphabetical)
print("apple" < "banana")  # True
print("Apple" < "apple")   # True (uppercase < lowercase)
print("abc" < "abcd")      # True (shorter comes first)
```

---

## 🔗 Logical Operators

```python
# ═══════════════════════════════════════════════════════════════
# LOGICAL OPERATORS
# ═══════════════════════════════════════════════════════════════

# and - True if BOTH are True
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# or - True if AT LEAST ONE is True
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

# not - inverts the boolean
print(not True)   # False
print(not False)  # True

# Short-circuit evaluation!
# and stops at first False
print(False and print("Not printed"))  # False (print not called!)

# or stops at first True
print(True or print("Not printed"))    # True (print not called!)

# Return values (not always True/False!)
print(5 and 3)      # 3 (last evaluated)
print(0 and 3)      # 0 (first falsy)
print(5 or 3)       # 5 (first truthy)
print(0 or 3)       # 3 (first truthy)
print("" or "hi")   # "hi"
print([] or [1,2])  # [1, 2]
```

---

## 🔢 Bitwise Operators

```python
# ═══════════════════════════════════════════════════════════════
# BITWISE OPERATORS
# ═══════════════════════════════════════════════════════════════

a = 5   # 0101 in binary
b = 3   # 0011 in binary

print(a & b)   # 1   AND  (0001)
print(a | b)   # 7   OR   (0111)
print(a ^ b)   # 6   XOR  (0110)
print(~a)      # -6  NOT  (inverts all bits)
print(a << 1)  # 10  Left shift  (1010)
print(a >> 1)  # 2   Right shift (0010)

# Useful patterns
# Check if even/odd
print(7 & 1)  # 1 (odd)
print(8 & 1)  # 0 (even)

# Multiply/divide by 2
print(5 << 1)  # 10 (multiply by 2)
print(5 >> 1)  # 2 (divide by 2, floor)
```

---

## ✏️ Assignment Operators

```python
# ═══════════════════════════════════════════════════════════════
# ASSIGNMENT OPERATORS
# ═══════════════════════════════════════════════════════════════

x = 10       # Simple assignment

# Compound assignment (augmented)
x += 5       # x = x + 5  → 15
x -= 3       # x = x - 3  → 12
x *= 2       # x = x * 2  → 24
x /= 4       # x = x / 4  → 6.0 (now float!)
x //= 2      # x = x // 2 → 3.0
x %= 2       # x = x % 2  → 1.0
x **= 3      # x = x ** 3 → 1.0

# Bitwise assignment
a = 5
a &= 3       # a = a & 3
a |= 2       # a = a | 2
a ^= 1       # a = a ^ 1
a <<= 1      # a = a << 1
a >>= 1      # a = a >> 1

# Walrus operator (Python 3.8+) - assigns and returns
# if (n := len("hello")) > 3:
#     print(f"Length is {n}")
```

---

## 🔍 Identity and Membership Operators

```python
# ═══════════════════════════════════════════════════════════════
# IDENTITY OPERATORS (is, is not)
# ═══════════════════════════════════════════════════════════════

# 'is' checks if same OBJECT (identity)
# '==' checks if same VALUE (equality)

a = [1, 2, 3]
b = a              # Same object
c = [1, 2, 3]      # Different object, same value

print(a is b)      # True (same object)
print(a is c)      # False (different objects)
print(a == c)      # True (same value)

# Use 'is' for None, True, False
x = None
print(x is None)      # True (correct)
print(x == None)      # True (works but not preferred)

# Small integer caching (-5 to 256)
a = 100
b = 100
print(a is b)  # True (cached)

a = 1000
b = 1000
print(a is b)  # False (not cached) - may vary!

# ═══════════════════════════════════════════════════════════════
# MEMBERSHIP OPERATORS (in, not in)
# ═══════════════════════════════════════════════════════════════

# Check if element exists in sequence
print(3 in [1, 2, 3])       # True
print(4 not in [1, 2, 3])   # True
print("h" in "hello")       # True
print("x" not in "hello")   # True

# Dictionary membership checks KEYS
d = {"a": 1, "b": 2}
print("a" in d)         # True (key exists)
print(1 in d)           # False (1 is value, not key)
print(1 in d.values())  # True
```

---

## 📊 Operator Precedence (CRITICAL!)

```
┌─────────────────────────────────────────────────────────────────┐
│              OPERATOR PRECEDENCE (Highest to Lowest)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. ()              Parentheses                                 │
│  2. **              Exponentiation (right-to-left!)             │
│  3. +x, -x, ~x      Unary plus, minus, NOT                      │
│  4. *, /, //, %     Multiplication, division, modulo            │
│  5. +, -            Addition, subtraction                       │
│  6. <<, >>          Bitwise shifts                              │
│  7. &               Bitwise AND                                 │
│  8. ^               Bitwise XOR                                 │
│  9. |               Bitwise OR                                  │
│  10. ==, !=, <, <=, >, >=, is, in  Comparisons                 │
│  11. not            Logical NOT                                 │
│  12. and            Logical AND                                 │
│  13. or             Logical OR                                  │
│                                                                  │
│  Remember: PEMDAS doesn't fully apply!                          │
│  When in doubt, use parentheses!                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# PRECEDENCE EXAMPLES
# ═══════════════════════════════════════════════════════════════

# Exponentiation before negation
print(-2 ** 2)     # -4 (not 4!)
print((-2) ** 2)   # 4

# Multiplication before addition
print(2 + 3 * 4)   # 14 (not 20)
print((2 + 3) * 4) # 20

# Comparison before logical
print(1 < 2 and 3 < 4)  # True
# Evaluated as: (1 < 2) and (3 < 4)

# not before and before or
print(not True or False)           # False
# = (not True) or False = False or False

print(True or False and False)     # True
# = True or (False and False) = True or False

print(not True and False or True)  # True
# = ((not True) and False) or True = (False and False) or True

# Use parentheses for clarity!
print((not True) and (False or True))  # False
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: Division always returns float
print(10 / 2)      # 5.0 (not 5!)

# TRAP 2: Floor division with negatives
print(-7 // 2)     # -4 (not -3!)
print(7 // -2)     # -4

# TRAP 3: Exponentiation is right-associative
print(2 ** 3 ** 2) # 512 (= 2^9)

# TRAP 4: Negation and exponentiation
print(-2 ** 2)     # -4 (** before -)

# TRAP 5: is vs ==
a = [1, 2]
b = [1, 2]
print(a == b)  # True
print(a is b)  # False

# TRAP 6: Logical operators return values
print(0 or 5)    # 5 (not True!)
print(5 and 0)   # 0 (not False!)

# TRAP 7: not has lower precedence than comparison
print(not 1 == 1)     # False (not (1 == 1))
print(not 1 == 2)     # True (not (1 == 2))
# print(1 not == 1)   # SyntaxError!
print(1 != 1)         # False (correct way)

# TRAP 8: Chained comparison
x = 5
print(1 < x < 10)     # True (1 < 5 and 5 < 10)
print(1 < x > 3)      # True (1 < 5 and 5 > 3)
```

---

## 📝 Quick Reference

| Operator | Description | Example |
|----------|-------------|---------|
| `+` `-` `*` | Add, Sub, Mul | `2 + 3` → `5` |
| `/` | Division (float) | `7 / 2` → `3.5` |
| `//` | Floor division | `7 // 2` → `3` |
| `%` | Modulo | `7 % 3` → `1` |
| `**` | Power | `2 ** 3` → `8` |
| `==` `!=` | Equal, Not equal | `5 == 5` → `True` |
| `<` `>` `<=` `>=` | Comparison | `3 < 5` → `True` |
| `and` `or` `not` | Logical | `True and False` → `False` |
| `is` | Identity | `a is b` |
| `in` | Membership | `3 in [1,2,3]` → `True` |

---

## 🎯 Exam Checklist

- [ ] Division (/) ALWAYS returns float
- [ ] Floor division (//) rounds toward negative infinity
- [ ] Exponentiation (**) is right-associative
- [ ] -2 ** 2 = -4 (not 4!)
- [ ] `is` checks identity, `==` checks equality
- [ ] `in` checks membership in sequences
- [ ] Logical operators return actual values, not just True/False
- [ ] Know the precedence order!
- [ ] Use parentheses when in doubt

---

[[03_Literals_Variables|← Literals]] | [[00_Index|Index]] | [[05_Data_Types|Data Types →]]
