---
title: Professional Libraries & Tools
tags: [python, libraries, professional, practical, tools]
created: 2026-02-01
type: topic
difficulty: intermediate-advanced
---

# 🚀 Professional Libraries & Tools

[[00_Index|← Back to Index]]

> **The most important libraries for professional Python development**

---

## 📦 Must-Have Libraries

### Overview by Category

| Category | Library | Use Case |
|----------|---------|----------|
| HTTP | `requests` | API calls, Web Scraping |
| Data | `pandas` | Data analysis |
| Math | `numpy` | Numerical computing |
| Plots | `matplotlib` | Visualization |
| CLI | `argparse`, `click` | Command-line tools |
| Config | `python-dotenv` | Environment variables |
| Validation | `pydantic` | Data validation |
| Testing | `pytest` | Unit tests |
| HTTP Server | `fastapi`, `flask` | Web APIs |
| Database | `sqlalchemy` | ORM |
| Async | `asyncio`, `aiohttp` | Asynchronous programming |

---

## 🌐 `requests` - HTTP for Humans

```bash
pip install requests
```

```python
import requests

# GET Request
response = requests.get('https://api.github.com/users/python')
print(response.status_code)  # 200
print(response.json())       # Dict with data

# With parameters
params = {'q': 'python', 'page': 1}
response = requests.get('https://api.example.com/search', params=params)

# POST Request
data = {'username': 'max', 'password': 'secret'}
response = requests.post('https://api.example.com/login', json=data)

# With headers (e.g. API Key)
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}
response = requests.get('https://api.example.com/data', headers=headers)

# Set timeout (important!)
response = requests.get(url, timeout=10)  # 10 seconds

# Session for multiple requests
session = requests.Session()
session.headers.update({'Authorization': 'Bearer TOKEN'})
response = session.get('https://api.example.com/data')

# Error handling
response = requests.get(url)
response.raise_for_status()  # Raises exception on 4xx/5xx

# Download a file
response = requests.get('https://example.com/file.pdf')
with open('file.pdf', 'wb') as f:
    f.write(response.content)
```

---

## 📊 `pandas` - Data Analysis

```bash
pip install pandas
```

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Berlin', 'Hamburg', 'Munich']
})

# Read/write CSV
df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)

# Read/write Excel
df = pd.read_excel('data.xlsx')
df.to_excel('output.xlsx', index=False)

# Read JSON
df = pd.read_json('data.json')

# Basic operations
df.head()           # First 5 rows
df.tail()           # Last 5 rows
df.info()           # Column info
df.describe()       # Statistics
df.shape            # (rows, columns)
df.columns          # Column names

# Select columns
df['name']              # One column (Series)
df[['name', 'age']]     # Multiple columns (DataFrame)

# Filter
df[df['age'] > 25]                    # Rows where age > 25
df[df['city'] == 'Berlin']            # Rows where city = Berlin
df[(df['age'] > 25) & (df['city'] == 'Berlin')]  # Combined

# Sort
df.sort_values('age')                  # Ascending
df.sort_values('age', ascending=False) # Descending

# Group & Aggregate
df.groupby('city')['age'].mean()       # Average age per city
df.groupby('city').agg({'age': 'mean', 'name': 'count'})

# Create new column
df['age_next_year'] = df['age'] + 1

# Missing values
df.isna().sum()           # Count NaN per column
df.dropna()               # Remove rows with NaN
df.fillna(0)              # Replace NaN with 0

# Duplicates
df.drop_duplicates()      # Remove duplicates
df.duplicated().sum()     # Count duplicates
```

---

## 🔢 `numpy` - Numerical Computing

```bash
pip install numpy
```

```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((3, 3))           # 3x3 matrix with zeros
ones = np.ones((2, 4))             # 2x4 matrix with ones
range_arr = np.arange(0, 10, 2)    # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)    # 5 values from 0 to 1

# Array properties
arr.shape       # (5,)
arr.dtype       # dtype('int64')
arr.ndim        # 1 (dimension)

# Math operations (element-wise!)
arr * 2         # [2, 4, 6, 8, 10]
arr ** 2        # [1, 4, 9, 16, 25]
np.sqrt(arr)    # Square root
np.exp(arr)     # e^x
np.log(arr)     # Natural log

# Statistics
np.mean(arr)    # Mean
np.median(arr)  # Median
np.std(arr)     # Standard deviation
np.sum(arr)     # Sum
np.min(arr)     # Minimum
np.max(arr)     # Maximum

# Matrix operations
matrix = np.array([[1, 2], [3, 4]])
matrix.T                    # Transpose
np.dot(matrix, matrix)      # Matrix multiplication
np.linalg.inv(matrix)       # Inverse
np.linalg.det(matrix)       # Determinant

# Indexing & Slicing
arr = np.array([1, 2, 3, 4, 5])
arr[0]          # 1
arr[-1]         # 5
arr[1:4]        # [2, 3, 4]
arr[arr > 2]    # [3, 4, 5] - Boolean indexing

# Reshape
arr = np.arange(12)
matrix = arr.reshape(3, 4)  # 3x4 matrix

# Random
np.random.seed(42)                    # Reproducible
np.random.rand(3, 3)                  # 3x3 random [0,1)
np.random.randint(0, 100, size=10)    # 10 random integers
np.random.choice([1, 2, 3], size=5)   # Random choice
np.random.shuffle(arr)                # In-place shuffle
```

---

## 📈 `matplotlib` - Visualization

```bash
pip install matplotlib
```

```python
import matplotlib.pyplot as plt
import numpy as np

# Simple line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Sine Function')
plt.legend()
plt.grid(True)
plt.savefig('plot.png', dpi=300)
plt.show()

# Bar chart
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

plt.bar(categories, values, color='steelblue')
plt.title('Bar Chart')
plt.show()

# Histogram
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram')
plt.show()

# Scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 100 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.colorbar()
plt.show()

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, y)
axes[0, 0].set_title('Plot 1')

axes[0, 1].bar(['A', 'B'], [10, 20])
axes[0, 1].set_title('Plot 2')

axes[1, 0].scatter(x, y)
axes[1, 0].set_title('Plot 3')

axes[1, 1].hist(data)
axes[1, 1].set_title('Plot 4')

plt.tight_layout()
plt.show()
```

---

## ⚙️ `argparse` - CLI Tools

```bash
# Already included in Python
```

```python
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='A tool that does something'
    )

    # Positional argument
    parser.add_argument('filename', help='The file to process')

    # Optional argument with value
    parser.add_argument('-o', '--output',
                        default='output.txt',
                        help='Output file (default: output.txt)')

    # Flag (True/False)
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Verbose output')

    # Argument with type
    parser.add_argument('-n', '--number',
                        type=int,
                        default=10,
                        help='Count (default: 10)')

    # Choice
    parser.add_argument('--format',
                        choices=['json', 'csv', 'xml'],
                        default='json',
                        help='Output format')

    args = parser.parse_args()

    # Usage
    print(f'File: {args.filename}')
    print(f'Output: {args.output}')
    print(f'Verbose: {args.verbose}')
    print(f'Number: {args.number}')

if __name__ == '__main__':
    main()

# Call:
# python script.py input.txt -o result.txt -v -n 20
```

---

## 🔐 `python-dotenv` - Environment Variables

```bash
pip install python-dotenv
```

```python
# .env file (DO NOT commit to Git!)
# API_KEY=your_secret_key
# DATABASE_URL=postgresql://user:pass@localhost/db
# DEBUG=true

from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Use variables
api_key = os.getenv('API_KEY')
database_url = os.getenv('DATABASE_URL')
debug = os.getenv('DEBUG', 'false').lower() == 'true'

# With path
load_dotenv('/path/to/.env')

# Allow override
load_dotenv(override=True)
```

**.gitignore:**
```
.env
.env.local
*.env
```

---

## ✅ `pydantic` - Data Validation

```bash
pip install pydantic
```

```python
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    age: Optional[int] = None
    tags: List[str] = []
    created_at: datetime = Field(default_factory=datetime.now)

    @validator('age')
    def age_must_be_positive(cls, v):
        if v is not None and v < 0:
            raise ValueError('Age must be positive')
        return v

# Usage
user = User(
    id=1,
    name='Max Mustermann',
    email='max@example.com',
    age=25
)

print(user.name)       # 'Max Mustermann'
print(user.dict())     # As dictionary
print(user.json())     # As JSON string

# Validation fails
try:
    invalid_user = User(id=1, name='M', email='invalid')
except Exception as e:
    print(e)  # Validation error

# Create from dict
data = {'id': 2, 'name': 'Anna', 'email': 'anna@example.com'}
user = User(**data)

# Settings with Pydantic
from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key: str
    debug: bool = False
    database_url: str

    class Config:
        env_file = '.env'

settings = Settings()
print(settings.api_key)
```

---

## 🧪 `pytest` - Testing

```bash
pip install pytest pytest-cov
```

```python
# test_calculator.py
import pytest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Simple test
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# Test with multiple values (parametrization)
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# Test exception
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# Fixtures
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_with_fixture(sample_data):
    assert len(sample_data) == 5
    assert sum(sample_data) == 15

# Setup/Teardown
@pytest.fixture
def database_connection():
    # Setup
    conn = create_connection()
    yield conn
    # Teardown
    conn.close()
```

**Run:**
```bash
pytest                          # All tests
pytest test_calculator.py       # Specific file
pytest -v                       # Verbose
pytest -k "add"                 # Only tests with "add" in name
pytest --cov=myproject          # With coverage
```

---

## ⚡ `fastapi` - Modern Web APIs

```bash
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Data models
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

class ItemResponse(Item):
    id: int

# In-memory "database"
items_db = {}
current_id = 0

# GET - List all items
@app.get("/items", response_model=List[ItemResponse])
def get_items():
    return list(items_db.values())

# GET - Single item
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# POST - Create item
@app.post("/items", response_model=ItemResponse)
def create_item(item: Item):
    global current_id
    current_id += 1
    new_item = ItemResponse(id=current_id, **item.dict())
    items_db[current_id] = new_item
    return new_item

# PUT - Update item
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = ItemResponse(id=item_id, **item.dict())
    items_db[item_id] = updated_item
    return updated_item

# DELETE - Delete item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted"}

# Query Parameters
@app.get("/search")
def search_items(q: str, limit: int = 10):
    results = [i for i in items_db.values() if q.lower() in i.name.lower()]
    return results[:limit]

# Start with: uvicorn main:app --reload
# Docs at: http://localhost:8000/docs
```

---

## 🗄️ `sqlalchemy` - Database ORM

```bash
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Database connection
engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define models
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)

    posts = relationship('Post', back_populates='author')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', back_populates='posts')

# Create tables
Base.metadata.create_all(engine)

# CRUD Operations
session = Session()

# Create
new_user = User(name='Max', email='max@example.com')
session.add(new_user)
session.commit()

# Read
user = session.query(User).filter_by(name='Max').first()
all_users = session.query(User).all()

# Update
user.email = 'max.new@example.com'
session.commit()

# Delete
session.delete(user)
session.commit()

# Queries
users = session.query(User).filter(User.name.like('%Max%')).all()
users = session.query(User).order_by(User.name).limit(10).all()

session.close()
```

---

## ⏰ `asyncio` - Asynchronous Programming

```python
import asyncio
import aiohttp  # pip install aiohttp

# Async function
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

# Multiple URLs in parallel
async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Run
urls = [
    'https://api.github.com/users/python',
    'https://api.github.com/users/django',
    'https://api.github.com/users/fastapi',
]

results = asyncio.run(fetch_all(urls))

# Async with timeout
async def fetch_with_timeout(url, timeout=10):
    async with aiohttp.ClientSession() as session:
        async with asyncio.timeout(timeout):
            async with session.get(url) as response:
                return await response.json()

# Sleep (non-blocking)
async def delayed_task():
    await asyncio.sleep(1)  # Doesn't block other tasks
    return "Done"
```

---

## 📋 Installation Cheatsheet

```bash
# Basic libraries
pip install requests pandas numpy matplotlib

# Web development
pip install fastapi uvicorn flask

# Data validation & config
pip install pydantic python-dotenv

# Testing
pip install pytest pytest-cov

# Database
pip install sqlalchemy

# Async
pip install aiohttp

# All at once (requirements.txt)
pip freeze > requirements.txt
pip install -r requirements.txt
```

---

## 🔗 Related Topics

- [[11_Standard_Library|Standard Library]]
- [[08_Unit_Testing|Unit Testing]]
- [[24_Pandas_Basics|Pandas Basics]]
- [[25_Python_Web_Flask|Flask Web]]

---

[[00_Index|← Back to Index]]

*These libraries are your toolkit for real projects! 🛠️*
