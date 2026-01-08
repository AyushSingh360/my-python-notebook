# Summary – Modules

## Key Take-aways

- **Modules** = Python files with reusable code (.py files)
- **Packages** = Directories with `__init__.py` + modules
- **Import mechanisms**: `import`, `from...import`, aliases
- **`__name__`** = `"__main__"` when executed directly, module name when imported
- **sys.path** = Module search path (current dir → PYTHONPATH → stdlib → site-packages)

## Import Syntax Reference

```python
# Basic import
import module
module.function()

# Specific import
from module import function
function()

# Import with alias
import module as alias
alias.function()

# Multiple imports
from module import func1, func2, Class1

# Import all (avoid!)
from module import *
```

## Package Structure

```
mypackage/
├── __init__.py          # Makes it a package
├── module1.py
├── subpackage/
│   ├── __init__.py
│   └── module2.py
└── utils.py
```

## Absolute vs Relative Imports

```python
# Absolute (recommended)
from mypackage.subpackage import module2

# Relative
from . import module1        # Same directory
from .. import utils        # Parent directory
from ..subpackage import module2
```

## __name__ Pattern

```python
def main():
    """Entry point."""
    pass

if __name__ == "__main__":
    main()  # Only runs when executed directly
```

## sys.path Order

1. Current directory
2. PYTHONPATH environment variable
3. Standard library directory
4. Site-packages (third-party)

## Common Standard Library Modules

| Module | Purpose |
|--------|---------|
| `math` | Mathematical functions |
| `random` | Random numbers |
| `os` | OS interface |
| `sys` | System parameters |
| `datetime` | Date/time |
| `json` | JSON data |
| `re` | Regular expressions |
| `pathlib` | File paths |

## pip Commands

```bash
pip install package
pip uninstall package
pip install -r requirements.txt
pip freeze > requirements.txt
pip list
```

## Virtual Environments

```bash
# Create
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Linux/Mac)
source myenv/bin/activate

# Deactivate
deactivate
```

## Best Practices

✅ Use meaningful module names (lowercase_with_underscores)  
✅ One module per logical component  
✅ Use `__init__.py` to simplify imports  
✅ Prefer absolute imports  
✅ Use `if __name__ == "__main__":` for scripts  
✅ Document modules with docstrings  
✅ Use virtual environments  

❌ Avoid circular imports  
❌ Avoid `from module import *`  
❌ Don't name modules like stdlib (e.g., `random.py`)  
❌ Don't modify sys.path unless necessary

## Common Patterns

### Pattern 1: Conditional Import
```python
try:
    import numpy as np
except ImportError:
    np = None  # Fallback
```

### Pattern 2: Lazy Import
```python
def heavy_function():
    import heavy_module  # Import when needed
    return heavy_module.process()
```

### Pattern 3: __all__ Export Control
```python
# module.py
__all__ = ['public_func']  # Only export this

def public_func():
    pass

def _private_func():
    pass
```

## Troubleshooting

**ModuleNotFoundError**:
- Check spelling
- Verify module in sys.path
- Install if third-party: `pip install module`
- Check `__init__.py` exists

**Circular Import**:
- Restructure code
- Use local import inside function
- Import at module level, use at function level

**Import from parent directory**:
- Use proper package structure
- Avoid modifying sys.path
- Run from project root

---

**Master modules to write organized, maintainable Python code!**
