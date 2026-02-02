# Level 5: Loops
Notebook: [[05_Level_Loops.ipynb]]


> **Difficulty:** ⭐⭐ Beginner-Intermediate
> **Topics:** for loops, while loops, range(), break, continue, enumerate
> **Prerequisites:** [[04_Level_Conditionals|Level 4]], [[../../01_Python_Basics/06_Loops_and_Iteration|Loops and Iteration]]

---

## Exercise 5.1: Count to Ten
**Task:** Print numbers from 1 to 10 using a for loop.

**Expected Output:**
```
1 2 3 4 5 6 7 8 9 10
```

> [!hint]- Hint
> Use `range(1, 11)` and `print(i, end=" ")`.

> [!success]- Solution
> ```python
> for i in range(1, 11):
>     print(i, end=" ")
> ```

---

## Exercise 5.2: Sum of Numbers
**Task:** Calculate the sum of numbers from 1 to 100 using a loop.

**Expected Output:**
```
Sum: 5050
```

> [!hint]- Hint
> Initialize a sum variable and add each number in the loop.

> [!success]- Solution
> ```python
> total = 0
> for i in range(1, 101):
>     total += i
> print(f"Sum: {total}")
> ```

---

## Exercise 5.3: Multiplication Table
**Task:** Print the multiplication table for 7 (7x1 through 7x10).

**Expected Output:**
```
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

> [!hint]- Hint
> Use a for loop with range(1, 11).

> [!success]- Solution
> ```python
> number = 7
> for i in range(1, 11):
>     print(f"{number} x {i} = {number * i}")
> ```

---

## Exercise 5.4: Iterate List
**Task:** Given `fruits = ["apple", "banana", "cherry"]`, print each fruit on a new line.

**Expected Output:**
```
apple
banana
cherry
```

> [!hint]- Hint
> Use `for fruit in fruits:`.

> [!success]- Solution
> ```python
> fruits = ["apple", "banana", "cherry"]
> for fruit in fruits:
>     print(fruit)
> ```

---

## Exercise 5.5: Enumerate Items
**Task:** Given `colors = ["red", "green", "blue"]`, print each with its index.

**Expected Output:**
```
0: red
1: green
2: blue
```

> [!hint]- Hint
> Use `enumerate()` to get index and value.

> [!success]- Solution
> ```python
> colors = ["red", "green", "blue"]
> for index, color in enumerate(colors):
>     print(f"{index}: {color}")
> ```

---

## Exercise 5.6: Countdown
**Task:** Count down from 10 to 1 and print "Liftoff!" at the end.

**Expected Output:**
```
10 9 8 7 6 5 4 3 2 1 Liftoff!
```

> [!hint]- Hint
> Use `range(10, 0, -1)` for counting down.

> [!success]- Solution
> ```python
> for i in range(10, 0, -1):
>     print(i, end=" ")
> print("Liftoff!")
> ```

---

## Exercise 5.7: While Counter
**Task:** Use a while loop to print numbers 1 to 5.

**Expected Output:**
```
1
2
3
4
5
```

> [!hint]- Hint
> Initialize counter, check condition, increment inside loop.

> [!success]- Solution
> ```python
> count = 1
> while count <= 5:
>     print(count)
>     count += 1
> ```

---

## Exercise 5.8: Find First Even
**Task:** Given `numbers = [1, 3, 5, 8, 9, 11]`, find and print the first even number, then stop.

**Expected Output:**
```
First even: 8
```

> [!hint]- Hint
> Use `break` to exit the loop early.

> [!success]- Solution
> ```python
> numbers = [1, 3, 5, 8, 9, 11]
> for num in numbers:
>     if num % 2 == 0:
>         print(f"First even: {num}")
>         break
> ```

---

## Exercise 5.9: Skip Negative
**Task:** Given `numbers = [1, -2, 3, -4, 5]`, print only positive numbers.

**Expected Output:**
```
1
3
5
```

> [!hint]- Hint
> Use `continue` to skip negative numbers.

> [!success]- Solution
> ```python
> numbers = [1, -2, 3, -4, 5]
> for num in numbers:
>     if num < 0:
>         continue
>     print(num)
> ```

---

## Exercise 5.10: Factorial
**Task:** Calculate the factorial of `n = 5` (5! = 5×4×3×2×1).

**Expected Output:**
```
5! = 120
```

> [!hint]- Hint
> Start with result = 1 and multiply in a loop.

> [!success]- Solution
> ```python
> n = 5
> factorial = 1
> for i in range(1, n + 1):
>     factorial *= i
> print(f"{n}! = {factorial}")
> ```

---

## Exercise 5.11: Pattern Print
**Task:** Print a right triangle pattern of stars with 5 rows.

**Expected Output:**
```
*
**
***
****
*****
```

> [!hint]- Hint
> Use string multiplication: `"*" * i`

> [!success]- Solution
> ```python
> for i in range(1, 6):
>     print("*" * i)
> ```

---

## Exercise 5.12: Nested Loop Grid
**Task:** Print a 3x3 grid of coordinates.

**Expected Output:**
```
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
```

> [!hint]- Hint
> Use nested for loops for rows and columns.

> [!success]- Solution
> ```python
> for row in range(3):
>     for col in range(3):
>         print(f"({row},{col})", end=" ")
>     print()
> ```

---

## Exercise 5.13: Sum Until Zero
**Task:** Keep adding user inputs until the sum exceeds 100. Use values: 25, 30, 50.

**Expected Output:**
```
Adding 25... Sum: 25
Adding 30... Sum: 55
Adding 50... Sum: 105
Sum exceeded 100!
```

> [!hint]- Hint
> Use a while loop with condition `sum <= 100`.

> [!success]- Solution
> ```python
> values = [25, 30, 50]  # Simulated inputs
> total = 0
> i = 0
>
> while total <= 100 and i < len(values):
>     total += values[i]
>     print(f"Adding {values[i]}... Sum: {total}")
>     i += 1
>
> if total > 100:
>     print("Sum exceeded 100!")
> ```

---

## Exercise 5.14: Prime Check
**Task:** Check if `number = 17` is prime using a loop.

**Expected Output:**
```
17 is prime
```

> [!hint]- Hint
> Check divisibility from 2 to sqrt(n).

> [!success]- Solution
> ```python
> number = 17
> is_prime = True
>
> if number < 2:
>     is_prime = False
> else:
>     for i in range(2, int(number ** 0.5) + 1):
>         if number % i == 0:
>             is_prime = False
>             break
>
> if is_prime:
>     print(f"{number} is prime")
> else:
>     print(f"{number} is not prime")
> ```

---

## Exercise 5.15: Zip Two Lists
**Task:** Given `names = ["Alice", "Bob", "Charlie"]` and `scores = [85, 92, 78]`, print them paired.

**Expected Output:**
```
Alice: 85
Bob: 92
Charlie: 78
```

> [!hint]- Hint
> Use `zip()` to iterate over both lists together.

> [!success]- Solution
> ```python
> names = ["Alice", "Bob", "Charlie"]
> scores = [85, 92, 78]
>
> for name, score in zip(names, scores):
>     print(f"{name}: {score}")
> ```

---

## 🎯 Level 5 Complete!

**Skills Practiced:**
- for loops with range()
- while loops
- break and continue
- enumerate() and zip()
- Nested loops
- Loop patterns

**Next Level:** [[06_Level_Functions|Level 6: Functions]]
