# Files & Exceptions Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** File I/O and error handling

Notebook: [[07_Files_Exceptions_Pack.ipynb]]

---

## FE1: Write File
**Task:** Solve the task below.

```python
# write 'hello' to file.txt
```

> [!hint]- 💡 Hint 1 (Low)
> Use open() with correct mode.

> [!hint]- 💡 Hint 2 (Mid)
> Use try/except for errors.

> [!hint]- 💡 Hint 3 (High)
> Keep file handling minimal.

> [!success]- ✅ Solution
> ```python
> with open('file.txt','w') as f:
>     f.write('hello')
> ```

---

---

## FE2: Read File
**Task:** Solve the task below.

```python
# read file.txt
```

> [!hint]- 💡 Hint 1 (Low)
> Use open() with correct mode.

> [!hint]- 💡 Hint 2 (Mid)
> Use try/except for errors.

> [!hint]- 💡 Hint 3 (High)
> Keep file handling minimal.

> [!success]- ✅ Solution
> ```python
> with open('file.txt','r') as f:
>     print(f.read())
> ```

---

---

## FE3: Append File
**Task:** Solve the task below.

```python
# append 'world'
```

> [!hint]- 💡 Hint 1 (Low)
> Use open() with correct mode.

> [!hint]- 💡 Hint 2 (Mid)
> Use try/except for errors.

> [!hint]- 💡 Hint 3 (High)
> Keep file handling minimal.

> [!success]- ✅ Solution
> ```python
> with open('file.txt','a') as f:
>     f.write('world')
> ```

---

---

## FE4: Read Lines
**Task:** Solve the task below.

```python
# print lines
```

> [!hint]- 💡 Hint 1 (Low)
> Use open() with correct mode.

> [!hint]- 💡 Hint 2 (Mid)
> Use try/except for errors.

> [!hint]- 💡 Hint 3 (High)
> Keep file handling minimal.

> [!success]- ✅ Solution
> ```python
> with open('file.txt','r') as f:
>     for line in f:
>         print(line.strip())
> ```

---

---

## FE5: Try/Except
**Task:** Solve the task below.

```python
# handle division by zero
```

> [!hint]- 💡 Hint 1 (Low)
> Use open() with correct mode.

> [!hint]- 💡 Hint 2 (Mid)
> Use try/except for errors.

> [!hint]- 💡 Hint 3 (High)
> Keep file handling minimal.

> [!success]- ✅ Solution
> ```python
> try:
>     print(1/0)
> except ZeroDivisionError:
>     print('error')
> ```

---

---

## FE6: Convert with try
**Task:** Solve the task below.

```python
s='x'
# expected: handle ValueError
```

> [!hint]- 💡 Hint 1 (Low)
> Use open() with correct mode.

> [!hint]- 💡 Hint 2 (Mid)
> Use try/except for errors.

> [!hint]- 💡 Hint 3 (High)
> Keep file handling minimal.

> [!success]- ✅ Solution
> ```python
> s='x'
> try:
>     print(int(s))
> except ValueError:
>     print('not a number')
> ```

---

---

## FE7: Finally
**Task:** Solve the task below.

```python
# always print Done
```

> [!hint]- 💡 Hint 1 (Low)
> Use open() with correct mode.

> [!hint]- 💡 Hint 2 (Mid)
> Use try/except for errors.

> [!hint]- 💡 Hint 3 (High)
> Keep file handling minimal.

> [!success]- ✅ Solution
> ```python
> try:
>     x=1
> finally:
>     print('Done')
> ```

---

---

## FE8: Raise Error
**Task:** Solve the task below.

```python
# raise ValueError
```

> [!hint]- 💡 Hint 1 (Low)
> Use open() with correct mode.

> [!hint]- 💡 Hint 2 (Mid)
> Use try/except for errors.

> [!hint]- 💡 Hint 3 (High)
> Keep file handling minimal.

> [!success]- ✅ Solution
> ```python
> raise ValueError('bad input')
> ```

---

---

## FE9: Check File Exists
**Task:** Solve the task below.

```python
# print True if file exists
```

> [!hint]- 💡 Hint 1 (Low)
> Use open() with correct mode.

> [!hint]- 💡 Hint 2 (Mid)
> Use try/except for errors.

> [!hint]- 💡 Hint 3 (High)
> Keep file handling minimal.

> [!success]- ✅ Solution
> ```python
> import os
> print(os.path.exists('file.txt'))
> ```

---

---

## FE10: Read JSON
**Task:** Solve the task below.

```python
# read data.json
```

> [!hint]- 💡 Hint 1 (Low)
> Use open() with correct mode.

> [!hint]- 💡 Hint 2 (Mid)
> Use try/except for errors.

> [!hint]- 💡 Hint 3 (High)
> Keep file handling minimal.

> [!success]- ✅ Solution
> ```python
> import json
> with open('data.json','r') as f:
>     data = json.load(f)
> print(data)
> ```

---

---
