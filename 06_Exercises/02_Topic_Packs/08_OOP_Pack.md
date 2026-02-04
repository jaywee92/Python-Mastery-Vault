# OOP Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** Classes and objects

Notebook: [[08_OOP_Pack.ipynb]]

---

## O1: Create Class
**Task:** Create a class `Dog` with a `name` attribute and create one instance.

```python
# create class Dog with name
```

> [!hint]- 💡 Hint 1 (Low)
> Define a class and use methods.

> [!hint]- 💡 Hint 2 (Mid)
> Instantiate and print results.

> [!hint]- 💡 Hint 3 (High)
> Keep it minimal and readable.

> [!success]- ✅ Solution
> ```python
> class Dog:
>     def __init__(self, name):
>         self.name = name
>
> d = Dog('Rex')
> print(d.name)
> ```

---

---

## O2: Method
**Task:** Add a `greet()` method that returns a message using the name.

```python
# class with greet method
```

> [!hint]- 💡 Hint 1 (Low)
> Define a class and use methods.

> [!hint]- 💡 Hint 2 (Mid)
> Instantiate and print results.

> [!hint]- 💡 Hint 3 (High)
> Keep it minimal and readable.

> [!success]- ✅ Solution
> ```python
> class Person:
>     def __init__(self, name):
>         self.name = name
>     def greet(self):
>         return f'Hi {self.name}'
>
> p = Person('Ana')
> print(p.greet())
> ```

---

---

## O3: Update Attribute
**Task:** Change an object's attribute (e.g., age) and print the new value.

```python
# change age
```

> [!hint]- 💡 Hint 1 (Low)
> Define a class and use methods.

> [!hint]- 💡 Hint 2 (Mid)
> Instantiate and print results.

> [!hint]- 💡 Hint 3 (High)
> Keep it minimal and readable.

> [!success]- ✅ Solution
> ```python
> class User:
>     def __init__(self, age):
>         self.age = age
>
> u = User(20)
> u.age = 21
> print(u.age)
> ```

---

---

## O4: Class Counter
**Task:** Use a class variable to count how many objects were created.

```python
# count instances
```

> [!hint]- 💡 Hint 1 (Low)
> Define a class and use methods.

> [!hint]- 💡 Hint 2 (Mid)
> Instantiate and print results.

> [!hint]- 💡 Hint 3 (High)
> Keep it minimal and readable.

> [!success]- ✅ Solution
> ```python
> class Counter:
>     count = 0
>     def __init__(self):
>         Counter.count += 1
>
> Counter()
> Counter()
> print(Counter.count)
> ```

---

---

## O5: Inheritance
**Task:** Create `Dog` that inherits from `Animal` and uses a method from it.

```python
# Dog inherits Animal
```

> [!hint]- 💡 Hint 1 (Low)
> Define a class and use methods.

> [!hint]- 💡 Hint 2 (Mid)
> Instantiate and print results.

> [!hint]- 💡 Hint 3 (High)
> Keep it minimal and readable.

> [!success]- ✅ Solution
> ```python
> class Animal:
>     def speak(self):
>         return 'sound'
> class Dog(Animal):
>     pass
> print(Dog().speak())
> ```

---

---

## O6: String Representation
**Task:** Implement `__str__` to return a friendly description.

```python
# __str__
```

> [!hint]- 💡 Hint 1 (Low)
> Define a class and use methods.

> [!hint]- 💡 Hint 2 (Mid)
> Instantiate and print results.

> [!hint]- 💡 Hint 3 (High)
> Keep it minimal and readable.

> [!success]- ✅ Solution
> ```python
> class Box:
>     def __init__(self, size):
>         self.size = size
>     def __str__(self):
>         return f'Box({self.size})'
>
> print(Box(3))
> ```

---

---

## O7: Default Value
**Task:** Use a default value in `__init__` when no argument is provided.

```python
# default parameter
```

> [!hint]- 💡 Hint 1 (Low)
> Define a class and use methods.

> [!hint]- 💡 Hint 2 (Mid)
> Instantiate and print results.

> [!hint]- 💡 Hint 3 (High)
> Keep it minimal and readable.

> [!success]- ✅ Solution
> ```python
> class User:
>     def __init__(self, name='friend'):
>         self.name = name
> print(User().name)
> ```

---

---

## O8: Static Method
**Task:** Create a static method `is_even(n)` that returns True/False.

```python
# is_even
```

> [!hint]- 💡 Hint 1 (Low)
> Define a class and use methods.

> [!hint]- 💡 Hint 2 (Mid)
> Instantiate and print results.

> [!hint]- 💡 Hint 3 (High)
> Keep it minimal and readable.

> [!success]- ✅ Solution
> ```python
> class Utils:
>     @staticmethod
>     def is_even(n):
>         return n % 2 == 0
> print(Utils.is_even(4))
> ```

---

---

## O9: Property
**Task:** Create a `full_name` property from `first` and `last`.

```python
# full_name
```

> [!hint]- 💡 Hint 1 (Low)
> Define a class and use methods.

> [!hint]- 💡 Hint 2 (Mid)
> Instantiate and print results.

> [!hint]- 💡 Hint 3 (High)
> Keep it minimal and readable.

> [!success]- ✅ Solution
> ```python
> class Person:
>     def __init__(self, first, last):
>         self.first = first
>         self.last = last
>     @property
>     def full_name(self):
>         return f'{self.first} {self.last}'
>
> print(Person('A','B').full_name)
> ```

---

---

## O10: Simple Dataclass
**Task:** Use `@dataclass` to define a `Point` with `x` and `y`.

```python
# Point
```

> [!hint]- 💡 Hint 1 (Low)
> Define a class and use methods.

> [!hint]- 💡 Hint 2 (Mid)
> Instantiate and print results.

> [!hint]- 💡 Hint 3 (High)
> Keep it minimal and readable.

> [!success]- ✅ Solution
> ```python
> from dataclasses import dataclass
> @dataclass
> class Point:
>     x:int
>     y:int
> print(Point(1,2))
> ```

---

---
