---
title: Context Managers
tags: [python, context-managers, with, contextlib, exam-essential]
created: 2026-01-27
exam_weight: high
difficulty: advanced
---

# 🚪 Context Managers

[[00_Index|← Back to Index]] | [[15_Decorators|← Decorators]] | [[17_Memory_and_Performance|Memory and Performance →]]

> **"With 'with' you go in - and Python cleans up after you."**

---

## 🎯 The Concept: Automatic Resource Management

```
┌─────────────────────────────────────────────────────────────────┐
│              WHAT IS A CONTEXT MANAGER?                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PROBLEM WITHOUT CONTEXT MANAGER:                               │
│  ┌──────────────────────────────────────────┐                   │
│  │ f = open('file.txt')                     │                   │
│  │ data = f.read()     # What if error?     │                   │
│  │ f.close()           # May never          │                   │
│  │                       be reached!        │                   │
│  └──────────────────────────────────────────┘                   │
│                                                                  │
│  SOLUTION WITH CONTEXT MANAGER:                                 │
│  ┌──────────────────────────────────────────┐                   │
│  │ with open('file.txt') as f:              │                   │
│  │     data = f.read()                      │                   │
│  │                                          │                   │
│  │ # File is ALWAYS closed!                 │                   │
│  │ # Even with Exceptions!                  │                   │
│  └──────────────────────────────────────────┘                   │
│                                                                  │
│  GUARANTEED: Setup → Code → Cleanup (even with errors!)         │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Basics: The with Statement

```python
# ═══════════════════════════════════════════════════════════════
# BASIC WITH STATEMENT
# ═══════════════════════════════════════════════════════════════

# Read file
with open('data.txt', 'r') as f:
    content = f.read()
# f.close() is called automatically!

# Write file
with open('output.txt', 'w') as f:
    f.write("Hello World!")
# File is automatically closed and flushed!

# What happens internally?
# 1. f = open('data.txt', 'r')
# 2. f.__enter__() is called
# 3. Code in with-block is executed
# 4. f.__exit__() is called (ALWAYS, even with Exception!)

# ═══════════════════════════════════════════════════════════════
# WHY IS THIS IMPORTANT?
# ═══════════════════════════════════════════════════════════════

# ❌ WITHOUT with - Problematic!
f = open('file.txt')
try:
    data = f.read()
    # What if an Exception occurs here?
    process(data)  # ← Exception here = File stays open!
finally:
    f.close()

# ✅ WITH with - Safe!
with open('file.txt') as f:
    data = f.read()
    process(data)  # Exception? File is still closed!
```

---

## 📋 Multiple Context Managers

```python
# ═══════════════════════════════════════════════════════════════
# MULTIPLE CONTEXT MANAGERS AT ONCE
# ═══════════════════════════════════════════════════════════════

# Variant 1: Nested (old, but valid)
with open('input.txt', 'r') as infile:
    with open('output.txt', 'w') as outfile:
        outfile.write(infile.read())

# Variant 2: On one line (Python 3.1+)
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    outfile.write(infile.read())

# Variant 3: With parentheses (Python 3.10+) - For many managers
with (
    open('file1.txt') as f1,
    open('file2.txt') as f2,
    open('file3.txt') as f3
):
    # All three files are open
    pass
# All three are closed, in reverse order!
```

---

## 🏗️ Creating Own Context Manager (Class)

```python
# ═══════════════════════════════════════════════════════════════
# CONTEXT MANAGER AS CLASS
# ═══════════════════════════════════════════════════════════════

class MyContextManager:
    """Context Manager must implement __enter__ and __exit__."""

    def __init__(self, name):
        self.name = name
        print(f"__init__: {name} created")

    def __enter__(self):
        """Called when entering the with-block.
        Return value is assigned to 'as variable'."""
        print(f"__enter__: Entering {self.name}")
        return self  # This is what comes out at 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called ALWAYS when exiting (even with Exception).

        Parameters:
            exc_type: Exception class (or None)
            exc_val: Exception instance (or None)
            exc_tb: Traceback (or None)

        Return:
            True = Suppress exception
            False = Re-raise exception
        """
        print(f"__exit__: Exiting {self.name}")
        if exc_type:
            print(f"  Exception: {exc_type.__name__}: {exc_val}")
        return False  # Don't suppress exception

# Usage
with MyContextManager("Test") as cm:
    print(f"In with-block with {cm.name}")

# Output:
# __init__: Test created
# __enter__: Entering Test
# In with-block with Test
# __exit__: Exiting Test
```

### Practical Example: Timer

```python
import time

class Timer:
    """Measures the execution time of a code block."""

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.duration = self.end - self.start
        print(f"Duration: {self.duration:.4f} seconds")
        return False

# Usage
with Timer() as t:
    # Something slow
    sum(range(1_000_000))

print(f"That took {t.duration:.2f}s")
```

### Practical Example: Database Connection

```python
class DatabaseConnection:
    """Manages database connection with automatic cleanup."""

    def __init__(self, host, database):
        self.host = host
        self.database = database
        self.connection = None

    def __enter__(self):
        print(f"Connecting to {self.database}@{self.host}...")
        self.connection = self._connect()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Error occurred, rollback...")
            self.connection.rollback()
        else:
            print("Success, commit...")
            self.connection.commit()

        print("Closing connection...")
        self.connection.close()
        return False

    def _connect(self):
        # Simulated connection
        return type('Connection', (), {
            'execute': lambda s, q: print(f"  Execute: {q}"),
            'commit': lambda s: None,
            'rollback': lambda s: None,
            'close': lambda s: None
        })()

# Usage
with DatabaseConnection("localhost", "mydb") as conn:
    conn.execute("INSERT INTO users VALUES (1, 'Anna')")
    conn.execute("UPDATE accounts SET balance = 100")
```

---

## 🎯 Context Manager with contextlib

### @contextmanager Decorator

```python
# ═══════════════════════════════════════════════════════════════
# CONTEXTLIB.CONTEXTMANAGER - THE EASY WAY
# ═══════════════════════════════════════════════════════════════
from contextlib import contextmanager

@contextmanager
def my_context():
    """Generator-based context manager."""
    # Setup (= __enter__)
    print("Before yield = Setup")
    resource = "My Resource"

    try:
        yield resource  # This is what comes out at 'as'
    finally:
        # Cleanup (= __exit__)
        print("After yield = Cleanup")

# Usage
with my_context() as res:
    print(f"In block: {res}")

# Output:
# Before yield = Setup
# In block: My Resource
# After yield = Cleanup
```

### Practical Examples with @contextmanager

```python
from contextlib import contextmanager
import os

# ─────────────────────────────────────────────────────────────
# Temporarily change directory
# ─────────────────────────────────────────────────────────────
@contextmanager
def change_dir(path):
    """Temporarily changes the working directory."""
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_dir)

with change_dir('/tmp'):
    print(os.getcwd())  # /tmp
print(os.getcwd())      # Back to original

# ─────────────────────────────────────────────────────────────
# Temporary environment variable
# ─────────────────────────────────────────────────────────────
@contextmanager
def temp_env(key, value):
    """Temporarily sets an environment variable."""
    old_value = os.environ.get(key)
    os.environ[key] = value
    try:
        yield
    finally:
        if old_value is None:
            del os.environ[key]
        else:
            os.environ[key] = old_value

with temp_env('DEBUG', 'true'):
    print(os.environ['DEBUG'])  # true
# DEBUG is back to how it was

# ─────────────────────────────────────────────────────────────
# Redirect output
# ─────────────────────────────────────────────────────────────
import sys
from io import StringIO

@contextmanager
def capture_output():
    """Captures stdout."""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_stdout

with capture_output() as output:
    print("This will be captured")

captured = output.getvalue()
print(f"Captured: {captured}")
```

---

## 🔄 Exception Handling in Context Managers

```python
# ═══════════════════════════════════════════════════════════════
# EXCEPTIONS IN CONTEXT MANAGER
# ═══════════════════════════════════════════════════════════════

class ExceptionHandler:
    """Demonstrates exception handling in context manager."""

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exit - Exception: {exc_type}")

        if exc_type is ValueError:
            print("ValueError is suppressed!")
            return True   # ← Suppress exception

        return False      # ← Re-raise exception

# Test 1: Without exception
with ExceptionHandler():
    print("All OK")
# Enter
# All OK
# Exit - Exception: None

# Test 2: ValueError (suppressed)
with ExceptionHandler():
    raise ValueError("Test")
print("Continuing!")  # This is reached!
# Enter
# Exit - Exception: <class 'ValueError'>
# ValueError is suppressed!
# Continuing!

# Test 3: TypeError (not suppressed)
try:
    with ExceptionHandler():
        raise TypeError("Test")
except TypeError:
    print("TypeError caught")
# Enter
# Exit - Exception: <class 'TypeError'>
# TypeError caught
```

### With @contextmanager

```python
from contextlib import contextmanager

@contextmanager
def suppress_errors(*exceptions):
    """Suppresses specific exceptions."""
    try:
        yield
    except exceptions:
        pass  # Swallow the exception

# Usage
with suppress_errors(ValueError, KeyError):
    raise ValueError("Will be ignored")

print("Continuing!")  # This is reached
```

---

## 📚 contextlib Utilities

```python
# ═══════════════════════════════════════════════════════════════
# USEFUL CONTEXT MANAGERS FROM CONTEXTLIB
# ═══════════════════════════════════════════════════════════════
from contextlib import (
    suppress, redirect_stdout, redirect_stderr,
    closing, nullcontext, ExitStack
)

# ─────────────────────────────────────────────────────────────
# suppress - Ignore exceptions
# ─────────────────────────────────────────────────────────────
with suppress(FileNotFoundError):
    os.remove('does_not_exist.txt')
# No error, even if file doesn't exist!

# Multiple exceptions
with suppress(FileNotFoundError, PermissionError):
    os.remove('file.txt')

# ─────────────────────────────────────────────────────────────
# redirect_stdout / redirect_stderr
# ─────────────────────────────────────────────────────────────
from io import StringIO

f = StringIO()
with redirect_stdout(f):
    print("This goes into f")

print(f"Captured: {f.getvalue()}")

# Redirect to file
with open('log.txt', 'w') as f:
    with redirect_stderr(f):
        print("Error!", file=sys.stderr)

# ─────────────────────────────────────────────────────────────
# closing - For objects with close() but no __exit__
# ─────────────────────────────────────────────────────────────
class LegacyResource:
    def open(self):
        print("Opened")

    def close(self):
        print("Closed")

resource = LegacyResource()
resource.open()

with closing(resource):
    print("Using resource")
# close() is called automatically!

# ─────────────────────────────────────────────────────────────
# nullcontext - Optional context manager
# ─────────────────────────────────────────────────────────────
def process_data(lock=None):
    """Lock is optional."""
    # If no lock, use nullcontext
    ctx = lock if lock else nullcontext()

    with ctx:
        print("Processing data...")

process_data()              # Without lock
# process_data(threading.Lock())  # With lock
```

---

## 🔗 ExitStack - Dynamic Context Managers

```python
# ═══════════════════════════════════════════════════════════════
# EXITSTACK - MULTIPLE CONTEXT MANAGERS DYNAMICALLY
# ═══════════════════════════════════════════════════════════════
from contextlib import ExitStack

# Useful when number of context managers is unknown
filenames = ['file1.txt', 'file2.txt', 'file3.txt']

with ExitStack() as stack:
    files = [
        stack.enter_context(open(fn, 'w'))
        for fn in filenames
    ]

    # All files are open
    for i, f in enumerate(files):
        f.write(f"Content {i}")

# ALL files are closed!

# ─────────────────────────────────────────────────────────────
# Register callbacks
# ─────────────────────────────────────────────────────────────
def cleanup():
    print("Cleanup executed!")

with ExitStack() as stack:
    stack.callback(cleanup)  # Called at the end
    print("In block")

# Output:
# In block
# Cleanup executed!

# With arguments
with ExitStack() as stack:
    stack.callback(print, "Done!", end="\n\n")
    print("Working...")

# ─────────────────────────────────────────────────────────────
# Error handling with ExitStack
# ─────────────────────────────────────────────────────────────
with ExitStack() as stack:
    # Only open files that exist
    for fn in filenames:
        try:
            f = stack.enter_context(open(fn))
            # Use f
        except FileNotFoundError:
            print(f"{fn} not found, skipping...")
```

---

## 🏛️ Async Context Manager

```python
# ═══════════════════════════════════════════════════════════════
# ASYNC CONTEXT MANAGER (Python 3.5+)
# ═══════════════════════════════════════════════════════════════
import asyncio

class AsyncConnection:
    """Async context manager for network connections."""

    async def __aenter__(self):
        print("Connecting async...")
        await asyncio.sleep(0.1)  # Simulate connection
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Disconnecting async...")
        await asyncio.sleep(0.1)  # Simulate disconnection
        return False

async def main():
    async with AsyncConnection() as conn:
        print("Connected!")

asyncio.run(main())

# ─────────────────────────────────────────────────────────────
# With asynccontextmanager
# ─────────────────────────────────────────────────────────────
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_timer():
    """Async timer context manager."""
    import time
    start = time.time()
    try:
        yield
    finally:
        print(f"Async duration: {time.time() - start:.2f}s")

async def main():
    async with async_timer():
        await asyncio.sleep(1)

asyncio.run(main())
```

---

## 📊 Visualization: Context Manager Flow

```
┌─────────────────────────────────────────────────────────────────┐
│              CONTEXT MANAGER FLOW                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  with context_manager as value:                                  │
│      code_block()                                                │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  1. __enter__() called                                    │   │
│  │     └── Return value → value                              │   │
│  └──────────────────────────────────────────────────────────┘   │
│                         │                                        │
│                         ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  2. code_block() executed                                 │   │
│  │     ├── Success → continue                                │   │
│  │     └── Exception → exc_type, exc_val, exc_tb set         │   │
│  └──────────────────────────────────────────────────────────┘   │
│                         │                                        │
│                         ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  3. __exit__(exc_type, exc_val, exc_tb) ALWAYS called    │   │
│  │     ├── return True → Exception suppressed                │   │
│  │     └── return False → Exception re-raised                │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Comparison: Class vs @contextmanager

| Aspect | Class | @contextmanager |
|--------|--------|-----------------|
| Code amount | More | Less |
| Readability | Explicit | Compact |
| Store state | Easy (self) | Harder |
| Exception handling | Detailed | Simple |
| Reusability | Good | Good |
| Async support | __aenter__/__aexit__ | @asynccontextmanager |

**Recommendation:**
- Simple cases → `@contextmanager`
- Complex logic/state → Class

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: yield forgotten
from contextlib import contextmanager

@contextmanager
def bad_context():
    print("Setup")
    # yield is missing!
    print("Cleanup")

# with bad_context():  # Generator yields nothing - Error!

# ✅ CORRECT: don't forget yield
@contextmanager
def good_context():
    print("Setup")
    yield  # Important even without value!
    print("Cleanup")

# ❌ WRONG: Exception after yield not handled
@contextmanager
def bad_error_handling():
    resource = acquire_resource()
    yield resource
    release_resource(resource)  # Not reached on exception!

# ✅ CORRECT: use try/finally
@contextmanager
def good_error_handling():
    resource = acquire_resource()
    try:
        yield resource
    finally:
        release_resource(resource)  # ALWAYS executed!

# ❌ WRONG: __exit__ return value forgotten
class BadContext:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass  # Implicitly None = False, OK but explicit is better

# ✅ CORRECT: Explicitly return False/True
class GoodContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False  # Explicitly: don't suppress exceptions

# ❌ WRONG: 'as' with context manager without return value
@contextmanager
def no_return():
    print("Block")
    yield  # Returns None

with no_return() as x:
    print(x)  # None - probably not intended
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| `try/finally` around yield | yield without error handling |
| `@contextmanager` for simple cases | Class for trivial cases |
| ALWAYS free resources | Forget cleanup |
| Log exception info in __exit__ | Silently swallow exceptions |
| `closing()` for legacy objects | Manual close() |
| `ExitStack` for dynamic managers | Deeply nested with-blocks |

---

## 🎯 Exam Checklist

- [ ] `with` statement syntax and flow
- [ ] `__enter__()` returns the value for `as`
- [ ] `__exit__(exc_type, exc_val, exc_tb)` is ALWAYS called
- [ ] `__exit__` return True = suppress exception
- [ ] `@contextmanager` decorator with yield
- [ ] `contextlib.suppress()` to ignore exceptions
- [ ] `contextlib.closing()` for legacy objects
- [ ] Multiple context managers on one line
- [ ] `ExitStack` for dynamic context managers

---

[[15_Decorators|← Decorators]] | [[00_Index|Index]] | [[17_Memory_and_Performance|Memory and Performance →]]
