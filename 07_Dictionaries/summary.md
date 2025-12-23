# Summary – Dictionaries

## Take‑aways
- **Keys** must be immutable hashables.
- Lookups are effectively O(1).
- Use `d.get(k, default)` to handle missing keys gracefully.
- Merging via `d1 | d2` (Python 3.9+) or `d1.update(d2)`.

## Syntax recap
```python
d = {"a": 1}
val = d["a"]
d["b"] = 2
if "b" in d: ...
```

## Checklist
- [ ] Check if keys are hashable (strings, numbers, tuples).
- [ ] Handle potential KeyErrors.
- [ ] Use dict comprehensions for efficient mapping.
