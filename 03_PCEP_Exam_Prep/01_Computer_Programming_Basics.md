---
title: Computer Programming Basics
tags: [pcep, python, fundamentals, compilation, interpretation]
created: 2026-01-30
exam_section: 1
exam_weight: 5%
---

# 💻 Computer Programming Basics

[[00_Index|← Back to Index]] | [[02_Python_Syntax_Structure|Python Syntax →]]

> **"Understanding the foundation of how programs work"**

---

## 🎯 What the Exam Tests

- Compilation vs Interpretation
- What Python is and its characteristics
- Python versions (Python 2 vs Python 3)
- How Python code is executed

---

## 📖 Natural Language vs Programming Language

```
┌─────────────────────────────────────────────────────────────────┐
│         NATURAL vs PROGRAMMING LANGUAGES                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  NATURAL LANGUAGE (English, German...):                         │
│  • Evolved over time, many exceptions                           │
│  • Ambiguous, context-dependent                                 │
│  • "I saw a man with a telescope" (who has the telescope?)      │
│                                                                  │
│  PROGRAMMING LANGUAGE (Python, Java...):                        │
│  • Designed by humans, strict rules                             │
│  • Unambiguous, precise meaning                                 │
│  • Computers execute exactly what you write                     │
│                                                                  │
│  KEY COMPONENTS:                                                │
│  • SYNTAX: Rules for writing code (grammar)                     │
│  • SEMANTICS: Meaning of the code                               │
│  • ALPHABET: Valid characters (letters, digits, symbols)        │
│  • LEXIS: Keywords and vocabulary                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ Compilation vs Interpretation

```
┌─────────────────────────────────────────────────────────────────┐
│              COMPILATION vs INTERPRETATION                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  COMPILATION:                                                   │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                  │
│  │ Source   │ →  │ Compiler │ →  │ Machine  │ →  Execute       │
│  │ Code     │    │          │    │ Code     │                  │
│  │ (.c/.cpp)│    │          │    │ (.exe)   │                  │
│  └──────────┘    └──────────┘    └──────────┘                  │
│                                                                  │
│  • Translates ENTIRE program at once                            │
│  • Creates executable file                                      │
│  • Fast execution (pre-compiled)                                │
│  • Examples: C, C++, Rust                                       │
│                                                                  │
│  INTERPRETATION:                                                │
│  ┌──────────┐    ┌─────────────┐                               │
│  │ Source   │ →  │ Interpreter │ →  Execute line by line       │
│  │ Code     │    │             │                                │
│  │ (.py)    │    │             │                                │
│  └──────────┘    └─────────────┘                               │
│                                                                  │
│  • Translates and executes LINE BY LINE                         │
│  • No separate executable                                       │
│  • Slower but more flexible                                     │
│  • Examples: Python, JavaScript                                 │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Comparison Table (EXAM FAVORITE!)

| Aspect | Compilation | Interpretation |
|--------|-------------|----------------|
| Translation | All at once | Line by line |
| Speed | Faster execution | Slower execution |
| Error detection | Before running | During running |
| Debugging | Harder | Easier |
| Portability | Platform-specific | More portable |
| Output | Executable file | No separate file |

---

## 🐍 What is Python?

```
┌─────────────────────────────────────────────────────────────────┐
│                    PYTHON CHARACTERISTICS                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Python is:                                                     │
│  ✓ HIGH-LEVEL: Human-readable, abstracts hardware              │
│  ✓ INTERPRETED: Runs line by line                              │
│  ✓ GENERAL-PURPOSE: Web, data science, automation, etc.        │
│  ✓ DYNAMICALLY TYPED: No need to declare variable types        │
│  ✓ OBJECT-ORIENTED: Supports OOP (also functional)             │
│                                                                  │
│  Created by: Guido van Rossum                                   │
│  First release: 1991                                            │
│  Named after: Monty Python (comedy group)                       │
│                                                                  │
│  Implementations:                                               │
│  • CPython: Standard, written in C (most common)               │
│  • Jython: Runs on Java Virtual Machine                        │
│  • PyPy: Faster, uses JIT compilation                          │
│  • IronPython: For .NET framework                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔢 Python 2 vs Python 3 (EXAM TOPIC!)

```python
# ═══════════════════════════════════════════════════════════════
# PYTHON 2 vs PYTHON 3 DIFFERENCES
# ═══════════════════════════════════════════════════════════════

# Print statement vs function
# Python 2: print "Hello"
# Python 3: print("Hello")    ← PCEP uses Python 3!

# Integer division
# Python 2: 5 / 2 = 2       (truncates)
# Python 3: 5 / 2 = 2.5     (true division)
# Python 3: 5 // 2 = 2      (floor division)

# Input function
# Python 2: raw_input()
# Python 3: input()         (always returns string)

# IMPORTANT: PCEP exam is Python 3 only!
```

---

## 🔄 Python Execution Process

```
┌─────────────────────────────────────────────────────────────────┐
│              HOW PYTHON CODE RUNS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. Source Code (.py)                                           │
│        ↓                                                        │
│  2. Lexical Analysis (tokenization)                             │
│        ↓                                                        │
│  3. Parsing (syntax tree)                                       │
│        ↓                                                        │
│  4. Bytecode Compilation (.pyc)                                 │
│        ↓                                                        │
│  5. Python Virtual Machine (PVM) executes bytecode              │
│        ↓                                                        │
│  6. Output                                                      │
│                                                                  │
│  Note: Python compiles to BYTECODE (not machine code),          │
│  then the interpreter (PVM) runs the bytecode.                  │
│  This makes Python "semi-compiled, semi-interpreted"            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📝 Exam Practice Questions

**Q1: Which of the following best describes Python?**
- A) A compiled language
- B) An interpreted, high-level language ✅
- C) A machine language
- D) An assembly language

**Q2: What is the main advantage of interpretation over compilation?**
- A) Faster execution
- B) Errors are detected before running
- C) Code can be run line by line for easier debugging ✅
- D) Creates standalone executables

**Q3: Who created Python?**
- A) Bjarne Stroustrup
- B) James Gosling
- C) Guido van Rossum ✅
- D) Dennis Ritchie

**Q4: In Python 3, what does `5 / 2` return?**
- A) 2
- B) 2.5 ✅
- C) 2.0
- D) Error

---

## 🎯 Exam Checklist

- [ ] Compilation: translate all at once → executable
- [ ] Interpretation: translate line by line → no executable
- [ ] Python is interpreted, high-level, dynamically typed
- [ ] Python 3 differences: print(), division, input()
- [ ] CPython is the standard implementation
- [ ] Python bytecode runs on Python Virtual Machine

---

[[00_Index|← Index]] | [[02_Python_Syntax_Structure|Python Syntax →]]
