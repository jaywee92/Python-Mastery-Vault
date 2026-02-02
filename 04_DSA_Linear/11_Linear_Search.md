---
title: Linear Search
tags: [dsa, searching, linear-search, sequential-search, beginner]
difficulty: beginner
complexity: O(n)
---

# 11. Linear Search

[[00_Index|← Back to Index]] | [[10_Merge_Sort|← Previous]] | [[12_Binary_Search|Next: Binary Search →]]

> **The simplest search - check every element one by one**

---

## 🎯 What is Linear Search?

**Linear Search** (also called Sequential Search) checks each element in order until the target is found or the end is reached.

**Real-life analogy:**
```
Looking for your friend in a line of people:
🧍🧍🧍🧍🧍🧍🧍
Start from first person, check each one until you find your friend!
```

---

## 📊 Complexity

| Case | Time | Space | Why |
|------|------|-------|-----|
| **Best** | O(1) | O(1) | Found immediately (first element) |
| **Average** | O(n/2) → O(n) | O(1) | Found in middle on average |
| **Worst** | O(n) | O(1) | Found at end or not found |

**Key fact:** Must check every element in worst case!

---

## 🎨 How It Works - Step by Step

### Visual Search Animation

```
Search for 7 in [3, 1, 4, 1, 5, 9, 7, 6]

Step 1: Check index 0
[3, 1, 4, 1, 5, 9, 7, 6]
 ↑
 3 ≠ 7 ✗ Continue...

Step 2: Check index 1
[3, 1, 4, 1, 5, 9, 7, 6]
    ↑
    1 ≠ 7 ✗ Continue...

Step 3: Check index 2
[3, 1, 4, 1, 5, 9, 7, 6]
       ↑
       4 ≠ 7 ✗ Continue...

Step 4: Check index 3
[3, 1, 4, 1, 5, 9, 7, 6]
          ↑
          1 ≠ 7 ✗ Continue...

Step 5: Check index 4
[3, 1, 4, 1, 5, 9, 7, 6]
             ↑
             5 ≠ 7 ✗ Continue...

Step 6: Check index 5
[3, 1, 4, 1, 5, 9, 7, 6]
                ↑
                9 ≠ 7 ✗ Continue...

Step 7: Check index 6
[3, 1, 4, 1, 5, 9, 7, 6]
                   ↑
                   7 == 7 ✓ FOUND at index 6!
```

### Not Found Example

```
Search for 8 in [3, 1, 4, 1, 5, 9, 7, 6]

Check all 8 elements:
[3, 1, 4, 1, 5, 9, 7, 6]
 ✗  ✗  ✗  ✗  ✗  ✗  ✗  ✗

Reached end → 8 NOT FOUND ✗
Return -1
```

---

## 💻 Implementation

### Beginner-Friendly Version

```python
def linear_search(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1

data = [10, 20, 30, 40, 50]
print(linear_search(data, 30))  # 2
print(linear_search(data, 99))  # -1
```

### Basic Version with Comments

```python
def linear_search(arr, target):
    """
    Search for target in array using linear search.
    
    Args:
        arr: List to search in
        target: Element to find
    
    Returns:
        Index of target if found, -1 if not found
    
    Time: O(n) - must check each element
    Space: O(1) - no extra space needed
    """
    # Check each element one by one
    for i in range(len(arr)):
        # If we find it, return the index immediately
        if arr[i] == target:
            return i
    
    # If we get here, target wasn't found
    return -1

# Example usage
numbers = [3, 1, 4, 1, 5, 9, 7, 6]

# Search for 7
index = linear_search(numbers, 7)
if index != -1:
    print(f"Found 7 at index {index}")  # Found 7 at index 6
else:
    print("Not found")

# Search for 8 (not in array)
index = linear_search(numbers, 8)
if index != -1:
    print(f"Found 8 at index {index}")
else:
    print("8 not found")  # 8 not found
```

### Detailed Version with Output

```python
def linear_search_explained(arr, target):
    """Linear search with step-by-step output for learning"""
    print(f"Searching for {target} in {arr}")
    print("=" * 50)
    
    # Check each element
    for i in range(len(arr)):
        current = arr[i]
        print(f"Step {i+1}: Check arr[{i}] = {current}", end=" ")
        
        if current == target:
            print(f"→ FOUND! ✓")
            print(f"\nResult: {target} found at index {i}")
            return i
        else:
            print(f"→ Not equal, continue...")
    
    # Target not found
    print(f"\nReached end of array")
    print(f"Result: {target} NOT FOUND ✗")
    return -1

# Example 1: Target found
numbers = [3, 1, 4, 1, 5, 9, 7, 6]
linear_search_explained(numbers, 7)

print("\n" + "=" * 50 + "\n")

# Example 2: Target not found
linear_search_explained(numbers, 8)
```

**Output:**
```
Searching for 7 in [3, 1, 4, 1, 5, 9, 7, 6]
==================================================
Step 1: Check arr[0] = 3 → Not equal, continue...
Step 2: Check arr[1] = 1 → Not equal, continue...
Step 3: Check arr[2] = 4 → Not equal, continue...
Step 4: Check arr[3] = 1 → Not equal, continue...
Step 5: Check arr[4] = 5 → Not equal, continue...
Step 6: Check arr[5] = 9 → Not equal, continue...
Step 7: Check arr[6] = 7 → FOUND! ✓

Result: 7 found at index 6

==================================================

Searching for 8 in [3, 1, 4, 1, 5, 9, 7, 6]
==================================================
Step 1: Check arr[0] = 3 → Not equal, continue...
Step 2: Check arr[1] = 1 → Not equal, continue...
Step 3: Check arr[2] = 4 → Not equal, continue...
Step 4: Check arr[3] = 1 → Not equal, continue...
Step 5: Check arr[4] = 5 → Not equal, continue...
Step 6: Check arr[5] = 9 → Not equal, continue...
Step 7: Check arr[6] = 7 → Not equal, continue...
Step 8: Check arr[7] = 6 → Not equal, continue...

Reached end of array
Result: 8 NOT FOUND ✗
```

### Using Python's Built-in Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 7, 6]

# Method 1: Using 'in' operator (just checks if exists)
if 7 in numbers:
    print("7 is in the list")  # True

# Method 2: Using index() method (returns index)
try:
    index = numbers.index(7)
    print(f"Found at index: {index}")  # Found at index: 6
except ValueError:
    print("Not found")

# Method 3: Using index() with start/end
# Search only in numbers[2:6]
try:
    index = numbers.index(7, 2, 8)  # Search from index 2 to 8
    print(f"Found at index: {index}")
except ValueError:
    print("Not found in that range")
```

---

## 💡 Practical Examples

### Example 1: Find Student

```python
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
target_student = "Charlie"

def find_student(students, name):
    """Find student and return their position"""
    for i in range(len(students)):
        if students[i] == name:
            return i
    return -1

position = find_student(students, target_student)
if position != -1:
    print(f"{target_student} is at position {position+1}")
    # Charlie is at position 3
else:
    print(f"{target_student} not found")
```

### Example 2: Find All Occurrences

```python
def find_all(arr, target):
    """Find ALL positions where target appears"""
    positions = []  # Store all positions
    
    for i in range(len(arr)):
        if arr[i] == target:
            positions.append(i)
    
    return positions

numbers = [1, 3, 7, 3, 5, 3, 9]
all_positions = find_all(numbers, 3)
print(f"Found 3 at positions: {all_positions}")
# Found 3 at positions: [1, 3, 5]
```

### Example 3: Search Objects

```python
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def __repr__(self):
        return f"Student({self.name}, ID:{self.id})"

students = [
    Student("Alice", 101),
    Student("Bob", 102),
    Student("Charlie", 103)
]

def find_student_by_id(students, student_id):
    """Search for student by ID"""
    for i in range(len(students)):
        if students[i].id == student_id:
            return students[i]
    return None

# Find student with ID 102
found = find_student_by_id(students, 102)
print(found)  # Student(Bob, ID:102)
```

### Example 4: Search with Condition

```python
def find_first_greater_than(arr, value):
    """Find first element greater than value"""
    for i in range(len(arr)):
        if arr[i] > value:
            print(f"Found {arr[i]} > {value} at index {i}")
            return i
    return -1

numbers = [2, 4, 3, 8, 1, 9, 5]
index = find_first_greater_than(numbers, 5)
# Found 8 > 5 at index 3
```

---

## 🎯 When to Use Linear Search

### ✅ Perfect For:

**1. Small arrays**
```python
small_list = [5, 2, 8, 1]  # Only 4 elements
linear_search(small_list, 8)  # Fast enough!
```

**2. Unsorted arrays**
```python
unsorted = [7, 2, 9, 1, 5, 3]  # Not sorted
# Can't use binary search - must use linear!
linear_search(unsorted, 9)
```

**3. One-time search**
```python
# If you only search once, don't bother sorting
# Sorting takes O(n log n), then O(log n) search
# Linear search takes O(n) - faster for single search!
```

**4. Finding all occurrences**
```python
arr = [1, 3, 5, 3, 7, 3, 9]
# Need to check every element anyway!
find_all(arr, 3)  # [1, 3, 5]
```

### ❌ Avoid When:

- Array is **sorted** → Use [[12_Binary_Search|Binary Search]]!
- Array is **very large** and sorted → Binary search is O(log n)
- **Multiple searches** needed → Sort first, then use binary search
- **Time is critical** and array is large → Use hash table (O(1))

---

## ⚖️ Linear vs Binary Search

| Feature | Linear Search | Binary Search |
|---------|---------------|---------------|
| **Time** | O(n) | O(log n) ⚡ |
| **Sorted needed?** | ❌ No | ✅ Yes |
| **Best case** | O(1) | O(1) |
| **Worst case** | O(n) | O(log n) |
| **Simple?** | ✅ Very simple | ⚠️ More complex |
| **Small arrays** | ✅ Good | ⚠️ Overkill |
| **Large arrays** | ❌ Slow | ✅ Fast |

**Speed comparison for 1 million elements:**
```
Linear Search: Up to 1,000,000 checks
Binary Search: Only ~20 checks!
```

---

## 🔍 Why O(n)?

### In Best Case

```python
arr = [7, 2, 9, 1, 5]
target = 7

# Found immediately at index 0
# Only 1 comparison = O(1)
```

### In Average Case

```python
arr = [7, 2, 9, 1, 5]
target = 9

# On average, find in middle
# n/2 comparisons ≈ O(n)
```

### In Worst Case

```python
arr = [7, 2, 9, 1, 5]
target = 5  # At end

# Check all elements
# n comparisons = O(n)

# Or target not in array
target = 8
# Still check all elements = O(n)
```

---

## 🎓 Key Takeaways

✅ **Simplest search** - just loop through array  
✅ **O(n) time** - checks every element in worst case  
✅ **O(1) space** - no extra memory needed  
✅ **Works on unsorted** arrays  
✅ **No preprocessing** needed  
✅ **Good for small arrays** (< 100 elements)  
✅ **Required for unsorted** data  

**Remember:** Simple but slow - upgrade to binary search for sorted large arrays!

---

## 🚀 Next Steps

1. ✅ Understand sequential checking pattern
2. ✅ Know when to use vs binary search
3. → Learn [[12_Binary_Search|Binary Search]] for sorted arrays
4. → Practice choosing right search algorithm

---

[[00_Index|← Back to Index]] | [[10_Merge_Sort|← Previous]] | [[12_Binary_Search|Next: Binary Search →]]

*Search one by one! 🔍*
