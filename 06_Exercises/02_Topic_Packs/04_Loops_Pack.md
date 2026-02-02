# Loops Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** For/while loops practice

Notebook: [[04_Loops_Pack.ipynb]]

---

## Lo1: Print 1 to 5
**Task:** Solve the task below.

```python
# expected: 1 2 3 4 5
```

> [!hint]- 💡 Hint 1 (Low)
> Use for/while loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use break/continue when needed.

> [!hint]- 💡 Hint 3 (High)
> Print outputs as shown.

> [!success]- ✅ Solution
> ```python
> for i in range(1, 6):
>     print(i)
> ```

---

---

## Lo2: Sum 1 to 5
**Task:** Solve the task below.

```python
# expected: 15
```

> [!hint]- 💡 Hint 1 (Low)
> Use for/while loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use break/continue when needed.

> [!hint]- 💡 Hint 3 (High)
> Print outputs as shown.

> [!success]- ✅ Solution
> ```python
> total = 0
> for i in range(1, 6):
>     total += i
> print(total)
> ```

---

---

## Lo3: Count Evens
**Task:** Solve the task below.

```python
nums = [1,2,3,4]
# expected: 2
```

> [!hint]- 💡 Hint 1 (Low)
> Use for/while loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use break/continue when needed.

> [!hint]- 💡 Hint 3 (High)
> Print outputs as shown.

> [!success]- ✅ Solution
> ```python
> nums = [1,2,3,4]
> count = 0
> for n in nums:
>     if n % 2 == 0:
>         count += 1
> print(count)
> ```

---

---

## Lo4: Find First > 10
**Task:** Solve the task below.

```python
nums = [3, 8, 12, 5]
# expected: 12
```

> [!hint]- 💡 Hint 1 (Low)
> Use for/while loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use break/continue when needed.

> [!hint]- 💡 Hint 3 (High)
> Print outputs as shown.

> [!success]- ✅ Solution
> ```python
> nums = [3, 8, 12, 5]
> for n in nums:
>     if n > 10:
>         print(n)
>         break
> ```

---

---

## Lo5: While Countdown
**Task:** Solve the task below.

```python
# expected: 3 2 1
```

> [!hint]- 💡 Hint 1 (Low)
> Use for/while loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use break/continue when needed.

> [!hint]- 💡 Hint 3 (High)
> Print outputs as shown.

> [!success]- ✅ Solution
> ```python
> n = 3
> while n > 0:
>     print(n)
>     n -= 1
> ```

---

---

## Lo6: Loop over String
**Task:** Solve the task below.

```python
text = "abc"
# expected: a b c
```

> [!hint]- 💡 Hint 1 (Low)
> Use for/while loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use break/continue when needed.

> [!hint]- 💡 Hint 3 (High)
> Print outputs as shown.

> [!success]- ✅ Solution
> ```python
> text = "abc"
> for ch in text:
>     print(ch)
> ```

---

---

## Lo7: Skip Negatives
**Task:** Solve the task below.

```python
nums = [1,-2,3]
# expected: 1 3
```

> [!hint]- 💡 Hint 1 (Low)
> Use for/while loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use break/continue when needed.

> [!hint]- 💡 Hint 3 (High)
> Print outputs as shown.

> [!success]- ✅ Solution
> ```python
> nums = [1,-2,3]
> for n in nums:
>     if n < 0:
>         continue
>     print(n)
> ```

---

---

## Lo8: Nested Loop
**Task:** Solve the task below.

```python
# expected: pairs (1,1),(1,2),(2,1),(2,2)
```

> [!hint]- 💡 Hint 1 (Low)
> Use for/while loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use break/continue when needed.

> [!hint]- 💡 Hint 3 (High)
> Print outputs as shown.

> [!success]- ✅ Solution
> ```python
> for i in [1,2]:
>     for j in [1,2]:
>         print(i, j)
> ```

---

---

## Lo9: Build Squares
**Task:** Solve the task below.

```python
# expected: [1,4,9]
```

> [!hint]- 💡 Hint 1 (Low)
> Use for/while loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use break/continue when needed.

> [!hint]- 💡 Hint 3 (High)
> Print outputs as shown.

> [!success]- ✅ Solution
> ```python
> squares = []
> for i in [1,2,3]:
>     squares.append(i*i)
> print(squares)
> ```

---

---

## Lo10: Stop at 7
**Task:** Solve the task below.

```python
nums = [3,5,7,9]
# expected: 3 5
```

> [!hint]- 💡 Hint 1 (Low)
> Use for/while loops.

> [!hint]- 💡 Hint 2 (Mid)
> Use break/continue when needed.

> [!hint]- 💡 Hint 3 (High)
> Print outputs as shown.

> [!success]- ✅ Solution
> ```python
> nums = [3,5,7,9]
> for n in nums:
>     if n == 7:
>         break
>     print(n)
> ```

---

---
