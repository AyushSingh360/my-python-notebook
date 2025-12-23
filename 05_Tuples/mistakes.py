# Common beginner mistakes for Tuples

# Mistake 1 – Forgetting the trailing comma for a single‑element tuple
# Incorrect
# single = (5)   # just an int
# Fixed
single = (5,)
print(type(single))

# Mistake 2 – Trying to modify a tuple element
# Incorrect
# t = (1, 2, 3)
# t[0] = 10   # TypeError
# Fixed – create a new tuple
t = (1, 2, 3)
t = (10,) + t[1:]
print(t)

# Mistake 3 – Using mutable objects inside a tuple and mutating them
# Incorrect
# t = ([1, 2], 3)
# t[0].append(3)   # changes inner list
# Fixed – avoid mutable members or treat them as immutable
t = (tuple([1, 2]), 3)
print(t)
