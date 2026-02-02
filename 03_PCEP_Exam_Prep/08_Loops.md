---
title: Loops (for & while)
tags: [pcep, python, loops, for, while, break, continue]
created: 2026-01-30
exam_section: 2
exam_weight: 12%
---

# 🔁 Loops

[[00_Index|← Back to Index]] | [[07_Conditionals|← Conditionals]] | [[09_Strings|Strings →]]

> **"Master loops and range() - they appear everywhere!"**

---

## ⚠️ EXAM ALERT: Loops are heavily tested!

---

## 🔄 The while Loop

```
┌─────────────────────────────────────────────────────────────────┐
│              WHILE LOOP                                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  while condition:                                               │
│      statement(s)                                               │
│                                                                  │
│  Flow:                                                          │
│    1. Check condition                                           │
│    2. If True → execute body → go to step 1                    │
│    3. If False → exit loop                                     │
│                                                                  │
│  DANGER: Infinite loop if condition never becomes False!        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# WHILE LOOP EXAMPLES
# ═══════════════════════════════════════════════════════════════

# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1  # Don't forget to update!
# Output: 0 1 2 3 4

# While with user input
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")

# Count down
n = 5
while n > 0:
    print(n)
    n -= 1
print("Blast off!")
# Output: 5 4 3 2 1 Blast off!

# While True (controlled infinite loop)
while True:
    command = input("Enter command (q to quit): ")
    if command == "q":
        break  # Exit the loop
    print(f"Processing: {command}")
```

---

## 🔢 The for Loop

```
┌─────────────────────────────────────────────────────────────────┐
│              FOR LOOP                                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  for variable in iterable:                                      │
│      statement(s)                                               │
│                                                                  │
│  Iterables: list, tuple, string, range, dict, set, file...     │
│                                                                  │
│  For each item in iterable:                                     │
│    1. Assign item to variable                                   │
│    2. Execute body                                              │
│    3. Move to next item                                         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# FOR LOOP WITH SEQUENCES
# ═══════════════════════════════════════════════════════════════

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: apple banana cherry

# Iterate over a string
for char in "Hello":
    print(char)
# Output: H e l l o

# Iterate over a tuple
for num in (1, 2, 3):
    print(num)

# Iterate over a dictionary (keys by default)
person = {"name": "Alice", "age": 25}
for key in person:
    print(key, person[key])
# name Alice
# age 25

# Iterate over dict values
for value in person.values():
    print(value)

# Iterate over dict items (key-value pairs)
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 🔢 The range() Function (CRITICAL!)

```
┌─────────────────────────────────────────────────────────────────┐
│              range() FUNCTION                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  range(stop)           → 0, 1, 2, ..., stop-1                  │
│  range(start, stop)    → start, start+1, ..., stop-1           │
│  range(start, stop, step) → start, start+step, ..., <stop      │
│                                                                  │
│  IMPORTANT: stop is EXCLUSIVE!                                  │
│                                                                  │
│  range(5)      → 0, 1, 2, 3, 4                                 │
│  range(1, 5)   → 1, 2, 3, 4                                    │
│  range(0, 10, 2) → 0, 2, 4, 6, 8                               │
│  range(5, 0, -1) → 5, 4, 3, 2, 1                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# RANGE EXAMPLES
# ═══════════════════════════════════════════════════════════════

# range(stop) - from 0 to stop-1
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# range(start, stop) - from start to stop-1
for i in range(1, 6):
    print(i)
# Output: 1 2 3 4 5

# range(start, stop, step) - with step
for i in range(0, 10, 2):
    print(i)
# Output: 0 2 4 6 8

# Negative step (counting down)
for i in range(5, 0, -1):
    print(i)
# Output: 5 4 3 2 1

# range() returns a range object, not a list
r = range(5)
print(r)         # range(0, 5)
print(list(r))   # [0, 1, 2, 3, 4]

# Common patterns
# Index-based iteration
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Better: use enumerate
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

---

## 🛑 break and continue

```python
# ═══════════════════════════════════════════════════════════════
# BREAK - Exit the loop immediately
# ═══════════════════════════════════════════════════════════════

for i in range(10):
    if i == 5:
        break  # Exit loop when i is 5
    print(i)
# Output: 0 1 2 3 4

# Find first even number
numbers = [1, 3, 5, 4, 7, 8]
for num in numbers:
    if num % 2 == 0:
        print(f"First even: {num}")
        break
# Output: First even: 4

# ═══════════════════════════════════════════════════════════════
# CONTINUE - Skip to next iteration
# ═══════════════════════════════════════════════════════════════

for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)
# Output: 0 1 3 4

# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1 3 5 7 9
```

---

## 🔄 else Clause in Loops

```python
# ═══════════════════════════════════════════════════════════════
# LOOP ELSE CLAUSE
# ═══════════════════════════════════════════════════════════════

# else runs when loop completes normally (no break)

# For loop with else
for i in range(5):
    print(i)
else:
    print("Loop completed!")  # This runs
# Output: 0 1 2 3 4 Loop completed!

# Break prevents else from running
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed!")  # This does NOT run
# Output: 0 1 2

# While loop with else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Done!")  # This runs
# Output: 0 1 2 Done!

# Common pattern: Search with else
def find_item(items, target):
    for item in items:
        if item == target:
            print("Found!")
            break
    else:
        print("Not found!")  # Only if loop didn't break

find_item([1, 2, 3, 4], 3)  # Found!
find_item([1, 2, 3, 4], 5)  # Not found!
```

---

## 🔢 Nested Loops

```python
# ═══════════════════════════════════════════════════════════════
# NESTED LOOPS
# ═══════════════════════════════════════════════════════════════

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end=" ")
    print()  # Newline after each row
# Output:
# 1x1=1 1x2=2 1x3=3
# 2x1=2 2x2=4 2x3=6
# 3x1=3 3x2=6 3x3=9

# Matrix iteration
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# Break in nested loop (breaks inner loop only!)
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only breaks inner loop
        print(f"({i},{j})")
# Output: (0,0) (1,0) (2,0)
```

---

## 🔧 Common Loop Patterns

```python
# ═══════════════════════════════════════════════════════════════
# USEFUL PATTERNS
# ═══════════════════════════════════════════════════════════════

# Accumulator pattern
total = 0
for i in range(1, 6):
    total += i
print(total)  # 15 (1+2+3+4+5)

# Counter pattern
count = 0
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if num % 2 == 0:
        count += 1
print(f"Even count: {count}")  # 5

# Max/Min finding
numbers = [4, 2, 8, 1, 9, 3]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)  # 9

# List building
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# Better: List comprehension
squares = [i ** 2 for i in range(5)]
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: range() stop is EXCLUSIVE
for i in range(5):
    print(i)  # Prints 0,1,2,3,4 (not 5!)

# TRAP 2: Modifying list while iterating
nums = [1, 2, 3, 4, 5]
# ❌ WRONG:
# for num in nums:
#     if num % 2 == 0:
#         nums.remove(num)  # Skips elements!

# ✅ RIGHT: Iterate over copy
for num in nums[:]:
    if num % 2 == 0:
        nums.remove(num)

# TRAP 3: break only exits innermost loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break  # Only breaks inner!
        print(i, j)

# TRAP 4: else runs when NO break occurs
for i in range(5):
    pass
else:
    print("Runs!")  # This executes!

for i in range(5):
    break
else:
    print("Doesn't run!")  # This doesn't execute!

# TRAP 5: range with negative step needs proper bounds
list(range(5, 0, -1))   # [5, 4, 3, 2, 1]
list(range(5, 0, 1))    # [] (empty! can't count up from 5 to 0)
list(range(0, 5, -1))   # [] (empty! can't count down from 0 to 5)

# TRAP 6: Variable scope
for i in range(5):
    x = i
print(x)  # 4 - variable exists after loop!

# TRAP 7: Empty loop body
# for i in range(5):  # SyntaxError!
for i in range(5):
    pass  # Use pass for empty body
```

---

## 📝 Quick Reference

| Pattern | Description | Example |
|---------|-------------|---------|
| `while cond:` | Loop while True | `while x < 10:` |
| `for x in seq:` | Loop over sequence | `for i in [1,2,3]:` |
| `range(n)` | 0 to n-1 | `range(5)` → 0,1,2,3,4 |
| `range(a,b)` | a to b-1 | `range(1,5)` → 1,2,3,4 |
| `range(a,b,s)` | a to b-1 by s | `range(0,10,2)` → 0,2,4,6,8 |
| `break` | Exit loop | Exits immediately |
| `continue` | Skip iteration | Goes to next iteration |
| `else:` | After loop | Runs if no break |

---

## 🎯 Exam Checklist

- [ ] range(stop) goes from 0 to stop-1
- [ ] range(start, stop) excludes stop
- [ ] range(start, stop, step) with negative step counts down
- [ ] break exits loop, else doesn't run
- [ ] continue skips to next iteration
- [ ] else clause runs when loop completes normally
- [ ] break only exits innermost loop
- [ ] Don't modify list while iterating
- [ ] Variable from loop exists after loop ends

---

[[07_Conditionals|← Conditionals]] | [[00_Index|Index]] | [[09_Strings|Strings →]]
