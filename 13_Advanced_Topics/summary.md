# Summary – Advanced Python Topics

## 1. Iterators & Generators

- **Iterator Protocol**: Objects with `__iter__` and `__next__`.
- **Generator**: Function using `yield`. Saves memory, lazy evaluation.

```python
# Generator Function
def my_gen():
    yield 1
    yield 2

# Generator Expression
gen = (x**2 for x in range(10))
```

## 2. Decorators

Functions that wrap other functions.

```python
# Syntax
@my_decorator
def my_func():
    pass

# Template
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Pre-processing
        result = func(*args, **kwargs)
        # Post-processing
        return result
    return wrapper
```

## 3. Context Managers

Manage resources automatically (setup/teardown).

```python
# Built-in
with open('file.txt') as f:
    content = f.read()

# Custom Class
class MyContext:
    def __enter__(self):
        print("Enter")
        return self
    def __exit__(self, exc_type, exc_val, tb):
        print("Exit")
```

## 4. Error Handling

Pattern for robust code.

```python
try:
    # Code that might fail
    x = 1 / 0
except ZeroDivisionError as e:
    # Handle specific error
    print("Zero error")
except Exception as e:
    # Handle generic error
    print("Error")
else:
    # Runs if NO error
    print("Success")
finally:
    # Runs ALWAYS
    print("Cleanup")
```

## 5. Functional Tools

- **Lambda**: `lambda args: expression`
- **Map**: `map(func, iter)` -> apply function to all
- **Filter**: `filter(func, iter)` -> keep items where func is True
- **Comprehensions**: `[x for x in list if condition]`

## 6. Type Hinting (Python 3.5+)

```python
def greet(name: str) -> str:
    return "Hello " + name

# Generics
from typing import List, Dict, Optional
def process(items: List[int]) -> Optional[int]:
    return items[0] if items else None
```

## Best Practices

✅ Use `with` statements for files/locks/sockets.  
✅ Use `try...except` blocks where errors are expected (EAFP).  
✅ Use generators for large datasets.  
✅ Use list comprehensions for simple loops (readability).  
✅ Avoid bare `except:` (always catch `Exception` or specific types).  
✅ Use `@wraps` when writing decorators to preserve metadata.
