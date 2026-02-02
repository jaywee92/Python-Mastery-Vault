# Level 10: OOP & Exceptions
Notebook: [[10_Level_OOP_Exceptions.ipynb]]


> **Difficulty:** ⭐⭐⭐⭐ Advanced
> **Topics:** Classes, Objects, Inheritance, Exception Handling
> **Prerequisites:** [[09_Level_Comprehensions|Level 9]], [[../../01_Python_Basics/11_Classes_and_OOP|Classes and OOP]], [[../../01_Python_Basics/13_Exceptions|Exceptions]]

---

## Exercise 10.1: Basic Class
**Task:** Create a `Person` class with `name` and `age` attributes.

**Expected Output:**
```
Alice is 25 years old
```

> [!hint]- Hint
> Use `__init__` method to initialize attributes.

> [!success]- Solution
> ```python
> class Person:
>     def __init__(self, name, age):
>         self.name = name
>         self.age = age
>
> person = Person("Alice", 25)
> print(f"{person.name} is {person.age} years old")
> ```

---

## Exercise 10.2: Class Method
**Task:** Add a `greet()` method to the Person class.

**Expected Output:**
```
Hello, my name is Alice!
```

> [!hint]- Hint
> Define a method that uses `self.name`.

> [!success]- Solution
> ```python
> class Person:
>     def __init__(self, name, age):
>         self.name = name
>         self.age = age
>
>     def greet(self):
>         return f"Hello, my name is {self.name}!"
>
> person = Person("Alice", 25)
> print(person.greet())
> ```

---

## Exercise 10.3: String Representation
**Task:** Add `__str__` and `__repr__` methods to a `Book` class.

**Expected Output:**
```
str: Python Basics by John Doe
repr: Book('Python Basics', 'John Doe', 2024)
```

> [!hint]- Hint
> `__str__` for users, `__repr__` for developers.

> [!success]- Solution
> ```python
> class Book:
>     def __init__(self, title, author, year):
>         self.title = title
>         self.author = author
>         self.year = year
>
>     def __str__(self):
>         return f"{self.title} by {self.author}"
>
>     def __repr__(self):
>         return f"Book('{self.title}', '{self.author}', {self.year})"
>
> book = Book("Python Basics", "John Doe", 2024)
> print(f"str: {str(book)}")
> print(f"repr: {repr(book)}")
> ```

---

## Exercise 10.4: Class with Validation
**Task:** Create a `BankAccount` class that prevents negative balance.

**Expected Output:**
```
Balance: $100
Cannot withdraw $150: Insufficient funds
Balance: $100
```

> [!hint]- Hint
> Check balance before allowing withdrawal.

> [!success]- Solution
> ```python
> class BankAccount:
>     def __init__(self, balance=0):
>         self.balance = balance
>
>     def deposit(self, amount):
>         self.balance += amount
>
>     def withdraw(self, amount):
>         if amount > self.balance:
>             print(f"Cannot withdraw ${amount}: Insufficient funds")
>             return False
>         self.balance -= amount
>         return True
>
> account = BankAccount(100)
> print(f"Balance: ${account.balance}")
> account.withdraw(150)
> print(f"Balance: ${account.balance}")
> ```

---

## Exercise 10.5: Inheritance
**Task:** Create a `Student` class that inherits from `Person`.

**Expected Output:**
```
Alice is 20 years old
Student ID: S12345
```

> [!hint]- Hint
> Use `super().__init__()` to call parent constructor.

> [!success]- Solution
> ```python
> class Person:
>     def __init__(self, name, age):
>         self.name = name
>         self.age = age
>
> class Student(Person):
>     def __init__(self, name, age, student_id):
>         super().__init__(name, age)
>         self.student_id = student_id
>
> student = Student("Alice", 20, "S12345")
> print(f"{student.name} is {student.age} years old")
> print(f"Student ID: {student.student_id}")
> ```

---

## Exercise 10.6: Method Overriding
**Task:** Override the `greet()` method in the `Student` class.

**Expected Output:**
```
Person: Hello, I'm Bob
Student: Hi, I'm Alice (ID: S12345)
```

> [!hint]- Hint
> Define the same method name in the child class.

> [!success]- Solution
> ```python
> class Person:
>     def __init__(self, name):
>         self.name = name
>
>     def greet(self):
>         return f"Hello, I'm {self.name}"
>
> class Student(Person):
>     def __init__(self, name, student_id):
>         super().__init__(name)
>         self.student_id = student_id
>
>     def greet(self):
>         return f"Hi, I'm {self.name} (ID: {self.student_id})"
>
> person = Person("Bob")
> student = Student("Alice", "S12345")
> print(f"Person: {person.greet()}")
> print(f"Student: {student.greet()}")
> ```

---

## Exercise 10.7: Class and Static Methods
**Task:** Create a `MathHelper` class with a class method and a static method.

**Expected Output:**
```
Instance count: 2
Is even: True
```

> [!hint]- Hint
> Use `@classmethod` for class methods, `@staticmethod` for static methods.

> [!success]- Solution
> ```python
> class MathHelper:
>     instance_count = 0
>
>     def __init__(self):
>         MathHelper.instance_count += 1
>
>     @classmethod
>     def get_instance_count(cls):
>         return cls.instance_count
>
>     @staticmethod
>     def is_even(n):
>         return n % 2 == 0
>
> m1 = MathHelper()
> m2 = MathHelper()
> print(f"Instance count: {MathHelper.get_instance_count()}")
> print(f"Is even: {MathHelper.is_even(4)}")
> ```

---

## Exercise 10.8: Property Decorator
**Task:** Create a `Circle` class with a property for area.

**Expected Output:**
```
Radius: 5
Area: 78.54
```

> [!hint]- Hint
> Use `@property` decorator for computed attributes.

> [!success]- Solution
> ```python
> import math
>
> class Circle:
>     def __init__(self, radius):
>         self._radius = radius
>
>     @property
>     def radius(self):
>         return self._radius
>
>     @property
>     def area(self):
>         return math.pi * self._radius ** 2
>
> circle = Circle(5)
> print(f"Radius: {circle.radius}")
> print(f"Area: {circle.area:.2f}")
> ```

---

## Exercise 10.9: Basic Exception Handling
**Task:** Handle a division by zero error.

**Expected Output:**
```
Cannot divide by zero!
Result: None
```

> [!hint]- Hint
> Use try-except block.

> [!success]- Solution
> ```python
> def divide(a, b):
>     try:
>         return a / b
>     except ZeroDivisionError:
>         print("Cannot divide by zero!")
>         return None
>
> result = divide(10, 0)
> print(f"Result: {result}")
> ```

---

## Exercise 10.10: Multiple Exceptions
**Task:** Handle different types of exceptions for a list operation.

**Expected Output:**
```
Index 10: Index out of range
Non-integer: Index must be an integer
```

> [!hint]- Hint
> Use multiple except clauses.

> [!success]- Solution
> ```python
> def get_element(lst, index):
>     try:
>         return lst[index]
>     except IndexError:
>         return "Index out of range"
>     except TypeError:
>         return "Index must be an integer"
>
> numbers = [1, 2, 3, 4, 5]
> print(f"Index 10: {get_element(numbers, 10)}")
> print(f"Non-integer: {get_element(numbers, 'a')}")
> ```

---

## Exercise 10.11: Finally Block
**Task:** Demonstrate the finally block always executes.

**Expected Output:**
```
Attempting division...
Error: division by zero
Cleanup completed (always runs)
```

> [!hint]- Hint
> `finally` runs regardless of whether an exception occurred.

> [!success]- Solution
> ```python
> def risky_operation():
>     try:
>         print("Attempting division...")
>         result = 10 / 0
>     except ZeroDivisionError as e:
>         print(f"Error: {e}")
>     finally:
>         print("Cleanup completed (always runs)")
>
> risky_operation()
> ```

---

## Exercise 10.12: Raise Exception
**Task:** Create a function that raises an exception for invalid input.

**Expected Output:**
```
Error: Age cannot be negative: -5
```

> [!hint]- Hint
> Use `raise ValueError("message")`.

> [!success]- Solution
> ```python
> def set_age(age):
>     if age < 0:
>         raise ValueError(f"Age cannot be negative: {age}")
>     return age
>
> try:
>     set_age(-5)
> except ValueError as e:
>     print(f"Error: {e}")
> ```

---

## Exercise 10.13: Custom Exception
**Task:** Create a custom `InsufficientFundsError` exception.

**Expected Output:**
```
Error: Cannot withdraw $150. Available: $100
```

> [!hint]- Hint
> Inherit from `Exception` class.

> [!success]- Solution
> ```python
> class InsufficientFundsError(Exception):
>     def __init__(self, amount, balance):
>         self.message = f"Cannot withdraw ${amount}. Available: ${balance}"
>         super().__init__(self.message)
>
> class BankAccount:
>     def __init__(self, balance):
>         self.balance = balance
>
>     def withdraw(self, amount):
>         if amount > self.balance:
>             raise InsufficientFundsError(amount, self.balance)
>         self.balance -= amount
>
> account = BankAccount(100)
> try:
>     account.withdraw(150)
> except InsufficientFundsError as e:
>     print(f"Error: {e}")
> ```

---

## Exercise 10.14: Context Manager
**Task:** Use a context manager for file handling with proper exception handling.

**Expected Output:**
```
File not found: nonexistent.txt
```

> [!hint]- Hint
> Use `with` statement and handle `FileNotFoundError`.

> [!success]- Solution
> ```python
> def read_file(filename):
>     try:
>         with open(filename, 'r') as f:
>             return f.read()
>     except FileNotFoundError:
>         return f"File not found: {filename}"
>
> content = read_file("nonexistent.txt")
> print(content)
> ```

---

## Exercise 10.15: Complete Class with Error Handling
**Task:** Create a `ShoppingCart` class with full error handling.

**Expected Output:**
```
Added: Apple ($1.50)
Added: Banana ($0.75)
Error: Item not in cart: Orange
Total: $2.25
```

> [!hint]- Hint
> Combine OOP with custom exceptions.

> [!success]- Solution
> ```python
> class ItemNotFoundError(Exception):
>     pass
>
> class ShoppingCart:
>     def __init__(self):
>         self.items = {}
>
>     def add_item(self, name, price):
>         self.items[name] = price
>         print(f"Added: {name} (${price:.2f})")
>
>     def remove_item(self, name):
>         if name not in self.items:
>             raise ItemNotFoundError(f"Item not in cart: {name}")
>         del self.items[name]
>
>     def get_total(self):
>         return sum(self.items.values())
>
> cart = ShoppingCart()
> cart.add_item("Apple", 1.50)
> cart.add_item("Banana", 0.75)
>
> try:
>     cart.remove_item("Orange")
> except ItemNotFoundError as e:
>     print(f"Error: {e}")
>
> print(f"Total: ${cart.get_total():.2f}")
> ```

---

## 🎯 Level 10 Complete!

**Skills Practiced:**
- Class creation and instantiation
- Instance methods and attributes
- Inheritance and method overriding
- Class and static methods
- Property decorators
- Exception handling (try/except/finally)
- Raising exceptions
- Custom exceptions
- Context managers

## 🏆 Congratulations!

You have completed all 10 levels of Python exercises!

**Total Exercises Completed:** 150

**What's Next?**
- Practice more on [LeetCode](https://leetcode.com)
- Try [Codewars](https://codewars.com) challenges
- Explore [[../../02_Python_Advanced/00_Index|Python Advanced]] topics
- Build real projects to apply your skills!
