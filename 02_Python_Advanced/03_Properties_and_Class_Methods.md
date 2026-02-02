---
title: Properties and Class Methods
tags: [python, oop, properties, classmethod, staticmethod, decorators, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# 🏠 Properties and Class Methods

[[00_Index|← Back to Index]] | [[11_A_OOP_Visual_Guide|OOP Visual Guide →]]

> **Control attribute access and define methods at class level**

---

## 🎯 Overview: Three Method Types

| Decorator | First Argument | Access to | Usage |
|-----------|-----------------|-------------|------------|
| (none) | `self` | Instance & Class | Normal methods |
| `@classmethod` | `cls` | Class only | Factory methods, class attributes |
| `@staticmethod` | (none) | Nothing | Utility functions |

```python
class Demo:
    class_attr = "shared"

    def instance_method(self):
        """Has access to self (instance) and self.__class__ (class)"""
        return f"Instance: {self}, Class: {self.__class__.class_attr}"

    @classmethod
    def class_method(cls):
        """Has access to cls (class), but not instance"""
        return f"Class: {cls}, Attr: {cls.class_attr}"

    @staticmethod
    def static_method(x, y):
        """No access to class or instance"""
        return x + y


# Calling
obj = Demo()
print(obj.instance_method())  # Requires instance
print(Demo.class_method())    # Called on class
print(obj.class_method())     # Also possible on instance
print(Demo.static_method(2, 3))  # Like normal function
```

---

## 🏷️ @property - Getters and Setters

### Why Properties?

Properties allow **controlled access** to attributes while looking like normal attributes.

```python
# ❌ WITHOUT Property - direct access, no control
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Can be negative!

c = Circle(-5)  # Allowed, but nonsensical!


# ✅ WITH Property - controlled access
class Circle:
    def __init__(self, radius):
        self._radius = None  # "Private" attribute
        self.radius = radius  # Uses the setter!

    @property
    def radius(self):
        """Getter - called when: circle.radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter - called when: circle.radius = value"""
        if value < 0:
            raise ValueError("Radius must be positive!")
        self._radius = value

    @radius.deleter
    def radius(self):
        """Deleter - called when: del circle.radius"""
        print("Radius is being deleted")
        self._radius = None


c = Circle(5)
print(c.radius)    # 5 (calls getter)

c.radius = 10      # Calls setter
print(c.radius)    # 10

# c.radius = -5    # ValueError: Radius must be positive!

del c.radius       # "Radius is being deleted"
```

### Computed Properties (Read-Only)

```python
import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive!")
        self._radius = value

    @property
    def diameter(self):
        """Computed property - calculated, not stored"""
        return self._radius * 2

    @property
    def area(self):
        """Read-Only property (no setter defined)"""
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        """Circumference"""
        return 2 * math.pi * self._radius


c = Circle(5)
print(f"Radius: {c.radius}")           # 5
print(f"Diameter: {c.diameter}")    # 10
print(f"Area: {c.area:.2f}")         # 78.54
print(f"Circumference: {c.circumference:.2f}")  # 31.42

# c.area = 100  # ❌ AttributeError: can't set attribute
```

### Property with Dependent Updates

```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @area.setter
    def area(self, value):
        """Set area, keep aspect ratio"""
        ratio = self._width / self._height
        self._height = (value / ratio) ** 0.5
        self._width = self._height * ratio


rect = Rectangle(4, 3)
print(f"Area: {rect.area}")  # 12

rect.area = 48  # Doubles both sides
print(f"Width: {rect.width:.2f}, Height: {rect.height:.2f}")  # 8.0, 6.0
```

---

## 🏭 @classmethod - Class Methods

### Factory Methods

The most common use case: **Alternative constructors**.

```python
from datetime import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor: creates Person from birth year"""
        age = datetime.now().year - birth_year
        return cls(name, age)  # Use cls instead of Person for inheritance!

    @classmethod
    def from_dict(cls, data):
        """Creates Person from dictionary"""
        return cls(data['name'], data['age'])

    @classmethod
    def from_string(cls, person_str):
        """Creates Person from string 'name,age'"""
        name, age = person_str.split(',')
        return cls(name, int(age))

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


# Different ways to create Person
p1 = Person("Alice", 30)
p2 = Person.from_birth_year("Bob", 1990)
p3 = Person.from_dict({'name': 'Charlie', 'age': 25})
p4 = Person.from_string("Diana,28")

print(p1)  # Person('Alice', 30)
print(p2)  # Person('Bob', 35) (depending on year)
print(p3)  # Person('Charlie', 25)
print(p4)  # Person('Diana', 28)
```

### Inheritance with @classmethod

```python
class Animal:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create_baby(cls, name):
        """cls is the CALLING class, not Animal!"""
        return cls(f"Baby {name}")


class Dog(Animal):
    def bark(self):
        return "Woof!"


class Cat(Animal):
    def meow(self):
        return "Meow!"


# cls is Dog, so Dog.__init__ is called
puppy = Dog.create_baby("Buddy")
print(type(puppy))  # <class 'Dog'>
print(puppy.bark()) # Woof!

# cls is Cat
kitten = Cat.create_baby("Whiskers")
print(type(kitten)) # <class 'Cat'>
print(kitten.meow()) # Meow!
```

### Managing Class Attributes

```python
class Counter:
    _count = 0  # Class attribute

    def __init__(self):
        Counter._count += 1
        self.id = Counter._count

    @classmethod
    def get_count(cls):
        """Returns number of created instances"""
        return cls._count

    @classmethod
    def reset_count(cls):
        """Resets counter"""
        cls._count = 0


c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.get_count())  # 3
print(c1.id, c2.id, c3.id)  # 1 2 3

Counter.reset_count()
print(Counter.get_count())  # 0
```

---

## ⚡ @staticmethod - Static Methods

### Utility Functions within the Class

```python
class MathUtils:
    """Collection of math utility functions"""

    @staticmethod
    def is_prime(n):
        """Checks if n is a prime number"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorial(n):
        """Calculates n!"""
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def gcd(a, b):
        """Greatest common divisor"""
        while b:
            a, b = b, a % b
        return a


# Call without instance
print(MathUtils.is_prime(17))    # True
print(MathUtils.factorial(5))    # 120
print(MathUtils.gcd(48, 18))     # 6

# Also possible on instance (but unusual)
utils = MathUtils()
print(utils.is_prime(7))  # True
```

### When to use @staticmethod instead of a function?

```python
class EmailValidator:
    # Static method when logically belongs to the class
    @staticmethod
    def is_valid_email(email):
        """Logically belongs to EmailValidator"""
        import re
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))

    def __init__(self, email):
        if not self.is_valid_email(email):
            raise ValueError(f"Invalid email: {email}")
        self.email = email


# Validation before instantiation
if EmailValidator.is_valid_email("test@example.com"):
    validator = EmailValidator("test@example.com")
```

---

## 🔄 Comparison: When to Use Which Method?

```python
class BankAccount:
    _interest_rate = 0.02  # Class attribute (same for all)

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # INSTANCE METHOD: Needs self (instance data)
    def deposit(self, amount):
        """Needs access to self.balance"""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Needs access to self.balance"""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    # PROPERTY: Calculated from instance data
    @property
    def annual_interest(self):
        """Needs self.balance AND cls._interest_rate"""
        return self.balance * self._interest_rate

    # CLASS METHOD: Modifies class state
    @classmethod
    def set_interest_rate(cls, rate):
        """Changes interest rate for ALL accounts"""
        if not 0 <= rate <= 1:
            raise ValueError("Rate must be between 0 and 1")
        cls._interest_rate = rate

    @classmethod
    def get_interest_rate(cls):
        """Reads class attribute"""
        return cls._interest_rate

    # STATIC METHOD: Needs neither self nor cls
    @staticmethod
    def validate_amount(amount):
        """Pure validation, no instance/class needed"""
        return isinstance(amount, (int, float)) and amount > 0


# Usage
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)

print(acc1.annual_interest)  # 20.0 (1000 * 0.02)
print(acc2.annual_interest)  # 40.0 (2000 * 0.02)

BankAccount.set_interest_rate(0.05)  # Changes for ALL

print(acc1.annual_interest)  # 50.0 (1000 * 0.05)
print(acc2.annual_interest)  # 100.0 (2000 * 0.05)

print(BankAccount.validate_amount(100))  # True
print(BankAccount.validate_amount(-50))  # False
```

---

## 📋 Decision Tree

```
Does the method need access to instance data (self)?
├─ YES → Instance Method
│       Should it look like an attribute?
│       ├─ YES → @property
│       └─ NO → Normal method
│
└─ NO → Does it need access to class data (cls)?
        ├─ YES → @classmethod
        │       - Factory methods
        │       - Modify class attributes
        │       - Alternative constructors
        │
        └─ NO → @staticmethod
                - Utility functions
                - Validation
                - Stateless calculations
```

---

## 🏗️ Practical Example: Complete Class

```python
from datetime import datetime
import json

class Product:
    """Product class with all method types"""

    _tax_rate = 0.19  # Class attribute

    def __init__(self, name, price, quantity=0):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._created_at = datetime.now()

    # === PROPERTIES ===

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not self.validate_price(value):
            raise ValueError("Price must be positive")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = value

    @property
    def price_with_tax(self):
        """Computed property"""
        return self._price * (1 + self._tax_rate)

    @property
    def total_value(self):
        """Total value in stock"""
        return self.price_with_tax * self._quantity

    @property
    def is_in_stock(self):
        return self._quantity > 0

    # === INSTANCE METHODS ===

    def add_stock(self, amount):
        """Adds stock quantity"""
        self._quantity += amount

    def remove_stock(self, amount):
        """Removes stock quantity"""
        if amount > self._quantity:
            raise ValueError("Not enough in stock")
        self._quantity -= amount

    def to_dict(self):
        """Converts to dictionary"""
        return {
            'name': self._name,
            'price': self._price,
            'quantity': self._quantity
        }

    def __repr__(self):
        return f"Product('{self._name}', {self._price}, {self._quantity})"

    # === CLASS METHODS ===

    @classmethod
    def from_dict(cls, data):
        """Factory: Creates Product from dictionary"""
        return cls(
            name=data['name'],
            price=data['price'],
            quantity=data.get('quantity', 0)
        )

    @classmethod
    def from_json(cls, json_str):
        """Factory: Creates Product from JSON"""
        data = json.loads(json_str)
        return cls.from_dict(data)

    @classmethod
    def set_tax_rate(cls, rate):
        """Sets tax rate for all products"""
        if not 0 <= rate <= 1:
            raise ValueError("Tax rate must be between 0 and 1")
        cls._tax_rate = rate

    @classmethod
    def get_tax_rate(cls):
        return cls._tax_rate

    # === STATIC METHODS ===

    @staticmethod
    def validate_price(price):
        """Validates price value"""
        return isinstance(price, (int, float)) and price > 0

    @staticmethod
    def format_currency(amount, currency="€"):
        """Formats amount as currency"""
        return f"{amount:.2f} {currency}"


# === USAGE ===

# Create
laptop = Product("Laptop", 999.99, 10)
phone = Product.from_dict({'name': 'Phone', 'price': 599.99, 'quantity': 25})
tablet = Product.from_json('{"name": "Tablet", "price": 449.99}')

# Use properties
print(laptop.name)           # Laptop
print(laptop.price_with_tax) # 1189.99 (with 19% VAT)
print(laptop.is_in_stock)    # True

# Change price (via setter with validation)
laptop.price = 899.99
# laptop.price = -100  # ValueError!

# Change class attribute
Product.set_tax_rate(0.07)  # Reduced VAT
print(laptop.price_with_tax) # 962.99 (with 7% VAT)

# Static method
print(Product.format_currency(laptop.price_with_tax))  # 962.99 €
print(Product.validate_price(100))  # True
```

---

## ⚠️ Common Pitfalls

### 1. Property without Underscore

```python
# ❌ WRONG - Recursion!
class Bad:
    @property
    def value(self):
        return self.value  # Calls itself!

# ✅ CORRECT - Underscore for internal variable
class Good:
    @property
    def value(self):
        return self._value  # Different name!
```

### 2. Confusing cls and self

```python
class Demo:
    class_var = 10

    @classmethod
    def wrong(cls):
        # ❌ self doesn't exist here!
        return self.class_var

    @classmethod
    def correct(cls):
        # ✅ Use cls
        return cls.class_var
```

### 3. Using @staticmethod where @classmethod is needed

```python
class Parent:
    @staticmethod
    def create():
        return Parent()  # Always Parent!

class Child(Parent):
    pass

# child = Child.create()  # Creates Parent, not Child!

# ✅ BETTER: @classmethod
class Parent:
    @classmethod
    def create(cls):
        return cls()  # Creates the correct class
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Use `@property` for computed attributes | Java-style getters/setters |
| Use `@classmethod` for alternative constructors | `__init__` with many parameters |
| Use `@staticmethod` for utility functions | Methods without self/cls as normal |
| Use `_underscore` for "private" attributes | Same name for property and attribute |
| Validate in setter | Forget validation |

---

## 🎯 Exam Checklist

- [ ] `@property` syntax and usage
- [ ] Define getters, setters, deleters
- [ ] Difference between `@classmethod` and `@staticmethod`
- [ ] Factory methods with `@classmethod`
- [ ] When to use which decorator
- [ ] Explain `cls` vs `self`

---

[[13_Magic_Methods|← Magic Methods]] | [[00_Index|Index]] | [[15_File_IO|File IO →]]
