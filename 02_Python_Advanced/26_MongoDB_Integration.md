---
title: MongoDB Integration
tags: [python, mongodb, database, nosql, pymongo, advanced]
category: advanced
type: topic
---

# 39. MongoDB Integration

[[00_Index|← Back to Index]]

> **Work with MongoDB databases in Python**

---

## 🗄️ What is MongoDB?

**MongoDB** is a NoSQL database that stores data in JSON-like documents.

**Key Features:**
- ✓ Flexible schema
- ✓ Document-based (JSON)
- ✓ Scalable
- ✓ Fast queries

**SQL vs NoSQL:**

| SQL (MySQL) | NoSQL (MongoDB) |
|-------------|-----------------|
| Tables | Collections |
| Rows | Documents |
| Columns | Fields |
| Fixed schema | Flexible schema |

---

## 🚀 Setup

### Install MongoDB

**Option 1:** Download from mongodb.com

**Option 2:** Use MongoDB Atlas (Cloud)
- Free tier available
- No local installation needed
- Visit: https://www.mongodb.com/atlas

### Install PyMongo

```bash
pip install pymongo
```

---

## 🔗 Connecting to MongoDB

### Local Connection

```python
from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Or simply
client = MongoClient()

# Check connection
print(client.list_database_names())
```

### MongoDB Atlas Connection

```python
from pymongo import MongoClient

# Connection string from Atlas
uri = "mongodb+srv://username:password@cluster.mongodb.net/"

client = MongoClient(uri)

# Test connection
try:
    client.admin.command('ping')
    print("Connected successfully!")
except Exception as e:
    print(f"Connection failed: {e}")
```

---

## 🗂️ Database and Collections

### Create/Access Database

```python
# Access (creates if doesn't exist)
db = client['myapp_database']

# Or using dot notation
db = client.myapp_database
```

### Create/Access Collection

```python
# Access collection (creates if doesn't exist)
users = db['users']

# Or
users = db.users

# List all collections
print(db.list_collection_names())
```

---

## ➕ Insert Documents

### Insert One

```python
# Document (dictionary)
user = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'age': 25,
    'city': 'NYC'
}

# Insert
result = users.insert_one(user)
print(f"Inserted ID: {result.inserted_id}")
```

### Insert Many

```python
# Multiple documents
new_users = [
    {'name': 'Bob', 'age': 30, 'city': 'LA'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
    {'name': 'David', 'age': 28, 'city': 'NYC'}
]

result = users.insert_many(new_users)
print(f"Inserted {len(result.inserted_ids)} documents")
```

---

## 🔍 Query Documents

### Find All

```python
# Get all documents
for user in users.find():
    print(user)

# Get as list
all_users = list(users.find())
```

### Find One

```python
# Find first matching document
user = users.find_one({'name': 'Alice'})
print(user)

# Find by ID
from bson import ObjectId
user = users.find_one({'_id': ObjectId('...')})
```

### Query with Conditions

```python
# Equal
young = users.find({'age': 25})

# Greater than
adults = users.find({'age': {'$gt': 30}})

# Less than or equal
users_lte_30 = users.find({'age': {'$lte': 30}})

# In list
cities = users.find({'city': {'$in': ['NYC', 'LA']}})

# AND condition
nyc_young = users.find({'city': 'NYC', 'age': {'$lt': 30}})

# OR condition
result = users.find({
    '$or': [
        {'age': {'$lt': 25}},
        {'city': 'NYC'}
    ]
})

# NOT
not_nyc = users.find({'city': {'$ne': 'NYC'}})

# Exists
has_email = users.find({'email': {'$exists': True}})
```

### Projection (Select Fields)

```python
# Only return specific fields
result = users.find({}, {'name': 1, 'age': 1, '_id': 0})

for user in result:
    print(user)  # Only name and age
```

### Sort and Limit

```python
# Sort ascending
sorted_users = users.find().sort('age', 1)

# Sort descending
sorted_desc = users.find().sort('age', -1)

# Limit results
top_5 = users.find().limit(5)

# Skip and limit (pagination)
page_2 = users.find().skip(10).limit(10)

# Combined
young_sorted = users.find({'age': {'$lt': 30}}).sort('name', 1).limit(5)
```

### Count

```python
# Count all documents
total = users.count_documents({})
print(f"Total users: {total}")

# Count with filter
nyc_count = users.count_documents({'city': 'NYC'})
print(f"NYC users: {nyc_count}")
```

---

## ✏️ Update Documents

### Update One

```python
# Update single document
users.update_one(
    {'name': 'Alice'},  # Filter
    {'$set': {'age': 26}}  # Update
)

# Increment value
users.update_one(
    {'name': 'Bob'},
    {'$inc': {'age': 1}}  # age = age + 1
)

# Add to array
users.update_one(
    {'name': 'Alice'},
    {'$push': {'hobbies': 'reading'}}
)
```

### Update Many

```python
# Update all matching documents
users.update_many(
    {'city': 'NYC'},
    {'$set': {'country': 'USA'}}
)

# Update all documents
users.update_many(
    {},  # Empty filter = all
    {'$set': {'verified': False}}
)
```

### Replace One

```python
# Replace entire document
new_data = {
    'name': 'Alice',
    'email': 'newemail@example.com',
    'age': 26
}

users.replace_one(
    {'name': 'Alice'},
    new_data
)
```

---

## 🗑️ Delete Documents

### Delete One

```python
# Delete single document
users.delete_one({'name': 'Bob'})

# Delete by ID
users.delete_one({'_id': ObjectId('...')})
```

### Delete Many

```python
# Delete all matching
users.delete_many({'city': 'Chicago'})

# Delete all documents
users.delete_many({})
```

---

## 💾 Practical Example: Blog System

```python
from pymongo import MongoClient
from datetime import datetime

# Connect
client = MongoClient('mongodb://localhost:27017/')
db = client['blog_db']
posts = db['posts']
comments = db['comments']

# Create post
post = {
    'title': 'Getting Started with MongoDB',
    'author': 'Alice',
    'content': 'MongoDB is a great NoSQL database...',
    'tags': ['mongodb', 'database', 'nosql'],
    'created_at': datetime.now(),
    'views': 0,
    'likes': []
}

post_id = posts.insert_one(post).inserted_id
print(f"Post created with ID: {post_id}")

# Add comment
comment = {
    'post_id': post_id,
    'author': 'Bob',
    'text': 'Great post!',
    'created_at': datetime.now()
}

comments.insert_one(comment)

# Increment views
posts.update_one(
    {'_id': post_id},
    {'$inc': {'views': 1}}
)

# Add like
posts.update_one(
    {'_id': post_id},
    {'$addToSet': {'likes': 'Charlie'}}  # addToSet prevents duplicates
)

# Find post with comments
post_data = posts.find_one({'_id': post_id})
post_comments = list(comments.find({'post_id': post_id}))

print(f"Post: {post_data['title']}")
print(f"Views: {post_data['views']}")
print(f"Likes: {len(post_data['likes'])}")
print(f"Comments: {len(post_comments)}")

# Get popular posts
popular = posts.find({'views': {'$gt': 100}}).sort('views', -1).limit(10)
```

---

## 🔍 Aggregation Pipeline

### Basic Aggregation

```python
# Group and count
pipeline = [
    {'$group': {
        '_id': '$city',
        'count': {'$sum': 1},
        'avg_age': {'$avg': '$age'}
    }}
]

result = users.aggregate(pipeline)
for doc in result:
    print(doc)
```

### Complex Pipeline

```python
# Match -> Group -> Sort
pipeline = [
    # Stage 1: Filter
    {'$match': {'age': {'$gte': 25}}},
    
    # Stage 2: Group
    {'$group': {
        '_id': '$city',
        'total': {'$sum': 1},
        'avg_age': {'$avg': '$age'}
    }},
    
    # Stage 3: Sort
    {'$sort': {'total': -1}}
]

result = users.aggregate(pipeline)
```

---

## 🔒 Indexes

### Create Index

```python
# Single field index
users.create_index('email')

# Compound index
users.create_index([('city', 1), ('age', -1)])

# Unique index
users.create_index('email', unique=True)

# Text index (for text search)
posts.create_index([('title', 'text'), ('content', 'text')])
```

### List Indexes

```python
# Get all indexes
indexes = users.list_indexes()
for index in indexes:
    print(index)
```

---

## 💡 Best Practices

### 1. Close Connections

```python
try:
    # Your code
    pass
finally:
    client.close()

# Or use context manager (if supported)
```

### 2. Handle Errors

```python
from pymongo.errors import DuplicateKeyError

try:
    users.insert_one({'email': 'duplicate@example.com'})
except DuplicateKeyError:
    print("Email already exists")
```

### 3. Use Indexes

```python
# Create indexes for frequently queried fields
users.create_index('email')
posts.create_index('created_at')
```

### 4. Validate Data

```python
def create_user(data):
    # Validate before inserting
    if 'email' not in data or 'name' not in data:
        raise ValueError("Missing required fields")
    
    if not isinstance(data['age'], int):
        raise TypeError("Age must be integer")
    
    return users.insert_one(data)
```

### 5. Use Aggregation for Complex Queries

```python
# Better than multiple queries
pipeline = [
    {'$match': {'status': 'active'}},
    {'$group': {'_id': '$category', 'total': {'$sum': 1'}}},
    {'$sort': {'total': -1}}
]

result = collection.aggregate(pipeline)
```

---

## 🎓 Summary

**MongoDB Basics:**
- `MongoClient()` = Connect
- `insert_one/many()` = Add data
- `find()` = Query data
- `update_one/many()` = Modify data
- `delete_one/many()` = Remove data
- `aggregate()` = Complex queries

**Key Takeaway:** MongoDB provides flexible, scalable document storage with powerful querying!

---

## 🔗 Related Topics

- [[16_Working_with_JSON|JSON]]
- [[37_Pandas_Basics|Pandas]]
- [[38_Python_Web_Flask|Flask]]

---

[[00_Index|← Back to Index]]

*NoSQL made simple! 🗄️*
