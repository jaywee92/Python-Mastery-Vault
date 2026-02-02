---
title: Big O Notation - Measuring Algorithmic Complexity
tags: [dsa, big-o, complexity, performance, analysis]
created: 2026-01-28
type: topic
difficulty: beginner
---

# 02. Big O Notation: Measuring Complexity

[[00_Index|← Back to Index]] | [[01_Why_Learn_DSA|← Previous]] | [[03_Arrays|Next: Arrays →]]

> **Learn to analyze and compare algorithm efficiency**

---

## 🎯 What is Big O Notation?

**Big O notation** describes how the runtime or space requirements of an algorithm grow as the input size increases.

**Simple analogy:**
```
🏃 Running a race:
- Distance = Input size (n)
- Time to finish = Algorithm complexity

Big O tells us: "As distance doubles, how much longer does it take?"
```

---

## 📊 Common Complexities

### Visual Comparison

```
Time →
│
│         O(n!)
│         │
│         │    O(2ⁿ)
│         │    │
│         │    │   O(n²)
│         │    │   │
│         │    │   │  O(n log n)
│         │    │   │  │
│         │    │   │  │ O(n)
│         │    │   │  │ │
│         │    │   │  │ │  O(log n)
│         │    │   │  │ │  │
│         │    │   │  │ │  │  O(1)
│         │    │   │  │ │  │  │
└─────────┴────┴───┴──┴─┴──┴──┴──→ Input Size (n)
                                    
Slower ←─────────────────────→ Faster
```

### Complexity Table

| Notation | Name | Example | n=10 | n=100 | n=1000 |
|----------|------|---------|------|-------|--------|
| O(1) | Constant | Array access | 1 | 1 | 1 |
| O(log n) | Logarithmic | Binary search | 3 | 7 | 10 |
| O(n) | Linear | Linear search | 10 | 100 | 1000 |
| O(n log n) | Linearithmic | Merge sort | 30 | 700 | 10000 |
| O(n²) | Quadratic | Bubble sort | 100 | 10000 | 1000000 |
| O(2ⁿ) | Exponential | Fibonacci (naive) | 1024 | 2³⁰ | 2¹⁰⁰⁰ |

---

## 🔍 Understanding Each Complexity

### O(1) - Constant Time ⚡ FASTEST

**Performance:** Same time regardless of input size

```python
def get_first_element(arr):
    return arr[0]  # Always 1 operation

# Examples:
get_first_element([1])           # 1 operation
get_first_element([1,2,3])       # 1 operation
get_first_element([1...million]) # 1 operation
```

**Visual:**
```
Time: ─────────────────
      ↑   ↑   ↑   ↑
      10  100 1K  1M   Input size
```

**Common examples:**
- Array access by index: `arr[5]`
- Hash table lookup: `dict[key]`
- Stack push/pop
- Math operations

---

### O(log n) - Logarithmic Time ⚡⚡ VERY FAST

**Performance:** Doubles input, adds constant time

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Eliminate left half
        else:
            right = mid - 1  # Eliminate right half
    return -1

# For 1 million items: only ~20 comparisons!
```

**Visual - Binary Search:**
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  Target: 7
 └──────────┬──────────┘
            5 (too small)
            
       [6, 7, 8, 9, 10]
        └──┬──┘
          8 (too big)
          
       [6, 7]
        │
        7 (found!)

3 steps for 10 items
~20 steps for 1 million items!
```

**Common examples:**
- Binary search
- Binary trees (balanced)
- Divide and conquer algorithms

---

### O(n) - Linear Time ⚡⚡⚡ GOOD

**Performance:** Doubles input, doubles time

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Must check each element once
```

**Visual:**
```
Time: 
│      ╱
│     ╱
│    ╱
│   ╱
│  ╱
└─────→ Input size

Double input = Double time
```

**Common examples:**
- Linear search
- Loop through array once
- Finding min/max
- Counting elements

---

### O(n log n) - Linearithmic Time ⚡⚡⚡⚡ DECENT

**Performance:** Efficient sorting algorithms

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide - O(log n) levels
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge - O(n) at each level
    return merge(left, right)

# Total: O(log n) levels × O(n) work per level = O(n log n)
```

**Visual - Merge Sort Tree:**
```
         [4,2,7,1,9,3]          Level 0: n operations
         ╱          ╲
    [4,2,7]      [1,9,3]        Level 1: n operations
    ╱    ╲       ╱    ╲
 [4,2]  [7]   [1,9]  [3]        Level 2: n operations
  ╱ ╲    │     ╱ ╲    │
[4] [2] [7]  [1] [9] [3]        Level 3: n operations

log₂(n) levels × n work = O(n log n)
```

**Common examples:**
- Merge sort
- Quick sort (average case)
- Heap sort

---

### O(n²) - Quadratic Time ⚠️ SLOW

**Performance:** Doubles input, quadruples time

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # Outer loop: n times
        for j in range(n - 1):   # Inner loop: n times
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# n × n = n² operations
```

**Visual:**
```
Time: 
│       ╱│
│      ╱ │
│     ╱  │
│    ╱   │
│   ╱    │
│  ╱     │
└────────→ Input size

10 items: 100 operations
100 items: 10,000 operations
1000 items: 1,000,000 operations!
```

**Common examples:**
- Bubble sort
- Selection sort
- Insertion sort
- Nested loops

---

### O(2ⁿ) - Exponential Time 🐌 VERY SLOW

**Performance:** Each additional input doubles time

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Calls itself twice each time!
```

**Visual - Fibonacci Tree:**
```
                fib(5)
              ╱      ╲
          fib(4)     fib(3)
         ╱     ╲     ╱    ╲
     fib(3)  fib(2) fib(2) fib(1)
     ╱   ╲   ╱   ╲  ╱   ╲
  fib(2) fib(1) ... ... ...

fib(5): 15 calls
fib(10): 177 calls
fib(20): 21,891 calls
fib(40): 331,160,281 calls! 💥
```

**Common examples:**
- Naive recursive algorithms
- Generating all subsets
- Brute force solutions

---

## 🎯 How to Calculate Big O

### Step 1: Count Operations

```python
def example(arr):
    x = 5           # O(1)
    y = x + 10      # O(1)
    
    for i in arr:   # O(n)
        print(i)    # O(1) × n times
    
    return x        # O(1)

# Total: O(1) + O(1) + O(n) + O(1) = O(n)
```

### Step 2: Drop Constants

```python
def example(arr):
    for i in arr:           # O(n)
        print(i)
    
    for i in arr:           # O(n)
        print(i * 2)
    
# O(n) + O(n) = O(2n)
# Drop constant: O(n) ✅
```

### Step 3: Keep Dominant Term

```python
def example(arr):
    for i in arr:                  # O(n)
        print(i)
    
    for i in arr:                  # O(n)
        for j in arr:              # O(n)
            print(i, j)

# O(n) + O(n²) = O(n²) ✅
# n² grows faster, dominates
```

---

## 💡 Practical Examples

### Example 1: Array Sum

```python
def sum_array(arr):
    total = 0              # O(1)
    for num in arr:        # O(n)
        total += num       # O(1) × n
    return total           # O(1)

# Analysis: O(1) + O(n) + O(1) = O(n)
```

### Example 2: Find Pairs

```python
def find_pairs(arr):
    for i in range(len(arr)):         # O(n)
        for j in range(i+1, len(arr)): # O(n)
            print(arr[i], arr[j])

# Analysis: O(n) × O(n) = O(n²)
```

### Example 3: Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:           # O(log n) iterations
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

# Analysis: O(log n)
# Halves search space each iteration
```

---

## 📊 Space Complexity

Big O also measures **memory usage**!

### O(1) - Constant Space

```python
def sum_array(arr):
    total = 0  # Only 1 variable
    for num in arr:
        total += num
    return total

# Space: O(1) - fixed number of variables
```

### O(n) - Linear Space

```python
def double_array(arr):
    result = []         # New array
    for num in arr:
        result.append(num * 2)
    return result

# Space: O(n) - new array of size n
```

### O(n²) - Quadratic Space

```python
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix

# Space: O(n²) - n × n matrix
```

---

## 🎯 Best, Average, Worst Case

Some algorithms have different complexities depending on input:

### Example: Quick Sort

```python
Best Case:    O(n log n)  # Perfect pivots
Average Case: O(n log n)  # Random pivots
Worst Case:   O(n²)       # Bad pivots

# Usually we talk about worst case!
```

**Visual:**
```
Best:    [5, 3, 7, 2, 8] → pivot=5 (middle)
         └─┬─┘   └─┬─┘
          2,3     7,8  ✅ Balanced

Worst:   [1, 2, 3, 4, 5] → pivot=1 (end)
         │  └───┬────┘
         1    2,3,4,5  ❌ Unbalanced
```

---

## ✅ Quick Reference

### When analyzing algorithms, ask:

**1. How many loops?**
- 0 loops → O(1)
- 1 loop → O(n)
- Nested loops → O(n²)

**2. Does it divide the problem?**
- Yes, in half each time → O(log n)
- Yes, but processes all → O(n log n)

**3. Does it multiply itself?**
- Recursive with multiple calls → O(2ⁿ) or worse

---

## 💪 Practice Problems

### Problem 1: Analyze This
```python
def mystery(arr):
    if len(arr) == 0:
        return 0
    
    mid = len(arr) // 2
    return arr[mid] + mystery(arr[:mid])
```
> [!success]- Answer
> O(n) - Processes n/2 + n/4 + n/8... = n elements total

### Problem 2: Compare These
```python
# Option A
def find_max_A(arr):
    arr.sort()           # O(n log n)
    return arr[-1]       # O(1)

# Option B  
def find_max_B(arr):
    max_val = arr[0]     # O(1)
    for num in arr:      # O(n)
        if num > max_val:
            max_val = num
    return max_val
```
> [!success]- Answer
> A: O(n log n), B: O(n) - B is faster!

---

## 🎓 Key Takeaways

✅ Big O measures **growth rate**, not exact time  
✅ Drop **constants** and **lower terms**  
✅ Focus on **worst case** usually  
✅ **Space complexity** matters too  
✅ **O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)**

---

## 🚀 Next Steps

Now that you understand Big O:
1. ✅ You can analyze algorithm efficiency
2. ✅ You can compare different solutions
3. → Learn about [[03_Arrays|Arrays]]
4. → See Big O in action with sorting algorithms!

---

[[00_Index|← Back to Index]] | [[01_Why_Learn_DSA|← Previous]] | [[03_Arrays|Next: Arrays →]]

*Master Big O, master algorithm analysis! 📊*
