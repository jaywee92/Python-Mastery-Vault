---
title: Python Advanced - Summary
tags: [python, advanced, summary, reference, cheatsheet]
---

# Python Advanced - Summary

## 📋 Overview

This summary covers the most important advanced Python concepts: OOP with inheritance and magic methods, functional programming with decorators and generators, and best practices for debugging, testing, and code quality. It's a quick reference guide for reviewing and deepening all topics.

---

## 🔑 Quick Reference

### OOP Concepts

| Concept | Description | Example |
|---------|-------------|----------|
| **Inheritance** | Inheritance from parent to child class | `class Dog(Animal):` |
| **super()** | Access to parent methods | `super().__init__(name)` |
| **Magic Methods** | Special methods with `__name__` | `__str__`, `__add__`, `__iter__` |
| **@property** | Attribute-like access with validation | `@property def value(self):` |
| **@classmethod** | Class method with `cls` parameter | `@classmethod def from_dict(cls, data):` |
| **@staticmethod** | Utility function without self/cls | `@staticmethod def validate(x):` |
| **ABC** | Abstract base classes for interfaces | `from abc import ABC, abstractmethod` |

### Important Magic Methods

| Category | Methods |
|-----------|----------|
| **Lifecycle** | `__init__`, `__new__`, `__del__` |
| **String** | `__str__`, `__repr__`, `__format__` |
| **Operator** | `__add__`, `__sub__`, `__mul__`, `__eq__`, `__lt__` |
| **Container** | `__len__`, `__getitem__`, `__setitem__`, `__iter__` |
| **Attribute** | `__getattr__`, `__setattr__`, `__delattr__` |
| **Context** | `__enter__`, `__exit__` |

### Important Modules

| Module | Purpose | Example |
|-------|-------|----------|
| **pathlib** | Modern path operations | `Path('data') / 'file.txt'` |
| **json** | Serialization & deserialization | `json.dumps()`, `json.loads()` |
| **datetime** | Date & time operations | `datetime.now()`, `date(2024, 1, 1)` |
| **re** | Regular expressions | `re.search(r'\d+', text)` |
| **itertools** | Iterator tools | `chain()`, `combinations()`, `product()` |
| **functools** | Higher-order functions | `reduce()`, `partial()`, `@wraps` |
| **logging** | Professional logging | `logging.getLogger(__name__)` |
| **unittest** | Unit testing framework | `unittest.TestCase` |

---

## 📝 Topic Summaries

### Inheritance

Enables code reuse by inheriting from parent classes. Child classes inherit attributes and methods and can override them. `super()` accesses parent methods. Multiple inheritance possible with MRO (Method Resolution Order). Abstract Base Classes (ABC) enforce implementation of certain methods in subclasses. Use case: shape hierarchy with specialized behavior per type.

### Magic Methods (Dunder Methods)

Special methods with double underscores that Python calls automatically. `__str__` for user-friendly output, `__repr__` for debugging. Arithmetic operators (`__add__`, `__mul__`) enable custom operations. Container methods (`__getitem__`, `__iter__`) make objects indexable/iterable. `__enter__`/`__exit__` for context manager. Use case: vector class with `__add__` and `__mul__` for mathematical operations.

### Properties and Class Methods

`@property` enables validated attribute access without getter/setter methods. `@classmethod` for alternative constructors and class variable management (e.g., `Person.from_dict()`). `@staticmethod` for utility functions without self/cls. Decision tree: needs self? → Instance method. Needs cls? → @classmethod. Needs nothing? → @staticmethod.

### JSON (Serialization)

`json.dumps()` converts Python to JSON string, `json.loads()` vice versa. `json.dump()` writes directly to file, `json.load()` reads from file. Type mapping: dict↔object, list↔array, str↔string, int/float↔number, bool↔true/false, None↔null. Custom encoder/decoder for complex types like datetime. Important: tuples become arrays and back to lists.

### Path Operations (pathlib)

`Path` is modern, OOP variant of `os.path`. `/` operator for path concatenation. Important attributes: `.name` (filename), `.stem` (without extension), `.suffix` (extension), `.parent` (directory). `.glob('*.py')` for pattern matching, `.rglob()` recursively. `.read_text()`, `.write_text()` for easy reading/writing. `.mkdir(parents=True)` for directory creation.

### Debugging

`breakpoint()` sets interactive breakpoints in PDB (Python Debugger). PDB commands: `n` (next), `s` (step into), `c` (continue), `p expr` (print). F-string debugging: `f"{var=}"` shows name and value. `assert` for internal invariants (development only). IDE debugger offers visual breakpoints and variable inspection. Print debugging is simple but forgetful.

### Logging

5 log levels: DEBUG < INFO < WARNING < ERROR < CRITICAL. `basicConfig()` for simple setup, `getLogger(__name__)` for module loggers. Handlers (console, file) with different levels. Formatter with format codes like `%(asctime)s`, `%(levelname)s`. `logger.exception()` for stack traces. Log rotation prevents unlimited file growth.

### Unit Testing

`unittest.TestCase` with `assertEqual()`, `assertTrue()`, `assertRaises()` methods. `setUp()`/`tearDown()` before/after each test, `setUpClass()`/`tearDownClass()` for class. `pytest` is more modern with simple functions instead of classes and `@pytest.fixture` for setup. `@pytest.mark.parametrize` for multiple test cases. Mocking with `@patch` for isolated API/DB testing.

### Code Quality

PEP 8 style guide: `snake_case` for variables/functions, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants. Readability counts (max 79 characters). Docstrings for modules/classes/functions. Type hints improve code readability. Linters (flake8, black) and formatters automate consistency. Good code is maintainable code.

### Common Pitfalls (Top 10)

1. **Mutable Defaults**: `def func(lst=[]):` → List reused! Fix: `lst=None` with creation in body
2. **Late Binding Closures**: Lambdas bind variables late → Use `default=i` parameter
3. **Modifying While Iterating**: Don't modify during iteration → Use list comprehension or copy
4. **== vs is**: `is` only for None/True/False, `==` for values
5. **Forgotten return**: Function returns None instead of value → Add explicit `return`
6. **Integer Caching**: -5 to 256 cached, outside new objects → `is` unreliable
7. **List as Class Attribute**: Shared between instances → Use instance attribute
8. **Shallow vs Deep Copy**: `copy()` for shallow, `deepcopy()` for nested structures
9. **Variable Scope in Loops**: Loop variable exists after loop → Avoid name reuse
10. **String Immutability**: Strings immutable → New string operations create new objects

### Standard Library

Important modules: `os`, `sys` (OS interface), `pathlib` (paths), `json` (serialization), `datetime` (time), `re` (regex), `collections` (advanced containers), `itertools` (iterator tools), `functools` (higher-order functions), `logging` (logging), `unittest` (testing). `os` is increasingly replaced by `pathlib`.

### Regular Expressions

`re.search()` finds first match, `re.match()` only at start, `re.fullmatch()` entire string. `re.findall()` returns list of all matches. `re.sub()` for search & replace. `r''` (raw string) essential for regex! Patterns: `\d` (digit), `\w` (word), `\s` (whitespace), `[abc]` (character set), `*` (0+), `+` (1+), `?` (0-1), `{n,m}` (n to m). Flags: `re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`.

### Working with Dates

`date` for date, `time` for time, `datetime` for both, `timedelta` for differences. `date.today()` current, `.strftime()` formatting, `.strptime()` parsing. `timedelta(days=1, hours=2)` for time differences. Timezone with `pytz` or `zoneinfo` (Python 3.9+). ISO format (`isoformat()`) is portable and sortable.

### Iterators and Generators

Iterator protocol: `__iter__()` returns iterator, `__next__()` returns next element or `StopIteration`. `yield` in generators → lazy evaluation, memory efficient. `next()` and `for` trigger `__next__()`. Generator expression `(x for x in range(1M))` vs list `[x for x in range(1M)]` - huge memory difference. `yield from` delegates to sub-generator.

### Decorators

Decorators are functions that wrap and extend functions. `@decorator` syntax is syntactic sugar for `func = decorator(func)`. Closure enables state between calls. `functools.wraps` preserves metadata. Use case: logging, timing, caching, validation. Parameters: `@decorator(arg)` needs triple nesting. Classes as decorators possible via `__call__`.

### Context Managers

`with` statement guarantees cleanup via `__enter__()`/`__exit__()` even with exceptions. `@contextlib.contextmanager` decorator simplifies custom context manager. Multiple: `with open(...) as f1, open(...) as f2:`. Use case: file handling, database transactions, locks, temp directories. `__exit__()` return value controls exception propagation.

### Memory and Performance

Larger data structures: `sys.getsizeof()` shallow size. Generators save memory (lazy). List comprehensions faster than loops. Dictionary/set O(1) lookup vs list O(n). `timeit` module for micro-benchmarking. `cProfile` for profiling. Avoid: nested loops, redundant calculations, large temporary lists. Optimize: builtin functions (C-written), vectorization (NumPy), caching.

### Operators Deep Dive

Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`. Comparison: `==`, `!=`, `<`, `<=`, `>`, `>=`. Logical: `and`, `or`, `not`. Bitwise: `&`, `|`, `^`, `~`, `<<`, `>>`. Assignment: `=`, `+=`, `-=`, etc. Identity: `is`, `is not` (only for None/True/False). Membership: `in`, `not in`. Operator precedence: exponentiation > multiplication > addition > comparison > logical.

### Modules and Packages

Module = `.py` file with code. Package = directory with `__init__.py`. `import mymodule`, `from mymodule import func`, `from mymodule import func as f`. Namespace management prevents name conflicts. `__all__` defines public API. Relative imports: `from . import sibling`, `from .. import parent`. Avoid circular imports through reorganization.

### pip Package Manager

`pip install package` installs from PyPI. `pip install package==1.0.0` specific version. `pip install -r requirements.txt` installs from file. `pip list` shows installed packages. `pip freeze > requirements.txt` exports currently installed. Virtual environments (`venv`, `virtualenv`) for project isolation. `pyenv` for Python version management.

### Web Scraping

`requests.get(url)` fetches HTML. `BeautifulSoup(html, 'lxml')` parses HTML. `.find()`, `.find_all()` for element selection. `.select()` with CSS selectors. Check robots.txt and ToS before scraping. Build in throttle/delays. User-agent header important. Handle exceptions (timeout, connection errors). Prefer structured data (JSON APIs) to scraping.

### Virtual Environments

`python -m venv myenv` creates virtual environment. `source myenv/bin/activate` (Linux/Mac) or `myenv\Scripts\activate` (Windows) activates. `deactivate` leaves environment. Isolates packages per project, prevents conflicts. Create `requirements.txt` with `pip freeze` for reproducibility. Add `venv/` to `.gitignore` to exclude from repo.

### Statistics

`statistics` module for basic stats: `mean()`, `median()`, `mode()`. `variance()`, `stdev()` for spread. NumPy & Pandas for advanced analysis. Scipy for statistical tests. Matplotlib for visualization. Important: distinguish sample vs population mean/variance. Outlier detection & handling. Check normal distribution before parametric tests.

### Pandas Basics

`Series` = 1D labeled array. `DataFrame` = 2D table (like Excel). `.read_csv()`, `.to_csv()` for CSV. `.loc[]` label-based selection, `.iloc[]` index-based. `.groupby()` for aggregation. `.apply()` for custom functions. `.merge()`, `.join()` for combining. Performance: vectorized operations faster than loops. Missing values: `.fillna()`, `.dropna()`.

### Flask Web Framework

Lightweight microframework. `@app.route()` defines routes. Request handling via `request` object. Response as string, JSON, redirect. Templates with Jinja2. Static files management. Error handling with `@app.errorhandler()`. Blueprints for modularization. Session & cookie management. Deployment on Gunicorn/uWSGI. Perfect for APIs & small apps.

### MongoDB Integration

NoSQL document database with JSON-like structure. `PyMongo` library for Python integration. Collections instead of tables, documents instead of rows. `insert_one()`, `insert_many()` for inserts. `find()` for query, `find_one()` for single. `update_one()`, `replace_one()` for updates. `delete_one()`, `delete_many()` for deletion. Indexing for performance. Aggregation pipeline for complex queries.

### Professional Libraries

`requests` for HTTP. `pandas` & `numpy` for data. `matplotlib` & `seaborn` for plots. `sqlalchemy` ORM for databases. `pydantic` for data validation. `fastapi` for modern web APIs. `asyncio` & `aiohttp` for async. `click` & `argparse` for CLI. `pytest` for testing. `python-dotenv` for environment variables. Standard in industry projects.

---

## ✅ Self-Test Checklist

### OOP & Inheritance
- [ ] I can design simple inheritance hierarchies
- [ ] I understand `super()` and when to use it
- [ ] I know the differences between inheritance vs composition
- [ ] I understand MRO (method resolution order) in multiple inheritance
- [ ] I can implement abstract base classes (ABC)

### Magic Methods
- [ ] I can distinguish `__str__` vs `__repr__`
- [ ] I can override arithmetic operators (`__add__`, `__mul__`)
- [ ] I understand `__getitem__`, `__setitem__`, `__len__` for containers
- [ ] I can write `__enter__`/`__exit__` for context managers
- [ ] I understand `__eq__` and `__hash__` relationship

### Properties & Methods
- [ ] I can implement `@property` with getter, setter, deleter
- [ ] I understand `@classmethod` for factory methods
- [ ] I can use `@staticmethod` for utility functions
- [ ] I know when to use which decorator

### Practical Topics
- [ ] I can serialize/deserialize JSON
- [ ] I use pathlib for modern path operations
- [ ] I can work with datetime and time formatting
- [ ] I write simple regular expressions
- [ ] I use itertools and functools efficiently

### Debugging & Testing
- [ ] I can use `breakpoint()` and PDB commands
- [ ] I write unit tests with unittest or pytest
- [ ] I understand mocking and when to apply it
- [ ] I can set up and configure logging
- [ ] I can use assertions for internal invariants

### Advanced Topics
- [ ] I understand generators and `yield` for memory efficiency
- [ ] I can write decorators and understand closures
- [ ] I understand context managers and the `with` statement
- [ ] I know common pitfalls and how to avoid them
- [ ] I can use code quality tools

### Professional Development
- [ ] I use virtual environments for project isolation
- [ ] I write PEP 8 compliant code
- [ ] I understand module/package structure
- [ ] I can work with APIs (requests)
- [ ] I understand basics of Pandas, Flask, MongoDB

---

## 🛤️ Recommended Learning Path

### Phase 1: OOP Foundation (Understanding basics)
1. **Inheritance** - Inheritance hierarchies, super(), polymorphism
2. **Magic Methods** - String representation, operator overloading
3. **Properties & Decorators** - @property, @classmethod, @staticmethod
4. Start: Write simple class with inheritance

### Phase 2: Working with Data (Practical skills)
1. **JSON** - Serialization, custom encoder/decoder
2. **pathlib** - Modern path operations
3. **datetime** - Date/time operations
4. **Regular Expressions** - Pattern matching & parsing
5. Project: Config file parser with JSON + pathlib

### Phase 3: Functional & Advanced (Conceptual)
1. **Iterators & Generators** - Lazy evaluation, memory efficiency
2. **Decorators** - Extend functions, closures
3. **Context Managers** - Resource management
4. Project: Decorator for logging/timing, generator for large data

### Phase 4: Quality & Best Practices (Professional)
1. **Debugging** - PDB, assertions, print debugging
2. **Logging** - Production logging, log levels
3. **Unit Testing** - unittest/pytest, mocking
4. **Code Quality** - PEP 8, linting, type hints
5. **Common Pitfalls** - Mutable defaults, late binding, etc.

### Phase 5: Professional Development (Practical)
1. **Standard Library** - os, sys, collections, itertools, functools
2. **Virtual Environments** - pip, requirements.txt
3. **Professional Libraries** - requests, pandas, numpy (selective)
4. **Web/DB Basics** - Flask/MongoDB or web scraping
5. **Memory & Performance** - Profiling, optimization
6. Project: Web app or API with testing & logging

### Phase 6: Deepening (Specialized)
- By interest: web (Flask/FastAPI), data (Pandas/NumPy), DevOps, async programming
- Continuous improvement: code reviews, open source, production experience

---

## 💡 Learning Tips

1. **Hands-On Learning**: Type every line of code, don't copy-paste
2. **Small Projects**: Quiz app, todo manager, web scraper → combine topics in mini-projects
3. **Practice Debugging**: Intentionally build bugs & debug with PDB
4. **Code Review**: Read others' code (open source, GitHub)
5. **Regular Testing**: Weekly mini-tests based on checklist
6. **Read Documentation**: Official docs are gold (docs.python.org)
7. **Understand Error Messages**: Read tracebacks from bottom to top

---

## 🎯 Exam Tips

1. **Time Management**: Easy/medium first, then hard
2. **Keyword Recognition**: "Write a decorator" vs "explain ABC"
3. **Code reading/debugging**: Don't write code blindly, predict errors
4. **Practical Examples**: Concrete scenarios better than theory
5. **Edge Cases**: Always test None, empty collections, 0, -1
6. **Best Practices**: PEP 8, error handling, documentation count
7. **Time Budget**: 2-3 minutes per question, review at end

---

Generated: 2026-02-05
Source: 25 Python Advanced Topics (01-27)
