---
title: Inheritance
tags: [python, oop, inheritance, polymorphism, super, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# 🧬 Inheritance

[[00_Index|← Back to Index]] | [[11_A_OOP_Visual_Guide|OOP Visual Guide →]]

> **Create specialized classes through inheritance**

---

## 🎯 What is Inheritance?

**Inheritance** allows a class (Child/Subclass) to adopt attributes and methods from another class (Parent/Superclass).

```
┌─────────────────────────────┐
│         Animal              │  ← Parent/Base/Superclass
│  - name                     │
│  - speak()                  │
└─────────────┬───────────────┘
              │ inherits from
    ┌─────────┴─────────┐
    ▼                   ▼
┌─────────┐       ┌─────────┐
│   Dog   │       │   Cat   │  ← Child/Derived/Subclass
│ speak() │       │ speak() │
│  bark() │       │  purr() │
└─────────┘       └─────────┘
```

**Benefits:**
- ✅ **Code Reuse** - DRY Principle
- ✅ **Logical Hierarchies** - "is-a" Relationships
- ✅ **Polymorphism** - Unified Interface
- ✅ **Extensibility** - Specialization without Change

---

## 📦 Basic Inheritance

### Simple Inheritance

```python
# Parent/Base Class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some sound"

    def info(self):
        return f"{self.name}, {self.age} years old"


# Child/Derived Class - inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

    def fetch(self):
        return f"{self.name} fetches the ball"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

    def purr(self):
        return f"{self.name} purrs"


# Usage
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 5)

print(dog.name)      # "Buddy" (inherited)
print(dog.info())    # "Buddy, 3 years old" (inherited)
print(dog.speak())   # "Buddy says: Woof!" (overridden)
print(dog.fetch())   # "Buddy fetches the ball" (new)

print(cat.speak())   # "Whiskers says: Meow!"
print(cat.purr())    # "Whiskers purrs"
```

### isinstance() and issubclass()

```python
# isinstance: Is object an instance of the class?
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (also Parent!)
print(isinstance(dog, Cat))     # False

# issubclass: Is class a subclass?
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Animal))  # True
print(issubclass(Dog, Cat))     # False
print(issubclass(Animal, object))  # True (everything inherits from object)
```

---

## 🔧 super() - Calling the Parent Class

`super()` provides access to methods of the parent class.

### Extending __init__

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        # Calls Animal.__init__()
        super().__init__(name, age)
        # Adds own attribute
        self.breed = breed

    def info(self):
        return f"{self.name} is a {self.breed}, {self.age} years old"


buddy = Dog("Buddy", 3, "Golden Retriever")
print(buddy.name)   # "Buddy"
print(buddy.age)    # 3
print(buddy.breed)  # "Golden Retriever"
print(buddy.info()) # "Buddy is a Golden Retriever, 3 years old"
```

### Extending Methods (not replacing)

```python
class Animal:
    def speak(self):
        return "Some generic sound"


class Dog(Animal):
    def speak(self):
        # Use parent implementation AND extend it
        parent_sound = super().speak()
        return f"{parent_sound} + Woof!"


dog = Dog()
print(dog.speak())  # "Some generic sound + Woof!"
```

### ⚠️ super() vs Direct Call

```python
class Animal:
    def __init__(self, name):
        self.name = name

# ✅ CORRECT: Use super()
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

# ❌ AVOID: Direct call (works but is inflexible)
class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)  # Hardcoded class name
        self.color = color

# super() is better for:
# - Multiple Inheritance
# - Refactoring (changing class names)
# - Diamond Problem
```

---

## 🔄 Method Overriding

Child classes can **override** parent methods.

```python
class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"A shape with area {self.area()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Overrides Shape.area()
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2


# Polymorphism in action
shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print(shape.describe())
# Output:
# A shape with area 20
# A shape with area 28.274333882308138
```

---

## 🎭 Polymorphism

**Polymorphism** = Same interface, different behavior

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1  # 10% Standard


class Manager(Employee):
    def calculate_bonus(self):
        return self.salary * 0.2  # 20% for Managers


class Developer(Employee):
    def calculate_bonus(self):
        return self.salary * 0.15  # 15% for Developers


class Intern(Employee):
    def calculate_bonus(self):
        return 500  # Fixed amount


# Polymorphic function - treats all the same
def print_bonus(employee):
    """Works with ANY Employee type"""
    bonus = employee.calculate_bonus()
    print(f"{employee.name}: {bonus:.2f}€ Bonus")


# Usage
employees = [
    Manager("Anna", 80000),
    Developer("Bob", 60000),
    Intern("Charlie", 30000)
]

for emp in employees:
    print_bonus(emp)

# Output:
# Anna: 16000.00€ Bonus
# Bob: 9000.00€ Bonus
# Charlie: 500.00€ Bonus
```

---

## 💎 Multiple Inheritance

Python supports inheritance from **multiple classes**.

```python
class Flyer:
    def fly(self):
        return "I can fly!"


class Swimmer:
    def swim(self):
        return "I can swim!"


class Walker:
    def walk(self):
        return "I can walk!"


# Multiple inheritance
class Duck(Flyer, Swimmer, Walker):
    def quack(self):
        return "Quack!"


donald = Duck()
print(donald.fly())   # "I can fly!"
print(donald.swim())  # "I can swim!"
print(donald.walk())  # "I can walk!"
print(donald.quack()) # "Quack!"
```

### MRO - Method Resolution Order

With multiple inheritance: In what order does Python search for methods?

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):  # Inherits from B AND C
    pass

d = D()
print(d.method())  # "B" - B comes before C

# Show MRO
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

# Or as a list
print(D.mro())
```

```
         A
        / \
       B   C
        \ /
         D

MRO: D → B → C → A → object
(Linearization using C3 algorithm)
```

### Solving Diamond Problem with super()

```python
class A:
    def __init__(self):
        print("A.__init__")

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

d = D()
# Output:
# D.__init__
# B.__init__
# C.__init__
# A.__init__
# → Each __init__ is called exactly ONCE!
```

---

## 🛡️ Abstract Base Classes (ABC)

Enforce that subclasses implement certain methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class - cannot be instantiated directly"""

    @abstractmethod
    def area(self):
        """Must be implemented by subclasses"""
        pass

    @abstractmethod
    def perimeter(self):
        """Must be implemented by subclasses"""
        pass

    def describe(self):
        """Concrete method - is inherited"""
        return f"Area: {self.area()}, Perimeter: {self.perimeter()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


# shape = Shape()  # ❌ TypeError: Can't instantiate abstract class
rect = Rectangle(4, 5)
print(rect.describe())  # "Area: 20, Perimeter: 18"


# Missing implementation = Error
class Triangle(Shape):
    def area(self):
        return 0
    # perimeter is missing!

# t = Triangle()  # ❌ TypeError: Can't instantiate abstract class
```

---

## 📋 Inheritance Patterns

### 1. Template Method Pattern

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Template defines workflow, subclasses define details"""

    def process(self):
        """Template Method - workflow is fixed"""
        data = self.load_data()
        processed = self.transform(data)
        self.save(processed)

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def save(self, data):
        pass


class CSVProcessor(DataProcessor):
    def load_data(self):
        return ["row1", "row2", "row3"]

    def transform(self, data):
        return [row.upper() for row in data]

    def save(self, data):
        print(f"Saving to CSV: {data}")


processor = CSVProcessor()
processor.process()
# Output: Saving to CSV: ['ROW1', 'ROW2', 'ROW3']
```

### 2. Mixin Classes

```python
# Mixins add functionality without true inheritance
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class PrintableMixin:
    def print_info(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")


class User(JSONMixin, PrintableMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email


user = User("Alice", "alice@example.com")
print(user.to_json())  # {"name": "Alice", "email": "alice@example.com"}
user.print_info()
# name: Alice
# email: alice@example.com
```

---

## ⚠️ Common Pitfalls

### 1. Forgetting super().__init__()

```python
# ❌ WRONG
class Child(Parent):
    def __init__(self, extra):
        # Parent.__init__ is NOT called!
        self.extra = extra  # Parent attributes missing!

# ✅ CORRECT
class Child(Parent):
    def __init__(self, parent_arg, extra):
        super().__init__(parent_arg)  # Parent first!
        self.extra = extra
```

### 2. Wrong Inheritance Hierarchy

```python
# ❌ WRONG: Modeling "has-a" as "is-a"
class Engine:
    def start(self):
        return "Engine running"

class Car(Engine):  # Car IS NOT an Engine!
    pass

# ✅ CORRECT: Composition for "has-a"
class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS an Engine

    def start(self):
        return self.engine.start()
```

### 3. Violating Liskov Substitution Principle

```python
# ❌ WRONG: Subclass changes expected behavior
class Bird:
    def fly(self):
        return "Flying!"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")  # Violates expectation!

# ✅ BETTER: Rethink hierarchy
class Bird:
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        return "Flying!"

class Penguin(Bird):
    def move(self):
        return "Swimming!"
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Use inheritance for "is-a" relationships | Abuse inheritance for code sharing |
| Use `super()` instead of direct parent call | Hardcode parent class name |
| Flat hierarchies (max 2-3 levels) | Deep inheritance chains |
| ABC for interfaces | Empty base classes |
| Prefer composition | Inherit everything |
| Understand MRO with multiple inheritance | Ignore diamond problem |

---

## 🎯 Exam Checklist

- [ ] Inheritance syntax: `class Child(Parent)`
- [ ] Use `super().__init__()` correctly
- [ ] Explain method overriding
- [ ] Distinguish `isinstance()` and `issubclass()`
- [ ] MRO with multiple inheritance
- [ ] ABC and `@abstractmethod`
- [ ] "is-a" vs "has-a" relationships

---

[[11_Classes_and_OOP|← Classes]] | [[00_Index|Index]] | [[13_Magic_Methods|Magic Methods →]]
