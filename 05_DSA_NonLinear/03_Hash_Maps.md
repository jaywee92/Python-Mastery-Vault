---
title: Hash Maps (Beginner)
tags: [dsa, hash-map, dictionary]
created: 2026-02-04
difficulty: beginner
---

# Hash Maps (Beginner)

[[00_Index|← Back to Index]] | [[02_Hash_Sets|← Hash Sets]] | [[04_Trees|Trees →]]

## What it is
A hash map is another name for a **dictionary** (key → value pairs).

## Simple Example
```python
# Store scores by name
scores = {
    "Ana": 10,
    "Ben": 7,
}

# Read
print(scores["Ana"])  # 10

# Update
scores["Ben"] = 8

# Add
scores["Cara"] = 9

# Safe get with default
print(scores.get("Dan", 0))  # 0
```

## Key Points
- Great for lookups and counting
- Use `.get(key, default)` to avoid errors
