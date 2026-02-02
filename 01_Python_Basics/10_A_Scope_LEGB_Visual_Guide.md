---
title: Scope - Visual Guide to LEGB Rule
category: functions
tags: ['python', 'scope', 'LEGB', 'closures', 'advanced']
created: 2026-01-27
type: topic
---

# 🔍 Scope - Visual Guide to LEGB Rule

[[00_Index|← Back to Index]] | [[10_Scope_and_Closures|Scope & Closures →]]

---

## 🎯 What is Scope?

**Scope** determines where variables are accessible in your code. Python uses the **LEGB Rule** to find variables.

---

## 📚 The LEGB Rule

```
L ocal      → Inside current function
E nclosing  → Inside parent function(s)
G lobal     → At module level
B uilt-in   → Python's built-in names
```

**Search Order:** Python looks for variables in this order: L → E → G → B

---

## 🎨 Visual Example 1: Basic LEGB

```python
# B: Built-in (always available)
print()  # ← This is a built-in function
len()    # ← Also built-in

# G: Global scope (module level)
x = "GLOBAL"

def outer():
    # E: Enclosing scope (outer function)
    x = "ENCLOSING"
    
    def inner():
        # L: Local scope (current function)
        x = "LOCAL"
        print(x)  # Which x will Python find?
    
    inner()
    print(x)  # Which x here?

outer()
print(x)  # Which x here?
```

### Visualization:
```
┌─────────────────────────────────────────┐
│ B: Built-in (print, len, etc.)         │
│  ↑                                      │
│  │ Python searches upward               │
│  │                                      │
│ ┌───────────────────────────────────┐  │
│ │ G: Global Scope                   │  │
│ │ x = "GLOBAL" ◄────────────────────┼──┼── print(x) finds THIS
│ │                                   │  │
│ │ ┌─────────────────────────────┐  │  │
│ │ │ E: Enclosing (outer fn)     │  │  │
│ │ │ x = "ENCLOSING" ◄───────────┼──┼──┼── print(x) in outer() finds THIS
│ │ │                             │  │  │
│ │ │ ┌─────────────────────────┐ │  │  │
│ │ │ │ L: Local (inner fn)     │ │  │  │
│ │ │ │ x = "LOCAL" ◄───────────┼─┼──┼──┼── print(x) in inner() finds THIS
│ │ │ │                         │ │  │  │
│ │ │ │ print(x) looks here ───┘ │  │  │
│ │ │ │         first!            │  │  │
│ │ │ └─────────────────────────┘ │  │  │
│ │ └─────────────────────────────┘  │  │
│ └───────────────────────────────────┘  │
└─────────────────────────────────────────┘

Output:
LOCAL       ← inner() finds LOCAL x
ENCLOSING   ← outer() finds ENCLOSING x
GLOBAL      ← module level finds GLOBAL x
```

---

## 🔄 Example 2: No Local Variable

```python
x = "GLOBAL"

def my_function():
    # No local x defined!
    print(x)  # Python searches: L → E → G → found!

my_function()
```

### Visualization:
```
┌─────────────────────────────────┐
│ G: Global                       │
│ x = "GLOBAL" ◄──────────────────┼── Found here!
│                                 │
│ ┌─────────────────────────────┐ │
│ │ L: my_function()            │ │
│ │ (no local x)                │ │
│ │                             │ │
│ │ print(x) ─────→ looks up ───┘ │
│ │                   in outer     │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘

Output: GLOBAL
```

---

## ⚠️ Common Mistake: UnboundLocalError

```python
x = "GLOBAL"

def my_function():
    print(x)  # ❌ UnboundLocalError!
    x = "LOCAL"

# Why? Python sees "x = ..." and marks x as LOCAL
# But print(x) comes BEFORE assignment!
```

### Visualization:
```
┌────────────────────────────────────┐
│ G: Global                          │
│ x = "GLOBAL"                       │
│                                    │
│ ┌────────────────────────────────┐ │
│ │ L: my_function()               │ │
│ │                                │ │
│ │ Step 1: Python scans function  │ │
│ │         sees "x = ..."         │ │
│ │         marks x as LOCAL ✓     │ │
│ │                                │ │
│ │ Step 2: print(x) ──→ look for │ │
│ │         local x... not         │ │
│ │         assigned yet! ❌       │ │
│ │                                │ │
│ │ Step 3: x = "LOCAL" (too late!)│ │
│ └────────────────────────────────┘ │
└────────────────────────────────────┘

Error: UnboundLocalError: local variable 'x' 
       referenced before assignment
```

**Fix:** Use `global` keyword:
```python
x = "GLOBAL"

def my_function():
    global x  # Now x refers to global scope
    print(x)  # ✓ Works!
    x = "MODIFIED"

my_function()
print(x)  # "MODIFIED" - global was changed!
```

---

## 🔗 The `global` Keyword

```python
count = 0  # Global variable

def increment():
    global count  # Tell Python: use global count
    count += 1
    return count

print(increment())  # 1
print(increment())  # 2
print(increment())  # 3
print(count)        # 3
```

### Visualization:
```
Without global:              With global:
┌──────────────────┐        ┌──────────────────┐
│ G: count = 0     │        │ G: count = 0     │
│                  │        │  ↑               │
│ ┌──────────────┐ │        │  │ Modified!    │
│ │ increment()  │ │        │  │               │
│ │ count += 1   │ │        │ ┌──────────────┐ │
│ │ ❌ Error!    │ │        │ │ increment()  │ │
│ │ (local not   │ │        │ │ global count │ │
│ │  defined)    │ │        │ │ count += 1   │ │
│ └──────────────┘ │        │ │ ✓ Works! ────┘ │
└──────────────────┘        │ └──────────────┘ │
                            └──────────────────┘
```

---

## 🏠 The `nonlocal` Keyword

For accessing variables in enclosing (parent) function:

```python
def outer():
    x = "OUTER"
    
    def inner():
        nonlocal x  # Access outer's x
        x = "MODIFIED"
        print(f"Inner: {x}")
    
    print(f"Before: {x}")
    inner()
    print(f"After: {x}")

outer()
```

### Visualization:
```
┌───────────────────────────────────────┐
│ outer()                               │
│ x = "OUTER" ◄─────────────────────────┼── Modified by inner!
│  ↑                                    │
│  │ nonlocal x creates link            │
│  │                                    │
│ ┌─────────────────────────────────┐  │
│ │ inner()                         │  │
│ │ nonlocal x  ──→ points to outer │  │
│ │ x = "MODIFIED" ──→ modifies ────┘  │
│ └─────────────────────────────────┘  │
└───────────────────────────────────────┘

Output:
Before: OUTER
Inner: MODIFIED
After: MODIFIED  ← outer's x was changed!
```

---

## 💡 Comparison Table

```
┌──────────┬─────────────────────────┬────────────────────────┐
│ Keyword  │ What it does            │ When to use            │
├──────────┼─────────────────────────┼────────────────────────┤
│ (none)   │ Creates local variable  │ Most of the time       │
│ global   │ Access global variable  │ Modify module variable │
│ nonlocal │ Access enclosing var    │ Modify parent function │
└──────────┴─────────────────────────┴────────────────────────┘
```

---

## 🎯 Real Example: Counter with Closure

```python
def make_counter():
    count = 0  # Enclosing scope
    
    def increment():
        nonlocal count  # Access enclosing count
        count += 1
        return count
    
    return increment  # Return the function

# Create counters
counter1 = make_counter()
counter2 = make_counter()

print(counter1())  # 1
print(counter1())  # 2
print(counter1())  # 3

print(counter2())  # 1  ← separate counter!
print(counter2())  # 2
```

### Visualization:
```
make_counter() call #1          make_counter() call #2
┌─────────────────────┐        ┌─────────────────────┐
│ count = 0           │        │ count = 0           │
│  ↑                  │        │  ↑                  │
│  │                  │        │  │                  │
│ ┌─────────────────┐ │        │ ┌─────────────────┐ │
│ │ increment()     │ │        │ │ increment()     │ │
│ │ nonlocal count  │ │        │ │ nonlocal count  │ │
│ │ count += 1 ─────┘ │        │ │ count += 1 ─────┘ │
│ └─────────────────┘ │        │ └─────────────────┘ │
│        ↓             │        │        ↓             │
│    counter1          │        │    counter2          │
│    (separate!)       │        │    (separate!)       │
└─────────────────────┘        └─────────────────────┘

Each has its OWN count variable!
```

---

## 🔥 Built-in Names

Python has many built-in names:

```python
# These are always available (Built-in scope)
print()
len()
range()
int()
str()
list()
dict()

# You CAN shadow them (but shouldn't!)
len = 42  # ❌ Bad idea!
print(len)  # 42 (not the function anymore!)

# Now len() doesn't work:
# len([1,2,3])  # ❌ TypeError: 'int' object is not callable
```

### Visualization:
```
Before shadowing:           After len = 42:
┌─────────────────┐        ┌─────────────────┐
│ B: len() ◄──────┼────┐   │ B: len()        │
│                 │    │   │ (hidden!)       │
│ ┌─────────────┐ │    │   │ ┌─────────────┐ │
│ │ G: (none)   │ │    │   │ │ G: len = 42 │ │
│ │             │ │    │   │ │      ↑      │ │
│ │ len(...) ───┘ │    │   │ │ len finds ──┘ │
│ │  finds ───────┘    │   │ │  this first!│ │
│ │  built-in          │   │ └─────────────┘ │
│ └─────────────┘ │        └─────────────────┘
└─────────────────┘        len(...) → Error!
```

**Best Practice:** Never shadow built-in names!

---

## 📝 Quick Reference

```
LEGB Search Order:
┌─────────┐
│ LOCAL   │ → def function(): x = 1
├─────────┤
│ ENCLOS  │ → def outer(): x = 1
│  -ING   │    def inner(): use x
├─────────┤
│ GLOBAL  │ → x = 1  (at module level)
├─────────┤
│ BUILT-  │ → print, len, range, etc.
│  IN     │
└─────────┘

Keywords:
• global    - access/modify global variable
• nonlocal  - access/modify enclosing variable
• (none)    - create new local variable

Common Errors:
• UnboundLocalError - using local var before assignment
• Shadowing built-ins - naming variable same as built-in
```

---

## 🎯 Practice Questions

```python
# Question 1: What prints?
x = "GLOBAL"
def func():
    print(x)
func()

# Question 2: What happens?
x = "GLOBAL"
def func():
    print(x)
    x = "LOCAL"
func()

# Question 3: What prints?
def outer():
    x = "OUTER"
    def inner():
        nonlocal x
        x = "CHANGED"
    inner()
    print(x)
outer()
```

> [!success]- Answers
> 1. Prints: `GLOBAL` - no local x, finds global
> 2. Error: `UnboundLocalError` - x marked as local due to assignment, but used before assignment
> 3. Prints: `CHANGED` - nonlocal modifies outer's x

---

## 🔗 Related Topics

- [[10_Scope_and_Closures|Scope & Closures (detailed)]]
- [[08_Functions|Functions Deep Dive]]
- [[../02_Python_Advanced/10_Common_Pitfalls|Common Pitfalls]] - Scope mistakes

---

[[00_Index|← Back to Index]]

*Understanding scope prevents many bugs! 🐛*
