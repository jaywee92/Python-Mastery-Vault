---
title: Hash Tables (Beginner)
tags: [dsa, hash-table, dictionary]
created: 2026-02-04
difficulty: beginner
---

# Hash Tables (Beginner)

[[00_Index|← Back to Index]] | [[02_Hash_Sets|Hash Sets →]]

## What it is
A hash table stores **key → value** pairs so you can find values quickly.
In Python, a **dict** is a hash table.

## Why it is useful
- Fast lookups by key
- Easy to store and update data

## Simple Example
```python
# A dictionary is a hash table in Python
prices = {
    "apple": 1.20,
    "banana": 0.80,
}

# Look up a value by key
print(prices["apple"])  # 1.20

# Add a new key/value
prices["orange"] = 1.50

# Update a value
prices["banana"] = 0.90

# Check if a key exists
if "apple" in prices:
    print("Apple is in the table")
```

## Key Points
- Keys are **unique**
- Values can be any type
- Use `in` to check if a key exists
