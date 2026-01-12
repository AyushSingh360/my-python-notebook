# Common Mistakes – Data Types & Operators

"""
This file demonstrates common errors beginners make with data types and operators.
Each section shows the WRONG way, explains WHY it's wrong, and shows the RIGHT way.
"""

def print_mistake(title):
    print(f"\n❌ Mistake: {title}")

def print_fix(title):
    print(f"✅ Fix: {title}")

# ---------------------------------------------------------
# 1. Assignment (=) vs Equality (==)
# ---------------------------------------------------------
print_mistake("Using = instead of == in conditions")
x = 10
try:
    # This is a SyntaxError in Python, but conceptually a common logic error in other languages
    # if x = 5: print("x is 5") 
    print("Code: if x = 5: ...")
    print("Error: SyntaxError: invalid syntax")
except SyntaxError as e:
    print(e)

print_fix("Use == for comparison")
if x == 10:
    print("x is 10")


# ---------------------------------------------------------
# 2. Floating Point Precision
# ---------------------------------------------------------
print_mistake("Assuming floats are exact")
result = 0.1 + 0.2
print(f"0.1 + 0.2 == 0.3 -> {result == 0.3}")
print(f"Actual value: {result}")

print_fix("Use a tolerance (epsilon) for comparison")
tolerance = 1e-9
print(f"abs(result - 0.3) < {tolerance} -> {abs(result - 0.3) < tolerance}")


# ---------------------------------------------------------
# 3. String Immutability
# ---------------------------------------------------------
print_mistake("Trying to change a character in a string")
s = "Hello"
try:
    # s[0] = 'h'
    print("Code: s[0] = 'h'")
    print("Error: TypeError: 'str' object does not support item assignment")
except TypeError as e:
    print(e)

print_fix("Create a new string instead")
s_new = 'h' + s[1:]
print(f"New string: {s_new}")


# ---------------------------------------------------------
# 4. Integer Division vs Float Division
# ---------------------------------------------------------
print_mistake("Confusing / and //")
print(f"5 / 2 = {5/2} (Float Division)")
print(f"5 // 2 = {5//2} (Floor/Integer Division)")


# ---------------------------------------------------------
# 5. Modifying List while Iterating
# ---------------------------------------------------------
print_mistake("Modifying a list while iterating over it")
nums = [1, 2, 3, 4, 5]
# Goal: Remove even numbers
# Incorrect way:
# for n in nums:
#     if n % 2 == 0:
#         nums.remove(n) 
# This skips elements because the index shifts.

print_fix("Iterate over a copy or use list comprehension")
nums = [1, 2, 3, 4, 5]
nums = [n for n in nums if n % 2 != 0]
print(f"Correctly filtered: {nums}")


# ---------------------------------------------------------
# 6. Boolean Logic Confusion
# ---------------------------------------------------------
print_mistake("Misunderstanding 'or' return value")
# Many expect 'or' to return True/False, but it returns the first truthy value
# name = input("Enter name (leave empty for default): ") or "Guest" 
name = "" or "Guest"
print(f"'' or 'Guest' -> '{name}' (Not True/False)")
