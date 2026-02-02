---
title: Practice Questions (45 Questions!)
tags: [pcep, python, practice, exam, questions]
created: 2026-01-30
updated: 2026-02-01
---

# 📝 Practice Questions (45 Questions!)

[[00_Index|← Back to Index]] | [[19_Common_Mistakes|← Common Mistakes]]

> **"45 exam-style questions with detailed explanations!"**

**Navigation:**
- Section 1: Q1-Q4 (Fundamentals)
- Section 2: Q5-Q8 (Control Flow)
- Section 3: Q9-Q14 (Data Collections)
- Section 4: Q15-Q20 (Functions & Exceptions)
- Bonus: Q21-Q45 (Advanced Traps)

---

## Section 1: Fundamentals (18%)

### Q1: What is the output?
```python
print(10 / 4)
print(10 // 4)
print(10 % 4)
```

> [!success]- Answer
> ```
> 2.5
> 2
> 2
> ```
> - `/` always returns float
> - `//` is floor division
> - `%` is modulo (remainder)

---

### Q2: What is the output?
```python
x = -7 // 2
print(x)
```

> [!success]- Answer
> ```
> -4
> ```
> Floor division rounds toward NEGATIVE infinity, not toward zero!

---

### Q3: What is the output?
```python
print(-2 ** 2)
print((-2) ** 2)
```

> [!success]- Answer
> ```
> -4
> 4
> ```
> Exponentiation (**) has higher precedence than negation (-).

---

### Q4: What is the output?
```python
print(bool("False"))
print(bool(""))
print(bool([0]))
```

> [!success]- Answer
> ```
> True
> False
> True
> ```
> - "False" is a non-empty string → truthy
> - "" is empty string → falsy
> - [0] is non-empty list → truthy (has one element!)

---

## Section 2: Control Flow (29%)

### Q5: What is the output?
```python
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
else:
    print("done")
```

> [!success]- Answer
> ```
> 0 1 2
> ```
> `else` doesn't run because `break` was executed.

---

### Q6: What is the output?
```python
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")
else:
    print("done")
```

> [!success]- Answer
> ```
> 0 1 2 4 done
> ```
> `continue` skips 3, but loop completes normally so `else` runs.

---

### Q7: What is the output?
```python
x = 10
if x > 5:
    print("A")
elif x > 8:
    print("B")
elif x > 3:
    print("C")
else:
    print("D")
```

> [!success]- Answer
> ```
> A
> ```
> Only the FIRST true condition executes. Even though x > 8 is also true, it's never reached.

---

### Q8: What is the output?
```python
print(list(range(5, 0, -2)))
```

> [!success]- Answer
> ```
> [5, 3, 1]
> ```
> Starts at 5, steps by -2, stops before 0.

---

## Section 3: Data Collections (25%)

### Q9: What is the output?
```python
s = "Python"
print(s[1:4])
print(s[-2:])
print(s[::-1])
```

> [!success]- Answer
> ```
> yth
> on
> nohtyP
> ```
> - `[1:4]` = indices 1, 2, 3
> - `[-2:]` = last 2 characters
> - `[::-1]` = reversed

---

### Q10: What is the output?
```python
lst = [1, 2, 3]
lst.append([4, 5])
print(lst)
print(len(lst))
```

> [!success]- Answer
> ```
> [1, 2, 3, [4, 5]]
> 4
> ```
> `append()` adds the list as ONE element.

---

### Q11: What is the output?
```python
t = (1, 2, 3)
t = t + (4,)
print(t)
```

> [!success]- Answer
> ```
> (1, 2, 3, 4)
> ```
> Tuples are immutable, but you can create a new tuple with concatenation.

---

### Q12: What is the output?
```python
d = {"a": 1, "b": 2}
print("a" in d)
print(1 in d)
```

> [!success]- Answer
> ```
> True
> False
> ```
> `in` checks KEYS, not values!

---

### Q13: What is the output?
```python
s = "hello"
print(s.find("x"))
# print(s.index("x"))  # What would this do?
```

> [!success]- Answer
> ```
> -1
> ```
> `find()` returns -1 if not found.
> `index()` would raise `ValueError`!

---

### Q14: What is the output?
```python
nums = [3, 1, 2]
result = nums.sort()
print(result)
print(nums)
```

> [!success]- Answer
> ```
> None
> [1, 2, 3]
> ```
> `sort()` modifies in place and returns None!

---

## Section 4: Functions & Exceptions (28%)

### Q15: What is the output?
```python
def func(a, b=10, c=20):
    return a + b + c

print(func(1))
print(func(1, 2))
print(func(1, c=3))
```

> [!success]- Answer
> ```
> 31
> 23
> 14
> ```
> - `func(1)`: a=1, b=10, c=20 → 31
> - `func(1, 2)`: a=1, b=2, c=20 → 23
> - `func(1, c=3)`: a=1, b=10, c=3 → 14

---

### Q16: What is the output?
```python
def add(a, b):
    print(a + b)

result = add(2, 3)
print(result)
```

> [!success]- Answer
> ```
> 5
> None
> ```
> Function prints 5, but returns None (no return statement).

---

### Q17: What is the output?
```python
x = 10
def func():
    x = 20
    print(x)

func()
print(x)
```

> [!success]- Answer
> ```
> 20
> 10
> ```
> Local `x` shadows global `x`. Global `x` is unchanged.

---

### Q18: What is the output?
```python
try:
    x = int("hello")
except ValueError:
    print("A")
except:
    print("B")
else:
    print("C")
finally:
    print("D")
```

> [!success]- Answer
> ```
> A
> D
> ```
> - ValueError is caught, prints "A"
> - finally always runs, prints "D"
> - else only runs if NO exception

---

### Q19: What is the output?
```python
double = lambda x: x * 2
print(double(5))
print(type(double))
```

> [!success]- Answer
> ```
> 10
> <class 'function'>
> ```
> Lambda is a function that returns x * 2.

---

### Q20: What is the output?
```python
def func(*args, **kwargs):
    print(type(args))
    print(type(kwargs))

func(1, 2, 3, a=4, b=5)
```

> [!success]- Answer
> ```
> <class 'tuple'>
> <class 'dict'>
> ```
> `*args` is a tuple, `**kwargs` is a dict.

---

## 🔥 More Practice Questions (Advanced Traps)

### Q21: What is the output?
```python
print(2 ** 3 ** 2)
```

> [!success]- Answer
> ```
> 512
> ```
> Exponentiation is RIGHT-TO-LEFT associative!
> - First: 3 ** 2 = 9
> - Then: 2 ** 9 = 512

---

### Q22: What is the output?
```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

> [!success]- Answer
> ```
> [1, 2, 3, 4]
> ```
> Assignment creates a REFERENCE, not a copy! Both x and y point to the same list.

---

### Q23: What is the output?
```python
print(type((1)))
print(type((1,)))
```

> [!success]- Answer
> ```
> <class 'int'>
> <class 'tuple'>
> ```
> Single element tuple needs a COMMA! `(1)` is just an int, `(1,)` is a tuple.

---

### Q24: What is the output?
```python
a = [1, 2, 3]
b = a[:]
b[0] = 100
print(a[0])
```

> [!success]- Answer
> ```
> 1
> ```
> `a[:]` creates a COPY. Modifying b doesn't affect a.

---

### Q25: What is the output?
```python
print("hello".replace("l", "L", 1))
```

> [!success]- Answer
> ```
> heLlo
> ```
> The third argument limits replacements to 1.

---

### Q26: What is the output?
```python
x = 5 and 10
y = 0 or 20
print(x, y)
```

> [!success]- Answer
> ```
> 10 20
> ```
> `and` returns last value if all truthy; `or` returns first truthy value.

---

### Q27: What is the output?
```python
def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())
```

> [!success]- Answer
> ```
> [1]
> [1, 1]
> ```
> TRAP! Mutable default argument is shared between calls!

---

### Q28: What is the output?
```python
s = "Python"
print(s[100:200])
```

> [!success]- Answer
> ```
> (empty string)
> ```
> Slicing never raises IndexError! Out-of-bounds slices return empty sequence.

---

### Q29: What is the output?
```python
print(round(2.5))
print(round(3.5))
```

> [!success]- Answer
> ```
> 2
> 4
> ```
> Python uses BANKER'S ROUNDING (round half to even).

---

### Q30: What is the output?
```python
d = {}
d[1] = "a"
d["1"] = "b"
d[1.0] = "c"
print(d)
```

> [!success]- Answer
> ```
> {1: 'c', '1': 'b'}
> ```
> 1 and 1.0 are equal and hash the same, so 1.0 overwrites 1!

---

### Q31: What is the output?
```python
try:
    print("A")
    raise ValueError
    print("B")
except:
    print("C")
finally:
    print("D")
```

> [!success]- Answer
> ```
> A
> C
> D
> ```
> "B" never prints because exception is raised before it.

---

### Q32: What is the output?
```python
lst = [1, 2, 3, 4, 5]
print(lst[1:4:2])
```

> [!success]- Answer
> ```
> [2, 4]
> ```
> Start at index 1, end before 4, step by 2: indices 1, 3 → values 2, 4.

---

### Q33: What is the output?
```python
print("   hello   ".strip().upper())
```

> [!success]- Answer
> ```
> HELLO
> ```
> `strip()` removes whitespace, `upper()` converts to uppercase. Methods chain!

---

### Q34: What is the output?
```python
x = 10
def outer():
    x = 20
    def inner():
        print(x)
    inner()

outer()
print(x)
```

> [!success]- Answer
> ```
> 20
> 10
> ```
> `inner()` sees x=20 from enclosing scope. Global x remains 10.

---

### Q35: What is the output?
```python
print(list(filter(lambda x: x > 0, [-1, 0, 1, 2])))
```

> [!success]- Answer
> ```
> [1, 2]
> ```
> `filter()` keeps elements where the function returns True.

---

### Q36: What is the output?
```python
a, *b, c = [1, 2, 3, 4, 5]
print(b)
```

> [!success]- Answer
> ```
> [2, 3, 4]
> ```
> Extended unpacking: a=1, c=5, b gets the rest as a LIST.

---

### Q37: What is the output?
```python
print("abc" * 2 + "def")
```

> [!success]- Answer
> ```
> abcabcdef
> ```
> String repetition (*) before concatenation (+).

---

### Q38: What is the output?
```python
d = {"a": 1, "b": 2}
print(d.get("c", d.get("a")))
```

> [!success]- Answer
> ```
> 1
> ```
> "c" not found, so default is `d.get("a")` which returns 1.

---

### Q39: What is the output?
```python
print([x for x in range(10) if x % 2 == 0 if x % 3 == 0])
```

> [!success]- Answer
> ```
> [0, 6]
> ```
> Multiple if conditions act as AND. Numbers divisible by BOTH 2 and 3.

---

### Q40: What is the output?
```python
def func(a, b, *args, c=10):
    return a + b + sum(args) + c

print(func(1, 2, 3, 4, c=5))
```

> [!success]- Answer
> ```
> 15
> ```
> a=1, b=2, args=(3,4), c=5 → 1+2+7+5 = 15.

---

### Q41: What is the output?
```python
print(all([]))
print(any([]))
```

> [!success]- Answer
> ```
> True
> False
> ```
> `all([])` is vacuously True (no False elements). `any([])` is False (no True elements).

---

### Q42: What is the output?
```python
x = "hello"
print(x[1:1])
print(x[2:2])
```

> [!success]- Answer
> ```
> (empty string)
> (empty string)
> ```
> When start equals stop, slice is empty.

---

### Q43: What is the output?
```python
try:
    1 / 0
except ZeroDivisionError:
    print("A")
    raise
except:
    print("B")
```

> [!success]- Answer
> ```
> A
> ZeroDivisionError: division by zero
> ```
> `raise` re-raises the caught exception after printing "A".

---

### Q44: What is the output?
```python
print({1, 2, 3} & {2, 3, 4})
print({1, 2, 3} | {2, 3, 4})
```

> [!success]- Answer
> ```
> {2, 3}
> {1, 2, 3, 4}
> ```
> `&` is intersection, `|` is union.

---

### Q45: What is the output?
```python
nums = [1, 2, 3]
nums.insert(10, 99)
print(nums)
```

> [!success]- Answer
> ```
> [1, 2, 3, 99]
> ```
> `insert()` with index beyond list length appends to end.

---

## 🎯 Final Tips

1. **Read CAREFULLY** - Exam questions often have subtle traps
2. **Watch for return values** - Many methods return None
3. **Remember precedence** - When in doubt, use parentheses
4. **Know your falsy values** - 0, 0.0, "", [], {}, None
5. **Division is float** - 10/2 = 5.0, not 5
6. **Indexing starts at 0** - First element is [0]
7. **Stop is exclusive** - range(5) gives 0,1,2,3,4
8. **in checks keys** - For dicts, "x" in d checks keys

---

## ✅ Good Luck on Your Exam!

**Remember:**
- 30 questions
- 40 minutes
- 70% to pass (21+ correct)
- Read each question twice!

---

[[19_Common_Mistakes|← Common Mistakes]] | [[00_Index|Index]]
