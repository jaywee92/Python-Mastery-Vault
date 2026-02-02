---
title: Conditionals (if/elif/else)
tags: [pcep, python, conditionals, if, elif, else]
created: 2026-01-30
exam_section: 2
exam_weight: 10%
---

# 🔀 Conditionals

[[00_Index|← Back to Index]] | [[06_Input_Output|← I/O]] | [[08_Loops|Loops →]]

> **"Understand truthiness and the flow of if-elif-else!"**

---

## 🎯 The if Statement

```
┌─────────────────────────────────────────────────────────────────┐
│              IF STATEMENT STRUCTURE                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  if condition:        ← Colon required!                         │
│      statement(s)     ← Indentation required!                   │
│                                                                  │
│  Flow:                                                          │
│    1. Evaluate condition                                        │
│    2. If True → execute body                                    │
│    3. If False → skip body                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# BASIC IF STATEMENT
# ═══════════════════════════════════════════════════════════════

age = 18

if age >= 18:
    print("You are an adult")
    print("You can vote")

# The code after if block continues regardless
print("This always prints")

# Single line if (valid but not recommended for readability)
if age >= 18: print("Adult")
```

---

## 🔄 if-else Statement

```python
# ═══════════════════════════════════════════════════════════════
# IF-ELSE STATEMENT
# ═══════════════════════════════════════════════════════════════

age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Only ONE of these blocks executes!
# If condition is True → if block
# If condition is False → else block
```

---

## 📊 if-elif-else Chain

```python
# ═══════════════════════════════════════════════════════════════
# IF-ELIF-ELSE CHAIN
# ═══════════════════════════════════════════════════════════════

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")  # B

# IMPORTANT: Only ONE block executes!
# Python checks from top to bottom
# First True condition's block runs, then exits
# else runs only if ALL conditions are False
```

```
┌─────────────────────────────────────────────────────────────────┐
│              IF-ELIF-ELSE FLOW                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│          ┌──────────────┐                                       │
│          │ if condition │                                       │
│          └──────┬───────┘                                       │
│                 │                                               │
│         True    │    False                                      │
│    ┌────────────┴────────────┐                                  │
│    ▼                         ▼                                  │
│  ┌─────────┐          ┌──────────────┐                         │
│  │ if body │          │elif condition│                         │
│  └────┬────┘          └──────┬───────┘                         │
│       │                      │                                  │
│       │               True   │   False                          │
│       │          ┌───────────┴───────────┐                      │
│       │          ▼                       ▼                      │
│       │    ┌───────────┐          ┌───────────┐                │
│       │    │ elif body │          │ else body │                │
│       │    └─────┬─────┘          └─────┬─────┘                │
│       │          │                      │                       │
│       └──────────┴──────────────────────┘                       │
│                         │                                       │
│                         ▼                                       │
│                  [Continue...]                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔗 Nested Conditionals

```python
# ═══════════════════════════════════════════════════════════════
# NESTED IF STATEMENTS
# ═══════════════════════════════════════════════════════════════

age = 25
has_license = True

if age >= 18:
    print("Old enough to drive")
    if has_license:
        print("You can drive!")
    else:
        print("Get a license first")
else:
    print("Too young to drive")

# Can often simplify with 'and'
if age >= 18 and has_license:
    print("You can drive!")
```

---

## ✅ Truthiness in Conditions

```python
# ═══════════════════════════════════════════════════════════════
# TRUTHINESS
# ═══════════════════════════════════════════════════════════════

# Any value can be a condition (not just True/False)!

# FALSY values (evaluate to False):
if not 0:         print("0 is falsy")
if not 0.0:       print("0.0 is falsy")
if not "":        print("'' is falsy")
if not []:        print("[] is falsy")
if not {}:        print("{} is falsy")
if not None:      print("None is falsy")

# TRUTHY values (evaluate to True):
if 1:             print("1 is truthy")
if -1:            print("-1 is truthy")
if "hello":       print("'hello' is truthy")
if [1, 2]:        print("[1, 2] is truthy")
if {"a": 1}:      print("{'a': 1} is truthy")

# Common pattern: check if list is not empty
items = [1, 2, 3]
if items:  # Same as: if len(items) > 0:
    print("List has items")

# Check if string is not empty
name = input("Name: ")
if name:  # Same as: if name != "":
    print(f"Hello, {name}")
else:
    print("No name entered")
```

---

## 🔧 Conditional Expressions (Ternary)

```python
# ═══════════════════════════════════════════════════════════════
# CONDITIONAL EXPRESSION (TERNARY OPERATOR)
# ═══════════════════════════════════════════════════════════════

# Syntax: value_if_true if condition else value_if_false

age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult

# Same as:
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Can be used in expressions
x = 10
result = x * 2 if x > 5 else x + 2
print(result)  # 20

# Chained (not recommended for readability)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # B

# In function arguments
print("Even" if 10 % 2 == 0 else "Odd")  # Even
```

---

## 🔗 Combining Conditions

```python
# ═══════════════════════════════════════════════════════════════
# LOGICAL OPERATORS IN CONDITIONS
# ═══════════════════════════════════════════════════════════════

age = 25
income = 50000
has_job = True

# and - both must be True
if age >= 18 and has_job:
    print("Can apply for credit card")

# or - at least one must be True
if age < 18 or age > 65:
    print("Special discount!")

# not - inverts the condition
if not has_job:
    print("Looking for work")

# Combined
if (age >= 21 and income >= 30000) or has_job:
    print("Loan approved")

# Use parentheses for clarity!
# Without: age >= 21 and income >= 30000 or has_job
# With: (age >= 21 and income >= 30000) or has_job
```

---

## 🔍 Comparison Chaining

```python
# ═══════════════════════════════════════════════════════════════
# CHAINED COMPARISONS (Python special!)
# ═══════════════════════════════════════════════════════════════

x = 5

# Instead of:
if x > 0 and x < 10:
    print("x is between 0 and 10")

# Python allows:
if 0 < x < 10:
    print("x is between 0 and 10")

# More examples
if 1 <= x <= 10:       # Inclusive range
    print("In range")

if 0 < x < y < 100:    # Multiple chained
    print("Ordered")

# This is equivalent to:
# 0 < x and x < y and y < 100
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: Assignment vs comparison
x = 5
# if x = 10:    # SyntaxError! Use ==
if x == 10:
    print("x is 10")

# TRAP 2: Forgetting colon
# if x > 5      # SyntaxError!
if x > 5:
    print("ok")

# TRAP 3: Indentation
if x > 5:
print("Missing indent!")  # IndentationError!

# TRAP 4: Empty body
# if x > 5:     # SyntaxError! Can't have empty body
#     # Nothing here
if x > 5:
    pass       # Use pass for empty body

# TRAP 5: Only first True condition runs
x = 100
if x > 50:
    print("A")    # Only this prints!
elif x > 80:
    print("B")    # Never reached!
elif x > 90:
    print("C")    # Never reached!

# TRAP 6: Truthiness surprises
if "False":      # True! Non-empty string
    print("Surprise!")

if [0]:          # True! Non-empty list
    print("Surprise!")

if 0.0:          # False! Zero value
    print("Won't print")

# TRAP 7: Comparison with None
x = None
if x == None:    # Works but not preferred
    pass
if x is None:    # Correct way!
    pass

# TRAP 8: and/or return values
x = 5 and 10     # x = 10 (not True!)
y = 0 or 20      # y = 20 (not True!)
```

---

## 📝 Quick Reference

| Pattern | Description |
|---------|-------------|
| `if cond:` | Execute if True |
| `if cond: else:` | Either/or |
| `if: elif: else:` | Multiple conditions |
| `x if cond else y` | Ternary expression |
| `a < x < b` | Chained comparison |
| `if items:` | Check if non-empty |
| `pass` | Placeholder for empty body |

---

## 🎯 Exam Checklist

- [ ] Colon (:) required after condition
- [ ] Body must be indented
- [ ] Only one block executes in if-elif-else
- [ ] elif/else are optional
- [ ] Know falsy values: 0, 0.0, "", [], {}, None
- [ ] Non-empty containers are truthy
- [ ] Ternary: value_if_true if condition else value_if_false
- [ ] Chained comparisons: 0 < x < 10
- [ ] Use `is` for None, `==` for values

---

[[06_Input_Output|← I/O]] | [[00_Index|Index]] | [[08_Loops|Loops →]]
