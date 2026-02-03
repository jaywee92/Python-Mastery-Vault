---
title: Radix Sort
tags: [dsa, sorting, radix-sort, non-comparison]
difficulty: intermediate
complexity: O(d(n+k))
---

# 09. Radix Sort

[[00_Index|← Back]] | [[08_Counting_Sort|← Previous]] | [[10_Merge_Sort|Next →]]

> **Sort by digits - from least to most significant**

## 🎯 Algorithm

Sort by each digit position using counting sort.

## 📊 Complexity

| Metric | Value |
|--------|-------|
| Time | O(d × (n + k)) |
| Space | O(n + k) |

*d = digits, n = elements, k = base (10)*

## 🎨 Visualization

```
Input: [170, 45, 75, 90, 802, 24, 2, 66]

Pass 1 (ones place):
0  2  4  5  6  0  2
170 802 24 45 66 90 2 75

Pass 2 (tens place):
2  24 45 66 70 75 90 802

Pass 3 (hundreds place):
2 24 45 66 75 90 170 802 ✓
```

## 💻 Code

```python
def radix_sort(arr):
    if not arr:
        return arr
    
    # Find max to know number of digits
    max_val = max(arr)
    exp = 1
    
    # Sort by each digit
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count occurrences
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output (stable)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    # Copy back
    for i in range(n):
        arr[i] = output[i]

numbers = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(numbers)
print(numbers)  # [2, 24, 45, 66, 75, 90, 170, 802]
```

## ✅ Key Points

- **O(d(n + k))** linear for fixed digits
- **Stable** sort
- **Not comparison-based**
- **Good for integers** with fixed digits
- **Poor for** variable-length data

[[00_Index|← Back]] | [[08_Counting_Sort|← Previous]] | [[10_Merge_Sort|Next →]]
---

## 🎨 Visualization (Optional)

```python
import sys
import site
from pathlib import Path

# Ensure user site-packages are visible (Obsidian runner)
user_site = site.getusersitepackages()
if user_site and user_site not in sys.path:
    sys.path.append(user_site)

# Add vault root to sys.path (Obsidian runner)
# Tries current dir, parent dirs, then a known vault path fallback.
added = False
for p in [Path.cwd(), *Path.cwd().parents]:
    if (p / "DSA_Utils").exists():
        sys.path.append(str(p))
        added = True
        break

if not added:
    fallback = Path("/Users/jochenwahl/Library/CloudStorage/OneDrive-Persönlich/z99_Obsidian_Vault/Codex_Coding")
    if fallback.exists():
        sys.path.append(str(fallback))

from DSA_Utils.utils import draw_sort

values = [170, 45, 75, 90, 802, 24, 2, 66]
# Start state for radix sort
draw_sort(values, title="Radix Sort (start)")

```
