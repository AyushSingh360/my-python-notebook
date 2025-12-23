# Dictionaries

## 1. Topic definition
A dictionary is a mutable mapping of **hashable keys** to arbitrary values.

## 2. Why dictionaries exist
- Provide O(1) average lookup, insertion, and deletion.
- Model associative data such as JSON objects, configuration tables, and frequency counters.

## 3. Real‑world usage
- Storing configuration parameters.
- Counting word frequencies in text analysis.
- Representing API responses.

## 4. Key rules & syntax
| Rule | Example |
|------|---------|
| Literal | `{"a": 1, "b": 2}` |
| Access | `d["a"]` |
| Get with default | `d.get("c", 0)` |
| Update | `d.update({"c": 3})` |
| Delete | `del d["b"]` |
| Dictionary comprehension | `{k: v*2 for k, v in d.items()}` |

## 5. Step‑by‑step explanation of examples
See **examples.py**.

## 6. Chapter layout
Same as other chapters.
