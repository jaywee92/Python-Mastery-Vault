---
title: Python Web - Flask Basics
tags: [python, flask, web, api, server, advanced]
category: advanced
type: topic
---

# 38. Python Web - Flask Basics

[[00_Index|← Back to Index]]

> **Build web applications with Flask**

---

## 🌐 What is Flask?

**Flask** is a lightweight web framework for Python. It's:
- ✓ Simple and easy to learn
- ✓ Flexible and extensible
- ✓ Great for APIs and small applications
- ✓ "Micro" framework (minimal core)

### Install Flask

```bash
pip install flask
```

---

## 🚀 Your First Flask App

### Minimal Application

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

**Run it:**
```bash
python app.py
```

**Visit:** http://127.0.0.1:5000/

---

## 🛤️ Routes and Views

### Multiple Routes

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact')
def contact():
    return 'Contact Page'
```

### Dynamic Routes

```python
@app.route('/user/<username>')
def show_user(username):
    return f'Hello, {username}!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

# Visit: /user/Alice → "Hello, Alice!"
# Visit: /post/123 → "Post ID: 123"
```

### HTTP Methods

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Processing login...'
    return 'Login page'

# GET only (default)
@app.route('/data')
def get_data():
    return 'GET request'

# POST only
@app.route('/submit', methods=['POST'])
def submit():
    return 'POST received'
```

---

## 📄 Templates (HTML)

### Using Templates

**app.py:**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username=name)
```

**templates/index.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to Flask!</h1>
    <p>This is the home page.</p>
</body>
</html>
```

**templates/user.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>User Profile</title>
</head>
<body>
    <h1>Hello, {{ username }}!</h1>
</body>
</html>
```

### Template Variables

```python
@app.route('/profile')
def profile():
    user = {
        'name': 'Alice',
        'age': 25,
        'city': 'NYC'
    }
    return render_template('profile.html', user=user)
```

**templates/profile.html:**
```html
<h1>{{ user.name }}</h1>
<p>Age: {{ user.age }}</p>
<p>City: {{ user.city }}</p>
```

### Template Loops

```python
@app.route('/users')
def users():
    users = ['Alice', 'Bob', 'Charlie']
    return render_template('users.html', users=users)
```

**templates/users.html:**
```html
<h1>Users</h1>
<ul>
{% for user in users %}
    <li>{{ user }}</li>
{% endfor %}
</ul>
```

### Template Conditionals

```html
{% if user.age >= 18 %}
    <p>Adult user</p>
{% else %}
    <p>Minor user</p>
{% endif %}
```

---

## 📥 Forms and Data

### Getting Form Data

```python
from flask import Flask, request

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f'Received: {name}, {email}'
    
    return '''
        <form method="post">
            <input name="name" placeholder="Name">
            <input name="email" placeholder="Email">
            <button type="submit">Submit</button>
        </form>
    '''
```

### Query Parameters

```python
@app.route('/search')
def search():
    # /search?q=python&page=1
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    return f'Searching for: {query}, Page: {page}'
```

### JSON Data

```python
from flask import jsonify, request

@app.route('/api/data', methods=['POST'])
def receive_json():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    return jsonify({
        'message': 'Data received',
        'name': name,
        'age': age
    })
```

---

## 🔄 Building a Simple API

### REST API Example

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]

# GET all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET single user
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

# POST new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT update user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user)

# DELETE user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```

**Test with curl:**
```bash
# GET all users
curl http://localhost:5000/api/users

# GET single user
curl http://localhost:5000/api/users/1

# POST new user
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Charlie","email":"charlie@example.com"}'

# PUT update user
curl -X PUT http://localhost:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice Updated"}'

# DELETE user
curl -X DELETE http://localhost:5000/api/users/1
```

---

## 🎨 Static Files

### Serving Static Files

**Project structure:**
```
myapp/
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── style.css
    ├── script.js
    └── logo.png
```

**In HTML:**
```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<script src="{{ url_for('static', filename='script.js') }}"></script>
<img src="{{ url_for('static', filename='logo.png') }}">
```

---

## 🔗 Redirects and URLs

### Redirects

```python
from flask import redirect, url_for

@app.route('/old-page')
def old_page():
    return redirect(url_for('new_page'))

@app.route('/new-page')
def new_page():
    return 'This is the new page'

# Redirect to external URL
@app.route('/google')
def go_to_google():
    return redirect('https://www.google.com')
```

### URL Building

```python
from flask import url_for

@app.route('/')
def index():
    # Build URL for 'user' route
    user_url = url_for('user', username='Alice')
    return f'User URL: {user_url}'
```

---

## 🍪 Sessions

### Using Sessions

```python
from flask import session

app.secret_key = 'your-secret-key-here'  # Required for sessions

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        return f'Logged in as: {username}'
    return 'Not logged in'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'Logged out'
```

---

## ⚙️ Configuration

### Basic Configuration

```python
app = Flask(__name__)

# Configuration
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['DATABASE'] = 'database.db'

# From file
app.config.from_file('config.json', load=json.load)

# From environment
app.config.from_prefixed_env()
```

---

## 💡 Best Practices

### 1. Use Blueprint for Large Apps

```python
from flask import Blueprint

# Create blueprint
api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/users')
def users():
    return 'API Users'

# Register in main app
app.register_blueprint(api)
```

### 2. Error Handling

```python
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
```

### 3. Environment Variables

```python
import os

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['DEBUG'] = os.environ.get('DEBUG', 'False') == 'True'
```

### 4. Don't Use Debug in Production

```python
if __name__ == '__main__':
    # Development only!
    app.run(debug=True)
    
    # Production: use WSGI server like Gunicorn
    # gunicorn app:app
```

---

## 🎓 Summary

**Flask Essentials:**
- `@app.route()` = Define routes
- `render_template()` = Serve HTML
- `request` = Get form/JSON data
- `jsonify()` = Return JSON
- `redirect()` = Redirect users
- `session` = Store user data

**Key Takeaway:** Flask makes web development in Python simple and fun!

---

## 🔗 Related Topics

- [[33_Package_Manager|Package Manager]]
- [[16_Working_with_JSON|JSON]]
- [[34_Web_Scraping|Web Scraping]]

---

[[00_Index|← Back to Index]]

*Build web apps with Python! 🌐*
