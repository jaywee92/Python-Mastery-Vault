---
title: Counting Sort
tags: [dsa, sorting, counting-sort, non-comparison]
difficulty: intermediate
complexity: O(n+k)
---

# 08. Counting Sort

[[00_Index|← Back]] | [[07_Quick_Sort|← Previous]] | [[09_Radix_Sort|Next →]]

> **Non-comparison sort for integers**

## 🎯 Algorithm

Count occurrences of each value, then reconstruct sorted array.

## 📊 Complexity

| Metric | Value |
|--------|-------|
| Time | O(n + k) |
| Space | O(k) |

*n = array size, k = range of values*

## 🎨 Visualization

```
Input: [4, 2, 2, 8, 3, 3, 1]
Range: 1-8

Count array:
Index: 1  2  3  4  5  6  7  8
Count: 1  2  2  1  0  0  0  1

Output: [1, 2, 2, 3, 3, 4, 8] ✓
```

## 💻 Code

```python
def counting_sort(arr):
    if not arr:
        return arr
    
    # Find range
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    # Rebuild array
    result = []
    for i in range(range_size):
        result.extend([i + min_val] * count[i])
    
    return result

numbers = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(numbers)
print(sorted_arr)  # [1, 2, 2, 3, 3, 4, 8]
```

## ✅ Key Points

- **O(n + k)** where k = range
- **Not comparison-based**
- **Stable** if implemented carefully
- **Great for small integer ranges**
- **Poor for large ranges** (wastes space)

[[00_Index|← Back]] | [[07_Quick_Sort|← Previous]] | [[09_Radix_Sort|Next →]]
---

## 🎨 Visualization (Optional)

```python
from DSA_Utils.utils import draw_sort

nums = [4, 2, 2, 8, 3, 3, 1]
draw_sort(nums, title="Before Sorting")
```
