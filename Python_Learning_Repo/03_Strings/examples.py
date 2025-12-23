# Examples demonstrating string operations

# 1. Concatenation
first = "Python"
second = "Rocks"
combined = first + " " + second
print(combined)  # Python Rocks

# 2. Escape sequences
print("Line1\nLine2")
print("Tab\tSeparated")

# 3. Raw string for Windows path
path = r"C:\Users\spide\Documents"
print(path)

# 4. Slicing
s = "abcdefgh"
print(s[2:6])   # cdef
print(s[:3])    # abc
print(s[5:])    # fgh
print(s[::-1])  # reverse

# 5. f‑string with expression
x = 7
print(f"The square of {x} is {x**2}")
