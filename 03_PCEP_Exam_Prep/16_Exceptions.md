---
title: Exceptions (HEAVILY TESTED!)
tags: [pcep, python, exceptions, try, except, finally, raise]
created: 2026-01-30
exam_section: 4
exam_weight: 10%
---

# ⚠️ Exceptions - Error Handling

[[00_Index|← Back to Index]] | [[15_Builtin_Functions|← Built-in Functions]] | [[17_Recursion_Generators|Recursion →]]

> **"Know the common exceptions and how to handle them!"**

---

## ⚠️ EXAM ALERT: Exception handling is heavily tested!

---

## 🎯 What are Exceptions?

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXCEPTIONS                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Exceptions are RUNTIME ERRORS that disrupt normal flow.        │
│                                                                  │
│  Without handling:                                               │
│    x = 10 / 0  → ZeroDivisionError → PROGRAM CRASHES!          │
│                                                                  │
│  With handling:                                                  │
│    try:                                                          │
│        x = 10 / 0                                               │
│    except ZeroDivisionError:                                    │
│        print("Cannot divide by zero!")                          │
│        x = 0  ← Program continues!                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔴 Common Exceptions (MEMORIZE!)

```python
# ═══════════════════════════════════════════════════════════════
# EXCEPTIONS YOU MUST KNOW FOR PCEP
# ═══════════════════════════════════════════════════════════════

# ValueError - wrong value for the type
int("hello")      # ValueError: invalid literal for int()
int("3.14")       # ValueError: can't convert float string to int

# TypeError - wrong type for operation
"hello" + 5       # TypeError: can only concatenate str to str
len(42)           # TypeError: object of type 'int' has no len()

# ZeroDivisionError - division by zero
10 / 0            # ZeroDivisionError
10 // 0           # ZeroDivisionError
10 % 0            # ZeroDivisionError

# IndexError - sequence index out of range
lst = [1, 2, 3]
lst[10]           # IndexError: list index out of range
"hello"[10]       # IndexError: string index out of range

# KeyError - dictionary key not found
d = {"a": 1}
d["b"]            # KeyError: 'b'

# NameError - undefined variable
print(undefined)  # NameError: name 'undefined' is not defined

# AttributeError - object has no such attribute
"hello".append("x")  # AttributeError: 'str' has no attribute 'append'

# FileNotFoundError - file doesn't exist
open("nonexistent.txt")  # FileNotFoundError

# ImportError / ModuleNotFoundError
import nonexistent_module  # ModuleNotFoundError

# SyntaxError - invalid Python syntax (compile-time, not runtime!)
# eval("if")       # SyntaxError
```

---

## 🛡️ Exception Handling: try-except

```python
# ═══════════════════════════════════════════════════════════════
# BASIC TRY-EXCEPT
# ═══════════════════════════════════════════════════════════════

# Basic structure
try:
    x = 10 / 0  # Risky code
except ZeroDivisionError:
    print("Cannot divide by zero!")
    x = 0

print(x)  # 0 - program continues!

# Multiple except blocks
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions in one except
try:
    x = int("hello")
except (ValueError, TypeError):
    print("Invalid input!")

# Catch all exceptions (use sparingly!)
try:
    # risky code
    pass
except:  # Catches EVERYTHING (including KeyboardInterrupt!)
    print("Something went wrong")

# Better: catch Exception (base class for most exceptions)
try:
    pass
except Exception as e:
    print(f"Error: {e}")
```

---

## 📋 Exception Object: as keyword

```python
# ═══════════════════════════════════════════════════════════════
# ACCESSING EXCEPTION INFORMATION
# ═══════════════════════════════════════════════════════════════

try:
    x = int("hello")
except ValueError as e:
    print(f"Error occurred: {e}")
    print(f"Error type: {type(e).__name__}")
# Output:
# Error occurred: invalid literal for int() with base 10: 'hello'
# Error type: ValueError

try:
    d = {"a": 1}
    value = d["b"]
except KeyError as e:
    print(f"Key not found: {e}")
# Output: Key not found: 'b'
```

---

## 🔄 try-except-else-finally

```
┌─────────────────────────────────────────────────────────────────┐
│              TRY-EXCEPT-ELSE-FINALLY                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  try:                                                            │
│      # Code that might raise exception                          │
│  except SomeError:                                               │
│      # Runs if exception occurs                                 │
│  else:                                                           │
│      # Runs ONLY if NO exception occurred                       │
│  finally:                                                        │
│      # ALWAYS runs (cleanup code)                               │
│                                                                  │
│  EXECUTION ORDER:                                                │
│  1. try block executes                                          │
│  2. If exception → except runs                                  │
│     If no exception → else runs                                 │
│  3. finally ALWAYS runs last                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# COMPLETE EXCEPTION HANDLING
# ═══════════════════════════════════════════════════════════════

# else clause - runs only if no exception
try:
    x = int("42")
except ValueError:
    print("Invalid input!")
else:
    print(f"Success! x = {x}")  # This runs
# Output: Success! x = 42

# finally clause - always runs
try:
    f = open("test.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleanup code runs always")
    # f.close()  # Would close file if opened

# Full example
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Divide function complete")

print(divide(10, 2))
# Division successful!
# Divide function complete
# 5.0

print(divide(10, 0))
# Cannot divide by zero!
# Divide function complete
# None
```

---

## 🚀 Raising Exceptions

```python
# ═══════════════════════════════════════════════════════════════
# RAISE STATEMENT
# ═══════════════════════════════════════════════════════════════

# Raise an exception manually
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age < 18:
        raise ValueError("Must be 18 or older!")
    return "Access granted"

try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")
# Output: Error: Age cannot be negative!

# Re-raise the current exception
try:
    x = int("hello")
except ValueError:
    print("Logging error...")
    raise  # Re-raises the caught exception

# Raise with custom message
raise ValueError("Custom error message")

# Raise without instance (creates one)
raise ValueError  # Same as raise ValueError()
```

---

## 📊 Exception Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│              EXCEPTION HIERARCHY (Simplified)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  BaseException                                                   │
│  ├── SystemExit                                                 │
│  ├── KeyboardInterrupt                                          │
│  └── Exception  ← Most exceptions inherit from here            │
│      ├── ArithmeticError                                        │
│      │   ├── ZeroDivisionError                                  │
│      │   └── OverflowError                                      │
│      ├── LookupError                                            │
│      │   ├── IndexError                                         │
│      │   └── KeyError                                           │
│      ├── TypeError                                              │
│      ├── ValueError                                             │
│      ├── AttributeError                                         │
│      ├── NameError                                              │
│      ├── OSError                                                │
│      │   └── FileNotFoundError                                  │
│      └── ...                                                    │
│                                                                  │
│  Order matters! Catch specific exceptions BEFORE general ones  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

```python
# ═══════════════════════════════════════════════════════════════
# EXCEPTION HIERARCHY IN PRACTICE
# ═══════════════════════════════════════════════════════════════

# ❌ WRONG: General exception first catches all
try:
    x = int("hello")
except Exception:
    print("General exception")  # This catches it!
except ValueError:
    print("Value error")        # Never reached!

# ✅ RIGHT: Specific exceptions first
try:
    x = int("hello")
except ValueError:
    print("Value error")        # This catches it!
except Exception:
    print("General exception")  # Fallback for others

# Parent class catches child exceptions
try:
    lst = [1, 2, 3]
    print(lst[10])
except LookupError:  # Parent of IndexError and KeyError
    print("Lookup error!")  # Catches IndexError
```

---

## 🔧 Assertions (Debugging Tool)

```python
# ═══════════════════════════════════════════════════════════════
# ASSERT STATEMENT
# ═══════════════════════════════════════════════════════════════

# assert condition, message
# Raises AssertionError if condition is False

def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty!"
    return sum(numbers) / len(numbers)

print(calculate_average([1, 2, 3]))  # 2.0

# calculate_average([])  # AssertionError: List cannot be empty!

# Assert is for debugging, not for handling user input!
# Can be disabled with python -O (optimize mode)

# Use assert for:
# - Internal checks during development
# - Verifying assumptions in code
# - Testing

# Don't use assert for:
# - Validating user input
# - Production error handling
```

---

## ⚠️ Common Exam Traps

```python
# TRAP 1: Order of except clauses
try:
    x = int("hello")
except Exception:  # Too general - catches everything!
    print("Exception")
except ValueError:  # NEVER reached!
    print("ValueError")

# TRAP 2: Bare except catches too much
try:
    while True:
        pass
except:  # Catches KeyboardInterrupt too!
    print("Caught")

# TRAP 3: finally ALWAYS runs
def demo():
    try:
        return "try"
    finally:
        print("finally")  # Still runs!

result = demo()  # Prints "finally"
print(result)    # "try"

# TRAP 4: finally with return
def trap():
    try:
        return 1
    finally:
        return 2  # Overrides the try's return!

print(trap())  # 2

# TRAP 5: else only runs without exception
try:
    x = int("42")
except ValueError:
    print("Error!")
else:
    print("No error!")  # Runs because no exception

# TRAP 6: Raising inside except
try:
    int("hello")
except ValueError:
    raise TypeError("Converted to TypeError")
# Raises TypeError, not ValueError!
```

---

## 📝 Quick Reference

| Exception | Cause | Example |
|-----------|-------|---------|
| `ValueError` | Wrong value | `int("hello")` |
| `TypeError` | Wrong type | `"a" + 1` |
| `ZeroDivisionError` | Division by 0 | `10 / 0` |
| `IndexError` | Bad index | `[1,2,3][10]` |
| `KeyError` | Missing key | `{}["x"]` |
| `NameError` | Undefined var | `print(x)` |
| `AttributeError` | Missing attr | `"".append()` |
| `FileNotFoundError` | No file | `open("x.txt")` |

---

## 🎯 Exam Checklist

- [ ] try-except handles exceptions
- [ ] else runs only if NO exception
- [ ] finally ALWAYS runs (even with return!)
- [ ] Catch specific exceptions before general ones
- [ ] `raise` creates/throws exceptions
- [ ] `as` captures exception object
- [ ] Bare `except:` catches everything (avoid!)
- [ ] Know common exceptions (ValueError, TypeError, etc.)
- [ ] Exception hierarchy: child caught by parent
- [ ] assert for debugging, not user input validation

---

[[15_Builtin_Functions|← Built-in Functions]] | [[00_Index|Index]] | [[17_Recursion_Generators|Recursion →]]
