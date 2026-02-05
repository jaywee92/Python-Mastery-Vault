---
title: Python Basics - Summary
tags: [python, basics, summary, reference, cheatsheet]
created: 2026-02-05
type: summary
---

# Python Basics - Zusammenfassung

## 📋 Überblick

Dieses Dokument fasst alle wesentlichen Python-Grundlagen zusammen. Von Variablen und Datentypen über Kontrollflussmechanismen bis hin zu Funktionen, Klassen und Dateioperationen - hier findest du alle wichtigen Konzepte in kompakter Form.

---

## 🔑 Quick Reference

### Datentypen

| Typ | Beispiel | Mutable | Geordnet | Hashable |
|-----|----------|---------|----------|----------|
| `int` | `42` | ❌ | - | ✅ |
| `float` | `3.14` | ❌ | - | ✅ |
| `str` | `"hello"` | ❌ | ✅ | ✅ |
| `bool` | `True` | ❌ | - | ✅ |
| `list` | `[1,2,3]` | ✅ | ✅ | ❌ |
| `tuple` | `(1,2,3)` | ❌ | ✅ | ✅ |
| `dict` | `{k: v}` | ✅ | ✅ | ❌ |
| `set` | `{1,2,3}` | ✅ | ❌ | ❌ |

### Collections Vergleich

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| **Geordnet** | ✅ | ✅ | ❌ | ✅ |
| **Mutable** | ✅ | ❌ | ✅ | ✅ |
| **Duplikate** | ✅ | ✅ | ❌ | Keys: ❌ |
| **Indexing** | ✅ | ✅ | ❌ | Key-based |
| **Hashbar** | ❌ | ✅ | ❌ | ❌ |

### Syntax Essentials

```python
# Variablen und Zuweisung
name = "Alice"
x, y, z = 1, 2, 3
a = b = c = 0

# String Operationen
text = "Python"
text[0]         # "P" (Indexing)
text[0:3]       # "Pyt" (Slicing)
text[::-1]      # "nohtyP" (Reverse)
text.upper()    # "PYTHON"
f"{name} is {age} years old"  # F-strings

# Listen
numbers = [1, 2, 3]
numbers.append(4)
numbers.extend([5, 6])
numbers.insert(0, 0)
numbers.remove(2)
numbers.pop()
numbers[1:3]    # [2, 3]

# Dictionaries
person = {"name": "Alice", "age": 25}
person["age"]           # 25
person.get("city", "Unknown")
person.keys()
person.values()
person.items()

# Bedingungen
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

result = "Even" if x % 2 == 0 else "Odd"

# Schleifen
for i in range(5):
    print(i)

for item in items:
    print(item)

while condition:
    # Code
    break       # Exit loop
    continue    # Skip iteration

# Comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
word_dict = {k: len(k) for k in words}
unique = {x for x in numbers}

# Funktionen
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda
square = lambda x: x ** 2
evens = list(filter(lambda x: x % 2 == 0, numbers))
sorted_by_length = sorted(words, key=len)

# Klassen
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

# Dateioperationen
with open("file.txt", "r") as f:
    content = f.read()

with open("file.txt", "w") as f:
    f.write("Hello World")

# Exception Handling
try:
    risky_operation()
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print("Unexpected error")
finally:
    cleanup()
```

---

## 📝 Topic-Zusammenfassungen

### Variables and Strings Advanced

Variablen speichern Daten unter einem Namen (dynamisch typisiert). Strings sind unveränderbare Textdatentypen mit umfangreichen Methoden. F-Strings bieten die modernste Formatierungsmethode mit Ausdrucksunterstützung.

**Wichtige Konzepte:**
- Variablennamenskonventionen (snake_case)
- String Indexing und Slicing
- String Methoden (upper, lower, strip, split, replace)
- Typkonvertierung (int, float, str, bool)

---

### Lists Deep Dive

Listen sind veränderbare, geordnete Sammlungen, die verschiedene Datentypen enthalten können. Sie unterstützen Indexing, Slicing und viele Operationen. List Comprehensions bieten eine elegante und effiziente Möglichkeit, Listen zu erstellen.

**Wichtige Konzepte:**
- Positive und negative Indizierung
- Slicing mit start:stop:step Syntax
- append vs extend (einzelnes Element vs mehrere)
- Shallow vs Deep Copy
- List Comprehensions mit if/else

---

### Tuples and Sets

Tuples sind unveränderbare Sequenzen, die als Dictionary-Schlüssel verwendet werden können. Sets sind ungeordnete Sammlungen mit eindeutigen Elementen, perfekt für Memberships-Tests und mathematische Operationen.

**Wichtige Konzepte:**
- Tuple Unpacking
- Set Operationen (Union, Intersection, Difference)
- Automatisches Entfernen von Duplikaten in Sets
- Sets für O(1) Memberships-Tests

---

### Dictionaries Mastery

Dictionaries sind Schlüssel-Wert-Sammlungen mit O(1) Zugriffszeit. Schlüssel müssen einzigartig und hashbar sein. Sie sind die Go-to Datenstruktur für strukturierte Daten.

**Wichtige Konzepte:**
- get() vs [] Zugriff (Fehlerbehandlung)
- pop(), update(), setdefault()
- Dictionary Comprehensions
- Iteration über keys(), values(), items()

---

### Conditionals

If/elif/else Anweisungen kontrollieren den Programmfluss basierend auf Bedingungen. Ternäre Operatoren bieten kompakte Wenn-Sonst Konstruktionen. Einige Werte sind falsy (False, 0, "", [], None) und andere truthy.

**Wichtige Konzepte:**
- Vergleichsoperatoren (==, !=, <, >, <=, >=)
- Logische Operatoren (and, or, not)
- Ternäre Ausdrücke: `value_if_true if condition else value_if_false`
- Walrus Operator (:=) in Python 3.8+

---

### Loops and Iteration

For-Schleifen iterieren über Sequenzen, während While-Schleifen auf Bedingungen basieren. Break beendet die Schleife, Continue überspringt zur nächsten Iteration. Enumerate und Zip sind mächtige Iterationswerkzeuge.

**Wichtige Konzepte:**
- range() mit start, stop, step
- enumerate() für Index und Wert
- zip() für parallele Iteration mehrerer Sequenzen
- Loop else (wird ausgeführt, wenn ohne break beendet)

---

### Comprehensions

List, Dict, Set und Generator Comprehensions bieten prägnante Syntax für das Erstellen von Sammlungen. Sie sind oft schneller als Schleifen und Pythonischer für einfache Transformationen.

**Wichtige Konzepte:**
- Syntax: `[expression for item in iterable if condition]`
- Verschachtelte Comprehensions
- If-Else in Comprehensions (Ternär)
- Generator Expressions mit () sind speichereffizient

---

### Functions

Funktionen sind wiederverwendbare Code-Blöcke mit Parametern und Rückgabewerten. *args und **kwargs ermöglichen variable Argumente. Default Parameter, Type Hints und Docstrings sind Best Practices.

**Wichtige Konzepte:**
- Parameter vs Arguments
- Default Parameter
- *args (Tupel von Positional-Argumenten)
- **kwargs (Dict von Keyword-Argumenten)
- Return Values (einzeln oder mehrfach)

---

### Lambda and Built-ins

Lambda-Funktionen sind anonyme, einzeilige Funktionen für einfache Operationen. map(), filter(), reduce() und sorted() sind mächtige funktionale Programmierungs-Tools. any() und all() für Bedingungsprüfungen.

**Wichtige Konzepte:**
- Lambda Syntax: `lambda params: expression`
- map() - Funktion auf alle Elemente anwenden
- filter() - Elemente filtern
- sorted() mit key Parameter
- any()/all() für Bedingungsprüfungen

---

### Scope and Closures

Die LEGB-Regel bestimmt die Variablensuche: Local → Enclosing → Global → Built-in. global und nonlocal Schlüsselwörter ermöglichen Zugriff auf äußere Scopes. Closures sind Funktionen, die auf äußere Variablen zugreifen.

**Wichtige Konzepte:**
- LEGB-Regel für Variablensuche
- global Schlüsselwort für Modul-Variablen
- nonlocal für Enclosing-Scope Variablen
- Closures für Zustandsverwaltung
- Late Binding Problem in Schleifen

---

### Classes and OOP

Klassen sind Baupläne für Objekte. __init__() ist der Konstruktor. self referenziert die Instanz. Attribute speichern Daten, Methoden definieren Verhalten.

**Wichtige Konzepte:**
- class Keyword und CamelCase Namenskonvention
- __init__() Konstruktor
- self Parameter (obligatorisch)
- Instance vs Class Attributes
- Methoden und ihr Aufruf

---

### File IO

Die with-Anweisung (Context Manager) garantiert automatisches Schließen. Modi: 'r' (Lesen), 'w' (Schreiben/Überschreiben), 'a' (Anhängen). Encoding sollte immer explizit angegeben werden.

**Wichtige Konzepte:**
- with open() für automatisches close()
- File Modi und ihre Bedeutung
- read(), readline(), readlines() vs Iteration
- write() vs writelines()
- CSV und JSON Verarbeitung

---

### Exceptions

Try/except Blöcke fangen Fehler ab und verhindern Programmabsturz. else läuft nur bei Erfolg, finally läuft immer. raise erstellt benutzerdefinierte Exceptions. Spezifische Exception-Behandlung ist wichtiger als generische.

**Wichtige Konzepte:**
- try/except/else/finally Struktur
- Spezifische vs generische Exception-Behandlung
- raise für eigene Exceptions
- Custom Exception Klassen
- EAFP vs LBYL Philosophie

---

### Useful Imports

Die Standardbibliothek bietet Module für häufige Aufgaben. os und pathlib für Dateisystem, datetime für Zeiten, random für Zufallswerte, json für Datenaustausch.

**Wichtige Module:**
- os - Dateisystem und Umgebung
- sys - Interpreter Parameter
- datetime - Datum und Zeit
- json - JSON Verarbeitung
- collections - Counter, defaultdict, namedtuple
- itertools - Kombinatorik und Iterationen
- re - Reguläre Ausdrücke
- math - Mathematische Funktionen

---

## ✅ Selbsttest-Checkliste

### Grundlagen
- [ ] Ich kann Variablen erstellen und zuweisen
- [ ] Ich kenne alle primitiven Datentypen (int, float, str, bool)
- [ ] Ich kann Strings mit f-strings formatieren
- [ ] Ich verstehe True/False und Walhy/Falsy Werte

### Collections
- [ ] Ich kann Listen erstellen, modifizieren und slicen
- [ ] Ich kann zwischen append() und extend() unterscheiden
- [ ] Ich kann Tuples erstellen und unpacking verwenden
- [ ] Ich verstehe Set Operationen (Union, Intersection)
- [ ] Ich kann Dictionary-Operationen durchführen

### Control Flow
- [ ] Ich kann if/elif/else Anweisungen schreiben
- [ ] Ich kann for und while Schleifen verwenden
- [ ] Ich verstehe break, continue und else in Schleifen
- [ ] Ich kann Comprehensions (List, Dict, Set) schreiben
- [ ] Ich verstehe enumerate() und zip()

### Funktionen
- [ ] Ich kann Funktionen mit Parametern definieren
- [ ] Ich verstehe Default Parameter
- [ ] Ich kann *args und **kwargs verwenden
- [ ] Ich kenne Lambda-Funktionen
- [ ] Ich kann map(), filter() und sorted() verwenden

### Scope & OOP
- [ ] Ich verstehe die LEGB-Regel
- [ ] Ich kann zwischen global und nonlocal unterscheiden
- [ ] Ich verstehe Closures
- [ ] Ich kann einfache Klassen schreiben
- [ ] Ich verstehe __init__ und self

### Praktisch
- [ ] Ich kann Dateien lesen und schreiben (with Statement)
- [ ] Ich kann Exceptions mit try/except behandeln
- [ ] Ich kann CSV und JSON verarbeiten
- [ ] Ich kann Module importieren (os, json, datetime)
- [ ] Ich kann List Comprehensions statt Schleifen nutzen

---

## 🛤️ Empfohlener Lernpfad

### Anfänger (Grundlagen)
1. **Variables and Strings Advanced** - Fundament aller Programme
2. **Data Types** - Verschiedene Datentypen verstehen
3. **Lists Deep Dive** - Mit Daten arbeiten
4. **Dictionaries Mastery** - Strukturierte Daten
5. **Conditionals** - Entscheidungen treffen

### Anfänger-Mittelstufe (Kontrollflusss)
6. **Loops and Iteration** - Code wiederholen
7. **Comprehensions** - Elegante Listen-Erstellung
8. **Functions** - Code wiederverwendbar machen
9. **Tuples and Sets** - Weitere Collection-Typen

### Mittelstufe (Fortgeschrittene Konzepte)
10. **Lambda and Built-ins** - Funktionale Programmierung
11. **Scope and Closures** - Variablen-Zugang verstehen
12. **File IO** - Mit Dateien arbeiten
13. **Exceptions** - Fehlerbehandlung

### Fortgeschrittene
14. **Classes and OOP** - Objektorientierte Programmierung
15. **Useful Imports** - Standardbibliothek nutzen

---

## 🎯 Häufige Anfängerfehler vermeiden

### 1. List Mutation vs String Immutability
```python
# ❌ FALSCH - Strings sind unveränderbar
text = "hello"
text[0] = "H"  # TypeError!

# ✅ RICHTIG
text = "hello".upper()  # "HELLO"
```

### 2. append vs extend
```python
# ❌ FALSCH
list1 = [1, 2]
list1.append([3, 4])  # [1, 2, [3, 4]] - Nested!

# ✅ RICHTIG
list1 = [1, 2]
list1.extend([3, 4])  # [1, 2, 3, 4]
```

### 3. Dict mit [] vs get()
```python
# ❌ FALSCH - KeyError wenn nicht vorhanden
value = my_dict["key"]

# ✅ RICHTIG - Sicher mit Default
value = my_dict.get("key", "default")
```

### 4. Mutable Default Parameter
```python
# ❌ FALSCH - Unerwartetes Verhalten
def add_item(item, list_=[]):
    list_.append(item)
    return list_

# ✅ RICHTIG - None als Default
def add_item(item, list_=None):
    if list_ is None:
        list_ = []
    list_.append(item)
    return list_
```

### 5. Scope und UnboundLocalError
```python
# ❌ FALSCH - UnboundLocalError
x = 10
def func():
    print(x)    # Diese Zeile gibt Error!
    x = 5

# ✅ RICHTIG
x = 10
def func():
    global x
    print(x)
    x = 5
```

### 6. with Statement nicht verwenden
```python
# ❌ FALSCH - Datei bleibt offen
f = open("file.txt")
content = f.read()

# ✅ RICHTIG
with open("file.txt") as f:
    content = f.read()
```

---

## 💡 Pro Tips

### Performance
- Verwende List Comprehensions statt append-Schleifen
- Verwende Sets für Memberships-Tests (O(1) vs O(n))
- Für große Dateien: Iteration statt alles in den RAM laden
- Lerne die Zeitkomplexität häufiger Operationen

### Code Qualität
- Verwende aussagekräftige Variablennamen
- Halte Funktionen klein und fokussiert
- Schreibe Docstrings für öffentliche Funktionen
- Verwende Type Hints für bessere Dokumentation

### Python Idioms
- Verwende f-strings statt % oder .format()
- EAFP (Easier to Ask Forgiveness) statt LBYL
- List Comprehensions über filter/map
- Context Managers (with) für Ressourcenverwaltung

---

## 📚 Weiterführende Ressourcen

Nachdem du diese Grundlagen beherrschst, sind die nächsten Schritte:
- Python Advanced Topics (Decorators, Context Managers, Generators)
- Object-Oriented Programming (Inheritance, Polymorphism, Design Patterns)
- Standard Library (mehr Module kennenlernen)
- Testing (unittest, pytest)

---

## 🔍 Debugging Tipps

```python
# 1. Print-Debugging
print(f"Debug: x = {x}, type = {type(x)}")

# 2. type() und isinstance()
print(type(variable))
print(isinstance(variable, int))

# 3. dir() für verfügbare Methoden
print(dir(object))

# 4. help() für Dokumentation
help(function_name)

# 5. Syntax Errors - Prüfe Indentation!
# 6. NameError - Variable nicht definiert
# 7. TypeError - Falscher Datentyp
# 8. IndexError - Index außerhalb Range
# 9. KeyError - Key nicht im Dict
# 10. ValueError - Falscher Wert für Typ
```

---

**Lernstrategie:** Praktiziere regelmäßig mit kleinen Projekten, baue Funktionalität Schritt für Schritt auf, und teste deinen Code gründlich!

*Master the basics, master Python! 🐍*
