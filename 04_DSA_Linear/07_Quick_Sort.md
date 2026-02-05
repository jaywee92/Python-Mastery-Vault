---
title: Quick Sort Algorithm
tags: [dsa, sorting, quick-sort, divide-conquer, advanced]
created: 2026-01-28
difficulty: intermediate
complexity: O(n log n)
---

# 07. Quick Sort

[[00_Index|← Back to Index]] | [[06_Insertion_Sort|← Previous]] | [[08_Counting_Sort|Next: Counting Sort →]]

> **The fastest comparison-based sort - divide and conquer at its best**

---

## 🎯 What is Quick Sort?

**Quick Sort** uses a pivot element to partition the array into smaller and larger elements, then recursively sorts each partition.

**Key Strategy:** Divide and conquer with intelligent partitioning.

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║         ⚡ QUICK SORT - DIVIDE & CONQUER LIGHTNING            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  [8, 3, 1, 7, 0, 10, 2]                                      ║
║         Choose pivot (e.g. last = 2)                         ║
║                                                               ║
║   Partition Phase:                                           ║
║   Small on left → Pivot → Large on right                     ║
║                                                               ║
║   [1, 0]  < 2  [2]  > 2  [8, 3, 10, 7]                       ║
║    unsorted  ✓ (correct place)  unsorted                      ║
║                                                               ║
║   Recursively sort left:                                     ║
║   [1, 0] → Pivot=0 → [0] [1]                                ║
║                                                               ║
║   Recursively sort right:                                    ║
║   [8,3,10,7] → Pivot=7 → [3] [7] [8,10]                    ║
║                                                               ║
║   Combine:                                                   ║
║   [0, 1, 2, 3, 7, 8, 10] ✓ SORTED!                          ║
║                                                               ║
║  💡 Divide with pivot, recursively both sides               ║
║  💡 O(n log n) on average ⚡ very fast                       ║
║  💡 In practice often the fastest sorter                    ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📊 Complexity

| Case | Time | Space | Why |
|------|------|-------|-----|
| **Best** | O(n log n) | O(log n) | Balanced partitions |
| **Average** | O(n log n) | O(log n) | Random pivots |
| **Worst** | O(n²) | O(n) | Bad pivots (sorted) |

**In practice:** Usually fastest! O(n log n) average.

---

## 🎨 How It Works

### The Algorithm

```
1. Pick a pivot element
2. Partition: smaller left, larger right
3. Recursively sort left partition
4. Recursively sort right partition
5. Done! (pivot is in correct position)
```

### Visual Example

```
Initial: [8, 3, 1, 7, 0, 10, 2]

Step 1: Choose pivot (last element = 2)
[8, 3, 1, 7, 0, 10, 2]
                    ↑ pivot

Step 2: Partition around pivot
- Move smaller than 2 to left
- Move larger than 2 to right

[1, 0, 2, 8, 3, 10, 7]
      ↑
      pivot now in correct position!

Step 3: Recursively sort left [1, 0]
[0, 1] ✓

Step 4: Recursively sort right [8, 3, 10, 7]
... recursive steps ...
[3, 7, 8, 10] ✓

Final: [0, 1, 2, 3, 7, 8, 10] ✓✓✓
```

### Complete Recursion Tree

```
                [8,3,1,7,0,10,2] pivot=2
               /                  \
         [1,0]                    [8,3,10,7]
        /     \                   /         \
      [0]     [1]           [3,7]         [10,8]
       ✓       ✓            /   \          /   \
                         [3]   [7]      [8]  [10]
                          ✓     ✓        ✓    ✓

Result: [0,1,2,3,7,8,10]
```

---

## 💻 Implementation

### Beginner-Friendly Version (Readable, Recursive)

```python
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    left = [x for x in numbers[1:] if x <= pivot]
    right = [x for x in numbers[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

data = [8, 3, 1, 7, 0, 10, 2]
print(quick_sort(data))  # [0, 1, 2, 3, 7, 8, 10]
```

### Basic Version (Lomuto Partition)

```python
def quick_sort(arr, low, high):
    """Sort arr[low..high] using Quick Sort"""
    if low < high:
        # Partition and get pivot position
        pi = partition(arr, low, high)
        
        # Recursively sort before and after partition
        quick_sort(arr, low, pi - 1)   # Left side
        quick_sort(arr, pi + 1, high)  # Right side

def partition(arr, low, high):
    """Partition arr[low..high], return pivot position"""
    pivot = arr[high]  # Choose last element as pivot
    i = low - 1        # Index of smaller element
    
    # Move elements smaller than pivot to left
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return pivot position

# Usage
numbers = [8, 3, 1, 7, 0, 10, 2]
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)  # [0, 1, 2, 3, 7, 8, 10]
```

### Step-by-Step Partition Explanation

```python
def partition_explained(arr, low, high):
    pivot = arr[high]
    print(f"\nPartitioning {arr[low:high+1]}, pivot={pivot}")
    
    i = low - 1  # Position for next small element
    
    for j in range(low, high):
        print(f"  Compare arr[{j}]={arr[j]} with pivot={pivot}", end=" ")
        
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"→ Swap to position {i}")
        else:
            print("→ Skip")
    
    # Place pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"  Final: {arr[low:high+1]}, pivot at index {i+1}")
    
    return i + 1

# Example
arr = [8, 3, 1, 7, 0, 10, 2]
partition_explained(arr, 0, len(arr) - 1)

# Output:
# Partitioning [8, 3, 1, 7, 0, 10, 2], pivot=2
#   Compare arr[0]=8 with pivot=2 → Skip
#   Compare arr[1]=3 with pivot=2 → Skip
#   Compare arr[2]=1 with pivot=2 → Swap to position 0
#   Compare arr[3]=7 with pivot=2 → Skip
#   Compare arr[4]=0 with pivot=2 → Swap to position 1
#   Compare arr[5]=10 with pivot=2 → Skip
#   Final: [1, 0, 2, 8, 3, 10, 7], pivot at index 2
```

### Pythonic Version (Easier to Understand)

```python
def quick_sort_simple(arr):
    """Simple recursive Quick Sort"""
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (middle element)
    pivot = arr[len(arr) // 2]
    
    # Partition into three parts
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort and combine
    return quick_sort_simple(left) + middle + quick_sort_simple(right)

# Usage
numbers = [8, 3, 1, 7, 0, 10, 2]
sorted_arr = quick_sort_simple(numbers)
print(sorted_arr)  # [0, 1, 2, 3, 7, 8, 10]
```

---

## 🔍 Partition Visualization

### Initial State
```
[8, 3, 1, 7, 0, 10, 2]  pivot=2
 ↑                  ↑
 i=-1 (before start) j=0
```

### Pass Through
```
j=0: 8 > 2 → Skip
[8, 3, 1, 7, 0, 10, 2]
 ↑  ↑
 i=-1 j=1

j=1: 3 > 2 → Skip
[8, 3, 1, 7, 0, 10, 2]
 ↑     ↑
 i=-1  j=2

j=2: 1 ≤ 2 → Swap arr[0] and arr[2]
[1, 3, 8, 7, 0, 10, 2]
 ↑     ↑
 i=0   j=3

j=3: 7 > 2 → Skip
[1, 3, 8, 7, 0, 10, 2]
 ↑        ↑
 i=0      j=4

j=4: 0 ≤ 2 → Swap arr[1] and arr[4]
[1, 0, 8, 7, 3, 10, 2]
    ↑        ↑
    i=1      j=5

j=5: 10 > 2 → Skip
[1, 0, 8, 7, 3, 10, 2]
    ↑           ↑
    i=1         j=6 (done)

Final: Place pivot at i+1
[1, 0, 2, 7, 3, 10, 8]
       ↑
    pivot position!
```

---

## ⚡ Choosing the Pivot

### Strategy Comparison

```python
# 1. Last element (simple but risky)
def pivot_last(arr, low, high):
    return high

# 2. First element
def pivot_first(arr, low, high):
    return low

# 3. Middle element (better)
def pivot_middle(arr, low, high):
    return (low + high) // 2

# 4. Random element (best average)
import random
def pivot_random(arr, low, high):
    return random.randint(low, high)

# 5. Median of three (optimal)
def pivot_median_of_three(arr, low, high):
    mid = (low + high) // 2
    pivot_candidates = [
        (arr[low], low),
        (arr[mid], mid),
        (arr[high], high)
    ]
    pivot_candidates.sort()
    return pivot_candidates[1][1]  # Return middle index
```

### Why Pivot Matters

```
Good pivot (middle value):
[1,2,3,4,5,6,7] pivot=4
[1,2,3] | 4 | [5,6,7]  ✓ Balanced → O(n log n)

Bad pivot (extreme value):
[1,2,3,4,5,6,7] pivot=7
[1,2,3,4,5,6] | 7 | []  ✗ Unbalanced → O(n²)
```

---

## 📈 Time Complexity Analysis

### Best/Average Case: O(n log n)

```
Tree depth: log n (balanced splits)
Work per level: n (partitioning)
Total: n × log n = O(n log n)

Example with 8 elements:
Level 0:  [........]  8 elements
         /          \
Level 1: [...]  [....]  8 elements total
        /   \   /    \
Level 2: [.][.] [.][.] 8 elements total

Depth = log₂(8) = 3
Work = 8 per level
Total = 8 × 3 = 24 operations
```

### Worst Case: O(n²)

```
Happens when pivot is always smallest/largest

[1,2,3,4,5] Always choose last (5)
[1,2,3,4] | 5  ← 4 comparisons
[1,2,3] | 4    ← 3 comparisons
[1,2] | 3      ← 2 comparisons
[1] | 2        ← 1 comparison

Total: 4+3+2+1 = 10 = n(n-1)/2 = O(n²)
```

---

## 💡 Practical Examples

### Example 1: Sort Array

```python
def quick_sort_wrapper(arr):
    """Convenient wrapper for quick sort"""
    def quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    quick_sort(arr, 0, len(arr) - 1)
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort_wrapper(numbers))
# [11, 12, 22, 25, 34, 64, 90]
```

### Example 2: Kth Largest Element

```python
def find_kth_largest(arr, k):
    """Find kth largest element using Quick Select"""
    def partition(low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] >= pivot:  # Note: >= for descending
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i
    
    left, right = 0, len(arr) - 1
    k = k - 1  # Convert to 0-indexed
    
    while True:
        pi = partition(left, right)
        if pi == k:
            return arr[pi]
        elif pi < k:
            left = pi + 1
        else:
            right = pi - 1

numbers = [3, 2, 1, 5, 6, 4]
print(find_kth_largest(numbers, 2))  # 5 (2nd largest)
```

---

## ✅ Quick Sort vs Others

| Feature | Quick | Merge | Heap |
|---------|-------|-------|------|
| **Average** | O(n log n) | O(n log n) | O(n log n) |
| **Worst** | O(n²) | O(n log n) | O(n log n) |
| **Space** | O(log n) | O(n) | O(1) |
| **Stable** | ❌ No | ✅ Yes | ❌ No |
| **In-place** | ✅ Yes | ❌ No | ✅ Yes |
| **Practical** | 🥇 Fastest | 🥈 Predictable | 🥉 Good |

**Why Quick Sort is popular:**
- ✅ Fastest in practice (good cache locality)
- ✅ In-place (low memory)
- ✅ Simple to implement
- ❌ But: Not stable, O(n²) worst case

---

## 🎓 Key Takeaways

✅ **Divide and conquer** with partitioning  
✅ **O(n log n)** average, O(n²) worst  
✅ **In-place** sorting (O(log n) stack)  
✅ **Not stable** (equal elements may swap)  
✅ **Fastest** in practice despite worst case  
✅ **Pivot choice** affects performance  

---

## 🚀 Next Steps

1. ✅ Understand partitioning logic
2. ✅ Know complexity trade-offs
3. → Learn [[10_Merge_Sort|Merge Sort]] for comparison
4. → Practice Quick Select variant

---

[[00_Index|← Back to Index]] | [[06_Insertion_Sort|← Previous]] | [[08_Counting_Sort|Next: Counting Sort →]]

*Divide, conquer, and sort! ⚡*
