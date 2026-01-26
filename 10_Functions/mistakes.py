# Common Beginner Mistakes with Functions

# ==========================================
# Mistake 1: Forgetting Return (Implicit None)
# ==========================================
# A function without a return statement returns None.

# INCORRECT:
def add(a, b):
    result = a + b
    # Missing return!

print(f"Result: {add(2, 3)}") # Prints: Result: None

# CORRECT:
def add_fixed(a, b):
    return a + b
print(f"Result: {add_fixed(2, 3)}")


# ==========================================
# Mistake 2: Mutable Default Arguments
# ==========================================
# Default arguments are evaluated ONCE at definition time.
# NEVER use mutable objects (lists, dicts) as defaults.

# INCORRECT:
def bad_append(item, lst=[]):
    lst.append(item)
    return lst

print(bad_append(1)) # [1]
print(bad_append(2)) # [1, 2] !!! (Shared list)

# CORRECT:
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst


# ==========================================
# Mistake 3: UnboundLocalError (Scope)
# ==========================================
# Trying to modify a global variable without declaring 'global'.

count = 0

# INCORRECT:
# def increment():
#     count += 1 # Error: local variable 'count' referenced before assignment

# CORRECT:
def increment():
    global count
    count += 1


# ==========================================
# Mistake 4: Argument Ordering
# ==========================================
# Positional args must come before keyword args.

def func(a, b): pass

# INCORRECT:
# func(a=1, 2) # SyntaxError: positional argument follows keyword argument

# CORRECT:
func(1, b=2)
