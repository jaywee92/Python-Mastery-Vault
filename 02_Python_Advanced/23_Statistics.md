---
title: Statistics with Python
tags: [python, statistics, data-analysis, numpy, math, advanced]
category: advanced
type: topic
---

# 36. Statistics with Python

[[00_Index|← Back to Index]]

> **Perform statistical analysis with Python**

---

## 📊 Built-in Statistics Module

Python's `statistics` module provides basic statistical functions.

### Import

```python
import statistics as stats
```

---

## 📈 Measures of Central Tendency

### Mean (Average)

```python
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

mean = stats.mean(data)
print(f'Mean: {mean}')  # 5.0
```

### Median (Middle Value)

```python
# Median - middle value
median = stats.median(data)
print(f'Median: {median}')  # 5.0

# For even number of values
even_data = [1, 2, 3, 4]
print(stats.median(even_data))  # 2.5
```

### Mode (Most Common)

```python
# Mode - most frequent value
mode = stats.mode(data)
print(f'Mode: {mode}')  # 5

# Multiple modes
multi_mode = [1, 1, 2, 2, 3]
# stats.mode(multi_mode)  # Would raise error

# Use multimode for multiple modes
modes = stats.multimode(multi_mode)
print(f'Modes: {modes}')  # [1, 2]
```

---

## 📏 Measures of Spread

### Range

```python
# Range - difference between max and min
data_range = max(data) - min(data)
print(f'Range: {data_range}')  # 8
```

### Variance

```python
# Variance - average of squared differences from mean
variance = stats.variance(data)
print(f'Variance: {variance:.2f}')  # 7.11
```

### Standard Deviation

```python
# Standard deviation - square root of variance
stdev = stats.stdev(data)
print(f'Standard Deviation: {stdev:.2f}')  # 2.67
```

---

## 📊 Practical Example: Grade Analysis

```python
grades = [85, 92, 78, 95, 88, 76, 90, 85, 82, 94]

print("=== Grade Statistics ===")
print(f"Mean: {stats.mean(grades):.1f}")
print(f"Median: {stats.median(grades):.1f}")
print(f"Mode: {stats.mode(grades)}")
print(f"Std Dev: {stats.stdev(grades):.2f}")
print(f"Highest: {max(grades)}")
print(f"Lowest: {min(grades)}")
print(f"Range: {max(grades) - min(grades)}")
```

---

## 🔢 Using NumPy for Advanced Stats

### Install NumPy

```bash
pip install numpy
```

### Import

```python
import numpy as np
```

### Descriptive Statistics

```python
data = np.array([1, 2, 3, 4, 5, 5, 6, 7, 8, 9])

print(f"Mean: {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Std Dev: {np.std(data)}")
print(f"Variance: {np.var(data)}")
print(f"Min: {np.min(data)}")
print(f"Max: {np.max(data)}")
```

### Percentiles

```python
# 25th, 50th (median), 75th percentile
percentiles = np.percentile(data, [25, 50, 75])
print(f"Quartiles: {percentiles}")

# 90th percentile
p90 = np.percentile(data, 90)
print(f"90th percentile: {p90}")
```

### Correlation

```python
# Two datasets
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Correlation coefficient
correlation = np.corrcoef(x, y)[0, 1]
print(f"Correlation: {correlation:.3f}")
```

---

## 📊 Distribution Analysis

### Normal Distribution Simulation

```python
import numpy as np

# Generate random data from normal distribution
mean = 100
std_dev = 15
size = 1000

data = np.random.normal(mean, std_dev, size)

print(f"Generated Mean: {np.mean(data):.2f}")
print(f"Generated Std Dev: {np.std(data):.2f}")
```

### Checking for Outliers

```python
def find_outliers(data):
    """Find outliers using IQR method"""
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    return outliers

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]  # 100 is outlier
outliers = find_outliers(data)
print(f"Outliers: {outliers}")
```

---

## 📈 Real-World Example: Sales Analysis

```python
import statistics as stats
import numpy as np

# Monthly sales data
sales = [45000, 52000, 48000, 61000, 55000, 58000, 
         63000, 59000, 56000, 64000, 68000, 72000]

print("=== Annual Sales Analysis ===")
print(f"Total Sales: ${sum(sales):,}")
print(f"Average Monthly: ${stats.mean(sales):,.2f}")
print(f"Median Monthly: ${stats.median(sales):,.2f}")
print(f"Best Month: ${max(sales):,}")
print(f"Worst Month: ${min(sales):,}")
print(f"Std Deviation: ${stats.stdev(sales):,.2f}")

# Growth rate
q1_avg = np.mean(sales[:3])
q4_avg = np.mean(sales[-3:])
growth = ((q4_avg - q1_avg) / q1_avg) * 100
print(f"Q1 to Q4 Growth: {growth:.1f}%")
```

---

## 🎲 Probability Basics

### Coin Flip Simulation

```python
import random

def flip_coin(n):
    """Simulate n coin flips"""
    flips = [random.choice(['H', 'T']) for _ in range(n)]
    heads = flips.count('H')
    tails = flips.count('T')
    
    print(f"Flips: {n}")
    print(f"Heads: {heads} ({heads/n*100:.1f}%)")
    print(f"Tails: {tails} ({tails/n*100:.1f}%)")

flip_coin(1000)
```

### Dice Roll Simulation

```python
def roll_dice(n, sides=6):
    """Simulate n dice rolls"""
    rolls = [random.randint(1, sides) for _ in range(n)]
    
    print(f"Rolled {n} times:")
    for i in range(1, sides + 1):
        count = rolls.count(i)
        percentage = (count / n) * 100
        print(f"{i}: {count} times ({percentage:.1f}%)")

roll_dice(1000)
```

---

## 📊 Data Summarization

```python
def summarize_data(data):
    """Print comprehensive statistics"""
    print("=== Data Summary ===")
    print(f"Count: {len(data)}")
    print(f"Sum: {sum(data):.2f}")
    print(f"Mean: {stats.mean(data):.2f}")
    print(f"Median: {stats.median(data):.2f}")
    
    try:
        print(f"Mode: {stats.mode(data):.2f}")
    except:
        print("Mode: No unique mode")
    
    print(f"Std Dev: {stats.stdev(data):.2f}")
    print(f"Variance: {stats.variance(data):.2f}")
    print(f"Min: {min(data):.2f}")
    print(f"Max: {max(data):.2f}")
    print(f"Range: {max(data) - min(data):.2f}")

# Example usage
test_scores = [78, 85, 92, 88, 76, 95, 84, 89, 91, 87]
summarize_data(test_scores)
```

---

## 💡 Best Practices

### 1. Check Data Quality

```python
def check_data(data):
    """Validate data before analysis"""
    # Remove None and NaN
    clean_data = [x for x in data if x is not None and not np.isnan(x)]
    
    if len(clean_data) == 0:
        raise ValueError("No valid data")
    
    return clean_data
```

### 2. Handle Missing Data

```python
# Option 1: Remove missing
data = [x for x in data if x is not None]

# Option 2: Replace with mean
mean_value = stats.mean([x for x in data if x is not None])
data = [x if x is not None else mean_value for x in data]

# Option 3: Replace with median (more robust)
median_value = stats.median([x for x in data if x is not None])
data = [x if x is not None else median_value for x in data]
```

### 3. Visualize Results

```python
# While statistics module doesn't do visualization,
# combine with matplotlib for plots:

import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

plt.hist(data, bins=5, edgecolor='black')
plt.axvline(stats.mean(data), color='r', label='Mean')
plt.axvline(stats.median(data), color='g', label='Median')
plt.legend()
plt.title('Data Distribution')
plt.show()
```

---

## 🎓 Summary

- **Mean** = Average value
- **Median** = Middle value
- **Mode** = Most frequent value
- **Std Dev** = Measure of spread
- **NumPy** = Advanced statistics

**Key Takeaway:** Python makes statistical analysis accessible and powerful!

---

## 🔗 Related Topics

- [[37_Pandas_Basics|Pandas Basics]]
- [[02_Lists_Deep_Dive|Lists]]

---

[[00_Index|← Back to Index]]

*Numbers tell stories! 📊✨*
