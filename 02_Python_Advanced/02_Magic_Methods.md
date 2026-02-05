---
title: Magic Methods (Dunder Methods)
tags: [python, oop, magic-methods, dunder, operators, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# ✨ Magic Methods (Dunder Methods)

[[00_Index|← Back to Index]] | [[11_A_OOP_Visual_Guide|OOP Visual Guide →]]

> **Customize the behavior of your classes with special methods**

---

## 🎯 What are Magic Methods?

**Magic Methods** (also **Dunder Methods** = "Double Underscore") are special methods with `__name__` syntax that Python calls automatically.

```python
# When you write...           # Python calls:
obj = MyClass()              # MyClass.__new__() + __init__()
print(obj)                   # obj.__str__()
len(obj)                     # obj.__len__()
obj[0]                       # obj.__getitem__(0)
obj + other                  # obj.__add__(other)
obj == other                 # obj.__eq__(other)
for item in obj:             # obj.__iter__()
with obj as x:               # obj.__enter__() / __exit__()
```

---

## 📦 Object Lifecycle

### __init__ and __new__

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        """Creates the instance (rarely overridden)"""
        print(f"__new__ called for {cls}")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        """Initializes the instance (often used)"""
        print(f"__init__ called with {value}")
        self.value = value

    def __del__(self):
        """Called when object is deleted (rarely needed)"""
        print(f"__del__ called, value was {self.value}")


obj = MyClass(42)
# Output:
# __new__ called for <class 'MyClass'>
# __init__ called with 42

del obj
# Output: __del__ called, value was 42
```

**Remember:**
- `__new__` creates the object (allocates memory)
- `__init__` initializes the object (sets attributes)
- `__del__` cleans up (destructor, rarely needed)

---

## 🖨️ String Representation

### __str__ vs __repr__

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Human-readable representation (print, str())"""
        return f"Point at ({self.x}, {self.y})"

    def __repr__(self):
        """For developers/debugging, should be valid Python code"""
        return f"Point({self.x}, {self.y})"


p = Point(3, 4)

print(p)           # "Point at (3, 4)" → __str__
print(str(p))      # "Point at (3, 4)" → __str__
print(repr(p))     # "Point(3, 4)" → __repr__
print(f"{p}")      # "Point at (3, 4)" → __str__
print(f"{p!r}")    # "Point(3, 4)" → __repr__

# In the REPL/Debugger:
>>> p
Point(3, 4)        # → __repr__

# In lists:
>>> [p, Point(1, 2)]
[Point(3, 4), Point(1, 2)]  # → __repr__ for each element
```

**Best Practice:**
```python
def __repr__(self):
    # Should be eval-able if possible
    return f"{self.__class__.__name__}({self.x!r}, {self.y!r})"

# So that this works:
p = Point(3, 4)
p_copy = eval(repr(p))  # Creates new Point(3, 4)
```

---

## 🔢 Comparison Operators

```python
class Money:
    def __init__(self, amount, currency="EUR"):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        """== operator"""
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __ne__(self, other):
        """!= operator (often auto-derived from __eq__)"""
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        """< operator"""
        if not isinstance(other, Money) or self.currency != other.currency:
            return NotImplemented
        return self.amount < other.amount

    def __le__(self, other):
        """<= operator"""
        return self == other or self < other

    def __gt__(self, other):
        """> operator"""
        if not isinstance(other, Money) or self.currency != other.currency:
            return NotImplemented
        return self.amount > other.amount

    def __ge__(self, other):
        """>= operator"""
        return self == other or self > other

    def __repr__(self):
        return f"Money({self.amount}, '{self.currency}')"


# Usage
m1 = Money(100)
m2 = Money(200)
m3 = Money(100)

print(m1 == m3)  # True
print(m1 < m2)   # True
print(m2 >= m1)  # True

# Sorting works automatically:
prices = [Money(300), Money(100), Money(200)]
print(sorted(prices))  # [Money(100), Money(200), Money(300)]
```

### @total_ordering Shortcut

```python
from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    # __le__, __gt__, __ge__ are auto-generated!
```

---

## ➕ Arithmetic Operators

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """self + other"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __radd__(self, other):
        """other + self (if other is not a Vector)"""
        return self.__add__(other)

    def __iadd__(self, other):
        """self += other (in-place)"""
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            return self
        return NotImplemented

    def __sub__(self, other):
        """self - other"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar):
        """self * scalar (scalar multiplication)"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __rmul__(self, scalar):
        """scalar * self"""
        return self.__mul__(scalar)

    def __neg__(self):
        """-self (negation)"""
        return Vector(-self.x, -self.y)

    def __abs__(self):
        """abs(self) (magnitude/length)"""
        return (self.x**2 + self.y**2) ** 0.5

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Usage
v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)     # Vector(4, 6)
print(v2 - v1)     # Vector(2, 2)
print(v1 * 3)      # Vector(3, 6)
print(3 * v1)      # Vector(3, 6) → __rmul__
print(-v1)         # Vector(-1, -2)
print(abs(v2))     # 5.0

v1 += v2
print(v1)          # Vector(4, 6)
```

### Vollständige Operator-Tabelle

| Operator | Method | Reverse | In-Place |
|----------|--------|---------|----------|
| `+` | `__add__` | `__radd__` | `__iadd__` |
| `-` | `__sub__` | `__rsub__` | `__isub__` |
| `*` | `__mul__` | `__rmul__` | `__imul__` |
| `/` | `__truediv__` | `__rtruediv__` | `__itruediv__` |
| `//` | `__floordiv__` | `__rfloordiv__` | `__ifloordiv__` |
| `%` | `__mod__` | `__rmod__` | `__imod__` |
| `**` | `__pow__` | `__rpow__` | `__ipow__` |

---

## 📋 Container Methods

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    def __len__(self):
        """len(playlist)"""
        return len(self._songs)

    def __getitem__(self, index):
        """playlist[index] or playlist[start:stop]"""
        return self._songs[index]

    def __setitem__(self, index, value):
        """playlist[index] = value"""
        self._songs[index] = value

    def __delitem__(self, index):
        """del playlist[index]"""
        del self._songs[index]

    def __contains__(self, item):
        """item in playlist"""
        return item in self._songs

    def __iter__(self):
        """for song in playlist:"""
        return iter(self._songs)

    def __reversed__(self):
        """reversed(playlist)"""
        return reversed(self._songs)

    def append(self, song):
        self._songs.append(song)

    def __repr__(self):
        return f"Playlist('{self.name}', songs={self._songs})"


# Usage
playlist = Playlist("My Mix")
playlist.append("Song A")
playlist.append("Song B")
playlist.append("Song C")

print(len(playlist))           # 3
print(playlist[0])             # "Song A"
print(playlist[-1])            # "Song C"
print(playlist[0:2])           # ["Song A", "Song B"]
print("Song B" in playlist)    # True

playlist[1] = "Song B (Remix)"
print(playlist[1])             # "Song B (Remix)"

for song in playlist:
    print(f"Playing: {song}")

for song in reversed(playlist):
    print(f"Reverse: {song}")
```

---

## 🔑 Attribute Access

```python
class SmartDict:
    def __init__(self, **kwargs):
        self._data = kwargs

    def __getattr__(self, name):
        """obj.name if name doesn't exist"""
        try:
            return self._data[name]
        except KeyError:
            raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")

    def __setattr__(self, name, value):
        """obj.name = value"""
        if name.startswith('_'):
            # Set internal attributes normally
            super().__setattr__(name, value)
        else:
            # Store others in _data
            self._data[name] = value

    def __delattr__(self, name):
        """del obj.name"""
        if name in self._data:
            del self._data[name]
        else:
            raise AttributeError(f"'{name}' not found")

    def __repr__(self):
        return f"SmartDict({self._data})"


# Usage
config = SmartDict(host="localhost", port=8080)

print(config.host)    # "localhost" → __getattr__
print(config.port)    # 8080

config.debug = True   # __setattr__
print(config.debug)   # True

del config.debug      # __delattr__
# print(config.debug) # AttributeError
```

### __getattribute__ vs __getattr__

```python
class Demo:
    def __init__(self):
        self.x = 10

    def __getattribute__(self, name):
        """ALWAYS called (before attribute lookup)"""
        print(f"__getattribute__: {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        """Only called if attribute NOT found"""
        print(f"__getattr__: {name}")
        return f"Default for {name}"


d = Demo()
print(d.x)        # __getattribute__: x → 10
print(d.unknown)  # __getattribute__: unknown → __getattr__: unknown → "Default for unknown"
```

---

## 📞 Callable Objects

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        """Makes object callable like a function"""
        return value * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

# Useful for closures with state
print(callable(double))  # True
```

### Practical Example: Caching Decorator

```python
class Memoize:
    """Decorator class with cache"""

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]


@Memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(100))  # Fast through caching!
```

---

## 🚪 Context Manager Methods

```python
class Timer:
    def __enter__(self):
        """When entering the 'with' block"""
        import time
        self.start = time.time()
        print("Timer started")
        return self  # Bound to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        """When exiting the 'with' block"""
        import time
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"Timer stopped: {self.elapsed:.4f} seconds")

        # Return True to suppress exceptions
        # Return False/None to propagate exceptions
        return False


# Usage
with Timer() as t:
    # Code to be measured
    total = sum(range(1000000))

print(f"Elapsed: {t.elapsed}")

# Output:
# Timer started
# Timer stopped: 0.0234 seconds
# Elapsed: 0.0234...
```

---

## 🔢 Numeric Conversions

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __int__(self):
        """int(temp)"""
        return int(self.celsius)

    def __float__(self):
        """float(temp)"""
        return float(self.celsius)

    def __bool__(self):
        """bool(temp) - also for if temp:"""
        return self.celsius != 0

    def __round__(self, ndigits=None):
        """round(temp, ndigits)"""
        return round(self.celsius, ndigits)

    def __repr__(self):
        return f"Temperature({self.celsius}°C)"


temp = Temperature(23.7)

print(int(temp))        # 23
print(float(temp))      # 23.7
print(bool(temp))       # True
print(round(temp, 1))   # 23.7
print(round(temp))      # 24

if temp:
    print("Temperature is non-zero")
```

---

## 🔒 Hash and Equality

For sets and dict keys you need `__hash__` and `__eq__`:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        """Must be consistent with __eq__!"""
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# Now Points can be used in sets and as dict keys
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)         # True
print(hash(p1) == hash(p2))  # True (must be true if p1 == p2!)

# In set
points = {p1, p2, p3}
print(len(points))      # 2 (p1 and p2 are "equal")

# As dict key
distances = {p1: 2.236, p3: 5.0}
print(distances[p2])    # 2.236 (p2 == p1)
```

**Important:**
- If `__eq__` is defined → `__hash__` becomes `None` automatically (unhashable)
- For hashable objects: `__hash__` must be consistent with `__eq__`
- Mutable objects should not be hashable!

---

## 📋 Most Important Magic Methods Overview

| Category | Methods |
|-----------|----------|
| **Lifecycle** | `__new__`, `__init__`, `__del__` |
| **String** | `__str__`, `__repr__`, `__format__` |
| **Comparison** | `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__` |
| **Arithmetic** | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__neg__`, `__abs__` |
| **Container** | `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__` |
| **Attribute** | `__getattr__`, `__setattr__`, `__delattr__`, `__getattribute__` |
| **Callable** | `__call__` |
| **Context** | `__enter__`, `__exit__` |
| **Conversion** | `__int__`, `__float__`, `__bool__`, `__hash__` |

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| `__repr__` should be eval-able | Define `__str__` without `__repr__` |
| Return `NotImplemented` for wrong types | Throw `TypeError` in operators |
| Use `@total_ordering` for comparisons | Manually code all 6 comparison operators |
| Keep `__hash__` consistent with `__eq__` | Make mutable objects hashable |
| Add docstrings to magic methods | Magic methods without clear purpose |

---

## 🎯 Exam Checklist

- [ ] `__str__` vs `__repr__` difference
- [ ] Relationship between `__eq__` and `__hash__`
- [ ] Name at least 3 arithmetic dunders
- [ ] `__getitem__` for index access
- [ ] `__call__` for callable objects
- [ ] `__enter__`/`__exit__` for context managers

---

[[12_Inheritance|← Inheritance]] | [[00_Index|Index]] | [[14_Properties_and_Class_Methods|Properties →]]
