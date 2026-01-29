# Advanced Python Concepts: Comprehensive Examples

import time
import functools
from contextlib import contextmanager

# ==========================================
# 1. Iterators (The Iterator Protocol)
# ==========================================
print("=== 1. Iterators ===")
# An iterable is an object capable of returning its members one at a time.
# It must implement __iter__().
# An iterator is an object representing a stream of data.
# It must implement __iter__() and __next__().

class CountDown:
    """A custom iterator that counts down from start to 0."""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

# Usage
for num in CountDown(3):
    print(num, end=" ")
print()


# ==========================================
# 2. Generators (Simple & Efficient Iterators)
# ==========================================
print("\n=== 2. Generators ===")
# Generators allow you to declare a function that behaves like an iterator.
# They allow programmers to make an iterator in a fast, easy, and clean way.

def infinite_sequence():
    """Generates an infinite sequence of numbers."""
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(f"First: {next(gen)}")
print(f"Second: {next(gen)}")
print(f"Third: {next(gen)}")
# Note: This list isn't huge in memory, it's generated on the fly!


# ==========================================
# 3. Decorators (Modifying Function Behavior)
# ==========================================
print("\n=== 3. Decorators ===")

def timer(func):
    """Decorator to measure execution time of a function."""
    @functools.wraps(func) # Preserves original function metadata (name, docstring)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[{func.__name__}] executed in {end_time - start_time:.4f}s")
        return result
    return wrapper

@timer
def waste_time(n):
    """Simulates a heavy task."""
    sum([i**2 for i in range(n)])

waste_time(10000)
print(f"Function name preserved: {waste_time.__name__}")


# ==========================================
# 4. Context Managers (Resource Management)
# ==========================================
print("\n=== 4. Context Managers ===")

# Class-based Context Manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

# Generator-based Context Manager using contextlib
@contextmanager
def file_manager_gen(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

# Usage
with FileManager('test_class.txt', 'w') as f:
    f.write('Hello from Class CM')

with file_manager_gen('test_gen.txt', 'w') as f:
    f.write('Hello from Generator CM')

print("Files created successfully.")


# ==========================================
# 5. Functional Tools (Map, Filter, Reduce)
# ==========================================
print("\n=== 5. Functional Tools ===")
numbers = [1, 2, 3, 4, 5]

# Map: Apply function to all items
squared = list(map(lambda x: x**2, numbers))
print(f"Squared (Map): {squared}")

# Filter: Keep items that match condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens (Filter): {evens}")

# Reduce: Combine items
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(f"Total (Reduce): {total}")


# ==========================================
# 6. Generator Pipelines
# ==========================================
print("\n=== 6. Generator Pipelines ===")
# Processing data in stages without loading everything into memory

def gen_nums(n):
    for i in range(n):
        yield i

def gen_squares(nums):
    for n in nums:
        yield n ** 2

pipeline = gen_squares(gen_nums(5))
print(f"Pipeline result: {list(pipeline)}")

import os
# Cleanup
if os.path.exists('test_class.txt'): os.remove('test_class.txt')
if os.path.exists('test_gen.txt'): os.remove('test_gen.txt')
