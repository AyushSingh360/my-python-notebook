# Common Beginner Mistakes with Tuples

# ==========================================
# Mistake 1: The Single Element Trap
# ==========================================
# Parentheses are used for grouping math operations AND tuples.
# Python needs a hint to distinguish them: the COMMA.

# INCORRECT:
not_tuple = (5)
print(f"Type of (5): {type(not_tuple)}") # <class 'int'>

# CORRECT:
is_tuple = (5,)
print(f"Type of (5,): {type(is_tuple)}") # <class 'tuple'>
# Note: For empty tuples (), no comma is needed.


# ==========================================
# Mistake 2: Attempting to Modify (Immutability)
# ==========================================
# Tuples are immutable. You cannot assign valid indices.

my_tuple = (1, 2, 3)

# INCORRECT:
# my_tuple[0] = 100 # TypeError: 'tuple' object does not support item assignment

# CORRECT:
# You must create a new tuple instead.
new_tuple = (100,) + my_tuple[1:]
print(f"New tuple: {new_tuple}")

# ==========================================
# Mistake 3: Concatenation Errors
# ==========================================
# You can only concatenate a tuple with another tuple.

t = (1, 2, 3)

# INCORRECT:
# result = t + 4        # TypeError
# result = t + [4]      # TypeError

# CORRECT:
result = t + (4,)
print(f"Concatenated: {result}")


# ==========================================
# Mistake 4: Mutable Iterables inside Tuples
# ==========================================
# A tuple is immutable, but if it holds a mutable object (like a list), that object CAN change.
# This makes the tuple "unhashable" and can be confusing.

# Tuple with a list inside
weird_tuple = ([10, 20], 30)

# weird_tuple[0] = [99, 88] # TypeError (Cannot change what the tuple points to)

# BUT we can modify the list it points to:
weird_tuple[0].append(99)
print(f"Modified inner list: {weird_tuple}")

# WARNING: Because it contains a mutable list, you cannot use this as a dict key!
# d = {weird_tuple: "value"} # TypeError: unhashable type: 'list'

# ==========================================
# Mistake 5: Parentheses Confusion in Function Calls
# ==========================================
# Passing integers vs passing a tuple

def inspect(x):
    print(f"Received type: {type(x)} value: {x}")

inspect((1, 2)) # Passed a single argument: a tuple (1,2)
inspect(1)      # Passed a single argument: int 1

# What if we want to pass a single tuple argument via unpack syntax?
# inspect(*(1, 2)) # Equivalent to inspect(1, 2) which fails if function only takes 1 arg.
