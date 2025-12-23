# Common beginner mistakes for Strings

# Mistake 1 – Forgetting to escape backslashes in Windows paths
# Incorrect
# path = "C:\new_folder\test.txt"
# Fixed
path = "C:\\new_folder\\test.txt"
print(path)

# Mistake 2 – Trying to modify an immutable string
# Incorrect
# s = "hello"
# s[0] = "H"
# Fixed
s = "hello"
s = "H" + s[1:]
print(s)

# Mistake 3 – Concatenating non‑string types without conversion
# Incorrect
# age = 25
# print("Age: " + age)
# Fixed
age = 25
print("Age: " + str(age))
