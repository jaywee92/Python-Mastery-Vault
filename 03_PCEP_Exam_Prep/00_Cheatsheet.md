---
title: PCEP Exam - Cheatsheet
tags: [pcep, python, exam, cheatsheet]
created: 2026-02-01
---

# 📜 PCEP Exam - Cheatsheet

**Exam: 30 questions | 40 minutes | 70% to pass**

---

## 🔢 Operators (Precedence High→Low)

```
()  **  +x -x  * / // %  + -  == != < > <= >=  not  and  or
```

**Critical Rules:**
- `10 / 2 = 5.0` (always float!)
- `-7 // 2 = -4` (rounds toward -∞)
- `-2 ** 2 = -4` (** before -)
- `2 ** 3 ** 2 = 512` (right-to-left)

---

## 📊 Types & Conversion

| Type | Falsy | Truthy |
|------|-------|--------|
| int | `0` | Any non-zero |
| float | `0.0` | Any non-zero |
| str | `""` | Any non-empty |
| list | `[]` | Any non-empty |
| dict | `{}` | Any non-empty |
| bool | `False` | `True` |
| None | `None` | - |

```python
int(3.9)    # 3 (truncates!)
int("42")   # 42
float("3.14") # 3.14
bool("")    # False
bool("0")   # True!
bool([0])   # True!
```

---

## 📝 Strings

```python
s = "Hello"
s[0]        # 'H'
s[-1]       # 'o'
s[1:4]      # 'ell'
s[::-1]     # 'olleH' (reverse)

s.find("x")   # -1 (not found)
s.index("x")  # ValueError!
s.split()     # ['Hello']
s.upper()     # 'HELLO'
len(s)        # 5
```

---

## 📋 Lists

```python
lst = [1, 2, 3]
lst.append(4)     # [1,2,3,4] (one item)
lst.extend([5,6]) # [1,2,3,4,5,6]
lst.insert(0, 0)  # Insert at index
lst.pop()         # Remove & return last
lst.remove(3)     # Remove by value
lst.sort()        # Returns None!
sorted(lst)       # Returns new list

# Copy trap!
a = [1, 2, 3]
b = a        # Same object!
b = a[:]     # Copy
```

---

## 📦 Tuples

```python
t = (1, 2, 3)
single = (1,)    # Comma required!
not_tuple = (1)  # Just int!

a, b, c = t      # Unpacking
first, *rest = t # Extended unpacking
```

---

## 📖 Dictionaries

```python
d = {"a": 1, "b": 2}
d["a"]          # 1
d.get("x")      # None (safe)
d.get("x", 0)   # 0 (default)

"a" in d        # True (checks keys!)
"1" in d        # False
1 in d.values() # True

for k, v in d.items():
    print(k, v)
```

---

## 🔁 Loops

```python
range(5)         # 0,1,2,3,4
range(1, 6)      # 1,2,3,4,5
range(0, 10, 2)  # 0,2,4,6,8
range(5, 0, -1)  # 5,4,3,2,1

for i in range(5):
    if i == 3:
        break
else:
    print("No break")  # Only runs if no break!

for i, v in enumerate(lst):
    print(i, v)
```

---

## 🔧 Functions

```python
def func(a, b=10, *args, **kwargs):
    return a + b

# *args = tuple
# **kwargs = dict

# Lambda
double = lambda x: x * 2

# Scope
x = 10
def f():
    x = 20  # Local! Global unchanged
```

---

## ⚠️ Exceptions

```python
try:
    risky()
except ValueError:
    handle()
except (TypeError, KeyError) as e:
    print(e)
else:
    no_exception()
finally:
    always_runs()  # Even with return!

# Order: specific → general
# finally overrides return!
```

---

## 🎯 Common Traps

| Trap | Wrong | Right |
|------|-------|-------|
| Division | `10/2 = 5` | `10/2 = 5.0` |
| Truncate | `int(3.9) = 4` | `int(3.9) = 3` |
| Single tuple | `(1)` | `(1,)` |
| Dict check | `val in d` | `key in d` |
| sort() | `x = lst.sort()` | `x = sorted(lst)` |
| Copy list | `b = a` | `b = a[:]` |
| find vs index | `s.index("x")` | `s.find("x")` |
| input type | `int` | `str` (always!) |

---

## ✅ Exam Tips

1. **Read twice** - Questions have traps!
2. **Watch returns** - `sort()`, `append()` return None
3. **Check types** - `input()` returns string
4. **Indexing** - Starts at 0, stop is exclusive
5. **Division** - Always returns float
6. **Truthiness** - `"0"` and `[0]` are truthy!

---

**Good luck! 🍀**

[[00_Index|← Back to Index]]
