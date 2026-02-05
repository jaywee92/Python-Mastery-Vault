---
title: Arrays - The Foundation
tags: [dsa, arrays, data-structures, fundamentals]
created: 2026-01-28
difficulty: beginner
---

# 03. Arrays: The Foundation

[[00_Index|← Back to Index]] | [[02_Big_O_Notation|← Previous]] | [[04_Bubble_Sort|Next: Bubble Sort →]]

> **Master the most fundamental data structure**

---

## 🎯 What is an Array?

An **array** is a collection of elements stored in contiguous memory locations, accessed by index.

**Key Properties:**
- ✅ Fixed or dynamic size
- ✅ Elements of same type
- ✅ O(1) access by index
- ✅ Sequential memory storage

**Visual Representation:**
```
Index:    0    1    2    3    4
        ┌────┬────┬────┬────┬────┐
Array:  │ 10 │ 20 │ 30 │ 40 │ 50 │
        └────┴────┴────┴────┴────┘
Memory: 1000 1004 1008 1012 1016  (addresses)
```

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║          📦 ARRAYS - SEQUENTIAL MEMORY CONTAINERS             ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Index (Label):    0      1      2      3      4             ║
║                   ┌──────┬──────┬──────┬──────┬──────┐        ║
║  Array Data:      │ 10   │ 20   │ 30   │ 40   │ 50   │        ║
║                   └──────┴──────┴──────┴──────┴──────┘        ║
║  Memory Address: 1000   1004   1008   1012   1016            ║
║                   ↑                                           ║
║             Contiguous Memory = Fast Access!                 ║
║                                                               ║
║  💡 O(1) Access: arr[2] = 30  (direct calculation)           ║
║  ⚠️  O(n) Insertion: Must shift elements right               ║
║  ⚠️  O(n) Deletion: Must shift elements left                 ║
║                                                               ║
║  Memory is like a row of lockers - each box holds           ║
║  one value, and we jump directly to the one we need!        ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📊 Array Operations & Complexity

| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| **Access** | O(1) | Direct index access |
| **Search** | O(n) | Check each element |
| **Insert (end)** | O(1)* | Append to end |
| **Insert (middle)** | O(n) | Shift elements right |
| **Delete (end)** | O(1) | Remove last |
| **Delete (middle)** | O(n) | Shift elements left |

*Amortized O(1) for dynamic arrays

---

## 💻 Python Lists (Dynamic Arrays)

### Beginner-Friendly Example

```python
# A list is Python's built-in dynamic array
scores = [10, 20, 30]

# Read by index (O(1))
print(scores[0])  # 10

# Add to the end (amortized O(1))
scores.append(40)
print(scores)  # [10, 20, 30, 40]

# Insert in the middle (O(n))
scores.insert(1, 15)
print(scores)  # [10, 15, 20, 30, 40]

# Remove by value (O(n))
scores.remove(30)
print(scores)  # [10, 15, 20, 40]
```

### Creating Arrays

```python
# Empty array
arr = []
arr = list()

# With initial values
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Using list comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# From other iterables
from_string = list("hello")  # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(10))  # [0, 1, 2, ..., 9]
```

### Accessing Elements - O(1)

```python
numbers = [10, 20, 30, 40, 50]

# Positive indexing
first = numbers[0]      # 10
third = numbers[2]      # 30

# Negative indexing
last = numbers[-1]      # 50
second_last = numbers[-2]  # 40

# Slicing - O(k) where k is slice size
subset = numbers[1:4]   # [20, 30, 40]
every_second = numbers[::2]  # [10, 30, 50]
reversed_arr = numbers[::-1]  # [50, 40, 30, 20, 10]
```

### Modifying Elements - O(1)

```python
numbers = [10, 20, 30, 40, 50]

# Change single element
numbers[0] = 100        # [100, 20, 30, 40, 50]
numbers[-1] = 500       # [100, 20, 30, 40, 500]

# Change slice
numbers[1:3] = [200, 300]  # [100, 200, 300, 40, 500]
```

---

## ➕ Adding Elements

### Append (End) - O(1)

```python
numbers = [1, 2, 3]
numbers.append(4)       # [1, 2, 3, 4]
numbers.append(5)       # [1, 2, 3, 4, 5]

# Visual:
# [1, 2, 3] + [4] = [1, 2, 3, 4]  ← Just add to end!
```

### Insert (Middle) - O(n)

```python
numbers = [1, 2, 4, 5]
numbers.insert(2, 3)    # [1, 2, 3, 4, 5]
#              ↑ index

# Visual - Must shift elements:
# Before: [1, 2, 4, 5]
#              ↓ insert 3 at index 2
# Shift:  [1, 2, _, 4, 5]  ← Move 4,5 right
# After:  [1, 2, 3, 4, 5]  ← Insert 3
```

### Extend (Multiple) - O(k)

```python
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])  # [1, 2, 3, 4, 5, 6]

# Same as:
numbers = numbers + [4, 5, 6]
```

---

## ➖ Removing Elements

### Remove by Value - O(n)

```python
numbers = [1, 2, 3, 2, 4]
numbers.remove(2)       # [1, 3, 2, 4]  ← Removes first 2
# Must search for value (O(n)), then shift (O(n))
```

### Pop (Remove & Return) - O(1) or O(n)

```python
numbers = [1, 2, 3, 4, 5]

# Pop last - O(1)
last = numbers.pop()    # returns 5, list: [1, 2, 3, 4]

# Pop specific index - O(n)
second = numbers.pop(1) # returns 2, list: [1, 3, 4]
#                ↑ Must shift elements after removal
```

### Delete by Index - O(n)

```python
numbers = [1, 2, 3, 4, 5]
del numbers[2]          # [1, 2, 4, 5]  ← Must shift

# Delete slice
del numbers[1:3]        # [1, 5]
```

### Clear All - O(1)

```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()         # []
```

---

## 🔍 Searching in Arrays

### Linear Search - O(n)

```python
def linear_search(arr, target):
    """Search for target, return index or -1"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [10, 20, 30, 40, 50]
index = linear_search(numbers, 30)  # Returns 2

# Python built-in:
index = numbers.index(30)           # Returns 2
# numbers.index(99)                 # Raises ValueError!
```

### Check Membership - O(n)

```python
numbers = [10, 20, 30, 40, 50]

# Check if exists
exists = 30 in numbers              # True
not_exists = 99 in numbers          # False

# Count occurrences
count = numbers.count(30)           # 1
```

---

## 📦 Common Array Patterns

### Find Min/Max - O(n)

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

minimum = min(numbers)              # 1
maximum = max(numbers)              # 9

# Manual implementation:
def find_min(arr):
    if not arr:
        return None
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val
```

### Sum/Average - O(n)

```python
numbers = [1, 2, 3, 4, 5]

total = sum(numbers)                # 15
average = sum(numbers) / len(numbers)  # 3.0

# Manual:
def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

### Reverse Array - O(n)

```python
numbers = [1, 2, 3, 4, 5]

# Method 1: Built-in
numbers.reverse()                   # [5, 4, 3, 2, 1]

# Method 2: Slicing
reversed_arr = numbers[::-1]        # [5, 4, 3, 2, 1]

# Method 3: Manual (in-place)
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

### Rotate Array - O(n)

```python
def rotate_right(arr, k):
    """Rotate array right by k positions"""
    if not arr:
        return arr
    k = k % len(arr)  # Handle k > len
    return arr[-k:] + arr[:-k]

numbers = [1, 2, 3, 4, 5]
rotated = rotate_right(numbers, 2)  # [4, 5, 1, 2, 3]

# Visual:
# Original: [1, 2, 3, 4, 5]
# Rotate 2: [4, 5, 1, 2, 3]
#            ↑─────↑ These moved to front
```

---

## 🎯 Two Pointer Technique

### Remove Duplicates - O(n)

```python
def remove_duplicates(arr):
    """Remove duplicates from sorted array in-place"""
    if len(arr) <= 1:
        return len(arr)
    
    # Two pointers: slow and fast
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1  # New length

# Example:
nums = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(nums)
print(nums[:new_length])  # [1, 2, 3, 4, 5]

# Visual:
# [1, 1, 2, 2, 3, 4, 4, 5]
#  ↑slow  ↑fast
# [1, 2, 2, 2, 3, 4, 4, 5]  ← fast found different, copy to slow+1
#     ↑slow     ↑fast
```

### Two Sum Problem - O(n)

```python
def two_sum(arr, target):
    """Find two numbers that sum to target"""
    seen = {}  # Store value: index
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None

numbers = [2, 7, 11, 15]
indices = two_sum(numbers, 9)  # [0, 1] because 2+7=9
```

---

## 💡 Practical Examples

### Example 1: Filter Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Method 1: List comprehension
evens = [x for x in numbers if x % 2 == 0]
# [2, 4, 6, 8, 10]

# Method 2: Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

### Example 2: Running Sum

```python
def running_sum(arr):
    """Calculate running sum [1,2,3,4] → [1,3,6,10]"""
    result = [arr[0]] if arr else []
    
    for i in range(1, len(arr)):
        result.append(result[-1] + arr[i])
    
    return result

numbers = [1, 2, 3, 4]
print(running_sum(numbers))  # [1, 3, 6, 10]

# Visual:
# [1, 2, 3, 4]
# [1, 1+2, 1+2+3, 1+2+3+4]
# [1, 3, 6, 10]
```

### Example 3: Merge Sorted Arrays

```python
def merge_sorted(arr1, arr2):
    """Merge two sorted arrays into one sorted array"""
    result = []
    i, j = 0, 0
    
    # Compare elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
merged = merge_sorted(arr1, arr2)
print(merged)  # [1, 2, 3, 4, 5, 6, 7, 8]
```

---

## 🔧 Python List Methods Summary

```python
arr = [1, 2, 3]

# Adding
arr.append(4)           # Add to end - O(1)
arr.insert(0, 0)        # Insert at index - O(n)
arr.extend([5, 6])      # Add multiple - O(k)

# Removing
arr.remove(3)           # Remove first occurrence - O(n)
arr.pop()               # Remove & return last - O(1)
arr.pop(0)              # Remove at index - O(n)
arr.clear()             # Remove all - O(1)

# Searching
arr.index(2)            # Find index - O(n)
arr.count(1)            # Count occurrences - O(n)
2 in arr                # Check membership - O(n)

# Sorting
arr.sort()              # Sort in-place - O(n log n)
sorted(arr)             # Return sorted copy - O(n log n)
arr.reverse()           # Reverse in-place - O(n)

# Other
len(arr)                # Get length - O(1)
arr.copy()              # Shallow copy - O(n)
```

---

## ⚡ Performance Tips

### ✅ Fast Operations

```python
# O(1) - Fast
arr[i]                  # Access by index
arr.append(x)           # Add to end
arr.pop()               # Remove from end
len(arr)                # Get length
```

### ⚠️ Slow Operations

```python
# O(n) - Slower
arr.insert(0, x)        # Insert at start
arr.pop(0)              # Remove from start
x in arr                # Search for value
arr.remove(x)           # Remove by value
```

### 💡 Optimizations

```python
# ❌ Slow: Build array with insert
result = []
for i in range(1000):
    result.insert(0, i)  # O(n) each time = O(n²) total!

# ✅ Fast: Use append + reverse
result = []
for i in range(1000):
    result.append(i)     # O(1) each time = O(n) total
result.reverse()         # O(n) once
```

---

## 🎓 Key Takeaways

✅ Arrays provide **O(1)** index access  
✅ Insertion/deletion at **end** is O(1)  
✅ Insertion/deletion in **middle** is O(n)  
✅ Searching unsorted array is **O(n)**  
✅ Python lists are **dynamic arrays**  
✅ Understanding arrays is **fundamental** for all DSA

---

## 🚀 Next Steps

Master arrays before sorting:
1. ✅ Understand O(1) access
2. ✅ Know operation complexities
3. → Learn [[04_Bubble_Sort|Bubble Sort]]
4. → Practice array problems

---

[[00_Index|← Back to Index]] | [[02_Big_O_Notation|← Previous]] | [[04_Bubble_Sort|Next: Bubble Sort →]]

*Arrays are everywhere! Master them! 📦*
