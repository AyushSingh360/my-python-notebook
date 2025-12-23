# Common beginner mistakes for Advanced Topics

# Mistake 1 – Confusing generator with list
# Incorrect
# gen = (x for x in range(3))
# print(gen[0])  # TypeError
# Fixed
gen = (x for x in range(3))
print(list(gen)[0])

# Mistake 2 – Late binding in lambdas (closures)
# Incorrect
# funcs = [lambda: i for i in range(3)]
# print([f() for f in funcs])  # [2, 2, 2]
# Fixed
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]

# Mistake 3 – Catching bare Exception
# Incorrect
# try: ... except: ... # Catches everything including Ctrl+C
# Fixed
# try: ... except Exception: ...
