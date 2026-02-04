# Functions Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** Functions and return values

Notebook: [[05_Functions_Pack.ipynb]]

---

## F1: Convert to Title
**Task:** Create a function that title-cases a sentence.

```python
text = "hello from python"
# expected: "Hello From Python"
```

> [!hint]- 💡 Hint 1 (Low)
> Split the sentence into words.

> [!hint]- 💡 Hint 2 (Mid)
> Use `word.capitalize()`.

> [!hint]- 💡 Hint 3 (High)
> Join words with spaces.

> [!success]- ✅ Solution
> ```python
> def title_case(text):
>     return " ".join(word.capitalize() for word in text.split())
> 
> print(title_case("hello from python"))  # Hello From Python
> ```

---

---

## F2: Greeting with Default
**Task:** Write a function that greets someone, defaulting to "friend".

```python
# expected: "Hello, friend!"
# expected: "Hello, Alice!"
```

> [!hint]- 💡 Hint 1 (Low)
> Use a default parameter.

> [!hint]- 💡 Hint 2 (Mid)
> `def greet(name="friend"):`

> [!hint]- 💡 Hint 3 (High)
> Return the string instead of printing it.

> [!success]- ✅ Solution
> ```python
> def greet(name="friend"):
>     return f"Hello, {name}!"
> 
> print(greet())
> print(greet("Alice"))
> ```

---

---

## F3: Apply Function
**Task:** Write a function that applies another function to each value.

```python
nums = [1, 2, 3]
# expected: [2, 4, 6] if function doubles
```

> [!hint]- 💡 Hint 1 (Low)
> A function can be passed as an argument.

> [!hint]- 💡 Hint 2 (Mid)
> Use a loop and call `func(value)`.

> [!hint]- 💡 Hint 3 (High)
> Return a new list of results.

> [!success]- ✅ Solution
> ```python
> def apply_to_all(nums, func):
>     results = []
>     for n in nums:
>         results.append(func(n))
>     return results
> 
> def double(x):
>     return x * 2
> 
> print(apply_to_all([1, 2, 3], double))  # [2, 4, 6]
> ```

---

---

## F4: Count Words
**Task:** Count words in a sentence.

```python
text = "python is fun"
# expected: 3
```

> [!hint]- 💡 Hint 1 (Low)
> Use `split()`.

> [!hint]- 💡 Hint 2 (Mid)
> The number of words is the length of the list.

> [!hint]- 💡 Hint 3 (High)
> `return len(text.split())`

> [!success]- ✅ Solution
> ```python
> def count_words(text):
>     return len(text.split())
> 
> print(count_words("python is fun"))  # 3
> ```

---

---

## F5: Simple Calculator
**Task:** Write a function that applies `+`, `-`, `*`, or `/`.

```python
calc(6, 2, "+")  # 8
calc(6, 2, "*")  # 12
```

> [!hint]- 💡 Hint 1 (Low)
> Use `if/elif` checks for the operator.

> [!hint]- 💡 Hint 2 (Mid)
> Return the result instead of printing.

> [!hint]- 💡 Hint 3 (High)
> Handle division carefully (float).

> [!success]- ✅ Solution
> ```python
> def calc(a, b, op):
>     if op == "+":
>         return a + b
>     if op == "-":
>         return a - b
>     if op == "*":
>         return a * b
>     if op == "/":
>         return a / b
>     raise ValueError("Unknown operator")
> 
> print(calc(6, 2, "+"))  # 8
> print(calc(6, 2, "*"))  # 12
> ```

---

## F6: Add Function
**Task:** Write `add(a, b)` that returns the sum.

```python
# expected: add(2,3) -> 5
```

> [!hint]- 💡 Hint 1 (Low)
> Write a simple function with return.

> [!hint]- 💡 Hint 2 (Mid)
> Use parameters and call the function.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> def add(a,b):
>     return a + b
> print(add(2,3))
> ```

---

---

## F7: Is Even
**Task:** Write `is_even(n)` that returns True if `n` is even.

```python
# expected: True for 4
```

> [!hint]- 💡 Hint 1 (Low)
> Write a simple function with return.

> [!hint]- 💡 Hint 2 (Mid)
> Use parameters and call the function.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> def is_even(n):
>     return n % 2 == 0
> print(is_even(4))
> ```

---

---

## F8: Square
**Task:** Write `square(n)` that returns `n * n`.

```python
# expected: 9 for 3
```

> [!hint]- 💡 Hint 1 (Low)
> Write a simple function with return.

> [!hint]- 💡 Hint 2 (Mid)
> Use parameters and call the function.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> def square(n):
>     return n*n
> print(square(3))
> ```

---

---

## F9: Max of Two
**Task:** Write `max_of_two(a, b)` that returns the larger value.

```python
# expected: 7
```

> [!hint]- 💡 Hint 1 (Low)
> Write a simple function with return.

> [!hint]- 💡 Hint 2 (Mid)
> Use parameters and call the function.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> def max2(a,b):
>     return a if a>b else b
> print(max2(7,2))
> ```

---

---

## F10: Greet
**Task:** Write `greet(name)` that returns `"Hi, <name>"`.

```python
# expected: Hi, Ana
```

> [!hint]- 💡 Hint 1 (Low)
> Write a simple function with return.

> [!hint]- 💡 Hint 2 (Mid)
> Use parameters and call the function.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> def greet(name):
>     return f"Hi, {name}"
> print(greet('Ana'))
> ```

---

---

## F11: Default Param
**Task:** Write `greet(name='friend')` and return a greeting.

```python
# expected: Hi, friend
```

> [!hint]- 💡 Hint 1 (Low)
> Write a simple function with return.

> [!hint]- 💡 Hint 2 (Mid)
> Use parameters and call the function.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> def greet(name='friend'):
>     return f"Hi, {name}"
> print(greet())
> ```

---

---

## F12: Sum List
**Task:** Write a function that returns the sum of a list.

```python
nums=[1,2,3]
# expected: 6
```

> [!hint]- 💡 Hint 1 (Low)
> Write a simple function with return.

> [!hint]- 💡 Hint 2 (Mid)
> Use parameters and call the function.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> def sum_list(nums):
>     total = 0
>     for n in nums:
>         total += n
>     return total
> print(sum_list([1,2,3]))
> ```

---

---

## F13: Count Digits
**Task:** Count how many digits are in a string.

```python
text = "a1b2c3"
# expected: 3
```

> [!hint]- 💡 Hint 1 (Low)
> Check each character in the string.

> [!hint]- 💡 Hint 2 (Mid)
> Use `ch.isdigit()` to test digits.

> [!hint]- 💡 Hint 3 (High)
> Increment a counter for each digit.

> [!success]- ✅ Solution
> ```python
> def count_digits(text):
>     count = 0
>     for ch in text:
>         if ch.isdigit():
>             count += 1
>     return count
> 
> print(count_digits("a1b2c3"))  # 3
> ```

---

---

## F14: Palindrome
**Task:** Return True if the string reads the same backward.

```python
# expected: True
```

> [!hint]- 💡 Hint 1 (Low)
> Write a simple function with return.

> [!hint]- 💡 Hint 2 (Mid)
> Use parameters and call the function.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> def is_pal(text):
>     return text == text[::-1]
> print(is_pal('racecar'))
> ```

---

---

## F15: Absolute
**Task:** Return the absolute value of a number.

```python
# expected: 3
```

> [!hint]- 💡 Hint 1 (Low)
> Write a simple function with return.

> [!hint]- 💡 Hint 2 (Mid)
> Use parameters and call the function.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> def absolute(n):
>     return n if n>=0 else -n
> print(absolute(-3))
> ```

---

---
