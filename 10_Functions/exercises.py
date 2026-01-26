# Exercises – Functions
# Fill in the code blocks below to solve the exercises.

# ==========================================
# Easy
# ==========================================

def exercise_1(n):
    """
    1. Even Number Checker
    Return True if `n` is even, False otherwise.
    """
    # Write your code here
    pass

def exercise_2(radius):
    """
    2. Circle Area
    Calculate area of circle (pi * r^2).
    Use 3.14159 or math.pi for pi.
    """
    # Write your code here
    pass

def exercise_3():
    """
    3. Simple Greeting
    Print "Hello, World!".
    """
    # Write your code here
    pass

def exercise_4(name):
    """
    4. Name Greeting
    Return a string "Hello, {name}!".
    """
    # Write your code here
    pass

def exercise_5(celsius):
    """
    5. Temperature Converter
    Convert `celsius` to Fahrenheit.
    Formula: F = C * 9/5 + 32
    """
    # Write your code here
    pass


# ==========================================
# Medium
# ==========================================

def exercise_6(a, b, c):
    """
    6. Maximum of Three
    Return the largest of three numbers (a, b, c).
    Do NOT use the built-in max() function.
    """
    # Write your code here
    pass

def exercise_7(text):
    """
    7. Vowel Counter
    Count the number of vowels (a, e, i, o, u) in `text`.
    Case insensitive (A and a both count).
    """
    # Write your code here
    pass

def exercise_8(lst):
    """
    8. List Reverser
    Return a NEW list with elements of `lst` in reverse order.
    Do NOT use lst.reverse() or lst[::-1].
    """
    # Write your code here
    pass

def exercise_9(base, exponent=2):
    """
    9. Default Parameters
    Calculate base to the power of exponent.
    Default exponent should be 2.
    """
    # Write your code here
    pass

def exercise_10(func, arg):
    """
    10. Apply Twice
    Apply the function `func` to `arg` twice.
    Result = func(func(arg))
    """
    # Write your code here
    pass

def exercise_11(*args):
    """
    11. Sum All
    Return the sum of all positional arguments passed.
    """
    # Write your code here
    pass

def exercise_12(**kwargs):
    """
    12. Keyword Printer
    Print all keyword arguments in "key: value" format.
    """
    # Write your code here
    pass


# ==========================================
# Hard
# ==========================================

def exercise_13(n):
    """
    13. Recursive Factorial
    Calculate n! using recursion.
    Base case: n=0 or n=1 -> 1.
    """
    # Write your code here
    pass

def exercise_14(nested_list):
    """
    14. Recursive Flatten
    Flatten an arbitrarily nested list.
    Ex: [1, [2, [3]]] -> [1, 2, 3]
    """
    # Write your code here
    pass

def exercise_15(n):
    """
    15. Recursive Fibonacci
    Return the nth Fibonacci number.
    fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2).
    """
    # Write your code here
    pass

def exercise_17(words):
    """
    17. Group by First Letter
    Group a list of `words` by their first letter.
    Return a dict: {'a': ['apple', ...], 'b': ['banana']}
    """
    # Write your code here
    pass

def exercise_18(command, *args):
    """
    18. Command Dispatcher
    Using a dictionary of lambda functions:
    - 'add': a+b
    - 'multiply': a*b
    - 'greet': "Hello, {name}"
    Execute the command with *args and return result.
    """
    # Write your code here
    pass


# ==========================================
# Bonus
# ==========================================

def exercise_21(f, g):
    """
    21. Function Composer
    Return a new function h(x) such that h(x) = f(g(x)).
    """
    # Write your code here
    pass

def exercise_22(func, *fixed_args):
    """
    22. Currying / Partial Application
    Return a new function that takes remaining args and calls func.
    Equivalent to functools.partial.
    """
    # Write your code here
    pass

if __name__ == "__main__":
    # Test your functions here
    pass
