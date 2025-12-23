# Solutions – Dictionaries

# 1. Book dictionary
book = {"title": "Python 101", "author": "John Doe", "pages": 250}
print(book["author"])

# 2. Add year
book["year"] = 2025
print(book)

# 3. get default
print(book.get("publisher", "Unknown"))

# 4. Invert dict
def invert_dict(d):
    return {v: k for k, v in d.items()}
print(invert_dict({"a":1, "b":2}))

# 5. Name to ID
def name_to_id(names):
    return {name: 1000 + i for i, name in enumerate(names)}
print(name_to_id(["Alice", "Bob"]))

# 6. Merge
d1 = {"x": 1, "y": 2}
d2 = {"y": 20, "z": 3}
merged = d1.copy()
merged.update(d2)
print(merged)

# 7. KV Store
class KVStore:
    def __init__(self):
        self._s = {}
    def set(self, k, v):
        self._s[k] = v
    def get(self, k, d=None):
        return self._s.get(k, d)
    def delete(self, k):
        if k in self._s: del self._s[k]
store = KVStore()
store.set("k", "v")
print(store.get("k"))

# 8. Flatten dict
def flatten(d, sep="."):
    flat = {}
    for k, v in d.items():
        if isinstance(v, dict):
            for sk, sv in v.items():
                flat[f"{k}{sep}{sk}"] = sv
        else:
            flat[k] = v
    return flat
print(flatten({"a": {"b": 2}, "c": 3}))

# 9. Factorials
import math
fact_map = {i: math.factorial(i) for i in range(1, 11)}
print(fact_map)

# 10. Select where
def select_where(rows, col, val):
    return [r for r in rows if r.get(col) == val]
rows = [{"id":1,"d":"HR"}, {"id":2,"d":"IT"}]
print(select_where(rows, "d", "HR"))
