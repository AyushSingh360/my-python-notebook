# Comprehensive Conditional Examples

# ==========================================
# 1. Basic Branching (if, elif, else)
# ==========================================
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")

# ==========================================
# 2. Boolean Logic & Chaining
# ==========================================
age = 25
has_id = True
is_banned = False

# AND: All conditions must be True
# OR: One condition must be True
# NOT: Inverses the boolean
if age >= 21 and has_id and not is_banned:
    print("Entry granted")
else:
    print("Entry denied")

# Chained Comparison (Pythonic)
x = 5
if 1 < x < 10:
    print("x is between 1 and 10")

# ==========================================
# 3. Truthy and Falsy Values
# ==========================================
# In Python, empty values (0, "", [], None) evaluate to False.
# Everything else evaluates to True.

name = ""
if not name:
    print("Name is empty (Falsy)")

items = ["apple"]
if items:
    print(f"List is not empty (Truthy), has {len(items)} items")

# ==========================================
# 4. Identity vs Equality (is vs ==)
# ==========================================
# '==' checks VALUE equality
# 'is' checks IDENTITY (same object in memory)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b? {a == b}") # True (values match)
print(f"a is b? {a is b}") # False (different objects)
print(f"a is c? {a is c}") # True (same object)

# Practice: Always use 'is' for None checks
val = None
if val is None:
    print("Value is None")

# ==========================================
# 5. Ternary Operator (Conditional Expression)
# ==========================================
# value_if_true if condition else value_if_false

status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# ==========================================
# 6. Combining Logic (Short-circuiting)
# ==========================================
# 'or' returns the first Truthy value
# 'and' returns the first Falsy value (or the last Truthy one)

username = input("Enter username (or press enter for Guest): ")
final_name = username or "Guest" 
print(f"Welcome, {final_name}")
