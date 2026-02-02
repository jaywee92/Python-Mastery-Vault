---
title: Python Basics - Quick Examples
tags: [python, cheatsheet, examples, quick-reference, patterns]
category: reference
type: quick-reference
---

# 🚀 Python Basics - Quick Examples

**Beginner-friendly examples from Python Crash Course**

[[00_Index|← Back to Index]]

---

## 💡 About This File

This file contains **beginner-friendly examples** extracted from the Python Crash Course Cheat Sheet. These complement the detailed topics with simple, clear examples perfect for quick reference.

---

## 1. Hello World & Variables

```python
# The classic
print("Hello world!")

# With a variable
msg = "Hello world!"
print(msg)

# F-strings (modern way!)
first_name = "albert"
last_name = "einstein"
full_name = f"{first_name} {last_name}"
print(full_name)  # albert einstein
```

---

## 2. Lists - Quick Examples

```python
# Create a list
bikes = ["trek", "redline", "giant"]

# Access elements
first_bike = bikes[0]      # "trek"
last_bike = bikes[-1]      # "giant" (negative indexing!)

# Loop through
for bike in bikes:
    print(bike)

# Start with empty list
bikes = []
bikes.append("trek")
bikes.append("redline")
print(bikes)  # ['trek', 'redline']

# Slicing
print(bikes[0:2])   # First 2 items
print(bikes[:2])    # Same thing
print(bikes[-2:])   # Last 2 items
```

**💡 Key Pattern:** Negative indexing (`-1` = last) is super useful!

---

## 3. Tuples - Simple Examples

```python
# Tuples are immutable (can't change)
dimensions = (1920, 1080)

# Access elements
width = dimensions[0]
height = dimensions[1]
print(f"Width: {width}, Height: {height}")

# Multiple tuples
resolutions = [(1920, 1080), (2560, 1440), (3840, 2160)]

# Loop through
for resolution in resolutions:
    print(resolution)
```

**💡 Use tuples when data shouldn't change!**

---

## 4. If Statements - Clear Examples

```python
# Comparison operators
x = 42
print(x == 42)   # True
print(x != 42)   # False
print(x > 40)    # True
print(x >= 42)   # True

# With lists
bikes = ["trek", "redline", "giant"]
print('trek' in bikes)         # True
print('surly' not in bikes)    # True

# Boolean values
game_active = True
can_edit = False

# If-elif-else chain (common pattern)
age = 12
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
elif age < 65:
    ticket_price = 40
else:
    ticket_price = 15

print(f"Your cost is ${ticket_price}.")
```

**💡 Remember:** `in` and `not in` are very readable!

---

## 5. Dictionaries - Practical Examples

```python
# Simple dictionary
alien = {"color": "green", "points": 5}

# Access value
print(alien['color'])  # "green"

# Add new key-value pair
alien["x_position"] = 0
alien["y_position"] = 25

# Loop through key-value pairs
fav_numbers = {"eric": 7, "ever": 4, "erin": 47}

for name, number in fav_numbers.items():
    print(f"{name} loves {number}.")

# Loop through keys only
for name in fav_numbers.keys():
    print(name)

# Loop through values only
for number in fav_numbers.values():
    print(number)

# Using .get() with default value (safe!)
alien_color = alien.get("color")
alien_points = alien.get("points", 0)     # 5
alien_speed = alien.get("speed", "slow")  # "slow" (default)
```

**💡 Always use `.get()` to avoid KeyError!**

### Nested Dictionaries

```python
# List of dictionaries
users = [
    {"last": "fermi", "first": "enrico", "username": "efermi"},
    {"last": "curie", "first": "marie", "username": "mcurie"},
]

for user in users:
    print(f"User: {user['username']}")
    print(f"  Name: {user['first']} {user['last']}")

# Dictionary of dictionaries
users_dict = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users_dict.items():
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]
    print(f"{username}: {full_name.title()} in {location.title()}")
```

---

## 6. User Input

```python
# Get text input
name = input("What's your name? ")
print(f"Hello, {name}!")

# Get number input (must convert!)
age = input("How old are you? ")
age = int(age)  # Convert string to integer

if age >= 18:
    print("You can vote!")

# Float conversion
pi = input("What's the value of pi? ")
pi = float(pi)  # Convert to decimal
```

**💡 Remember:** `input()` always returns a string!

---

## 7. While Loops - Common Patterns

```python
# Count to 5
current = 1
while current <= 5:
    print(current)
    current += 1

# While True with break (common!)
prompt = "Enter 'quit' to exit: "
while True:
    message = input(prompt)
    if message == 'quit':
        break
    print(f"You entered: {message}")

# With continue (skip iteration)
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(count)
```

**💡 Pattern:** `while True` with `break` is very common!

---

## 8. Functions - Essential Patterns

```python
# Basic function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# With parameter
def greet(name):
    """Display personalized greeting."""
    print(f"Hello, {name}!")

greet("Alice")

# With return value
def add(a, b):
    """Return sum of two numbers."""
    return a + b

result = add(5, 3)
print(result)  # 8

# With default parameter
def greet(name='World'):
    """Greet with default name."""
    print(f"Hello, {name}!")

greet()          # Hello, World!
greet("Alice")   # Hello, Alice!

# With *args (variable arguments)
def make_pizza(size, *toppings):
    """Make pizza with any number of toppings."""
    print(f"\nMaking {size}-inch pizza with:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, 'mushrooms', 'peppers', 'olives')

# With **kwargs (keyword arguments)
def build_profile(first, last, **user_info):
    """Build a profile dictionary."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

profile = build_profile('albert', 'einstein',
                       location='princeton',
                       field='physics')
print(profile)
```

**💡 Key Patterns:**
- Default params: `def func(param='default')`
- Variable args: `*args` for tuples, `**kwargs` for dicts

---

## 9. Classes - Getting Started

```python
# Simple class
class Dog:
    """A simple dog class."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate dog sitting."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over."""
        print(f"{self.name} rolled over!")

# Create instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

# Use methods
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

# Inheritance example
class Car:
    """A simple car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def describe(self):
        """Return formatted description."""
        return f"{self.year} {self.make} {self.model}"

class ElectricCar(Car):
    """Electric car, inherits from Car."""
    
    def __init__(self, make, model, year):
        """Initialize parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75  # New attribute
    
    def describe_battery(self):
        """Describe the battery."""
        print(f"Battery size: {self.battery_size}-kWh")

# Use inherited class
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.describe())
my_tesla.describe_battery()
```

**💡 Pattern:** `super().__init__()` calls parent's `__init__`

---

## 10. Files - Quick Reference

```python
# Read entire file
with open('file.txt', 'r') as f:
    contents = f.read()
    print(contents)

# Read line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Read all lines into list
with open('file.txt', 'r') as f:
    lines = f.readlines()

# Write to file
with open('output.txt', 'w') as f:
    f.write("Hello, file!\n")
    f.write("Second line\n")

# Append to file
with open('log.txt', 'a') as f:
    f.write("New log entry\n")
```

**💡 Always use `with` - file closes automatically!**

---

## 11. JSON - Data Storage

```python
import json

# Save data to JSON file
user_data = {
    "first_name": "Albert",
    "last_name": "Einstein",
    "age": 76
}

with open('user.json', 'w') as f:
    json.dump(user_data, f)

# Load data from JSON file
with open('user.json', 'r') as f:
    loaded_data = json.load(f)
    print(loaded_data)

# Convert to/from strings
json_string = json.dumps(user_data)  # Dict → String
back_to_dict = json.loads(json_string)  # String → Dict
```

**💡 Remember:**
- `dump`/`load` = files
- `dumps`/`loads` = strings

---

## 12. Exceptions - Handle Errors

```python
# Basic try-except
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Catch multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Can't divide by zero!")

# try-except-else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Result: {result}")  # Runs if no exception

# try-except-finally
try:
    f = open('file.txt')
    contents = f.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This always runs!")
```

**💡 Pattern:** Use `else` for code that runs only if no exception

---

## 13. Testing - Assert Basics

```python
# Simple function to test
def get_full_name(first, last):
    """Return full name."""
    return f"{first.title()} {last.title()}"

# Test with assert
def test_first_last():
    """Test names like John Doe."""
    full_name = get_full_name("john", "doe")
    assert full_name == "John Doe"
    print("✓ Test passed!")

# Run test
test_first_last()

# Test a class
class Account:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

def test_deposit():
    """Test deposit works."""
    account = Account()
    account.deposit(100)
    assert account.balance == 100
    print("✓ Deposit test passed!")

test_deposit()
```

---

## 14. Advanced - Quick Patterns

### List Comprehensions
```python
# Basic
squares = [x**2 for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]

# Convert to uppercase
names = ["kai", "abe", "ada"]
upper_names = [name.upper() for name in names]
# ['KAI', 'ABE', 'ADA']
```

### Dict Comprehensions
```python
# Basic
squares_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Using zip
names = ["kai", "abe", "ada"]
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
# {'kai': 25, 'abe': 30, 'ada': 35}
```

### Enumerate & Zip
```python
# Enumerate - get index and value
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")
# 0: Alice
# 1: Bob
# 2: Charlie

# Zip - combine lists
names = ["Alice", "Bob"]
ages = [25, 30]
cities = ["NYC", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")
```

### Sets
```python
# Create set (unordered, unique)
fruits = {"apple", "banana", "cherry", "apple"}
# Duplicates removed automatically!

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)  # Union: {1,2,3,4,5,6}
print(set1 & set2)  # Intersection: {3,4}
print(set1 - set2)  # Difference: {1,2}
print(set1 ^ set2)  # Symmetric diff: {1,2,5,6}
```

---

## 🎯 Quick Tips

1. **F-strings** are the modern way: `f"Hello {name}"`
2. **Negative indexing** is handy: `list[-1]` = last item
3. **`.get()` for dicts** prevents errors: `dict.get('key', default)`
4. **`with` for files** always: auto-closes the file
5. **List comprehensions** are Pythonic: `[x*2 for x in list]`
6. **`enumerate()`** when you need index: `for i, val in enumerate(list)`
7. **`*args` and `**kwargs`** for flexible functions
8. **Always use `try-except`** for user input and files

---

## 🔗 Related Topics

- [[01_Variables_and_Strings_Advanced|Variables & Strings (detailed)]]
- [[02_Lists_Deep_Dive|Lists (comprehensive)]]
- [[04_Dictionaries_Mastery|Dictionaries (advanced)]]
- [[08_Functions|Functions (deep dive)]]
- [[11_Classes_and_OOP|Classes (detailed)]]

---

[[00_Index|← Back to Index]]

*Quick examples for rapid reference - see individual topics for deeper explanations!*
