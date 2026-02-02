---
title: Exceptions
tags: [python, exceptions, errors, try-except, raise, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: beginner-intermediate
---

# ⚠️ Exceptions (Error Handling)

[[00_Index|← Back to Index]] | [[17_Path_Operations|← Paths]] | [[19_Debugging|Debugging →]]

> **Handle errors elegantly with try/except**

---

## 🎯 What are Exceptions?

**Exceptions** are errors that occur during program execution. Python "raises" an Exception when something goes wrong.

```python
# Different exception types
print(10 / 0)          # ZeroDivisionError
print(int("abc"))      # ValueError
print(my_list[100])    # IndexError
print(my_dict["key"])  # KeyError
print(undefined_var)   # NameError
print("hello".foo())   # AttributeError
```

Without handling, the program crashes. With `try/except` we can catch errors.

---

## 📦 Basic Syntax: try/except

```python
# Simple try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero not allowed!")
    result = 0

print(f"Result: {result}")  # Program continues
```

### Using Exception Object

```python
try:
    value = int("not a number")
except ValueError as e:
    print(f"Error occurred: {e}")
    # Output: Error occurred: invalid literal for int() with base 10: 'not a number'
```

---

## 🔀 Handling Multiple Exceptions

### Separate except Blocks

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Invalid types for division!")
        return None

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # None (ZeroDivisionError)
print(safe_divide("10", 2))  # None (TypeError)
```

### Group Multiple Exceptions

```python
try:
    # Some code
    data = process_input(user_input)
except (ValueError, TypeError, KeyError) as e:
    print(f"Input error: {e}")
```

### Catch All Exceptions (be careful!)

```python
# ⚠️ Only if really necessary
try:
    risky_operation()
except Exception as e:
    print(f"Unexpected error: {e}")
    # Logging, cleanup, etc.

# ❌ NEVER (catches SystemExit, KeyboardInterrupt too)
try:
    something()
except:  # Bare except
    pass  # Swallows ALL errors - very dangerous!
```

---

## 🔧 try/except/else/finally

```python
try:
    # Code that might fail
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    # Executed on error
    print("File not found!")
    content = ""
else:
    # Only executed if NO error
    print(f"File read: {len(content)} characters")
finally:
    # ALWAYS executed (cleanup)
    print("Operation completed")
```

### Visualized

```
try:
    │
    ▼ (Execute code)
    │
    ├── Exception occurs ──► except Block
    │                           │
    └── No error ────────────► else Block
                               │
                ◄──────────────┘
                │
                ▼
           finally Block (ALWAYS)
```

### When to Use What?

| Block | When to use |
|-------|-------------|
| `try` | Code that might fail |
| `except` | Error handling |
| `else` | Code that only runs on success |
| `finally` | Cleanup (free resources, close connections) |

---

## 🚀 Raising Exceptions with `raise`

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Unrealistic age!")
    return age

# Usage
try:
    age = set_age(-5)
except ValueError as e:
    print(f"Invalid input: {e}")
```

### Re-raising Exception

```python
def process_data(data):
    try:
        result = complex_operation(data)
    except ValueError as e:
        print(f"Logging: {e}")
        raise  # Raises the SAME exception again

# Or with a different exception
def process_data(data):
    try:
        result = complex_operation(data)
    except ValueError as e:
        raise RuntimeError(f"Data processing failed: {e}") from e
```

---

## 🏗️ Creating Custom Exceptions

```python
# Simple custom exception
class ValidationError(Exception):
    """Error during validation"""
    pass


# With additional attributes
class InsufficientFundsError(Exception):
    """Not enough balance in account"""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        message = f"Balance {balance} is insufficient for {amount} (missing {self.deficit})"
        super().__init__(message)


# Usage
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance


# Test
account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
    print(f"Missing: {e.deficit}")
```

### Creating Exception Hierarchy

```python
# Base exception for your application
class AppError(Exception):
    """Base for all app exceptions"""
    pass


class DatabaseError(AppError):
    """Database error"""
    pass


class ConnectionError(DatabaseError):
    """Connection error"""
    pass


class QueryError(DatabaseError):
    """Query error"""
    pass


# Now you can catch specifically or generally
try:
    database_operation()
except ConnectionError:
    # Only connection errors
    reconnect()
except DatabaseError:
    # All database errors
    log_error()
except AppError:
    # All app errors
    show_error_page()
```

---

## 📋 Important Built-in Exceptions

| Exception | When |
|-----------|------|
| `ValueError` | Wrong value (e.g., `int("abc")`) |
| `TypeError` | Wrong type (e.g., `"a" + 1`) |
| `KeyError` | Key not in dict |
| `IndexError` | Index out of list |
| `AttributeError` | Attribute/method doesn't exist |
| `FileNotFoundError` | File not found |
| `PermissionError` | No permission |
| `ZeroDivisionError` | Division by zero |
| `ImportError` | Import failed |
| `RuntimeError` | General runtime error |
| `StopIteration` | Iterator exhausted |
| `AssertionError` | `assert` failed |

### Exception-Hierarchie

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── OSError
    │   ├── FileNotFoundError
    │   └── PermissionError
    ├── ValueError
    ├── TypeError
    └── ...
```

---

## 🎯 EAFP vs LBYL

### LBYL (Look Before You Leap)

```python
# Check first, then act
def get_value(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return None
```

### EAFP (Easier to Ask Forgiveness than Permission)

```python
# Just try, handle errors
def get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None
```

**Python prefers EAFP!**

| LBYL | EAFP |
|------|------|
| More checks upfront | Less code |
| Race conditions possible | Thread-safe |
| Slower on success | Faster on success |
| Better for rare errors | Better for frequent errors |

---

## 🔄 Practical Examples

### Safe Type Conversion

```python
def safe_int(value, default=0):
    """Converts to int, returns default on error"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int("42"))      # 42
print(safe_int("abc"))     # 0
print(safe_int(None, -1))  # -1
```

### Retry Mechanism

```python
import time

def retry(func, max_attempts=3, delay=1):
    """Attempts to execute function multiple times"""
    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if attempt < max_attempts - 1:
                print(f"Attempt {attempt + 1} failed: {e}")
                print(f"Waiting {delay}s before retry...")
                time.sleep(delay)
            else:
                raise  # Last attempt also failed

# Usage
result = retry(lambda: fetch_data_from_api(), max_attempts=3)
```

### Input Validation

```python
def get_positive_number(prompt):
    """Asks for positive number until valid input"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Must be positive!")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")
            print("Please try again.")

age = get_positive_number("Enter age: ")
```

### Context Manager with Exception Handling

```python
class DatabaseConnection:
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        if exc_type is not None:
            print(f"Exception during DB operation: {exc_val}")
            # Return True to suppress exception
            # Return False/None to re-raise it
        return False

# Usage
with DatabaseConnection() as db:
    db.query("SELECT ...")
# Connection is ALWAYS closed, even on exception
```

---

## ⚠️ Common Pitfalls

### 1. Bare except (swallow all errors)

```python
# ❌ WRONG - Swallows Ctrl+C too!
try:
    something()
except:
    pass

# ✅ CORRECT - Be specific
try:
    something()
except ValueError:
    handle_value_error()
except Exception as e:
    log_unexpected_error(e)
    raise
```

### 2. Too broad exception handling

```python
# ❌ WRONG - Hides real bugs
try:
    data = fetch_data()
    result = process(data)
    save(result)
except Exception:
    print("An error occurred")

# ✅ CORRECT - Handle specifically
try:
    data = fetch_data()
except NetworkError:
    data = use_cached_data()

try:
    result = process(data)
except ProcessingError as e:
    log_error(e)
    result = None
```

### 3. Ignoring exceptions

```python
# ❌ WRONG
try:
    important_operation()
except SomeError:
    pass  # "It'll be fine..."

# ✅ CORRECT
try:
    important_operation()
except SomeError as e:
    logger.warning(f"Operation failed: {e}")
    # Or: Alternative action
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Catch specific exceptions | Use bare `except:` |
| Prefer EAFP style | Excessive LBYL |
| Use `finally` for cleanup | Leave resources open |
| Custom exceptions for domains | Generic exceptions everywhere |
| Log errors | Silently ignore errors |
| Use `raise` without argument for re-raise | Lose exception chain |

---

## 🎯 Exam Checklist

- [ ] `try/except/else/finally` syntax
- [ ] Handle multiple exceptions
- [ ] `raise` for custom exceptions
- [ ] `as e` to get exception object
- [ ] Create custom exception classes
- [ ] EAFP vs LBYL principle
- [ ] Know important built-in exceptions

---

[[17_Path_Operations|← Paths]] | [[00_Index|Index]] | [[19_Debugging|Debugging →]]
