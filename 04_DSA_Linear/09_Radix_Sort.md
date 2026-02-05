---
title: Radix Sort Algorithm
tags: [dsa, sorting, radix-sort, non-comparison, beginner-friendly]
created: 2026-01-28
difficulty: intermediate
complexity: O(d*(n+k))
---

# 09. Radix Sort

[[00_Index|← Back to Index]] | [[08_Counting_Sort|← Previous]] | [[10_Merge_Sort|Next: Merge Sort →]]

> **Sort by digits - from least to most significant, like sorting library cards!**

---

## 🎨 Visual Memory Aid

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    🔢 RADIX SORT - THE DIGIT SORTER                       ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   Input: [170, 45, 75, 90, 802, 24, 2, 66]                               ║
║                                                                           ║
║   Sort by each digit position (right to left):                            ║
║                                                                           ║
║   ┌─────────────────────────────────────────────────────────────────┐     ║
║   │  PASS 1: Sort by ONES place (rightmost digit)                   │     ║
║   │                                                                 │     ║
║   │  17[0]  4[5]  7[5]  9[0]  80[2]  2[4]  [2]  6[6]               │     ║
║   │     ↓     ↓     ↓     ↓      ↓     ↓    ↓     ↓                 │     ║
║   │                                                                 │     ║
║   │  Buckets:  0    1    2    3    4    5    6    7    8    9       │     ║
║   │          ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐             │     ║
║   │          │170│   │802│   │ 24│ 45│ 66│   │   │   │             │     ║
║   │          │ 90│   │  2│   │   │ 75│   │   │   │   │             │     ║
║   │          └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘             │     ║
║   │                                                                 │     ║
║   │  Result: [170, 90, 802, 2, 24, 45, 75, 66]                      │     ║
║   └─────────────────────────────────────────────────────────────────┘     ║
║                                                                           ║
║   ┌─────────────────────────────────────────────────────────────────┐     ║
║   │  PASS 2: Sort by TENS place                                     │     ║
║   │                                                                 │     ║
║   │  1[7]0  [9]0  8[0]2  [0]2  [2]4  [4]5  [7]5  [6]6              │     ║
║   │                                                                 │     ║
║   │  Result: [802, 2, 24, 45, 66, 170, 75, 90]                      │     ║
║   └─────────────────────────────────────────────────────────────────┘     ║
║                                                                           ║
║   ┌─────────────────────────────────────────────────────────────────┐     ║
║   │  PASS 3: Sort by HUNDREDS place                                 │     ║
║   │                                                                 │     ║
║   │  [8]02  [0]02  [0]24  [0]45  [0]66  [1]70  [0]75  [0]90        │     ║
║   │                                                                 │     ║
║   │  Result: [2, 24, 45, 66, 75, 90, 170, 802] ✅ SORTED!           │     ║
║   └─────────────────────────────────────────────────────────────────┘     ║
║                                                                           ║
║   💡 Key: Sort digit by digit, from right to left!                        ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## 🎯 What is Radix Sort?

**Radix Sort** sorts numbers by processing individual digits. It sorts from the least significant digit (rightmost) to the most significant digit (leftmost), using a stable sort (like Counting Sort) for each digit.

**Real-life analogy:**
```
Imagine sorting library cards by call number (e.g., 621.3, 500.1, 621.8):

1. First, sort by last digit:     .1, .3, .8
2. Then by second digit:          00, 21, 21
3. Finally by first digit:        5, 6, 6

Result: 500.1, 621.3, 621.8 - Sorted!

This is exactly how Radix Sort works!
```

**Key Insight:** If we sort stably by each digit position (right to left), the array becomes fully sorted!

---

## 📊 Complexity

| Metric | Value | Explanation |
|--------|-------|-------------|
| **Time** | O(d × (n + k)) | d = digits, n = elements, k = base |
| **Space** | O(n + k) | For counting sort arrays |
| **Best/Worst** | Same | Always processes all digits |

**For decimal numbers:** k = 10 (digits 0-9), so effectively **O(d × n)** - Linear!

---

## 🎨 How It Works - Step by Step

### Complete Walkthrough

```
Input: [170, 45, 75, 90, 802, 24, 2, 66]

Maximum value: 802 (3 digits → 3 passes needed)

╔═══════════════════════════════════════════════════════════════════════════╗
║                           PASS 1: ONES PLACE                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   Extract ones digit from each number:                                    ║
║                                                                           ║
║   Number:  170   45   75   90   802   24    2   66                       ║
║   Digit:     0    5    5    0     2    4    2    6                       ║
║                                                                           ║
║   Place in buckets (0-9):                                                 ║
║                                                                           ║
║   Bucket 0: [170, 90]      ← Numbers ending in 0                         ║
║   Bucket 1: []                                                            ║
║   Bucket 2: [802, 2]       ← Numbers ending in 2                         ║
║   Bucket 3: []                                                            ║
║   Bucket 4: [24]           ← Numbers ending in 4                         ║
║   Bucket 5: [45, 75]       ← Numbers ending in 5                         ║
║   Bucket 6: [66]           ← Numbers ending in 6                         ║
║   Bucket 7-9: []                                                          ║
║                                                                           ║
║   Collect from buckets (in order):                                        ║
║   [170, 90, 802, 2, 24, 45, 75, 66]                                      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════════════╗
║                           PASS 2: TENS PLACE                              ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   Current: [170, 90, 802, 2, 24, 45, 75, 66]                             ║
║                                                                           ║
║   Extract tens digit (treat missing as 0):                                ║
║                                                                           ║
║   Number:  170   90   802    2   24   45   75   66                       ║
║   Digit:     7    9     0    0    2    4    7    6                       ║
║                                                                           ║
║   Bucket 0: [802, 2]       ← Tens digit is 0                             ║
║   Bucket 2: [24]                                                          ║
║   Bucket 4: [45]                                                          ║
║   Bucket 6: [66]                                                          ║
║   Bucket 7: [170, 75]      ← Note: 170 before 75 (stable!)               ║
║   Bucket 9: [90]                                                          ║
║                                                                           ║
║   Collect: [802, 2, 24, 45, 66, 170, 75, 90]                             ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════════════╗
║                        PASS 3: HUNDREDS PLACE                             ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   Current: [802, 2, 24, 45, 66, 170, 75, 90]                             ║
║                                                                           ║
║   Extract hundreds digit:                                                 ║
║                                                                           ║
║   Number:  802    2   24   45   66  170   75   90                        ║
║   Digit:     8    0    0    0    0    1    0    0                        ║
║                                                                           ║
║   Bucket 0: [2, 24, 45, 66, 75, 90]  ← All numbers < 100                 ║
║   Bucket 1: [170]                     ← Numbers 100-199                   ║
║   Bucket 8: [802]                     ← Numbers 800-899                   ║
║                                                                           ║
║   Collect: [2, 24, 45, 66, 75, 90, 170, 802] ✅ SORTED!                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### Visual Animation

```
Input: [170, 45, 75, 90, 802, 24, 2, 66]

┌──────────────────────────────────────────────────────────────────┐
│ ONES PLACE (÷1, %10)                                             │
│                                                                  │
│   170 → 0    45 → 5    75 → 5    90 → 0                         │
│   802 → 2    24 → 4     2 → 2    66 → 6                         │
│                                                                  │
│   Buckets: 0:[170,90] 2:[802,2] 4:[24] 5:[45,75] 6:[66]         │
│   After:   [170, 90, 802, 2, 24, 45, 75, 66]                    │
├──────────────────────────────────────────────────────────────────┤
│ TENS PLACE (÷10, %10)                                            │
│                                                                  │
│   170 → 7    90 → 9   802 → 0     2 → 0                         │
│    24 → 2    45 → 4    75 → 7    66 → 6                         │
│                                                                  │
│   Buckets: 0:[802,2] 2:[24] 4:[45] 6:[66] 7:[170,75] 9:[90]     │
│   After:   [802, 2, 24, 45, 66, 170, 75, 90]                    │
├──────────────────────────────────────────────────────────────────┤
│ HUNDREDS PLACE (÷100, %10)                                       │
│                                                                  │
│   802 → 8     2 → 0    24 → 0    45 → 0                         │
│    66 → 0   170 → 1    75 → 0    90 → 0                         │
│                                                                  │
│   Buckets: 0:[2,24,45,66,75,90] 1:[170] 8:[802]                 │
│   After:   [2, 24, 45, 66, 75, 90, 170, 802] ✅                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 💻 Implementation

### Beginner-Friendly Version

```python
def radix_sort(numbers):
    """
    Sort numbers using Radix Sort.
    Works with non-negative integers.

    Think of it like sorting by digit positions,
    starting from the rightmost digit!
    """
    if not numbers:
        return numbers

    # Find maximum to know number of digits
    max_num = max(numbers)

    # Process each digit position
    exp = 1  # Start with ones place (10^0 = 1)

    while max_num // exp > 0:
        # Sort by current digit using counting sort
        counting_sort_by_digit(numbers, exp)
        exp *= 10  # Move to next digit (tens, hundreds, etc.)

    return numbers


def counting_sort_by_digit(arr, exp):
    """
    Counting sort based on digit at position 'exp'.
    exp = 1: ones place
    exp = 10: tens place
    exp = 100: hundreds place
    etc.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Digits 0-9

    # Count occurrences of each digit
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Calculate cumulative count (positions)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (traverse backwards for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]

    # Copy back to original array
    for i in range(n):
        arr[i] = output[i]


# Example
numbers = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(numbers)
print(numbers)  # [2, 24, 45, 66, 75, 90, 170, 802]
```

### Step-by-Step Walkthrough Version

```python
def radix_sort_explained(arr):
    """Radix sort with detailed output for learning"""
    print(f"🎯 Input array: {arr}")
    print("=" * 70)

    if not arr:
        return arr

    max_num = max(arr)
    num_digits = len(str(max_num))

    print(f"📊 Maximum value: {max_num}")
    print(f"📏 Number of digits: {num_digits}")
    print(f"   → Need {num_digits} passes\n")

    exp = 1
    pass_num = 1

    while max_num // exp > 0:
        place_name = ["ones", "tens", "hundreds", "thousands"][min(pass_num-1, 3)]
        print(f"{'='*70}")
        print(f"🔄 PASS {pass_num}: Sorting by {place_name.upper()} place (÷{exp}, %10)")
        print(f"{'='*70}")

        # Show digit extraction
        print("\n📝 Extracting digits:")
        for num in arr:
            digit = (num // exp) % 10
            print(f"   {num:4d} → digit = ({num} ÷ {exp}) % 10 = {digit}")

        # Perform counting sort
        counting_sort_by_digit_explained(arr, exp)

        print(f"\n✅ After pass {pass_num}: {arr}\n")

        exp *= 10
        pass_num += 1

    print("=" * 70)
    print(f"🎉 FINAL SORTED ARRAY: {arr}")
    return arr


def counting_sort_by_digit_explained(arr, exp):
    """Counting sort for specific digit with explanation"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count digits
    print("\n📦 Counting digits into buckets:")
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    print(f"   Bucket counts: {count}")
    print(f"   (index = digit, value = count)")

    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    print(f"   Cumulative:    {count}")

    # Build output (backwards for stability)
    print("\n🔨 Building sorted array (backwards for stability):")
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        count[digit] -= 1
        output[count[digit]] = arr[i]
        print(f"   Place {arr[i]:4d} (digit {digit}) at position {count[digit]}")

    # Copy back
    for i in range(n):
        arr[i] = output[i]


# Test it
numbers = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort_explained(numbers)
```

**Output:**
```
🎯 Input array: [170, 45, 75, 90, 802, 24, 2, 66]
======================================================================
📊 Maximum value: 802
📏 Number of digits: 3
   → Need 3 passes

======================================================================
🔄 PASS 1: Sorting by ONES place (÷1, %10)
======================================================================

📝 Extracting digits:
    170 → digit = (170 ÷ 1) % 10 = 0
     45 → digit = (45 ÷ 1) % 10 = 5
     75 → digit = (75 ÷ 1) % 10 = 5
     90 → digit = (90 ÷ 1) % 10 = 0
    802 → digit = (802 ÷ 1) % 10 = 2
     24 → digit = (24 ÷ 1) % 10 = 4
      2 → digit = (2 ÷ 1) % 10 = 2
     66 → digit = (66 ÷ 1) % 10 = 6

📦 Counting digits into buckets:
   Bucket counts: [2, 0, 2, 0, 1, 2, 1, 0, 0, 0]
   Cumulative:    [2, 2, 4, 4, 5, 7, 8, 8, 8, 8]

🔨 Building sorted array (backwards for stability):
   Place   66 (digit 6) at position 7
   Place    2 (digit 2) at position 3
   Place   24 (digit 4) at position 4
   Place  802 (digit 2) at position 2
   Place   90 (digit 0) at position 1
   Place   75 (digit 5) at position 6
   Place   45 (digit 5) at position 5
   Place  170 (digit 0) at position 0

✅ After pass 1: [170, 90, 802, 2, 24, 45, 75, 66]

[... passes 2 and 3 ...]

🎉 FINAL SORTED ARRAY: [2, 24, 45, 66, 75, 90, 170, 802]
```

### Version with Negative Numbers

```python
def radix_sort_with_negatives(arr):
    """
    Radix sort that handles negative numbers.

    Strategy: Separate positives and negatives,
    sort each, then combine.
    """
    if not arr:
        return arr

    # Separate positive and negative numbers
    negatives = [-x for x in arr if x < 0]  # Make positive
    positives = [x for x in arr if x >= 0]

    # Sort both (as positive numbers)
    if positives:
        radix_sort(positives)
    if negatives:
        radix_sort(negatives)
        negatives = [-x for x in reversed(negatives)]  # Reverse and negate

    # Combine: negatives first (reversed), then positives
    return negatives + positives


# Example
numbers = [170, -45, 75, -90, 802, 24, -2, 66]
result = radix_sort_with_negatives(numbers)
print(result)  # [-90, -45, -2, 24, 66, 75, 170, 802]
```

---

## 🔍 Why Does It Work?

### The Magic of Stable Sorting

```
The key insight: Using a STABLE sort at each digit position
preserves the relative order from previous passes!

Example with [45, 42]:

Pass 1 (ones): 42 comes before 45 (2 < 5)
               Result: [42, 45]

Pass 2 (tens): Both have tens digit 4
               Stable sort keeps [42, 45] order!
               Result: [42, 45] ✅

If we used an UNSTABLE sort:
               [45, 42] might become [45, 42] - WRONG!
```

### Why Right-to-Left?

```
LSD (Least Significant Digit first) - What we use:
┌────────────────────────────────────────────────────┐
│ Sort by ones → stable sort preserves              │
│ Sort by tens → stable sort preserves              │
│ Sort by hundreds → final result correct!          │
└────────────────────────────────────────────────────┘

MSD (Most Significant Digit first) - Alternative:
┌────────────────────────────────────────────────────┐
│ Sort by hundreds → split into groups              │
│ Recursively sort each group by tens               │
│ More complex, but works for strings!              │
└────────────────────────────────────────────────────┘
```

---

## 🔍 Complexity Analysis

### Time Complexity Breakdown

```python
def radix_sort(arr):
    max_num = max(arr)                    # O(n)
    exp = 1

    # Loop runs d times (d = number of digits)
    while max_num // exp > 0:             # O(d) iterations
        counting_sort_by_digit(arr, exp)  # O(n + k) each
        exp *= 10

# Total: O(d × (n + k))
# For decimal numbers: k = 10
# So effectively: O(d × n)
```

### Comparison with Other Algorithms

```
┌─────────────────────────────────────────────────────────────────┐
│                    TIME COMPLEXITY COMPARISON                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ Radix Sort:   O(d × n)  where d = number of digits              │
│ Quick Sort:   O(n log n) average                                │
│ Merge Sort:   O(n log n) always                                 │
│                                                                 │
│ When is Radix faster?                                           │
│                                                                 │
│ If d < log n, then d × n < n log n                              │
│                                                                 │
│ Example: n = 1,000,000 numbers (log n ≈ 20)                     │
│          max = 999,999 (d = 6 digits)                           │
│                                                                 │
│          Radix: 6 × 1,000,000 = 6,000,000 operations            │
│          Quick: 1,000,000 × 20 = 20,000,000 operations          │
│                                                                 │
│          Radix is ~3x faster! 🚀                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Space Complexity

```
Space needed:
- Output array: O(n)
- Count array: O(k) where k = base (10 for decimal)
- Total: O(n + k) = O(n) for fixed base

Memory layout:
┌──────────────────────────────────────────────────────────────┐
│ Input array:   [170, 45, 75, 90, 802, 24, 2, 66]  → n slots │
│ Output array:  [___, ___, ___, ___, ___, ___, ___, ___]      │
│ Count array:   [_, _, _, _, _, _, _, _, _, _]     → 10 slots│
└──────────────────────────────────────────────────────────────┘
```

---

## 💡 Practical Examples

### Example 1: Sort Phone Numbers

```python
# Phone numbers (fixed length)
phones = [5551234, 5559876, 5551111, 5553333, 5552222]

radix_sort(phones)
print(phones)
# [5551111, 5551234, 5552222, 5553333, 5559876]
```

### Example 2: Sort Student IDs

```python
# Student IDs (all same length)
student_ids = [20230001, 20210005, 20220003, 20210002, 20230004]

radix_sort(student_ids)
print(student_ids)
# [20210002, 20210005, 20220003, 20230001, 20230004]
```

### Example 3: Sort Strings (Fixed Length)

```python
def radix_sort_strings(strings, max_len):
    """
    Sort fixed-length strings using radix sort.
    Process characters from right to left.
    """
    if not strings:
        return strings

    # Pad strings to same length
    strings = [s.ljust(max_len) for s in strings]

    # Sort by each character position (right to left)
    for pos in range(max_len - 1, -1, -1):
        # Use counting sort on character at position 'pos'
        strings = counting_sort_by_char(strings, pos)

    return [s.strip() for s in strings]


def counting_sort_by_char(arr, pos):
    """Counting sort based on character at position pos"""
    count = [0] * 256  # ASCII characters
    output = [''] * len(arr)

    for s in arr:
        count[ord(s[pos])] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        char = ord(arr[i][pos])
        count[char] -= 1
        output[count[char]] = arr[i]

    return output


# Example
words = ["cat", "car", "bat", "bar", "cap"]
sorted_words = radix_sort_strings(words, 3)
print(sorted_words)  # ['bar', 'bat', 'cap', 'car', 'cat']
```

---

## 🎯 When to Use Radix Sort

### ✅ Perfect For:

**1. Large datasets with small digit count**
```python
# Million numbers, max 6 digits
numbers = [random.randint(0, 999999) for _ in range(1000000)]
# Radix: O(6n) vs Quick: O(n log n) ≈ O(20n)
# Radix is 3x faster!
```

**2. Fixed-length keys (IDs, phone numbers)**
```python
# Social Security Numbers (9 digits)
ssns = [123456789, 987654321, 555123456, ...]
# All have exactly 9 digits - perfect for radix!
```

**3. When stability is required**
```python
# Sort records by multiple fields
# First by name (stable), then by age (stable)
# Original order preserved for equal keys!
```

**4. Integers or fixed-length strings**
```python
# Postal codes, dates (YYYYMMDD), etc.
dates = [20230115, 20220301, 20230101, 20210515]
```

### ❌ Avoid When:

- **Floating-point numbers** (infinite precision)
- **Variable-length strings** (use MSD radix or other)
- **Small datasets** (overhead not worth it)
- **Very large numbers** (many digits = many passes)

---

## ⚖️ Comparison with Other Sorts

| Feature | Radix | Quick | Merge | Counting |
|---------|-------|-------|-------|----------|
| **Time** | O(d×n) | O(n log n) | O(n log n) | O(n+k) |
| **Space** | O(n+k) | O(log n) | O(n) | O(k) |
| **Stable** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| **Comparison** | ❌ No | ✅ Yes | ✅ Yes | ❌ No |
| **Best for** | Integers | General | Linked lists | Small range |

---

## ⚠️ Common Mistakes

### Mistake 1: Forgetting Stability

```python
# ❌ Using unstable sort for digits
# This will give wrong results!

# ✅ Always use stable counting sort
# Backwards traversal ensures stability
for i in range(n - 1, -1, -1):  # Must be backwards!
    ...
```

### Mistake 2: Wrong Digit Extraction

```python
# ❌ Wrong formula
digit = num % (exp * 10)  # Wrong!

# ✅ Correct formula
digit = (num // exp) % 10  # Right!

# Example for num=345, exp=10 (tens digit):
# ❌ 345 % 100 = 45 (wrong)
# ✅ (345 // 10) % 10 = 34 % 10 = 4 (correct)
```

### Mistake 3: Not Handling Zero

```python
# ❌ Loop might not execute for single-digit max
while max_num // exp > 0:  # If max_num = 5, exp = 10: 5//10 = 0

# ✅ Ensure at least one pass
while max_num // exp > 0:
    ...
    exp *= 10
# Works because we start with exp = 1
```

---

## 🎓 Key Takeaways

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                        RADIX SORT SUMMARY                                 ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  ✅ Time: O(d × n) - Linear when d is small!                             ║
║  ✅ Space: O(n + k) - Needs extra arrays                                  ║
║  ✅ NOT comparison-based - processes digits                               ║
║  ✅ Stable - preserves relative order                                     ║
║  ✅ Best for: Large arrays of integers with few digits                    ║
║                                                                           ║
║  ❌ Avoid: Floats, very large numbers, variable-length data               ║
║                                                                           ║
║  💡 Key formula: digit = (num // exp) % 10                                ║
║  💡 Remember: Sort right to left, use stable sort!                        ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## 🚀 Next Steps

1. ✅ Understand LSD (Least Significant Digit) approach
2. ✅ Know when radix beats comparison sorts
3. → Learn [[10_Merge_Sort|Merge Sort]] for comparison-based O(n log n)
4. → Try implementing MSD radix for strings

---

[[00_Index|← Back to Index]] | [[08_Counting_Sort|← Previous]] | [[10_Merge_Sort|Next: Merge Sort →]]

*Sort digit by digit for lightning speed! ⚡*
