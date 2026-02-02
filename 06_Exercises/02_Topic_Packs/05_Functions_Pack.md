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

## F1: Add Function
**Task:** Solve the task below.

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

## F2: Is Even
**Task:** Solve the task below.

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

## F3: Square
**Task:** Solve the task below.

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

## F4: Max of Two
**Task:** Solve the task below.

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

## F5: Greet
**Task:** Solve the task below.

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

## F6: Default Param
**Task:** Solve the task below.

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

## F7: Sum List
**Task:** Solve the task below.

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

## F8: Count Letter
**Task:** Solve the task below.

```python
# expected: 2
```

> [!hint]- 💡 Hint 1 (Low)
> Write a simple function with return.

> [!hint]- 💡 Hint 2 (Mid)
> Use parameters and call the function.

> [!hint]- 💡 Hint 3 (High)
> Keep it short and readable.

> [!success]- ✅ Solution
> ```python
> def count_letter(text, ch):
>     return text.count(ch)
> print(count_letter('hello','l'))
> ```

---

---

## F9: Palindrome
**Task:** Solve the task below.

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

## F10: Absolute
**Task:** Solve the task below.

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
