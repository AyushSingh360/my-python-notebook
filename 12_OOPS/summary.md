# Summary – Object-Oriented Programming

## Key Vocabulary

- **Class**: Blueprint for objects (`class Dog:`)
- **Object**: Instance of a class (`my_dog = Dog()`)
- **Attribute**: Variable belonging to an object (`self.name`)
- **Method**: Function belonging to an object (`def bark(self):`)
- **self**: Reference to the current instance
- **__init__**: Constructor method, runs on creation
- **Instantiation**: The act of creating an object

## The 4 Pillars

1.  **Encapsulation**: Hiding internals. Use `_variable` (protected) or `__variable` (private).
2.  **Abstraction**: Hiding complexity. Use Abstract Base Classes (`ABC`).
3.  **Inheritance**: Reusing code. `class Child(Parent):`.
4.  **Polymorphism**: Unified interface. Same method name, different behaviors.

## Magic Methods (Dunder) Cheat Sheet

| Method | Purpose | Usage |
| ... | ... | ... |
| `__new__` | Allocator | Before `__init__` |
| `__init__` | Initializer | `x = Class()` |
| `__str__` | String Repr | `print(x)` |
| `__repr__` | Official Repr | `repr(x)` |
| `__len__` | Length | `len(x)` |
| `__eq__` | Equality | `x == y` |
| `__lt__`, `__gt__` | Comparison | `x < y`, `x > y` |
| `__add__` | Addition | `x + y` |
| `__getitem__` | Indexing | `x[key]` |
| `__call__` | Callable | `x()` |

## Class Decorators

```python
@property           # Define a getter
@name.setter        # Define a setter
@classmethod        # Method taking 'cls', usually factories
@staticmethod       # Regular function inside class namespace
```

## Types of Inheritance

-   **Single**: One parent.
-   **Multiple**: `class Child(Mom, Dad)`
-   **Multilevel**: Grandparent -> Parent -> Child
-   **Hierarchical**: One Parent -> Many Children

## Design Principles (SOLID)

-   **S**ingle Responsibility
-   **O**pen/Closed
-   **L**iskov Substitution
-   **I**nterface Segregation
-   **D**ependency Inversion

## Common Pitfalls

❌ **Mutable Class Attributes**:
```python
class Bad:
    items = [] # Shared by ALL instances!

# Use instance attributes instead:
class Good:
    def __init__(self):
        self.items = []
```

❌ **Forgetting `self`**:
```python
def my_method(): # Error!
def my_method(self): # Correct
```

❌ **Direct Private Access**:
Trying to access `obj.__private` raises generic AttributeError. Use getters/setters.
