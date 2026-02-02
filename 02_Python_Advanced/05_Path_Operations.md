---
title: Path Operations
tags: [python, pathlib, filesystem, paths, practical, exam-essential]
created: 2026-01-26
exam_weight: medium
difficulty: beginner-intermediate
---

# 📁 Path Operations with pathlib

[[00_Index|← Back to Index]] | [[15_File_IO|← File IO]] | [[16_Working_with_JSON|← JSON]]

> **Modern path operations with the pathlib module**

---

## 🎯 Why pathlib?

`pathlib` is the **modern standard** for path operations in Python (since 3.4).

```python
# ❌ OLD: os.path (cumbersome)
import os
path = os.path.join('data', 'subdir', 'file.txt')
name = os.path.basename(path)
exists = os.path.exists(path)

# ✅ NEW: pathlib (elegant)
from pathlib import Path
path = Path('data') / 'subdir' / 'file.txt'
name = path.name
exists = path.exists()
```

**Advantages of pathlib:**
- ✅ Object-oriented and intuitive
- ✅ `/` operator for path concatenation
- ✅ Platform-independent
- ✅ Methods directly on path object
- ✅ Better readability

---

## 📦 Create Path Objects

```python
from pathlib import Path

# From string
path = Path('data/file.txt')
path = Path('/home/user/documents')

# Current directory
cwd = Path.cwd()
print(cwd)  # /home/user/project

# Home directory
home = Path.home()
print(home)  # /home/user (Linux) or C:\Users\Username (Windows)

# Concatenate paths with /
base = Path('data')
full = base / 'subdir' / 'file.txt'
print(full)  # data/subdir/file.txt

# From multiple parts
path = Path('data', 'subdir', 'file.txt')
print(path)  # data/subdir/file.txt
```

---

## 🔍 Path Components

```python
from pathlib import Path

path = Path('/home/user/documents/report.pdf')

# Individual parts
print(path.name)      # report.pdf (filename with extension)
print(path.stem)      # report (filename without extension)
print(path.suffix)    # .pdf (extension)
print(path.suffixes)  # ['.pdf'] (all extensions, e.g., ['.tar', '.gz'])
print(path.parent)    # /home/user/documents (parent directory)
print(path.anchor)    # / (root on Unix, C:\ on Windows)

# All parent directories
print(path.parents[0])  # /home/user/documents
print(path.parents[1])  # /home/user
print(path.parents[2])  # /home

# Parts as tuple
print(path.parts)  # ('/', 'home', 'user', 'documents', 'report.pdf')

# Is absolute or relative?
print(path.is_absolute())  # True
print(Path('data/file.txt').is_absolute())  # False
```

### Path Components Visualized

```
          Path: /home/user/docs/report.final.pdf
                ↓
┌───────────────┴───────────────────────────────┐
│ anchor    │ parent           │ name           │
│ /         │ /home/user/docs  │ report.final.pdf│
│           │                  │ ↓              │
│           │                  │ stem   suffix  │
│           │                  │ report .final  │
│           │                  │        .pdf    │
│           │                  │ (suffixes)     │
└───────────┴──────────────────┴────────────────┘
```

---

## ✅ Check Existence and Type

```python
from pathlib import Path

path = Path('data/file.txt')

# Does it exist?
path.exists()      # True/False

# What is it?
path.is_file()     # Is it a file?
path.is_dir()      # Is it a directory?
path.is_symlink()  # Is it a symbolic link?
path.is_mount()    # Is it a mount point?

# Practical pattern
if path.exists() and path.is_file():
    content = path.read_text()
```

---

## 📝 Read and Write Files

`pathlib` provides built-in methods for reading/writing:

```python
from pathlib import Path

path = Path('example.txt')

# === WRITE ===

# Write text (overwrites!)
path.write_text('Hello, World!')

# With encoding
path.write_text('Hallo, Welt!', encoding='utf-8')

# Write bytes
path.write_bytes(b'\x00\x01\x02\x03')


# === READ ===

# Read text
content = path.read_text()
content = path.read_text(encoding='utf-8')

# Read bytes
data = path.read_bytes()


# === PRACTICAL EXAMPLE ===

# Read JSON file
import json
data = json.loads(Path('config.json').read_text())

# Write JSON file
Path('output.json').write_text(
    json.dumps(data, indent=2),
    encoding='utf-8'
)
```

**Note:** For more complex operations (appending, reading line by line), continue using `open()` with `with`.

---

## 📂 Directories

### Create Directory

```python
from pathlib import Path

# Create simple directory
Path('new_dir').mkdir()

# With exist_ok (no error if exists)
Path('new_dir').mkdir(exist_ok=True)

# Create nested directories
Path('a/b/c/d').mkdir(parents=True, exist_ok=True)
```

### List Directory Contents

```python
from pathlib import Path

dir_path = Path('.')

# All entries (files and directories)
for item in dir_path.iterdir():
    print(item)

# Files only
for item in dir_path.iterdir():
    if item.is_file():
        print(item.name)

# Directories only
for item in dir_path.iterdir():
    if item.is_dir():
        print(item.name)

# As list
all_items = list(dir_path.iterdir())
files = [f for f in dir_path.iterdir() if f.is_file()]
dirs = [d for d in dir_path.iterdir() if d.is_dir()]
```

---

## 🔎 Glob - Pattern Search

```python
from pathlib import Path

dir_path = Path('.')

# All .txt files in current directory
for txt_file in dir_path.glob('*.txt'):
    print(txt_file)

# All .py files (including subdirectories)
for py_file in dir_path.glob('**/*.py'):  # ** = recursive
    print(py_file)

# rglob = recursive glob (shorthand)
for py_file in dir_path.rglob('*.py'):
    print(py_file)

# More complex patterns
dir_path.glob('data_*.csv')       # data_001.csv, data_test.csv
dir_path.glob('**/test_*.py')     # test_*.py in all subdirectories
dir_path.glob('[0-9]*.txt')       # Starts with digit

# As list
all_python_files = list(dir_path.rglob('*.py'))
```

### Glob Patterns

| Pattern | Meaning | Example |
|---------|---------|----------|
| `*` | Any characters (except /) | `*.txt` → all .txt |
| `**` | All directories (recursive) | `**/*.py` → all .py everywhere |
| `?` | Any single character | `file?.txt` → file1.txt, fileA.txt |
| `[abc]` | Any character in set | `[0-9]*` → starts with digit |
| `[!abc]` | Any character not in set | `[!.]* ` → non-hidden files |

---

## 🔧 Modify Path

```python
from pathlib import Path

path = Path('data/old_name.txt')

# Change extension
new_path = path.with_suffix('.md')
print(new_path)  # data/old_name.md

# Change filename (with extension)
new_path = path.with_name('new_name.txt')
print(new_path)  # data/new_name.txt

# Change stem only
new_path = path.with_stem('renamed')
print(new_path)  # data/renamed.txt

# Convert relative path to absolute
abs_path = path.resolve()
print(abs_path)  # /home/user/project/data/old_name.txt

# Convert absolute to relative path
rel_path = abs_path.relative_to(Path.cwd())
print(rel_path)  # data/old_name.txt

# Normalize path (resolve . and ..)
messy = Path('data/../data/./file.txt')
clean = messy.resolve()
print(clean)  # /home/user/project/data/file.txt
```

---

## 🗑️ Delete Files and Directories

```python
from pathlib import Path

# Delete file
Path('file.txt').unlink()

# Delete file (no error if doesn't exist)
Path('maybe_file.txt').unlink(missing_ok=True)

# Delete empty directory
Path('empty_dir').rmdir()

# Delete directory with content (requires shutil)
import shutil
shutil.rmtree('dir_with_content')
```

---

## 📋 Copy and Move Files

`pathlib` has no built-in methods for this - use `shutil`:

```python
from pathlib import Path
import shutil

src = Path('source.txt')
dst = Path('destination.txt')

# Copy
shutil.copy(src, dst)           # File only
shutil.copy2(src, dst)          # With metadata (time, etc.)
shutil.copytree(src_dir, dst_dir)  # Entire directory

# Move/Rename
src.rename(dst)                 # pathlib method
shutil.move(src, dst)           # shutil alternative

# Example: Copy all .txt to backup/
backup = Path('backup')
backup.mkdir(exist_ok=True)

for txt_file in Path('.').glob('*.txt'):
    shutil.copy2(txt_file, backup / txt_file.name)
```

---

## 📊 File Information

```python
from pathlib import Path
from datetime import datetime

path = Path('file.txt')

# Statistics
stat = path.stat()
print(stat.st_size)    # Size in bytes
print(stat.st_mtime)   # Last modification (timestamp)
print(stat.st_ctime)   # Creation time (timestamp)

# Human-readable
size_kb = stat.st_size / 1024
modified = datetime.fromtimestamp(stat.st_mtime)
print(f"Size: {size_kb:.2f} KB")
print(f"Modified: {modified}")

# Owner (Unix)
print(path.owner())    # Owner name
print(path.group())    # Group name
```

---

## 🔄 Practical Examples

### Organize Files by Extension

```python
from pathlib import Path
import shutil

def organize_by_extension(source_dir):
    """Sort files into subfolders by extension"""
    source = Path(source_dir)

    for file in source.iterdir():
        if file.is_file():
            ext = file.suffix.lower() or 'no_extension'
            target_dir = source / ext[1:]  # Without dot
            target_dir.mkdir(exist_ok=True)
            shutil.move(file, target_dir / file.name)

organize_by_extension('downloads')
# Creates: downloads/pdf/, downloads/jpg/, etc.
```

### Find All Empty Directories

```python
from pathlib import Path

def find_empty_dirs(root):
    """Find all empty directories"""
    root = Path(root)
    empty = []

    for path in root.rglob('*'):
        if path.is_dir() and not any(path.iterdir()):
            empty.append(path)

    return empty

empty_dirs = find_empty_dirs('project')
for d in empty_dirs:
    print(f"Empty: {d}")
```

### Calculate File Size

```python
from pathlib import Path

def get_dir_size(path):
    """Calculate total size of directory"""
    total = 0
    for file in Path(path).rglob('*'):
        if file.is_file():
            total += file.stat().st_size
    return total

def format_size(bytes):
    """Format bytes human-readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024

size = get_dir_size('project')
print(f"Project size: {format_size(size)}")
```

### Create Backup with Timestamp

```python
from pathlib import Path
from datetime import datetime
import shutil

def backup_file(filepath):
    """Create backup with timestamp"""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist")

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"{path.stem}_{timestamp}{path.suffix}"
    backup_path = path.parent / 'backups' / backup_name

    backup_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, backup_path)

    return backup_path

backup = backup_file('config.json')
print(f"Backup created: {backup}")
```

---

## ⚠️ Common Pitfalls

### 1. String Instead of Path

```python
from pathlib import Path

# ❌ WRONG
path = 'data' + '/' + 'file.txt'

# ✅ CORRECT
path = Path('data') / 'file.txt'
```

### 2. Use Path with open()

```python
from pathlib import Path

path = Path('file.txt')

# ✅ Both work
with open(path, 'r') as f:    # Path works with open()
    content = f.read()

content = path.read_text()     # Or directly
```

### 3. Comparing Paths

```python
from pathlib import Path

# ✅ Path objects compare correctly
Path('data/../data/file.txt').resolve() == Path('data/file.txt').resolve()
# True (after normalization)

# ⚠️ But without resolve():
Path('data/../data/file.txt') == Path('data/file.txt')
# False (different strings!)
```

### 4. Platform Independence

```python
from pathlib import Path

# ✅ Automatically platform-independent
path = Path('data') / 'subdir' / 'file.txt'
# Windows: data\subdir\file.txt
# Unix: data/subdir/file.txt

# ❌ Hardcoded separator
path = 'data\\subdir\\file.txt'  # Windows only!
```

---

## 📋 pathlib vs os.path Reference

| Operation | os.path | pathlib |
|-----------|---------|---------|
| Join paths | `os.path.join(a, b)` | `Path(a) / b` |
| Exists? | `os.path.exists(p)` | `Path(p).exists()` |
| Is file? | `os.path.isfile(p)` | `Path(p).is_file()` |
| Is directory? | `os.path.isdir(p)` | `Path(p).is_dir()` |
| Filename | `os.path.basename(p)` | `Path(p).name` |
| Directory | `os.path.dirname(p)` | `Path(p).parent` |
| Extension | `os.path.splitext(p)[1]` | `Path(p).suffix` |
| Absolute path | `os.path.abspath(p)` | `Path(p).resolve()` |
| Home directory | `os.path.expanduser('~')` | `Path.home()` |
| List directory | `os.listdir(p)` | `Path(p).iterdir()` |
| Glob | `glob.glob('*.py')` | `Path('.').glob('*.py')` |

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| `pathlib` for all path operations | `os.path` for new projects |
| `/` operator for concatenation | String concatenation with `/` or `\\` |
| `exist_ok=True` with `mkdir()` | Manual check before `mkdir()` |
| `resolve()` for comparisons | Compare paths as strings |
| `rglob()` for recursive search | Manual recursive traversal |
| `with_suffix()` to change extension | String manipulation |

---

## 🎯 Exam Checklist

- [ ] Create `Path()` objects
- [ ] `/` operator for path concatenation
- [ ] `name`, `stem`, `suffix`, `parent`
- [ ] `exists()`, `is_file()`, `is_dir()`
- [ ] `mkdir(parents=True, exist_ok=True)`
- [ ] `glob()` and `rglob()` patterns
- [ ] `read_text()`, `write_text()`
- [ ] `resolve()` for absolute paths

---

[[16_Working_with_JSON|← JSON]] | [[00_Index|Index]] | [[18_Exceptions|Exceptions →]]
