# Basics of Advanced Features

# List Comprehension
print([x**2 for x in range(5)])

# Lambda
add = lambda a,b: a+b
print(add(2,3))

# Generator Function
def gen():
    yield 1
    yield 2
for x in gen(): print(x)

# Exception Handling
try:
    print(1/0)
except ZeroDivisionError:
    print("Caught error")
