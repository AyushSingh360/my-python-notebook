# Object-Oriented Programming (OOP)

## 1. Topic definition
OOP organizes software design around "objects", which contain data (attributes) and methods (code).

## 2. Why OOP exists
- **Encapsulation**: Bundling data and methods.
- **Inheritance**: Reuse code from existing classes.
- **Polymorphism**: Interchange objects with shared interfaces.

## 3. Real‑world usage
- A `User` class handling authentication and profile data.
- A `Widget` hierarchy in a GUI library.
- Game entities (Player, Enemy) sharing a base `Entity` class.

## 4. Key rules & syntax
```python
class Name(Parent):
    def __init__(self, arg):
        self.arg = arg
    def method(self):
        pass
```
- `self` refers to the instance.
- `__init__` initializes the object.
- Inheritance is defined in parentheses `class Child(Parent):`.

## 5. Step‑by‑step explanation of examples
See **examples.py**.

## 6. Chapter layout
Standard layout.
