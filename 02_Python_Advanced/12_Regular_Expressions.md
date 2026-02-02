---
title: Regular Expressions
tags: [python, regex, regular-expressions, text, exam-essential]
created: 2026-01-26
exam_weight: medium
difficulty: intermediate-advanced
---

# 🔍 Regular Expressions

[[00_Index|← Back to Index]] | [[24_Standard_Library|← Standard Library]] | [[26_Working_with_Dates|Working with Dates →]]

> **"Some people, when confronted with a problem, think: 'I know, I'll use regex!' Now they have two problems."**

---

## 🎯 What are Regular Expressions?

Regex are patterns for searching, matching, and replacing text.

```
┌─────────────────────────────────────────────────────────────────┐
│                    WHEN TO USE REGEX?                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ✅ Pattern matching              Emails, URLs, phone numbers   │
│  ✅ Validate data                 Postal codes, IDs             │
│  ✅ Extract text                  Parse values from logs        │
│  ✅ Search & replace              Complex transformations       │
│                                                                  │
│  ❌ NOT for:                                                     │
│  - Simple string operations (split, find, replace)              │
│  - HTML/XML parsing (use parsers!)                              │
│  - When str methods are sufficient                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📚 Basics

### Import module

```python
import re

# ALWAYS use r'' (raw strings)!
pattern = r'\d+'      # ✅ Raw string
pattern = '\\d+'      # ❌ Escaped - works, but unreadable
```

### Most important functions

```python
import re

text = "My number is 0123-456789 and 0987-654321"
pattern = r'\d{4}-\d{6}'

# ═══════════════════════════════════════════════════════════════
# RE.SEARCH - Find first match
# ═══════════════════════════════════════════════════════════════
match = re.search(pattern, text)
if match:
    print(match.group())             # '0123-456789'
    print(match.start())             # 20 (start position)
    print(match.end())               # 31 (end position)
    print(match.span())              # (20, 31)

# ═══════════════════════════════════════════════════════════════
# RE.MATCH - Only match at start
# ═══════════════════════════════════════════════════════════════
print(re.match(r'\d+', '123abc'))    # Match! '123'
print(re.match(r'\d+', 'abc123'))    # None (must be at start!)

# ═══════════════════════════════════════════════════════════════
# RE.FULLMATCH - Entire string must match
# ═══════════════════════════════════════════════════════════════
print(re.fullmatch(r'\d+', '123'))      # Match!
print(re.fullmatch(r'\d+', '123abc'))   # None

# ═══════════════════════════════════════════════════════════════
# RE.FINDALL - All matches as list
# ═══════════════════════════════════════════════════════════════
numbers = re.findall(r'\d{4}-\d{6}', text)
print(numbers)                       # ['0123-456789', '0987-654321']

# ═══════════════════════════════════════════════════════════════
# RE.FINDITER - Iterator over match objects
# ═══════════════════════════════════════════════════════════════
for match in re.finditer(r'\d{4}-\d{6}', text):
    print(f"{match.group()} at {match.span()}")

# ═══════════════════════════════════════════════════════════════
# RE.SUB - Search and replace
# ═══════════════════════════════════════════════════════════════
result = re.sub(r'\d', 'X', 'Tel: 123-456')
print(result)                        # 'Tel: XXX-XXX'

# With count (max replacements)
result = re.sub(r'\d', 'X', '123456', count=3)
print(result)                        # 'XXX456'

# ═══════════════════════════════════════════════════════════════
# RE.SPLIT - Split by pattern
# ═══════════════════════════════════════════════════════════════
parts = re.split(r'[,;]\s*', 'a, b; c,d')
print(parts)                         # ['a', 'b', 'c', 'd']
```

---

## 🔤 Metacharacters Reference

```
┌─────────────────────────────────────────────────────────────────┐
│                    METACHARACTERS OVERVIEW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CHARACTER CLASSES                                              │
│  ─────────────────────────────────────────────────────────────  │
│  .        Any character (except \n)                             │
│  \d       Digit [0-9]                                           │
│  \D       Non-digit [^0-9]                                      │
│  \w       Word character [a-zA-Z0-9_]                           │
│  \W       Non-word character                                    │
│  \s       Whitespace [ \t\n\r\f\v]                              │
│  \S       Non-whitespace                                        │
│  [abc]    a, b, or c                                            │
│  [^abc]   Not a, b, or c                                        │
│  [a-z]    Lowercase a-z                                         │
│  [0-9]    Digit 0-9                                             │
│                                                                  │
│  QUANTIFIERS                                                    │
│  ─────────────────────────────────────────────────────────────  │
│  *        0 or more (greedy)                                    │
│  +        1 or more (greedy)                                    │
│  ?        0 or 1                                                │
│  {n}      Exactly n times                                       │
│  {n,}     n or more times                                       │
│  {n,m}    n to m times                                          │
│  *?       0+ (non-greedy/lazy)                                  │
│  +?       1+ (non-greedy/lazy)                                  │
│                                                                  │
│  ANCHORS                                                        │
│  ─────────────────────────────────────────────────────────────  │
│  ^        Start of line                                         │
│  $        End of line                                           │
│  \b       Word boundary                                         │
│  \B       Non-word boundary                                     │
│                                                                  │
│  GROUPS & ALTERNATIVES                                         │
│  ─────────────────────────────────────────────────────────────  │
│  (...)    Group (capturing)                                     │
│  (?:...)  Group (non-capturing)                                 │
│  (?P<n>.) Named group                                           │
│  |        Or (alternative)                                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📝 Practical Examples

### Character Classes

```python
import re

text = "Email: test@example.com, Tel: 0123-456789"

# \d - Digits
print(re.findall(r'\d+', text))      # ['0123', '456789']

# \w - Word characters
print(re.findall(r'\w+', text))      # ['Email', 'test', 'example', 'com', ...]

# \s - Whitespace
print(re.split(r'\s+', 'a   b  c'))  # ['a', 'b', 'c']

# [abc] - Character set
print(re.findall(r'[aeiou]', 'hello')) # ['e', 'o']

# [^abc] - Negated set
print(re.findall(r'[^aeiou]', 'hello')) # ['h', 'l', 'l']

# [a-z] - Range
print(re.findall(r'[A-Za-z]+', 'Hello123World')) # ['Hello', 'World']
```

### Quantifiers

```python
import re

# * (0 or more)
print(re.findall(r'ab*c', 'ac abc abbc'))     # ['ac', 'abc', 'abbc']

# + (1 or more)
print(re.findall(r'ab+c', 'ac abc abbc'))     # ['abc', 'abbc']

# ? (0 or 1)
print(re.findall(r'colou?r', 'color colour')) # ['color', 'colour']

# {n} (exactly n)
print(re.findall(r'\d{4}', '123 1234 12345')) # ['1234', '1234']

# {n,m} (n to m)
print(re.findall(r'\d{2,4}', '1 12 123 1234 12345'))
# ['12', '123', '1234', '1234']
```

### Greedy vs Non-Greedy

```python
import re

html = '<div>Content</div><span>More</span>'

# Greedy (default) - match as much as possible
print(re.findall(r'<.*>', html))
# ['<div>Content</div><span>More</span>']  ← One match!

# Non-greedy (*?) - match as little as possible
print(re.findall(r'<.*?>', html))
# ['<div>', '</div>', '<span>', '</span>']  ← Four matches!
```

### Anchors

```python
import re

lines = ['hello world', 'world hello', 'hello']

# ^ - Start of line
for line in lines:
    if re.search(r'^hello', line):
        print(f"Starts with hello: {line}")

# $ - End of line
for line in lines:
    if re.search(r'hello$', line):
        print(f"Ends with hello: {line}")

# \b - Word boundary
text = "cat category caterpillar"
print(re.findall(r'\bcat\b', text))      # ['cat'] (only whole word)
print(re.findall(r'\bcat', text))        # ['cat', 'cat', 'cat'] (word start)
```

---

## 👥 Groups

### Capturing Groups

```python
import re

# Simple groups
pattern = r'(\d{3})-(\d{4})'
match = re.search(pattern, 'Tel: 123-4567')

print(match.group())                 # '123-4567' (entire match)
print(match.group(0))                # '123-4567' (same as above)
print(match.group(1))                # '123' (first group)
print(match.group(2))                # '4567' (second group)
print(match.groups())                # ('123', '4567') (all groups)

# findall with groups
pattern = r'(\w+)@(\w+)\.(\w+)'
emails = 'alice@mail.com and bob@web.de'
print(re.findall(pattern, emails))
# [('alice', 'mail', 'com'), ('bob', 'web', 'de')]
```

### Named Groups

```python
import re

pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, 'Date: 2024-03-15')

print(match.group('year'))           # '2024'
print(match.group('month'))          # '03'
print(match.group('day'))            # '15'
print(match.groupdict())             # {'year': '2024', 'month': '03', 'day': '15'}
```

### Non-Capturing Groups

```python
import re

# (?:...) - Groups, but doesn't capture
pattern = r'(?:https?://)?www\.(\w+)\.com'
urls = ['www.google.com', 'https://www.facebook.com']

for url in urls:
    match = re.search(pattern, url)
    if match:
        print(match.group(1))        # 'google', 'facebook' (domain only)
```

### Backreferences

```python
import re

# \1 refers to first group
pattern = r'(\w+) \1'                # Repeated words
text = 'the the quick brown fox fox'
print(re.findall(pattern, text))     # ['the', 'fox']

# In replacements
text = 'Hello World'
result = re.sub(r'(\w+) (\w+)', r'\2 \1', text)
print(result)                        # 'World Hello'
```

---

## 🚩 Flags

```python
import re

# ═══════════════════════════════════════════════════════════════
# RE.IGNORECASE / RE.I - Case insensitive
# ═══════════════════════════════════════════════════════════════
print(re.findall(r'hello', 'Hello HELLO', re.I))
# ['Hello', 'HELLO']

# ═══════════════════════════════════════════════════════════════
# RE.MULTILINE / RE.M - ^ and $ for each line
# ═══════════════════════════════════════════════════════════════
text = """line1
line2
line3"""

print(re.findall(r'^line\d', text, re.M))
# ['line1', 'line2', 'line3']

# ═══════════════════════════════════════════════════════════════
# RE.DOTALL / RE.S - . also matches \n
# ═══════════════════════════════════════════════════════════════
text = "<div>\nContent\n</div>"
print(re.findall(r'<div>.*</div>', text))         # [] (. doesn't match \n)
print(re.findall(r'<div>.*</div>', text, re.S))   # ['<div>\nContent\n</div>']

# ═══════════════════════════════════════════════════════════════
# RE.VERBOSE / RE.X - Readable regex with comments
# ═══════════════════════════════════════════════════════════════
email_pattern = re.compile(r'''
    ^                   # Start
    [\w.+-]+            # Username (letters, dots, plus, dash)
    @                   # @ symbol
    [\w-]+              # Domain name
    \.                  # Dot
    [\w.-]+             # TLD (can have multiple dots)
    $                   # End
''', re.VERBOSE)

# ═══════════════════════════════════════════════════════════════
# COMBINE FLAGS
# ═══════════════════════════════════════════════════════════════
pattern = re.compile(r'hello', re.I | re.M)
```

---

## ⚡ Compiled Patterns

Compile patterns for frequent use:

```python
import re

# Compile for better performance
email_pattern = re.compile(r'^[\w.+-]+@[\w-]+\.[\w.-]+$')

# Use like functions after
emails = ['valid@email.com', 'invalid', 'also@valid.de']

for email in emails:
    if email_pattern.match(email):
        print(f"✅ {email}")
    else:
        print(f"❌ {email}")

# All methods available
email_pattern.search(text)
email_pattern.findall(text)
email_pattern.sub(replacement, text)
```

---

## 📧 Common Patterns

```python
import re

# ═══════════════════════════════════════════════════════════════
# EMAIL (simplified)
# ═══════════════════════════════════════════════════════════════
email_pattern = r'^[\w.+-]+@[\w-]+\.[\w.-]+$'

# ═══════════════════════════════════════════════════════════════
# URL
# ═══════════════════════════════════════════════════════════════
url_pattern = r'https?://[\w.-]+(?:/[\w./-]*)?'

# ═══════════════════════════════════════════════════════════════
# POSTAL CODE (Germany)
# ═══════════════════════════════════════════════════════════════
plz_pattern = r'\b\d{5}\b'

# ═══════════════════════════════════════════════════════════════
# PHONE NUMBER (various formats)
# ═══════════════════════════════════════════════════════════════
phone_pattern = r'\+?[\d\s-]{10,}'

# ═══════════════════════════════════════════════════════════════
# DATE (YYYY-MM-DD)
# ═══════════════════════════════════════════════════════════════
date_pattern = r'\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])'

# ═══════════════════════════════════════════════════════════════
# IPv4 ADDRESS
# ═══════════════════════════════════════════════════════════════
ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

# ═══════════════════════════════════════════════════════════════
# HTML TAG
# ═══════════════════════════════════════════════════════════════
tag_pattern = r'<(\w+)[^>]*>.*?</\1>'
```

---

## ⚠️ Common Pitfalls

```python
import re

# ❌ WRONG: No raw string
pattern = '\d+'          # \d is interpreted as escape!
pattern = r'\d+'         # ✅ Raw string

# ❌ WRONG: Greedy when lazy needed
html = '<b>text</b><b>more</b>'
re.findall(r'<b>.*</b>', html)    # One match for everything!
re.findall(r'<b>.*?</b>', html)   # ✅ Two separate matches

# ❌ WRONG: findall with groups
# findall returns only groups when groups present!
pattern = r'(\d+)-(\d+)'
re.findall(pattern, '12-34 56-78')   # [('12', '34'), ('56', '78')]
# If you want the entire match:
re.findall(r'\d+-\d+', '12-34 56-78')  # ['12-34', '56-78']

# ❌ WRONG: Confusing match vs search
re.match(r'\d+', 'abc123')    # None (match only checks start!)
re.search(r'\d+', 'abc123')   # Match! '123'

# ❌ WRONG: Regex for simple tasks
# When str methods are sufficient:
text.startswith('Hello')      # ✅ Instead of: re.match(r'^Hello', text)
text.endswith('.txt')         # ✅ Instead of: re.search(r'\.txt$', text)
text.replace('old', 'new')    # ✅ Instead of: re.sub(r'old', 'new', text)
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Use `r''` raw strings | Escape backslashes |
| Compile patterns for reuse | Recompile every time |
| `re.VERBOSE` for complex patterns | Unreadable one-liners |
| Specific patterns (`\d{4}`) | Too general (`.*`) |
| Use str methods when sufficient | Regex for everything |
| Non-greedy (`*?`) for HTML/tags | Greedy for bracketed structures |
| Test patterns (regex101.com) | Blind in production |

---

## 🎯 Exam Checklist

- [ ] `re.search()` vs `re.match()` vs `re.fullmatch()`
- [ ] `re.findall()` and `re.finditer()`
- [ ] `re.sub()` for replacements
- [ ] Metacharacters: `\d`, `\w`, `\s`, `.`, `^`, `$`, `\b`
- [ ] Quantifiers: `*`, `+`, `?`, `{n,m}`
- [ ] Greedy vs non-greedy (`*` vs `*?`)
- [ ] Capturing groups and `match.group(n)`
- [ ] Named groups `(?P<name>...)` and `groupdict()`
- [ ] Flags: `re.I`, `re.M`, `re.S`, `re.VERBOSE`
- [ ] Use raw strings `r''`

---

[[24_Standard_Library|← Standard Library]] | [[00_Index|Index]] | [[26_Working_with_Dates|Working with Dates →]]
