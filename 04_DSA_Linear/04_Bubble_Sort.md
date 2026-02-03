---
title: Bubble Sort Algorithm
tags: [dsa, sorting, bubble-sort, algorithms, beginner]
created: 2026-01-28
difficulty: beginner
complexity: O(n²)
---

# 04. Bubble Sort

[[00_Index|← Back to Index]] | [[03_Arrays|← Previous]] | [[05_Selection_Sort|Next: Selection Sort →]]

> **The simplest sorting algorithm - learn by comparing neighbors**

---

## 🎯 What is Bubble Sort?

**Bubble Sort** repeatedly compares adjacent elements and swaps them if they're in the wrong order. Larger elements "bubble up" to the end of the array.

**Key Idea:** Keep comparing neighbors until no swaps are needed.

---

## 📊 Complexity

| Case | Time Complexity | Explanation |
|------|----------------|-------------|
| **Best** | O(n) | Already sorted - one pass |
| **Average** | O(n²) | Random order |
| **Worst** | O(n²) | Reverse sorted |
| **Space** | O(1) | In-place sorting |

---

## 🎨 Visualization

### How It Works

```
Initial: [5, 2, 8, 1, 9]

Pass 1: Compare adjacent pairs, swap if needed
[5, 2, 8, 1, 9]  → 5 > 2? Yes, swap
[2, 5, 8, 1, 9]  → 5 > 8? No
[2, 5, 8, 1, 9]  → 8 > 1? Yes, swap
[2, 5, 1, 8, 9]  → 8 > 9? No
[2, 5, 1, 8, 9]  ✅ Largest (9) is now at end

Pass 2: Repeat (ignore last element)
[2, 5, 1, 8, 9]  → 2 > 5? No
[2, 5, 1, 8, 9]  → 5 > 1? Yes, swap
[2, 1, 5, 8, 9]  → 5 > 8? No
[2, 1, 5, 8, 9]  ✅ Second largest (8) in place

Pass 3:
[2, 1, 5, 8, 9]  → 2 > 1? Yes, swap
[1, 2, 5, 8, 9]  → 2 > 5? No
[1, 2, 5, 8, 9]  ✅ Sorted!

Final: [1, 2, 5, 8, 9]
```

### Visual Animation

```
Pass 1:  [5  2  8  1  9]
         ↓↓              Compare 5 and 2
        [2  5  8  1  9]  Swap!
            ↓↓           Compare 5 and 8
        [2  5  8  1  9]  No swap
               ↓↓        Compare 8 and 1
        [2  5  1  8  9]  Swap!
                  ↓↓     Compare 8 and 9
        [2  5  1  8  9]  No swap
                     ✓   9 bubbled to end!

Pass 2:  [2  5  1  8 |9]
         ↓↓              Compare 2 and 5
        [2  5  1  8 |9]  No swap
            ↓↓           Compare 5 and 1
        [2  1  5  8 |9]  Swap!
               ↓↓        Compare 5 and 8
        [2  1  5  8 |9]  No swap
                  ✓      8 in place!

Pass 3:  [2  1  5 |8  9]
         ↓↓              Compare 2 and 1
        [1  2  5 |8  9]  Swap!
            ↓↓           Compare 2 and 5
        [1  2  5 |8  9]  No swap
             ✓           5 in place!

Done:    [1  2  5  8  9] ✅ Sorted!
```

---

## 💻 Implementation

### Beginner-Friendly Version

```python
def bubble_sort(numbers):
    # Work on a copy so the original list is unchanged
    nums = numbers[:]
    n = len(nums)

    for pass_index in range(n - 1):
        for i in range(n - 1 - pass_index):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums

data = [5, 2, 8, 1, 9]
print(bubble_sort(data))  # [1, 2, 5, 8, 9]
```

### Basic Version

```python
def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop: n-1 passes
    for i in range(n - 1):
        # Inner loop: compare adjacent elements
        for j in range(n - 1 - i):
            # Compare current with next
            if arr[j] > arr[j + 1]:
                # Swap if in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Example
numbers = [5, 2, 8, 1, 9]
bubble_sort(numbers)
print(numbers)  # [1, 2, 5, 8, 9]
```

### Step-by-Step Explanation

```python
def bubble_sort_explained(arr):
    n = len(arr)  # Get array length
    print(f"Sorting {n} elements")
    
    # Pass through array n-1 times
    for i in range(n - 1):
        print(f"\n--- Pass {i+1} ---")
        
        # Compare adjacent elements
        # Stop at n-1-i because last i elements are sorted
        for j in range(n - 1 - i):
            current = arr[j]
            next_val = arr[j + 1]
            
            print(f"Compare {current} and {next_val}", end=" ")
            
            # Swap if current > next
            if current > next_val:
                arr[j], arr[j + 1] = next_val, current
                print("→ Swap!")
            else:
                print("→ No swap")
        
        print(f"After pass: {arr}")
    
    return arr

# Example
numbers = [5, 2, 8, 1, 9]
bubble_sort_explained(numbers)
```

**Output:**
```
Sorting 5 elements

--- Pass 1 ---
Compare 5 and 2 → Swap!
Compare 5 and 8 → No swap
Compare 8 and 1 → Swap!
Compare 8 and 9 → No swap
After pass: [2, 5, 1, 8, 9]

--- Pass 2 ---
Compare 2 and 5 → No swap
Compare 5 and 1 → Swap!
Compare 5 and 8 → No swap
After pass: [2, 1, 5, 8, 9]

--- Pass 3 ---
Compare 2 and 1 → Swap!
Compare 2 and 5 → No swap
After pass: [1, 2, 5, 8, 9]

--- Pass 4 ---
Compare 1 and 2 → No swap
After pass: [1, 2, 5, 8, 9]
```

### Optimized Version (Early Exit)

```python
def bubble_sort_optimized(arr):
    n = len(arr)
    
    for i in range(n - 1):
        # Flag to detect if any swap happened
        swapped = False
        
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that we swapped
        
        # If no swaps, array is sorted!
        if not swapped:
            print(f"Array sorted after {i+1} passes!")
            break
    
    return arr

# Example: Already sorted
numbers = [1, 2, 3, 4, 5]
bubble_sort_optimized(numbers)
# Output: Array sorted after 1 passes!
```

---

## 🔍 Complexity Analysis

### Time Complexity Breakdown

```python
def bubble_sort(arr):
    n = len(arr)                    # O(1)
    
    for i in range(n - 1):          # O(n) - outer loop
        swapped = False             # O(1)
        
        for j in range(n - 1 - i):  # O(n) - inner loop
            if arr[j] > arr[j + 1]: # O(1) - comparison
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(1) - swap
                swapped = True      # O(1)
        
        if not swapped:             # O(1)
            break                   # O(1)
    
    return arr

# Total: O(n) × O(n) = O(n²) - Dominant term
```

### Pass Count Analysis

```
Elements: n
Passes: n-1 (worst case)

Pass 1: n-1 comparisons
Pass 2: n-2 comparisons
Pass 3: n-3 comparisons
...
Pass n-1: 1 comparison

Total comparisons = (n-1) + (n-2) + ... + 1 = n(n-1)/2 = O(n²)
```

### Best vs Worst Case

```python
# Best Case: O(n)
already_sorted = [1, 2, 3, 4, 5]
# Only 1 pass needed, no swaps → O(n)

# Worst Case: O(n²)
reverse_sorted = [5, 4, 3, 2, 1]
# Every element needs to bubble through entire array
# Pass 1: 4 swaps
# Pass 2: 3 swaps
# Pass 3: 2 swaps
# Pass 4: 1 swap
# Total: 10 swaps = n(n-1)/2 → O(n²)
```

---

## 💡 Practical Examples

### Example 1: Simple Array

```python
numbers = [13, 123, 1, 4, 2, 8, 54, 3, 7, 4, 5]
print("Before:", numbers)
bubble_sort(numbers)
print("After:", numbers)

# Before: [13, 123, 1, 4, 2, 8, 54, 3, 7, 4, 5]
# After: [1, 2, 3, 4, 4, 5, 7, 8, 13, 54, 123]
```

### Example 2: Sorting Names

```python
names = ["Charlie", "Alice", "Bob", "David"]
bubble_sort(names)
print(names)  # ['Alice', 'Bob', 'Charlie', 'David']
```

### Example 3: Descending Order

```python
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Change > to < for descending
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

numbers = [3, 1, 4, 1, 5, 9, 2]
bubble_sort_desc(numbers)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]
```

---

## ✅ When to Use Bubble Sort

### Good For:
✅ **Learning purposes** - easiest to understand  
✅ **Small datasets** - simple implementation  
✅ **Nearly sorted data** - O(n) with optimization  
✅ **Teaching** - visual and intuitive

### Avoid For:
❌ **Large datasets** - O(n²) is too slow  
❌ **Production code** - better alternatives exist  
❌ **Performance-critical** - use Quick/Merge sort

---

## 🎯 Advantages & Disadvantages

### Advantages
✅ **Simple** - Easy to understand and implement  
✅ **In-place** - O(1) extra space  
✅ **Stable** - Preserves order of equal elements  
✅ **Adaptive** - O(n) for nearly sorted data

### Disadvantages
❌ **Slow** - O(n²) average and worst case  
❌ **Not practical** - Rarely used in real applications  
❌ **Many swaps** - More operations than needed

---

## 🔗 Comparison with Other Sorts

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| **Bubble** | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |

---

## 🎓 Key Takeaways

✅ Bubble sort compares **adjacent elements**  
✅ Time complexity: **O(n²)** average and worst  
✅ Can be optimized to **O(n)** for sorted data  
✅ **Stable** and **in-place** algorithm  
✅ Good for **learning**, bad for **production**

---

## 🚀 Next Steps

Now that you understand Bubble Sort:
1. ✅ You can implement basic sorting
2. ✅ You understand O(n²) complexity
3. → Learn [[05_Selection_Sort|Selection Sort]]
4. → Compare different sorting approaches

---

[[00_Index|← Back to Index]] | [[03_Arrays|← Previous]] | [[05_Selection_Sort|Next: Selection Sort →]]

*Simple but effective for learning! 🫧*
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

nums = [5, 2, 8, 1]
draw_sort(nums, title="Before Sorting")
```
