# Solutions – Functions
# Complete solutions with detailed explanations for all exercises

import math
import time

# =============================================================================
# EASY LEVEL  
# =============================================================================

# 1. Even Number Checker
def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

print("=== Exercise 1: Even Checker ===")
print(is_even(4))  # True
print(is_even(7))  # False

# ---

# 2. Circle Area Calculator
def area_circle(r):
    """Calculate area of circle with radius r."""
    return math.pi * r ** 2

print("\n=== Exercise 2: Circle Area ===")
print(f"Area of circle with radius 5: {area_circle(5):.2f}")

# ---

# 3. Simple Greeting
def say_hello():
    """Print a simple greeting."""
    print("Hello, World!")

print("\n=== Exercise 3: Simple Greeting ===")
say_hello()

# ---

# 4. Name Greeting
def greet(name):
    """Return personalized greeting."""
    return f"Hello, {name}!"

print("\n=== Exercise 4: Name Greeting ===")
print(greet("Alice"))

# ---

# 5. Temperature Converter
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9/5 + 32

print("\n=== Exercise 5: Temperature Converter ===")
print(f"20°C = {celsius_to_fahrenheit(20)}°F")

# =============================================================================
# MEDIUM LEVEL
# =============================================================================

# 6. Maximum of Three
def max_of_three(a, b, c):
    """Return largest of three numbers without using max()."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Alternative using nested comparisons
def max_of_three_alt(a, b, c):
    return a if (a >= b and a >= c) else (b if b >= c else c)

print("\n=== Exercise 6: Max of Three ===")
print(max_of_three(10, 25, 15))  # 25

# ---

# 7. Vowel Counter
def count_vowels(s):
    """Count vowels in string s."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Alternative using sum and generator expression
def count_vowels_alt(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print("\n=== Exercise 7: Vowel Counter ===")
print(count_vowels("hello world"))  # 3

# ---

# 8. List Reverser
def reverse_list(lst):
    """Reverse list without using .reverse() or slicing."""
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print("\n=== Exercise 8: List Reverser ===")
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]

# ---

# 9. Default Parameters
def power(base, exponent=2):
    """Calculate base^exponent with default exponent of 2."""
    return base ** exponent

print("\n=== Exercise 9: Default Parameters ===")
print(power(5))      # 25 (5^2)
print(power(5, 3))   # 125 (5^3)

# ---

# 10. Apply Twice (Higher-Order Function)
def apply_twice(func, arg):
    """Apply function to argument twice."""
    return func(func(arg))

def add_five(x):
    return x + 5

print("\n=== Exercise 10: Apply Twice ===")
print(apply_twice(add_five, 10))  # 20

# ---

# 11. Variable Arguments Sum
def sum_all(*numbers):
    """Sum any number of arguments using *args."""
    return sum(numbers)

print("\n=== Exercise 11: Variable Arguments Sum ===")
print(sum_all(1, 2, 3))              # 6
print(sum_all(10, 20, 30, 40, 50))   # 150

# ---

# 12. Keyword Arguments Printer
def print_info(**kwargs):
    """Print all keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\n=== Exercise 12: Keyword Arguments ===")
print_info(name="Alice", age=30, city="NYC")

# =============================================================================
# HARD LEVEL
# =============================================================================

# 13. Recursive Factorial
def factorial(n):
    """Calculate factorial using recursion."""
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print("\n=== Exercise 13: Recursive Factorial ===")
print(factorial(5))  # 120

# ---

# 14. Recursive List Flatten
def flatten(lst):
    """Flatten arbitrarily nested lists recursively."""
    result = []
    for item in lst:
        if isinstance(item, list):
            # Recursively flatten nested list
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print("\n=== Exercise 14: Recursive Flatten ===")
print(flatten([1, [2, 3], [[4], 5]]))  # [1, 2, 3, 4, 5]

# ---

# 15. Fibonacci Sequence
def fibonacci(n):
    """Return nth Fibonacci number using recursion."""
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n=== Exercise 15: Fibonacci ===")
print(f"Fibonacci sequence: {[fibonacci(i) for i in range(10)]}")

# ---

# 16. Timer Decorator
def timer(func):
    """Decorator to measure execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """Example slow function."""
    time.sleep(1)
    return "Done"

print("\n=== Exercise 16: Timer Decorator ===")
slow_function()

# ---

# 17. Group by First Letter
def group_by_first_letter(words):
    """Group words by their first letter."""
    result = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(word)
    return result

# Alternative using defaultdict
from collections import defaultdict

def group_by_first_letter_alt(words):
    result = defaultdict(list)
    for word in words:
        result[word[0].lower()].append(word)
    return dict(result)

print("\n=== Exercise 17: Group by First Letter ===")
words = ["apple", "banana", "apricot", "blueberry"] 
print(group_by_first_letter(words))

# ---

# 18. Command Dispatcher
def run(command, *args):
    """Execute command using dictionary dispatch."""
    commands = {
        'add': lambda a, b: a + b,
        'multiply': lambda a, b: a * b,
        'greet': lambda name: f"Hello, {name}",
        'power': lambda base, exp: base ** exp
    }
    if command in commands:
        return commands[command](*args)
    return f"Unknown command: {command}"

print("\n=== Exercise 18: Command Dispatcher ===")
print(run('add', 5, 3))        # 8
print(run('greet', 'Alice'))   # Hello, Alice

# ---

# 19. Memoization Decorator
def memoize(func):
    """Decorator to cache function results."""
    cache = {}
    
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    
    return wrapper

@memoize
def fibonacci_memoized(n):
    """Fibonacci with memoization for speed."""
    if n < 2:
        return n
    return fibonacci_memoized(n-1) + fibonacci_memoized(n-2)

print("\n=== Exercise 19: Memoization ===")
print(f"Fibonacci(50) = {fibonacci_memoized(50)}")  # Fast with caching!

# Alternative using functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# ---

# 20. Closure Counter
def make_counter():
    """Return a closure function that maintains a counter."""
    count = 0  # Enclosing scope variable
    
    def increment():
        nonlocal count  # Modify enclosing variable
        count += 1
        return count
    
    return increment

print("\n=== Exercise 20: Closure Counter ===")
counter1 = make_counter()
print(counter1())  # 1
print(counter1())  # 2

counter2 = make_counter()  # Independent counter
print(counter2())  # 1

# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# 21. Function Composer
def compose(f, g):
    """Return function h where h(x) = f(g(x))."""
    def composed(x):
        return f(g(x))
    return composed

def add_one(x):
    return x + 1

def double(x):
    return x * 2

print("\n=== Exercise 21: Function Composer ===")
add_then_double = compose(double, add_one)
print(add_then_double(5))  # 12 (double(add_one(5)))

# ---

# 22. Currying Function  
def curry(func, *partial_args):
    """Enable partial application of function."""
    def curried(*args):
        return func(*(partial_args + args))
    return curried

def add_three(a, b, c):
    return a + b + c

print("\n=== Exercise 22: Currying ===")
add_five_and_ten = curry(add_three, 5, 10)
print(add_five_and_ten(20))  # 35

# Alternative using functools.partial
from functools import partial

add_five_and_ten_alt = partial(add_three, 5, 10)
print(add_five_and_ten_alt(20))  # 35

# =============================================================================
# ADDITIONAL EXAMPLES
# =============================================================================

print("\n=== Additional Concepts ===")

# Lambda functions in practice
print("\n--- Lambda Examples ---")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

# Decorator with arguments
def repeat(times):
    """Decorator factory that repeats function calls."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet_random():
    return "Hello!"

print(f"\nRepeated greetings: {greet_random()}")

# Closure for encapsulation
def make_account(initial_balance):
    """Create a simple account with closure."""
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    
    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        return "Insufficient funds"
    
    def get_balance():
        return balance
    
    return deposit, withdraw, get_balance

print("\n--- Bank Account Closure ---")
deposit, withdraw, balance = make_account(100)
print(f"Initial: {balance()}")
print(f"After deposit 50: {deposit(50)}")
print(f"After withdraw 30: {withdraw(30)}")

print("\n=== All Solutions Complete! ===")
