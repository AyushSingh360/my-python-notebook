## 1. Topic Definition
A **String** in Python is an immutable sequence of Unicode characters. Python 3 treats all strings as Unicode by default, allowing for international character support.

## 2. Why Strings Exist
- To represent and manipulate text-based data.
- To handle communication between humans and machines (I/O).
- To store structured text formats like JSON, HTML, or CSV.

## 3. Real-World Usage
- Web development (rendering HTML templates).
- Data Science (parsing log files and cleaning datasets).
- Natural Language Processing (analyzing human speech or writing).

## 4. Technical Architecture: Unicode & Indexing
Python strings are highly optimized. Each character has a unique Unicode code point, and Python uses different internal representations (Latin-1, UCS-2, or UCS-4) depending on the characters present to save memory.

![Python String Handling: Unicode, UTF-8, and Indexing](./assets/string_encoding_indexing.png)

## 5. Key Rules & Syntax

### 5.1. Creating Strings
- **Single/Double Quotes**: `'Hello'` or `"World"` (identical).
- **Triple Quotes**: `'''Multi-line content'''` (useful for docstrings).
- **f-strings (Recommended)**: `f"Value: {x}"` for fast interpolation.

### 5.2. Core String Methods
| Method | Description | Example |
|--------|-------------|---------|
| `strip()` | Removes leading/trailing whitespace. | `" hello ".strip()` -> `"hello"` |
| `lower()` / `upper()` | Case conversion. | `"Hi".lower()` -> `"hi"` |
| `replace(a, b)` | Replaces substring `a` with `b`. | `"cat".replace("c", "b")` -> `"bat"` |
| `split(sep)` | Splits string into a list. | `"a,b".split(",")` -> `["a", "b"]` |
| `join(list)` | Joins a list into a string. | `"-".join(["a", "b"])` -> `"a-b"` |

## 6. String Immutability
Once a string is created, **it cannot be modified**. Any operation that seems to "change" a string actually creates a brand new string object in memory.
```python
s = "Hello"
s[0] = "h"  # Raises TypeError
```

## 7. Step‑by‑step explanation of examples
See **examples.py** for practical usage of slicing, formatting, and methods.

## 8. Chapter layout
Standard academic layout.
