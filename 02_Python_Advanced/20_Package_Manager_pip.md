---
title: Package Manager - pip
tags: [python, pip, packages, installation, pypi, advanced]
category: advanced
type: topic
---

# 33. Package Manager - pip

[[00_Index|← Back to Index]]

> **Install and manage Python packages with pip**

---

## 📦 What is pip?

**pip** is Python's package installer. It lets you install packages from the Python Package Index (PyPI) and other repositories.

**PyPI** = Python Package Index (pypi.org)
- 400,000+ packages available
- Free and open source
- Community maintained

---

## 🔧 Basic pip Commands

### Check pip Version

```bash
# Check if pip is installed
pip --version

# Or
python -m pip --version
```

### Upgrade pip

```bash
# Upgrade to latest version
pip install --upgrade pip

# On Windows
python -m pip install --upgrade pip
```

---

## 📥 Installing Packages

### Install Single Package

```bash
# Install latest version
pip install requests

# Install specific version
pip install requests==2.28.0

# Install minimum version
pip install requests>=2.25.0

# Install version range
pip install "requests>=2.25.0,<3.0.0"
```

### Install Multiple Packages

```bash
# Install multiple at once
pip install requests pandas numpy

# From requirements file
pip install -r requirements.txt
```

### Common Useful Packages

```bash
# Web requests
pip install requests

# Data analysis
pip install pandas numpy

# Web scraping
pip install beautifulsoup4

# Testing
pip install pytest

# Formatting
pip install black

# Type checking
pip install mypy

# Environment management
pip install virtualenv

# Web framework
pip install flask
```

---

## 📋 Listing Packages

### List Installed Packages

```bash
# List all installed packages
pip list

# Show in columns
pip list --format=columns

# Only outdated packages
pip list --outdated
```

### Show Package Details

```bash
# Show package information
pip show requests

# Output:
# Name: requests
# Version: 2.28.0
# Summary: Python HTTP for Humans.
# Home-page: https://requests.readthedocs.io
# Author: Kenneth Reitz
# License: Apache 2.0
# Location: /usr/local/lib/python3.9/site-packages
# Requires: charset-normalizer, idna, urllib3, certifi
```

---

## 🔄 Updating Packages

### Update Single Package

```bash
# Upgrade to latest version
pip install --upgrade requests

# Or
pip install -U requests
```

### Update All Packages

```bash
# List outdated packages
pip list --outdated

# Update each manually (no built-in "update all")
pip install --upgrade package1 package2 package3
```

---

## 🗑️ Uninstalling Packages

### Uninstall Single Package

```bash
pip uninstall requests

# Skip confirmation prompt
pip uninstall -y requests
```

### Uninstall Multiple Packages

```bash
pip uninstall requests pandas numpy

# From requirements file
pip uninstall -r requirements.txt -y
```

---

## 📝 Requirements Files

### Create requirements.txt

```bash
# Save current packages to file
pip freeze > requirements.txt
```

**Example requirements.txt:**
```
requests==2.28.0
pandas==1.4.2
numpy==1.22.3
beautifulsoup4==4.11.1
```

### Install from requirements.txt

```bash
# Install all packages listed
pip install -r requirements.txt
```

### Why Use requirements.txt?

✅ **Reproducibility** - Same versions everywhere  
✅ **Easy sharing** - Share exact dependencies  
✅ **Version control** - Track in git  
✅ **Deployment** - Quick setup on servers

---

## 🔍 Searching Packages

### Search PyPI

```bash
# Search for packages (deprecated in newer pip versions)
pip search "web scraping"

# Better: Search on pypi.org website
```

**Alternative:** Visit https://pypi.org and use web search

---

## 💻 Using Packages in Code

### Example: requests

```python
# After: pip install requests

import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 200
print(response.json()[:100])  # First 100 chars
```

### Example: pandas

```python
# After: pip install pandas

import pandas as pd

# Create DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}

df = pd.DataFrame(data)
print(df)
#       name  age     city
# 0    Alice   25      NYC
# 1      Bob   30       LA
# 2  Charlie   35  Chicago
```

### Example: beautifulsoup4

```python
# After: pip install beautifulsoup4

from bs4 import BeautifulSoup

html = '<html><body><h1>Hello World</h1></body></html>'
soup = BeautifulSoup(html, 'html.parser')
print(soup.h1.text)  # Hello World
```

---

## 🏠 Installation Locations

### Where Packages are Installed

```bash
# Show installation directory
python -c "import site; print(site.getsitepackages())"

# Example output:
# ['/usr/local/lib/python3.9/site-packages']
```

### User vs System Installation

```bash
# Install for current user only
pip install --user requests

# System-wide (may need sudo/admin)
pip install requests
```

---

## 🔧 Advanced pip Commands

### Download Without Installing

```bash
# Download package to current directory
pip download requests

# Download with dependencies
pip download requests -d ./packages/
```

### Install from Local File

```bash
# Install from .whl or .tar.gz file
pip install ./requests-2.28.0-py3-none-any.whl
```

### Install from Git Repository

```bash
# Install from GitHub
pip install git+https://github.com/user/repo.git

# Install specific branch
pip install git+https://github.com/user/repo.git@branch-name

# Install specific commit
pip install git+https://github.com/user/repo.git@commit-hash
```

### Editable Install (Development)

```bash
# Install package in editable mode
# Changes to source code reflected immediately
pip install -e ./mypackage/
```

---

## ⚙️ pip Configuration

### Configuration File Locations

- **Windows:** `%APPDATA%\pip\pip.ini`
- **macOS/Linux:** `~/.config/pip/pip.conf`
- **Global:** `/etc/pip.conf`

**Example pip.conf:**
```ini
[global]
timeout = 60
index-url = https://pypi.org/simple

[install]
trusted-host = pypi.org
```

---

## 🛡️ Security Best Practices

### 1. Verify Package Source

```bash
# Always check package on PyPI first
# Look for: verified publishers, download stats, last update
```

### 2. Use Specific Versions

```bash
# Bad: Installs any version
pip install requests

# Good: Pins specific version
pip install requests==2.28.0
```

### 3. Check for Vulnerabilities

```bash
# Install safety checker
pip install safety

# Check installed packages
safety check

# Check requirements.txt
safety check -r requirements.txt
```

### 4. Use Virtual Environments

Always install packages in virtual environments (see [[35_Virtual_Environments|Virtual Environments]])

---

## 🐛 Common Issues & Solutions

### Issue: pip not found

```bash
# Solution 1: Use python -m pip
python -m pip install requests

# Solution 2: Add pip to PATH
# Windows: Add Python\Scripts to PATH
# macOS/Linux: Usually in /usr/local/bin
```

### Issue: Permission denied

```bash
# Solution 1: Install for user only
pip install --user requests

# Solution 2: Use virtual environment (recommended)
```

### Issue: SSL Certificate Error

```bash
# Temporary fix (not recommended for production)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org requests

# Better: Fix system certificates
```

### Issue: Package conflicts

```bash
# Check dependencies
pip show requests

# Use virtual environment to isolate
```

---

## 📊 pip vs conda

| Feature | pip | conda |
|---------|-----|-------|
| **Language** | Python only | Multi-language |
| **Source** | PyPI | Anaconda |
| **Binary packages** | Limited | Extensive |
| **Environment management** | Via virtualenv | Built-in |
| **Best for** | Pure Python | Data science |

---

## 💡 Best Practices

### 1. Always Use requirements.txt

```bash
# Create
pip freeze > requirements.txt

# Use in project
git add requirements.txt
git commit -m "Add dependencies"
```

### 2. Pin Major Versions

```
# Good
requests>=2.28.0,<3.0.0
pandas~=1.4.0  # Compatible with 1.4.x
```

### 3. Use Virtual Environments

```bash
# Never install globally
# Always use venv or virtualenv
```

### 4. Keep pip Updated

```bash
# Regularly update
pip install --upgrade pip
```

### 5. Document Dependencies

```python
# In README.md
"""
## Installation

```bash
pip install -r requirements.txt
```
"""
```

---

## 🎓 Summary

**pip** is Python's package manager:
- `pip install` - Install packages
- `pip uninstall` - Remove packages  
- `pip list` - Show installed
- `pip freeze` - Export to requirements.txt
- `pip install -r` - Install from requirements.txt

**Key Takeaway:** Use pip + virtual environments + requirements.txt for clean, reproducible projects!

---

## 🔗 Related Topics

- [[32_Modules_and_Packages|Modules & Packages]]
- [[35_Virtual_Environments|Virtual Environments]]
- [[00_Quick_Examples|Quick Examples]]

---

[[00_Index|← Back to Index]]

*Master pip, master Python packages! 📦*
