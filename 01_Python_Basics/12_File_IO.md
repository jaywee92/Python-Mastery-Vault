---
title: File IO
tags: [python, files, io, with-statement, csv, practical, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: beginner-intermediate
---

# 📂 File IO (Reading & Writing Files)

[[00_Index|← Back to Index]] | [[16_Working_with_JSON|JSON →]] | [[17_Path_Operations|Paths →]]

> **Read and write files safely with Python**

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║       📂 FILE IO - READING/WRITING FILES                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║   Correct method: WITH statement (Recommended)                ║
║   ┌──────────────────────────────────────────┐               ║
║   │ with open('file.txt', 'r') as f:         │               ║
║   │     content = f.read()                   │               ║
║   │ # File automatically closed!             │               ║
║   └──────────────────────────────────────────┘               ║
║                                                               ║
║   Modes: 'r' (Read) | 'w' (Write) | 'a' (Append)            ║
║                                                               ║
║   File access visualization:                                  ║
║                                                               ║
║   FILE ─────────┐                                             ║
║   "text.txt"    │  open()                                     ║
║                 └──→ [File object] ←─ Python                 ║
║                      ↓                                        ║
║                   read()   write()   append()                 ║
║                      ↓         ↓         ↓                    ║
║                   Content  Modify    Add                     ║
║                                                               ║
║   close() OR with automatic ← SAFETY!                        ║
║                                                               ║
║   File modes in detail:                                       ║
║   'r'  ← Read only (Error if not exists)                     ║
║   'w'  ← Write (DELETES ALL!)                                ║
║   'a'  ← Append (add at end)                                 ║
║   'x'  ← Create only (if not exists)                         ║
║                                                               ║
║   💡 Always use with! Safer & automatic close               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 🎯 Most Important: The `with` Statement

**Always** use `with`! It guarantees that files are closed properly.

```python
# ✅ CORRECT: with statement (Context Manager)
with open('file.txt', 'r') as f:
    content = f.read()
# File is automatically closed, even on Exceptions!

# ❌ AVOID: Manual open/close
f = open('file.txt', 'r')
content = f.read()
f.close()  # Won't be called on Exception!
```

---

## 📖 File Modes

| Mode | Description | Creates File? | Overwrites? |
|------|-------------|---------------|------------|
| `'r'` | **Read** - Reading (Default) | ❌ Error if not exists | - |
| `'w'` | **Write** - Writing | ✅ Yes | ✅ Yes (deletes all!) |
| `'a'` | **Append** - Appending | ✅ Yes | ❌ Adds at end |
| `'x'` | **Exclusive** - Create | ✅ Only if not exists | - |
| `'r+'` | Read + Write | ❌ Must exist | Depends on position |
| `'w+'` | Write + Read | ✅ Yes | ✅ Yes |
| `'a+'` | Append + Read | ✅ Yes | ❌ No |

**Binary Mode** (for images, PDFs, etc.):
- `'rb'` - Read binary
- `'wb'` - Write binary
- `'ab'` - Append binary

```python
# Text vs Binary
with open('text.txt', 'r') as f:     # Text mode
    text = f.read()  # str

with open('image.png', 'rb') as f:   # Binary mode
    data = f.read()  # bytes
```

---

## 📖 Reading Files

### Read Entire Content

```python
# All at once (for small files)
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

# Specify encoding (important for special characters!)
with open('german.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### Read Line by Line

```python
# Method 1: readlines() - List of all lines
with open('file.txt', 'r') as f:
    lines = f.readlines()  # ['Line 1\n', 'Line 2\n', ...]

# Method 2: Iteration (memory efficient for large files)
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # strip() removes \n

# Method 3: readline() - One line
with open('file.txt', 'r') as f:
    first_line = f.readline()
    second_line = f.readline()
```

### Read Specific Number of Characters

```python
with open('file.txt', 'r') as f:
    chunk = f.read(100)  # First 100 characters
    next_chunk = f.read(100)  # Next 100 characters
```

### Read Large Files in Chunks

```python
def read_in_chunks(file_path, chunk_size=1024):
    """Reads large files in chunks"""
    with open(file_path, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Usage
for chunk in read_in_chunks('large_file.txt'):
    process(chunk)
```

---

## ✍️ Writing Files

### Write New Content (overwrites!)

```python
# Single string
with open('output.txt', 'w') as f:
    f.write('Hello, World!\n')
    f.write('Second line\n')

# List of lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('output.txt', 'w') as f:
    f.writelines(lines)  # Does NOT add newlines!

# Write using print() to file
with open('output.txt', 'w') as f:
    print('Hello', 'World', sep=', ', file=f)
    print('Second line', file=f)
```

### Append to Existing File

```python
from datetime import datetime

# Append mode
with open('log.txt', 'a') as f:
    f.write('New entry\n')
    f.write(f'Timestamp: {datetime.now()}\n')
```

### Write Multiple Lines Elegantly

```python
data = ['Alice', 'Bob', 'Charlie']

# Mit join und newline
with open('names.txt', 'w') as f:
    f.write('\n'.join(data))

# Mit print und Schleife
with open('names.txt', 'w') as f:
    for name in data:
        print(name, file=f)
```

---

## 🔍 File Positions

```python
with open('file.txt', 'r') as f:
    # Get position
    print(f.tell())  # 0 (at beginning)

    content = f.read(10)
    print(f.tell())  # 10 (after 10 characters)

    # Set position
    f.seek(0)  # Back to beginning
    f.seek(5)  # Position 5

    # seek with whence parameter
    f.seek(0, 0)  # 0 = from beginning
    f.seek(0, 1)  # 1 = from current position
    f.seek(0, 2)  # 2 = from end (binary mode only)
```

---

## 📊 CSV Files

### Read CSV

```python
import csv

# As list of lists
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ['col1', 'col2', 'col3']

# As dictionary (with header)
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['age'])

# With different delimiter
with open('data.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)
```

### Write CSV

```python
import csv

# As list of lists
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'Berlin'],
    ['Bob', '25', 'Munich']
]

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)  # All at once

# As dictionaries
data = [
    {'name': 'Alice', 'age': 30, 'city': 'Berlin'},
    {'name': 'Bob', 'age': 25, 'city': 'Munich'}
]

with open('output.csv', 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # Writes header
    writer.writerows(data)
```

**Important:** `newline=''` prevents double blank lines on Windows!

---

## 🔤 Encoding

```python
# UTF-8 (recommended for international text)
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Latin-1 (for older European text)
with open('old_file.txt', 'r', encoding='latin-1') as f:
    content = f.read()

# Error handling
with open('file.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()  # Ignores invalid characters

with open('file.txt', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()  # Replaces invalid characters with ?
```

---

## 📁 Multiple Files at Once

```python
# Open two files at the same time
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        outfile.write(line.upper())

# Or with line break
with open('input.txt', 'r') as infile, \
     open('output.txt', 'w') as outfile:
    for line in infile:
        outfile.write(line.upper())
```

---

## 🛡️ Error Handling

```python
from pathlib import Path

# Check if file exists
if Path('file.txt').exists():
    with open('file.txt', 'r') as f:
        content = f.read()
else:
    print("File does not exist!")

# With try/except
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("No permission!")
except IOError as e:
    print(f"IO Error: {e}")

# Create file safely (only if not exists)
try:
    with open('new_file.txt', 'x') as f:
        f.write('New content')
except FileExistsError:
    print("File already exists!")
```

---

## 🔄 Practical Examples

### Write Log File

```python
from datetime import datetime

def log(message, filename='app.log'):
    """Adds timestamped log entry"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filename, 'a') as f:
        f.write(f'[{timestamp}] {message}\n')

log('Application started')
log('User logged in')
log('Error occurred', 'error.log')
```

### Copy File

```python
def copy_file(source, destination):
    """Copy file (binary-safe)"""
    with open(source, 'rb') as src, open(destination, 'wb') as dst:
        dst.write(src.read())

# For large files (chunked)
def copy_large_file(source, destination, chunk_size=1024*1024):
    """Copy large file in 1MB chunks"""
    with open(source, 'rb') as src, open(destination, 'wb') as dst:
        while chunk := src.read(chunk_size):
            dst.write(chunk)
```

### Read Configuration File

```python
def read_config(filename):
    """Reads key=value configuration file"""
    config = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
    return config

# config.ini:
# # This is a comment
# host = localhost
# port = 8080
# debug = true

config = read_config('config.ini')
print(config['host'])  # localhost
```

### Count Words

```python
from collections import Counter

def count_words(filename):
    """Counts words in file"""
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        words = text.split()
    return Counter(words)

counts = count_words('document.txt')
print(counts.most_common(10))
```

---

## ⚠️ Common Pitfalls

### 1. Not Closing File

```python
# ❌ WRONG
f = open('file.txt')
content = f.read()
# Forgot: f.close()

# ✅ CORRECT
with open('file.txt') as f:
    content = f.read()
```

### 2. Ignoring Encoding

```python
# ❌ WRONG - can crash with special characters
with open('german.txt') as f:
    content = f.read()

# ✅ CORRECT
with open('german.txt', encoding='utf-8') as f:
    content = f.read()
```

### 3. Binary vs Text Mode

```python
# ❌ WRONG - Text mode for images
with open('image.png', 'r') as f:
    data = f.read()  # UnicodeDecodeError!

# ✅ CORRECT
with open('image.png', 'rb') as f:
    data = f.read()
```

### 4. Forgetting newline in CSV

```python
import csv

# ❌ WRONG - double blank lines on Windows
with open('data.csv', 'w') as f:
    writer = csv.writer(f)

# ✅ CORRECT
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Always use `with` statement | Manual `open()` and `close()` |
| Explicitly specify encoding | Trust default encoding |
| Use `'rb'`/`'wb'` for binary files | Text mode for images/PDFs |
| Read large files in chunks | Load entire 10GB file in RAM |
| Error handling with try/except | Ignore exceptions |
| Use `pathlib` for paths | String manipulation for paths |

---

## 🎯 Exam Checklist

- [ ] `with open()` syntax
- [ ] File modes: r, w, a, x, rb, wb
- [ ] `read()`, `readline()`, `readlines()`
- [ ] `write()`, `writelines()`
- [ ] Reading and writing CSV
- [ ] Encoding parameter
- [ ] Error handling for file operations

---

[[14_Properties_and_Class_Methods|← Properties]] | [[00_Index|Index]] | [[16_Working_with_JSON|JSON →]]
