# Common beginner mistakes for File Handling

# Mistake 1 – Not closing the file (resource leak)
# Incorrect
# f = open("test.txt", "w")
# f.write("data")
# (no f.close())
# Fixed
with open("test.txt", "w") as f:
    f.write("data")

# Mistake 2 – Wrong mode
# Incorrect
# with open("test.txt", "r") as f:
#     f.write("Fail")  # UnsupportedOperation
# Fixed
with open("test.txt", "w") as f:
    f.write("Success")

# Mistake 3 – Reading binary as text
# Incorrect
# open("img.png", "r").read()  # UnicodeDecodeError
# Fixed
# open("img.png", "rb").read()
