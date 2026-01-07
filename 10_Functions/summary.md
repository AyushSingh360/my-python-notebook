# Summary – Functions

## Key Take-aways

### Core Concepts
- **Functions** are reusable blocks of code that perform specific tasks
- **First-class objects** in Python - can be assigned, passed, and returned
- **Parameters** allow functions to accept input; **return** sends output back
- **Scope (LEGB)**: Local → Enclosing → Global → Built-in
- **Docstrings** make functions self-documenting

### Advanced Concepts
- ***args** captures variable positional arguments as a tuple
- ****kwargs** captures variable keyword arguments as a dictionary
- **Recursion**: Functions calling themselves (need base case!)
- **Lambda**: Anonymous single-expression functions
- **Decorators**: Functions that modify other functions
- **Closures**: Functions that remember enclosing scope variables

## Syntax Quick Reference

```python
# Basic function
def function_name(param1, param2=default):
    """Docstring explaining the function."""
    result = param1 + param2
    return result

# All parameter types
def full_signature(pos_only, /, pos_or_kw, *args, kw_only, **kwargs):
    pass

# Lambda (anonymous function)
square = lambda x: x ** 2

# Decorator
@decorator_function
def my_function():
    pass

# Recursion
def factorial(n):
    if n == 0:
        return 1  # Base case
    return n * factorial(n-1)  # Recursive case
```

## Parameter Types Comparison

| Type | Syntax | Usage | Example |
|------|--------|-------|---------|
| **Positional** | `def f(a, b)` | Order matters | `f(1, 2)` |
| **Keyword** | `f(a=1, b=2)` | Named args | `f(b=2, a=1)` |
| **Default** | `def f(a=10)` | Optional | `f()` or `f(20)` |
| ***args** | `def f(*args)` | Variable positional | `f(1, 2, 3)` |
| ****kwargs** | `def f(**kw)` | Variable keyword | `f(a=1, b=2)` |
| **Positional-only** | `def f(a, /)` | Before `/` | `f(1)` not `f(a=1)` |
| **Keyword-only** | `def f(*, a)` | After `*` | `f(a=1)` not `f(1)` |

**Parameter Order Rule**:  
`pos_only, /, pos_or_kw, *args, kw_only, **kwargs`

## LEGB Scope Rule

Python searches for variables in this order:

1. **L**ocal: Inside current function
2. **E**nclosing: In outer (enclosing) functions  
3. **G**lobal: Module/script level
4. **B**uilt-in: Python's built-in names

```python
# Modifying scopes
global var_name    # Modify global variable
nonlocal var_name  # Modify enclosing scope variable
```

## Common Patterns

### 1. Function with Default Parameters
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

### 2. Return Multiple Values (Tuple)
```python
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([1, 5, 3, 9, 2])
```

### 3. *args for Flexible Arguments
```python
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4, 5)  # Works with any number of args
```

### 4. **kwargs for Flexible Keywords
```python
def print_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
```

### 5. Lambda for Simple Operations
```python
# Sorting by a key
students = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted_students = sorted(students, key=lambda s: s["age"])
```

### 6. Decorator Pattern
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Before function call
        result = func(*args, **kwargs)
        # After function call
        return result
    return wrapper

@decorator
def my_function():
    pass
```

### 7. Closure (Encapsulating State)
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
```

### 8. Recursive Base + Recursive Case
```python
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n-1)  # Recursive case
```

### 9. Higher-Order Function
```python
def apply_to_list(func, lst):
    return [func(item) for item in lst]

apply_to_list(lambda x: x**2, [1, 2, 3])  # [1, 4, 9]
```

### 10. Factory Function
```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_five = make_multiplier(5)
times_five(10)  # 50
```

## Function Types Comparison

| Type | Use Case | Example |
|------|----------|---------|
| **Regular** | Most common, reusable logic | `def add(a, b): return a + b` |
| **Lambda** | Short one-liners, callbacks | `lambda x: x ** 2` |
| **Recursive** | Tree/graph traversal, divide-and-conquer | `factorial`, `fibonacci` |
| **Higher-order** | Take/return functions | `map`, `filter`, `sorted` |
| **Generator** | Lazy evaluation, large datasets | `def gen(): yield value` |
| **Async** | Concurrent operations | `async def fetch(): await ...` |

## Best Practices Checklist

### Function Design:
- [ ] Single Responsibility Principle (one task per function)
- [ ] Descriptive names (`calculate_total` not `calc`)
- [ ] Docstrings with parameters and return value documented
- [ ] Keep functions short (< 20 lines ideally)
- [ ] Limit parameters (< 5 recommended)
- [ ] Use type hints for clarity: `def add(a: int, b: int) -> int:`

### Code Quality:
- [ ] Avoid modifying global state (prefer pure functions)
- [ ] Handle edge cases and errors
- [ ] Return consistent types
- [ ] Avoid deep nesting (max 2-3 levels)
- [ ] Use meaningful variable/parameter names

### Performance:
- [ ] Avoid unnecessary recursion (use loops when simpler)
- [ ] Consider memoization for expensive recursive functions
- [ ] Don't create functions inside loops (define outside)

## Common Pitfalls

❌ **Mutable default arguments:**
```python
# BAD
def append_to_list(item, lst=[]):
    lst.append(item)
    return lst

# lst is shared across calls!

# GOOD
def append_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

❌ **Missing base case in recursion:**
```python
# BAD - Infinite recursion!
def factorial(n):
    return n * factorial(n-1)

# GOOD
def factorial(n):
    if n == 0:  # Base case
        return 1
    return n * factorial(n-1)
```

❌ **Modifying variables without global/nonlocal:**
```python
# BAD - Creates local variable
count = 0
def increment():
    count += 1  # UnboundLocalError!

# GOOD
count = 0
def increment():
    global count
    count += 1
```

❌ **Too many return statements:**
```python
# BAD - Hard to follow
def check_value(x):
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    elif x < 10:
        return "small"
    elif x < 100:
        return "medium"
    else:
        return "large"

# BETTER - Use data structures
def check_value(x):
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    
    ranges = [(10, "small"), (100, "medium"), (float('inf'), "large")]
    for limit, label in ranges:
        if x < limit:
            return label
```

## When to Use What

| Scenario | Best Choice |
|----------|-------------|
| Reusable logic | Regular function with `def` |
| One-liner transformation | Lambda function |
| Need to remember state | Closure |
| Modify function behavior | Decorator |
| Tree/recursive structure | Recursive function |
| Sorting by custom key | Lambda in `sorted(key=...)` |
| Map/filter operations | Lambda or regular function |
| Unknown number of args | *args or **kwargs |

## Pro Tips

✅ **Use type hints** for better IDE support and documentation  
✅ **Write docstrings** - future you will thank present you  
✅ **Test with edge cases**: empty inputs, None, negative numbers  
✅ **Prefer pure functions** (no side effects) when possible  
✅ **Use `functools.lru_cache`** for automatic memoization  
✅ **Break complex functions** into smaller helper functions  
✅ **Document algorithms** with comments for non-obvious logic

## Further Reading

- Function annotations and type hints (PEP 484)
- Generator functions and iterators
- `functools` module (partial, reduce, wraps)
- Async functions with `async` and `await`
- Metaclasses and function factories
- Currying and partial application

---

**Remember**: Functions are the foundation of clean, maintainable code. Master these concepts and you'll write better Python!
