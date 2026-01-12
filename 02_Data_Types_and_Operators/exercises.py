# Exercises – Data Types & Operators

"""
Completion Guide:
- Easy: Beginners (1-4)
- Medium: Intermediate (5-8)
- Hard: Advanced (9-11)
- Expert: Master (12-14)
"""

print("--- Exercises: Data Types & Operators ---")

# ----------------- EASY -----------------
# 1. Basic Arithmetic
# Calculate the area of a rectangle with length 10 and width 5.
# Expected Output: Area: 50

# 2. String Concatenation
# Create two variables, first_name and last_name, and print a greeting: "Hello, [First] [Last]!"
# Expected Output: Hello, John Doe!

# 3. Type Checking
# create a variable x = 10.5. Print its type. Then convert it to an integer and print the new type.
# Expected Output: <class 'float'>, <class 'int'>

# 4. Modulus
# Check if 25 is odd or even using the modulus operator.
# Expected Output: 25 is Odd


# ----------------- MEDIUM -----------------
# 5. Fahrenheit to Celsius
# Convert 98.6 degrees Fahrenheit to Celsius. Formula: C = (F - 32) * 5/9.
# Expected Output: 37.0

# 6. String Slicing & Methods
# Given text = "Python is awesome", print the word "awesome" in uppercase using slicing and .upper().
# Expected Output: AWESOME

# 7. List Operations
# Create a list `colors = ['red', 'green', 'blue']`. Check if 'yellow' is not in the list.
# Expected Output: True

# 8. Dictionary Lookup
# Create a dictionary `prices = {'apple': 0.5, 'banana': 0.3}`. Check if 'orange' exists in it.
# Expected Output: False


# ----------------- HARD -----------------
# 9. Compound Interest
# Calculate compound interest. P=1000, r=0.05, n=10 (years). Formula: A = P(1 + r)^n.
# Round the result to 2 decimal places.
# Expected Output: 1628.89

# 10. Bitwise Swap
# Swap two integers a=5, b=10 using ONLY bitwise XOR operators (no temp variable).
# Expected Output: a=10, b=5

# 11. String Palindrome Checker
# Check if the string "Racecar" is a palindrome (case-insensitive).
# Expected Output: True


# ----------------- EXPERT -----------------
# 12. Floating Point Equality
# Verify if 0.1 + 0.2 == 0.3. If False, check if they are "close enough" using a tolerance of 1e-9.
# Expected Output: Strict Equality: False, Close Enough: True

# 13. Logical Short-Circuiting
# Explain (via code comments or print) why `True or (1/0)` does not crash, but `False and (1/0)` also does not crash (wait, check that!).
# Task: Demonstrate a case that WOULD crash if order was reversed, e.g. `(1/0) or True`.

# 14. Complex Parsing
# Parse the string "Item:Apple,Price:0.50,Qty:10" into a dictionary `{'Item': 'Apple', 'Price': 0.5, 'Qty': 10}`.
# convert Price to float and Qty to int.
# Expected Output: {'Item': 'Apple', 'Price': 0.5, 'Qty': 10}
