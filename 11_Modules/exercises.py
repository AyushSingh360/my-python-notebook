# Exercises – Modules

## Easy Level

### 1. Basic Import
Import the `math` module and print the value of pi.

### 2. Specific Import
Import only `sqrt` from math and calculate the square root of 144.

### 3. Import with Alias
Import `datetime` as `dt` and print the current date.

### 4. Multiple Imports
Import both `randint` and `choice` from the `random` module. Generate a random number between 1-10 and choose randomly from `['a', 'b', 'c']`.

### 5. __name__ Guard
Create a file with a function and use `if __name__ == "__main__":` to call it only when executed directly.

## Medium Level

### 6. Create a Module
Create `utils.py` with functions `add(a, b)` and `subtract(a, b)`. Import and use them in another file.

### 7. Package Creation
Create a package `mypackage` with two modules: `math_utils.py` and `string_utils.py`. Each should have at least 2 functions.

### 8. __init__.py Usage
Add an `__init__.py` to your package that imports functions from sub-modules for easier access.

### 9. Relative Imports
Create a package with nested modules and use relative imports (`.` and `..`).

### 10. sys.path Exploration
Print `sys.path` and explain what each entry represents.

### 11. Standard Library
Use `os.path.join()` to create a cross-platform file path.

### 12. JSON Module
Create a dictionary, save it to a JSON file, then read it back.

## Hard Level

### 13. Custom Package Structure
Create a package structure:
```
calculator/
├──__init__.py
├── operations/
│   ├── __init__.py
│   ├── basic.py
│   └── advanced.py
└── utils.py
```
Implement add, subtract, multiply, divide, power, and sqrt functions.

### 14. Conditional Import
Write code that tries to import `numpy`, and if not available, uses standard lists instead.

### 15. Dynamic Import
Use `importlib.import_module()` to import a module whose name is provided as a string.

### 16. __all__ Definition
Create a module with multiple functions but use `__all__` to export only specific ones.

### 17. Module Reload
Use `importlib.reload()` to reload a modified module without restarting Python.

### 18. Virtual Environment
Create a virtual environment, activate it, install a package, freeze requirements, and deactivate.

## Bonus Challenges

### 19. Plugin System
Create a simple plugin system that automatically loads all modules from a `plugins/` directory.

### 20. Namespace Package
Create a namespace package (package without `__init__.py` in Python 3.3+).

### 21. Module Introspection
Use `dir(module)` and `help(module)` to explore a module's contents programmatically.

### 22. Circular Import Resolution
Create two modules with circular dependencies and resolve it using local imports.

**See `solutions.py` for complete solutions!**
