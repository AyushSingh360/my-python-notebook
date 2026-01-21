# Comprehensive Set Examples
# Sets are unordered collections of unique, hashable items.

# ==========================================
# 1. Creation and Uniqueness
# ==========================================
# Using curly braces
fruits = {"apple", "banana", "cherry", "apple"}
print(f"Fruits (deduplicated): {fruits}") # 'apple' only appears once

# Using set() constructor (great for converting lists)
numbers = set([1, 2, 2, 3, 3, 3])
print(f"Numbers: {numbers}")

# Creating an empty set (CRITICAL)
empty_set = set()      # Correct
empty_dict = {}        # This creates an empty Dictionary!
print(f"Type of set(): {type(empty_set)}, Type of {{}}: {type(empty_dict)}")

# ==========================================
# 2. Modifying Sets
# ==========================================
my_set = {1, 2, 3}

# Adding
my_set.add(4)
print(f"Added 4: {my_set}")

# Updating (adding multiple)
my_set.update([5, 6, 7])
print(f"Updated: {my_set}")

# Removing
my_set.remove(7)      # Raises KeyError if not found
my_set.discard(99)    # Safe: does nothing if not found
popped = my_set.pop() # Removes and returns an arbitrary element
print(f"Popped: {popped}, Remaining: {my_set}")

# Clearing
my_set.clear()
print(f"Cleared: {my_set}")

# ==========================================
# 3. Mathematical Operations
# ==========================================
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (OR): Elements in A OR B
print(f"Union (A | B): {A | B}")

# Intersection (AND): Elements in BOTH A AND B
print(f"Intersection (A & B): {A & B}")

# Difference: Elements in A but NOT in B
print(f"Difference (A - B): {A - B}")

# Symmetric Difference: Elements in A OR B but NOT BOTH
print(f"Symmetric Diff (A ^ B): {A ^ B}")

# ==========================================
# 4. Subset and Superset
# ==========================================
small = {1, 2}
big = {1, 2, 3, 4}

print(f"Is small subset of big? {small.issubset(big)}") # True
print(f"Is big superset of small? {big.issuperset(small)}") # True
print(f"Is small <= big? {small <= big}") # Alias for issubset

# Disjoint: No common elements
C = {8, 9}
print(f"Is small disjoint from C? {small.isdisjoint(C)}") # True

# ==========================================
# 5. Frozenset (Immutable Set)
# ==========================================
# Normal sets are mutable and unhashable (cannot be dict keys).
# Frozensets are immutable and hashable.

frozen = frozenset([1, 2, 3])
# frozen.add(4) # AttributeError: 'frozenset' object has no attribute 'add'

# Using frozenset as a dictionary key or set element
nested_set = {frozenset({1, 2}), frozenset({3, 4})}
print(f"Set of frozensets: {nested_set}")

# ==========================================
# 6. Set Comprehension
# ==========================================
# {expression for item in iterable if condition}
squares = {x**2 for x in range(10)}
print(f"Squares: {squares}")
