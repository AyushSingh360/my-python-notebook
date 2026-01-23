# Common Beginner Mistakes with Dictionaries

# ==========================================
# Mistake 1: Valid vs Invalid Keys
# ==========================================
# Keys must be HASHABLE (immutable).

# INCORRECT:
# d = {[1, 2]: "value"}      # TypeError: unhashable type: 'list'
# d = {{"a": 1}: "value"}    # TypeError: unhashable type: 'dict'

# CORRECT: Use tuples for composite keys
location = {(40.7128, -74.0060): "New York"}
print(f"Location: {location[(40.7128, -74.0060)]}")


# ==========================================
# Mistake 2: Key Errors & get() check
# ==========================================
# Accessing a missing key raises a KeyError.

scores = {"Alice": 10}

# INCORRECT:
# print(scores["Bob"]) # KeyError: 'Bob'

# CORRECT: Check existence or use .get()
if "Bob" in scores:
    print(scores["Bob"])
else:
    print("Bob not found")

# Concise way:
print(f"Bob's score: {scores.get('Bob', 0)}")


# ==========================================
# Mistake 3: Modifying while iterating
# ==========================================
# You cannot iterate over a dictionary and modify its structure (add/remove keys) at the same time.

data = {"a": 1, "b": 2, "c": 3}

# INCORRECT:
# for k in data:
#     if k == "b":
#         del data[k] # RuntimeError: dictionary changed size during iteration

# CORRECT: Iterate over a copy of the keys
for k in list(data.keys()):
    if k == "b":
        del data[k]
print(f"Safe deletion result: {data}")


# ==========================================
# Mistake 4: .update() returns None
# ==========================================
d = {"a": 1}

# INCORRECT:
# new_d = d.update({"b": 2})
# print(new_d) # None!

# CORRECT:
d.update({"b": 2})
print(d)


# ==========================================
# Mistake 5: 'defaultdict' gotcha
# ==========================================
# Accessing a key in a defaultdict CREATES it.
from collections import defaultdict

d = defaultdict(int)
print(f"Before check: {dict(d)}")

if d["missing_key"] == 0: # This ACCESS creates the key 'missing_key' -> 0
    pass

print(f"After check: {dict(d)}") # {'missing_key': 0} - Size grew!

# CORRECT: Use normal 'in' check to avoid creation
if "other_key" in d:
    pass # Won't create it
