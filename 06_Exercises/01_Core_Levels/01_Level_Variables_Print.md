# Level 1: Variables & Print
Notebook: [[01_Level_Variables_Print.ipynb]]


> **Difficulty:** ⭐ Beginner
> **Topics:** Variables, Data Types, Print, Basic Math, Type Conversion
> **Prerequisites:** [[../../01_Python_Basics/01_Variables_and_Strings_Advanced|Variables and Strings]]

---

## Exercise 1.1: Hello World
**Task:** Write a program that prints "Hello, World!" to the console.

> [!hint]- 💡 Hint 1 (Low)
> You need to use a function that outputs text to the console.

> [!hint]- 💡 Hint 2 (Mid)
> The function is called `print()` and takes a string as argument.

> [!hint]- 💡 Hint 3 (High)
> Strings are enclosed in quotes: `print("your text here")`

> [!success]- ✅ Solution
> ```python
> print("Hello, World!")
> ```

---

## Exercise 1.2: Personal Greeting
**Task:** Create a variable `name` with your name and print "Hello, [name]!".

**Expected Output:**
```
Hello, Vito!
```

> [!hint]- 💡 Hint 1 (Low)
> You need to combine a variable with a string.

> [!hint]- 💡 Hint 2 (Mid)
> Use an f-string which starts with `f"..."`.

> [!hint]- 💡 Hint 3 (High)
> Inside f-strings, use `{variable}` to insert values: `f"Hello, {name}!"`

> [!success]- ✅ Solution
> ```python
> name = "Vito"
> print(f"Hello, {name}!")
> ```

---

## Exercise 1.3: Variable Swap
**Task:** Given two variables `a = 5` and `b = 10`, swap their values without using a third variable.

**Expected Output:**
```
a = 10, b = 5
```

> [!hint]- 💡 Hint 1 (Low)
> Python has a special way to assign multiple values at once.

> [!hint]- 💡 Hint 2 (Mid)
> You can unpack values on both sides of `=`.

> [!hint]- 💡 Hint 3 (High)
> Use tuple unpacking: `a, b = b, a`

> [!success]- ✅ Solution
> ```python
> a = 5
> b = 10
> print(f"Before: a = {a}, b = {b}")
>
> a, b = b, a
>
> print(f"After: a = {a}, b = {b}")
> ```

---

## Exercise 1.4: Circle Area
**Task:** Given a radius `r = 7`, calculate and print the area of a circle.

**Formula:** Area = π × r²

**Expected Output:**
```
Area: 153.94
```

> [!hint]- 💡 Hint 1 (Low)
> You need to multiply pi by the radius squared.

> [!hint]- 💡 Hint 2 (Mid)
> Use the `**` operator for exponentiation (powers).

> [!hint]- 💡 Hint 3 (High)
> Formula in Python: `area = pi * r ** 2`

> [!success]- ✅ Solution
> ```python
> import math
>
> r = 7
> area = math.pi * r ** 2
>
> print(f"Area: {area:.2f}")
> ```

---

## Exercise 1.5: Temperature Converter
**Task:** Convert a temperature from Celsius to Fahrenheit.

**Formula:** F = C × 9/5 + 32

**Expected Output:**
```
25°C = 77.0°F
```

> [!hint]- 💡 Hint 1 (Low)
> Apply the mathematical formula directly in Python.

> [!hint]- 💡 Hint 2 (Mid)
> Multiply celsius by 9/5, then add 32.

> [!hint]- 💡 Hint 3 (High)
> `fahrenheit = celsius * 9/5 + 32`

> [!success]- ✅ Solution
> ```python
> celsius = 25
> fahrenheit = celsius * 9/5 + 32
>
> print(f"{celsius}°C = {fahrenheit}°F")
> ```

---

## Exercise 1.6: Type Detective
**Task:** Print the type of each of these values: `42`, `3.14`, `"Hello"`, `True`, `None`.

**Expected Output:**
```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
```

> [!hint]- 💡 Hint 1 (Low)
> There's a built-in function that tells you the type of a value.

> [!hint]- 💡 Hint 2 (Mid)
> The function is called `type()`.

> [!hint]- 💡 Hint 3 (High)
> Use `print(type(42))` for each value.

> [!success]- ✅ Solution
> ```python
> print(type(42))
> print(type(3.14))
> print(type("Hello"))
> print(type(True))
> print(type(None))
> ```

---

## Exercise 1.7: String to Number
**Task:** Given `num_str = "123"`, convert it to an integer, add 100, and print the result.

**Expected Output:**
```
223
```

> [!hint]- 💡 Hint 1 (Low)
> You can't add a number to a string directly - you need to convert first.

> [!hint]- 💡 Hint 2 (Mid)
> Use a function to convert the string to an integer.

> [!hint]- 💡 Hint 3 (High)
> `int("123")` converts the string to integer 123.

> [!success]- ✅ Solution
> ```python
> num_str = "123"
> result = int(num_str) + 100
> print(result)
> ```

---

## Exercise 1.8: Float Precision
**Task:** Given `price = 19.99`, print it with exactly 2 decimal places and a currency symbol.

**Expected Output:**
```
Price: $19.99
```

> [!hint]- 💡 Hint 1 (Low)
> F-strings can format numbers with specific decimal places.

> [!hint]- 💡 Hint 2 (Mid)
> Use a format specifier after the variable name with a colon.

> [!hint]- 💡 Hint 3 (High)
> Use `{price:.2f}` to format with 2 decimal places.

> [!success]- ✅ Solution
> ```python
> price = 19.99
> print(f"Price: ${price:.2f}")
> ```

---

## Exercise 1.9: Multiple Assignment
**Task:** In one line, assign `x = 1`, `y = 2`, `z = 3`. Then print their sum.

**Expected Output:**
```
Sum: 6
```

> [!hint]- 💡 Hint 1 (Low)
> Python allows assigning multiple variables in one line.

> [!hint]- 💡 Hint 2 (Mid)
> Use commas to separate variables and values.

> [!hint]- 💡 Hint 3 (High)
> Syntax: `x, y, z = 1, 2, 3`

> [!success]- ✅ Solution
> ```python
> x, y, z = 1, 2, 3
> print(f"Sum: {x + y + z}")
> ```

---

## Exercise 1.10: Calculate Age
**Task:** Given `birth_year = 1995` and `current_year = 2025`, calculate and print the age.

**Expected Output:**
```
Age: 30
```

> [!hint]- 💡 Hint 1 (Low)
> Age is the difference between two years.

> [!hint]- 💡 Hint 2 (Mid)
> Subtract birth year from current year.

> [!hint]- 💡 Hint 3 (High)
> `age = current_year - birth_year`

> [!success]- ✅ Solution
> ```python
> birth_year = 1995
> current_year = 2025
> age = current_year - birth_year
> print(f"Age: {age}")
> ```

---

## Exercise 1.11: BMI Calculator
**Task:** Calculate BMI given `weight = 70` (kg) and `height = 1.75` (m).

**Formula:** BMI = weight / height²

**Expected Output:**
```
BMI: 22.86
```

> [!hint]- 💡 Hint 1 (Low)
> Divide weight by the square of height.

> [!hint]- 💡 Hint 2 (Mid)
> Use `**2` to square the height.

> [!hint]- 💡 Hint 3 (High)
> `bmi = weight / height ** 2` then format with `:.2f`

> [!success]- ✅ Solution
> ```python
> weight = 70
> height = 1.75
> bmi = weight / height ** 2
> print(f"BMI: {bmi:.2f}")
> ```

---

## Exercise 1.12: Seconds Converter
**Task:** Given `total_seconds = 3725`, convert to hours, minutes, and seconds.

**Expected Output:**
```
1 hours, 2 minutes, 5 seconds
```

> [!hint]- 💡 Hint 1 (Low)
> You need integer division and remainder (modulo) operations.

> [!hint]- 💡 Hint 2 (Mid)
> Use `//` for integer division and `%` for remainder.

> [!hint]- 💡 Hint 3 (High)
> Hours: `total // 3600`, Minutes: `(total % 3600) // 60`, Seconds: `total % 60`

> [!success]- ✅ Solution
> ```python
> total_seconds = 3725
> hours = total_seconds // 3600
> minutes = (total_seconds % 3600) // 60
> seconds = total_seconds % 60
> print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
> ```

---

## Exercise 1.13: Rectangle Properties
**Task:** Given `length = 8` and `width = 5`, calculate area and perimeter.

**Expected Output:**
```
Area: 40
Perimeter: 26
```

> [!hint]- 💡 Hint 1 (Low)
> Area is length times width. Perimeter is the sum of all sides.

> [!hint]- 💡 Hint 2 (Mid)
> Perimeter = 2 × (length + width)

> [!hint]- 💡 Hint 3 (High)
> `area = length * width` and `perimeter = 2 * (length + width)`

> [!success]- ✅ Solution
> ```python
> length = 8
> width = 5
> area = length * width
> perimeter = 2 * (length + width)
> print(f"Area: {area}")
> print(f"Perimeter: {perimeter}")
> ```

---

## Exercise 1.14: Scientific Notation
**Task:** Given `distance = 384400` (km to the moon), print it in scientific notation.

**Expected Output:**
```
Distance: 3.84e+05 km
```

> [!hint]- 💡 Hint 1 (Low)
> F-strings have a format specifier for scientific notation.

> [!hint]- 💡 Hint 2 (Mid)
> Use `e` instead of `f` in the format specifier.

> [!hint]- 💡 Hint 3 (High)
> Use `{distance:.2e}` for scientific notation with 2 decimals.

> [!success]- ✅ Solution
> ```python
> distance = 384400
> print(f"Distance: {distance:.2e} km")
> ```

---

## Exercise 1.15: Tip Calculator
**Task:** Given `bill = 85.50` and `tip_percent = 18`, calculate the tip and total.

**Expected Output:**
```
Tip: $15.39
Total: $100.89
```

> [!hint]- 💡 Hint 1 (Low)
> Tip is a percentage of the bill.

> [!hint]- 💡 Hint 2 (Mid)
> Divide tip_percent by 100 to get the decimal.

> [!hint]- 💡 Hint 3 (High)
> `tip = bill * (tip_percent / 100)`

> [!success]- ✅ Solution
> ```python
> bill = 85.50
> tip_percent = 18
> tip = bill * (tip_percent / 100)
> total = bill + tip
> print(f"Tip: ${tip:.2f}")
> print(f"Total: ${total:.2f}")
> ```

---

## 🎯 Level 1 Complete!

**Skills Practiced:**
- Variable assignment and multiple assignment
- Print formatting with f-strings
- Basic arithmetic operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- Type conversion (`int()`, `float()`, `str()`)
- Number formatting (`.2f`, `.2e`)

**Next Level:** [[02_Level_Strings|Level 2: Strings]]
