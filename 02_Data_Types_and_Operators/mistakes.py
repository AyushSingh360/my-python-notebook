# Common beginner mistakes for Data Types & Operators

# Mistake 1 – Using assignment (=) instead of equality (==) in a condition
# Incorrect
# if x = 5:
#     print("x is five")
# Fixed
if x == 5:
    print("x is five")

# Mistake 2 – Forgetting parentheses in arithmetic (operator precedence)
# Incorrect
result = 5 + 2 * 3   # gives 11, not 21
# Fixed
result = (5 + 2) * 3
print(result)

# Mistake 3 – Comparing strings with 'is' instead of '=='
# Incorrect
# if user_input is "yes":
#     print("Confirmed")
# Fixed
if user_input == "yes":
    print("Confirmed")
