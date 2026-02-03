---
title: Stacks - LIFO Data Structure
tags: [dsa, stack, lifo, data-structures]
created: 2026-01-28
difficulty: beginner
---

# 13. Stacks

[[00_Index|← Back to Index]] | [[12_Binary_Search|← Previous]] | [[14_Queues|Next: Queues →]]

> **Last-In-First-Out - like a stack of plates**

---

## 🎯 What is a Stack?

A **stack** is a linear data structure that follows **LIFO** (Last-In-First-Out) principle.

**Think of it like:**
- Stack of plates 🍽️
- Stack of books 📚
- Browser back button ←
- Undo/Redo functionality ↶

---

## 📊 Operations & Complexity

| Operation | Time | Description |
|-----------|------|-------------|
| **push(x)** | O(1) | Add to top |
| **pop()** | O(1) | Remove from top |
| **peek()** | O(1) | View top element |
| **is_empty()** | O(1) | Check if empty |
| **size()** | O(1) | Get size |

---

## 🎨 Visualization

```
Push operations:
─────────────────
push(1)        push(2)        push(3)
  │              │              │
  ▼              ▼              ▼
┌───┐          ┌───┐          ┌───┐
│ 1 │ ← top    │ 2 │ ← top    │ 3 │ ← top
└───┘          ├───┤          ├───┤
               │ 1 │          │ 2 │
               └───┘          ├───┤
                              │ 1 │
                              └───┘

Pop operations:
──────────────
pop()          pop()          pop()
  │              │              │
  ▼              ▼              ▼
┌───┐          ┌───┐
│ 2 │ ← top    │ 1 │ ← top    Empty!
├───┤          └───┘
│ 1 │
└───┘
Returns: 3     Returns: 2     Returns: 1
```

---

## 💻 Implementation

### Beginner-Friendly Version (Using List)

```python
stack = []

# Push
stack.append("A")
stack.append("B")
stack.append("C")

# Peek (top item)
print(stack[-1])  # C

# Pop
print(stack.pop())  # C
print(stack)        # ['A', 'B']
```

### Using Python List

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top - O(1)"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items - O(1)"""
        return len(self.items)
    
    def __str__(self):
        """String representation"""
        return f"Stack({self.items})"

# Usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)        # Stack([1, 2, 3])
print(stack.peek()) # 3
print(stack.pop())  # 3
print(stack.size()) # 2
```

### Simple Version

```python
# Using list directly
stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)

# Pop
top = stack.pop()  # 3

# Peek
top = stack[-1]    # 2

# Check empty
is_empty = len(stack) == 0
```

---

## 💡 Practical Applications

### 1. Check Balanced Parentheses

```python
def is_balanced(expression):
    """Check if parentheses are balanced"""
    stack = []
    matching = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in matching:  # Opening bracket
            stack.append(char)
        elif char in matching.values():  # Closing bracket
            if not stack:
                return False
            if matching[stack.pop()] != char:
                return False
    
    return len(stack) == 0

print(is_balanced("({[]})"))   # True
print(is_balanced("({[}])"))   # False
print(is_balanced("((())"))    # False
```

### 2. Reverse a String

```python
def reverse_string(s):
    """Reverse string using stack"""
    stack = []
    
    # Push all characters
    for char in s:
        stack.append(char)
    
    # Pop all characters
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

print(reverse_string("hello"))  # "olleh"
```

### 3. Undo/Redo Functionality

```python
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []
    
    def type(self, chars):
        """Type new characters"""
        self.undo_stack.append(self.text)
        self.text += chars
        self.redo_stack.clear()  # Clear redo on new action
    
    def undo(self):
        """Undo last action"""
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()
    
    def redo(self):
        """Redo last undone action"""
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()

# Usage
editor = TextEditor()
editor.type("Hello")
editor.type(" World")
print(editor.text)    # "Hello World"
editor.undo()
print(editor.text)    # "Hello"
editor.redo()
print(editor.text)    # "Hello World"
```

### 4. Evaluate Postfix Expression

```python
def eval_postfix(expression):
    """Evaluate postfix expression like '2 3 + 5 *'"""
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            
            stack.append(result)
    
    return stack.pop()

print(eval_postfix("2 3 + 5 *"))  # (2+3)*5 = 25
print(eval_postfix("5 1 2 + 4 * + 3 -"))  # 5+((1+2)*4)-3 = 14
```

---

## 🎯 Common Stack Patterns

### Pattern 1: Monotonic Stack

```python
def next_greater_element(arr):
    """Find next greater element for each element"""
    result = [-1] * len(arr)
    stack = []  # Store indices
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    
    return result

arr = [4, 5, 2, 10, 8]
print(next_greater_element(arr))  # [5, 10, 10, -1, -1]
```

### Pattern 2: Min Stack (O(1) min)

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Track minimums
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

# Usage
stack = MinStack()
stack.push(3)
stack.push(1)
stack.push(2)
print(stack.get_min())  # 1 - in O(1)!
```

---

## ✅ When to Use Stacks

**Perfect for:**
- ✅ Function call management
- ✅ Expression evaluation
- ✅ Undo/Redo operations
- ✅ Browser history
- ✅ Balanced parentheses
- ✅ DFS traversal
- ✅ Backtracking algorithms

**Not suitable for:**
- ❌ Need access to middle elements
- ❌ FIFO required (use queue)
- ❌ Need random access

---

## 🎓 Key Takeaways

✅ **LIFO** - Last In, First Out  
✅ **O(1)** for push, pop, peek  
✅ **Simple** - easy to implement  
✅ **Versatile** - many applications  
✅ **Use Python list** as stack

---

[[00_Index|← Back to Index]] | [[12_Binary_Search|← Previous]] | [[14_Queues|Next: Queues →]]

*Stack it up! 📚*
---

## 🎨 Visualization (Optional)

```python
import sys
from pathlib import Path

# Add vault root to sys.path (Obsidian runner)
vault_root = Path.cwd()
if str(vault_root) not in sys.path:
    sys.path.append(str(vault_root))

from DSA_Utils.utils import draw_stack

stack = ["A", "B", "C"]
draw_stack(stack)
```
