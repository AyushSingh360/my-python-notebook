# Summary – Tuples

## Take‑aways
- Tuples are immutable and hashable (if they contain only immutable items).
- Use a trailing comma for single‑element tuples `(x,)`.
- Ideal for returning multiple values and as dictionary keys.

## Syntax recap
```python
t = (1, 2, 3)
a, b, c = t         # unpacking
new = t + (4,)      # concatenation
```

## Checklist
- [ ] Remember the comma for one‑element tuples.
- [ ] Do not attempt to modify tuple items directly.
- [ ] Use tuples for fixed collections (e.g., coordinates).
