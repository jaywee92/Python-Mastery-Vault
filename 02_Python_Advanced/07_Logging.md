---
title: Logging
tags: [python, logging, monitoring, production, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# 📝 Logging

[[00_Index|← Back to Index]] | [[19_Debugging|← Debugging]] | [[21_Unit_Testing|Unit Testing →]]

> **"print() is for debugging - logging is for eternity!"**

---

## 🎯 Why Logging instead of Print?

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRINT VS LOGGING                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  print()                        logging                          │
│  ├── No levels                 ├── 5 levels (DEBUG→CRITICAL)     │
│  ├── Only stdout               ├── File, console, network...     │
│  ├── No timestamp              ├── Automatic timestamps          │
│  ├── Hard to filter            ├── Filterable by level           │
│  ├── Hard to disable           ├── Easy to toggle on/off         │
│  └── For development           └── For production                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 The 5 Log Levels

```python
import logging

# Log levels from low to high
logging.debug("Detailed debug info")      # Level 10
logging.info("General information")       # Level 20
logging.warning("Warning, but continues") # Level 30
logging.error("Error occurred")           # Level 40
logging.critical("Critical! Crash danger")# Level 50
```

```
┌─────────────────────────────────────────────────────────────────┐
│                      LOG LEVEL PYRAMID                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                    ▲                                             │
│                   /█\         CRITICAL (50)                      │
│                  /███\        System about to crash              │
│                 /█████\                                          │
│                /███████\      ERROR (40)                         │
│               /█████████\     Error, but system runs             │
│              /███████████\                                       │
│             /█████████████\   WARNING (30)                       │
│            /███████████████\  Unexpected, but ok                 │
│           /█████████████████\                                    │
│          /███████████████████\ INFO (20)                         │
│         /█████████████████████\ Normal operations                │
│        /███████████████████████\                                 │
│       /█████████████████████████\ DEBUG (10)                     │
│      /███████████████████████████\ Developer details             │
│                                                                  │
│  Higher = more important → fewer messages                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### When to use which level?

| Level | When to use | Example |
|-------|-------------|---------|
| `DEBUG` | Detailed developer info | `Processing element 42 of 100` |
| `INFO` | Normal operations | `Server started on port 8080` |
| `WARNING` | Unusual, but works | `Config file missing, using defaults` |
| `ERROR` | Error occurred | `Database connection failed` |
| `CRITICAL` | System crash imminent | `Disk full, cannot write` |

---

## 🚀 Basic Setup

### Simplest Configuration

```python
import logging

# Simple setup - shows from WARNING onwards
logging.basicConfig(level=logging.INFO)

logging.debug("Not shown")      # Level < INFO
logging.info("Will be shown")   # ✓
logging.warning("Will be shown")# ✓
```

### Formatted Output

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Server started")
# Output: 2026-01-26 14:30:00 - INFO - Server started
```

### Important Format Codes

```
┌─────────────────────────────────────────────────────────────────┐
│                     FORMAT PLACEHOLDERS                          │
├────────────────┬────────────────────────────────────────────────┤
│ %(asctime)s    │ Timestamp (formattable with datefmt)           │
│ %(levelname)s  │ Level name (DEBUG, INFO, etc.)                 │
│ %(message)s    │ The actual log message                         │
│ %(name)s       │ Logger name                                     │
│ %(filename)s   │ Source file                                     │
│ %(lineno)d     │ Line number                                     │
│ %(funcName)s   │ Function name                                   │
│ %(module)s     │ Module name                                     │
│ %(process)d    │ Process ID                                      │
│ %(thread)d     │ Thread ID                                       │
└────────────────┴────────────────────────────────────────────────┘
```

---

## 📄 Logging to File

```python
import logging

# Write to file
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("This message goes to the file")

# With filemode='w' overwrites file (default: 'a' = append)
logging.basicConfig(
    filename='app.log',
    filemode='w',  # Overwrite instead of append
    level=logging.DEBUG
)
```

---

## 🎛️ Logger, Handler and Formatter

For more control: create your own logger.

```
┌─────────────────────────────────────────────────────────────────┐
│                  LOGGING ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Logger                                                         │
│     │                                                            │
│     ├──→ Handler 1 (Console) ──→ Formatter A ──→ stdout         │
│     │                                                            │
│     └──→ Handler 2 (File) ──→ Formatter B ──→ app.log           │
│                                                                  │
│   Logger:    Creates log entries                                │
│   Handler:   Where does log go? (Console, file, network)        │
│   Formatter: How does the log look?                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Practical Example: Console + File

```python
import logging

# 1. Create logger
logger = logging.getLogger(__name__)  # Name = current module
logger.setLevel(logging.DEBUG)        # Logger accepts everything

# 2. Console handler (only INFO and higher)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_format)

# 3. File handler (everything from DEBUG)
file_handler = logging.FileHandler('debug.log')
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

# 4. Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 5. Usage
logger.debug("Only in file")           # → debug.log
logger.info("Console AND file")        # → both
logger.error("Console AND file")       # → both
```

### Handler Types

| Handler | Description |
|---------|-------------|
| `StreamHandler` | Console output (stdout/stderr) |
| `FileHandler` | Write to file |
| `RotatingFileHandler` | File with size limit + rotation |
| `TimedRotatingFileHandler` | Daily/weekly rotation |
| `SMTPHandler` | Send logs via email |
| `SocketHandler` | Send over network |

---

## 🔄 Log Rotation

Prevent log files from becoming too large:

```python
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import logging

logger = logging.getLogger(__name__)

# Rotate by size (max 5 MB, 3 backup files)
size_handler = RotatingFileHandler(
    'app.log',
    maxBytes=5*1024*1024,  # 5 MB
    backupCount=3           # app.log.1, app.log.2, app.log.3
)
logger.addHandler(size_handler)

# Rotate by time (daily at midnight)
time_handler = TimedRotatingFileHandler(
    'app.log',
    when='midnight',        # 'S', 'M', 'H', 'D', 'midnight', 'W0-W6'
    interval=1,
    backupCount=7           # Keep 7 days
)
logger.addHandler(time_handler)
```

```
🔄 ROTATION EXAMPLE (by size)
================================

Before rotation:           After rotation:
app.log (5 MB full)        app.log (new, empty)
app.log.1                  app.log.1 (was app.log)
app.log.2                  app.log.2 (was app.log.1)
app.log.3                  app.log.3 (was app.log.2)
                           [old .3 is deleted]
```

---

## 🏭 Best Practice: Module Logger

```python
# my_module.py
import logging

# ✅ Standard pattern for modules
logger = logging.getLogger(__name__)  # logger is named 'my_module'

def my_function():
    logger.debug("Function started")
    try:
        # ... code ...
        logger.info("Operation successful")
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)

# main.py
import logging
from my_module import my_function

# Configure root logger (only once, in main program!)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

my_function()
# Output: 2026-01-26 14:30:00 - my_module - DEBUG - Function started
```

---

## 🐛 Exception Logging

```python
import logging

logger = logging.getLogger(__name__)

def risky_operation():
    try:
        result = 1 / 0
    except ZeroDivisionError:
        # ❌ Loses stack trace
        logger.error("Division by zero")

        # ✅ With stack trace (exc_info=True)
        logger.error("Division by zero", exc_info=True)

        # ✅ Even better: logger.exception() (only in except block!)
        logger.exception("Division by zero")

# exc_info=True and logger.exception() show:
# ERROR - Division by zero
# Traceback (most recent call last):
#   File "...", line 7, in risky_operation
#     result = 1 / 0
# ZeroDivisionError: division by zero
```

---

## 📊 Logging with Extra Data

```python
import logging

logging.basicConfig(
    format='%(asctime)s - %(user)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Use extra fields in format
logger.info("Login successful", extra={'user': 'alice'})
# 2026-01-26 14:30:00 - alice - Login successful

# With LoggerAdapter for recurring extra data
class UserAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        kwargs.setdefault('extra', {})
        kwargs['extra']['user'] = self.extra.get('user', 'anonymous')
        return msg, kwargs

# Usage
user_logger = UserAdapter(logger, {'user': 'bob'})
user_logger.info("Action performed")
# 2026-01-26 14:30:00 - bob - Action performed
```

---

## 🔧 Configuration via Dictionary

For complex setups (professional approach):

```python
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'simple': {
            'format': '%(levelname)s - %(message)s'
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': 'app.log',
            'maxBytes': 10485760,  # 10 MB
            'backupCount': 5
        }
    },

    'loggers': {
        '': {  # Root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG'
        },
        'my_module': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': False  # Don't pass to root
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
```

---

## ⚠️ Common Pitfalls

```python
# ❌ WRONG: Call basicConfig multiple times (only works first time!)
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)  # Has NO effect!

# ✅ CORRECT: Modify root logger directly
logging.getLogger().setLevel(logging.INFO)

# ❌ WRONG: f-String for lazy evaluation
logger.debug(f"Result: {expensive_calculation()}")  # ALWAYS calculated!

# ✅ CORRECT: %-formatting (only evaluated if needed)
logger.debug("Result: %s", expensive_calculation())  # Only if DEBUG active

# ❌ WRONG: Log exception without stack trace
try:
    risky_code()
except Exception as e:
    logger.error(f"Error: {e}")  # No stack trace!

# ✅ CORRECT: Use exc_info or exception()
try:
    risky_code()
except Exception as e:
    logger.exception(f"Error: {e}")  # Includes stack trace

# ❌ WRONG: Use root logger directly in modules
logging.info("...")  # Hard to control

# ✅ CORRECT: Use module logger
logger = logging.getLogger(__name__)
logger.info("...")
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| `logger = logging.getLogger(__name__)` | `logging.info()` directly |
| `basicConfig()` only once in main | `basicConfig()` in modules |
| `%-formatting` for lazy evaluation | f-Strings for expensive logs |
| `logger.exception()` in except block | Exceptions without stack trace |
| Handlers with different levels | Everything on same level |
| Log rotation for production | Unbounded growing log files |

---

## 🎯 Recommended Setup for Projects

```python
# config/logging_config.py
import logging
import logging.handlers
import os

def setup_logging(log_level=logging.INFO):
    """Set up standard logging for projects."""

    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    # Define format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # Console handler (INFO+)
    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(formatter)
    root_logger.addHandler(console)

    # File handler with rotation (DEBUG+)
    file_handler = logging.handlers.RotatingFileHandler(
        f'{log_dir}/app.log',
        maxBytes=10*1024*1024,  # 10 MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

# main.py
from config.logging_config import setup_logging

setup_logging(log_level=logging.INFO)
```

---

## 🎯 Exam Checklist

- [ ] 5 log levels and their meanings (DEBUG < INFO < WARNING < ERROR < CRITICAL)
- [ ] `basicConfig()` for simple setup
- [ ] `getLogger(__name__)` for modules
- [ ] Handlers (StreamHandler, FileHandler, RotatingFileHandler)
- [ ] Formatter and format codes (%(asctime)s, %(levelname)s, etc.)
- [ ] `exc_info=True` vs `logger.exception()`
- [ ] Why %-format instead of f-String in logging

---

[[19_Debugging|← Debugging]] | [[00_Index|Index]] | [[21_Unit_Testing|Unit Testing →]]
