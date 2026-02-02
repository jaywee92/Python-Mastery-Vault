# Level 6: Functions
Notebook: [[06_Level_Functions.ipynb]]


> **Difficulty:** ⭐⭐⭐ Intermediate
> **Topics:** Function Definition, Parameters, Return Values, Default Arguments
> **Prerequisites:** [[05_Level_Loops|Level 5]], [[../../01_Python_Basics/08_Functions|Functions]]

---

## Exercise 6.1: Simple Greeting
**Task:** Create a function `greet()` that prints "Hello, World!".

**Expected Output:**
```
Hello, World!
```

> [!hint]- Hint
> Use `def greet():` to define the function.

> [!success]- Solution
> ```python
> def greet():
>     print("Hello, World!")
>
> greet()
> ```

---

## Exercise 6.2: Personalized Greeting
**Task:** Create a function `greet(name)` that takes a name and prints "Hello, [name]!".

**Expected Output:**
```
Hello, Alice!
```

> [!hint]- Hint
> Use a parameter in the function definition.

> [!success]- Solution
> ```python
> def greet(name):
>     print(f"Hello, {name}!")
>
> greet("Alice")
> ```

---

## Exercise 6.3: Add Two Numbers
**Task:** Create a function `add(a, b)` that returns the sum of two numbers.

**Expected Output:**
```
5 + 3 = 8
```

> [!hint]- Hint
> Use `return` to return the result.

> [!success]- Solution
> ```python
> def add(a, b):
>     return a + b
>
> result = add(5, 3)
> print(f"5 + 3 = {result}")
> ```

---

## Exercise 6.4: Default Parameter
**Task:** Create a function `power(base, exponent=2)` with a default exponent of 2.

**Expected Output:**
```
5^2 = 25
5^3 = 125
```

> [!hint]- Hint
> Set default value in parameter: `exponent=2`.

> [!success]- Solution
> ```python
> def power(base, exponent=2):
>     return base ** exponent
>
> print(f"5^2 = {power(5)}")
> print(f"5^3 = {power(5, 3)}")
> ```

---

## Exercise 6.5: Multiple Returns
**Task:** Create a function `min_max(numbers)` that returns both minimum and maximum.

**Expected Output:**
```
Min: 1, Max: 9
```

> [!hint]- Hint
> Return a tuple: `return min_val, max_val`.

> [!success]- Solution
> ```python
> def min_max(numbers):
>     return min(numbers), max(numbers)
>
> minimum, maximum = min_max([3, 1, 4, 1, 5, 9, 2, 6])
> print(f"Min: {minimum}, Max: {maximum}")
> ```

---

## Exercise 6.6: Is Even Function
**Task:** Create a function `is_even(number)` that returns True if even, False otherwise.

**Expected Output:**
```
4 is even: True
7 is even: False
```

> [!hint]- Hint
> Use `return number % 2 == 0`.

> [!success]- Solution
> ```python
> def is_even(number):
>     return number % 2 == 0
>
> print(f"4 is even: {is_even(4)}")
> print(f"7 is even: {is_even(7)}")
> ```

---

## Exercise 6.7: Keyword Arguments
**Task:** Create a function `introduce(name, age, city)` and call it with keyword arguments.

**Expected Output:**
```
I'm Alice, 25 years old, from Berlin.
```

> [!hint]- Hint
> Call with `introduce(name="Alice", age=25, city="Berlin")`.

> [!success]- Solution
> ```python
> def introduce(name, age, city):
>     print(f"I'm {name}, {age} years old, from {city}.")
>
> introduce(name="Alice", age=25, city="Berlin")
> ```

---

## Exercise 6.8: Variable Arguments (*args)
**Task:** Create a function `sum_all(*numbers)` that sums any number of arguments.

**Expected Output:**
```
Sum: 15
Sum: 100
```

> [!hint]- Hint
> Use `*args` to accept variable arguments.

> [!success]- Solution
> ```python
> def sum_all(*numbers):
>     return sum(numbers)
>
> print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")
> print(f"Sum: {sum_all(10, 20, 30, 40)}")
> ```

---

## Exercise 6.9: Keyword Variable Arguments (**kwargs)
**Task:** Create a function `print_info(**info)` that prints all key-value pairs.

**Expected Output:**
```
name: Alice
age: 25
city: Berlin
```

> [!hint]- Hint
> Use `**kwargs` and iterate over `.items()`.

> [!success]- Solution
> ```python
> def print_info(**info):
>     for key, value in info.items():
>         print(f"{key}: {value}")
>
> print_info(name="Alice", age=25, city="Berlin")
> ```

---

## Exercise 6.10: Docstring
**Task:** Create a function `calculate_area(length, width)` with a proper docstring.

**Expected Output:**
```
Area: 35
Help: Calculate the area of a rectangle.
```

> [!hint]- Hint
> Add a docstring as the first line inside the function.

> [!success]- Solution
> ```python
> def calculate_area(length, width):
>     """Calculate the area of a rectangle.
>
>     Args:
>         length: The length of the rectangle.
>         width: The width of the rectangle.
>
>     Returns:
>         The area as length * width.
>     """
>     return length * width
>
> print(f"Area: {calculate_area(7, 5)}")
> print(f"Help: {calculate_area.__doc__.split(chr(10))[0]}")
> ```

---

## Exercise 6.11: Recursive Function
**Task:** Create a recursive function `factorial(n)` to calculate n!.

**Expected Output:**
```
5! = 120
```

> [!hint]- Hint
> Base case: n <= 1 returns 1. Recursive: n * factorial(n-1).

> [!success]- Solution
> ```python
> def factorial(n):
>     if n <= 1:
>         return 1
>     return n * factorial(n - 1)
>
> print(f"5! = {factorial(5)}")
> ```

---

## Exercise 6.12: Fibonacci
**Task:** Create a function `fibonacci(n)` that returns the nth Fibonacci number.

**Expected Output:**
```
fib(10) = 55
```

> [!hint]- Hint
> Use iteration or recursion with base cases for n=0 and n=1.

> [!success]- Solution
> ```python
> def fibonacci(n):
>     if n <= 1:
>         return n
>     a, b = 0, 1
>     for _ in range(2, n + 1):
>         a, b = b, a + b
>     return b
>
> print(f"fib(10) = {fibonacci(10)}")
> ```

---

## Exercise 6.13: Filter Function
**Task:** Create a function `filter_positive(numbers)` that returns only positive numbers.

**Expected Output:**
```
[1, 3, 5]
```

> [!hint]- Hint
> Use a list comprehension or loop to filter.

> [!success]- Solution
> ```python
> def filter_positive(numbers):
>     return [n for n in numbers if n > 0]
>
> result = filter_positive([1, -2, 3, -4, 5])
> print(result)
> ```

---

## Exercise 6.14: Function as Argument
**Task:** Create a function `apply_operation(a, b, operation)` that applies a given function.

**Expected Output:**
```
Add: 8
Multiply: 15
```

> [!hint]- Hint
> Pass a function as a parameter and call it inside.

> [!success]- Solution
> ```python
> def apply_operation(a, b, operation):
>     return operation(a, b)
>
> def add(x, y):
>     return x + y
>
> def multiply(x, y):
>     return x * y
>
> print(f"Add: {apply_operation(3, 5, add)}")
> print(f"Multiply: {apply_operation(3, 5, multiply)}")
> ```

---

## Exercise 6.15: Closure Example
**Task:** Create a function `counter()` that returns a function counting calls.

**Expected Output:**
```
1
2
3
```

> [!hint]- Hint
> Use a nested function that modifies a nonlocal variable.

> [!success]- Solution
> ```python
> def counter():
>     count = 0
>     def increment():
>         nonlocal count
>         count += 1
>         return count
>     return increment
>
> my_counter = counter()
> print(my_counter())
> print(my_counter())
> print(my_counter())
> ```

---

## 🎯 Level 6 Complete!

**Skills Practiced:**
- Function definition and calling
- Parameters and return values
- Default and keyword arguments
- *args and **kwargs
- Docstrings
- Recursion
- Higher-order functions
- Closures

**Next Level:** [[07_Level_Tuples_Sets|Level 7: Tuples & Sets]]
