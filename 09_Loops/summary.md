# Summary – Loops

## Key Take-aways

### Core Concepts
- **`for` loops** iterate over sequences (lists, strings, ranges) - use when you know the collection
- **`while` loops** repeat based on conditions - use when the number of iterations is unknown
- **Iterator protocol** (`__iter__()` and `__next__()`) powers all for loops in Python
- **Loop control**: `break` exits immediately, `continue` skips to next iteration, `else` runs if no break

### Performance & Best Practices
- **Nested loops** multiply time complexity: O(n) → O(n²) → O(n³)
- **Always ensure termination** - update loop variables in `while` loops to avoid infinite loops
- **Use built-in functions**: `range()`, `enumerate()`, `zip()` for cleaner, more efficient code
- **List comprehensions** are preferred for simple transformations and filtering

## Syntax Quick Reference

```python
# For loop - iterate over sequence
for item in iterable:
    process(item)

# While loop - repeat on condition
while condition:
    do_something()
    update_condition()  # Important!

# Loop control
for item in collection:
    if invalid(item):
        continue  # Skip this iteration
    if found(item):
        break     # Exit loop
else:
    print("Completed normally")  # Runs if NO break

# Built-in helpers
for index, value in enumerate(items):
    print(f"{index}: {value}")

for x, y in zip(list1, list2):
    print(f"{x} → {y}")

# Range variations
range(5)           # 0, 1, 2, 3, 4
range(2, 8)        # 2, 3, 4, 5, 6, 7
range(0, 10, 2)    # 0, 2, 4, 6, 8
range(10, 0, -1)   # 10, 9, 8, ..., 1
```

## Common Loop Patterns

### 1. Accumulator Pattern
```python
total = 0
for num in numbers:
    total += num
```

### 2. Search with break/else
```python
for item in collection:
    if item == target:
        print("Found!")
        break
else:
    print("Not found")
```

### 3. Filter Pattern
```python
results = []
for item in items:
    if condition(item):
        results.append(item)
# Or: results = [item for item in items if condition(item)]
```

### 4. Transform Pattern
```python
transformed = []
for item in items:
    transformed.append(transform(item))
# Or: transformed = [transform(item) for item in items]
```

### 5. Enumerate for Index
```python
for i, value in enumerate(values):
    print(f"Index {i}: {value}")
```

### 6. Zip for Parallel Iteration
```python
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

### 7. Nested Loops
```python
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = compute(i, j)
```

### 8. Input Validation Loop
```python
while True:
    value = input("Enter positive number: ")
    if value.isdigit() and int(value) > 0:
        break
    print("Invalid, try again")
```

## Time Complexity Comparison

| Loop Type | Time Complexity | Example |
|-----------|----------------|---------|
| Single loop | O(n) | `for i in range(n)` |
| Nested (2 levels) | O(n²) | `for i: for j:` |
| Triple nested | O(n³) | `for i: for j: for k:` |

## When to Use What

| Scenario | Best Choice | Why |
|----------|-------------|-----|
| Known collection | `for` loop | Iterates over items directly |
| Unknown iterations | `while` loop | Repeats until condition met |
| Need index + value | `enumerate()` | Provides both automatically |
| Parallel iteration | `zip()` | Combines multiple iterables |
| Simple transformation | List comprehension | More concise and Pythonic |
| Complex logic | Traditional loop | Better readability |
| Numeric sequence | `range()` | Memory-efficient generator |

## Common Pitfalls Checklist

- [ ] **Infinite loops**: Ensure `while` loop variables change to eventually make condition False
- [ ] **Off-by-one errors**: Remember `range(10)` gives 0-9, not 1-10
- [ ] **Modifying while iterating**: Don't add/remove from list during iteration (use copy or comprehension)
- [ ] **Deep nesting**: Avoid more than 2-3 levels; consider extracting to functions
- [ ] **Incorrect range**: `range(1, 10)` excludes 10; use `range(1, 11)` for 1-10
- [ ] **Break without else**: The `else` clause only runs if loop completes normally (no break)
- [ ] **continue in wrong place**: Ensure `continue` doesn't skip critical updates

## Pro Tips

✅ **Use `enumerate()`** instead of `range(len(list))` for cleaner code  
✅ **Use `zip()`** instead of parallel indexing for multiple lists  
✅ **Use comprehensions** for simple transformations (more Pythonic)  
✅ **Use `for...else`** for search patterns (cleaner than flag variables)  
✅ **Test edge cases**: Empty collections, single items, large datasets  
✅ **Consider generators** for memory-efficient iteration over large datasets

## Further Reading

- Iterator protocol and custom iterators
- Generator functions with `yield`
- `itertools` module for advanced iteration patterns
- Performance optimization with NumPy for numerical loops
- List/dict/set comprehensions as loop alternatives

---

**Remember**: Loops are fundamental to programming. Master these patterns and you'll write cleaner, more efficient Python code!
