---
title: Merge Sort Algorithm
tags: [dsa, sorting, merge-sort, divide-conquer, stable]
created: 2026-01-28
difficulty: intermediate
complexity: O(n log n)
---

# 10. Merge Sort

[[00_Index|← Back to Index]] | [[09_Radix_Sort|← Previous]] | [[11_Linear_Search|Next: Linear Search →]]

> **Guaranteed O(n log n) - the reliable workhorse**

---

## 🎯 What is Merge Sort?

**Merge Sort** divides the array into halves, recursively sorts them, then merges the sorted halves.

**Key Strategy:** Divide until trivial, then merge back in order.

---

## 📊 Complexity

| Case | Time | Space | Why |
|------|------|-------|-----|
| **Best** | O(n log n) | O(n) | Always divides evenly |
| **Average** | O(n log n) | O(n) | Consistent performance |
| **Worst** | O(n log n) | O(n) | Still divides evenly |
| **Stable** | ✅ Yes | | Preserves order |

**Guarantee:** Always O(n log n), never worse!

---

## 🎨 How It Works

### The Two Phases

**1. Divide Phase** (Top-down)
```
[38, 27, 43, 3, 9, 82, 10]
         ↓ split
[38, 27, 43, 3] | [9, 82, 10]
         ↓             ↓
[38, 27] [43, 3]  [9, 82] [10]
   ↓       ↓        ↓       ↓
[38] [27] [43] [3] [9] [82] [10]
 ↓    ↓    ↓   ↓   ↓   ↓    ↓
All single elements (trivially sorted)
```

**2. Merge Phase** (Bottom-up)
```
[38] [27] → [27, 38]
[43] [3]  → [3, 43]
[9] [82]  → [9, 82]
[10]      → [10]

[27, 38] [3, 43] → [3, 27, 38, 43]
[9, 82] [10]     → [9, 10, 82]

[3, 27, 38, 43] [9, 10, 82] → [3, 9, 10, 27, 38, 43, 82]
✓ Sorted!
```

---

## 💻 Implementation

### Beginner-Friendly Version (Readable, Recursive)

```python
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

data = [5, 2, 4, 6, 1, 3]
print(merge_sort(data))  # [1, 2, 3, 4, 5, 6]
```

### Complete Implementation

```python
def merge_sort(arr):
    """Sort array using merge sort"""
    # Base case: array of 0 or 1 element is sorted
    if len(arr) <= 1:
        return arr
    
    # Divide: split array in half
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Conquer: recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Combine: merge sorted halves
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays into one sorted array"""
    result = []
    i = j = 0
    
    # Compare elements from left and right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Usage
numbers = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(numbers)
print(sorted_arr)  # [3, 9, 10, 27, 38, 43, 82]
```

### Step-by-Step Merge Explanation

```python
def merge_explained(left, right):
    """Merge with detailed output"""
    print(f"\nMerging {left} and {right}")
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            print(f"  {left[i]} ≤ {right[j]} → take {left[i]} from left")
            result.append(left[i])
            i += 1
        else:
            print(f"  {left[i]} > {right[j]} → take {right[j]} from right")
            result.append(right[j])
            j += 1
    
    # Add remaining
    if i < len(left):
        print(f"  Add remaining from left: {left[i:]}")
        result.extend(left[i:])
    if j < len(right):
        print(f"  Add remaining from right: {right[j:]}")
        result.extend(right[j:])
    
    print(f"  Result: {result}")
    return result

# Example
merge_explained([3, 27, 38, 43], [9, 10, 82])

# Output:
# Merging [3, 27, 38, 43] and [9, 10, 82]
#   3 ≤ 9 → take 3 from left
#   27 > 9 → take 9 from right
#   27 > 10 → take 10 from right
#   27 ≤ 82 → take 27 from left
#   38 ≤ 82 → take 38 from left
#   43 ≤ 82 → take 43 from left
#   Add remaining from right: [82]
#   Result: [3, 9, 10, 27, 38, 43, 82]
```

---

## 🔍 Merge Process Visualization

### Merging [3, 27] and [9, 38]

```
Initial state:
Left:  [3, 27]    Right: [9, 38]
        ↑                  ↑
        i=0                j=0
Result: []

Step 1: Compare 3 vs 9
Left:  [3, 27]    Right: [9, 38]
        ↑                  ↑
3 < 9 → take 3
Result: [3]
        i=1, j=0

Step 2: Compare 27 vs 9
Left:  [3, 27]    Right: [9, 38]
           ↑                 ↑
27 > 9 → take 9
Result: [3, 9]
        i=1, j=1

Step 3: Compare 27 vs 38
Left:  [3, 27]    Right: [9, 38]
           ↑                    ↑
27 < 38 → take 27
Result: [3, 9, 27]
        i=2, j=1

Step 4: Left exhausted, take remaining from right
Result: [3, 9, 27, 38] ✓
```

---

## 📈 Recursion Tree Analysis

```
Example: [38, 27, 43, 3, 9, 82, 10]

Divide Phase:                        Merge Phase:
Level 0: [38,27,43,3,9,82,10]       [3,9,10,27,38,43,82] ← n ops
        /                \
Level 1: [38,27,43,3]  [9,82,10]    merge(left,right)  ← n ops
        /        \      /      \
Level 2: [38,27] [43,3] [9,82] [10]  merge pairs       ← n ops
        /  \     / \    / \     |
Level 3: [38][27][43][3][9][82][10]  trivial           ← n ops

Levels: log₂(7) ≈ 3
Work per level: n comparisons/moves
Total: n × log n = O(n log n)
```

---

## 🧮 Time Complexity Proof

### Master Theorem

```
Recurrence: T(n) = 2T(n/2) + O(n)
           ↑       ↑          ↑
        2 subproblems        merging
        each size n/2

Using Master Theorem:
a = 2, b = 2, f(n) = n
log_b(a) = log₂(2) = 1

Since f(n) = Θ(n^1), Case 2 applies:
T(n) = Θ(n log n)
```

### Detailed Count

```
For n=8 elements:

Level 0: 1 array of 8 = 8 operations
Level 1: 2 arrays of 4 = 8 operations
Level 2: 4 arrays of 2 = 8 operations
Level 3: 8 arrays of 1 = 0 operations (base)

Levels = log₂(8) = 3
Ops per level = 8
Total = 8 × 3 = 24 = n log n
```

---

## 💡 Practical Examples

### Example 1: In-Place Merge Sort (Optimized)

```python
def merge_sort_inplace(arr, left, right):
    """Sort arr[left:right+1] in-place"""
    if left < right:
        mid = (left + right) // 2
        
        # Sort halves
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        
        # Merge in-place
        merge_inplace(arr, left, mid, right)

def merge_inplace(arr, left, mid, right):
    """Merge arr[left:mid+1] and arr[mid+1:right+1]"""
    # Create temp arrays
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    
    i = j = 0
    k = left
    
    # Merge back into arr
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

# Usage
numbers = [38, 27, 43, 3, 9, 82, 10]
merge_sort_inplace(numbers, 0, len(numbers) - 1)
print(numbers)  # [3, 9, 10, 27, 38, 43, 82]
```

### Example 2: Count Inversions

```python
def count_inversions(arr):
    """Count inversions using merge sort"""
    def merge_count(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, left_inv = merge_count(arr[:mid])
        right, right_inv = merge_count(arr[mid:])
        
        merged, split_inv = merge_and_count(left, right)
        
        return merged, left_inv + right_inv + split_inv
    
    def merge_and_count(left, right):
        result = []
        inversions = 0
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                inversions += len(left) - i  # All remaining in left
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inversions
    
    _, count = merge_count(arr)
    return count

# Example: [2,4,1,3,5] has inversions: (2,1), (4,1), (4,3)
print(count_inversions([2, 4, 1, 3, 5]))  # 3
```

---

## ✅ Merge Sort vs Quick Sort

| Feature | Merge Sort | Quick Sort |
|---------|------------|------------|
| **Best** | O(n log n) | O(n log n) |
| **Average** | O(n log n) | O(n log n) |
| **Worst** | O(n log n) | O(n²) |
| **Space** | O(n) | O(log n) |
| **Stable** | ✅ Yes | ❌ No |
| **In-place** | ❌ No | ✅ Yes |
| **Predictable** | ✅ Yes | ❌ No |
| **Cache** | ❌ Poor | ✅ Good |

**When to use Merge Sort:**
- ✅ Need guaranteed O(n log n)
- ✅ Need stable sort
- ✅ Sorting linked lists
- ✅ External sorting (large data)

**When to use Quick Sort:**
- ✅ Need in-place sorting
- ✅ Average case is fine
- ✅ Memory is limited

---

## 🔧 Optimizations

### 1. Switch to Insertion Sort for Small Arrays

```python
def merge_sort_optimized(arr):
    # Use insertion sort for small arrays (< 10 elements)
    if len(arr) < 10:
        return insertion_sort(arr)
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_optimized(arr[:mid])
    right = merge_sort_optimized(arr[mid:])
    
    return merge(left, right)
```

### 2. Check if Already Sorted

```python
def merge_optimized(left, right):
    # If already in order, just concatenate
    if left[-1] <= right[0]:
        return left + right
    
    # Otherwise merge normally
    return merge(left, right)
```

---

## 🎓 Key Takeaways

✅ **Divide and conquer** with merging  
✅ **O(n log n)** guaranteed - all cases  
✅ **Stable** - preserves equal element order  
✅ **Predictable** - no worst-case degradation  
✅ **Space:** O(n) - needs extra arrays  
✅ **Best for:** Linked lists, external sorting  

---

## 🚀 Next Steps

1. ✅ Understand divide-conquer pattern
2. ✅ Master merging technique
3. → Learn [[12_Binary_Search|Binary Search]]
4. → Compare with [[07_Quick_Sort|Quick Sort]]

---

[[00_Index|← Back to Index]] | [[09_Radix_Sort|← Previous]] | [[11_Linear_Search|Next: Linear Search →]]

*Divide, sort, merge! 🔀*
---

## 🎨 Visualization (Optional)

```python
import sys
from pathlib import Path

# Add vault root to sys.path (Obsidian runner)
vault_root = Path.cwd()
if str(vault_root) not in sys.path:
    sys.path.append(str(vault_root))

from DSA_Utils.utils import draw_sort

nums = [5, 2, 4, 6, 1, 3]
draw_sort(nums, title="Before Sorting")
```
