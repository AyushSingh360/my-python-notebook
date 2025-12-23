# Common beginner mistakes for Introduction chapter

# Mistake 1 – Missing parentheses in print (Python 2 style)
# Incorrect
# print "Hello"
# Fixed
print("Hello")

# Mistake 2 – Using assignment (=) instead of equality (==) in condition
# Incorrect
# if x = 5:
#     print("x is five")
# Fixed
if x == 5:
    print("x is five")

# Mistake 3 – Mixing tabs and spaces (IndentationError)
# Incorrect (mixed indentation)
# def foo():
# 	print("Hi")   # Tab
#     print("Bye")  # Spaces
# Fixed – use 4 spaces consistently
def foo():
    print("Hi")
    print("Bye")
