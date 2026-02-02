---
title: Working with Dates
tags: [python, datetime, time, dates, exam-essential]
created: 2026-01-26
exam_weight: high
difficulty: intermediate
---

# 📅 Working with Dates

[[00_Index|← Back to Index]] | [[12_Regular_Expressions|← Regular Expressions]] | [[14_Iterators_and_Generators|Iterators & Generators →]]

> **"There are only two hard problems in computer science: cache invalidation and time zones."**

---

## 🎯 The datetime Module

```
┌─────────────────────────────────────────────────────────────────┐
│                    DATETIME CLASSES                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  date          │ Date only (year, month, day)                   │
│  time          │ Time only (hour, minute, second, microsecond)  │
│  datetime      │ Date + time combined                           │
│  timedelta     │ Time difference / duration                     │
│  timezone      │ Timezone (UTC offset)                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📆 date - Date Only

```python
from datetime import date

# ═══════════════════════════════════════════════════════════════
# CREATE
# ═══════════════════════════════════════════════════════════════
today = date.today()                      # Today's date
birthday = date(1990, 5, 15)              # Specific date
christmas = date(2024, 12, 25)

# ═══════════════════════════════════════════════════════════════
# ATTRIBUTES
# ═══════════════════════════════════════════════════════════════
print(today.year)                         # 2024
print(today.month)                        # 1
print(today.day)                          # 26

# ═══════════════════════════════════════════════════════════════
# METHODS
# ═══════════════════════════════════════════════════════════════
today.weekday()                           # 0=Mon, 1=Tue, ..., 6=Sun
today.isoweekday()                        # 1=Mon, 2=Tue, ..., 7=Sun
today.isoformat()                         # '2024-01-26'
today.strftime('%d.%m.%Y')                # '26.01.2024'

# Parse from string
from datetime import datetime
d = datetime.strptime('26.01.2024', '%d.%m.%Y').date()

# Replace
new_date = today.replace(year=2025)       # Same date, different year
```

---

## ⏰ time - Time Only

```python
from datetime import time

# ═══════════════════════════════════════════════════════════════
# CREATE
# ═══════════════════════════════════════════════════════════════
t = time(14, 30, 0)                       # 14:30:00
t = time(14, 30, 45, 123456)              # With microseconds
t = time(hour=14, minute=30)              # With keywords

# ═══════════════════════════════════════════════════════════════
# ATTRIBUTES
# ═══════════════════════════════════════════════════════════════
print(t.hour)                             # 14
print(t.minute)                           # 30
print(t.second)                           # 45
print(t.microsecond)                      # 123456

# ═══════════════════════════════════════════════════════════════
# METHODS
# ═══════════════════════════════════════════════════════════════
t.isoformat()                             # '14:30:45.123456'
t.strftime('%H:%M')                       # '14:30'
t.replace(minute=0)                       # 14:00:45
```

---

## 📅⏰ datetime - Date + Time

```python
from datetime import datetime

# ═══════════════════════════════════════════════════════════════
# CREATE
# ═══════════════════════════════════════════════════════════════
now = datetime.now()                      # Now (local)
utc_now = datetime.utcnow()               # Now (UTC) - deprecated!
                                          # Better: datetime.now(timezone.utc)

dt = datetime(2024, 12, 25, 14, 30, 0)    # Specific moment
dt = datetime(year=2024, month=12, day=25, hour=14, minute=30)

# ═══════════════════════════════════════════════════════════════
# ATTRIBUTES
# ═══════════════════════════════════════════════════════════════
print(now.year)                           # 2024
print(now.month)                          # 1
print(now.day)                            # 26
print(now.hour)                           # 14
print(now.minute)                         # 30
print(now.second)                         # 45
print(now.microsecond)                    # 123456
print(now.weekday())                      # 0-6 (Mon-Sun)

# ═══════════════════════════════════════════════════════════════
# CONVERT
# ═══════════════════════════════════════════════════════════════
now.date()                                # Just date object
now.time()                                # Just time object

# Combine
from datetime import date, time, datetime
d = date(2024, 1, 26)
t = time(14, 30)
dt = datetime.combine(d, t)               # datetime(2024, 1, 26, 14, 30)
```

---

## 📝 Formatting (strftime)

```python
from datetime import datetime

now = datetime.now()

# ═══════════════════════════════════════════════════════════════
# COMMON FORMATS
# ═══════════════════════════════════════════════════════════════
now.strftime('%Y-%m-%d')                  # '2024-01-26'
now.strftime('%d.%m.%Y')                  # '26.01.2024'
now.strftime('%d/%m/%y')                  # '26/01/24'
now.strftime('%H:%M:%S')                  # '14:30:45'
now.strftime('%H:%M')                     # '14:30'
now.strftime('%I:%M %p')                  # '02:30 PM'
now.strftime('%Y-%m-%d %H:%M:%S')         # '2024-01-26 14:30:45'

# ═══════════════════════════════════════════════════════════════
# WEEKDAYS & MONTHS
# ═══════════════════════════════════════════════════════════════
now.strftime('%A')                        # 'Friday' (full name)
now.strftime('%a')                        # 'Fri' (short form)
now.strftime('%B')                        # 'January'
now.strftime('%b')                        # 'Jan'

# ISO format
now.isoformat()                           # '2024-01-26T14:30:45.123456'
```

### Format Codes Reference

```
┌─────────────────────────────────────────────────────────────────┐
│                    STRFTIME FORMAT CODES                         │
├─────────────────────────────────────────────────────────────────┤
│  DATE                                                           │
│  ─────────────────────────────────────────────────────────────  │
│  %Y       Year 4 digits                 2024                    │
│  %y       Year 2 digits                 24                      │
│  %m       Month zero-padded              01-12                  │
│  %d       Day zero-padded                01-31                  │
│  %j       Day of year                    001-366                │
│                                                                  │
│  TIME                                                           │
│  ─────────────────────────────────────────────────────────────  │
│  %H       Hour 24h zero-padded           00-23                  │
│  %I       Hour 12h zero-padded           01-12                  │
│  %M       Minute zero-padded             00-59                  │
│  %S       Second zero-padded             00-59                  │
│  %f       Microsecond                    000000-999999          │
│  %p       AM/PM                          AM, PM                 │
│                                                                  │
│  WEEKDAY/MONTH                                                  │
│  ─────────────────────────────────────────────────────────────  │
│  %A       Weekday full                   Friday                 │
│  %a       Weekday short                  Fri                    │
│  %B       Month full                     January                │
│  %b       Month short                    Jan                    │
│  %w       Weekday number                 0=Sun, 6=Sat           │
│                                                                  │
│  WEEK                                                           │
│  ─────────────────────────────────────────────────────────────  │
│  %W       Calendar week (Mon=start)      00-53                  │
│  %U       Calendar week (Sun=start)      00-53                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📥 Parsing (strptime)

```python
from datetime import datetime

# ═══════════════════════════════════════════════════════════════
# STRING → DATETIME
# ═══════════════════════════════════════════════════════════════
dt = datetime.strptime('2024-01-26', '%Y-%m-%d')
dt = datetime.strptime('26.01.2024', '%d.%m.%Y')
dt = datetime.strptime('2024-01-26 14:30:00', '%Y-%m-%d %H:%M:%S')
dt = datetime.strptime('Jan 26, 2024', '%b %d, %Y')

# ⚠️ Format must match exactly!
# datetime.strptime('2024/01/26', '%Y-%m-%d')  # ValueError!

# ═══════════════════════════════════════════════════════════════
# ISO FORMAT PARSING
# ═══════════════════════════════════════════════════════════════
dt = datetime.fromisoformat('2024-01-26')
dt = datetime.fromisoformat('2024-01-26T14:30:00')
dt = datetime.fromisoformat('2024-01-26T14:30:00+01:00')  # With timezone

# ═══════════════════════════════════════════════════════════════
# FLEXIBLE PARSING WITH DATEUTIL (Third-party)
# ═══════════════════════════════════════════════════════════════
# pip install python-dateutil
from dateutil import parser

parser.parse('January 26, 2024')
parser.parse('26/01/2024')
parser.parse('2024-01-26T14:30:00Z')
parser.parse('next friday')  # Relative!
```

---

## ⏱️ timedelta - Time Differences

```python
from datetime import datetime, timedelta

# ═══════════════════════════════════════════════════════════════
# CREATE
# ═══════════════════════════════════════════════════════════════
delta = timedelta(days=7)
delta = timedelta(hours=2, minutes=30)
delta = timedelta(weeks=2)
delta = timedelta(days=1, hours=12, minutes=30, seconds=45)

# Negative time spans
delta = timedelta(days=-7)                # One week ago

# ═══════════════════════════════════════════════════════════════
# CALCULATE WITH DATETIME
# ═══════════════════════════════════════════════════════════════
now = datetime.now()

# Addition
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
in_2_hours = now + timedelta(hours=2)

# Subtraction
yesterday = now - timedelta(days=1)
last_month = now - timedelta(days=30)

# Difference between two moments
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)
diff = end - start                        # timedelta object
print(diff.days)                          # 365

# ═══════════════════════════════════════════════════════════════
# TIMEDELTA ATTRIBUTES
# ═══════════════════════════════════════════════════════════════
delta = timedelta(days=2, hours=3, minutes=30)
print(delta.days)                         # 2
print(delta.seconds)                      # 12600 (3h 30min in seconds)
print(delta.total_seconds())              # 185400.0 (all in seconds)

# ⚠️ WARNING: .seconds is not total!
delta = timedelta(days=1, hours=2)
print(delta.seconds)                      # 7200 (only the 2h!)
print(delta.total_seconds())              # 93600 (1 day + 2h)
```

### Practical Examples

```python
from datetime import datetime, timedelta

# Calculate age
birthday = datetime(1990, 5, 15)
age = datetime.now() - birthday
print(f"Age: {age.days // 365} years")

# Check deadline
deadline = datetime(2024, 2, 1)
remaining = deadline - datetime.now()
if remaining.days > 0:
    print(f"Still {remaining.days} days until deadline")
else:
    print("Deadline exceeded!")

# Find next Friday
today = datetime.now()
days_until_friday = (4 - today.weekday()) % 7  # 4 = Friday
if days_until_friday == 0:
    days_until_friday = 7
next_friday = today + timedelta(days=days_until_friday)
```

---

## 🌍 Timezones

```python
from datetime import datetime, timezone, timedelta

# ═══════════════════════════════════════════════════════════════
# UTC
# ═══════════════════════════════════════════════════════════════
utc_now = datetime.now(timezone.utc)
print(utc_now)                            # 2024-01-26 13:30:00+00:00

# ═══════════════════════════════════════════════════════════════
# TIMEZONE WITH OFFSET
# ═══════════════════════════════════════════════════════════════
cet = timezone(timedelta(hours=1))        # Central European Time (UTC+1)
berlin_time = datetime.now(cet)

# ═══════════════════════════════════════════════════════════════
# NAIVE VS AWARE
# ═══════════════════════════════════════════════════════════════
naive = datetime.now()                    # Without timezone
aware = datetime.now(timezone.utc)        # With timezone

# Naive → Aware (add timezone)
naive = datetime(2024, 1, 26, 14, 30)
aware = naive.replace(tzinfo=timezone.utc)

# ═══════════════════════════════════════════════════════════════
# WITH ZONEINFO (Python 3.9+)
# ═══════════════════════════════════════════════════════════════
from zoneinfo import ZoneInfo

berlin_tz = ZoneInfo("Europe/Berlin")
tokyo_tz = ZoneInfo("Asia/Tokyo")
ny_tz = ZoneInfo("America/New_York")

berlin_time = datetime.now(berlin_tz)
tokyo_time = datetime.now(tokyo_tz)

# Convert between timezones
berlin_time = datetime.now(berlin_tz)
tokyo_time = berlin_time.astimezone(tokyo_tz)
```

---

## 📊 Comparing

```python
from datetime import datetime, date

# ═══════════════════════════════════════════════════════════════
# COMPARISON OPERATORS
# ═══════════════════════════════════════════════════════════════
dt1 = datetime(2024, 1, 1)
dt2 = datetime(2024, 12, 31)

dt1 < dt2                                 # True
dt1 > dt2                                 # False
dt1 == dt2                                # False
dt1 != dt2                                # True
dt1 <= dt2                                # True

# ═══════════════════════════════════════════════════════════════
# SORTING
# ═══════════════════════════════════════════════════════════════
dates = [
    datetime(2024, 3, 1),
    datetime(2024, 1, 1),
    datetime(2024, 2, 1)
]
sorted_dates = sorted(dates)              # Sorted chronologically

# ═══════════════════════════════════════════════════════════════
# CHECK IF IN TIME RANGE
# ═══════════════════════════════════════════════════════════════
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)
check = datetime(2024, 6, 15)

if start <= check <= end:
    print("In time range!")
```

---

## ⏲️ Unix Timestamps

```python
from datetime import datetime, timezone

# ═══════════════════════════════════════════════════════════════
# DATETIME → TIMESTAMP
# ═══════════════════════════════════════════════════════════════
now = datetime.now()
timestamp = now.timestamp()               # 1706277045.123456 (float)

# ═══════════════════════════════════════════════════════════════
# TIMESTAMP → DATETIME
# ═══════════════════════════════════════════════════════════════
dt = datetime.fromtimestamp(1706277045)   # Local time
dt_utc = datetime.fromtimestamp(1706277045, tz=timezone.utc)  # UTC

# ═══════════════════════════════════════════════════════════════
# WITH TIME MODULE
# ═══════════════════════════════════════════════════════════════
import time

current_timestamp = time.time()           # Seconds since 1970-01-01 00:00 UTC
time.sleep(1)                             # Pause for 1 second
```

---

## ⚠️ Common Pitfalls

```python
from datetime import datetime, timedelta, timezone

# ❌ WRONG: strptime format doesn't match
# datetime.strptime('2024/01/26', '%Y-%m-%d')  # ValueError!
datetime.strptime('2024/01/26', '%Y/%m/%d')   # ✅

# ❌ WRONG: .seconds vs .total_seconds()
delta = timedelta(days=1, hours=2)
print(delta.seconds)                      # 7200 (only the 2h, not the day!)
print(delta.total_seconds())              # 93600 ✅

# ❌ WRONG: Mixing naive and aware
naive = datetime.now()
aware = datetime.now(timezone.utc)
# naive - aware  # TypeError!

# ❌ WRONG: Using utcnow() (deprecated)
datetime.utcnow()                         # Returns naive datetime
datetime.now(timezone.utc)                # ✅ Returns aware datetime

# ❌ WRONG: Adding months with timedelta
# timedelta has no 'months' parameter!
# Use dateutil.relativedelta:
from dateutil.relativedelta import relativedelta
next_month = datetime.now() + relativedelta(months=1)

# ❌ WRONG: Changing year/month/day without validation
# date(2024, 2, 30)  # ValueError: day is out of range for month
```

---

## ✅ Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| `datetime.now(timezone.utc)` for UTC | `datetime.utcnow()` |
| ISO format for storage | Custom formats in DB |
| `total_seconds()` for calculations | `.seconds` for total duration |
| `fromisoformat()` for ISO strings | Manual parsing |
| Timezone-aware datetimes | Mix naive datetimes |
| `zoneinfo` (Python 3.9+) | Manual offset |

---

## 🎯 Exam Checklist

- [ ] `date`, `time`, `datetime`, `timedelta` differences
- [ ] `strftime()` for formatting, `strptime()` for parsing
- [ ] Format codes: `%Y`, `%m`, `%d`, `%H`, `%M`, `%S`
- [ ] `timedelta` for time calculations
- [ ] `total_seconds()` vs `.seconds` vs `.days`
- [ ] DateTime comparisons with `<`, `>`, `==`
- [ ] `timestamp()` and `fromtimestamp()`
- [ ] `isoformat()` and `fromisoformat()`
- [ ] `datetime.now(timezone.utc)` for UTC

---

[[12_Regular_Expressions|← Regular Expressions]] | [[00_Index|Index]] | [[14_Iterators_and_Generators|Iterators & Generators →]]
