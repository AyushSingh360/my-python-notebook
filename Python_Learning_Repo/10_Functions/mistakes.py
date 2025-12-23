# Common beginner mistakes for Functions

# Mistake 1 – Forgetting to return (returns None by default)
# Incorrect
# def add(a, b):
#     result = a + b
# print(add(2, 3))   # prints None
# Fixed
def add(a, b):
    return a + b
print(add(2, 3))

# Mistake 2 – Mutable default argument
# Incorrect
# def append_it(x, L=[]):
#     L.append(x)
#     return L
# Fixed
def append_it(x, L=None):
    if L is None: L = []
    L.append(x)
    return L
print(append_it(1))
print(append_it(2))  # [2], not [1, 2]

# Mistake 3 – SyntaxError with args positioning
# Incorrect
# def f(a, *args, b): ...  # b must be keyword-only or it fails
# Fixed
def f(a, b, *args):
    pass
