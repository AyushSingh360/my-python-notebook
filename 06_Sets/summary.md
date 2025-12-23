# Summary – Sets

## Take‑aways
- Sets store **unique** hashable items.
- No indexing/slicing (unordered).
- Fast membership testing and mathematical operations.

## Syntax recap
```python
s = {1, 2, 3}
s.add(4)
if 2 in s: ...
union = s | {5,6}
```

## Checklist
- [ ] Use `set()` for an empty set (not `{}`).
- [ ] Ensure set elements are immutable.
- [ ] Use `discard` for safe removal.
