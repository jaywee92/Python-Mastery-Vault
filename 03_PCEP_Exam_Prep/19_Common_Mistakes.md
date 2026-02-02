---
title: Common Mistakes & Traps
tags: [pcep, python, mistakes, traps, gotchas]
created: 2026-01-30
---

# ⚠️ Common Mistakes & Exam Traps

[[00_Index|← Back to Index]] | [[18_Quick_Reference|← Quick Reference]] | [[20_Practice_Questions|Practice →]]

> **"Avoid these mistakes - they're designed to trick you!"**

---

## 🔢 Number Traps

```python
# ❌ TRAP: Division ALWAYS returns float
print(10 / 2)      # 5.0 (not 5!)
print(10 / 5)      # 2.0 (not 2!)

# ❌ TRAP: Floor division rounds toward NEGATIVE infinity
print(7 // 2)      # 3
print(-7 // 2)     # -4 (not -3!)

# ❌ TRAP: int() TRUNCATES, doesn't round
print(int(3.9))    # 3 (not 4!)
print(int(-3.9))   # -3 (not -4!)

# ❌ TRAP: Exponentiation before negation
print(-2 ** 2)     # -4 (not 4!)
print((-2) ** 2)   # 4

# ❌ TRAP: Exponentiation is right-associative
print(2 ** 3 ** 2) # 512 (= 2^9, not 8^2)

# ❌ TRAP: round() uses banker's rounding
print(round(2.5))  # 2 (not 3!)
print(round(3.5))  # 4

# ❌ TRAP: Float precision
print(0.1 + 0.2)   # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False!
```

---

## 📝 String Traps

```python
# ❌ TRAP: Strings are IMMUTABLE
s = "hello"
# s[0] = "H"       # TypeError!
s = "Hello"        # Creates NEW string (OK)

# ❌ TRAP: find() vs index()
s = "hello"
print(s.find("x"))  # -1 (not found)
# print(s.index("x"))  # ValueError!

# ❌ TRAP: split() with no argument
print("a  b  c".split())   # ['a', 'b', 'c'] (any whitespace)
print("a  b  c".split(" ")) # ['a', '', 'b', '', 'c'] (single space)

# ❌ TRAP: Empty string is falsy, but "0" and "False" are truthy
print(bool(""))        # False
print(bool("0"))       # True!
print(bool("False"))   # True!

# ❌ TRAP: Escape sequences
print("Hello\nWorld")   # Two lines
print(r"Hello\nWorld")  # One line: Hello\nWorld
```

---

## 📋 List Traps

```python
# ❌ TRAP: Assignment creates reference, not copy
a = [1, 2, 3]
b = a              # Same object!
b[0] = 100
print(a)           # [100, 2, 3] - BOTH changed!

# ✅ FIX: Use slicing or copy()
b = a[:]           # or a.copy()

# ❌ TRAP: append() vs extend()
a = [1, 2]
a.append([3, 4])   # Adds list as ONE element
print(a)           # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])   # Adds each element
print(b)           # [1, 2, 3, 4]

# ❌ TRAP: sort() returns None!
nums = [3, 1, 2]
result = nums.sort()
print(result)      # None!
print(nums)        # [1, 2, 3]

# ❌ TRAP: Modifying list while iterating
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num % 2 == 0:
        nums.remove(num)  # Skips elements!
print(nums)        # [1, 3, 5] - missed 4!

# ✅ FIX: Iterate over copy
for num in nums[:]:
    if num % 2 == 0:
        nums.remove(num)

# ❌ TRAP: List multiplication with nested lists
row = [[0] * 3] * 3
row[0][0] = 1
print(row)         # [[1,0,0], [1,0,0], [1,0,0]] - ALL changed!

# ✅ FIX: Use comprehension
row = [[0] * 3 for _ in range(3)]
```

---

## 🔢 Tuple Traps

```python
# ❌ TRAP: Single element tuple NEEDS comma
single = (42,)     # This is a tuple
not_tuple = (42)   # This is just an int!
print(type(single))     # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>

# ❌ TRAP: Unpacking must match count
t = (1, 2, 3)
# a, b = t         # ValueError!
a, b, c = t        # OK

# ❌ TRAP: sorted() returns list, not tuple
t = (3, 1, 2)
result = sorted(t)
print(type(result))  # <class 'list'>
```

---

## 📖 Dictionary Traps

```python
# ❌ TRAP: 'in' checks KEYS, not values
d = {"name": "Alice", "age": 25}
print("name" in d)   # True (key exists)
print("Alice" in d)  # False! (value, not key)

# ✅ To check value:
print("Alice" in d.values())  # True

# ❌ TRAP: [] raises KeyError for missing key
d = {"a": 1}
# print(d["b"])      # KeyError!
print(d.get("b"))    # None (safe)
print(d.get("b", 0)) # 0 (default)

# ❌ TRAP: {} creates empty dict, not empty set
empty = {}
print(type(empty))  # <class 'dict'>
# For empty set:
empty_set = set()

# ❌ TRAP: Modifying dict while iterating
d = {"a": 1, "b": 2, "c": 3}
# for key in d:
#     del d[key]    # RuntimeError!

# ✅ FIX: Iterate over copy
for key in list(d.keys()):
    del d[key]
```

---

## 🔧 Function Traps

```python
# ❌ TRAP: Mutable default argument
def add_item(item, lst=[]):  # DANGER!
    lst.append(item)
    return lst

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b'] - Surprise!

# ✅ FIX: Use None as default
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# ❌ TRAP: print() vs return
def add(a, b):
    print(a + b)     # Just displays!

result = add(2, 3)   # Prints 5
print(result)        # None!

# ❌ TRAP: Forgetting parentheses
def greet():
    return "Hello"

print(greet)         # <function greet at 0x...>
print(greet())       # Hello

# ❌ TRAP: Modifying global without 'global'
x = 10
def modify():
    x = 20          # Creates LOCAL x!
modify()
print(x)            # Still 10!
```

---

## 🔄 Loop Traps

```python
# ❌ TRAP: range() stop is EXCLUSIVE
for i in range(5):
    print(i)        # 0, 1, 2, 3, 4 (not 5!)

# ❌ TRAP: range with wrong step direction
print(list(range(5, 0, 1)))   # [] (empty!)
print(list(range(0, 5, -1)))  # [] (empty!)

# ❌ TRAP: break only exits innermost loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break   # Only breaks inner loop!
        print(i, j)

# ❌ TRAP: else runs when NO break occurs
for i in range(5):
    pass
else:
    print("Runs!")  # This executes!

for i in range(5):
    break
else:
    print("Doesn't run!")  # NOT executed

# ❌ TRAP: Loop variable persists after loop
for i in range(5):
    pass
print(i)            # 4 (still accessible!)
```

---

## ⚠️ Exception Traps

```python
# ❌ TRAP: General exception catches everything
try:
    x = int("hello")
except Exception:   # Catches it!
    print("Error")
except ValueError:  # Never reached!
    print("Value Error")

# ✅ FIX: Specific exceptions first
try:
    x = int("hello")
except ValueError:
    print("Value Error")
except Exception:
    print("Other Error")

# ❌ TRAP: finally ALWAYS runs
def demo():
    try:
        return "try"
    finally:
        print("finally")  # Still runs!

result = demo()     # Prints "finally"
print(result)       # "try"

# ❌ TRAP: finally with return overrides
def trap():
    try:
        return 1
    finally:
        return 2    # Overrides!

print(trap())       # 2
```

---

## 🔍 Comparison Traps

```python
# ❌ TRAP: is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)       # True (same value)
print(a is b)       # False (different objects!)

# ❌ TRAP: Chained comparison
x = 5
print(1 < x < 10)   # True (1 < 5 AND 5 < 10)

# ❌ TRAP: Boolean operators return values
print(5 and 3)      # 3 (not True!)
print(0 or 5)       # 5 (not True!)
print(0 and 5)      # 0 (not False!)
```

---

## 📥 Input/Output Traps

```python
# ❌ TRAP: input() ALWAYS returns string
x = input("Enter: ")  # User types: 5
print(x + 10)         # TypeError! "5" + 10

# ✅ FIX:
x = int(input("Enter: "))

# ❌ TRAP: print() returns None
result = print("Hello")
print(result)         # None
```

---

[[18_Quick_Reference|← Quick Reference]] | [[00_Index|Index]] | [[20_Practice_Questions|Practice →]]
