# Examples of advanced concepts

# 1. Map/Filter with Lambda
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x%2==0, nums))
print(doubled, evens)

# 2. Custom Exception
class MyErr(Exception): pass
def check(x):
    if x < 0: raise MyErr("Negative!")
try:
    check(-1)
except MyErr as e:
    print(e)

# 3. Decorator
def log(func):
    def wrapper():
        print("Calling...")
        func()
    return wrapper

@log
def hello(): print("Hi")
hello()

# 4. Generator for large sequence
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1
print(list(count_up_to(5)))
