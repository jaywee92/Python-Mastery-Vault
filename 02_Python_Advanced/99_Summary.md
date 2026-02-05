---
title: Python Advanced - Summary
tags: [python, advanced, summary, reference, cheatsheet]
---

# Python Advanced - Zusammenfassung

## 📋 Überblick

Diese Zusammenfassung deckt die wichtigsten fortgeschrittenen Python-Konzepte ab: OOP mit Vererbung und Magic Methods, funktionale Programmierung mit Decorators und Generatoren, sowie Best Practices für Debugging, Testing und Code Quality. Sie ist eine Schnelleinstiegshilfe zum Wiederholen und Vertiefen aller Topics.

---

## 🔑 Quick Reference

### OOP Konzepte

| Konzept | Beschreibung | Beispiel |
|---------|-------------|----------|
| **Inheritance** | Vererbung von Parent zu Child-Klasse | `class Dog(Animal):` |
| **super()** | Zugriff auf Parent-Methoden | `super().__init__(name)` |
| **Magic Methods** | Spezielle Methoden mit `__name__` | `__str__`, `__add__`, `__iter__` |
| **@property** | Attribut-ähnlicher Zugriff mit Validierung | `@property def value(self):` |
| **@classmethod** | Klassenmethode mit `cls` Parameter | `@classmethod def from_dict(cls, data):` |
| **@staticmethod** | Utility-Funktion ohne self/cls | `@staticmethod def validate(x):` |
| **ABC** | Abstract Base Classes für Interfaces | `from abc import ABC, abstractmethod` |

### Wichtige Magic Methods

| Kategorie | Methoden |
|-----------|----------|
| **Lifecycle** | `__init__`, `__new__`, `__del__` |
| **String** | `__str__`, `__repr__`, `__format__` |
| **Operator** | `__add__`, `__sub__`, `__mul__`, `__eq__`, `__lt__` |
| **Container** | `__len__`, `__getitem__`, `__setitem__`, `__iter__` |
| **Attribute** | `__getattr__`, `__setattr__`, `__delattr__` |
| **Context** | `__enter__`, `__exit__` |

### Wichtige Module

| Modul | Zweck | Beispiel |
|-------|-------|----------|
| **pathlib** | Moderne Pfadoperationen | `Path('data') / 'file.txt'` |
| **json** | Serialisierung & Deserialisierung | `json.dumps()`, `json.loads()` |
| **datetime** | Datums- & Zeitoperationen | `datetime.now()`, `date(2024, 1, 1)` |
| **re** | Regular Expressions | `re.search(r'\d+', text)` |
| **itertools** | Iterator-Werkzeuge | `chain()`, `combinations()`, `product()` |
| **functools** | Higher-Order Functions | `reduce()`, `partial()`, `@wraps` |
| **logging** | Professionelle Log-Ausgabe | `logging.getLogger(__name__)` |
| **unittest** | Unit Testing Framework | `unittest.TestCase` |

---

## 📝 Topic-Zusammenfassungen

### Inheritance (Vererbung)

Ermöglicht Code-Wiederverwendung durch Vererbung von Parent-Klassen. Child-Klassen erben Attribute und Methoden und können diese überschreiben. `super()` greift auf Parent-Methoden zu. Multiple Inheritance möglich mit MRO (Method Resolution Order). Abstract Base Classes (ABC) erzwingen Implementierung bestimmter Methoden in Subklassen. Use-Case: Shape-Hierarchie mit spezialisiertem Verhalten pro Typ.

### Magic Methods (Dunder Methods)

Spezielle Methoden mit doppelten Unterstrichen, die Python automatisch aufruft. `__str__` für benutzerfreundliche Ausgabe, `__repr__` für Debugging. Arithmetische Operatoren (`__add__`, `__mul__`) ermöglichen Custom-Operationen. Container-Methoden (`__getitem__`, `__iter__`) machen Objekte indexierbar/iterable. `__enter__`/`__exit__` für Context Manager. Use-Case: Vector-Klasse mit `__add__` und `__mul__` für mathematische Operationen.

### Properties und Class Methods

`@property` ermöglicht validierte Attributzugriffe ohne Getter/Setter-Methoden. `@classmethod` für Alternative Konstruktoren und Klassenvariablenmanagement (z.B. `Person.from_dict()`). `@staticmethod` für Utility-Funktionen ohne self/cls. Entscheidungsbaum: Braucht self? → Instance Method. Braucht cls? → @classmethod. Braucht nichts? → @staticmethod.

### JSON (Serialisierung)

`json.dumps()` konvertiert Python zu JSON-String, `json.loads()` vice versa. `json.dump()` schreibt direkt in Datei, `json.load()` liest von Datei. Type-Mapping: dict↔object, list↔array, str↔string, int/float↔number, bool↔true/false, None↔null. Custom Encoder/Decoder für komplexe Typen wie datetime. Wichtig: Tuples werden zu Arrays und zurück zu Listen.

### Path Operations (pathlib)

`Path` ist moderne, OOP-Variante zu `os.path`. `/` Operator für Pfad-Konkatenation. Wichtige Attribute: `.name` (Dateiname), `.stem` (ohne Extension), `.suffix` (Extension), `.parent` (Verzeichnis). `.glob('*.py')` für Pattern-Matching, `.rglob()` rekursiv. `.read_text()`, `.write_text()` für einfaches Lesen/Schreiben. `.mkdir(parents=True)` für Verzeichniserstellung.

### Debugging

`breakpoint()` setzt interaktive Haltepunkte im PDB (Python Debugger). PDB-Kommandos: `n` (next), `s` (step into), `c` (continue), `p expr` (print). F-String-Debugging: `f"{var=}"` zeigt Name und Wert. `assert` für interne Invarianten (nur Entwicklung). IDE-Debugger bietet visuelle Breakpoints und Variable Inspection. Print-Debugging einfach, aber vergesslich.

### Logging

5 Log-Level: DEBUG < INFO < WARNING < ERROR < CRITICAL. `basicConfig()` für einfaches Setup, `getLogger(__name__)` für Module-Logger. Handler (Console, File) mit verschiedenen Levels. Formatter mit Format-Codes wie `%(asctime)s`, `%(levelname)s`. `logger.exception()` für Stack-Traces. Log-Rotation verhindert unbegrenztes Dateiwachstum.

### Unit Testing

`unittest.TestCase` mit `assertEqual()`, `assertTrue()`, `assertRaises()` Methoden. `setUp()`/`tearDown()` vor/nach jedem Test, `setUpClass()`/`tearDownClass()` für Klasse. `pytest` moderner mit einfachen Functions statt Klassen und `@pytest.fixture` für Setup. `@pytest.mark.parametrize` für mehrere Test-Cases. Mocking mit `@patch` zum Testen von APIs/DBs isoliert.

### Code Quality

PEP 8 Style-Guide: `snake_case` für Variablen/Funktionen, `PascalCase` für Klassen, `UPPER_SNAKE_CASE` für Konstanten. Readability zählt (max 79 Zeichen). Docstrings für Module/Klassen/Funktionen. Type Hints verbessern Code-Lesbarkeit. Linter (flake8, black) und Formatter automatisieren Konsistenz. Guter Code ist wartbarer Code.

### Common Pitfalls (Top 10)

1. **Mutable Defaults**: `def func(lst=[]):` → List reused! Fix: `lst=None` mit Erstellung im Body
2. **Late Binding Closures**: Lambdas binden Variable spät → Verwende `default=i` Parameter
3. **Modifying While Iterating**: Nicht während Iteration modify → Nutze List Comprehension oder kopiere
4. **== vs is**: `is` nur für None/True/False, `==` für Werte
5. **Forgotten return**: Funktion returniert None statt Wert → Explizites `return` hinzufügen
6. **Integer Caching**: -5 bis 256 gecacht, außerhalb neue Objekte → `is` unreliable
7. **List as Class Attribute**: Wird zwischen Instances geteilt → Instance-Attribut nutzen
8. **Shallow vs Deep Copy**: `copy()` für shallow, `deepcopy()` für verschachtelte Strukturen
9. **Variable Scope in Loops**: Loop-Variable existiert nach Loop → Name-Reuse vermeiden
10. **String Immutability**: Strings unveränderlich → Neue String-Operationen schaffen neue Objekte

### Standard Library

Wichtige Module: `os`, `sys` (OS-Interface), `pathlib` (Pfade), `json` (Serialisierung), `datetime` (Zeit), `re` (Regex), `collections` (Advanced Containers), `itertools` (Iterator-Tools), `functools` (Higher-Order Functions), `logging` (Logging), `unittest` (Testing). `os` wird zunehmend durch `pathlib` ersetzt.

### Regular Expressions

`re.search()` findet erste Match, `re.match()` nur am Start, `re.fullmatch()` ganzer String. `re.findall()` gibt Liste aller Matches. `re.sub()` für Search & Replace. `r''` (raw string) essential für Regex! Patterns: `\d` (digit), `\w` (word), `\s` (whitespace), `[abc]` (character set), `*` (0+), `+` (1+), `?` (0-1), `{n,m}` (n bis m). Flags: `re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`.

### Working with Dates

`date` für Datum, `time` für Uhrzeit, `datetime` für beides, `timedelta` für Differenzen. `date.today()` aktuell, `.strftime()` Formatting, `.strptime()` Parsing. `timedelta(days=1, hours=2)` für Zeitdifferenzen. Timezone mit `pytz` oder `zoneinfo` (Python 3.9+). ISO Format (`isoformat()`) ist portabel und sortierbar.

### Iterators and Generators

Iterator-Protokoll: `__iter__()` returns Iterator, `__next__()` returns next Element oder `StopIteration`. `yield` in Generatoren → Lazy Evaluation, speicher-effizient. `next()` und `for` triggern `__next__()`. Generator-Expression `(x for x in range(1M))` vs List `[x for x in range(1M)]` - huge Memory Difference. `yield from` delegiert an Sub-Generator.

### Decorators

Decorators sind Functions, die Functions wrappen und erweitern. `@decorator` syntax ist syntactic sugar für `func = decorator(func)`. Closure ermöglicht State zwischen Aufrufen. `functools.wraps` preserviert Metadaten. Usecase: Logging, Timing, Caching, Validation. Parameter: `@decorator(arg)` braucht Triple-Nesting. Classes als Decorators möglich via `__call__`.

### Context Managers

`with` Statement garantiert Cleanup via `__enter__()`/`__exit__()` auch bei Exceptions. `@contextlib.contextmanager` Decorator vereinfacht Custom Context Manager. Multiple: `with open(...) as f1, open(...) as f2:`. Usecase: File-Handling, Database Transactions, Locks, Temp-Directories. `__exit__()` Return-Value kontrolliert Exception-Propagation.

### Memory and Performance

Größere Datenstrukturen: `sys.getsizeof()` shallow Size. Generators sparen Memory (lazy). List Comprehensions schneller als loops. Dictionary/Set O(1) lookup vs List O(n). `timeit` Module für Micro-Benchmarking. `cProfile` für Profiling. Avoid: Nested Loops, Redundante Berechnungen, Große temporäre Listen. Optimize: Builtin Functions (C-written), Vectorization (NumPy), Caching.

### Operators Deep Dive

Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`. Comparison: `==`, `!=`, `<`, `<=`, `>`, `>=`. Logical: `and`, `or`, `not`. Bitwise: `&`, `|`, `^`, `~`, `<<`, `>>`. Assignment: `=`, `+=`, `-=`, etc. Identity: `is`, `is not` (nur für None/True/False). Membership: `in`, `not in`. Operator Precedence: Exponentiation > Multiplication > Addition > Comparison > Logical.

### Modules and Packages

Module = `.py` Datei mit Code. Package = Directory mit `__init__.py`. `import mymodule`, `from mymodule import func`, `from mymodule import func as f`. Namespace Management verhindert Name-Konflikte. `__all__` definiert Public API. Relative imports: `from . import sibling`, `from .. import parent`. Circular Imports vermeiden durch Reorganization.

### pip Package Manager

`pip install package` installiert von PyPI. `pip install package==1.0.0` spezifische Version. `pip install -r requirements.txt` installiert aus Datei. `pip list` zeigt installierte Packages. `pip freeze > requirements.txt` exportiert aktuell installierte. Virtuelle Envs (`venv`, `virtualenv`) für Project-Isolation. `pyenv` für Python-Version Management.

### Web Scraping

`requests.get(url)` fetcht HTML. `BeautifulSoup(html, 'lxml')` parsed HTML. `.find()`, `.find_all()` für Element-Selection. `.select()` mit CSS Selectors. Robots.txt und ToS prüfen vor Scraping. Throttle/Delays einbauen. User-Agent Header wichtig. Handle Exceptions (timeout, connection errors). Strukturierte Daten (JSON APIs) bevorzugen zu Scraping.

### Virtual Environments

`python -m venv myenv` creates Virtual Environment. `source myenv/bin/activate` (Linux/Mac) oder `myenv\Scripts\activate` (Windows) activates. `deactivate` leaves Environment. Isoliert Packages pro Project, verhindert Konflikte. `requirements.txt` mit `pip freeze` erstellen für Reproducibility. `.gitignore` mit `venv/` um nicht ins Repo zu checken.

### Statistics

`statistics` Module für Basic Stats: `mean()`, `median()`, `mode()`. `variance()`, `stdev()` für Spread. NumPy & Pandas für Advanced Analysis. Scipy für Statistical Tests. Matplotlib für Visualization. Wichtig: Sample vs Population Mean/Variance unterscheiden. Outlier-Detection & Handling. Normalverteilung prüfen vor Parametrischen Tests.

### Pandas Basics

`Series` = 1D Labeled Array. `DataFrame` = 2D Tabelle (wie Excel). `.read_csv()`, `.to_csv()` für CSV. `.loc[]` Label-based Selection, `.iloc[]` Index-based. `.groupby()` für Aggregation. `.apply()` für Custom Functions. `.merge()`, `.join()` für Kombinieren. Performance: Vectorized Operations schneller als loops. Missing Values: `.fillna()`, `.dropna()`.

### Flask Web Framework

Lightweight Microframework. `@app.route()` definiert Routes. Request Handling via `request` object. Response als String, JSON, Redirect. Templates mit Jinja2. Static Files Management. Error Handling mit `@app.errorhandler()`. Blueprints für Modularisierung. Session & Cookie Management. Deployment auf Gunicorn/uWSGI. Perfect für APIs & Small Apps.

### MongoDB Integration

NoSQL Document Database mit JSON-ähnliche Struktur. `PyMongo` Library für Python Integration. Collections statt Tables, Documents statt Rows. `insert_one()`, `insert_many()` für Insert. `find()` für Query, `find_one()` für Single. `update_one()`, `replace_one()` für Updates. `delete_one()`, `delete_many()` für Delete. Indexing für Performance. Aggregation Pipeline für Complex Queries.

### Professional Libraries

`requests` für HTTP. `pandas` & `numpy` für Data. `matplotlib` & `seaborn` für Plots. `sqlalchemy` ORM für Databases. `pydantic` für Datenvalidation. `fastapi` für Modern Web APIs. `asyncio` & `aiohttp` für Async. `click` & `argparse` für CLI. `pytest` für Testing. `python-dotenv` für Env-Variablen. Standard in Industry-Projekten.

---

## ✅ Selbsttest-Checkliste

### OOP & Vererbung
- [ ] Ich kann einfache Vererbungshierarchien designen
- [ ] Ich verstehe `super()` und wann ich es verwende
- [ ] Ich kenne die Unterschiede zwischen Inheritance vs Composition
- [ ] Ich verstehe MRO (Method Resolution Order) bei Multiple Inheritance
- [ ] Ich kann Abstract Base Classes (ABC) implementieren

### Magic Methods
- [ ] Ich kann `__str__` vs `__repr__` unterscheiden
- [ ] Ich kann Arithmetic Operators überschreiben (`__add__`, `__mul__`)
- [ ] Ich verstehe `__getitem__`, `__setitem__`, `__len__` für Container
- [ ] Ich kann `__enter__`/`__exit__` für Context Manager schreiben
- [ ] Ich verstehe `__eq__` und `__hash__` Beziehung

### Properties & Methods
- [ ] Ich kann `@property` mit Getter, Setter, Deleter implementieren
- [ ] Ich verstehe `@classmethod` für Factory Methods
- [ ] Ich kann `@staticmethod` für Utility-Funktionen nutzen
- [ ] Ich weiß wann ich welchen Decorator verwende

### Praktische Themen
- [ ] Ich kann JSON serialisieren/deserialisieren
- [ ] Ich handle pathlib für moderne Pfadoperationen
- [ ] Ich kann mit datetime arbeiten und Zeitformatierung machen
- [ ] Ich schreibe einfache Regular Expressions
- [ ] Ich nutze itertools und functools effizient

### Debugging & Testing
- [ ] Ich kann `breakpoint()` und PDB Commands nutzen
- [ ] Ich schreibe Unit Tests mit unittest oder pytest
- [ ] Ich verstehe Mocking und wann ich es anwende
- [ ] Ich kann Logging setup und konfigurieren
- [ ] Ich kann Assertions für interne Invarianten nutzen

### Advanced Topics
- [ ] Ich verstehe Generators und `yield` für Memory-Effizienz
- [ ] Ich kann Decorators schreiben und verstehe Closures
- [ ] Ich verstehe Context Managers und das `with` Statement
- [ ] Ich kenne Common Pitfalls und wie ich sie vermeide
- [ ] Ich kann Code Quality Tools einsetzen

### Professionelle Entwicklung
- [ ] Ich nutze Virtual Environments für Project-Isolation
- [ ] Ich schreibe PEP 8 konformen Code
- [ ] Ich verstehe Module/Package-Struktur
- [ ] Ich kann mit APIs (requests) arbeiten
- [ ] Ich verstehe Grundlagen von Pandas, Flask, MongoDB

---

## 🛤️ Empfohlener Lernpfad

### Phase 1: OOP Foundation (Grundlagen verstehen)
1. **Inheritance** - Vererbungshierarchien, super(), Polymorphismus
2. **Magic Methods** - String-Repräsentation, Operator-Überladung
3. **Properties & Decorators** - @property, @classmethod, @staticmethod
4. Start: Einfache Klasse mit Vererbung schreiben

### Phase 2: Working with Data (Praktische Fähigkeiten)
1. **JSON** - Serialisierung, Custom Encoder/Decoder
2. **pathlib** - Moderne Pfadoperationen
3. **datetime** - Datums-/Zeitoperationen
4. **Regular Expressions** - Pattern Matching & Parsing
5. Projekt: Config-Datei Parser mit JSON + pathlib

### Phase 3: Functional & Advanced (Konzeptuell)
1. **Iterators & Generators** - Lazy Evaluation, Memory-Effizienz
2. **Decorators** - Funktionen erweitern, Closures
3. **Context Managers** - Ressourcen-Management
4. Projekt: Decorator für Logging/Timing, Generator für große Datenmengen

### Phase 4: Quality & Best Practices (Professionell)
1. **Debugging** - PDB, Assertions, Print-Debugging
2. **Logging** - Produktions-Logging, Log-Levels
3. **Unit Testing** - unittest/pytest, Mocking
4. **Code Quality** - PEP 8, Linting, Type Hints
5. **Common Pitfalls** - Mutable Defaults, Late Binding, etc.

### Phase 5: Professionelle Entwicklung (Praktisch)
1. **Standard Library** - os, sys, collections, itertools, functools
2. **Virtual Environments** - pip, requirements.txt
3. **Professional Libraries** - requests, pandas, numpy (selektiv)
4. **Web/DB Basics** - Flask/MongoDB oder Web Scraping
5. **Memory & Performance** - Profiling, Optimization
6. Projekt: Web-App oder API mit Testing & Logging

### Phase 6: Vertiefung (Spezialisiert)
- Nach Interesse: Web (Flask/FastAPI), Data (Pandas/NumPy), DevOps, Async Programming
- Kontinuierliche Verbesserung: Code Reviews, Open Source, Production-Erfahrung

---

## 💡 Learning Tips

1. **Hands-On Lernen**: Jeden Code selbst tippen, nicht copy-paste
2. **Kleine Projekte**: Quiz-App, Todo-Manager, Web-Scraper → Mini-Projekte kombinieren Topics
3. **Debugging Üben**: Absichtlich Bugs bauen & mit PDB debuggen
4. **Code Review**: Anderen Code lesen (Open Source, GitHub)
5. **Regelmäßig Testen**: Wöchentliche Mini-Tests auf Basis Checkliste
6. **Dokumentation Lesen**: Offizielle Docs sind Gold (docs.python.org)
7. **Error Messages Verstehen**: Tracebacks von Bottom zu Top lesen

---

## 🎯 Prüfungs-Tipps (für Examen)

1. **Time Management**: Leicht/Medium zuerst, dann schwierig
2. **Keyword-Erkennung**: "Schreibe einen Decorator" vs "Erkläre ABC"
3. **Code lesen/Debuggen**: Nicht blind Code schreiben, Fehler vorhersagen
4. **Praktische Beispiele**: Konkrete Szenarien besser als Theorie
5. **Edge Cases**: None, Empty Collections, 0, -1 immer testen
6. **Best Practices**: PEP 8, Error Handling, Dokumentation zählen
7. **Zeitbudget**: 2-3 Minuten pro Frage, am Ende Review

---

Generated: 2026-02-05
Source: 25 Python Advanced Topics (01-27)
