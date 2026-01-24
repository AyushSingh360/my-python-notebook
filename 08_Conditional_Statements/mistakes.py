# Common Beginner Mistakes with Conditional Statements

# ==========================================
# Mistake 1: Assignment in Condition
# ==========================================
# Using '=' instead of '==' for comparison.
# Python usually catches this as a SyntaxError, but it's a very common typo.

x = 10

# INCORRECT:
# if x = 10: # SyntaxError
#     print("ten")

# CORRECT:
if x == 10:
    print("ten")


# ==========================================
# Mistake 2: Missing Colons & Indentation
# ==========================================
# Forgetting the ':' or messing up whitespace.

# INCORRECT:
# if x > 5
# print("greater") # IndentationError

# CORRECT:
if x > 5:
    print("greater")


# ==========================================
# Mistake 3: Boolean Logic Falsies
# ==========================================
# Trying to check if a variable equals one of multiple values.

val = "orange"

# INCORRECT:
# Reads as: (if val == "apple") OR ("pear")
# "pear" is truthy, so this ALWAYS runs!
if val == "apple" or "pear":
    print("It's a fruit") 

# CORRECT:
if val == "apple" or val == "pear":
    print("It's a known fruit")
# Better:
if val in ("apple", "pear"):
    print("It's a known fruit")


# ==========================================
# Mistake 4: Chained comparisons confusion
# ==========================================
score = 85

# INCORRECT:
# if 90 > score > 80: # This actually works in Python! But beginners often write logic incorrectly like:
# if score > 80 and < 90: # SyntaxError

# CORRECT:
if 80 < score < 90:
    print("B grade")


# ==========================================
# Mistake 5: 'is' vs '==' for values
# ==========================================
# Using 'is' for equality checks on literals (works sometimes, but unreliable).

a = 1000
b = 1000

# INCORRECT (often):
if a is b: # might be False depending on interpreter caching
    print("Same")

# CORRECT:
if a == b:
    print("Equal values")
