# Python Basics Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** Variables, math, conditionals, and short warmups

Notebook: [[01_Basics_Pack.ipynb]]

---

## R1: Swap Variables
**Task:** Swap `a` and `b` without a third variable.

```python
a = 1
b = 2
# expected: a = 2, b = 1
```

> [!hint]- 💡 Hint 1 (Low)
> Python supports multiple assignment.

> [!hint]- 💡 Hint 2 (Mid)
> Put both variables on left and right of `=`.

> [!hint]- 💡 Hint 3 (High)
> `a, b = b, a`

> [!success]- ✅ Solution
> ```python
> a, b = 1, 2
> a, b = b, a
> print(a, b)  # 2 1
> ```

---

---

## R2: Count Vowels
**Task:** Count vowels in a string.

```python
text = "hello"
# expected: 2
```

> [!hint]- 💡 Hint 1 (Low)
> Check each character.

> [!hint]- 💡 Hint 2 (Mid)
> Use a set of vowels: `{'a','e','i','o','u'}`.

> [!hint]- 💡 Hint 3 (High)
> Increase a counter when a char is a vowel.

> [!success]- ✅ Solution
> ```python
> def count_vowels(text):
>     vowels = {"a", "e", "i", "o", "u"}
>     count = 0
>     for ch in text.lower():
>         if ch in vowels:
>             count += 1
>     return count
> 
> print(count_vowels("hello"))  # 2
> ```

---

---

## R3: Sum of List
**Task:** Return the sum of all numbers in a list.

```python
nums = [1, 2, 3, 4]
# expected: 10
```

> [!hint]- 💡 Hint 1 (Low)
> Use a loop and a running total.

> [!hint]- 💡 Hint 2 (Mid)
> Start at 0 and add each number.

> [!hint]- 💡 Hint 3 (High)
> Python also has `sum(nums)`.

> [!success]- ✅ Solution
> ```python
> def list_sum(nums):
>     total = 0
>     for n in nums:
>         total += n
>     return total
> 
> print(list_sum([1, 2, 3, 4]))  # 10
> ```

---

---

## R4: FizzBuzz
**Task:** Print numbers 1..15 but replace:
- multiples of 3 with "Fizz"
- multiples of 5 with "Buzz"
- multiples of both with "FizzBuzz"

> [!hint]- 💡 Hint 1 (Low)
> Use a loop and `if/elif` checks.

> [!hint]- 💡 Hint 2 (Mid)
> Check for both 3 and 5 first.

> [!hint]- 💡 Hint 3 (High)
> `if n % 3 == 0 and n % 5 == 0:`

> [!success]- ✅ Solution
> ```python
> def fizzbuzz():
>     for n in range(1, 16):
>         if n % 3 == 0 and n % 5 == 0:
>             print("FizzBuzz")
>         elif n % 3 == 0:
>             print("Fizz")
>         elif n % 5 == 0:
>             print("Buzz")
>         else:
>             print(n)
> 
> fizzbuzz()
> ```

---

---

## R5: Simple Filter
**Task:** Return words longer than 3 letters.

```python
words = ["hi", "tree", "sun", "cloud"]
# expected: ["tree", "cloud"]
```

> [!hint]- 💡 Hint 1 (Low)
> Loop and check length.

> [!hint]- 💡 Hint 2 (Mid)
> Use `len(word) > 3`.

> [!hint]- 💡 Hint 3 (High)
> A list comprehension can do this.

> [!success]- ✅ Solution
> ```python
> def filter_words(words):
>     return [w for w in words if len(w) > 3]
> 
> print(filter_words(["hi", "tree", "sun", "cloud"]))
> # ['tree', 'cloud']
> ```

---

## R6: Add Two Numbers
**Task:** Add `a` and `b` and print the result.

```python
a = 3
b = 4
# expected: 7
```

> [!hint]- 💡 Hint 1 (Low)
> Use simple arithmetic or type conversion.

> [!hint]- 💡 Hint 2 (Mid)
> Assign values to variables, then compute.

> [!hint]- 💡 Hint 3 (High)
> Write one print(...) with the result.

> [!success]- ✅ Solution
> ```python
> a = 3
> b = 4
> print(a + b)
> ```

---

---

## R7: Minutes to Seconds
**Task:** Convert `minutes` to seconds and print the result.

```python
minutes = 5
# expected: 300
```

> [!hint]- 💡 Hint 1 (Low)
> Use simple arithmetic or type conversion.

> [!hint]- 💡 Hint 2 (Mid)
> Assign values to variables, then compute.

> [!hint]- 💡 Hint 3 (High)
> Write one print(...) with the result.

> [!success]- ✅ Solution
> ```python
> minutes = 5
> print(minutes * 60)
> ```

---

---

## R8: Square a Number
**Task:** Square `n` and print the result.

```python
n = 7
# expected: 49
```

> [!hint]- 💡 Hint 1 (Low)
> Use simple arithmetic or type conversion.

> [!hint]- 💡 Hint 2 (Mid)
> Assign values to variables, then compute.

> [!hint]- 💡 Hint 3 (High)
> Write one print(...) with the result.

> [!success]- ✅ Solution
> ```python
> n = 7
> print(n * n)
> ```

---

---

## R9: Average of Three
**Task:** Compute the average of `a`, `b`, and `c` and print it.

```python
a, b, c = 3, 6, 9
# expected: 6.0
```

> [!hint]- 💡 Hint 1 (Low)
> Use simple arithmetic or type conversion.

> [!hint]- 💡 Hint 2 (Mid)
> Assign values to variables, then compute.

> [!hint]- 💡 Hint 3 (High)
> Write one print(...) with the result.

> [!success]- ✅ Solution
> ```python
> a, b, c = 3, 6, 9
> print((a + b + c) / 3)
> ```

---

---

## R10: Celsius to Fahrenheit
**Task:** Convert `c` Celsius to Fahrenheit and print the result.

```python
c = 0
# expected: 32
```

> [!hint]- 💡 Hint 1 (Low)
> Use simple arithmetic or type conversion.

> [!hint]- 💡 Hint 2 (Mid)
> Assign values to variables, then compute.

> [!hint]- 💡 Hint 3 (High)
> Write one print(...) with the result.

> [!success]- ✅ Solution
> ```python
> c = 0
> print(c * 9/5 + 32)
> ```

---

---

## R11: Swap Variables
**Task:** Swap `x` and `y` and print them.

```python
x = 1
y = 2
# expected: x=2, y=1
```

> [!hint]- 💡 Hint 1 (Low)
> Use simple arithmetic or type conversion.

> [!hint]- 💡 Hint 2 (Mid)
> Assign values to variables, then compute.

> [!hint]- 💡 Hint 3 (High)
> Write one print(...) with the result.

> [!success]- ✅ Solution
> ```python
> x = 1
> y = 2
> x, y = y, x
> print(x, y)
> ```

---

---

## R12: Area of Rectangle
**Task:** Compute the area using `w` and `h` and print it.

```python
w = 4
h = 5
# expected: 20
```

> [!hint]- 💡 Hint 1 (Low)
> Use simple arithmetic or type conversion.

> [!hint]- 💡 Hint 2 (Mid)
> Assign values to variables, then compute.

> [!hint]- 💡 Hint 3 (High)
> Write one print(...) with the result.

> [!success]- ✅ Solution
> ```python
> w = 4
> h = 5
> print(w * h)
> ```

---

---

## R13: Remainder
**Task:** Compute `a % b` and print the remainder.

```python
a = 17
b = 5
# expected: 2
```

> [!hint]- 💡 Hint 1 (Low)
> Use simple arithmetic or type conversion.

> [!hint]- 💡 Hint 2 (Mid)
> Assign values to variables, then compute.

> [!hint]- 💡 Hint 3 (High)
> Write one print(...) with the result.

> [!success]- ✅ Solution
> ```python
> a = 17
> b = 5
> print(a % b)
> ```

---

---

## R14: Simple Interest
**Task:** Compute simple interest using `p * r * t` and print it.

```python
p = 1000
r = 0.05
t = 2
# expected: 100
```

> [!hint]- 💡 Hint 1 (Low)
> Use simple arithmetic or type conversion.

> [!hint]- 💡 Hint 2 (Mid)
> Assign values to variables, then compute.

> [!hint]- 💡 Hint 3 (High)
> Write one print(...) with the result.

> [!success]- ✅ Solution
> ```python
> p = 1000
> r = 0.05
> t = 2
> print(p * r * t)
> ```

---

---

## R15: Convert to Int
**Task:** Convert string `s` to an integer and print it.

```python
s = "42"
# expected: 42
```

> [!hint]- 💡 Hint 1 (Low)
> Use simple arithmetic or type conversion.

> [!hint]- 💡 Hint 2 (Mid)
> Assign values to variables, then compute.

> [!hint]- 💡 Hint 3 (High)
> Write one print(...) with the result.

> [!success]- ✅ Solution
> ```python
> s = "42"
> print(int(s))
> ```

---

---

## E3: Leap Year
**Task:** Return `True` if a year is a leap year.

Rules:
- divisible by 4
- except divisible by 100, unless also divisible by 400

> [!hint]- 💡 Hint 1 (Low)
> Check divisibility with `%`.

> [!hint]- 💡 Hint 2 (Mid)
> Order matters: 400 first, then 100, then 4.

> [!hint]- 💡 Hint 3 (High)
> A leap year is divisible by 400, or divisible by 4 but not by 100.

> [!success]- ✅ Solution
> ```python
> def is_leap(year):
>     if year % 400 == 0:
>         return True
>     if year % 100 == 0:
>         return False
>     return year % 4 == 0
> 
> print(is_leap(2000))  # True
> print(is_leap(1900))  # False
> print(is_leap(1996))  # True
> ```

---

---
