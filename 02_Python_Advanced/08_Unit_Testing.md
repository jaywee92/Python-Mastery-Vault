---
title: Unit Testing
tags: [python, testing, unittest, pytest, quality, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# 🧪 Unit Testing

[[00_Index|← Back to Index]] | [[20_Logging|← Logging]] | [[22_Code_Quality|Code Quality →]]

> **"Code without tests is like a house without a foundation - it stands, until it doesn't."**

---

## 🎯 Why test?

```
┌─────────────────────────────────────────────────────────────────┐
│                    BENEFITS OF TESTS                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ✅ Find bugs early           Tests catch errors BEFORE prod    │
│  ✅ Refactoring safely        Changes without fear of breaking  │
│  ✅ Documentation             Tests show how code works          │
│  ✅ Better design             Testable code = well structured    │
│  ✅ Time savings              Less manual testing                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 unittest - The Standard Library

### Basic Structure

```python
import unittest

# The function we want to test
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero!")
    return a / b

# Test class (inherits from unittest.TestCase)
class TestMathFunctions(unittest.TestCase):
    """Tests for math functions."""

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed(self):
        """Test addition of mixed numbers."""
        self.assertEqual(add(-1, 1), 0)

    def test_divide_normal(self):
        """Test normal division."""
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """Test division by zero raises exception."""
        with self.assertRaises(ValueError):
            divide(10, 0)

# Run tests
if __name__ == '__main__':
    unittest.main()
```

### Running Tests

```bash
# Single file
python test_math.py

# With more details
python -m unittest test_math -v

# All tests in directory
python -m unittest discover

# Specific test
python -m unittest test_math.TestMathFunctions.test_add_positive_numbers
```

---

## ✓ Important Assertions

```python
import unittest

class TestAssertions(unittest.TestCase):

    # ═══════════════════════════════════════════════════════════════
    # EQUALITY
    # ═══════════════════════════════════════════════════════════════
    def test_equality(self):
        self.assertEqual(1 + 1, 2)           # Equal
        self.assertNotEqual(1 + 1, 3)        # Not equal

    # ═══════════════════════════════════════════════════════════════
    # TRUTH VALUES
    # ═══════════════════════════════════════════════════════════════
    def test_boolean(self):
        self.assertTrue(5 > 3)               # True
        self.assertFalse(5 < 3)              # False

    # ═══════════════════════════════════════════════════════════════
    # NONE
    # ═══════════════════════════════════════════════════════════════
    def test_none(self):
        self.assertIsNone(None)              # Is None
        self.assertIsNotNone("text")         # Is not None

    # ═══════════════════════════════════════════════════════════════
    # IDENTITY
    # ═══════════════════════════════════════════════════════════════
    def test_identity(self):
        a = [1, 2, 3]
        b = a                                # Same reference
        c = [1, 2, 3]                        # Same content, different reference
        self.assertIs(a, b)                  # Identical (same object)
        self.assertIsNot(a, c)               # Not identical

    # ═══════════════════════════════════════════════════════════════
    # CONTAINS / IN
    # ═══════════════════════════════════════════════════════════════
    def test_membership(self):
        self.assertIn(3, [1, 2, 3])          # Element in list
        self.assertNotIn(4, [1, 2, 3])       # Element not in list

    # ═══════════════════════════════════════════════════════════════
    # TYPES
    # ═══════════════════════════════════════════════════════════════
    def test_types(self):
        self.assertIsInstance([1, 2], list)  # Is of type
        self.assertNotIsInstance([1], dict)  # Not of type

    # ═══════════════════════════════════════════════════════════════
    # COMPARISONS
    # ═══════════════════════════════════════════════════════════════
    def test_comparisons(self):
        self.assertGreater(5, 3)             # >
        self.assertGreaterEqual(5, 5)        # >=
        self.assertLess(3, 5)                # <
        self.assertLessEqual(5, 5)           # <=

    # ═══════════════════════════════════════════════════════════════
    # FLOATS (with tolerance!)
    # ═══════════════════════════════════════════════════════════════
    def test_floats(self):
        # ❌ WRONG: Direct float comparisons
        # self.assertEqual(0.1 + 0.2, 0.3)  # Can fail!

        # ✅ CORRECT: With tolerance
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)

    # ═══════════════════════════════════════════════════════════════
    # EXCEPTIONS
    # ═══════════════════════════════════════════════════════════════
    def test_exceptions(self):
        def divide(a, b):
            if b == 0:
                raise ValueError("Division by zero!")
            return a / b

        # Check if exception is raised
        with self.assertRaises(ValueError):
            divide(1, 0)

        # With message check
        with self.assertRaisesRegex(ValueError, "zero"):
            divide(1, 0)

    # ═══════════════════════════════════════════════════════════════
    # STRINGS
    # ═══════════════════════════════════════════════════════════════
    def test_strings(self):
        self.assertRegex("hello world", r"hello.*")     # Regex match
        self.assertNotRegex("hello", r"\d+")            # No match
```

```
┌─────────────────────────────────────────────────────────────────┐
│                 ASSERTIONS OVERVIEW                              │
├──────────────────────────┬──────────────────────────────────────┤
│ assertEqual(a, b)        │ a == b                               │
│ assertNotEqual(a, b)     │ a != b                               │
│ assertTrue(x)            │ bool(x) is True                      │
│ assertFalse(x)           │ bool(x) is False                     │
│ assertIs(a, b)           │ a is b                               │
│ assertIsNone(x)          │ x is None                            │
│ assertIn(a, b)           │ a in b                               │
│ assertIsInstance(a, b)   │ isinstance(a, b)                     │
│ assertRaises(exc)        │ Exception is raised                  │
│ assertAlmostEqual(a, b)  │ For float comparisons                │
└──────────────────────────┴──────────────────────────────────────┘
```

---

## 🔧 setUp and tearDown

For setup/cleanup before/after tests:

```python
import unittest
import tempfile
import os

class TestWithSetup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Once before ALL tests of the class."""
        print(">>> Class setup (once)")
        cls.shared_resource = "Shared Data"

    @classmethod
    def tearDownClass(cls):
        """Once after ALL tests of the class."""
        print(">>> Class teardown (once)")

    def setUp(self):
        """Before EACH individual test."""
        print("  > Test setup")
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(b"test data")
        self.temp_file.close()

    def tearDown(self):
        """After EACH individual test."""
        print("  > Test teardown")
        os.unlink(self.temp_file.name)

    def test_one(self):
        """First test."""
        print("    Running test_one")
        self.assertTrue(os.path.exists(self.temp_file.name))

    def test_two(self):
        """Second test."""
        print("    Running test_two")
        self.assertEqual(self.shared_resource, "Shared Data")

# Output:
# >>> Class setup (once)
#   > Test setup
#     Running test_one
#   > Test teardown
#   > Test setup
#     Running test_two
#   > Test teardown
# >>> Class teardown (once)
```

```
┌─────────────────────────────────────────────────────────────────┐
│                   SETUP/TEARDOWN FLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   setUpClass()                                                   │
│       │                                                          │
│       ├──→ setUp() → test_1() → tearDown()                      │
│       │                                                          │
│       ├──→ setUp() → test_2() → tearDown()                      │
│       │                                                          │
│       └──→ setUp() → test_3() → tearDown()                      │
│       │                                                          │
│   tearDownClass()                                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🚀 pytest - The Modern Standard

pytest is simpler and more powerful than unittest:

```bash
pip install pytest
```

### Simple Tests with pytest

```python
# test_example.py

def add(a, b):
    return a + b

# Simple functions - no class needed!
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_mixed():
    assert add(-1, 1) == 0

# With helpful error message
def test_with_message():
    result = add(2, 2)
    assert result == 4, f"Expected 4, got {result}"
```

### Running pytest

```bash
# All tests
pytest

# Verbose
pytest -v

# Specific file
pytest test_example.py

# Specific test
pytest test_example.py::test_add_positive

# With print output
pytest -s

# Stop at first failure
pytest -x

# Show slowest tests
pytest --durations=10
```

---

## 📝 pytest Fixtures

Fixtures replace setUp/tearDown:

```python
import pytest
import tempfile
import os

# Fixture as function
@pytest.fixture
def temp_file():
    """Creates temporary file for tests."""
    # Setup
    f = tempfile.NamedTemporaryFile(mode='w', delete=False)
    f.write("test content")
    f.close()

    yield f.name  # Gives value to test

    # Teardown
    os.unlink(f.name)

# Test uses fixture as parameter
def test_read_temp_file(temp_file):
    with open(temp_file) as f:
        assert f.read() == "test content"

def test_file_exists(temp_file):
    assert os.path.exists(temp_file)

# Fixture with scope
@pytest.fixture(scope="module")  # Once per module
def database_connection():
    """Expensive resource, create only once."""
    conn = create_db_connection()
    yield conn
    conn.close()

# Scopes: function (default), class, module, package, session
```

---

## 🎯 Parametrized Tests

Run the same test with different data:

### With pytest

```python
import pytest

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Parametrized tests
@pytest.mark.parametrize("input,expected", [
    ("radar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("", True),
    ("a", True),
])
def test_is_palindrome(input, expected):
    assert is_palindrome(input) == expected

# Combine multiple parameters
@pytest.mark.parametrize("a", [1, 2, 3])
@pytest.mark.parametrize("b", [10, 20])
def test_multiply(a, b):
    # Runs 6x: (1,10), (1,20), (2,10), (2,20), (3,10), (3,20)
    assert a * b == a * b
```

### With unittest

```python
import unittest

class TestPalindrome(unittest.TestCase):
    def test_palindromes(self):
        test_cases = [
            ("radar", True),
            ("hello", False),
            ("madam", True),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input=input_str):
                self.assertEqual(is_palindrome(input_str), expected)
```

---

## 🎭 Mocking

Fake external dependencies:

```python
from unittest.mock import Mock, patch, MagicMock
import unittest

# Example: Function that calls API
def get_user_name(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()['name']

class TestWithMocking(unittest.TestCase):

    # Mock with patch (recommended)
    @patch('requests.get')
    def test_get_user_name(self, mock_get):
        # Configure mock
        mock_response = Mock()
        mock_response.json.return_value = {'name': 'Alice'}
        mock_get.return_value = mock_response

        # Run test
        result = get_user_name(123)

        # Assertions
        self.assertEqual(result, 'Alice')
        mock_get.assert_called_once_with("https://api.example.com/users/123")

    # Patch as context manager
    def test_with_context_manager(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {'name': 'Bob'}
            result = get_user_name(456)
            self.assertEqual(result, 'Bob')

# Create mock objects directly
def test_mock_basics():
    mock = Mock()

    # Attributes created automatically
    mock.some_method.return_value = 42
    assert mock.some_method() == 42

    # Track calls
    mock.another_method("arg1", "arg2")
    mock.another_method.assert_called_with("arg1", "arg2")
    assert mock.another_method.call_count == 1
```

```
┌─────────────────────────────────────────────────────────────────┐
│                    WHEN TO USE MOCKING?                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ✅ External APIs            Mock network calls                 │
│  ✅ Databases                Isolate DB access                  │
│  ✅ File system              Control file I/O                   │
│  ✅ Time-dependent code      Mock datetime.now()                │
│  ✅ Slow operations          Make tests faster                  │
│                                                                  │
│  ❌ Own logic mocking        Better refactor!                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📂 Test Organization

```
my_project/
├── src/
│   └── my_module/
│       ├── __init__.py
│       ├── calculator.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py         # Shared pytest fixtures
│   ├── test_calculator.py
│   └── test_utils.py
├── pytest.ini              # pytest configuration
└── requirements-dev.txt    # Test dependencies
```

### conftest.py (Shared Fixtures)

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_data():
    """Available to all tests."""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def empty_list():
    return []
```

### pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --tb=short
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Make tests dependent on other tests
class TestBad(unittest.TestCase):
    counter = 0

    def test_1_increment(self):
        TestBad.counter += 1

    def test_2_check(self):
        # Depends on test_1! Test order not guaranteed!
        self.assertEqual(TestBad.counter, 1)

# ✅ CORRECT: Each test independent
class TestGood(unittest.TestCase):
    def setUp(self):
        self.counter = 0

    def test_increment(self):
        self.counter += 1
        self.assertEqual(self.counter, 1)

# ❌ WRONG: Use external resources directly
def test_bad_external():
    result = requests.get("https://real-api.com")  # Slow, unreliable!

# ✅ CORRECT: Mock
@patch('requests.get')
def test_good_external(mock_get):
    mock_get.return_value.json.return_value = {"data": "mocked"}
    # ...

# ❌ WRONG: Too much in one test
def test_everything():
    # Tests add, subtract, multiply, divide...
    assert add(1, 1) == 2
    assert subtract(5, 3) == 2
    assert multiply(2, 3) == 6
    assert divide(10, 2) == 5

# ✅ CORRECT: One concept per test
def test_add():
    assert add(1, 1) == 2

def test_subtract():
    assert subtract(5, 3) == 2
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Each test independent | Tests dependent on each other |
| Clear test names (`test_add_positive_numbers`) | Generic names (`test_1`) |
| AAA-Pattern (Arrange-Act-Assert) | Everything mixed together |
| Mock external dependencies | Use real APIs in tests |
| Test edge cases (0, None, empty list) | Only test happy path |
| pytest for new projects | unittest for modern tests |

### AAA-Pattern

```python
def test_user_creation():
    # Arrange - Setup
    name = "Alice"
    email = "alice@example.com"

    # Act - Execute
    user = create_user(name, email)

    # Assert - Check
    assert user.name == name
    assert user.email == email
    assert user.id is not None
```

---

## 🎯 Exam Checklist

- [ ] `unittest.TestCase` and assertions (assertEqual, assertTrue, assertRaises)
- [ ] `setUp()` / `tearDown()` vs `setUpClass()` / `tearDownClass()`
- [ ] pytest: Simple functions with `assert`
- [ ] `@pytest.fixture` for setup/teardown
- [ ] `@pytest.mark.parametrize` for multiple test cases
- [ ] `unittest.mock.patch` for mocking
- [ ] `assertAlmostEqual()` for float comparisons
- [ ] `with self.assertRaises(Exception):` syntax

---

[[20_Logging|← Logging]] | [[00_Index|Index]] | [[22_Code_Quality|Code Quality →]]
