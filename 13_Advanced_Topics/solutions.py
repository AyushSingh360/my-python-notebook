# Solutions – Advanced Python

import time
import functools
from collections.abc import Iterator
from contextlib import contextmanager

# =============================================================================
# EASY LEVEL
# =============================================================================

# 1. Lambda Functions
print("=== 1. Lambda Functions ===")
square = lambda x: x ** 2
print(f"Square of 8: {square(8)}")

# 2. List Comprehension
print("\n=== 2. List Comprehension ===")
all_nums = range(10)
evens = [x for x in all_nums if x % 2 == 0]
print(f"Evens: {evens}")

# 3. Basic Exception Handling
print("\n=== 3. Exception Handling ===")
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

safe_divide(10, 0)
print(f"10/2 = {safe_divide(10, 2)}")

# 4. Simple Generator
print("\n=== 4. Simple Generator ===")
def yield_colors():
    yield "Red"
    yield "Green"
    yield "Blue"

for color in yield_colors():
    print(color)

# 5. Map Function
print("\n=== 5. Map Function ===")
str_nums = ["1", "2", "3"]
int_nums = list(map(int, str_nums)) # map(int, ...) works or map(lambda x: int(x), ...)
print(f"Integers: {int_nums}, Type: {type(int_nums[0])}")

# =============================================================================
# MEDIUM LEVEL
# =============================================================================

# 6. Custom Exception
print("\n=== 6. Custom Exception ===")
class NegativeNumberError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError(f"Number {n} is negative!")
    return "OK"

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"Caught: {e}")

# 7. Dictionary Comprehension
print("\n=== 7. Dict Comprehension ===")
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

# 8. Basic Decorator
print("\n=== 8. Basic Decorator ===")
def simple_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started...")
        result = func(*args, **kwargs)
        print("Function ended.")
        return result
    return wrapper

@simple_logger
def hello():
    print("Hello world!")

hello()

# 9. File Context Manager
print("\n=== 9. File Context Manager ===")
filename = "test_adv.txt"
with open(filename, "w") as f:
    f.write("Hello context manager!")

with open(filename, "r") as f:
    print(f"Read callback: {f.read()}")

# 10. Filter Function
print("\n=== 10. Filter Function ===")
names = ["Alice", "Bob", "Charlie", "Adam"]
starts_with_a = list(filter(lambda n: n.startswith("A"), names))
print(f"Names with A: {starts_with_a}")

# 11. Generator Expression
print("\n=== 11. Generator Expression ===")
gen_squares = (x**2 for x in range(11))
# sum() takes an iterable, so it consumes the generator
print(f"Sum of squares 0-10: {sum(gen_squares)}")

# =============================================================================
# HARD LEVEL
# =============================================================================

# 12. Context Manager Class
print("\n=== 12. Context Manager Class (Timer) ===")
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self # can return object to use in 'as var'
    
    def __exit__(self, exc_type, exc_val, tb):
        self.end = time.time()
        print(f"Execution time: {self.end - self.start:.4f} seconds")

with Timer():
    time.sleep(0.5)
    print("Sleeping...")

# 13. Decorator with Arguments
print("\n=== 13. Decorator with Args ===")
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Run {i+1}: ", end="")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hi {name}")

greet("Python")

# 14. Custom Iterator
print("\n=== 14. Custom Iterator ===")
class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(3):
    print(num)

# 15. Exception Chaining
print("\n=== 15. Exception Chaining ===")
class DataProcessingError(Exception):
    pass

def process_data(val):
    try:
        int(val) # Raises ValueError if text
    except ValueError as e:
        # Chain the exception "from" the original cause
        raise DataProcessingError("Failed to process data") from e

try:
    process_data("NotANumber")
except DataProcessingError as e:
    print(f"Caught wrapper error: {e}")
    print(f"Original cause: {e.__cause__}")

# 16. Nested Decorators
print("\n=== 16. Nested Decorators ===")
def make_upper(func):
    def wrapper():
        return func().upper()
    return wrapper

def make_exclaim(func):
    def wrapper():
        return func() + "!"
    return wrapper

@make_upper   # 2. Uppercases result "hello!" -> "HELLO!"
@make_exclaim # 1. returns "hello!"
def get_msg():
    return "hello"

print(get_msg())

# 17. Safe Execution Wrapper
print("\n=== 17. Safe Execution Wrapper ===")
def safe_execute(func, *args):
    try:
        return func(*args)
    except Exception as e:
        print(f"SafeExec caught crash: {e}")
        return None

def crashy_func(): return 1/0

result = safe_execute(crashy_func)
print(f"Result: {result}")

# 18. Infinite Generator
print("\n=== 18. Infinite Generator (Fibonacci) ===")
def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fib_gen()
print("First 10 Fib numbers:")
for _ in range(10):
    print(next(fib), end=" ")
print()

# =============================================================================
# BONUS
# =============================================================================

# 19. Type Hinting
print("\n=== 19. Type Hinting ===")
from typing import List, Dict

def calculate_stats(data: List[int]) -> Dict[str, float]:
    return {
        "sum": float(sum(data)),
        "max": float(max(data))
    }

stats = calculate_stats([10, 20, 30])
print(stats)

# 20. Coroutine (Send)
print("\n=== 20. Coroutine ===")
def receiver():
    print("Ready to receive")
    while True:
        data = yield
        print(f"Received: {data}")

r = receiver()
next(r) # Prime the coroutine
r.send("Packet 1")
r.send("Packet 2")
r.close()

# 21. Generator Pipeline
print("\n=== 21. Generator Pipeline ===")
gen1 = (x for x in range(1, 101)) # 1-100
gen2 = (x**2 for x in gen1)       # Squares
gen3 = (x for x in gen2 if x % 5 == 0) # Divisible by 5

# Consume first 5
for _ in range(5):
    print(next(gen3), end=" ")
print()

# 22. Singleton Decorator
print("\n=== 22. Singleton Decorator ===")
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Config:
    def __init__(self):
        print("Loading config...")

c1 = Config()
c2 = Config()
print(f"Same instance? {c1 is c2}") # True, "Loading config..." printed only once
