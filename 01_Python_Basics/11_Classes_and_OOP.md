---
title: Classes and OOP
tags: [python, oop, classes, objects]
created: 2026-01-26
---

# Classes and OOP

[[00_Index|← Back to Index]]

> **Object-Oriented Programming with Python classes**

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║      🏗️ KLASSEN - BAUPLANO FUER OBJEKTE (OOP)                 ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   Klasse = Baupläne    |    Objekt = Reales Produkt          ║
║   ─────────────────────────────────────────────────────      ║
║                                                               ║
║   class Car:              ← BAUPLÄNE                          ║
║     def __init__(self, color):                               ║
║       self.color = color                                      ║
║     def drive(self):                                          ║
║       print(f"{self.color} auto fährt!")                      ║
║                                                               ║
║   my_car = Car("red")     ← PRODUKT (Instanz)                ║
║   ┌──────────────────────┐                                    ║
║   │ Objekt               │                                    ║
║   │ • color = "red"      │  Attribute (Daten)                ║
║   │ • drive()            │  Methoden (Funktionen)            ║
║   └──────────────────────┘                                    ║
║                                                               ║
║   my_car.drive()  → "red auto fährt!"                        ║
║   my_car.color    → "red"                                     ║
║                                                               ║
║   Mehrere Objekte aus EINE Klasse:                            ║
║   your_car = Car("blue")   ← Neues Objekt                    ║
║   ┌──────────────────────┐                                    ║
║   │ Objekt               │                                    ║
║   │ • color = "blue"     │  ← Unterschiedliche Daten!        ║
║   │ • drive()            │     Gleiche Methoden!             ║
║   └──────────────────────┘                                    ║
║                                                               ║
║   💡 Klasse: WAS (Struktur)   Objekt: WIE VIELE (Exemplare)   ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 🎯 What is a Class?

A **class** is a blueprint for creating objects. It defines attributes (data) and methods (functions) that objects will have.

Everything in Python is an object with a type (class):

```python
# Check types
num = 10
print(type(num))  # <class 'int'>

string = 'hello'
print(type(string))  # <class 'str'>

lst = []
print(type(lst))  # <class 'list'>
```

---

## 🏗️ Creating a Class

### Basic Class

```python
# Define class with CamelCase name
class Person:
    pass

# Create object (instance)
p = Person()
print(p)  # <__main__.Person object at 0x...>
```

### Class with Constructor

```python
class Person:
    def __init__(self, name):
        self.name = name  # Instance attribute

# Create object
p = Person('Alice')
print(p.name)  # Alice
```

### Multiple Parameters

```python
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

# Create object
p = Person('John', 'Doe', 30, 'USA', 'NYC')
print(p.firstname)  # John
print(p.age)        # 30
print(p.city)       # NYC
```

---

## 🔧 Object Methods

Methods are functions that belong to objects:

```python
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. Lives in {self.city}, {self.country}'

p = Person('Alice', 'Smith', 25, 'USA', 'Boston')
print(p.person_info())
# Alice Smith is 25 years old. Lives in Boston, USA
```

---

## 🎨 Default Values

```python
class Person:
    def __init__(self, firstname='John', lastname='Doe', age=0, country='Unknown', city='Unknown'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old.'

# Create with defaults
p1 = Person()
print(p1.person_info())  # John Doe is 0 years old.

# Create with some values
p2 = Person(firstname='Alice', age=25)
print(p2.person_info())  # Alice Doe is 25 years old.

# Create with all values
p3 = Person('Bob', 'Wilson', 30, 'UK', 'London')
print(p3.person_info())  # Bob Wilson is 30 years old.
```

---

## 💡 Practical Examples

### Bank Account

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # _ indicates 'private'
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f'Deposited ${amount}. New balance: ${self._balance}'
        return 'Invalid amount'
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return f'Withdrew ${amount}. New balance: ${self._balance}'
        return 'Invalid amount or insufficient funds'
    
    def get_balance(self):
        return self._balance

# Use the class
account = BankAccount('Alice', 1000)
print(account.deposit(500))   # Deposited $500. New balance: $1500
print(account.withdraw(200))  # Withdrew $200. New balance: $1300
print(f'Balance: ${account.get_balance()}')  # Balance: $1300
```

### Shopping Cart

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item, price, quantity=1):
        self.items.append({
            'item': item,
            'price': price,
            'quantity': quantity
        })
        return f'Added {quantity}x {item}'
    
    def get_total(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total
    
    def show_cart(self):
        print('Shopping Cart:')
        for item in self.items:
            print(f"  {item['quantity']}x {item['item']} - ${item['price']} each")
        print(f'Total: ${self.get_total()}')

# Use the cart
cart = ShoppingCart()
cart.add_item('Apple', 1.5, 5)
cart.add_item('Bread', 2.5, 2)
cart.add_item('Milk', 3.0, 1)
cart.show_cart()
# Shopping Cart:
#   5x Apple - $1.5 each
#   2x Bread - $2.5 each
#   1x Milk - $3.0 each
# Total: $15.5
```

### Rectangle Class

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height

# Create rectangles
rect1 = Rectangle(10, 5)
print(f'Area: {rect1.area()}')           # Area: 50
print(f'Perimeter: {rect1.perimeter()}') # Perimeter: 30
print(f'Is square: {rect1.is_square()}') # Is square: False

rect2 = Rectangle(5, 5)
print(f'Is square: {rect2.is_square()}') # Is square: True
```

---

## 📦 Class vs Instance Attributes

```python
class Dog:
    # Class attribute (shared by all instances)
    species = 'Canis familiaris'
    
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    def bark(self):
        return f'{self.name} says Woof!'

# Create dogs
dog1 = Dog('Buddy', 3)
dog2 = Dog('Max', 5)

# Instance attributes are different
print(dog1.name)  # Buddy
print(dog2.name)  # Max

# Class attribute is same for all
print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

# Methods work independently
print(dog1.bark())  # Buddy says Woof!
print(dog2.bark())  # Max says Woof!
```

---

## ✅ Best Practices

### 1. Use CamelCase for Class Names

```python
# Good
class BankAccount:
    pass

class ShoppingCart:
    pass

# Bad
class bank_account:
    pass
```

### 2. Use __init__ for Initialization

```python
# Good
class Person:
    def __init__(self, name):
        self.name = name

# Avoid setting attributes outside __init__
```

### 3. self is Always First Parameter

```python
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def my_method(self):  # self is first!
        return self.value
```

### 4. Use _ for 'Private' Attributes

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # "Private" attribute
    
    def get_balance(self):
        return self._balance
```

### 5. Keep Methods Focused

```python
# Good - single responsibility
class User:
    def validate_email(self):
        return '@' in self.email
    
    def send_welcome_email(self):
        if self.validate_email():
            # send email
            pass
```

---

## 🎓 Summary

**Classes:**
- Blueprints for creating objects
- Use CamelCase naming
- Defined with `class` keyword

**Objects:**
- Instances of classes
- Have attributes (data)
- Have methods (functions)

**Key Concepts:**
- `__init__()` - Constructor
- `self` - Reference to instance
- Instance vs Class attributes

---

## 🔗 Related Topics

- [[12_Inheritance|Inheritance]]
- [[13_Magic_Methods|Magic Methods]]
- [[14_Properties|Properties]]

---

[[00_Index|← Back to Index]]

*Object-Oriented Power! 🎯*

---

[[00_Index|← Back to Index]]
