---
title: Selection Sort
tags: [dsa, sorting, selection-sort]
difficulty: beginner
complexity: O(n²)
---

# 05. Selection Sort

[[00_Index|← Back to Index]] | [[04_Bubble_Sort|← Previous]] | [[06_Insertion_Sort|Next: Insertion Sort →]]

> **Find the smallest, put it first - repeat!**

---

## 🎯 What is Selection Sort?

**Selection Sort** finds the smallest element and moves it to the front, then repeats for the remaining array.

**Think of it like:** Picking cards from smallest to largest from a messy deck.

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════╗
║          🎯 SELECTION SORT - FIND & PLACE SMALLEST            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Array: [64, 25, 12, 22, 11]                                ║
║          ↓                                                   ║
║  Pass 1: Find minimum in entire array                        ║
║  [64, 25, 12, 22, 11]  →  min = 11                          ║
║  [11, 25, 12, 22, 64]  →  Swap!  ✓ Sorted                  ║
║                                                               ║
║  Pass 2: Find minimum in [25, 12, 22, 64]                  ║
║  [11, 25, 12, 22, 64]  →  min = 12                          ║
║  [11, 12, 25, 22, 64]  →  Swap!  ✓✓ Sorted                 ║
║                                                               ║
║  Pass 3: Find minimum in [25, 22, 64]                      ║
║  [11, 12, 25, 22, 64]  →  min = 22                          ║
║  [11, 12, 22, 25, 64]  →  Swap!  ✓✓✓ Sorted               ║
║                                                               ║
║  💡 Find the smallest from "unsorted"                        ║
║  💡 Swap with first unsorted element                        ║
║  💡 Repeat until done!                                       ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 📊 Complexity

| Case | Time | Space | Why |
|------|------|-------|-----|
| **All cases** | O(n²) | O(1) | Always scans entire remaining array |

**Key insight:** No best case - always does n² comparisons!

---

## 🎨 How It Works - Step by Step

### Visual Animation

```
Initial: [64, 25, 12, 22, 11]

Pass 1: Find minimum in entire array (11)
[64, 25, 12, 22, 11]
 └─────────────┘
 Search all: min = 11
[11, 25, 12, 22, 64] ← Swap 64 and 11
 ✓ Sorted part

Pass 2: Find minimum in [25, 12, 22, 64]
[11, 25, 12, 22, 64]
     └────────┘
     min = 12
[11, 12, 25, 22, 64] ← Swap 25 and 12
 ✓✓ Sorted part

Pass 3: Find minimum in [25, 22, 64]
[11, 12, 25, 22, 64]
         └─────┘
         min = 22
[11, 12, 22, 25, 64] ← Swap 25 and 22
 ✓✓✓

Pass 4: Find minimum in [25, 64]
[11, 12, 22, 25, 64]
             └──┘
             min = 25 (already there)
[11, 12, 22, 25, 64] ← No swap needed
 ✓✓✓✓

Done! [11, 12, 22, 25, 64] ✓✓✓✓✓
```

---

## 💻 Implementation

### Beginner-Friendly Version

```python
def selection_sort(numbers):
    nums = numbers[:]
    n = len(nums)

    for start in range(n - 1):
        min_index = start
        for i in range(start + 1, n):
            if nums[i] < nums[min_index]:
                min_index = i
        nums[start], nums[min_index] = nums[min_index], nums[start]

    return nums

data = [64, 25, 12, 22, 11]
print(selection_sort(data))  # [11, 12, 22, 25, 64]
```

### Basic Version with Comments

```python
def selection_sort(arr):
    """
    Sort array using selection sort.
    Time: O(n²), Space: O(1)
    """
    n = len(arr)  # Get array length
    
    # Pass through array n times
    for i in range(n):
        # Assume current position has minimum
        min_idx = i
        
        # Find actual minimum in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Found smaller element
        
        # Swap minimum with current position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage
numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print(numbers)  # [11, 12, 22, 25, 64]
```

### Line-by-Line Explanation

```python
def selection_sort_explained(arr):
    """Selection sort with detailed output"""
    n = len(arr)
    print(f"Starting array: {arr}\n")
    
    for i in range(n):
        print(f"--- Pass {i + 1} ---")
        print(f"Finding minimum in arr[{i}:] = {arr[i:]}")
        
        # Start by assuming current element is minimum
        min_idx = i
        min_value = arr[i]
        
        # Search remaining array for smaller value
        for j in range(i + 1, n):
            print(f"  Compare arr[{j}]={arr[j]} with current min={min_value}", end="")
            
            if arr[j] < arr[min_idx]:
                min_idx = j
                min_value = arr[j]
                print(f" → New min!")
            else:
                print()
        
        # Swap if we found a smaller element
        if min_idx != i:
            print(f"  Swap arr[{i}]={arr[i]} with arr[{min_idx}]={arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            print(f"  Element {arr[i]} already in place")
        
        print(f"  After pass: {arr}")
        print(f"  Sorted: {arr[:i+1]}\n")
    
    return arr

# Example
numbers = [64, 25, 12, 22, 11]
selection_sort_explained(numbers)
```

**Output:**
```
Starting array: [64, 25, 12, 22, 11]

--- Pass 1 ---
Finding minimum in arr[0:] = [64, 25, 12, 22, 11]
  Compare arr[1]=25 with current min=64 → New min!
  Compare arr[2]=12 with current min=25 → New min!
  Compare arr[3]=22 with current min=12
  Compare arr[4]=11 with current min=12 → New min!
  Swap arr[0]=64 with arr[4]=11
  After pass: [11, 25, 12, 22, 64]
  Sorted: [11]

--- Pass 2 ---
Finding minimum in arr[1:] = [25, 12, 22, 64]
  Compare arr[2]=12 with current min=25 → New min!
  Compare arr[3]=22 with current min=12
  Compare arr[4]=64 with current min=12
  Swap arr[1]=25 with arr[2]=12
  After pass: [11, 12, 25, 22, 64]
  Sorted: [11, 12]

...
```

---

## 🔍 Why O(n²)?

### Comparison Count

```
Pass 1: Compare with n-1 elements
Pass 2: Compare with n-2 elements
Pass 3: Compare with n-3 elements
...
Pass n: Compare with 0 elements

Total comparisons:
(n-1) + (n-2) + (n-3) + ... + 1 + 0
= n(n-1)/2
= O(n²)

Example with 5 elements:
4 + 3 + 2 + 1 + 0 = 10 comparisons
5 × 4 / 2 = 10 ✓
```

---

## 💡 Practical Example

### Sort Student Scores

```python
# Student scores (name, score)
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 95),
    ("Eve", 88)
]

def selection_sort_students(students):
    """Sort students by score (lowest to highest)"""
    n = len(students)
    
    for i in range(n):
        # Find student with minimum score
        min_idx = i
        for j in range(i + 1, n):
            if students[j][1] < students[min_idx][1]:  # Compare scores
                min_idx = j
        
        # Swap
        students[i], students[min_idx] = students[min_idx], students[i]
    
    return students

selection_sort_students(students)
for name, score in students:
    print(f"{name}: {score}")

# Output:
# Charlie: 78
# Alice: 85
# Eve: 88
# Bob: 92
# Diana: 95
```

---

## ⚖️ Selection Sort vs Bubble Sort

| Feature | Selection | Bubble |
|---------|-----------|--------|
| **Comparisons** | Always n² | n² (worst), n (best) |
| **Swaps** | Only n | Up to n² |
| **Best case** | O(n²) | O(n) |
| **Stable** | ❌ No | ✅ Yes |
| **When to use** | Minimizing swaps | Already sorted data |

**Key difference:** Selection sort makes fewer swaps (exactly n-1)!

---

## ✅ When to Use Selection Sort

### ✅ Good For:
- **Minimizing swaps** - Only n swaps maximum
- **Small arrays** - Simple to implement
- **Educational purposes** - Easy to understand
- **Memory writes are expensive** - Fewer writes than bubble

### ❌ Avoid For:
- **Large arrays** - Too slow (O(n²))
- **Nearly sorted** - Doesn't take advantage
- **Need stability** - May change order of equal elements
- **Production code** - Better algorithms exist

---

## 🎓 Key Takeaways

✅ **Always O(n²)** - no best case  
✅ **Minimum swaps** - exactly n-1 swaps  
✅ **Not stable** - equal elements may swap  
✅ **In-place** - O(1) extra space  
✅ **Simple** - easy to understand and code  
✅ **Better than bubble** - fewer swaps  

---

## 🚀 Next Steps

1. ✅ Understand minimum-finding pattern
2. ✅ Compare with bubble sort
3. → Learn [[06_Insertion_Sort|Insertion Sort]]
4. → See how it builds sorted portion

---

[[00_Index|← Back to Index]] | [[04_Bubble_Sort|← Previous]] | [[06_Insertion_Sort|Next: Insertion Sort →]]

*Select the smallest, build the sorted! 🎯*
