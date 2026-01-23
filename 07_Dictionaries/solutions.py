# Solutions – Dictionaries

# ==========================================
# Easy
# ==========================================

# 1. Book Dictionary
# ------------------------------------------
def exercise_1():
    book = {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "pages": 310
    }
    print(f"Author: {book['author']}")
    return book

# 2. Add Year
# ------------------------------------------
def exercise_2(book_dict):
    book_dict["year"] = 1937
    return book_dict

# 3. Safe Access
# ------------------------------------------
def exercise_3(book_dict):
    return book_dict.get("publisher", "Unknown")

# Test Easy
b = exercise_1()
print(f"Added year: {exercise_2(b)}")
print(f"Publisher: {exercise_3(b)}")


# ==========================================
# Medium
# ==========================================

# 4. Invert Dictionary
# ------------------------------------------
def exercise_4(d):
    # Dict comprehension: {new_key: new_value}
    return {v: k for k, v in d.items()}

print(f"Inverted: {exercise_4({'a': 1, 'b': 2})}")


# 5. Name to ID
# ------------------------------------------
def exercise_5(names):
    # enumerate gives us (index, value) tuples
    return {name: 1000 + i for i, name in enumerate(names)}

print(f"IDs: {exercise_5(['Alice', 'Bob'])}")


# 6. Merge
# ------------------------------------------
def exercise_6(d1, d2):
    # Python 3.9+ syntax
    return d1 | d2
    # Old way:
    # m = d1.copy()
    # m.update(d2)
    # return m

print(f"Merged: {exercise_6({'x': 1}, {'y': 2})}")


# ==========================================
# Hard
# ==========================================

# 7. KV Store
# ------------------------------------------
class KVStore:
    def __init__(self):
        self._store = {}
        
    def set(self, key, value):
        self._store[key] = value
        
    def get(self, key):
        return self._store.get(key) # Returns None by default
        
    def delete(self, key):
        if key in self._store: # Avoid error
            del self._store[key]

# Test Store
store = KVStore()
store.set("user", "admin")
print(f"Get user: {store.get('user')}")
store.delete("user")
print(f"Get deleted: {store.get('user')}")


# 8. Flatten Dictionary
# ------------------------------------------
def exercise_8(nested_dict):
    flat = {}
    for key, val in nested_dict.items():
        if isinstance(val, dict):
            # It's nested, iterate through sub-dict
            for sub_key, sub_val in val.items():
                flat[f"{key}.{sub_key}"] = sub_val
        else:
            flat[key] = val
    return flat

data = {"a": {"x": 1}, "b": 2}
print(f"Flattened: {exercise_8(data)}")


# 9. Factorial Comprehension
# ------------------------------------------
import math
def exercise_9():
    return {n: math.factorial(n) for n in range(1, 6)}

print(f"Factorials: {exercise_9()}")


# 10. Select Where
# ------------------------------------------
def exercise_10(rows, column, value):
    return [row for row in rows if row.get(column) == value]

users = [{"id": 1, "role": "admin"}, {"id": 2, "role": "user"}, {"id": 3, "role": "admin"}]
admins = exercise_10(users, "role", "admin")
print(f"Admins: {admins}")
