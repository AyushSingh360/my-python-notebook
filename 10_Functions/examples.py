# Comprehensive Function Examples

# ==========================================
# 1. Basic Definition & Return
# ==========================================
def greet(name):
    """Simple greeting function."""
    return f"Hello, {name}!"

print(greet("Alice"))

# ==========================================
# 2. Default Parameters (and the Mutable Trap)
# ==========================================
def safe_append(item, lst=None):
    """Correct way to handle mutable default args."""
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(f"List 1: {safe_append(1)}")
print(f"List 2: {safe_append(2)}") # New list, distinct from List 1

# ==========================================
# 3. Variable Arguments (*args & **kwargs)
# ==========================================
def super_func(required, *args, **kwargs):
    """
    required: regular argument
    *args: tuple of positional arguments
    **kwargs: dictionary of keyword arguments
    """
    print(f"Req: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

super_func("Start", 1, 2, 3, mode="debug", verbose=True)

# ==========================================
# 4. Scope (LEGB Rule)
# ==========================================
x = "Global"

def outer():
    x = "Enclosing"
    
    def inner():
        x = "Local"
        print(f"Inner: {x}")
    
    inner()
    print(f"Outer: {x}")

outer()
print(f"Global: {x}")

# ==========================================
# 5. Lambda Functions
# ==========================================
# Anonymous one-line functions
add = lambda a, b: a + b
print(f"Lambda add: {add(5, 3)}")

# Often used with map/filter
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(f"Squared map: {squared}")

# ==========================================
# 6. Documentation & Type Hints
# ==========================================
def calculate_area(width: float, height: float) -> float:
    """
    Calculate area of a rectangle.
    
    Args:
        width: The width of rectangle
        height: The height of rectangle
        
    Returns:
        The calculated area
    """
    return width * height

print(f"Area: {calculate_area(10.5, 2.0)}")
