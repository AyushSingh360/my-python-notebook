# Exercises – Advanced Python

## Easy Level

### 1. Lambda Functions
Write a lambda function that takes a number and returns its square. Use it to square the number 8.

### 2. List Comprehension
Create a list of numbers from 0 to 9. Use a list comprehension to create a new list containing only the even numbers.

### 3. Basic Exception Handling
Write a function that divides two numbers. Use `try...except` to catch `ZeroDivisionError` and print a friendly message.

### 4. Simple Generator
Write a generator function `yield_colors()` that yields "Red", "Green", and "Blue" one by one. Iterate over it and print.

### 5. Map Function
Use `map()` and a lambda to convert a list of strings `["1", "2", "3"]` into a list of integers `[1, 2, 3]`.

## Medium Level

### 6. Custom Exception
Define a custom exception class `NegativeNumberError`. Write a function that raises this if the input is negative.

### 7. Dictionary Comprehension
Given a list of words `["apple", "banana", "cherry"]`, use a dict comprehension to create a dictionary mapping the word to its length.

### 8. Basic Decorator
Write a decorator `@simple_logger` that prints "Function started..." before calling the function and "Function ended." after.

### 9. File Context Manager
Use the `with` statement to write "Hello World" to a file `test.txt`, then read it back and print the content.

### 10. Filter Function
Use `filter()` to extract names starting with "A" from a list `["Alice", "Bob", "Charlie", "Adam"]`.

### 11. Generator Expression
Create a generator expression (not a function) that squares numbers from 0 to 10. Print the sum of these squares.

## Hard Level

### 12. Context Manager Class
Implement a class `Timer` that acts as a context manager. It should measure and print the time taken to execute the block inside `with Timer():`.

### 13. Decorator with Arguments
Write a decorator `@repeat(n)` that repeats the execution of the decorated function `n` times.

### 14. Custom Iterator
Create a class `Countdown` that implements the iterator protocol (`__iter__` and `__next__`). It should count down from `n` to 0.

### 15. Exception Chaining
Write code that catches a `ValueError` inside a `try` block, and raises a custom `DataProcessingError` from it using `raise ... from ...`.

### 16. Nested Decorators
Apply two decorators to a function: one that converts the result to string, and another that uppercases the string. Observe the order of execution.

### 17. Safe Execution Wrapper
Write a function `safe_execute(func, *args)` that calls `func(*args)` inside a try/except block and returns `None` if an error occurs, preventing the crash.

### 18. Infinite Generator
Create a generator that yields the Fibonacci sequence indefinitely. Use `next()` to print the first 10 numbers.

## Bonus Challenges

### 19. Type Hinting
Annotate a function `calculate_stats(data: list[int]) -> dict[str, float]` and use `mypy` style annotations for variables.

### 20. Coroutines (Intro)
Write a simple coroutine using `yield` that receives data sent via `.send()`.

### 21. Generator Pipeline
Create a pipeline of 3 generators: 
1. Generates numbers 1-100.
2. Squares them.
3. Filters for numbers divisible by 5.
Iterate and print.

### 22. Singleton Decorator
Write a decorator `@singleton` that ensures a class only has one instance.

**See `solutions.py` for complete solutions!**
