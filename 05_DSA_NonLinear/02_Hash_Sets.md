---
title: Hash Sets (Beginner)
tags: [dsa, set, hash]
created: 2026-02-04
difficulty: beginner
---

# Hash Sets (Beginner)

[[00_Index|← Back to Index]] | [[01_Hash_Tables|← Hash Tables]] | [[03_Hash_Maps|Hash Maps →]]

## What it is
A hash set stores **unique values**. In Python, this is a **set**.

## Simple Example
```python
nums = {1, 2, 3}

# Add a value
nums.add(4)

# Duplicate values are ignored
nums.add(3)

# Check membership
print(2 in nums)  # True

# Remove a value
nums.remove(1)

print(nums)  # {2, 3, 4}
```

## Key Points
- Values are **unique**
- Membership checks are fast
- Sets are great for removing duplicates
