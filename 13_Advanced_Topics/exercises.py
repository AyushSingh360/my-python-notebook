# Exercises – Advanced Python
import time
import functools
from typing import List, Dict

# Helper to print section headers
def print_header(title):
    print(f"\n=== {title} ===")

# =============================================================================
# EASY LEVEL
# =============================================================================

def exercise_1():
    """
    1. Lambda Functions
    Write a lambda function that takes a number and returns its square. 
    Use it to square the number 8.
    """
    print_header("Exercise 1: Lambda Functions")
    # Write your code here
    pass

def exercise_2():
    """
    2. List Comprehension
    Create a list of numbers from 0 to 9. 
    Use a list comprehension to create a new list containing only the even numbers.
    """
    print_header("Exercise 2: List Comprehension")
    # Write your code here
    pass

def exercise_3():
    """
    3. Basic Exception Handling
    Write a function that divides two numbers. 
    Use `try...except` to catch `ZeroDivisionError` and print a friendly message.
    """
    print_header("Exercise 3: Exception Handling")
    # Write your code here
    pass

def exercise_4():
    """
    4. Simple Generator
    Write a generator function `yield_colors()` that yields "Red", "Green", and "Blue". 
    Iterate over it and print each color.
    """
    print_header("Exercise 4: Simple Generator")
    # Write your code here
    pass

def exercise_5():
    """
    5. Map Function
    Use `map()` and a lambda to convert a list of strings `["1", "2", "3"]` 
    into a list of integers `[1, 2, 3]`.
    """
    print_header("Exercise 5: Map Function")
    # Write your code here
    pass

# =============================================================================
# MEDIUM LEVEL
# =============================================================================

def exercise_6():
    """
    6. Custom Exception
    Define a custom exception class `NegativeNumberError`. 
    Write a function that raises this if the input argument number is negative.
    """
    print_header("Exercise 6: Custom Exception")
    # Write your code here
    pass

def exercise_7():
    """
    7. Dictionary Comprehension
    Given a list of words `["apple", "banana", "cherry"]`, 
    use a dict comprehension to create a dictionary mapping the word to its length.
    """
    print_header("Exercise 7: Dict Comprehension")
    # Write your code here
    pass

def exercise_8():
    """
    8. Basic Decorator
    Write a decorator `@simple_logger` that prints "Function started..." before 
    calling the function and "Function ended." after.
    """
    print_header("Exercise 8: Basic Decorator")
    # Write your code here
    pass

def exercise_9():
    """
    9. File Context Manager
    Use the `with` statement to write "Hello World" to a file `test.txt`, 
    then read it back and print the content.
    """
    print_header("Exercise 9: File Context Manager")
    # Write your code here
    pass

def exercise_10():
    """
    10. Filter Function
    Use `filter()` to extract names starting with "A" from `["Alice", "Bob", "Charlie", "Adam"]`.
    """
    print_header("Exercise 10: Filter Function")
    # Write your code here
    pass

def exercise_11():
    """
    11. Generator Expression
    Create a generator expression (not a function) that squares numbers from 0 to 10. 
    Print the sum of these squares (use `sum()`).
    """
    print_header("Exercise 11: Generator Expression")
    # Write your code here
    pass

# =============================================================================
# HARD LEVEL
# =============================================================================

def exercise_12():
    """
    12. Context Manager Class
    Implement a class `Timer` that acts as a context manager. 
    It should measure and print the time taken to execute the block inside `with Timer():`.
    """
    print_header("Exercise 12: Context Manager Class")
    # Write your code here
    pass

def exercise_13():
    """
    13. Decorator with Arguments
    Write a decorator `@repeat(n)` that repeats the execution of the decorated function `n` times.
    """
    print_header("Exercise 13: Decorator with Arguments")
    # Write your code here
    pass

def exercise_14():
    """
    14. Custom Iterator
    Create a class `Countdown` that implements the iterator protocol (`__iter__` and `__next__`). 
    It should count down from `n` to 0.
    """
    print_header("Exercise 14: Custom Iterator")
    # Write your code here
    pass

def exercise_15():
    """
    15. Exception Chaining
    Write code that catches a `ValueError` inside a `try` block, 
    and raises a custom `DataProcessingError` from it using `raise ... from ...`.
    """
    print_header("Exercise 15: Exception Chaining")
    # Write your code here
    pass

def exercise_16():
    """
    16. Nested Decorators
    Apply two decorators to a function: one that converts the result to string, 
    and another that uppercases the string. Observe the order of execution.
    """
    print_header("Exercise 16: Nested Decorators")
    # Write your code here
    pass

def exercise_17():
    """
    17. Safe Execution Wrapper
    Write a function `safe_execute(func, *args)` that calls `func(*args)` inside a try/except block 
    and returns `None` if an error occurs, preventing the crash.
    """
    print_header("Exercise 17: Safe Execution Wrapper")
    # Write your code here
    pass

def exercise_18():
    """
    18. Infinite Generator
    Create a generator that yields the Fibonacci sequence indefinitely. 
    Use `next()` to print the first 10 numbers.
    """
    print_header("Exercise 18: Infinite Generator")
    # Write your code here
    pass

# =============================================================================
# BONUS CHALLENGES
# =============================================================================

def exercise_19():
    """
    19. Type Hinting
    Annotate a function `calculate_stats(data: List[int]) -> Dict[str, float]` 
    and use type annotations for variables.
    """
    print_header("Exercise 19: Type Hinting")
    # Write your code here
    pass

def exercise_20():
    """
    20. Coroutines (Intro)
    Write a simple coroutine using `yield` that receives data sent via `.send()`.
    """
    print_header("Exercise 20: Coroutines")
    # Write your code here
    pass

def exercise_21():
    """
    21. Generator Pipeline
    Create a pipeline of 3 generators/iterables:
    1. Generates numbers 1-100.
    2. Squares them.
    3. Filters for numbers divisible by 5.
    Iterate and print the first 5 results.
    """
    print_header("Exercise 21: Generator Pipeline")
    # Write your code here
    pass

def exercise_22():
    """
    22. Singleton Decorator
    Write a decorator `@singleton` that ensures a class only has one instance.
    """
    print_header("Exercise 22: Singleton Decorator")
    # Write your code here
    pass

if __name__ == '__main__':
    # Call exercises here to test
    exercise_1()
    print("\nRun specific examples by calling the functions above!")
