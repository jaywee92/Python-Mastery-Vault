---
title: Insertion Sort
tags: [dsa, sorting, insertion-sort, beginner-friendly]
difficulty: beginner
complexity: O(n²)
---

# 06. Insertion Sort

[[00_Index|← Back to Index]] | [[05_Selection_Sort|← Previous]] | [[07_Quick_Sort|Next: Quick Sort →]]

> **Build sorted array one element at a time - like sorting playing cards in your hand**

---

## 🎯 What is Insertion Sort?

**Insertion Sort** builds a sorted array by picking elements one by one and inserting them into their correct position.

**Real-life analogy:**
```
Imagine sorting playing cards in your hand:
1. Pick up first card → already "sorted"
2. Pick up second card → insert before/after first card
3. Pick up third card → insert in correct spot among first two
4. Repeat until all cards are sorted!
```

---

## 📊 Complexity

| Case | Time | Space | Why |
|------|------|-------|-----|
| **Best** | O(n) | O(1) | Already sorted - just scan once |
| **Average** | O(n²) | O(1) | Random order - many shifts |
| **Worst** | O(n²) | O(1) | Reverse sorted - maximum shifts |

**Key advantage:** O(n) for nearly sorted data!

---

## 🎨 How It Works - Playing Cards Example

### Visual Step-by-Step

```
Initial hand: [5, 2, 4, 6, 1, 3]
Goal: Sort them in ascending order

Step 1: First card is already "sorted"
Sorted: [5] | Unsorted: [2, 4, 6, 1, 3]
        ↑
        Start here

Step 2: Pick 2, insert before 5
Pick: 2
Compare: 2 < 5? Yes → Insert before 5
Sorted: [2, 5] | Unsorted: [4, 6, 1, 3]
        ↑  ↑
        Inserted!

Step 3: Pick 4, insert between 2 and 5
Pick: 4
Compare: 4 < 5? Yes, move 5 right
Compare: 4 < 2? No, insert here
Sorted: [2, 4, 5] | Unsorted: [6, 1, 3]
           ↑
           Inserted!

Step 4: Pick 6, already in correct spot
Pick: 6
Compare: 6 < 5? No → Insert at end
Sorted: [2, 4, 5, 6] | Unsorted: [1, 3]
                 ↑
                 Inserted!

Step 5: Pick 1, insert at beginning
Pick: 1
Compare: 1 < 6? Yes, move 6 right
Compare: 1 < 5? Yes, move 5 right
Compare: 1 < 4? Yes, move 4 right
Compare: 1 < 2? Yes, move 2 right
Insert at start
Sorted: [1, 2, 4, 5, 6] | Unsorted: [3]
        ↑
        Inserted!

Step 6: Pick 3, insert between 2 and 4
Pick: 3
Compare: 3 < 6? Yes, move right
Compare: 3 < 5? Yes, move right
Compare: 3 < 4? Yes, move right
Compare: 3 < 2? No, insert here
Sorted: [1, 2, 3, 4, 5, 6] ✓
              ↑
              Inserted!
```

---

## 💻 Implementation

### Beginner-Friendly Version

```python
def insertion_sort(numbers):
    nums = numbers[:]

    for i in range(1, len(nums)):
        current = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = current

    return nums

data = [5, 2, 4, 6, 1, 3]
print(insertion_sort(data))  # [1, 2, 3, 4, 5, 6]
```

### Basic Version with Detailed Comments

```python
def insertion_sort(arr):
    """
    Sort array using insertion sort.
    Like sorting playing cards in your hand!
    
    Time: O(n²) worst case, O(n) best case
    Space: O(1) - in-place sorting
    """
    # Start from second element (first is already "sorted")
    for i in range(1, len(arr)):
        # This is the card we're inserting
        key = arr[i]
        
        # Position to check (start from just before current)
        j = i - 1
        
        # Move elements greater than key one position right
        # This makes space for our key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift right
            j -= 1  # Check previous element
        
        # Insert key in the correct position
        arr[j + 1] = key
    
    return arr

# Example usage
numbers = [12, 11, 13, 5, 6]
print("Before:", numbers)
insertion_sort(numbers)
print("After:", numbers)  # [5, 6, 11, 12, 13]
```

### Step-by-Step Walkthrough with Output

```python
def insertion_sort_explained(arr):
    """Insertion sort with detailed output for learning"""
    print(f"Starting array: {arr}")
    print("=" * 50)
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        print(f"\n--- Step {i}: Inserting {key} ---")
        print(f"Sorted part: {arr[:i]}")
        print(f"Current key to insert: {key}")
        print(f"Unsorted part: {arr[i+1:]}")
        
        # Track movements
        moves = 0
        
        # Find correct position for key
        while j >= 0 and arr[j] > key:
            print(f"  {arr[j]} > {key}: Move {arr[j]} right")
            arr[j + 1] = arr[j]
            j -= 1
            moves += 1
        
        # Insert key
        arr[j + 1] = key
        
        if moves == 0:
            print(f"  {key} already in correct position!")
        else:
            print(f"  Insert {key} at position {j + 1}")
        
        print(f"Array now: {arr}")
        print(f"Sorted: {arr[:i+1]} | Remaining: {arr[i+1:]}")
    
    print("\n" + "=" * 50)
    print(f"Final sorted array: {arr}")
    return arr

# Example
numbers = [12, 11, 13, 5, 6]
insertion_sort_explained(numbers)
```

**Output:**
```
Starting array: [12, 11, 13, 5, 6]
==================================================

--- Step 1: Inserting 11 ---
Sorted part: [12]
Current key to insert: 11
Unsorted part: [13, 5, 6]
  12 > 11: Move 12 right
  Insert 11 at position 0
Array now: [11, 12, 13, 5, 6]
Sorted: [11, 12] | Remaining: [13, 5, 6]

--- Step 2: Inserting 13 ---
Sorted part: [11, 12]
Current key to insert: 13
Unsorted part: [5, 6]
  13 already in correct position!
Array now: [11, 12, 13, 5, 6]
Sorted: [11, 12, 13] | Remaining: [5, 6]

--- Step 3: Inserting 5 ---
Sorted part: [11, 12, 13]
Current key to insert: 5
Unsorted part: [6]
  13 > 5: Move 13 right
  12 > 5: Move 12 right
  11 > 5: Move 11 right
  Insert 5 at position 0
Array now: [5, 11, 12, 13, 6]
Sorted: [5, 11, 12, 13] | Remaining: [6]

--- Step 4: Inserting 6 ---
Sorted part: [5, 11, 12, 13]
Current key to insert: 6
Unsorted part: []
  13 > 6: Move 13 right
  12 > 6: Move 12 right
  11 > 6: Move 11 right
  Insert 6 at position 1
Array now: [5, 6, 11, 12, 13]
Sorted: [5, 6, 11, 12, 13] | Remaining: []

==================================================
Final sorted array: [5, 6, 11, 12, 13]
```

---

## 🔍 Why Different Complexities?

### Best Case: O(n) - Already Sorted

```python
arr = [1, 2, 3, 4, 5]  # Already sorted

# Each element just needs 1 comparison
# No shifts needed!
# Total: n comparisons = O(n)
```

### Worst Case: O(n²) - Reverse Sorted

```python
arr = [5, 4, 3, 2, 1]  # Reverse sorted

# Element at position i needs i shifts
# Position 1: 1 shift
# Position 2: 2 shifts
# Position 3: 3 shifts
# Position 4: 4 shifts
# Total: 1+2+3+4 = 10 = n(n-1)/2 = O(n²)
```

---

## 💡 Practical Examples

### Example 1: Sort Student Names

```python
students = ["Charlie", "Alice", "David", "Bob"]

print("Unsorted:", students)
insertion_sort(students)
print("Sorted:", students)
# ['Alice', 'Bob', 'Charlie', 'David']
```

### Example 2: Sort by Last Name

```python
people = [
    ("John", "Smith"),
    ("Alice", "Johnson"),
    ("Bob", "Anderson"),
    ("Charlie", "Brown")
]

def insertion_sort_by_last_name(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Compare last names (index 1)
        while j >= 0 and arr[j][1] > key[1]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    return arr

insertion_sort_by_last_name(people)
for first, last in people:
    print(f"{first} {last}")

# Output:
# Bob Anderson
# Charlie Brown
# Alice Johnson
# John Smith
```

### Example 3: Nearly Sorted Data (Fast!)

```python
# Data that's almost sorted
nearly_sorted = [1, 2, 3, 5, 4, 6, 7, 8]

print("Nearly sorted:", nearly_sorted)
insertion_sort(nearly_sorted)
print("Sorted:", nearly_sorted)

# Only 1 element (4) needs to move!
# Very fast: O(n) time!
```

---

## 🎯 When to Use Insertion Sort

### ✅ Perfect For:

**1. Small arrays (< 10-50 elements)**
```python
small_list = [5, 2, 8, 1, 9]
insertion_sort(small_list)  # Fast enough!
```

**2. Nearly sorted data**
```python
nearly_sorted = [1, 2, 3, 5, 4, 6, 7]
insertion_sort(nearly_sorted)  # O(n) - very fast!
```

**3. Online sorting (data arrives gradually)**
```python
sorted_so_far = [1, 3, 5, 7]
new_item = 4
# Insert 4 into correct position efficiently!
```

**4. When stability is needed**
```python
# Equal elements keep their original order
arr = [(1, 'a'), (1, 'b'), (2, 'c')]
insertion_sort(arr)
# (1, 'a') stays before (1, 'b') ✓
```

### ❌ Avoid For:

- Large arrays (> 100 elements) - too slow
- Completely random data - O(n²) hurts
- When you need guaranteed O(n log n) - use merge/quick sort

---

## ⚖️ Comparison with Other Sorts

| Feature | Insertion | Bubble | Selection |
|---------|-----------|--------|-----------|
| **Best case** | O(n) ✅ | O(n) | O(n²) |
| **Average** | O(n²) | O(n²) | O(n²) |
| **Worst** | O(n²) | O(n²) | O(n²) |
| **Stable** | ✅ Yes | ✅ Yes | ❌ No |
| **Nearly sorted** | ✅ Fast | ⚠️ Slow | ⚠️ Slow |
| **Online** | ✅ Yes | ❌ No | ❌ No |
| **Simple** | ⚠️ Medium | ✅ Easy | ✅ Easy |

**Why insertion beats bubble/selection:**
- ✅ Adaptive (fast on nearly sorted data)
- ✅ Online (can sort as data arrives)
- ✅ Stable (preserves order of equal elements)
- ✅ Actually used in practice (for small arrays)

---

## 🔧 Optimization: Binary Insertion Sort

```python
def binary_insertion_sort(arr):
    """
    Use binary search to find insertion position.
    Reduces comparisons but still O(n²) due to shifts.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Binary search for correct position
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        
        # Shift elements and insert
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = key
    
    return arr

# Still O(n²) due to shifts, but fewer comparisons!
```

---

## 🎓 Key Takeaways

✅ **Like sorting playing cards** - easy to understand!  
✅ **Adaptive: O(n)** for nearly sorted data  
✅ **Stable** - preserves order of equal elements  
✅ **Online** - can sort as data arrives  
✅ **In-place** - O(1) extra space  
✅ **Best simple sort** for small/nearly sorted arrays  
✅ **Used in practice** - hybrid sorts use it for small subarrays

**Remember:** Good for small arrays, great for nearly sorted data!

---

## 🚀 Next Steps

1. ✅ Understand the "insert into sorted part" pattern
2. ✅ Practice on nearly sorted data
3. → Learn [[07_Quick_Sort|Quick Sort]] for large arrays
4. → See how real sorting libraries combine algorithms

---

[[00_Index|← Back to Index]] | [[05_Selection_Sort|← Previous]] | [[07_Quick_Sort|Next: Quick Sort →]]

*Insert and sort like a card player! 🃏*
---

## 🎨 Visualization (Optional)

```python
import sys
from pathlib import Path

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

nums = [5, 2, 8, 1]
draw_sort(nums, title="Before Sorting")
```
