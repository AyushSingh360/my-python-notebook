# Common beginner mistakes for Dictionaries

# Mistake 1 – Using a mutable type as a key
# Incorrect
# d = {["list"]: "value"}   # TypeError: unhashable type
# Fixed
d = {("tuple",): "value"}
print(d)

# Mistake 2 – Assuming .update modifies without copying if assigned
# Incorrect usage logic (update modifies in place)
# d = {"a": 1}
# e = d.update({"b": 2})   # e is None
# Fixed
d = {"a": 1}
d.update({"b": 2})
print(d)

# Mistake 3 – Direct access to missing key
# Incorrect
# val = d["missing"]   # KeyError
# Fixed
val = d.get("missing", "default")
print(val)
