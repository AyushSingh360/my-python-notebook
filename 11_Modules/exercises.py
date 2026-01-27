# Exercises – Modules
import sys
import os
import importlib

# Helper to print section headers
def print_header(title):
    print(f"\n=== {title} ===")

# =============================================================================
# EASY LEVEL
# =============================================================================

def exercise_1():
    """
    1. Basic Import
    Import the `math` module and print the value of pi.
    """
    print_header("Exercise 1: Basic Import")
    # Write your code here
    pass

def exercise_2():
    """
    2. Specific Import
    Import only `sqrt` from math and calculate the square root of 144.
    """
    print_header("Exercise 2: Specific Import")
    # Write your code here
    pass

def exercise_3():
    """
    3. Import with Alias
    Import `datetime` as `dt` and print the current date.
    """
    print_header("Exercise 3: Import with Alias")
    # Write your code here
    pass

def exercise_4():
    """
    4. Multiple Imports
    Import both `randint` and `choice` from the `random` module.
    Generate a random number between 1-10 and choose randomly from ['a', 'b', 'c'].
    """
    print_header("Exercise 4: Multiple Imports")
    # Write your code here
    pass

def exercise_5():
    """
    5. __name__ Guard
    Explain (in a comment) why we use `if __name__ == "__main__":`.
    """
    print_header("Exercise 5: __name__ Guard")
    # Write your answer here
    pass

# =============================================================================
# MEDIUM LEVEL
# =============================================================================

def exercise_6():
    """
    6. Create a Module
    Create a file named `utils.py` (manually) with a function `add(a, b)`.
    Then import it here and use the `add` function.
    Note: You might need to adjust sys.path or ensure the file is in the same directory.
    """
    print_header("Exercise 6: Create a Module")
    # Write your code here
    pass

def exercise_7():
    """
    7. Package Creation
    Create a folder `mypackage` with empty `__init__.py` and a module `math_utils.py`.
    Add `multiply(a, b)` to `math_utils.py`.
    Import and use it here.
    """
    print_header("Exercise 7: Package Creation")
    # Write your code here
    pass

def exercise_8():
    """
    8. __init__.py Usage
    Modify `mypackage/__init__.py` to import `multiply` from `math_utils`.
    Then import `multiply` directly from `mypackage` here.
    """
    print_header("Exercise 8: __init__.py Usage")
    # Write your code here
    pass

def exercise_9():
    """
    9. Relative Imports
    Explain (in a comment) the difference between `from . import module` and `from .. import module`.
    """
    print_header("Exercise 9: Relative Imports")
    # Write your answer here
    pass

def exercise_10():
    """
    10. sys.path Exploration
    Print the contents of `sys.path`.
    """
    print_header("Exercise 10: sys.path Exploration")
    # Write your code here
    pass

def exercise_11():
    """
    11. Standard Library: os.path
    Use `os.path.join` to create a path 'folder/subfolder/file.txt' correctly (cross-platform).
    """
    print_header("Exercise 11: os.path.join")
    # Write your code here
    pass

def exercise_12():
    """
    12. JSON Module
    Create a dictionary, save it to 'data.json' using `json.dump`, 
    then read it back using `json.load`.
    """
    print_header("Exercise 12: JSON Module")
    # Write your code here
    pass

# =============================================================================
# HARD LEVEL
# =============================================================================

def exercise_13():
    """
    13. Custom Package Structure
    Create a more complex package structure with subpackages.
    Explain (in a comment) how you would structure a 'calculator' package with 
    'basic' and 'advanced' operations.
    """
    print_header("Exercise 13: Custom Package Structure")
    # Write your description or code here
    pass

def exercise_14():
    """
    14. Conditional Import
    Try to import `numpy`. If it fails (ImportError), set a flag `HAS_NUMPY` to False.
    Print whether NumPy is available.
    """
    print_header("Exercise 14: Conditional Import")
    # Write your code here
    pass

def exercise_15():
    """
    15. Dynamic Import
    Use `importlib.import_module` to import the 'math' module using a string variable.
    Print `math.pi` from the imported module.
    """
    print_header("Exercise 15: Dynamic Import")
    # Write your code here
    pass

def exercise_16():
    """
    16. __all__ Definition
    Explain (in a comment) what the `__all__` list controls in a module.
    """
    print_header("Exercise 16: __all__ Definition")
    # Write your answer here
    pass

def exercise_17():
    """
    17. Module Reload
    Explain (in a comment) when and how to use `importlib.reload()`.
    """
    print_header("Exercise 17: Module Reload")
    # Write your answer here
    pass

def exercise_18():
    """
    18. Virtual Environment
    List the commands (in comments) to create and activate a virtual environment.
    """
    print_header("Exercise 18: Virtual Environment")
    # Write your commands here
    pass

# =============================================================================
# BONUS CHALLENGES
# =============================================================================

def exercise_19():
    """
    19. Plugin System
    Describe how you would implement a simple plugin system that loads all .py files 
    from a 'plugins' directory.
    """
    print_header("Exercise 19: Plugin System")
    # Write your description here
    pass

def exercise_20():
    """
    20. Namespace Package
    Explain what a namespace package is (Python 3.3+).
    """
    print_header("Exercise 20: Namespace Package")
    # Write your answer here
    pass

def exercise_21():
    """
    21. Module Introspection
    Use `dir()` to print the attributes of the `math` module.
    """
    print_header("Exercise 21: Module Introspection")
    # Write your code here
    pass

def exercise_22():
    """
    22. Circular Import Resolution
    Explain two ways to resolve a circular import error.
    """
    print_header("Exercise 22: Circular Import Resolution")
    # Write your answer here
    pass

if __name__ == '__main__':
    # Run exercises
    exercise_1()
    exercise_2()
    # ... call other exercises as needed or let the user call them
    print("\nRun specific exercises by calling the functions above!")
