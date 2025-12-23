# File Handling

## 1. Topic definition
File handling allows searching, reading, writing, and appending data to files on the persistent storage.

## 2. Why it exists
- **Persistence**: Save user data, configurations, or game state between runs.
- **Data Exchange**: Read CSVs, logs, or other input formats.

## 3. Real‑world usage
- A logger writing errors to `error.log`.
- An app reading `settings.config`.
- Exporting a report to `.csv`.

## 4. Key rules & syntax
```python
with open("file.txt", "mode") as f:
    data = f.read()
```
- Modes: `'r'` (read), `'w'` (write/overwrite), `'a'` (append), `'rb'`/`'wb'` (binary).
- Always use the `with` statement to ensure the file closes automatically.

## 5. Step‑by‑step explanation of examples
See **examples.py**.

## 6. Chapter layout
Standard layout.
