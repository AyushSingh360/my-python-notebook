# Common beginner mistakes for Modules

# Mistake 1 – Circular import
# a.py imports b, b.py imports a
# Fixed: Refactor shared logic to c.py

# Mistake 2 – Variables shadowing module names
# Incorrect
# random = 5
# import random
# random.randint(1, 10)  # AttributeError
# Fixed: Don't name variables same as modules

# Mistake 3 – from module import *
# Incorrect
# from math import *
# Fixed
from math import sqrt, pi
