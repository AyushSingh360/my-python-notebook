# Comprehensive Dictionary Examples
# Dictionaries are mutable, unordered (insertion-ordered in 3.7+) collections of key-value pairs.

# ==========================================
# 1. Creation
# ==========================================
# Literal syntax
person = {"name": "Alice", "age": 30, "city": "New York"}

# dict() constructor (keyword arguments)
point = dict(x=10, y=20)

# From a list of tuples
pairs = [("a", 1), ("b", 2)]
from_tuples = dict(pairs)

# Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print(f"Squares: {squares}")

# ==========================================
# 2. Accessing & Modifying
# ==========================================
# Accessing
print(f"Name: {person['name']}")
# print(person['job']) # KeyError if missing

# safe access with .get()
job = person.get("job", "Unemployed")
print(f"Job: {job}")

# Adding/Updating
person["email"] = "alice@example.com" # New key
person["age"] = 31                    # Update existing
print(f"Updated person: {person}")

# Bulk update
person.update({"age": 32, "phone": "555-1234"})

# ==========================================
# 3. Removing Items
# ==========================================
# pop(key) - removes and returns value
email = person.pop("email")
print(f"Popped email: {email}")

# popitem() - removes and returns last inserted (key, value) pair (LIFO)
last_item = person.popitem()
print(f"Popped last item: {last_item}")

# del keyword
del person["city"]

# clear()
# person.clear()

# ==========================================
# 4. Iterating
# ==========================================
d = {"a": 1, "b": 2, "c": 3}

print("Keys:", list(d.keys()))
print("Values:", list(d.values()))
print("Items:", list(d.items()))

# Idiomatic iteration
print("Iterating items:")
for k, v in d.items():
    print(f"  {k} -> {v}")

# ==========================================
# 5. Default Dictionary (collections.defaultdict)
# ==========================================
from collections import defaultdict

# Useful for grouping or counting without checking if key exists
# Lambda returns default value (0) for new keys
freq = defaultdict(int) 
words = ["apple", "banana", "apple", "cherry"]
for w in words:
    freq[w] += 1
print(f"Frequencies: {dict(freq)}")

# Grouping loop (list default)
groups = defaultdict(list)
groups["fruit"].append("apple")
groups["fruit"].append("banana")
print(f"Groups: {dict(groups)}")

# ==========================================
# 6. Merging (Python 3.9+)
# ==========================================
x = {"key1": "value1 from x", "key2": "value2 from x"}
y = {"key2": "value2 from y", "key3": "value3 from y"}

# Pipe operator | creates a new merged dictionary
merged = x | y 
print(f"Merged (|): {merged}")
# Note: y's value for key2 overwrites x's

# In-place merge
x |= y
print(f"In-place merged (|=): {x}")
