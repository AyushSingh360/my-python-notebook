# Summary – File Handling

## Take‑aways
- **Persistence** is key for real apps.
- **Context Managers** (`with`) are mandatory for safety.
- **Modes**: `r` (read), `w` (overwrite), `a` (append), `b` (binary).

## Syntax recap
```python
with open("file.txt", "r") as f:
    lines = f.readlines()
```

## Checklist
- [ ] Use `with` always.
- [ ] Handle `FileNotFoundError`.
- [ ] Be careful with `w` mode (it clears the file).
