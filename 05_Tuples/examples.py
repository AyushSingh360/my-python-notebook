# Comprehensive Tuple Examples
# Tuples are ordered, immutable collections of items.

# ==========================================
# 1. Creation and The "Comma" Rule
# ==========================================
# Parentheses are often optional; the comma makes the tuple.
t1 = 1, 2, 3
print(f"Implicit tuple: {t1} type: {type(t1)}")

# Single element tuple (CRITICAL)
not_a_tuple = (5)   # This is just an Integer 5
is_a_tuple = (5,)   # The comma tells Python it's a tuple
print(f"Not tuple: {type(not_a_tuple)}, Is tuple: {type(is_a_tuple)}")

# Empty tuple
empty = ()

# Tuple constructor
from_list = tuple([10, 20, 30])
print(f"From list: {from_list}")

# ==========================================
# 2. Accessing & Slicing (Same as Lists)
# ==========================================
coords = (10, 20, 30, 40, 50)

print(f"First: {coords[0]}")
print(f"Last: {coords[-1]}")
print(f"Slice: {coords[1:4]}")

# ==========================================
# 3. Immutability & Hashing
# ==========================================
# Tuples cannot be changed after creation.
# coords[0] = 99 # TypeError: 'tuple' object does not support item assignment

# Because they are immutable, tuples (containing only immutable items) are Hashable.
# This means they can be used as Dictionary Keys or Set elements.
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}
print(f"Dictionary lookup: {locations[(40.7128, -74.0060)]}")

# ==========================================
# 4. Unpacking
# ==========================================
point = (3, 4)
x, y = point # Unpacking to variables
print(f"x: {x}, y: {y}")

# Extended Unpacking (* operator)
numbers = (1, 2, 3, 4, 5)
head, *body, tail = numbers
print(f"Head: {head}, Body: {body}, Tail: {tail}")

# Swapping variables using packing/unpacking
a = 10
b = 20
a, b = b, a # Effectively: tuple (b, a) unpacked into a, b
print(f"Swapped: a={a}, b={b}")

# ==========================================
# 5. Named Tuples
# ==========================================
# Named tuples exist in the collections module. They allow accessing fields by name.
from collections import namedtuple

# Define the structure
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

print(f"Access by index: {p[0]}")
print(f"Access by name:  {p.x}, {p.y}")

# ==========================================
# 6. Performance: Tuples vs Lists
# ==========================================
import sys

# Tuples generally use less memory than lists of the same size
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(my_list)} bytes")
print(f"Tuple size: {sys.getsizeof(my_tuple)} bytes")
# Tuples are also slightly faster to construct.
