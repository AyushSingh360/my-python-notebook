# Solutions – Modules

import math
import sys
import os
import json
import importlib

# =============================================================================
# EASY LEVEL
# =============================================================================

# 1. Basic Import
print("=== Exercise 1: Basic Import ===")
import math
print(f"Value of pi: {math.pi}")

# 2. Specific Import
print("\n=== Exercise 2: Specific Import ===")
from math import sqrt
print(f"Square root of 144: {sqrt(144)}")

# 3. Import with Alias
print("\n=== Exercise 3: Import with Alias ===")
import datetime as dt
print(f"Current date: {dt.date.today()}")

# 4. Multiple Imports
print("\n=== Exercise 4: Multiple Imports ===")
from random import randint, choice
print(f"Random number (1-10): {randint(1, 10)}")
print(f"Random choice: {choice(['a', 'b', 'c'])}")

# 5. __name__ Guard
print("\n=== Exercise 5: __name__ Guard ===")
# Create this in a separate file:
"""
# my_script.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Alice"))  # Only runs when executed directly
"""
print("See example above - demonstrates __name__ guard pattern")

# =============================================================================
# MEDIUM LEVEL
# =============================================================================

# 6. Create a Module
print("\n=== Exercise 6: Create a Module ===")
# Create utils.py:
"""
# utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""

# Then use it:
"""
import utils
print(utils.add(5, 3))      # 8
print(utils.subtract(10, 4))  # 6
"""
print("Create utils.py and import it as shown above")

# 7. Package Creation
print("\n=== Exercise 7: Package Creation ===")
# Directory structure:
"""
mypackage/
├── __init__.py
├── math_utils.py
└── string_utils.py

# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# string_utils.py
def uppercase(s):
    return s.upper()

def reverse(s):
    return s[::-1]
"""
print("Package structure created as shown above")

# 8. __init__.py Usage
print("\n=== Exercise 8: __init__.py Usage ===")
"""
# mypackage/__init__.py
from .math_utils import add, multiply
from .string_utils import uppercase, reverse

__all__ = ['add', 'multiply', 'uppercase', 'reverse']

# Now you can import directly:
from mypackage import add, uppercase
"""
print("__init__.py allows convenient imports")

# 9. Relative Imports
print("\n=== Exercise 9: Relative Imports ===")
"""
myproject/
├── __init__.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
└── models/
    ├── __init__.py
    └── user.py

# In models/user.py:
from ..utils import helpers  # Parent package
from . import __init__       # Same package
"""
print("Use . for current package, .. for parent")

# 10. sys.path Exploration
print("\n=== Exercise 10: sys.path Exploration ===")
print("sys.path contents:")
for i, path in enumerate(sys.path, 1):
    print(f"{i}. {path}")

# 11. Standard Library: os.path
print("\n=== Exercise 11: os.path.join ===")
file_path = os.path.join('folder', 'subfolder', 'file.txt')
print(f"Cross-platform path: {file_path}")

# 12. JSON Module
print("\n=== Exercise 12: JSON Module ===")
data = {"name": "Alice", "age": 30, "city": "NYC"}

# Save to file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Read from file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)

print(f"Original: {data}")
print(f"Loaded: {loaded_data}")

# =============================================================================
# HARD LEVEL
# =============================================================================

# 13. Custom Package Structure
print("\n=== Exercise 13: Custom Package Structure ===")
"""
calculator/
├── __init__.py
├── operations/
│   ├── __init__.py
│   ├── basic.py
│   └── advanced.py
└── utils.py

# operations/basic.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# operations/advanced.py
import math

def power(base, exponent):
    return base ** exponent

def sqrt(n):
    return math.sqrt(n)

# calculator/__init__.py
from .operations.basic import add, subtract, multiply, divide
from .operations.advanced import power, sqrt

__all__ = ['add', 'subtract', 'multiply', 'divide', 'power', 'sqrt']
"""
print("Calculator package structure created")

# 14. Conditional Import
print("\n=== Exercise 14: Conditional Import ===")
try:
    import numpy as np
    HAS_NUMPY = True
    print("NumPy is available")
except ImportError:
    HAS_NUMPY = False
    print("NumPy not available, using standard lists")

def create_array(data):
    if HAS_NUMPY:
        return np.array(data)
    else:
        return list(data)

# 15. Dynamic Import
print("\n=== Exercise 15: Dynamic Import ===")
module_name = "math"
imported_module = importlib.import_module(module_name)
print(f"Dynamically imported {module_name}")
print(f"Pi from dynamic import: {imported_module.pi}")

# 16. __all__ Definition
print("\n=== Exercise 16: __all__ Definition ===")
"""
# my_module.py
__all__ = ['public_function']

def public_function():
    return "This is public"

def _private_function():
    return "This is private"

def another_function():
    return "Also private (not in __all__)"

# Usage:
from my_module import *  # Only imports public_function
"""
print("Use __all__ to control what's exported")

# 17. Module Reload
print("\n=== Exercise 17: Module Reload ===")
"""
import my_module
# ... make changes to my_module.py ...
import importlib
importlib.reload(my_module)  # Reload without restarting Python
"""
print("Use importlib.reload() to reload modified modules")

# 18. Virtual Environment
print("\n=== Exercise 18: Virtual Environment ===")
"""
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\\Scripts\\activate

# Activate (Linux/Mac)
source myenv/bin/activate

# Install package
pip install requests

# Freeze requirements
pip freeze > requirements.txt

# Deactivate
deactivate

# Later, recreate environment:
python -m venv newenv
source newenv/bin/activate
pip install -r requirements.txt
"""
print("Virtual environment workflow shown above")

# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# 19. Plugin System
print("\n=== Exercise 19: Plugin System ===")
"""
# plugin_loader.py
import os
import importlib.util

def load_plugins(plugin_dir='plugins'):
    plugins = []
    for filename in os.listdir(plugin_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            filepath = os.path.join(plugin_dir, filename)
            module_name = filename[:-3]
            
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            plugins.append(module)
    
    return plugins

# Usage:
plugins = load_plugins()
for plugin in plugins:
    if hasattr(plugin, 'run'):
        plugin.run()
"""
print("Plugin system loads modules dynamically from directory")

# 20. Namespace Package
print("\n=== Exercise 20: Namespace Package ===")
"""
# Python 3.3+ supports namespace packages (no __init__.py)
# Structure:
mypackage/
├── subpackage1/
│   └── module1.py
└── subpackage2/
    └── module2.py

# Import still works:
from mypackage.subpackage1 import module1
"""
print("Namespace packages don't require __init__.py")

# 21. Module Introspection
print("\n=== Exercise 21: Module Introspection ===")
print(f"Math module attributes: {dir(math)[:5]}...")  # First 5
print(f"Math module docstring: {math.__doc__[:50]}...")

# 22. Circular Import Resolution
print("\n=== Exercise 22: Circular Import Resolution ===")
"""
# BAD: a.py and b.py import each other at module level

# SOLUTION 1: Import inside function
# a.py
def function_a():
    from b import function_b  # Local import
    return function_b()

# b.py
def function_b():
    from a import function_a  # Local import
    return "B"

# SOLUTION 2: Restructure to avoid circular dependency
# Extract shared code to c.py
"""
print("Resolve circular imports with local imports or restructuring")

print("\n=== All Solutions Complete! ===")
