---
title: Functions
category: functions
tags: ['python', 'functions', 'def', 'core', 'basics']
created: 2026-01-27
type: topic
---

# Functions

[[00_Index|← Back to Index]]

> **Reusable blocks of code**

---

## 📦 What is a Function?

A **function** is a reusable block of code that performs a specific task.

**Benefits:**
- ✓ Code reusability
- ✓ Better organization
- ✓ Easier testing
- ✓ Reduced repetition

---

## 🏗️ Defining Functions

### Without Parameters

```python
# Define function
def generate_full_name():
    first_name = 'John'
    last_name = 'Doe'
    full_name = first_name + ' ' + last_name
    print(full_name)

# Call function
generate_full_name()  # John Doe
```

### With Return Value

```python
def generate_full_name():
    first_name = 'John'
    last_name = 'Doe'
    return first_name + ' ' + last_name

# Call and use return value
name = generate_full_name()
print(name)  # John Doe

def add_two_numbers():
    return 2 + 3

print(add_two_numbers())  # 5
```

---

## 📥 Parameters and Arguments

### Single Parameter

```python
def greet(name):
    return f'{name}, welcome to Python!'

print(greet('Alice'))  # Alice, welcome to Python!

def add_ten(num):
    return num + 10

print(add_ten(90))  # 100

def square_number(x):
    return x * x

print(square_number(5))  # 25
```

### Multiple Parameters

```python
def add_two_numbers(num1, num2):
    return num1 + num2

print(add_two_numbers(5, 3))  # 8

def full_name(first, last):
    return f'{first} {last}'

print(full_name('John', 'Doe'))  # John Doe

def calculate_age(current_year, birth_year):
    return current_year - birth_year

print(calculate_age(2024, 1990))  # 34
```

---

## 🎯 Default Parameters

```python
def greet(name='Guest'):
    return f'Hello, {name}!'

print(greet())         # Hello, Guest!
print(greet('Alice'))  # Hello, Alice!

def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9 (3^2)
print(power(3, 3))   # 27 (3^3)

def calculate_tax(amount, rate=0.1):
    return amount * rate

print(calculate_tax(100))      # 10.0
print(calculate_tax(100, 0.2)) # 20.0
```

---

## 🌟 *args - Variable Arguments

```python
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))         # 6
print(sum_all(1, 2, 3, 4, 5))   # 15

def print_items(*items):
    for item in items:
        print(item)

print_items('apple', 'banana', 'orange')
```

---

## 🔑 **kwargs - Keyword Arguments

```python
def print_info(**info):
    for key, value in info.items():
        print(f'{key}: {value}')

print_info(name='John', age=30, city='NYC')
# name: John
# age: 30
# city: NYC

def create_person(**person):
    return person

person = create_person(
    first_name='Alice',
    last_name='Smith',
    age=25
)
print(person)
# {'first_name': 'Alice', 'last_name': 'Smith', 'age': 25}
```

---

## 🎨 Combining Everything

```python
def complex_func(required, optional='default', *args, key=None, **kwargs):
    print(f'Required: {required}')
    print(f'Optional: {optional}')
    print(f'Args: {args}')
    print(f'Key: {key}')
    print(f'Kwargs: {kwargs}')

complex_func(
    'value1',
    'value2',
    'arg1', 'arg2',
    key='special',
    extra1='data1',
    extra2='data2'
)
```

---

## 🔄 Return Values

### Return Single Value

```python
def square(x):
    return x * x

result = square(5)
print(result)  # 25
```

### Return Multiple Values

```python
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 2, 3, 4, 5])
print(f'Min: {minimum}, Max: {maximum}')  # Min: 1, Max: 5
```

### Early Return

```python
def is_even(num):
    if num % 2 == 0:
        return True
    return False

print(is_even(4))  # True
print(is_even(3))  # False
```

---

## 💡 Practical Examples

### Calculate Area

```python
def area_of_circle(radius):
    PI = 3.14159
    return PI * radius ** 2

print(area_of_circle(5))   # 78.53975
print(area_of_circle(10))  # 314.159
```

### Sum Range

```python
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(sum_of_numbers(10))   # 55
print(sum_of_numbers(100))  # 5050
```

### Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(celsius_to_fahrenheit(0))    # 32.0
print(fahrenheit_to_celsius(32))   # 0.0
```

### Validate Input

```python
def is_valid_email(email):
    return '@' in email and '.' in email

print(is_valid_email('user@example.com'))  # True
print(is_valid_email('invalid'))            # False
```

---

## 📚 Function Documentation

```python
def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index.
    
    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in meters
    
    Returns:
    float: BMI value
    """
    return weight / (height ** 2)

# Access docstring
print(calculate_bmi.__doc__)

# Use function
print(calculate_bmi(70, 1.75))  # 22.86
```

---

## ✅ Best Practices

### 1. Use Descriptive Names

```python
# Good
def calculate_total_price(price, tax_rate):
    return price * (1 + tax_rate)

# Bad
def calc(p, t):
    return p * (1 + t)
```

### 2. Keep Functions Small

```python
# Good - single responsibility
def validate_email(email):
    return '@' in email

def send_email(to, subject, body):
    if validate_email(to):
        # send email
        pass
```

### 3. Use Type Hints (Optional)

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f'Hello, {name}!'
```

### 4. Avoid Side Effects

```python
# Bad - modifies global state
total = 0
def add_to_total(value):
    global total
    total += value

# Good - pure function
def add(a, b):
    return a + b
```

---

## 🎓 Summary

**Functions:**
- Defined with `def` keyword
- Can have parameters
- Can return values
- Support *args and **kwargs
- Should be small and focused

**Key Concepts:**
- Parameters vs Arguments
- Default values
- Return values
- Documentation

---

## 🔗 Related Topics

- [[09_Lambda_and_Builtins|Lambda Functions]]
- [[10_Scope_and_Closures|Scope]]

---

[[00_Index|← Back to Index]]

*Functions make code reusable! 🔄*

✅ Use descriptive names
✅ Keep functions small
✅ Avoid mutable defaults

---

[[00_Index|← Back to Index]]
