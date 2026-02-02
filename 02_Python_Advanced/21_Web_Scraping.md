---
title: Web Scraping
tags: [python, web-scraping, beautifulsoup, requests, html, advanced]
category: advanced
type: topic
---

# 34. Web Scraping

[[00_Index|← Back to Index]]

> **Extract data from websites with Python**

---

## 🌐 What is Web Scraping?

**Web scraping** is the automated process of extracting data from websites.

**Common Uses:**
- ✓ Price monitoring
- ✓ Data collection for research
- ✓ News aggregation
- ✓ Job listings
- ✓ Social media analysis

**⚠️ Legal Note:** Always check a website's `robots.txt` and Terms of Service before scraping!

---

## 🛠️ Required Packages

```bash
pip install requests
pip install beautifulsoup4
pip install lxml
```

---

## 📥 Basic Web Scraping

### Step 1: Fetch Web Page

```python
import requests

# Get webpage
url = 'https://example.com'
response = requests.get(url)

# Check if successful
if response.status_code == 200:
    html_content = response.text
    print("Page fetched successfully!")
else:
    print(f"Error: {response.status_code}")
```

### Step 2: Parse HTML

```python
from bs4 import BeautifulSoup

# Parse HTML
soup = BeautifulSoup(html_content, 'lxml')

# Get page title
title = soup.title.string
print(f"Page title: {title}")
```

---

## 🔍 Finding Elements

### By Tag Name

```python
# Find first paragraph
first_p = soup.find('p')
print(first_p.text)

# Find all paragraphs
all_paragraphs = soup.find_all('p')
for p in all_paragraphs:
    print(p.text)
```

### By Class

```python
# Find element by class
element = soup.find('div', class_='content')

# Find all elements with class
elements = soup.find_all('div', class_='item')
```

### By ID

```python
# Find element by ID
header = soup.find(id='header')
print(header.text)
```

### By CSS Selector

```python
# Select using CSS selector
items = soup.select('.product-item')
for item in items:
    print(item.text)

# Complex selector
links = soup.select('div.content a[href]')
```

---

## 📊 Practical Example: Scraping Quotes

```python
import requests
from bs4 import BeautifulSoup

# Fetch page
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# Extract quotes
quotes = []
quote_elements = soup.find_all('span', class_='text')

for quote in quote_elements:
    quotes.append(quote.text)

# Extract authors
authors = []
author_elements = soup.find_all('small', class_='author')

for author in author_elements:
    authors.append(author.text)

# Display results
for i in range(len(quotes)):
    print(f"{quotes[i]} - {authors[i]}")
```

---

## 🔗 Extracting Links

```python
# Find all links
links = soup.find_all('a')

for link in links:
    href = link.get('href')
    text = link.text
    print(f"Text: {text}, URL: {href}")

# Filter links by pattern
import re
pdf_links = soup.find_all('a', href=re.compile(r'\.pdf$'))
```

---

## 🖼️ Extracting Images

```python
# Find all images
images = soup.find_all('img')

for img in images:
    src = img.get('src')
    alt = img.get('alt', 'No alt text')
    print(f"Image: {alt}, URL: {src}")
```

---

## 📋 Extracting Tables

```python
# Find table
table = soup.find('table')

# Extract headers
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# Extract rows
rows = []
for tr in table.find_all('tr')[1:]:  # Skip header row
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    rows.append(row)

# Display as DataFrame (if pandas installed)
import pandas as pd
df = pd.DataFrame(rows, columns=headers)
print(df)
```

---

## 💾 Saving Scraped Data

### Save to CSV

```python
import csv

data = [
    ['Name', 'Price'],
    ['Product 1', '$19.99'],
    ['Product 2', '$29.99']
]

with open('products.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
```

### Save to JSON

```python
import json

data = {
    'products': [
        {'name': 'Product 1', 'price': 19.99},
        {'name': 'Product 2', 'price': 29.99}
    ]
}

with open('products.json', 'w') as f:
    json.dump(data, f, indent=2)
```

---

## 🚦 Handling Common Issues

### User-Agent Header

Some sites block requests without proper headers:

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

response = requests.get(url, headers=headers)
```

### Rate Limiting

Add delays between requests:

```python
import time

urls = ['url1', 'url2', 'url3']

for url in urls:
    response = requests.get(url)
    # Process response...
    time.sleep(2)  # Wait 2 seconds
```

### Error Handling

```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise error for bad status
    soup = BeautifulSoup(response.text, 'lxml')
except requests.exceptions.RequestException as e:
    print(f"Error fetching {url}: {e}")
```

---

## 📜 Respecting robots.txt

Check what's allowed:

```python
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('https://example.com/robots.txt')
rp.read()

# Check if URL can be scraped
can_scrape = rp.can_fetch('*', 'https://example.com/page')
print(f"Can scrape: {can_scrape}")
```

---

## 💡 Best Practices

### 1. Check Terms of Service
Always verify you're allowed to scrape the site.

### 2. Use Rate Limiting
Don't overload servers with requests.

```python
import time
time.sleep(1)  # 1 second delay
```

### 3. Handle Errors Gracefully
Sites can change structure or go down.

```python
try:
    element = soup.find('div', class_='content')
    if element:
        text = element.text
    else:
        text = "Element not found"
except AttributeError:
    text = "Parse error"
```

### 4. Cache Results
Don't re-scrape unnecessarily.

### 5. Identify Yourself
Use descriptive User-Agent.

---

## ⚠️ Legal & Ethical Considerations

- ✓ Check `robots.txt`
- ✓ Read Terms of Service
- ✓ Don't overload servers
- ✓ Respect copyright
- ✓ Consider using APIs instead

---

## 🎓 Summary

- **requests** = Fetch web pages
- **BeautifulSoup** = Parse HTML
- **find/find_all** = Extract elements
- **CSS selectors** = Advanced queries
- **Rate limiting** = Be respectful

**Key Takeaway:** Web scraping is powerful but must be done responsibly!

---

## 🔗 Related Topics

- [[33_Package_Manager|Package Manager]]
- [[15_File_IO|File I/O]]
- [[16_Working_with_JSON|JSON]]

---

[[00_Index|← Back to Index]]

*Scrape responsibly! 🌐✨*
