---
title: Working with JSON
tags: [python, json, serialization, api, data, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: beginner-intermediate
---

# 📋 Working with JSON

[[00_Index|← Back to Index]] | [[15_File_IO|← File IO]] | [[17_Path_Operations|Paths →]]

> **Serialize and deserialize data with JSON**

---

## 🎯 What is JSON?

**JSON** (JavaScript Object Notation) is a lightweight data format for data exchange.

```json
{
    "name": "Alice",
    "age": 30,
    "is_student": false,
    "courses": ["Python", "Math"],
    "address": {
        "city": "Berlin",
        "zip": "10115"
    }
}
```

**Why JSON?**
- ✅ Human-readable
- ✅ Language-independent (every language can read it)
- ✅ Standard for Web APIs
- ✅ Simple structure

---

## 🔄 Python ↔ JSON Type Mapping

| Python | JSON | Example |
|--------|------|----------|
| `dict` | object | `{"key": "value"}` |
| `list`, `tuple` | array | `[1, 2, 3]` |
| `str` | string | `"hello"` |
| `int`, `float` | number | `42`, `3.14` |
| `True` | true | `true` |
| `False` | false | `false` |
| `None` | null | `null` |

**Warning:** Tuple becomes an array and when reading back becomes a list!

```python
import json

# Python to JSON
data = {'tuple': (1, 2, 3)}
json_str = json.dumps(data)
print(json_str)  # {"tuple": [1, 2, 3]}

# JSON to Python
parsed = json.loads(json_str)
print(parsed['tuple'])  # [1, 2, 3] - Now a list!
```

---

## 📤 Python to JSON (Serialization)

### dumps() - Convert to String

```python
import json

data = {
    'name': 'Alice',
    'age': 30,
    'active': True,
    'scores': [95, 87, 92],
    'address': None
}

# Compact
json_str = json.dumps(data)
print(json_str)
# {"name": "Alice", "age": 30, "active": true, "scores": [95, 87, 92], "address": null}

# Pretty-print with indentation
json_pretty = json.dumps(data, indent=2)
print(json_pretty)
# {
#   "name": "Alice",
#   "age": 30,
#   "active": true,
#   "scores": [95, 87, 92],
#   "address": null
# }

# Sorted keys (for consistent output)
json_sorted = json.dumps(data, indent=2, sort_keys=True)
```

### dump() - Write Directly to File

```python
import json

data = {'name': 'Bob', 'age': 25}

# Write to file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

# With unicode characters
data_de = {'name': 'Müller', 'city': 'München'}

# ensure_ascii=False preserves Unicode characters
with open('german.json', 'w', encoding='utf-8') as f:
    json.dump(data_de, f, indent=2, ensure_ascii=False)
# File contains: {"name": "Müller", "city": "München"}

# With ensure_ascii=True (default)
with open('escaped.json', 'w') as f:
    json.dump(data_de, f, indent=2)
# File contains: {"name": "M\u00fcller", "city": "M\u00fcnchen"}
```

---

## 📥 JSON to Python (Deserialization)

### loads() - Read from String

```python
import json

json_str = '{"name": "Charlie", "age": 35, "active": true}'

data = json.loads(json_str)
print(data)           # {'name': 'Charlie', 'age': 35, 'active': True}
print(data['name'])   # Charlie
print(type(data))     # <class 'dict'>

# Access nested data
nested_json = '''
{
    "user": {
        "name": "Dana",
        "contacts": {
            "email": "dana@example.com",
            "phone": "+49123456789"
        }
    }
}
'''

data = json.loads(nested_json)
print(data['user']['contacts']['email'])  # dana@example.com
```

### load() - Read from File

```python
import json

# Read from file
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)

# Safe variant with error handling
try:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found!")
    data = {}
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
    data = {}
```

---

## 🔧 Advanced Options

### Compact Output

```python
import json

data = {'a': 1, 'b': 2, 'c': [1, 2, 3]}

# Standard
print(json.dumps(data))
# {"a": 1, "b": 2, "c": [1, 2, 3]}

# Without spaces (maximally compact)
print(json.dumps(data, separators=(',', ':')))
# {"a":1,"b":2,"c":[1,2,3]}
```

### Custom Encoders for Non-Serializable Types

```python
import json
from datetime import datetime, date
from decimal import Decimal

# ❌ PROBLEM: These types are not JSON serializable
data = {
    'timestamp': datetime.now(),
    'date': date.today(),
    'price': Decimal('19.99')
}

# json.dumps(data)  # TypeError!

# ✅ SOLUTION 1: Custom Encoder Class
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

json_str = json.dumps(data, cls=CustomEncoder, indent=2)
print(json_str)
# {
#   "timestamp": "2026-01-29T15:30:00.123456",
#   "date": "2026-01-29",
#   "price": 19.99
# }

# ✅ SOLUTION 2: default parameter as function
def json_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

json_str = json.dumps(data, default=json_serializer, indent=2)
```

### Custom Decoder

```python
import json
from datetime import datetime

json_str = '{"name": "Event", "date": "2026-01-29T15:30:00"}'

# Custom object_hook
def datetime_decoder(dct):
    for key, value in dct.items():
        if isinstance(value, str):
            try:
                dct[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return dct

data = json.loads(json_str, object_hook=datetime_decoder)
print(data['date'])  # 2026-01-29 15:30:00
print(type(data['date']))  # <class 'datetime.datetime'>
```

---

## 📊 Practical Examples

### Process API Response

```python
import json

# Typical API response
api_response = '''
{
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ],
        "total": 2
    }
}
'''

response = json.loads(api_response)

if response['status'] == 'success':
    for user in response['data']['users']:
        print(f"{user['name']}: {user['email']}")
```

### Configuration File

```python
import json
from pathlib import Path

class Config:
    DEFAULT = {
        'debug': False,
        'host': 'localhost',
        'port': 8080,
        'database': {
            'name': 'app_db',
            'user': 'admin'
        }
    }

    def __init__(self, filepath='config.json'):
        self.filepath = Path(filepath)
        self.data = self._load()

    def _load(self):
        if self.filepath.exists():
            with open(self.filepath, 'r') as f:
                return {**self.DEFAULT, **json.load(f)}
        return self.DEFAULT.copy()

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=2)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save()


# Usage
config = Config()
print(config.get('host'))  # localhost
config.set('debug', True)
```

### Cache Data

```python
import json
from pathlib import Path
from datetime import datetime, timedelta

class JSONCache:
    def __init__(self, filepath, ttl_seconds=3600):
        self.filepath = Path(filepath)
        self.ttl = ttl_seconds

    def get(self, key):
        if not self.filepath.exists():
            return None

        with open(self.filepath, 'r') as f:
            cache = json.load(f)

        if key not in cache:
            return None

        entry = cache[key]
        timestamp = datetime.fromisoformat(entry['timestamp'])

        if datetime.now() - timestamp > timedelta(seconds=self.ttl):
            return None  # Expired

        return entry['value']

    def set(self, key, value):
        cache = {}
        if self.filepath.exists():
            with open(self.filepath, 'r') as f:
                cache = json.load(f)

        cache[key] = {
            'value': value,
            'timestamp': datetime.now().isoformat()
        }

        with open(self.filepath, 'w') as f:
            json.dump(cache, f, indent=2)


# Usage
cache = JSONCache('cache.json', ttl_seconds=60)
cache.set('api_data', {'users': ['Alice', 'Bob']})
data = cache.get('api_data')
```

### JSON Lines (JSONL) Format

```python
import json

# JSONL: One JSON object per line
# Good for streaming and large datasets

# Write
records = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'}
]

with open('data.jsonl', 'w') as f:
    for record in records:
        f.write(json.dumps(record) + '\n')

# Read (memory-efficient)
with open('data.jsonl', 'r') as f:
    for line in f:
        record = json.loads(line)
        print(record['name'])
```

---

## 🔒 Security

### No Code Execution through JSON

```python
import json

# ✅ json.loads is SAFE (unlike eval)
malicious = '{"__class__": "os.system", "cmd": "rm -rf /"}'
data = json.loads(malicious)  # Simply parsed as dict
print(data)  # {'__class__': 'os.system', 'cmd': 'rm -rf /'}
# No execution!

# ❌ NEVER use eval for JSON!
# data = eval(json_string)  # DANGEROUS!
```

### Validate Input

```python
import json

def safe_parse(json_str, max_size=1024*1024):  # 1MB limit
    """Parse JSON with size restriction"""
    if len(json_str) > max_size:
        raise ValueError("JSON too large")
    return json.loads(json_str)

# Mit Schema-Validierung (externe Bibliothek)
# pip install jsonschema
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0}
    },
    "required": ["name"]
}

data = {"name": "Alice", "age": 30}
try:
    validate(instance=data, schema=schema)
    print("Valid!")
except ValidationError as e:
    print(f"Invalid: {e.message}")
```

---

## ⚠️ Common Pitfalls

### 1. Confusing dumps vs dump

```python
import json

data = {'key': 'value'}

# ❌ WRONG
with open('file.json', 'w') as f:
    f.write(json.dump(data, f))  # dump returns None!

# ✅ CORRECT
with open('file.json', 'w') as f:
    json.dump(data, f)  # Writes directly

# Or:
with open('file.json', 'w') as f:
    f.write(json.dumps(data))  # dumps returns string
```

### 2. Non-serializable Types

```python
import json
from datetime import datetime

# ❌ WRONG
data = {'time': datetime.now()}
# json.dumps(data)  # TypeError!

# ✅ CORRECT
data = {'time': datetime.now().isoformat()}
json.dumps(data)  # OK
```

### 3. Forgetting Encoding

```python
import json

# ❌ Unicode characters get escaped
json.dumps({'city': 'München'})
# '{"city": "M\\u00fcnchen"}'

# ✅ With ensure_ascii=False
json.dumps({'city': 'München'}, ensure_ascii=False)
# '{"city": "München"}'
```

### 4. No Comments in JSON

```python
# ❌ JSON does NOT support comments
invalid_json = '''
{
    "name": "Alice",  // This doesn't work!
    "age": 30
}
'''
# json.loads(invalid_json)  # JSONDecodeError!
```

---

## 📋 Memory Aid: dumps/loads vs dump/load

```
┌─────────────────────────────────────────────┐
│  String (s at end = String)                 │
│  ─────────────────────────────              │
│  json.dumps(data) → JSON String             │
│  json.loads(string) → Python Object         │
├─────────────────────────────────────────────┤
│  File (no s = directly in/out File)         │
│  ─────────────────────────────              │
│  json.dump(data, file)                      │
│  json.load(file) → Python Object            │
└─────────────────────────────────────────────┘
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| `indent=2` for readable output | Compact JSON for config files |
| `ensure_ascii=False` for Unicode | ASCII-escape for special characters |
| `encoding='utf-8'` when opening | Omit encoding |
| Custom encoder for complex types | Manual conversion everywhere |
| JSON Schema for validation | Blindly trust data |
| `json.loads()` for parsing | `eval()` for JSON |

---

## 🎯 Exam Checklist

- [ ] `json.dumps()` vs `json.dump()`
- [ ] `json.loads()` vs `json.load()`
- [ ] Python ↔ JSON type mapping
- [ ] `indent` parameter for pretty-print
- [ ] `ensure_ascii=False` for Unicode
- [ ] Error handling with `JSONDecodeError`
- [ ] Handle non-serializable types

---

[[15_File_IO|← File IO]] | [[00_Index|Index]] | [[17_Path_Operations|Paths →]]
