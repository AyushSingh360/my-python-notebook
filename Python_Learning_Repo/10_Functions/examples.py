# Examples demonstrating functions

# 1. Temperature converter
def c_to_f(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9/5 + 32

print(c_to_f(20))

# 2. Recursive factorial
def fact(n):
    if n == 0: return 1
    return n * fact(n-1)

print(fact(5))

# 3. Higher-order function (map logic)
def apply_func(func, data):
    return [func(x) for x in data]

print(apply_func(lambda x: x*2, [1, 2, 3]))

# 4. Using *args for summation
def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30))
