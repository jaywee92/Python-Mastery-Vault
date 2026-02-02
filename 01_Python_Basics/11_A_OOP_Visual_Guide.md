---
title: OOP - Visual Guide to Classes & Objects
category: oop
tags: ['python', 'classes', 'oop', 'objects', 'core']
created: 2026-01-27
type: topic
---

# 🏗️ OOP - Visual Guide to Classes & Objects

[[00_Index|← Back to Index]] | [[11_Classes_and_OOP|Classes & OOP →]]

---

## 🎯 What is a Class?

A **class** is a blueprint for creating objects. Think of it like a cookie cutter! 🍪

```
Class = Blueprint/Template
   ↓
Objects = Actual instances created from that blueprint
```

---

## 📐 Class vs Object Visualization

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
```

### Visualization:
```
┌────────────────────────────────┐
│      Dog Class (Blueprint)     │
│                                │
│  Attributes:                   │
│  • name                        │
│  • age                         │
│                                │
│  Methods:                      │
│  • bark()                      │
└────────────────────────────────┘
         │
         │ Create instances
         ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ dog1         │  │ dog2         │  │ dog3         │
│ name="Buddy" │  │ name="Max"   │  │ name="Lucy"  │
│ age=3        │  │ age=5        │  │ age=2        │
│ bark() ✓     │  │ bark() ✓     │  │ bark() ✓     │
└──────────────┘  └──────────────┘  └──────────────┘

Each object is INDEPENDENT with its OWN data!
```

---

## 🔍 Understanding `self`

`self` represents THE CURRENT INSTANCE.

```python
class Dog:
    def __init__(self, name):
        self.name = name  # THIS dog's name
    
    def bark(self):
        print(f"{self.name} says Woof!")
        #      ↑
        #      Refers to THIS dog's name

dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.bark()  # "Buddy says Woof!"
dog2.bark()  # "Max says Woof!"
```

### Visualization:
```
When dog1.bark() is called:

┌───────────────────────────────┐
│ dog1                          │
│ name = "Buddy" ◄──────────────┼── self.name refers to THIS
│                               │
│ bark() method:                │
│   print(f"{self.name} ...")   │
│              ↑                │
│              └────────────────┼── Points to dog1's name
└───────────────────────────────┘

When dog2.bark() is called:

┌───────────────────────────────┐
│ dog2                          │
│ name = "Max" ◄────────────────┼── self.name refers to THIS
│                               │
│ bark() method:                │
│   print(f"{self.name} ...")   │
│              ↑                │
│              └────────────────┼── Points to dog2's name
└───────────────────────────────┘

self = "the current object"
```

---

## 🏗️ The `__init__` Method

`__init__` is the **constructor** - it runs when you create a new object.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        print(f"Creating account for {owner}")
        self.owner = owner      # Set owner
        self.balance = balance  # Set balance

# When you create an object:
account = BankAccount("Alice", 1000)
```

### Step-by-Step Visualization:
```
Step 1: Python creates empty object
┌──────────────────┐
│ Empty Object     │
│ (no attributes)  │
└──────────────────┘

Step 2: Python calls __init__ with that object as 'self'
┌──────────────────┐
│ self             │  __init__(self, "Alice", 1000)
│                  │      ↓
│ self.owner =     │  Set attributes
│   "Alice"        │
│ self.balance =   │
│   1000           │
└──────────────────┘

Step 3: Return the initialized object
┌──────────────────┐
│ account          │
│ owner = "Alice"  │
│ balance = 1000   │
└──────────────────┘
```

---

## 📊 Instance vs Class Attributes

```python
class Dog:
    # Class attribute (shared by ALL dogs)
    species = "Canis familiaris"
    
    def __init__(self, name):
        # Instance attribute (unique to each dog)
        self.name = name
```

### Visualization:
```
┌─────────────────────────────────────────┐
│ Dog Class                               │
│                                         │
│ Class Attribute:                        │
│ species = "Canis familiaris" ◄──────────┼── Shared by all!
│                                         │
└─────────────────────────────────────────┘
    │                    │                │
    │                    │                │
    ↓                    ↓                ↓
┌──────────┐        ┌──────────┐    ┌──────────┐
│ dog1     │        │ dog2     │    │ dog3     │
│ name=    │        │ name=    │    │ name=    │
│ "Buddy"  │        │ "Max"    │    │ "Lucy"   │
│          │        │          │    │          │
│ species? │        │ species? │    │ species? │
│    ↓     │        │    ↓     │    │    ↓     │
│ looks up │        │ looks up │    │ looks up │
│ in class │        │ in class │    │ in class │
└──────────┘        └──────────┘    └──────────┘
     ↓                   ↓                ↓
     └───────────────────┴────────────────┘
                    │
                    ↓
         All find: "Canis familiaris"

Instance attributes: unique per object
Class attributes: shared by all objects
```

---

## 🎨 Methods Explained

```python
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, n):
        self.result += n
        return self  # Return self for chaining!
    
    def multiply(self, n):
        self.result *= n
        return self

calc = Calculator()
calc.add(5).multiply(3).add(10)  # Method chaining!
```

### Visualization:
```
calc = Calculator()
┌──────────────┐
│ calc         │
│ result = 0   │
└──────────────┘

calc.add(5)
┌──────────────┐
│ calc         │
│ result = 5   │  ← Modified
└──────────────┘
      ↓ returns self (the calc object)

.multiply(3)
┌──────────────┐
│ calc         │
│ result = 15  │  ← Modified again
└──────────────┘
      ↓ returns self

.add(10)
┌──────────────┐
│ calc         │
│ result = 25  │  ← Final value
└──────────────┘
```

---

## 🔗 Inheritance Visualization

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):  # Override parent method
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
```

### Visualization:
```
┌────────────────────────────┐
│      Animal (Parent)       │
│                            │
│  Attributes:               │
│  • name                    │
│                            │
│  Methods:                  │
│  • speak() → "Some sound"  │
└────────────────────────────┘
         ↑         ↑
         │         │ Inherit
    ┌────┴────┐    │
    │         │    │
┌───┴────┐ ┌──┴────────┐
│  Dog   │ │    Cat    │
│        │ │           │
│ speak()│ │  speak()  │
│ →"Woof"│ │  →"Meow"  │
└────────┘ └───────────┘

Dog and Cat:
✓ Inherit name attribute from Animal
✓ Override speak() method with their own
```

### How it works:
```
dog = Dog("Buddy")

When you call dog.speak():

Step 1: Look in Dog class
        ┌──────────┐
        │ Dog      │
        │ speak() ✓│ ← Found! Use this
        └──────────┘

Step 2: (Not needed)
        ┌──────────┐
        │ Animal   │
        │ speak()  │
        └──────────┘

If Dog didn't have speak():
Step 1: Look in Dog
        ┌──────────┐
        │ Dog      │
        │ (none)   │
        └──────────┘

Step 2: Look in parent (Animal)
        ┌──────────┐
        │ Animal   │
        │ speak() ✓│ ← Use this
        └──────────┘
```

---

## 🚀 Using `super()`

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent's __init__
        self.breed = breed
        print(f"Dog breed: {breed}")

dog = Dog("Buddy", "Golden Retriever")
```

### Visualization:
```
dog = Dog("Buddy", "Golden Retriever")

Step 1: Dog.__init__ called
┌────────────────────────────────┐
│ Dog.__init__(self, name, breed)│
│                                │
│ super().__init__(name) ────┐   │
│                            │   │
└────────────────────────────┼───┘
                             │
Step 2: Calls parent        │
┌────────────────────────────┼───┐
│ Animal.__init__(self, name)↓   │
│                                │
│ self.name = "Buddy"            │
│ print("Animal created")        │
└────────────────────────────────┘
                 │
Step 3: Return to Dog       │
┌────────────────────────────┼───┐
│ Dog.__init__ continued     ↓   │
│                                │
│ self.breed = "Golden Ret."     │
│ print("Dog breed")             │
└────────────────────────────────┘

Final object:
┌────────────────────────────┐
│ dog                        │
│ name = "Buddy"      ← from Animal │
│ breed = "Golden Ret." ← from Dog   │
└────────────────────────────┘

Output:
Animal created: Buddy
Dog breed: Golden Retriever
```

---

## 💡 Real-World Example: Building a Game Character

```python
class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.level = 1
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {amount} damage. Health: {self.health}")
    
    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100
        print(f"{self.name} healed {amount}. Health: {self.health}")

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150)  # Warriors start with more health
        self.strength = 20
    
    def attack(self):
        return self.strength

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80)  # Mages have less health
        self.mana = 100
    
    def cast_spell(self):
        if self.mana >= 20:
            self.mana -= 20
            return 30  # spell damage
        return 0

# Create characters
warrior = Warrior("Conan")
mage = Mage("Gandalf")
```

### Visualization:
```
Character Class (Parent)
┌────────────────────────────┐
│ name                       │
│ health = 100               │
│ level = 1                  │
│                            │
│ take_damage()              │
│ heal()                     │
└────────────────────────────┘
         │          │
    ┌────┴────┐     └────┐
    │         │          │
┌───┴───┐ ┌──┴──────┐
│Warrior│ │  Mage   │
├───────┤ ├─────────┤
│+30 HP │ │ -20 HP  │
│strength│ │ mana    │
│attack()│ │cast()   │
└───────┘ └─────────┘
    │          │
    ↓          ↓
┌────────┐ ┌─────────┐
│ Conan  │ │ Gandalf │
│ HP:150 │ │ HP: 80  │
│ STR:20 │ │ Mana:100│
└────────┘ └─────────┘

Battle:
damage = warrior.attack()  # 20
mage.take_damage(damage)   # Gandalf HP: 60

spell_dmg = mage.cast_spell()  # 30
warrior.take_damage(spell_dmg) # Conan HP: 120
```

---

## 📝 Quick Reference

```
Class Definition:
┌────────────────────────────────────┐
│ class ClassName:                   │
│     def __init__(self, params):    │
│         self.attribute = value     │
│                                    │
│     def method(self, params):      │
│         # use self.attribute       │
└────────────────────────────────────┘

Creating Objects:
object = ClassName(arguments)

Inheritance:
class Child(Parent):
    def __init__(self, params):
        super().__init__(parent_params)
        # child-specific code

Key Concepts:
• self = reference to current instance
• __init__ = constructor (setup)
• super() = access parent class
• Override = replace parent's method
```

---

## 🎯 Common Patterns

### Pattern 1: Builder Pattern
```python
class Pizza:
    def __init__(self):
        self.toppings = []
    
    def add_topping(self, topping):
        self.toppings.append(topping)
        return self  # Return self for chaining!
    
    def show(self):
        print(f"Pizza with: {', '.join(self.toppings)}")

pizza = Pizza().add_topping("cheese").add_topping("pepperoni").add_topping("olives")
pizza.show()
# Output: Pizza with: cheese, pepperoni, olives
```

### Pattern 2: Property Encapsulation
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # "Private" by convention
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def get_balance(self):
        return self._balance

account = BankAccount(1000)
# account._balance = 9999  # ❌ Don't do this!
account.deposit(500)        # ✓ Use methods!
print(account.get_balance())
```

---

## 🔗 Related Topics

- [[11_Classes_and_OOP|Classes & OOP (detailed)]]
- [[12_Inheritance|Inheritance & Polymorphism]]
- [[13_Magic_Methods|Magic Methods]]
- [[14_Properties_and_Class_Methods|Properties]]

---

[[00_Index|← Back to Index]]

*Objects make complex programs manageable! 🏗️*
