---
title: Virtual Environments
tags: [python, venv, virtualenv, environment, isolation, advanced]
category: advanced
type: topic
---

# 35. Virtual Environments

[[00_Index|← Back to Index]]

> **Isolate project dependencies with virtual environments**

---

## 🎯 What is a Virtual Environment?

A **virtual environment** is an isolated Python environment where you can install packages without affecting your system Python.

**Why use them?**
- ✓ Avoid package conflicts between projects
- ✓ Different Python versions per project
- ✓ Clean, reproducible environments
- ✓ Easy to share requirements

---

## 🆚 Without vs With Virtual Environments

### ❌ Without Virtual Env

```
System Python
├── pandas==1.5.0  (Project A needs)
├── pandas==2.0.0  (Project B needs) ← CONFLICT!
└── 100+ other packages (messy!)
```

### ✅ With Virtual Envs

```
System Python (clean)

Project A/
└── venv/ (isolated)
    └── pandas==1.5.0

Project B/
└── venv/ (isolated)
    └── pandas==2.0.0
```

---

## 🛠️ Creating Virtual Environments

### Method 1: venv (Built-in)

**Create:**
```bash
# Windows
python -m venv myenv

# Mac/Linux
python3 -m venv myenv
```

**Activate:**
```bash
# Windows
myenv\Scripts\activate

# Mac/Linux
source myenv/bin/activate
```

**Deactivate:**
```bash
deactivate
```

### Method 2: virtualenv (Third-party)

**Install:**
```bash
pip install virtualenv
```

**Create:**
```bash
virtualenv myenv
```

**Activate:** (same as venv)

---

## 📋 Complete Workflow

### Step 1: Create Project

```bash
mkdir my_project
cd my_project
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

**Directory structure:**
```
my_project/
├── venv/
│   ├── Scripts/ (Windows) or bin/ (Mac/Linux)
│   ├── Lib/
│   └── ...
└── (your code here)
```

### Step 3: Activate

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**You'll see:**
```bash
(venv) C:\my_project>
```

### Step 4: Install Packages

```bash
pip install requests
pip install pandas
```

### Step 5: Save Dependencies

```bash
pip freeze > requirements.txt
```

**requirements.txt:**
```
requests==2.28.2
pandas==1.5.3
numpy==1.24.0
```

### Step 6: Share Project

Someone else can recreate your environment:

```bash
# Create venv
python -m venv venv

# Activate
source venv/bin/activate  # or venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt
```

---

## 🎨 VS Code Integration

### Auto-detect Virtual Environment

1. Open project folder
2. Press `Ctrl+Shift+P`
3. Type "Python: Select Interpreter"
4. Choose your venv

**VS Code will:**
- Auto-activate venv in terminal
- Use venv's Python for running code
- Show venv packages in IntelliSense

---

## 📦 Managing Multiple Projects

### Project Structure

```
Projects/
├── web_scraper/
│   ├── venv/
│   ├── requirements.txt
│   └── scraper.py
│
├── data_analysis/
│   ├── venv/
│   ├── requirements.txt
│   └── analysis.py
│
└── api_project/
    ├── venv/
    ├── requirements.txt
    └── app.py
```

Each project has its own isolated environment!

---

## 🔄 Updating Environments

### Update Single Package

```bash
pip install --upgrade package_name
```

### Update All Packages

```bash
pip list --outdated  # See what's outdated

# Update one by one
pip install --upgrade requests
pip install --upgrade pandas

# Save new versions
pip freeze > requirements.txt
```

---

## 🗑️ Cleaning Up

### Delete Virtual Environment

```bash
# Deactivate first
deactivate

# Delete folder
# Windows
rmdir /s venv

# Mac/Linux
rm -rf venv
```

### Recreate from requirements.txt

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🎯 Best Practices

### 1. One Venv Per Project

```
✅ project1/venv/
✅ project2/venv/

❌ shared_venv/  (Don't share between projects!)
```

### 2. Add venv to .gitignore

```
# .gitignore
venv/
env/
*.pyc
__pycache__/
```

**Never commit venv to git!** Use requirements.txt instead.

### 3. Name Consistently

```
✅ venv/     (common)
✅ env/      (common)
✅ .venv/    (hidden)

❌ myproject_venv/  (too specific)
```

### 4. Always Activate

```bash
# Before working:
source venv/bin/activate

# Before installing packages:
pip list  # Check you're in venv

# When done:
deactivate
```

### 5. Document Python Version

```
# requirements.txt
python>=3.9

# Or README.md
## Requirements
- Python 3.9 or higher
```

---

## 🔧 Troubleshooting

### "python not found"

```bash
# Use full path
python3 -m venv venv

# Or
py -m venv venv
```

### Activation Not Working (Windows)

```bash
# Enable scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

### Wrong Python Version

```bash
# Specify Python version
python3.9 -m venv venv

# Or
py -3.9 -m venv venv
```

### Packages Not Found After Activation

```bash
# Check you're in venv
which python  # Mac/Linux
where python  # Windows

# Should show path inside venv/
```

---

## 💡 Advanced: conda

For data science, consider **conda**:

```bash
# Create environment
conda create -n myenv python=3.9

# Activate
conda activate myenv

# Install packages
conda install numpy pandas matplotlib

# Deactivate
conda deactivate
```

**Advantage:** Handles non-Python dependencies better.

---

## 📊 Comparison

| Feature | venv | virtualenv | conda |
|---------|------|------------|-------|
| Built-in | ✅ | ❌ | ❌ |
| Speed | Fast | Fast | Slower |
| Python only | ✅ | ✅ | ❌ |
| System packages | ❌ | Optional | ✅ |
| Best for | General | General | Data Science |

---

## 🎓 Summary

- **Virtual env** = Isolated Python environment
- **venv** = Built-in tool (recommended)
- **requirements.txt** = Share dependencies
- **Activate** = Use environment
- **Deactivate** = Exit environment

**Key Takeaway:** Always use virtual environments to keep projects isolated and manageable!

---

## 🔗 Related Topics

- [[33_Package_Manager|Package Manager]]
- [[32_Modules_and_Packages|Modules & Packages]]

---

[[00_Index|← Back to Index]]

*Isolate and conquer! 🎯✨*
