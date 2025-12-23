# Examples demonstrating set operations

# 1. Removing duplicates from a list
raw = [1,2,2,3,4,4,4,5]
unique = set(raw)
print(unique)  # {1,2,3,4,5}

# 2. Membership test
allowed = {"admin", "user", "guest"}
role = "admin"
print(role in allowed)

# 3. Set comprehension – squares of numbers 0‑5
squares = {x*x for x in range(6)}
print(squares)

# 4. Union, intersection, difference
a = {1,2,3}
b = {3,4,5}
print("union", a | b)
print("intersection", a & b)
print("difference a-b", a - b)
print("sym diff", a ^ b)
