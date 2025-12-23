# Common beginner mistakes for Sets

# Mistake 1 – Using mutable object as set element
# Incorrect
# s = { [1,2], (3,4) }   # TypeError: unhashable type: 'list'
# Fixed
s = { (1,2), (3,4) }   # use only hashable types (tuples)

# Mistake 2 – Assuming order in a set
# Incorrect
# ordered = {3,1,2}
# print(ordered[0])    # TypeError: 'set' object is not subscriptable
# Fixed – convert to sorted list if order matters
ordered = {3,1,2}
print(sorted(ordered)[0])  # 1

# Mistake 3 – Using remove on a non‑existent element
# Incorrect
# s = {1,2,3}
# s.remove(4)          # KeyError
# Fixed – use discard
s = {1,2,3}
s.discard(4)           # does nothing, safe
