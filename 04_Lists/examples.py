# Comprehensive List Examples
# Lists are ordered, mutable collections of items.

# ==========================================
# 1. Basic Creation and Data Types
# ==========================================
# Lists can contain mixed data types
mixed_list = [42, "hello", 3.14, True, None]
print(f"Mixed list: {mixed_list}")

# Nested lists (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix element [1][2]: {matrix[1][2]}") # Accessing row 1, col 2 -> 6

# Creating lists using list() constructor
char_list = list("hello")
print(f"Char list from string: {char_list}") # ['h', 'e', 'l', 'l', 'o']

# ==========================================
# 2. Accessing and Slicing
# ==========================================
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Slicing [start:stop:step]
print(f"First three: {fruits[:3]}")
print(f"Middle slice: {fruits[1:4]}")
print(f"Every second fruit: {fruits[::2]}")
print(f"Reversed list: {fruits[::-1]}")

# ==========================================
# 3. Modifying Lists
# ==========================================
# Changing elements
fruits[1] = "blackberry"
print(f"Modified fruits: {fruits}")

# Adding elements
fruits.append("fig")          # Adds to end
fruits.insert(0, "apricot")   # Inserts at index 0
fruits.extend(["grape", "honeydew"]) # Adds multiple items
print(f"Extended fruits: {fruits}")

# Removing elements
fruits.remove("cherry")       # Removes first occurrence
popped_item = fruits.pop()    # Removes and returns last item
first_popped = fruits.pop(0)  # Removes and returns item at index 0
del fruits[1]                 # Deletes by index
print(f"After removals: {fruits}")

# ==========================================
# 4. List Methods
# ==========================================
numbers = [3, 1, 4, 1, 5, 9, 2]

# Counting and Indexing
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 5: {numbers.index(5)}")

# Sorting and Reversing
numbers.sort()                # Sorts in-place
print(f"Sorted: {numbers}")

numbers.reverse()             # Reverses in-place
print(f"Reversed: {numbers}")

# 'sorted()' function is equivalent but returns a NEW list
unsorted = [5, 2, 8]
new_sorted = sorted(unsorted)
print(f"Original: {unsorted}, New Sorted: {new_sorted}")

# ==========================================
# 5. List Operations & Unpacking
# ==========================================
# Concatenation
combined = [1, 2] + [3, 4]

# Repetition
repeated = [0] * 5

# Unpacking
first, *middle, last = [10, 20, 30, 40, 50]
print(f"First: {first}, Middle: {middle}, Last: {last}")

# ==========================================
# 6. Aliasing vs Copying (Crucial Concept)
# ==========================================
original = [1, 2, 3]

# Reference (Aliasing) - Both variables point to the same object
alias = original
alias[0] = 99
print(f"Original after alias change: {original}") # [99, 2, 3] !

# Shallow Copy - Creates a new list object
original = [1, 2, 3]
copy_1 = original[:]
copy_2 = original.copy()
copy_3 = list(original)

copy_1[0] = 100
print(f"Original after copy change: {original}") # [1, 2, 3] (Unaffected)

# Deep Copy - Needed for nested lists
import copy
nested = [[1, 2], [3, 4]]
shallow_copy = nested.copy()
deep_copy = copy.deepcopy(nested)

shallow_copy[0][0] = 999
print(f"Original after shallow copy nested change: {nested}") # [[999, 2], [3, 4]] ! Changed!
deep_copy[1][0] = 888
print(f"Original after deep copy nested change: {nested}")   # [[999, 2], [3, 4]] Unaffected by deep copy

# ==========================================
# 7. List Comprehensions
# ==========================================
# [expression for item in iterable if condition]
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")
