# Common beginner mistakes for Conditional Statements

# Mistake 1 – Assignment in condition
# Incorrect
# if x = 5: ...
# Fixed
if x == 5:
    print("x is 5")

# Mistake 2 – IndentationError
# Incorrect
# if True:
# print("Yes")
# Fixed
if True:
    print("Yes")

# Mistake 3 – Mutable default argument causing state retention across calls
# Incorrect
# def add(item, L=[]): ...
# Fixed
def add(item, L=None):
    if L is None: L = []
    L.append(item)
    return L
