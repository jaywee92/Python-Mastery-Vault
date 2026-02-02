# Level 4: Conditionals
Notebook: [[04_Level_Conditionals.ipynb]]


> **Difficulty:** ⭐⭐ Beginner-Intermediate
> **Topics:** if, elif, else, Comparison Operators, Logical Operators
> **Prerequisites:** [[03_Level_Lists|Level 3]], [[../../01_Python_Basics/05_Conditionals|Conditionals]]

---

## Exercise 4.1: Even or Odd
**Task:** Given `number = 17`, print whether it's even or odd.

**Expected Output:**
```
17 is odd
```

> [!hint]- Hint
> Use modulo operator `%`. A number is even if `number % 2 == 0`.

> [!success]- Solution
> ```python
> number = 17
> if number % 2 == 0:
>     print(f"{number} is even")
> else:
>     print(f"{number} is odd")
> ```

---

## Exercise 4.2: Positive, Negative, Zero
**Task:** Given `number = -5`, determine if it's positive, negative, or zero.

**Expected Output:**
```
-5 is negative
```

> [!hint]- Hint
> Use if-elif-else to check the three cases.

> [!success]- Solution
> ```python
> number = -5
> if number > 0:
>     print(f"{number} is positive")
> elif number < 0:
>     print(f"{number} is negative")
> else:
>     print(f"{number} is zero")
> ```

---

## Exercise 4.3: Grade Calculator
**Task:** Given `score = 85`, assign a letter grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60).

**Expected Output:**
```
Grade: B
```

> [!hint]- Hint
> Use if-elif chain starting from the highest grade.

> [!success]- Solution
> ```python
> score = 85
> if score >= 90:
>     grade = "A"
> elif score >= 80:
>     grade = "B"
> elif score >= 70:
>     grade = "C"
> elif score >= 60:
>     grade = "D"
> else:
>     grade = "F"
> print(f"Grade: {grade}")
> ```

---

## Exercise 4.4: Leap Year
**Task:** Given `year = 2024`, determine if it's a leap year.

**Rules:**
- Divisible by 4 AND
- (Not divisible by 100 OR divisible by 400)

**Expected Output:**
```
2024 is a leap year
```

> [!hint]- Hint
> Use logical operators: `and`, `or`, `not`.

> [!success]- Solution
> ```python
> year = 2024
> if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
>     print(f"{year} is a leap year")
> else:
>     print(f"{year} is not a leap year")
> ```

---

## Exercise 4.5: Voting Eligibility
**Task:** Given `age = 16` and `citizenship = True`, check if the person can vote (must be 18+ and citizen).

**Expected Output:**
```
Cannot vote: Too young
```

> [!hint]- Hint
> Use nested if or combine conditions with `and`.

> [!success]- Solution
> ```python
> age = 16
> citizenship = True
>
> if age >= 18 and citizenship:
>     print("Eligible to vote")
> elif age < 18:
>     print("Cannot vote: Too young")
> else:
>     print("Cannot vote: Not a citizen")
> ```

---

## Exercise 4.6: Triangle Type
**Task:** Given three sides `a = 5`, `b = 5`, `c = 5`, determine if it's equilateral, isosceles, or scalene.

**Expected Output:**
```
Equilateral triangle
```

> [!hint]- Hint
> Equilateral: all equal. Isosceles: exactly two equal. Scalene: none equal.

> [!success]- Solution
> ```python
> a, b, c = 5, 5, 5
>
> if a == b == c:
>     print("Equilateral triangle")
> elif a == b or b == c or a == c:
>     print("Isosceles triangle")
> else:
>     print("Scalene triangle")
> ```

---

## Exercise 4.7: Password Strength
**Task:** Given `password = "Python123"`, check if it's at least 8 characters and contains a digit.

**Expected Output:**
```
Strong password
```

> [!hint]- Hint
> Use `len()` and `any(c.isdigit() for c in password)`.

> [!success]- Solution
> ```python
> password = "Python123"
>
> has_length = len(password) >= 8
> has_digit = any(c.isdigit() for c in password)
>
> if has_length and has_digit:
>     print("Strong password")
> else:
>     print("Weak password")
> ```

---

## Exercise 4.8: Number Range
**Task:** Given `number = 50`, check if it's between 1 and 100 (inclusive).

**Expected Output:**
```
50 is in range
```

> [!hint]- Hint
> Python allows chained comparisons: `1 <= number <= 100`

> [!success]- Solution
> ```python
> number = 50
>
> if 1 <= number <= 100:
>     print(f"{number} is in range")
> else:
>     print(f"{number} is out of range")
> ```

---

## Exercise 4.9: Ticket Price
**Task:** Calculate ticket price based on `age = 25`:
- Under 4: Free
- 4-12: $10
- 13-64: $20
- 65+: $15 (senior discount)

**Expected Output:**
```
Ticket price: $20
```

> [!hint]- Hint
> Use if-elif chain with age ranges.

> [!success]- Solution
> ```python
> age = 25
>
> if age < 4:
>     price = 0
> elif age <= 12:
>     price = 10
> elif age <= 64:
>     price = 20
> else:
>     price = 15
>
> print(f"Ticket price: ${price}")
> ```

---

## Exercise 4.10: Quadrant Finder
**Task:** Given coordinates `x = 5`, `y = -3`, determine which quadrant the point is in.

**Expected Output:**
```
Point (5, -3) is in Quadrant IV
```

> [!hint]- Hint
> Q1: +,+  Q2: -,+  Q3: -,-  Q4: +,-

> [!success]- Solution
> ```python
> x, y = 5, -3
>
> if x > 0 and y > 0:
>     quadrant = "I"
> elif x < 0 and y > 0:
>     quadrant = "II"
> elif x < 0 and y < 0:
>     quadrant = "III"
> elif x > 0 and y < 0:
>     quadrant = "IV"
> else:
>     quadrant = "on an axis"
>
> print(f"Point ({x}, {y}) is in Quadrant {quadrant}")
> ```

---

## Exercise 4.11: Ternary Operator
**Task:** Given `temperature = 25`, use a ternary operator to print "Hot" if >= 30, else "Cool".

**Expected Output:**
```
Weather: Cool
```

> [!hint]- Hint
> Syntax: `value_if_true if condition else value_if_false`

> [!success]- Solution
> ```python
> temperature = 25
> weather = "Hot" if temperature >= 30 else "Cool"
> print(f"Weather: {weather}")
> ```

---

## Exercise 4.12: Valid Triangle
**Task:** Given sides `a = 3`, `b = 4`, `c = 5`, check if they can form a valid triangle.

**Rule:** Sum of any two sides must be greater than the third.

**Expected Output:**
```
Valid triangle
```

> [!hint]- Hint
> Check all three combinations: a+b>c, b+c>a, a+c>b.

> [!success]- Solution
> ```python
> a, b, c = 3, 4, 5
>
> if a + b > c and b + c > a and a + c > b:
>     print("Valid triangle")
> else:
>     print("Invalid triangle")
> ```

---

## Exercise 4.13: Divisibility Check
**Task:** Given `number = 15`, check if it's divisible by 3, 5, both, or neither.

**Expected Output:**
```
15 is divisible by both 3 and 5
```

> [!hint]- Hint
> Check the "both" condition first, then individual conditions.

> [!success]- Solution
> ```python
> number = 15
>
> if number % 3 == 0 and number % 5 == 0:
>     print(f"{number} is divisible by both 3 and 5")
> elif number % 3 == 0:
>     print(f"{number} is divisible by 3")
> elif number % 5 == 0:
>     print(f"{number} is divisible by 5")
> else:
>     print(f"{number} is divisible by neither")
> ```

---

## Exercise 4.14: Login System
**Task:** Check if `username = "admin"` and `password = "secret123"` match the expected values.

**Expected Output:**
```
Login successful!
```

> [!hint]- Hint
> Use `and` to check both conditions.

> [!success]- Solution
> ```python
> username = "admin"
> password = "secret123"
>
> correct_user = "admin"
> correct_pass = "secret123"
>
> if username == correct_user and password == correct_pass:
>     print("Login successful!")
> elif username != correct_user:
>     print("Invalid username")
> else:
>     print("Invalid password")
> ```

---

## Exercise 4.15: Season Determiner
**Task:** Given `month = 4` (April), determine the season (Spring: 3-5, Summer: 6-8, Fall: 9-11, Winter: 12,1,2).

**Expected Output:**
```
April is in Spring
```

> [!hint]- Hint
> Use `in` operator with lists or ranges.

> [!success]- Solution
> ```python
> month = 4
> month_names = ["", "January", "February", "March", "April", "May", "June",
>                "July", "August", "September", "October", "November", "December"]
>
> if month in [3, 4, 5]:
>     season = "Spring"
> elif month in [6, 7, 8]:
>     season = "Summer"
> elif month in [9, 10, 11]:
>     season = "Fall"
> else:
>     season = "Winter"
>
> print(f"{month_names[month]} is in {season}")
> ```

---

## 🎯 Level 4 Complete!

**Skills Practiced:**
- if, elif, else statements
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Chained comparisons
- Ternary operator
- Complex condition logic

**Next Level:** [[05_Level_Loops|Level 5: Loops]]
