---
title: Code Quality
tags: [python, code-quality, pep8, best-practices, style, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# ✨ Code Quality

[[00_Index|← Back to Index]] | [[08_Unit_Testing|← Unit Testing]] | [[10_Common_Pitfalls|Common Pitfalls →]]

> **"Code is read much more often than written - write for the reader!"**

---

## 🎯 What is Code Quality?

```
┌─────────────────────────────────────────────────────────────────┐
│                    QUALITY CHARACTERISTICS                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  📖 Readability      Code is easy to understand                 │
│  🔧 Maintainability  Code is easy to change                     │
│  🧪 Testability      Code is easy to test                       │
│  🔄 Reusability      Code can be used elsewhere                 │
│  📏 Consistency      Same style throughout project              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📜 PEP 8 - The Python Style Guide

PEP 8 is the official style guide for Python code.

### Naming Conventions

```python
# ═══════════════════════════════════════════════════════════════
# VARIABLES & FUNCTIONS: snake_case
# ═══════════════════════════════════════════════════════════════
user_name = "Alice"
total_count = 42
is_active = True

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def get_user_by_id(user_id):
    pass

# ═══════════════════════════════════════════════════════════════
# CONSTANTS: UPPER_SNAKE_CASE
# ═══════════════════════════════════════════════════════════════
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
PI = 3.14159
DATABASE_URL = "postgresql://localhost/db"

# ═══════════════════════════════════════════════════════════════
# CLASSES: PascalCase (CapWords)
# ═══════════════════════════════════════════════════════════════
class UserAccount:
    pass

class HTTPConnection:  # Acronyms capitalized
    pass

class XMLParser:
    pass

# ═══════════════════════════════════════════════════════════════
# PRIVATE/PROTECTED: With underscore
# ═══════════════════════════════════════════════════════════════
_internal_variable = "internal only"      # Protected (convention)
__private_variable = "name mangling"   # Private (no direct access)

class MyClass:
    def _helper_method(self):          # Protected
        pass

    def __private_method(self):        # Private
        pass

# ═══════════════════════════════════════════════════════════════
# MODULES & PACKAGES: lowercase (short names)
# ═══════════════════════════════════════════════════════════════
# my_module.py
# user_utils.py
# database_handler.py
```

```
┌─────────────────────────────────────────────────────────────────┐
│                   NAMING OVERVIEW                                │
├───────────────────┬─────────────────────────────────────────────┤
│ Variables         │ snake_case         │ user_name, total_count │
│ Functions         │ snake_case         │ get_user(), calc_sum() │
│ Constants         │ UPPER_SNAKE_CASE   │ MAX_SIZE, PI           │
│ Classes           │ PascalCase         │ UserAccount, HTTPError │
│ Modules           │ lowercase          │ my_module.py           │
│ Protected         │ _single_underscore │ _internal_var          │
│ Private           │ __double_underscore│ __private_method       │
└───────────────────┴─────────────────────────────────────────────┘
```

### Indentation and Formatting

```python
# ═══════════════════════════════════════════════════════════════
# INDENTATION: 4 spaces (NO tabs!)
# ═══════════════════════════════════════════════════════════════
def function():
    if condition:
        do_something()
        if another_condition:
            do_more()

# ═══════════════════════════════════════════════════════════════
# LINE LENGTH: Max 79 characters (99 for teams allowed)
# ═══════════════════════════════════════════════════════════════

# ❌ Too long
result = some_function(argument_one, argument_two, argument_three, argument_four, argument_five)

# ✅ Broken with parentheses (implicit continuation)
result = some_function(
    argument_one,
    argument_two,
    argument_three,
    argument_four
)

# ✅ Or with hanging indent
result = some_function(argument_one, argument_two,
                       argument_three, argument_four)

# ═══════════════════════════════════════════════════════════════
# BLANK LINES
# ═══════════════════════════════════════════════════════════════

# 2 blank lines between top-level definitions
class FirstClass:
    pass


class SecondClass:  # 2 blank lines above
    pass


def top_level_function():  # 2 blank lines above
    pass

# 1 blank line between methods
class MyClass:
    def method_one(self):
        pass

    def method_two(self):  # 1 blank line above
        pass
```

### Whitespace

```python
# ═══════════════════════════════════════════════════════════════
# WHITESPACE AROUND OPERATORS
# ═══════════════════════════════════════════════════════════════

# ✅ CORRECT
x = 1
y = x + 2
z = x * 2 + y
flag = x == y

# ❌ WRONG
x=1
y=x+2

# ═══════════════════════════════════════════════════════════════
# NO WHITESPACE
# ═══════════════════════════════════════════════════════════════

# ✅ Directly before/after parentheses
function(arg1, arg2)
my_list[0]
my_dict['key']

# ❌ WRONG
function( arg1, arg2 )
my_list[ 0 ]

# ✅ After comma, but not before
print(a, b, c)
my_tuple = (1, 2, 3)

# ❌ WRONG
print(a , b , c)

# ✅ Keyword arguments with no space around =
def func(arg1, arg2=None):
    pass

func(10, arg2=20)

# ❌ WRONG
def func(arg1, arg2 = None):
    pass
```

---

## 📝 Docstrings

Documentation directly in code:

### Function Docstrings

```python
def calculate_area(width: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle in meters.
        height: The height of the rectangle in meters.

    Returns:
        The area in square meters.

    Raises:
        ValueError: If width or height are negative.

    Examples:
        >>> calculate_area(3, 4)
        12.0
        >>> calculate_area(0, 5)
        0.0
    """
    if width < 0 or height < 0:
        raise ValueError("Measurements must not be negative")
    return width * height

# Short docstrings on one line
def double(x):
    """Double the input value."""
    return x * 2
```

### Class Docstrings

```python
class BankAccount:
    """
    Represents a bank account.

    A BankAccount manages a balance and allows
    deposits and withdrawals.

    Attributes:
        owner: Name of the account holder.
        balance: Current account balance in euros.
        account_number: Unique account number.

    Example:
        >>> account = BankAccount("Alice", 1000)
        >>> account.deposit(500)
        >>> account.balance
        1500
    """

    def __init__(self, owner: str, initial_balance: float = 0):
        """
        Create a new bank account.

        Args:
            owner: Name of the account holder.
            initial_balance: Initial balance (default: 0).
        """
        self.owner = owner
        self.balance = initial_balance
```

### Docstring Formats

```
┌─────────────────────────────────────────────────────────────────┐
│                   DOCSTRING FORMATS                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Google Style (recommended):                                     │
│  Args:                                                           │
│      param1: Description                                         │
│  Returns:                                                        │
│      Description                                                 │
│                                                                  │
│  NumPy Style:                                                    │
│  Parameters                                                      │
│  ----------                                                      │
│  param1 : type                                                   │
│      Description                                                 │
│                                                                  │
│  Sphinx/reStructuredText:                                        │
│  :param param1: Description                                      │
│  :returns: Description                                           │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏷️ Type Hints

Python 3.5+ supports optional type annotations:

### Basic Types

```python
# Simple types
name: str = "Alice"
age: int = 30
price: float = 19.99
is_active: bool = True

# Functions with type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

# None as return value
def print_message(msg: str) -> None:
    print(msg)
```

### Complex Types

```python
from typing import List, Dict, Tuple, Set, Optional, Union, Any, Callable

# Lists
def process_numbers(numbers: List[int]) -> List[int]:
    return [n * 2 for n in numbers]

# Dictionaries
def get_user_ages(users: Dict[str, int]) -> Dict[str, int]:
    return users

# Tuples (fixed length and types)
def get_point() -> Tuple[int, int]:
    return (10, 20)

# Set
def unique_items(items: List[str]) -> Set[str]:
    return set(items)

# Optional (can be None)
def find_user(user_id: int) -> Optional[str]:
    """Return username or None if not found."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# Union (multiple types possible)
def process(value: Union[int, str]) -> str:
    return str(value)

# Python 3.10+: Simplified syntax
def process_modern(value: int | str) -> str:
    return str(value)

def find_user_modern(user_id: int) -> str | None:
    pass

# Callable (functions as parameters)
def apply_func(func: Callable[[int], int], value: int) -> int:
    return func(value)

# Any (any type - use sparingly!)
def log_anything(value: Any) -> None:
    print(value)
```

### Classes with Type Hints

```python
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int
    friends: List[str] = None

    def __post_init__(self):
        if self.friends is None:
            self.friends = []

# Oder traditionell
class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price

    def apply_discount(self, percent: float) -> float:
        return self.price * (1 - percent / 100)
```

---

## 🔍 Import Organization

```python
# ═══════════════════════════════════════════════════════════════
# IMPORT ORDER (with blank line between groups)
# ═══════════════════════════════════════════════════════════════

# 1. Standard Library
import os
import sys
from collections import defaultdict
from typing import List, Optional

# 2. Third-Party Packages
import numpy as np
import pandas as pd
from flask import Flask, request

# 3. Local Imports
from .my_module import my_function
from mypackage import utils

# ═══════════════════════════════════════════════════════════════
# IMPORT STYLES
# ═══════════════════════════════════════════════════════════════

# ✅ RECOMMENDED: Individual imports
import os
import sys

# ✅ OK: Multiple from one module
from typing import List, Dict, Optional

# ❌ AVOID: Wildcard imports (except in __init__.py)
from module import *  # Where does what come from?

# ✅ Break long imports
from very_long_module_name import (
    function_one,
    function_two,
    ClassOne,
    ClassTwo,
)
```

---

## 🛠️ Code Quality Tools

### Linter: flake8

```bash
pip install flake8
flake8 my_script.py
flake8 src/ --max-line-length=100
```

### Formatter: black

```bash
pip install black
black my_script.py           # Auto-format
black src/ --check           # Check only, don't change
black src/ --diff            # Show changes
```

### Type Checker: mypy

```bash
pip install mypy
mypy my_script.py
mypy src/ --strict           # Strict mode
```

### All together: pre-commit

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.1.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.0.0
    hooks:
      - id: mypy
```

```bash
pip install pre-commit
pre-commit install  # Runs automatically before each commit
```

---

## 📏 Code Metrics

### Cyclomatic Complexity

```python
# Complexity = Number of decision paths

# ❌ High complexity (hard to test/understand)
def complex_function(a, b, c, d):
    if a:
        if b:
            if c:
                return 1
            else:
                return 2
        elif d:
            return 3
    else:
        if c and d:
            return 4
    return 0

# ✅ Low complexity (split up)
def check_condition_a(a, b, c, d):
    if not a:
        return check_without_a(c, d)
    return check_with_a(b, c, d)

def check_with_a(b, c, d):
    if b:
        return 1 if c else 2
    if d:
        return 3
    return 0
```

```
┌─────────────────────────────────────────────────────────────────┐
│                 COMPLEXITY GUIDELINES                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Complexity │ Meaning                                           │
│  ──────────┼──────────────────────────────────────────────────│
│      1-10    │ ✅ Simple, easy to test                         │
│     11-20    │ ⚠️ Moderate, consider refactoring              │
│     21-50    │ ❌ Complex, hard to maintain                    │
│      >50     │ 🔥 Too complex, must be split up               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Inconsistent naming
userName = "Alice"      # camelCase
user_age = 30           # snake_case
UserEmail = "a@b.com"   # PascalCase

# ✅ CORRECT: Consistent snake_case
user_name = "Alice"
user_age = 30
user_email = "a@b.com"

# ❌ WRONG: Single-letter names (except in loops)
def f(x, y, z):
    return x + y * z

# ✅ CORRECT: Descriptive names
def calculate_total(base_price, quantity, tax_rate):
    return base_price + quantity * tax_rate

# ❌ WRONG: Magic numbers
def calculate_price(amount):
    return amount * 1.19  # What is 1.19?

# ✅ CORRECT: Named constants
TAX_RATE = 0.19

def calculate_price(amount):
    return amount * (1 + TAX_RATE)

# ❌ WRONG: Functions that are too long
def do_everything():
    # 200 lines of code...
    pass

# ✅ CORRECT: Small, focused functions
def validate_input(data):
    pass

def process_data(data):
    pass

def save_result(result):
    pass
```

---

## ✅ Best Practices Overview

| Do ✅ | Don't ❌ |
|-------|---------|
| Follow PEP 8 | Invent your own style |
| snake_case for variables | camelCase for variables |
| Use type hints | Leave types unclear |
| Short functions (<20 lines) | Giant functions |
| Write docstrings | Undocumented code |
| Constants over magic numbers | `if x > 86400:` |
| Use linter/formatter | Manually format |
| Meaningful names | `x`, `temp`, `data` |

---

## 🎯 Exam Checklist

- [ ] PEP 8 Naming: snake_case, PascalCase, UPPER_CASE
- [ ] 4 space indentation, max 79 characters
- [ ] Docstrings (Google Style: Args, Returns, Raises)
- [ ] Type Hints: `List[int]`, `Optional[str]`, `Union[int, str]`
- [ ] Import order: stdlib, third-party, local
- [ ] Tools: flake8 (Linter), black (Formatter), mypy (Type Checker)
- [ ] No magic numbers, descriptive names
- [ ] Private attributes: `_protected`, `__private`

---

[[08_Unit_Testing|← Unit Testing]] | [[00_Index|Index]] | [[10_Common_Pitfalls|Common Pitfalls →]]
