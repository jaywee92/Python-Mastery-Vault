---
title: Pandas Basics
tags: [python, pandas, dataframe, data-analysis, csv, advanced]
category: advanced
type: topic
---

# 37. Pandas Basics

[[00_Index|← Back to Index]]

> **Powerful data analysis with pandas DataFrames**

---

## 📊 What is Pandas?

**Pandas** is Python's premier data analysis library. It provides:
- **DataFrame** - 2D table structure (like Excel)
- **Series** - 1D array (like a column)
- Data manipulation tools
- File I/O (CSV, Excel, JSON)

### Install Pandas

```bash
pip install pandas
```

---

## 🎯 Core Concepts

### Series - 1D Data

```python
import pandas as pd

# Create Series from list
s = pd.Series([1, 2, 3, 4, 5])
print(s)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# Create with custom index
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
# a    10
# b    20
# c    30
# dtype: int64

# Access values
print(s['a'])  # 10
print(s[0])    # 10
```

### DataFrame - 2D Data

```python
# Create DataFrame from dictionary
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

---

## 📥 Reading Data

### From CSV

```python
# Read CSV file
df = pd.read_csv('data.csv')

# With custom separator
df = pd.read_csv('data.tsv', sep='\t')

# Select specific columns
df = pd.read_csv('data.csv', usecols=['name', 'age'])

# Skip rows
df = pd.read_csv('data.csv', skiprows=1)
```

### From Excel

```python
# Read Excel file
df = pd.read_excel('data.xlsx')

# Specific sheet
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
```

### From JSON

```python
# Read JSON file
df = pd.read_json('data.json')

# From JSON string
json_str = '[{"name":"Alice","age":25},{"name":"Bob","age":30}]'
df = pd.read_json(json_str)
```

### From Dictionary

```python
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)
```

---

## 🔍 Exploring Data

### Basic Info

```python
# First rows
print(df.head())     # First 5 rows
print(df.head(10))   # First 10 rows

# Last rows
print(df.tail())     # Last 5 rows

# Shape (rows, columns)
print(df.shape)      # (3, 3)

# Column names
print(df.columns)    # Index(['name', 'age', 'salary'])

# Data types
print(df.dtypes)
# name      object
# age        int64
# salary     int64

# Summary statistics
print(df.describe())
#              age        salary
# count   3.000000      3.000000
# mean   30.000000  60000.000000
# std     5.000000  10000.000000
# min    25.000000  50000.000000
# 25%    27.500000  55000.000000
# 50%    30.000000  60000.000000
# 75%    32.500000  65000.000000
# max    35.000000  70000.000000

# Info about DataFrame
df.info()
```

---

## 📌 Selecting Data

### Select Columns

```python
# Single column (returns Series)
names = df['name']

# Multiple columns (returns DataFrame)
subset = df[['name', 'age']]

# Using dot notation
names = df.name  # Works if column name is valid Python identifier
```

### Select Rows

```python
# By position (iloc)
first_row = df.iloc[0]      # First row
first_3 = df.iloc[:3]       # First 3 rows
last_row = df.iloc[-1]      # Last row

# By label (loc)
df_with_index = df.set_index('name')
alice = df_with_index.loc['Alice']

# Boolean indexing
adults = df[df['age'] > 25]
young_rich = df[(df['age'] < 30) & (df['salary'] > 55000)]
```

### Select Specific Cells

```python
# Single value
value = df.loc[0, 'name']      # 'Alice'
value = df.iloc[0, 0]          # 'Alice'

# Range
subset = df.loc[0:2, ['name', 'age']]
subset = df.iloc[0:2, 0:2]
```

---

## ✏️ Modifying Data

### Add Column

```python
# New column with same value
df['country'] = 'USA'

# New column from calculation
df['age_in_10'] = df['age'] + 10

# New column from function
df['senior'] = df['age'] > 30
```

### Modify Values

```python
# Modify single value
df.loc[0, 'age'] = 26

# Modify column
df['age'] = df['age'] + 1

# Conditional update
df.loc[df['age'] > 30, 'senior'] = True
```

### Rename Columns

```python
# Rename specific columns
df = df.rename(columns={'name': 'full_name', 'age': 'years'})

# Rename all columns
df.columns = ['col1', 'col2', 'col3']
```

### Drop Columns/Rows

```python
# Drop column
df = df.drop('salary', axis=1)
df = df.drop(columns=['salary'])

# Drop row
df = df.drop(0, axis=0)  # Drop row at index 0
df = df.drop(index=[0, 1])  # Drop multiple rows

# Drop in place
df.drop('salary', axis=1, inplace=True)
```

---

## 🔧 Data Cleaning

### Handle Missing Values

```python
# Check for missing values
print(df.isnull())
print(df.isnull().sum())  # Count per column

# Drop rows with any NaN
df = df.dropna()

# Drop rows where specific column is NaN
df = df.dropna(subset=['age'])

# Fill missing values
df = df.fillna(0)  # Fill with 0
df['age'] = df['age'].fillna(df['age'].mean())  # Fill with mean

# Forward fill
df = df.fillna(method='ffill')

# Backward fill
df = df.fillna(method='bfill')
```

### Remove Duplicates

```python
# Check for duplicates
print(df.duplicated())

# Drop duplicates
df = df.drop_duplicates()

# Drop based on specific columns
df = df.drop_duplicates(subset=['name'])
```

### Change Data Types

```python
# Convert column type
df['age'] = df['age'].astype(int)
df['salary'] = df['salary'].astype(float)

# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Convert to category
df['city'] = df['city'].astype('category')
```

---

## 📊 Grouping and Aggregation

### GroupBy

```python
# Group by single column
grouped = df.groupby('city')

# Get group
nyc_group = grouped.get_group('NYC')

# Aggregate
avg_age = df.groupby('city')['age'].mean()
total_salary = df.groupby('city')['salary'].sum()

# Multiple aggregations
stats = df.groupby('city').agg({
    'age': ['mean', 'min', 'max'],
    'salary': ['sum', 'mean']
})
```

### Common Aggregations

```python
# Sum
df['salary'].sum()

# Mean
df['age'].mean()

# Median
df['age'].median()

# Count
df['name'].count()

# Min/Max
df['age'].min()
df['age'].max()

# Standard deviation
df['salary'].std()

# Value counts
df['city'].value_counts()
```

---

## 🔗 Merging DataFrames

### Concatenate

```python
# Vertical concatenation (stack)
df3 = pd.concat([df1, df2], axis=0)

# Horizontal concatenation (side by side)
df3 = pd.concat([df1, df2], axis=1)

# Ignore index
df3 = pd.concat([df1, df2], ignore_index=True)
```

### Merge (SQL-like JOIN)

```python
# Inner join
merged = pd.merge(df1, df2, on='id')

# Left join
merged = pd.merge(df1, df2, on='id', how='left')

# Right join
merged = pd.merge(df1, df2, on='id', how='right')

# Outer join
merged = pd.merge(df1, df2, on='id', how='outer')

# Multiple keys
merged = pd.merge(df1, df2, on=['id', 'date'])
```

---

## 💾 Saving Data

### To CSV

```python
# Save to CSV
df.to_csv('output.csv', index=False)

# With specific encoding
df.to_csv('output.csv', encoding='utf-8')

# Custom separator
df.to_csv('output.tsv', sep='\t')
```

### To Excel

```python
# Save to Excel
df.to_excel('output.xlsx', index=False)

# Multiple sheets
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')
```

### To JSON

```python
# Save to JSON
df.to_json('output.json')

# Orient records
df.to_json('output.json', orient='records')
```

---

## 📈 Practical Example

```python
import pandas as pd

# Create sample data
data = {
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop'],
    'price': [1200, 25, 75, 300, 1100],
    'quantity': [5, 50, 30, 10, 8],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics']
}

df = pd.DataFrame(data)

# Add total column
df['total'] = df['price'] * df['quantity']

# Group by category
category_stats = df.groupby('category').agg({
    'total': 'sum',
    'quantity': 'sum',
    'price': 'mean'
})

print(category_stats)
#                  total  quantity   price
# category                                
# Accessories      3250       80   50.00
# Electronics     14500       23  866.67

# Find expensive products
expensive = df[df['price'] > 100]

# Sort by total
sorted_df = df.sort_values('total', ascending=False)

print(sorted_df)
```

---

## 💡 Best Practices

### 1. Use Appropriate Data Types

```python
# Convert to category for memory efficiency
df['city'] = df['city'].astype('category')
```

### 2. Chain Operations

```python
# Good - readable chain
result = (df
    .dropna()
    .groupby('city')
    .agg({'age': 'mean'})
    .sort_values('age', ascending=False)
)
```

### 3. Use `inplace=False` (default)

```python
# Better - explicit
df_clean = df.dropna()

# Avoid unless necessary
df.dropna(inplace=True)
```

### 4. Check Data After Loading

```python
# Always inspect after reading
df = pd.read_csv('data.csv')
print(df.head())
print(df.info())
print(df.describe())
```

---

## 🎓 Summary

**Pandas Essentials:**
- **DataFrame** = 2D table
- **Series** = 1D array
- `read_csv/excel/json` = Load data
- `head/tail/describe` = Explore
- `loc/iloc/[]` = Select
- `groupby/agg` = Analyze
- `to_csv/excel/json` = Save

**Key Takeaway:** Pandas makes data analysis in Python fast and intuitive!

---

## 🔗 Related Topics

- [[36_Statistics|Statistics]]
- [[16_Working_with_JSON|JSON]]
- [[15_File_IO|File I/O]]

---

[[00_Index|← Back to Index]]

*Data analysis made easy! 🐼*
