# Level 2: Strings
Notebook: [[02_Level_Strings.ipynb]]


> **Difficulty:** ⭐ Beginner
> **Topics:** String Indexing, Slicing, Methods, Formatting
> **Prerequisites:** [[01_Level_Variables_Print|Level 1]], [[../../01_Python_Basics/01_Variables_and_Strings_Advanced|Strings Advanced]]

---

## Exercise 2.1: First and Last
**Task:** Given `text = "Python"`, print the first and last character.

**Expected Output:**
```
First: P
Last: n
```

> [!hint]- Hint
> Use index `[0]` for first and `[-1]` for last.

> [!success]- Solution
> ```python
> text = "Python"
> print(f"First: {text[0]}")
> print(f"Last: {text[-1]}")
> ```

---

## Exercise 2.2: String Length
**Task:** Given `sentence = "The quick brown fox"`, print how many characters it contains.

**Expected Output:**
```
Length: 19
```

> [!hint]- Hint
> Use the `len()` function.

> [!success]- Solution
> ```python
> sentence = "The quick brown fox"
> print(f"Length: {len(sentence)}")
> ```

---

## Exercise 2.3: Reverse String
**Task:** Given `word = "Hello"`, print it reversed.

**Expected Output:**
```
olleH
```

> [!hint]- Hint
> Use slicing with step -1: `[::-1]`

> [!success]- Solution
> ```python
> word = "Hello"
> print(word[::-1])
> ```

---

## Exercise 2.4: Extract Substring
**Task:** Given `text = "Hello, World!"`, extract and print only "World".

**Expected Output:**
```
World
```

> [!hint]- Hint
> Use slicing: `text[start:end]`

> [!success]- Solution
> ```python
> text = "Hello, World!"
> print(text[7:12])
> ```

---

## Exercise 2.5: Uppercase and Lowercase
**Task:** Given `text = "PyThOn"`, print it in all uppercase and all lowercase.

**Expected Output:**
```
PYTHON
python
```

> [!hint]- Hint
> Use `.upper()` and `.lower()` methods.

> [!success]- Solution
> ```python
> text = "PyThOn"
> print(text.upper())
> print(text.lower())
> ```

---

## Exercise 2.6: Title Case
**Task:** Given `sentence = "hello world from python"`, convert to title case.

**Expected Output:**
```
Hello World From Python
```

> [!hint]- Hint
> Use the `.title()` method.

> [!success]- Solution
> ```python
> sentence = "hello world from python"
> print(sentence.title())
> ```

---

## Exercise 2.7: Count Character
**Task:** Given `text = "mississippi"`, count how many times 's' appears.

**Expected Output:**
```
Count of 's': 4
```

> [!hint]- Hint
> Use the `.count()` method.

> [!success]- Solution
> ```python
> text = "mississippi"
> print(f"Count of 's': {text.count('s')}")
> ```

---

## Exercise 2.8: Find Position
**Task:** Given `text = "Hello, World!"`, find the position of "World".

**Expected Output:**
```
Position: 7
```

> [!hint]- Hint
> Use the `.find()` method.

> [!success]- Solution
> ```python
> text = "Hello, World!"
> print(f"Position: {text.find('World')}")
> ```

---

## Exercise 2.9: Replace Text
**Task:** Given `text = "I love Java"`, replace "Java" with "Python".

**Expected Output:**
```
I love Python
```

> [!hint]- Hint
> Use the `.replace()` method.

> [!success]- Solution
> ```python
> text = "I love Java"
> print(text.replace("Java", "Python"))
> ```

---

## Exercise 2.10: Check Start and End
**Task:** Given `filename = "document.pdf"`, check if it starts with "doc" and ends with ".pdf".

**Expected Output:**
```
Starts with 'doc': True
Ends with '.pdf': True
```

> [!hint]- Hint
> Use `.startswith()` and `.endswith()` methods.

> [!success]- Solution
> ```python
> filename = "document.pdf"
> print(f"Starts with 'doc': {filename.startswith('doc')}")
> print(f"Ends with '.pdf': {filename.endswith('.pdf')}")
> ```

---

## Exercise 2.11: Strip Whitespace
**Task:** Given `text = "   Hello World   "`, remove leading and trailing spaces.

**Expected Output:**
```
'Hello World'
```

> [!hint]- Hint
> Use the `.strip()` method.

> [!success]- Solution
> ```python
> text = "   Hello World   "
> print(f"'{text.strip()}'")
> ```

---

## Exercise 2.12: Split String
**Task:** Given `csv = "apple,banana,cherry"`, split into a list of fruits.

**Expected Output:**
```
['apple', 'banana', 'cherry']
```

> [!hint]- Hint
> Use `.split(',')` to split by comma.

> [!success]- Solution
> ```python
> csv = "apple,banana,cherry"
> fruits = csv.split(',')
> print(fruits)
> ```

---

## Exercise 2.13: Join Strings
**Task:** Given `words = ["Python", "is", "awesome"]`, join them with spaces.

**Expected Output:**
```
Python is awesome
```

> [!hint]- Hint
> Use `" ".join(list)` method.

> [!success]- Solution
> ```python
> words = ["Python", "is", "awesome"]
> sentence = " ".join(words)
> print(sentence)
> ```

---

## Exercise 2.14: Check Content
**Task:** Given `text = "Python3"`, check if it's alphanumeric, alphabetic, and if it contains digits.

**Expected Output:**
```
Alphanumeric: True
Alphabetic: False
Has digits: True
```

> [!hint]- Hint
> Use `.isalnum()`, `.isalpha()`, and check with `any(c.isdigit() for c in text)`

> [!success]- Solution
> ```python
> text = "Python3"
> print(f"Alphanumeric: {text.isalnum()}")
> print(f"Alphabetic: {text.isalpha()}")
> print(f"Has digits: {any(c.isdigit() for c in text)}")
> ```

---

## Exercise 2.15: String Formatting
**Task:** Given `name = "Alice"`, `age = 30`, and `city = "Berlin"`, create a formatted introduction.

**Expected Output:**
```
My name is Alice, I am 30 years old, and I live in Berlin.
```

> [!hint]- Hint
> Use an f-string with all three variables.

> [!success]- Solution
> ```python
> name = "Alice"
> age = 30
> city = "Berlin"
> print(f"My name is {name}, I am {age} years old, and I live in {city}.")
> ```

---

## 🎯 Level 2 Complete!

**Skills Practiced:**
- String indexing and slicing
- String methods (upper, lower, split, join, etc.)
- String searching and replacing
- String validation methods
- F-string formatting

**Next Level:** [[03_Level_Lists|Level 3: Lists]]
