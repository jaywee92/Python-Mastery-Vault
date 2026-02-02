---
title: Built-in Functions
tags: [pcep, python, builtins, functions]
created: 2026-01-30
exam_section: 4
exam_weight: 8%
---

# 🔧 Built-in Functions

[[00_Index|← Back to Index]] | [[14_Functions_Advanced|← Functions Advanced]] | [[16_Exceptions|Exceptions →]]

> **"Know these functions - they appear throughout the exam!"**

---

## 📊 Type Conversion Functions

```python
# ═══════════════════════════════════════════════════════════════
# TYPE CONVERSION
# ═══════════════════════════════════════════════════════════════

# int() - convert to integer
print(int(3.7))       # 3 (truncates!)
print(int("42"))      # 42
print(int(True))      # 1
print(int("FF", 16))  # 255 (hex to int)

# float() - convert to float
print(float(42))      # 42.0
print(float("3.14"))  # 3.14
print(float("1e3"))   # 1000.0

# str() - convert to string
print(str(42))        # "42"
print(str(3.14))      # "3.14"
print(str([1,2,3]))   # "[1, 2, 3]"

# bool() - convert to boolean
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("hello"))  # True
print(bool([]))       # False
print(bool([0]))      # True (has element!)

# list(), tuple(), set(), dict()
print(list("abc"))           # ['a', 'b', 'c']
print(tuple([1, 2, 3]))      # (1, 2, 3)
print(set([1, 2, 2, 3]))     # {1, 2, 3}
print(dict([("a",1),("b",2)])) # {'a': 1, 'b': 2}
```

---

## 🔢 Math Functions

```python
# ═══════════════════════════════════════════════════════════════
# MATH FUNCTIONS
# ═══════════════════════════════════════════════════════════════

# abs() - absolute value
print(abs(-5))      # 5
print(abs(3.14))    # 3.14
print(abs(-3.14))   # 3.14

# pow() - power
print(pow(2, 3))        # 8 (same as 2**3)
print(pow(2, 3, 5))     # 3 (2**3 % 5)

# round() - round to n decimal places
print(round(3.7))       # 4
print(round(3.14159, 2))  # 3.14
print(round(2.5))       # 2 (banker's rounding!)
print(round(3.5))       # 4

# divmod() - returns (quotient, remainder)
print(divmod(17, 5))    # (3, 2)
q, r = divmod(17, 5)
print(q, r)             # 3 2

# min() and max()
print(min(3, 1, 4, 1, 5))   # 1
print(max(3, 1, 4, 1, 5))   # 5
print(min([3, 1, 4, 1, 5])) # 1
print(max("hello"))          # 'o' (by ASCII)

# min/max with key
words = ["apple", "pie", "banana"]
print(min(words, key=len))   # "pie"
print(max(words, key=len))   # "banana"

# sum()
print(sum([1, 2, 3, 4, 5]))  # 15
print(sum([1, 2, 3], 10))    # 16 (start=10)
```

---

## 📏 Sequence Functions

```python
# ═══════════════════════════════════════════════════════════════
# SEQUENCE FUNCTIONS
# ═══════════════════════════════════════════════════════════════

# len() - length
print(len("hello"))     # 5
print(len([1, 2, 3]))   # 3
print(len({"a": 1}))    # 1

# sorted() - returns NEW sorted list
print(sorted([3, 1, 4, 1, 5]))      # [1, 1, 3, 4, 5]
print(sorted("hello"))               # ['e', 'h', 'l', 'l', 'o']
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]

# reversed() - returns iterator
print(list(reversed([1, 2, 3])))    # [3, 2, 1]
print(list(reversed("hello")))       # ['o', 'l', 'l', 'e', 'h']

# enumerate() - index + value pairs
for i, v in enumerate(['a', 'b', 'c']):
    print(i, v)
# 0 a, 1 b, 2 c

for i, v in enumerate(['a', 'b'], start=1):
    print(i, v)
# 1 a, 2 b

# zip() - combine iterables
names = ["Alice", "Bob"]
ages = [25, 30]
print(list(zip(names, ages)))  # [('Alice', 25), ('Bob', 30)]

for name, age in zip(names, ages):
    print(f"{name}: {age}")

# range() - sequence of numbers
print(list(range(5)))       # [0, 1, 2, 3, 4]
print(list(range(1, 6)))    # [1, 2, 3, 4, 5]
print(list(range(0, 10, 2))) # [0, 2, 4, 6, 8]
```

---

## ✅ Boolean Functions

```python
# ═══════════════════════════════════════════════════════════════
# BOOLEAN FUNCTIONS
# ═══════════════════════════════════════════════════════════════

# all() - True if ALL elements are truthy
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False
print(all([1, 2, 3]))            # True
print(all([1, 0, 3]))            # False (0 is falsy)
print(all([]))                   # True (vacuous truth!)

# any() - True if ANY element is truthy
print(any([False, False, True])) # True
print(any([False, False, False])) # False
print(any([0, 0, 1]))            # True
print(any([]))                   # False
```

---

## 🔍 Type & Identity Functions

```python
# ═══════════════════════════════════════════════════════════════
# TYPE CHECKING
# ═══════════════════════════════════════════════════════════════

# type() - get type
print(type(42))         # <class 'int'>
print(type("hello"))    # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>

# isinstance() - check type (includes inheritance)
print(isinstance(42, int))       # True
print(isinstance(42, (int, float)))  # True
print(isinstance(True, int))     # True (bool is subclass of int!)

# id() - memory address
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(id(a) == id(b))  # True (same object)
print(id(a) == id(c))  # False (different objects)

# callable() - check if object can be called
print(callable(print))      # True
print(callable(len))        # True
print(callable(42))         # False
print(callable(lambda x: x)) # True
```

---

## 📥📤 I/O Functions

```python
# ═══════════════════════════════════════════════════════════════
# INPUT/OUTPUT
# ═══════════════════════════════════════════════════════════════

# print() - output
print("Hello")                    # Hello
print(1, 2, 3)                    # 1 2 3
print(1, 2, 3, sep="-")           # 1-2-3
print("Hello", end="")            # No newline

# input() - returns STRING always!
name = input("Name: ")            # Returns string
age = int(input("Age: "))         # Convert to int

# open() - file operations
f = open("file.txt", "r")
content = f.read()
f.close()

# Better: with statement
with open("file.txt", "r") as f:
    content = f.read()
```

---

## 🔧 Other Useful Built-ins

```python
# ═══════════════════════════════════════════════════════════════
# OTHER BUILT-INS
# ═══════════════════════════════════════════════════════════════

# map() - apply function to each element
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16]

# filter() - keep elements where function returns True
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]

# chr() and ord() - character/ASCII conversion
print(chr(65))    # 'A'
print(chr(97))    # 'a'
print(ord('A'))   # 65
print(ord('a'))   # 97

# bin(), hex(), oct() - number base conversion
print(bin(10))    # '0b1010'
print(hex(255))   # '0xff'
print(oct(8))     # '0o10'

# eval() - evaluate string as Python expression
print(eval("2 + 3"))     # 5
print(eval("[1, 2, 3]")) # [1, 2, 3]

# repr() - string representation
print(repr("hello"))     # "'hello'"
print(repr([1, 2, 3]))   # '[1, 2, 3]'

# help() - get documentation
# help(print)  # Shows documentation for print
```

---

## 📝 Quick Reference Table

| Function | Description | Example |
|----------|-------------|---------|
| `int(x)` | Convert to int | `int("42")` → `42` |
| `float(x)` | Convert to float | `float("3.14")` → `3.14` |
| `str(x)` | Convert to string | `str(42)` → `"42"` |
| `bool(x)` | Convert to bool | `bool(0)` → `False` |
| `list(x)` | Convert to list | `list("ab")` → `['a','b']` |
| `len(x)` | Get length | `len([1,2,3])` → `3` |
| `abs(x)` | Absolute value | `abs(-5)` → `5` |
| `round(x,n)` | Round | `round(3.14,1)` → `3.1` |
| `min(...)` | Minimum | `min(1,2,3)` → `1` |
| `max(...)` | Maximum | `max(1,2,3)` → `3` |
| `sum(iter)` | Sum | `sum([1,2,3])` → `6` |
| `sorted(iter)` | Sorted list | `sorted([3,1,2])` → `[1,2,3]` |
| `all(iter)` | All truthy? | `all([1,1,0])` → `False` |
| `any(iter)` | Any truthy? | `any([0,0,1])` → `True` |
| `type(x)` | Get type | `type(42)` → `<class 'int'>` |
| `range(n)` | Sequence | `range(3)` → `0,1,2` |
| `enumerate(iter)` | Index+value | `enumerate(['a'])` → `(0,'a')` |
| `zip(a,b)` | Combine | `zip([1],[2])` → `[(1,2)]` |

---

## 🎯 Exam Checklist

- [ ] int() truncates (doesn't round!)
- [ ] round(2.5) = 2 (banker's rounding)
- [ ] input() ALWAYS returns string
- [ ] sorted() returns NEW list
- [ ] all([]) = True, any([]) = False
- [ ] isinstance(True, int) = True
- [ ] range(5) gives 0,1,2,3,4
- [ ] enumerate() gives (index, value) pairs
- [ ] chr(65) = 'A', ord('A') = 65

---

[[14_Functions_Advanced|← Functions Advanced]] | [[00_Index|Index]] | [[16_Exceptions|Exceptions →]]
