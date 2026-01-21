# Common Beginner Mistakes with Sets

# ==========================================
# Mistake 1: The Empty Set Trap
# ==========================================
# {} creates an empty dictionary, NOT an empty set.

# INCORRECT:
my_set = {}
# my_set.add(1) # AttributeError: 'dict' object has no attribute 'add'
print(f"Type of {{}}: {type(my_set)}")

# CORRECT:
real_set = set()
real_set.add(1)
print(f"Type of set(): {type(real_set)}")


# ==========================================
# Mistake 2: Unhashable Elements (Mutable items)
# ==========================================
# Sets require their elements to be hashable (immutable).
# Lists are mutable, so they cannot be in a set.

# INCORRECT:
# s = {[1, 2], [3, 4]} # TypeError: unhashable type: 'list'

# CORRECT: Use tuples instead
s = {(1, 2), (3, 4)}
print(f"Set of tuples: {s}")


# ==========================================
# Mistake 3: Assuming Order
# ==========================================
# Sets are unordered. You cannot access them by index.

my_set = {10, 20, 30}

# INCORRECT:
# print(my_set[0]) # TypeError: 'set' object is not subscriptable

# CORRECT: Convert to list if you need indexing (but order is arbitrary unless sorted)
my_list = list(my_set)
print(f"As list: {my_list[0]}")


# ==========================================
# Mistake 4: 'remove' vs 'discard'
# ==========================================
# Removing an item that doesn't exist.

s = {1, 2, 3}

# INCORRECT:
# s.remove(4) # KeyError: 4

# CORRECT:
s.discard(4) # No error, does nothing
if 4 in s:
    s.remove(4) # Check before removing


# ==========================================
# Mistake 5: Boolean Logic Confusion
# ==========================================
# Using 'and'/'or' instead of intersection/union symbols.
# In Python, 'and' returns the second operand if the first is truthy.

A = {1, 2}
B = {3, 4}

# INCORRECT (usually):
result = A and B 
print(f"A and B: {result}") # {3, 4} (Just returns B!)

# CORRECT:
intersection = A & B
print(f"A & B: {intersection}") # set() (Empty set)
