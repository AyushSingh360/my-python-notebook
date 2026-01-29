# Common Beginner Mistakes in Advanced Python

import functools

print("\n=== Mistake 1: Consuming a Generator Twice ===")
# Generators are "one-time use". Once exhausted, they are empty.
gen = (x for x in range(3))
print(f"First run: {list(gen)}")
print(f"Second run: {list(gen)}") # Empty!
print("Fix: Create a new generator or use a list/tuple if need to reuse.\n")


print("=== Mistake 2: Mutable Default Argument in Decorators ===")
# Incorrect:
# def add_item(item, items=[]): 
#     items.append(item)
#     return items

# Fixed:
def add_item_fixed(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(f"Call 1: {add_item_fixed('apple')}")
print(f"Call 2: {add_item_fixed('banana')}") # Correctly starts fresh
print()


print("=== Mistake 3: Decorators masking function metadata ===")
# Incorrect:
# def my_decorator(func):
#     def wrapper():
#         """Wrapper docstring"""
#         return func()
#     return wrapper

# @my_decorator
# def my_func():
#     """Original docstring"""
#     pass
# print(my_func.__name__) # Prints 'wrapper' instead of 'my_func'

# Fixed:
def my_decorator_fixed(func):
    @functools.wraps(func) # Crucial!
    def wrapper():
        return func()
    return wrapper

@my_decorator_fixed
def my_func_fixed():
    """Original docstring"""
    pass

print(f"Function name preserved: {my_func_fixed.__name__}")
print(f"Docstring preserved: {my_func_fixed.__doc__}")
print()


print("=== Mistake 4: Broad Exception Handling ===")
# Incorrect:
# try:
#     do_something()
# except Exception: # Bad practice! Hides real bugs.
#     pass 

# Fixed:
# try:
#     do_something()
# except ValueError: # Catch specific errors
#     print("Invalid value")
# except Exception as e: # Catch generic only if necessary and LOG IT
#     print(f"Unexpected error: {e}")
print("Always catch specific exceptions when possible!\n")
