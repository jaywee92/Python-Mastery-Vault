---
title: Debugging
tags: [python, debugging, pdb, breakpoint, tools, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# 🔍 Debugging

[[00_Index|← Back to Index]] | [[18_Exceptions|← Exceptions]] | [[20_Logging|Logging →]]

> **"Debugging is like being a detective - find the bug before it finds you!"**

---

## 🎯 Why Debugging is Important

Debugging is the art of finding and fixing errors in code. Being a good debugger is one of the most valuable skills for any developer.

```
🔍 DEBUGGING WORKFLOW
====================

   Bug discovered
        ↓
  ┌─────────────────┐
  │ 1. Reproduce    │ ← When does the error occur?
  └────────┬────────┘
           ↓
  ┌─────────────────┐
  │ 2. Isolate      │ ← Where exactly is the problem?
  └────────┬────────┘
           ↓
  ┌─────────────────┐
  │ 3. Analyze      │ ← Why does it happen?
  └────────┬────────┘
           ↓
  ┌─────────────────┐
  │ 4. Fix          │ ← Implement the fix
  └────────┬────────┘
           ↓
  ┌─────────────────┐
  │ 5. Verify       │ ← Is the bug really gone?
  └─────────────────┘
```

---

## 🖨️ Print Debugging

The simplest, but often effective method:

```python
# Simple print debugging
def calculate_average(numbers):
    print(f"DEBUG: Input = {numbers}")           # What comes in?

    total = sum(numbers)
    print(f"DEBUG: Sum = {total}")               # Intermediate result

    count = len(numbers)
    print(f"DEBUG: Count = {count}")

    result = total / count
    print(f"DEBUG: Result = {result}")           # What comes out?

    return result

# Better variant: Function to track variables
def debug_print(var_name, var_value, line=None):
    """Formatted debug output."""
    prefix = f"[Line {line}]" if line else "[DEBUG]"
    print(f"{prefix} {var_name} = {var_value!r} (Type: {type(var_value).__name__})")

# Usage
x = [1, 2, 3]
debug_print("x", x)  # [DEBUG] x = [1, 2, 3] (Type: list)
```

### F-String Debugging (Python 3.8+)

```python
# The = sign shows variable and value
name = "Alice"
age = 30
numbers = [1, 2, 3]

print(f"{name=}")           # name='Alice'
print(f"{age=}")            # age=30
print(f"{len(numbers)=}")   # len(numbers)=3
print(f"{numbers[0]=}")     # numbers[0]=1

# With formatting
pi = 3.14159265
print(f"{pi=:.2f}")         # pi=3.14

# Complex expressions
print(f"{2 + 2 = }")        # 2 + 2 = 4
```

---

## 🐛 Python Debugger (pdb)

The built-in debugger for interactive debugging:

### Setting Breakpoints

```python
# Method 1: breakpoint() (Python 3.7+) - RECOMMENDED
def problematic_function(x):
    result = x * 2
    breakpoint()            # Execution stops here
    result += 10
    return result

# Method 2: pdb.set_trace() (older Python versions)
import pdb

def old_style(x):
    result = x * 2
    pdb.set_trace()         # Breakpoint
    return result

# Method 3: Start from command line
# python -m pdb script.py
```

### PDB Commands

```
┌──────────────────────────────────────────────────────────────────┐
│                     PDB COMMANDS OVERVIEW                        │
├──────────┬──────────────────────────────────────────────────────┤
│ NAVIGATION                                                       │
├──────────┼──────────────────────────────────────────────────────┤
│ n        │ Next - next line (skips functions)                   │
│ s        │ Step - next line (goes INTO functions)               │
│ c        │ Continue - until next breakpoint                     │
│ r        │ Return - until return from current function          │
│ unt [N]  │ Until - until line N                                 │
├──────────┼──────────────────────────────────────────────────────┤
│ INSPECTION                                                       │
├──────────┼──────────────────────────────────────────────────────┤
│ p expr   │ Print - evaluate and print expression                │
│ pp expr  │ Pretty-print - formatted output                      │
│ l        │ List - show surrounding code                         │
│ ll       │ Long list - show whole function                      │
│ w        │ Where - show call stack (stack trace)                │
│ u        │ Up - move one frame up in stack                      │
│ d        │ Down - move one frame down in stack                  │
├──────────┼──────────────────────────────────────────────────────┤
│ BREAKPOINTS                                                      │
├──────────┼──────────────────────────────────────────────────────┤
│ b N      │ Set breakpoint on line N                             │
│ b func   │ Set breakpoint in function                           │
│ cl N     │ Clear - delete breakpoint N                          │
│ disable N│ Disable breakpoint                                   │
│ enable N │ Enable breakpoint                                    │
├──────────┼──────────────────────────────────────────────────────┤
│ OTHER                                                            │
├──────────┼──────────────────────────────────────────────────────┤
│ q        │ Quit - exit debugger                                 │
│ h        │ Help - show help                                     │
│ !stmt    │ Execute Python statement                             │
└──────────┴──────────────────────────────────────────────────────┘
```

### Practical PDB Example

```python
def find_bug(data):
    """Function with hidden bug."""
    results = []

    for item in data:
        breakpoint()        # We can inspect here

        # In pdb we can enter:
        # p item            → show current item
        # p type(item)      → check type
        # p results         → show results so far
        # n                 → go to next line

        if item > 0:
            results.append(item * 2)

    return results

# Example session:
# > find_bug([1, -2, 3])
# -> breakpoint()
# (Pdb) p item
# 1
# (Pdb) n
# (Pdb) p results
# [2]
# (Pdb) c          # Continue to next iteration
```

---

## ✅ Assertions

Assertions are conditions that are checked during development:

```python
def calculate_discount(price, discount_percent):
    """Calculates discounted price."""
    # Check preconditions
    assert price >= 0, f"Price must be positive, was: {price}"
    assert 0 <= discount_percent <= 100, "Discount must be between 0 and 100"

    result = price * (1 - discount_percent / 100)

    # Check postcondition
    assert result >= 0, "Result cannot be negative"
    assert result <= price, "Discounted price cannot be higher"

    return result

# Usage
print(calculate_discount(100, 20))  # 80.0
print(calculate_discount(-50, 10))  # AssertionError: Price must be positive
```

### Important with Assertions

```python
# ⚠️ WARNING: Assertions can be disabled!
# python -O script.py  (optimization mode)

# ❌ WRONG: Assertions for user input
def process_user_input(value):
    assert value.isdigit()  # DANGEROUS! Ignored in production!
    return int(value)

# ✅ CORRECT: Exceptions for user input
def process_user_input(value):
    if not value.isdigit():
        raise ValueError("Input must be a number")
    return int(value)

# ✅ CORRECT: Assertions for internal invariants
def _internal_calculation(data):
    # Only for developers, not for users
    assert isinstance(data, list), "Internal error: data must be list"
    # ...
```

---

## 🔧 IDE Debugging

Modern IDEs offer powerful debugging tools:

```
┌─────────────────────────────────────────────────────────────────┐
│                    IDE DEBUGGING FEATURES                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ● Breakpoints          - Click on line number                  │
│  ● Conditional BP       - Stops only if condition met           │
│  ● Watch Variables      - Monitor variables                     │
│  ● Call Stack           - Show call hierarchy                   │
│  ● Step Over/Into/Out   - Navigation in code                    │
│  ● Evaluate Expression  - Execute code while paused             │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  VS Code Shortcuts:                                              │
│  F5        - Start debugging                                     │
│  F9        - Set/remove breakpoint                               │
│  F10       - Step Over                                           │
│  F11       - Step Into                                           │
│  Shift+F11 - Step Out                                            │
│  Shift+F5  - Stop debugging                                      │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  PyCharm Shortcuts:                                              │
│  Shift+F9  - Start debug                                         │
│  Ctrl+F8   - Set breakpoint                                      │
│  F8        - Step Over                                           │
│  F7        - Step Into                                           │
│  Shift+F8  - Step Out                                            │
└─────────────────────────────────────────────────────────────────┘
```

### Conditional Breakpoints

```python
# Stops only if condition is met
def process_items(items):
    for i, item in enumerate(items):
        # Breakpoint with condition: i == 50
        # or: item > 100
        result = transform(item)
        save(result)

# In VS Code: Right-click on breakpoint → "Edit Breakpoint"
# In PyCharm: Right-click on breakpoint → "Condition"
```

---

## 🔬 Reading Tracebacks

Interpret error tracebacks correctly:

```python
def outer():
    inner()

def inner():
    buggy()

def buggy():
    return 1 / 0

outer()
```

```
Traceback (most recent call last):     ← READ FROM BOTTOM TO TOP!
  File "script.py", line 11, in <module>
    outer()                            ← 3. Call: outer()
  File "script.py", line 2, in outer
    inner()                            ← 2. Call: inner()
  File "script.py", line 5, in inner
    buggy()                            ← 1. Call: buggy()
  File "script.py", line 8, in buggy
    return 1 / 0                       ← THE ERROR IS HERE!
ZeroDivisionError: division by zero    ← Error type and message
```

```
┌─────────────────────────────────────────────────────────────────┐
│                   TRACEBACK ANATOMY                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. "Traceback (most recent call last):"                        │
│     → Most recent call is at the BOTTOM                         │
│                                                                  │
│  2. Each frame shows:                                           │
│     - File name and line number                                 │
│     - Function name                                             │
│     - The code line itself                                      │
│                                                                  │
│  3. Last line = Error type: Error message                       │
│                                                                  │
│  TIP: Start with LAST frame (bottom) and work your way up!      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Debugging Techniques Comparison

| Technique | When to use | Advantages | Disadvantages |
|---------|----------------|----------|-----------|
| `print()` | Quick checks | Simple, no tools | Must be removed |
| `f"{x=}"` | Python 3.8+ | Compact, shows name | Only for simple values |
| `breakpoint()` | Complex bugs | Interactive, powerful | Learning curve for pdb |
| IDE Debugger | Large projects | Visual, features | IDE-dependent |
| `assert` | Invariants | Self-documenting | Can be disabled |
| `logging` | Production | Persistent, levels | Setup required |

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Forgot to remove print
def calculate(x):
    print(f"DEBUG: {x}")  # Forgotten!
    return x * 2

# ✅ CORRECT: Use logging
import logging
logger = logging.getLogger(__name__)

def calculate(x):
    logger.debug(f"Input: {x}")  # Can be controlled by level
    return x * 2

# ❌ WRONG: Assert for validation
def transfer_money(amount):
    assert amount > 0  # Ignored in production!
    # ...

# ✅ CORRECT: Exception for validation
def transfer_money(amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    # ...

# ❌ WRONG: Too many breakpoints
def complex_function():
    breakpoint()
    step1()
    breakpoint()
    step2()
    breakpoint()  # Debugging becomes tedious!

# ✅ CORRECT: Set deliberately
def complex_function():
    step1()
    breakpoint()  # Only where really needed
    step2()
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| `breakpoint()` for interactive debugging | `pdb.set_trace()` in new code |
| f-Strings with `=` for quick checks | Complex print formatting |
| Assertions for internal invariants | Assertions for user input |
| IDE-Debugger for complex projects | Only print-debugging for large bugs |
| Logging for production code | print() in production |
| Read traceback from bottom up | Stare panicked at first line |

---

## 🛠️ Debugging Checklist

When you're searching for a bug:

1. **Reproduce**: Can you reliably trigger the error?
2. **Narrow down**: Which function/line causes the error?
3. **Hypothesis**: What do you think is going wrong?
4. **Test**: Verify your hypothesis with pdb/prints
5. **Fix**: Fix the problem
6. **Verify**: Is the bug really gone? No side effects?

---

## 🎯 Exam Checklist

- [ ] `breakpoint()` and pdb commands (n, s, c, p, l)
- [ ] f-String debugging with `{var=}`
- [ ] Assertions and their limits
- [ ] Read traceback from bottom to top
- [ ] Difference between `n` (next) and `s` (step) in pdb
- [ ] When to use print vs pdb vs IDE-Debugger

---

[[18_Exceptions|← Exceptions]] | [[00_Index|Index]] | [[20_Logging|Logging →]]
