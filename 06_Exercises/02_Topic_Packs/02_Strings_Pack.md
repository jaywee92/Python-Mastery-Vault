# Strings Pack

> **Difficulty:** ⭐ - ⭐⭐⭐
> **Focus:** Strings, slicing, and text problems

Notebook: [[02_Strings_Pack.ipynb]]

---

## S1: First and Last
**Task:** Return the first and last character as a tuple.

```python
text = "python"
# expected: ('p', 'n')
```

> [!hint]- 💡 Hint 1 (Low)
> Use indexing with `0` and `-1`.

> [!hint]- 💡 Hint 2 (Mid)
> Strings support negative indexing.

> [!hint]- 💡 Hint 3 (High)
> `return (text[0], text[-1])`

> [!success]- ✅ Solution
> ```python
> def first_last(text):
>     return (text[0], text[-1])
> 
> print(first_last("python"))  # ('p', 'n')
> ```

---

---

## S2: Count Letter
**Task:** Count how often a letter appears in a string.

```python
text = "banana"
letter = "a"
# expected: 3
```

> [!hint]- 💡 Hint 1 (Low)
> Python has a string method for counting.

> [!hint]- 💡 Hint 2 (Mid)
> Use `text.count(letter)`.

> [!hint]- 💡 Hint 3 (High)
> Return the count as an integer.

> [!success]- ✅ Solution
> ```python
> def count_letter(text, letter):
>     return text.count(letter)
> 
> print(count_letter("banana", "a"))  # 3
> ```

---

---

## S3: Title Case
**Task:** Capitalize the first letter of every word.

```python
text = "hello world"
# expected: "Hello World"
```

> [!hint]- 💡 Hint 1 (Low)
> Split the string into words.

> [!hint]- 💡 Hint 2 (Mid)
> Use `word.capitalize()` on each word.

> [!hint]- 💡 Hint 3 (High)
> Join the words with spaces.

> [!success]- ✅ Solution
> ```python
> def title_case(text):
>     return " ".join(word.capitalize() for word in text.split())
> 
> print(title_case("hello world"))  # Hello World
> ```

---

---

## S4: Remove Vowels
**Task:** Remove all vowels from a string.

```python
text = "developer"
# expected: "dvlpr"
```

> [!hint]- 💡 Hint 1 (Low)
> Check each character.

> [!hint]- 💡 Hint 2 (Mid)
> Use a set of vowels.

> [!hint]- 💡 Hint 3 (High)
> Build a new string with only non-vowels.

> [!success]- ✅ Solution
> ```python
> def remove_vowels(text):
>     vowels = {"a", "e", "i", "o", "u"}
>     return "".join(ch for ch in text if ch.lower() not in vowels)
> 
> print(remove_vowels("developer"))  # dvlpr
> ```

---

---

## S5: Palindrome Check
**Task:** Return `True` if the string is a palindrome.

```python
text = "racecar"
# expected: True
```

> [!hint]- 💡 Hint 1 (Low)
> Compare the string to its reverse.

> [!hint]- 💡 Hint 2 (Mid)
> Use slicing with `[::-1]`.

> [!hint]- 💡 Hint 3 (High)
> `text == text[::-1]`.

> [!success]- ✅ Solution
> ```python
> def is_palindrome(text):
>     return text == text[::-1]
> 
> print(is_palindrome("racecar"))  # True
> ```

---

## S1: Reverse String
**Task:** Solve the task below.

```python
text = "hello"
# expected: "olleh"
```

> [!hint]- 💡 Hint 1 (Low)
> Work with string methods or slicing.

> [!hint]- 💡 Hint 2 (Mid)
> Use slicing with step -1.

> [!hint]- 💡 Hint 3 (High)
> Keep it one line with print(...).

> [!success]- ✅ Solution
> ```python
> text = "hello"
> print(text[::-1])
> ```

---

---

## S2: First 3 Chars
**Task:** Solve the task below.

```python
text = "python"
# expected: "pyt"
```

> [!hint]- 💡 Hint 1 (Low)
> Work with string methods or slicing.

> [!hint]- 💡 Hint 2 (Mid)
> Use slicing.

> [!hint]- 💡 Hint 3 (High)
> Keep it one line with print(...).

> [!success]- ✅ Solution
> ```python
> text = "python"
> print(text[:3])
> ```

---

---

## S3: Last 3 Chars
**Task:** Solve the task below.

```python
text = "python"
# expected: "hon"
```

> [!hint]- 💡 Hint 1 (Low)
> Work with string methods or slicing.

> [!hint]- 💡 Hint 2 (Mid)
> Use negative slicing.

> [!hint]- 💡 Hint 3 (High)
> Keep it one line with print(...).

> [!success]- ✅ Solution
> ```python
> text = "python"
> print(text[-3:])
> ```

---

---

## S4: Uppercase
**Task:** Solve the task below.

```python
text = "hi"
# expected: "HI"
```

> [!hint]- 💡 Hint 1 (Low)
> Work with string methods or slicing.

> [!hint]- 💡 Hint 2 (Mid)
> Use `.upper()`.

> [!hint]- 💡 Hint 3 (High)
> Keep it one line with print(...).

> [!success]- ✅ Solution
> ```python
> text = "hi"
> print(text.upper())
> ```

---

---

## S5: Replace Space
**Task:** Solve the task below.

```python
text = "a b"
# expected: "a-b"
```

> [!hint]- 💡 Hint 1 (Low)
> Work with string methods or slicing.

> [!hint]- 💡 Hint 2 (Mid)
> Use `.replace()`.

> [!hint]- 💡 Hint 3 (High)
> Keep it one line with print(...).

> [!success]- ✅ Solution
> ```python
> text = "a b"
> print(text.replace(' ', '-'))
> ```

---

---

## S6: Count a
**Task:** Solve the task below.

```python
text = "banana"
# expected: 3
```

> [!hint]- 💡 Hint 1 (Low)
> Work with string methods or slicing.

> [!hint]- 💡 Hint 2 (Mid)
> Use `.count()`.

> [!hint]- 💡 Hint 3 (High)
> Keep it one line with print(...).

> [!success]- ✅ Solution
> ```python
> text = "banana"
> print(text.count('a'))
> ```

---

---

## S7: Starts With
**Task:** Solve the task below.

```python
text = "python"
# expected: True
```

> [!hint]- 💡 Hint 1 (Low)
> Work with string methods or slicing.

> [!hint]- 💡 Hint 2 (Mid)
> Use `.startswith()`.

> [!hint]- 💡 Hint 3 (High)
> Keep it one line with print(...).

> [!success]- ✅ Solution
> ```python
> text = "python"
> print(text.startswith('py'))
> ```

---

---

## S8: Ends With
**Task:** Solve the task below.

```python
text = "python"
# expected: True
```

> [!hint]- 💡 Hint 1 (Low)
> Work with string methods or slicing.

> [!hint]- 💡 Hint 2 (Mid)
> Use `.endswith()`.

> [!hint]- 💡 Hint 3 (High)
> Keep it one line with print(...).

> [!success]- ✅ Solution
> ```python
> text = "python"
> print(text.endswith('on'))
> ```

---

---

## S9: Split Words
**Task:** Solve the task below.

```python
text = "hi there"
# expected: ['hi','there']
```

> [!hint]- 💡 Hint 1 (Low)
> Work with string methods or slicing.

> [!hint]- 💡 Hint 2 (Mid)
> Use `.split()`.

> [!hint]- 💡 Hint 3 (High)
> Keep it one line with print(...).

> [!success]- ✅ Solution
> ```python
> text = "hi there"
> print(text.split())
> ```

---

---

## S10: Join Words
**Task:** Solve the task below.

```python
words = ['hi','there']
# expected: "hi there"
```

> [!hint]- 💡 Hint 1 (Low)
> Work with string methods or slicing.

> [!hint]- 💡 Hint 2 (Mid)
> Use `' '.join(...)`.

> [!hint]- 💡 Hint 3 (High)
> Keep it one line with print(...).

> [!success]- ✅ Solution
> ```python
> words = ['hi','there']
> print(' '.join(words))
> ```

---

---

## E1: Two Fer
**Task:** Return a sentence that includes a name. If no name is given, use "you".

Expected examples:
```
One for Alice, one for me.
One for you, one for me.
```

> [!hint]- 💡 Hint 1 (Low)
> Use a default value for the name.

> [!hint]- 💡 Hint 2 (Mid)
> A function parameter can have a default: `name="you"`.

> [!hint]- 💡 Hint 3 (High)
> Use an f-string to build the sentence.

> [!success]- ✅ Solution
> ```python
> def two_fer(name="you"):
>     return f"One for {name}, one for me."
> 
> print(two_fer("Alice"))  # One for Alice, one for me.
> print(two_fer())          # One for you, one for me.
> ```

---

---

## E2: Reverse String
**Task:** Return the reverse of a string.

Examples:
```
"stressed" -> "desserts"
"racecar"  -> "racecar"
```

> [!hint]- 💡 Hint 1 (Low)
> Python can slice strings.

> [!hint]- 💡 Hint 2 (Mid)
> Use `text[::-1]`.

> [!hint]- 💡 Hint 3 (High)
> Or build a new string by iterating backwards.

> [!success]- ✅ Solution
> ```python
> def reverse_string(text):
>     return text[::-1]
> 
> print(reverse_string("stressed"))  # desserts
> ```

---

---

## E4: Hamming Distance
**Task:** Count the differences between two equal-length DNA strings.

Example:
```
"GAGC" vs "GATC" -> 1
```

> [!hint]- 💡 Hint 1 (Low)
> Compare characters at the same index.

> [!hint]- 💡 Hint 2 (Mid)
> Use `zip(a, b)`.

> [!hint]- 💡 Hint 3 (High)
> Raise `ValueError` if lengths differ.

> [!success]- ✅ Solution
> ```python
> def hamming(a, b):
>     if len(a) != len(b):
>         raise ValueError("Strands must be of equal length.")
>     count = 0
>     for x, y in zip(a, b):
>         if x != y:
>             count += 1
>     return count
> 
> print(hamming("GAGC", "GATC"))  # 1
> ```

---
