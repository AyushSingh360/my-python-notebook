# Common beginner mistakes for Lists

# Mistake 1 – Index out of range
# Incorrect
# L = [1, 2]
# print(L[5])
# Fixed
L = [1, 2]
if len(L) > 5: print(L[5])

# Mistake 2 – Modifying while iterating
# Incorrect
# for x in L: L.remove(x)
# Fixed
for x in L[:]: L.remove(x)

# Mistake 3 – append vs extend
# Incorrect
# L.append([3, 4])  # [1, 2, [3, 4]]
# Fixed
# L.extend([3, 4])  # [1, 2, 3, 4]
