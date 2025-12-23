# Basic function syntax

# Simple definition
def greet():
    print("Hello")

# With parameters and return
def add(a, b):
    return a + b

# Default values
def power(base, exp=2):
    return base ** exp

# *args and **kwargs
def varying_args(*args, **kwargs):
    print(args)    # tuple
    print(kwargs)  # dict
