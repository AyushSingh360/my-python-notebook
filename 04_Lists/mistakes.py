# Common Beginner Mistakes with Lists

# ==========================================
# Mistake 1: Index out of range
# ==========================================
# Trying to access an index that doesn't exist raises an IndexError.
L = [1, 2, 3]

# INCORRECT:
# print(L[3]) # IndexError! Lists are 0-indexed (0, 1, 2)

# CORRECT:
if len(L) > 3:
    print(L[3])
else:
    print("Index doesn't exist")

# ==========================================
# Mistake 2: Modifying a list while iterating over it
# ==========================================
# This often leads to skipped elements or runtime errors.

numbers = [1, 2, 3, 4, 5]

# INCORRECT:
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num) 
# Result happens to be [1, 3, 5] here, but often behavior is unpredictable.

# CORRECT: Iterate over a copy (using slice [:])
for num in numbers[:]: 
    if num % 2 == 0:
        numbers.remove(num)

# ==========================================
# Mistake 3: expecting append() to return the list
# ==========================================
# List methods like append(), sort(), reverse() modify the list IN-PLACE and return None.

my_list = [1, 2, 3]

# INCORRECT:
# new_list = my_list.append(4)
# print(new_list) # Prints: None

# CORRECT:
my_list.append(4)
print(my_list) # [1, 2, 3, 4]

# ==========================================
# Mistake 4: Aliasing (The "Equal Sign" Trap)
# ==========================================
# Assigning a list to valid variable just copies the REFERENCE, not the list itself.

original = [10, 20, 30]
copy_cat = original # Both point to the same object!

copy_cat[0] = 999
# print(original) # [999, 20, 30] - Surprise!

# CORRECT: Create a true copy
real_copy = original[:] # or original.copy()

# ==========================================
# Mistake 5: Mutable Default Arguments
# ==========================================
# Using a list as a default argument in a function.

# INCORRECT:
def append_to(element, target=[]):
    target.append(element)
    return target

# print(append_to(1)) # [1]
# print(append_to(2)) # [1, 2] - Keeps memory of previous calls!

# CORRECT: Use None
def append_to_fixed(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

# ==========================================
# Mistake 6: split() vs list()
# ==========================================
text = "hello"

# list(text) -> ['h', 'e', 'l', 'l', 'o']
# text.split() -> ['hello'] (splits by whitespace)
