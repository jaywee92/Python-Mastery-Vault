---
title: Counting Sort Algorithm
tags: [dsa, sorting, counting-sort, non-comparison, beginner-friendly]
created: 2026-01-28
difficulty: intermediate
complexity: O(n+k)
---

# 08. Counting Sort

[[00_Index|← Back to Index]] | [[07_Quick_Sort|← Previous]] | [[09_Radix_Sort|Next: Radix Sort →]]

> **Count, don't compare! A blazing-fast sort for integers with limited range**

---

## 🎨 Visual Memory Aid

```
    ╔═══════════════════════════════════════════════════════════════╗
    ║               🧮 COUNTING SORT - THE TALLY KEEPER             ║
    ╠═══════════════════════════════════════════════════════════════╣
    ║                                                               ║
    ║   Input: [4, 2, 2, 8, 3, 3, 1]                                ║
    ║                                                               ║
    ║   Step 1: Count each number (like tally marks!)               ║
    ║                                                               ║
    ║   Number:  1   2   3   4   5   6   7   8                      ║
    ║           ┌───┬───┬───┬───┬───┬───┬───┬───┐                   ║
    ║   Count:  │ 1 │ 2 │ 2 │ 1 │ 0 │ 0 │ 0 │ 1 │                   ║
    ║           └───┴───┴───┴───┴───┴───┴───┴───┘                   ║
    ║            │   │││ │││ │                   │                   ║
    ║            ▼   ▼▼▼ ▼▼▼ ▼                   ▼                   ║
    ║                                                               ║
    ║   Step 2: Rebuild array from counts                           ║
    ║                                                               ║
    ║   Output: [1, 2, 2, 3, 3, 4, 8] ✓                             ║
    ║                                                               ║
    ║   💡 No comparisons needed! Just counting!                    ║
    ╚═══════════════════════════════════════════════════════════════╝
```

---

## 🎯 What is Counting Sort?

**Counting Sort** is a non-comparison sorting algorithm that counts how many times each value appears, then uses those counts to place elements in the correct position.

**Real-life analogy:**
```
Imagine sorting a deck of numbered cards (1-10):

1. Create 10 boxes labeled 1 through 10
2. Go through cards, put each in its matching box
3. Empty boxes in order → Sorted cards!

No need to compare cards - just count and place!
```

**Key Insight:** Instead of asking "Is A > B?", we ask "How many of each number?"

---

## 📊 Complexity

| Case | Time | Space | Explanation |
|------|------|-------|-------------|
| **All** | O(n + k) | O(k) | n = elements, k = value range |
| **Best** | O(n + k) | O(k) | Same - always counts everything |
| **Worst** | O(n + k) | O(k) | Same - predictable performance |

**When k ≤ n:** Effectively O(n) - Linear time! 🚀

---

## 🎨 How It Works - Step by Step

### The Counting Process

```
Input Array: [4, 2, 2, 8, 3, 3, 1]
Range: 1 to 8 (k = 8)

╔═══════════════════════════════════════════════════════════════════╗
║  STEP 1: Create Count Array (size = max value + 1)                ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Index:   0   1   2   3   4   5   6   7   8                       ║
║         ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐                     ║
║  Count: │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │  (all zeros)       ║
║         └───┴───┴───┴───┴───┴───┴───┴───┴───┘                     ║
╚═══════════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════╗
║  STEP 2: Count Each Element                                       ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Process: [4, 2, 2, 8, 3, 3, 1]                                   ║
║            ↓                                                      ║
║  See 4 → count[4]++                                               ║
║                                                                   ║
║  Index:   0   1   2   3   4   5   6   7   8                       ║
║         ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐                     ║
║  After: │ 0 │ 1 │ 2 │ 2 │ 1 │ 0 │ 0 │ 0 │ 1 │                     ║
║         └───┴───┴───┴───┴───┴───┴───┴───┴───┘                     ║
║              ↑   ↑   ↑   ↑               ↑                        ║
║             1×  2×  2×  1×              1×                        ║
║             one two three four         eight                      ║
╚═══════════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════╗
║  STEP 3: Rebuild Sorted Array                                     ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  Read counts in order:                                            ║
║  • count[1] = 1 → output one "1"                                  ║
║  • count[2] = 2 → output two "2"s                                 ║
║  • count[3] = 2 → output two "3"s                                 ║
║  • count[4] = 1 → output one "4"                                  ║
║  • count[5-7] = 0 → skip                                          ║
║  • count[8] = 1 → output one "8"                                  ║
║                                                                   ║
║  Result: [1, 2, 2, 3, 3, 4, 8] ✅                                  ║
╚═══════════════════════════════════════════════════════════════════╝
```

### Visual Animation

```
Input: [4, 2, 2, 8, 3, 3, 1]

Counting Phase:
┌─────────────────────────────────────────────────────┐
│ Element │ Action           │ Count Array            │
├─────────┼──────────────────┼────────────────────────┤
│    4    │ count[4]++       │ [0,0,0,0,1,0,0,0,0]   │
│    2    │ count[2]++       │ [0,0,1,0,1,0,0,0,0]   │
│    2    │ count[2]++       │ [0,0,2,0,1,0,0,0,0]   │
│    8    │ count[8]++       │ [0,0,2,0,1,0,0,0,1]   │
│    3    │ count[3]++       │ [0,0,2,1,1,0,0,0,1]   │
│    3    │ count[3]++       │ [0,0,2,2,1,0,0,0,1]   │
│    1    │ count[1]++       │ [0,1,2,2,1,0,0,0,1]   │
└─────────┴──────────────────┴────────────────────────┘

Building Phase:
┌─────────────────────────────────────────────────────┐
│ Index │ Count │ Output so far                       │
├───────┼───────┼─────────────────────────────────────┤
│   1   │   1   │ [1]                                 │
│   2   │   2   │ [1, 2, 2]                           │
│   3   │   2   │ [1, 2, 2, 3, 3]                     │
│   4   │   1   │ [1, 2, 2, 3, 3, 4]                  │
│  5-7  │   0   │ [1, 2, 2, 3, 3, 4]  (skip zeros)   │
│   8   │   1   │ [1, 2, 2, 3, 3, 4, 8] ✅            │
└───────┴───────┴─────────────────────────────────────┘
```

---

## 💻 Implementation

### Beginner-Friendly Version

```python
def counting_sort(numbers):
    """
    Sort numbers using counting sort.
    Works for non-negative integers.

    Think of it like sorting mail into numbered mailboxes!
    """
    if not numbers:
        return numbers

    # Step 1: Find the range of values
    max_val = max(numbers)

    # Step 2: Create count array (like mailboxes)
    count = [0] * (max_val + 1)

    # Step 3: Count each number
    for num in numbers:
        count[num] += 1

    # Step 4: Rebuild sorted array
    result = []
    for i in range(len(count)):
        # Add 'count[i]' copies of number 'i'
        result.extend([i] * count[i])

    return result

# Example
numbers = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(numbers))  # [1, 2, 2, 3, 3, 4, 8]
```

### Version with Negative Numbers

```python
def counting_sort_with_negatives(arr):
    """
    Counting sort that handles negative numbers too!

    Trick: Shift all values to be non-negative,
    then shift back after sorting.
    """
    if not arr:
        return arr

    # Find range
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Create count array for shifted values
    count = [0] * range_size

    # Count occurrences (shift by min_val)
    for num in arr:
        count[num - min_val] += 1

    # Rebuild (shift back)
    result = []
    for i in range(range_size):
        # i + min_val gives original value
        result.extend([i + min_val] * count[i])

    return result

# Example with negative numbers
numbers = [4, -2, 2, 0, -3, 3, 1]
print(counting_sort_with_negatives(numbers))
# [-3, -2, 0, 1, 2, 3, 4]
```

### Step-by-Step Walkthrough

```python
def counting_sort_explained(arr):
    """Counting sort with detailed output for learning"""
    print(f"🎯 Input array: {arr}")
    print("=" * 60)

    if not arr:
        return arr

    # Step 1: Find range
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    print(f"\n📊 Step 1: Find the range")
    print(f"   Minimum value: {min_val}")
    print(f"   Maximum value: {max_val}")
    print(f"   Range size: {range_size}")

    # Step 2: Create count array
    count = [0] * range_size
    print(f"\n📦 Step 2: Create count array")
    print(f"   Initial counts: {count}")

    # Step 3: Count each element
    print(f"\n🧮 Step 3: Count each element")
    for num in arr:
        index = num - min_val
        count[index] += 1
        print(f"   Found {num} → count[{index}] = {count[index]}")

    print(f"\n   Final counts: {count}")
    print(f"   (Index 0 = value {min_val}, Index {range_size-1} = value {max_val})")

    # Step 4: Rebuild array
    print(f"\n🔨 Step 4: Rebuild sorted array")
    result = []
    for i in range(range_size):
        value = i + min_val
        if count[i] > 0:
            print(f"   count[{i}] = {count[i]} → Add {count[i]}x '{value}'")
            result.extend([value] * count[i])

    print(f"\n✅ Sorted array: {result}")
    return result

# Test it
numbers = [4, 2, 2, 8, 3, 3, 1]
counting_sort_explained(numbers)
```

**Output:**
```
🎯 Input array: [4, 2, 2, 8, 3, 3, 1]
============================================================

📊 Step 1: Find the range
   Minimum value: 1
   Maximum value: 8
   Range size: 8

📦 Step 2: Create count array
   Initial counts: [0, 0, 0, 0, 0, 0, 0, 0]

🧮 Step 3: Count each element
   Found 4 → count[3] = 1
   Found 2 → count[1] = 1
   Found 2 → count[1] = 2
   Found 8 → count[7] = 1
   Found 3 → count[2] = 1
   Found 3 → count[2] = 2
   Found 1 → count[0] = 1

   Final counts: [1, 2, 2, 1, 0, 0, 0, 1]
   (Index 0 = value 1, Index 7 = value 8)

🔨 Step 4: Rebuild sorted array
   count[0] = 1 → Add 1x '1'
   count[1] = 2 → Add 2x '2'
   count[2] = 2 → Add 2x '3'
   count[3] = 1 → Add 1x '4'
   count[7] = 1 → Add 1x '8'

✅ Sorted array: [1, 2, 2, 3, 3, 4, 8]
```

### Stable Version (Preserves Original Order)

```python
def counting_sort_stable(arr):
    """
    Stable counting sort - equal elements keep original order.
    Important for sorting objects or as subroutine in Radix Sort.
    """
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # Convert to cumulative count (positions)
    # count[i] now tells us "how many elements are ≤ i"
    for i in range(1, range_size):
        count[i] += count[i - 1]

    # Build output array (traverse input backwards for stability)
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        index = arr[i] - min_val
        count[index] -= 1
        output[count[index]] = arr[i]

    return output

# This version is stable!
numbers = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort_stable(numbers))  # [1, 2, 2, 3, 3, 4, 8]
```

---

## 🔍 Complexity Analysis

### Time Complexity Breakdown

```python
def counting_sort(arr):
    n = len(arr)

    max_val = max(arr)              # O(n) - scan once
    min_val = min(arr)              # O(n) - scan once
    k = max_val - min_val + 1       # O(1)

    count = [0] * k                 # O(k) - create array

    for num in arr:                 # O(n) - count elements
        count[num - min_val] += 1

    result = []
    for i in range(k):              # O(k) - iterate counts
        result.extend([i + min_val] * count[i])  # O(n) total

    return result

# Total: O(n) + O(k) + O(n) + O(k) + O(n) = O(n + k)
```

### When is Counting Sort Fast?

```
Scenario 1: k ≤ n (range smaller than array size)
┌────────────────────────────────────────────────┐
│ Array: [5,2,8,1,9,3,7,4,6,0] (n=10, k=10)     │
│ Time: O(10 + 10) = O(20) ≈ O(n) 🚀           │
│ Very fast! Linear time!                       │
└────────────────────────────────────────────────┘

Scenario 2: k >> n (range much larger than array)
┌────────────────────────────────────────────────┐
│ Array: [1, 1000000] (n=2, k=1000000)          │
│ Time: O(2 + 1000000) = O(1000000) 😰          │
│ Very slow! Don't use counting sort!           │
└────────────────────────────────────────────────┘
```

### Space Complexity

```
Space needed: O(k) for count array

Example 1: Numbers 1-100 → count[101] → 101 integers → ~400 bytes ✅
Example 2: Numbers 1-1000000 → count[1000001] → ~4 MB ⚠️
Example 3: Numbers 1-1000000000 → count[1B+] → ~4 GB ❌
```

---

## 💡 Practical Examples

### Example 1: Sort Exam Scores

```python
# Exam scores range from 0 to 100
scores = [85, 92, 78, 85, 90, 78, 92, 85, 100, 65]

print("Unsorted scores:", scores)
sorted_scores = counting_sort(scores)
print("Sorted scores:", sorted_scores)
# [65, 78, 78, 85, 85, 85, 90, 92, 92, 100]
```

### Example 2: Sort Ages

```python
# Ages typically range 0-120
ages = [25, 32, 18, 25, 45, 32, 18, 60, 25]

sorted_ages = counting_sort(ages)
print(sorted_ages)  # [18, 18, 25, 25, 25, 32, 32, 45, 60]
```

### Example 3: Character Frequency (for strings)

```python
def sort_string_by_chars(s):
    """Sort characters in a string using counting sort"""
    # ASCII values 0-127
    count = [0] * 128

    # Count each character
    for char in s:
        count[ord(char)] += 1

    # Rebuild string
    result = []
    for i in range(128):
        if count[i] > 0:
            result.append(chr(i) * count[i])

    return ''.join(result)

text = "programming"
print(sort_string_by_chars(text))  # "aggimmnoprr"
```

---

## 🎯 When to Use Counting Sort

### ✅ Perfect For:

**1. Integer data with small range**
```python
# Sorting playing card values (1-13)
cards = [7, 2, 10, 13, 1, 5, 8, 2, 7]
# k = 13, very efficient!
```

**2. Known, limited value range**
```python
# Sorting months (1-12)
months = [5, 12, 1, 7, 3, 12, 5, 1]
# k = 12, perfect!
```

**3. Many duplicate values**
```python
# Survey ratings (1-5 scale)
ratings = [3, 4, 5, 3, 2, 4, 4, 3, 5, 3, 4, 3]
# Many duplicates, counting sort shines!
```

**4. As subroutine for Radix Sort**
```python
# Radix sort uses counting sort on each digit
# Digit range is always 0-9, very efficient!
```

### ❌ Avoid When:

- **Large range of values** (k >> n)
- **Floating-point numbers** (infinite possible values)
- **Strings** (unless character-by-character)
- **Memory is limited** (need O(k) extra space)

---

## ⚖️ Comparison with Other Sorts

| Feature | Counting | Quick | Merge | Bubble |
|---------|----------|-------|-------|--------|
| **Best Time** | O(n+k) | O(n log n) | O(n log n) | O(n) |
| **Average** | O(n+k) | O(n log n) | O(n log n) | O(n²) |
| **Worst** | O(n+k) | O(n²) | O(n log n) | O(n²) |
| **Space** | O(k) | O(log n) | O(n) | O(1) |
| **Stable** | ✅ Yes* | ❌ No | ✅ Yes | ✅ Yes |
| **Comparison-based** | ❌ No | ✅ Yes | ✅ Yes | ✅ Yes |

*Stable version required

**Key advantage:** Beats O(n log n) when k is small!

---

## ⚠️ Common Mistakes

### Mistake 1: Forgetting Range Check

```python
# ❌ Bad - doesn't handle empty array
def bad_counting_sort(arr):
    max_val = max(arr)  # Error if arr is empty!
    ...

# ✅ Good - check first
def good_counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    ...
```

### Mistake 2: Not Handling Negative Numbers

```python
# ❌ Bad - negative index error
arr = [3, -1, 2]
count[arr[1]]  # count[-1] - wrong!

# ✅ Good - shift by minimum
min_val = min(arr)
count[arr[1] - min_val]  # count[-1 - (-1)] = count[0] ✓
```

### Mistake 3: Using for Large Ranges

```python
# ❌ Bad - wastes memory
arr = [1, 1000000]  # Only 2 elements but huge count array!

# ✅ Better - use comparison sort instead
sorted(arr)  # O(n log n) but O(1) extra space
```

---

## 🎓 Key Takeaways

```
╔═══════════════════════════════════════════════════════════════════╗
║                    COUNTING SORT SUMMARY                          ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  ✅ Time: O(n + k) - Linear when k ≤ n                           ║
║  ✅ Space: O(k) - Extra space for counts                          ║
║  ✅ NOT comparison-based - counts instead of compares             ║
║  ✅ Stable (with proper implementation)                           ║
║  ✅ Best for: Small integer ranges, many duplicates               ║
║                                                                   ║
║  ❌ Avoid: Large ranges, floats, strings                          ║
║                                                                   ║
║  💡 Remember: "Count and place, don't compare!"                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

---

## 🚀 Next Steps

1. ✅ Understand counting without comparing
2. ✅ Know when O(n+k) beats O(n log n)
3. → Learn [[09_Radix_Sort|Radix Sort]] which uses Counting Sort
4. → Try sorting exam scores or survey data

---

[[00_Index|← Back to Index]] | [[07_Quick_Sort|← Previous]] | [[09_Radix_Sort|Next: Radix Sort →]]

*Count your way to a sorted array! 🧮*
