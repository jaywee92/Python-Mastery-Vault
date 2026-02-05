---
title: Binary Search Algorithm
tags: [dsa, searching, binary-search, algorithms, logarithmic]
created: 2026-01-28
difficulty: beginner-intermediate
complexity: O(log n)
---

# 12. Binary Search

[[00_Index|← Back to Index]] | [[11_Linear_Search|← Previous]] | [[13_Stacks|Next: Stacks →]]

> **The fastest search algorithm - O(log n) magic**

---

## 🎯 What is Binary Search?

**Binary Search** finds an element in a **sorted array** by repeatedly dividing the search space in half.

**Requirement:** Array MUST be sorted!
**Speed:** O(log n) - incredibly fast!

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║         🎯 BINARY SEARCH - HALBE & HERRSCHE                  ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Suche 7 in: [1, 3, 5, 7, 9, 11, 13, 15, 17]                ║
║             (Muss sortiert sein!)                            ║
║                                                               ║
║  Step 1: Check Mitte (Index 4)                              ║
║  [1, 3, 5, 7, 9, 11, 13, 15, 17]                            ║
║                 ↑ = 9                                        ║
║              9 > 7 → Suche LINKS                             ║
║                                                               ║
║  Step 2: Check Mitte von links (Index 1)                    ║
║  [1, 3, 5, 7]                                               ║
║     ↑ = 3                                                   ║
║     3 < 7 → Suche RECHTS                                     ║
║                                                               ║
║  Step 3: Check Mitte (Index 2-3)                            ║
║  [5, 7]                                                     ║
║        ↑ = 7                                                ║
║        7 == 7 → ✓ GEFUNDEN!                                 ║
║                                                               ║
║  Nur 3 Schritte statt 9!                                     ║
║                                                               ║
║  💡 Teile in zwei Hälften                                     ║
║  💡 Geh in die Hälfte wo Ziel ist                            ║
║  💡 O(log n) = exponentiell schneller!                       ║
║  💡 WICHTIG: Nur auf sortierte Arrays!                       ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📊 Complexity

| Operation | Time | Why |
|-----------|------|-----|
| **Search** | O(log n) | Halves space each step |
| **Space** | O(1) | Iterative version |
| **Space** | O(log n) | Recursive version |

**Speed comparison:**
```
Linear Search: 1,000,000 elements → 1,000,000 steps
Binary Search: 1,000,000 elements → 20 steps! ⚡
```

---

## 🎨 How It Works

### The Algorithm

```
1. Start with entire sorted array
2. Check middle element
3. If target equals middle → Found!
4. If target < middle → Search left half
5. If target > middle → Search right half
6. Repeat until found or no more space
```

### Visual Example

```
Search for 7 in [1, 3, 5, 7, 9, 11, 13, 15, 17]

Step 1: Check middle (index 4)
[1, 3, 5, 7, 9, 11, 13, 15, 17]
             ↑
             9 > 7 → search left

Step 2: Check middle of left half (index 1)
[1, 3, 5, 7]
    ↑
    3 < 7 → search right

Step 3: Check middle of right section (index 3)
[5, 7]
    ↑
    7 == 7 → FOUND! ✓

Only 3 comparisons for 9 elements!
```

### Complete Search Animation

```
Array: [1, 3, 5, 7, 9, 11, 13, 15, 17]
Target: 7

Iteration 1:
[1, 3, 5, 7, 9, 11, 13, 15, 17]
 ↑        ↑        ↑
low      mid      high
Compare 9 vs 7 → 9 > 7, go left

Iteration 2:
[1, 3, 5, 7]
 ↑  ↑     ↑
low mid  high
Compare 3 vs 7 → 3 < 7, go right

Iteration 3:
[5, 7]
 ↑  ↑
mid=high
Compare 7 vs 7 → FOUND at index 3! ✓
```

---

## 💻 Implementation

### Beginner-Friendly Version (Iterative)

```python
def binary_search(sorted_numbers, target):
    left = 0
    right = len(sorted_numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_numbers[mid]

        if mid_value == target:
            return mid
        if mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

data = [1, 3, 5, 7, 9, 11]
print(binary_search(data, 7))   # 3
print(binary_search(data, 4))   # -1
```

### Iterative Version (Recommended)

```python
def binary_search(arr, target):
    """
    Search for target in sorted array.
    Returns index if found, -1 if not found.
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        # Calculate middle (avoid overflow)
        mid = left + (right - left) // 2
        
        # Check if target is at mid
        if arr[mid] == target:
            return mid
        
        # If target is smaller, search left half
        elif arr[mid] > target:
            right = mid - 1
        
        # If target is larger, search right half
        else:  # arr[mid] < target
            left = mid + 1
    
    # Target not found
    return -1

# Usage
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
index = binary_search(numbers, 7)
print(f"Found at index: {index}")  # Found at index: 3
```

### Step-by-Step Explanation

```python
def binary_search_explained(arr, target):
    """Binary search with detailed output"""
    left = 0
    right = len(arr) - 1
    step = 1
    
    print(f"Searching for {target} in {arr}")
    
    while left <= right:
        mid = left + (right - left) // 2
        
        print(f"\nStep {step}:")
        print(f"  Range: arr[{left}:{right+1}] = {arr[left:right+1]}")
        print(f"  Middle index: {mid}, value: {arr[mid]}")
        
        if arr[mid] == target:
            print(f"  ✓ Found {target} at index {mid}!")
            return mid
        
        elif arr[mid] > target:
            print(f"  {arr[mid]} > {target} → Search LEFT half")
            right = mid - 1
        
        else:
            print(f"  {arr[mid]} < {target} → Search RIGHT half")
            left = mid + 1
        
        step += 1
    
    print(f"\n  ✗ {target} not found in array")
    return -1

# Example
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
binary_search_explained(numbers, 7)

# Output:
# Searching for 7 in [1, 3, 5, 7, 9, 11, 13, 15, 17]
#
# Step 1:
#   Range: arr[0:9] = [1, 3, 5, 7, 9, 11, 13, 15, 17]
#   Middle index: 4, value: 9
#   9 > 7 → Search LEFT half
#
# Step 2:
#   Range: arr[0:4] = [1, 3, 5, 7]
#   Middle index: 1, value: 3
#   3 < 7 → Search RIGHT half
#
# Step 3:
#   Range: arr[2:4] = [5, 7]
#   Middle index: 3, value: 7
#   ✓ Found 7 at index 3!
```

### Recursive Version

```python
def binary_search_recursive(arr, target, left, right):
    """Recursive binary search"""
    # Base case: search space exhausted
    if left > right:
        return -1
    
    # Calculate middle
    mid = left + (right - left) // 2
    
    # Found target
    if arr[mid] == target:
        return mid
    
    # Search left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    
    # Search right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# Usage
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
index = binary_search_recursive(numbers, 7, 0, len(numbers) - 1)
print(f"Found at index: {index}")  # Found at index: 3
```

---

## 🔍 Why O(log n)?

### Mathematical Proof

```
Each iteration halves the search space:

Start:  n elements
Step 1: n/2 elements
Step 2: n/4 elements
Step 3: n/8 elements
...
Step k: n/2^k = 1 element

Solve for k:
n/2^k = 1
2^k = n
k = log₂(n)

Therefore: O(log n) steps
```

### Practical Examples

```
Array Size    Linear Search    Binary Search
─────────────────────────────────────────────
10            10 steps         4 steps
100           100 steps        7 steps
1,000         1,000 steps      10 steps
1,000,000     1,000,000 steps  20 steps! ⚡
1,000,000,000 1 billion steps  30 steps! 🚀
```

---

## ⚠️ Common Pitfalls

### Pitfall 1: Integer Overflow

```python
# ❌ Bad: Can overflow with large indices
mid = (left + right) // 2

# ✅ Good: Prevents overflow
mid = left + (right - left) // 2
```

### Pitfall 2: Infinite Loop

```python
# ❌ Bad: Can create infinite loop
while left < right:  # Should be <=
    mid = (left + right) // 2
    if arr[mid] < target:
        left = mid  # Should be mid + 1
    else:
        right = mid - 1

# ✅ Good: Correct boundaries
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] < target:
        left = mid + 1  # Move past mid
    else:
        right = mid - 1
```

### Pitfall 3: Unsorted Array

```python
# ❌ Binary search on unsorted array = WRONG
arr = [5, 2, 8, 1, 9]
binary_search(arr, 8)  # Will give wrong result!

# ✅ Sort first
arr.sort()  # [1, 2, 5, 8, 9]
binary_search(arr, 8)  # Correct!
```

---

## 💡 Variations & Applications

### Find First Occurrence

```python
def binary_search_first(arr, target):
    """Find first occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid  # Record position
            right = mid - 1  # Continue searching left
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return result

# Example: [1, 2, 2, 2, 3, 4, 5]
arr = [1, 2, 2, 2, 3, 4, 5]
print(binary_search_first(arr, 2))  # 1 (first occurrence)
```

### Find Last Occurrence

```python
def binary_search_last(arr, target):
    """Find last occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid  # Record position
            left = mid + 1  # Continue searching right
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return result

# Example
arr = [1, 2, 2, 2, 3, 4, 5]
print(binary_search_last(arr, 2))  # 3 (last occurrence)
```

### Find Insert Position

```python
def search_insert(arr, target):
    """Find position where target should be inserted"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return left  # Insert position

# Example
arr = [1, 3, 5, 6]
print(search_insert(arr, 5))  # 2
print(search_insert(arr, 2))  # 1 (insert between 1 and 3)
print(search_insert(arr, 7))  # 4 (insert at end)
```

### Search in Rotated Array

```python
def search_rotated(arr, target):
    """Binary search in rotated sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Example: [4, 5, 6, 7, 0, 1, 2] (rotated at index 4)
arr = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated(arr, 0))  # 4
```

---

## 🎯 When to Use Binary Search

### ✅ Use When:
- Array is **sorted**
- Need **fast searches** (O(log n))
- Array is **large**
- **Multiple searches** on same array
- Finding **boundaries** (first/last occurrence)

### ❌ Don't Use When:
- Array is **not sorted** (sort first or use linear)
- Array is **very small** (< 10 elements)
- Only **one search** needed
- Need to find **all occurrences**

---

## 📊 Binary Search vs Linear Search

| Feature | Binary | Linear |
|---------|--------|--------|
| **Time** | O(log n) | O(n) |
| **Requirement** | Sorted | Any order |
| **Best for** | Large arrays | Small arrays |
| **Implementation** | More complex | Simple |
| **Use case** | Repeated searches | Single search |

---

## 🎓 Key Takeaways

✅ **O(log n)** - Incredibly fast  
✅ **Requires sorted array** - Must sort first  
✅ **Halves search space** each iteration  
✅ **Iterative preferred** over recursive  
✅ **Watch for** integer overflow & boundaries  
✅ **Many variations** - first, last, insert position  

---

## 🚀 Next Steps

1. ✅ Understand halving concept
2. ✅ Practice boundary conditions
3. → Learn [[13_Stacks|Stacks]] data structure
4. → Solve LeetCode binary search problems

---

[[00_Index|← Back to Index]] | [[11_Linear_Search|← Previous]] | [[13_Stacks|Next: Stacks →]]

*Divide and search! 🔍*
