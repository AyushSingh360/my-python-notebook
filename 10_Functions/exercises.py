# Exercises – Functions

Practice creating and using functions with these progressively challenging exercises!

## Easy Level

### 1. Even Number Checker
Write a function `is_even(n)` that returns `True` if the number is even, `False` otherwise.

**Example:**
```python
is_even(4)  # True
is_even(7)  # False
```

---

### 2. Circle Area Calculator
Create a function `area_circle(r)` that calculates the area of a circle given its radius.  
Formula: area = π × r²

**Hint:** Import `math.pi` or use `3.14159`

---

### 3. Simple Greeting
Write a function `say_hello()` that prints "Hello, World!" (no parameters, no return value).

---

### 4. Name Greeting
Create a function `greet(name)` that returns a personalized greeting.

**Example:**
```python
greet("Alice")  # Returns "Hello, Alice!"
```

---

### 5. Temperature Converter
Write `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit.  
Formula: F = C × 9/5 + 32

---

## Medium Level

### 6. Maximum of Three
Create `max_of_three(a, b, c)` that returns the largest of three numbers.

**Don't use** built-in `max()` function.

---

### 7. Vowel Counter
Write `count_vowels(s)` that counts the number of vowels (a, e, i, o, u) in a string.

**Example:**
```python
count_vowels("hello world")  # Returns 3
```

---

### 8. List Reverser
Create `reverse_list(lst)` that returns a new list with elements in reverse order.

**Don't use** `.reverse()` or slicing `[::-1]`

---

### 9. Default Parameters
Write `power(base, exponent=2)` that calculates base^exponent. Default exponent should be 2.

**Example:**
```python
power(5)      # Returns 25 (5^2)
power(5, 3)   # Returns 125 (5^3)
```

---

### 10. Apply Twice (Higher-Order Function)
Create `apply_twice(func, arg)` that applies a function to an argument twice.

**Example:**
```python
def add_five(x):
    return x + 5

apply_twice(add_five, 10)  # Returns 20 (add_five(add_five(10)))
```

---

### 11. Variable Arguments Sum
Write `sum_all(*numbers)` that returns the sum of any number of arguments.

**Example:**
```python
sum_all(1, 2, 3)           # Returns 6
sum_all(10, 20, 30, 40, 50)  # Returns 150
```

---

### 12. Keyword Arguments Printer
Create `print_info(**kwargs)` that prints all keyword arguments in "key: value" format.

**Example:**
```python
print_info(name="Alice", age=30, city="NYC")
# Output:
# name: Alice
# age: 30
# city: NYC
```

---

## Hard Level

### 13. Recursive Factorial
Implement `factorial(n)` using recursion.

**Base case:** factorial(0) = 1  
**Recursive case:** factorial(n) = n × factorial(n-1)

**Example:**
```python
factorial(5)  # Returns 120 (5 × 4 × 3 × 2 × 1)
```

---

### 14. Recursive List Flatten
Write `flatten(lst)` that flattens arbitrarily nested lists using recursion.

**Example:**
```python
flatten([1, [2, 3], [[4], 5]])  # Returns [1, 2, 3, 4, 5]
```

---

### 15. Fibonacci Sequence
Create `fibonacci(n)` that returns the nth Fibonacci number using recursion.

**Base cases:** fib(0) = 0, fib(1) = 1  
**Recursive:** fib(n) = fib(n-1) + fib(n-2)

---

### 16. Timer Decorator
Create a `@timer` decorator that prints the execution time of a function.

**Example:**
```python
import time

@timer
def slow_function():
    time.sleep(2)
    return "Done"

slow_function()
# Output: "Function 'slow_function' took 2.00 seconds"
```

---

### 17. Group by First Letter
Write `group_by_first_letter(words)` that returns a dictionary grouping words by their first letter.

**Example:**
```python
group_by_first_letter(["apple", "banana", "apricot", "blueberry"])
# Returns:
# {
#     'a': ['apple', 'apricot'],
#     'b': ['banana', 'blueberry']
# }
```

---

### 18. Command Dispatcher
Create a `run(command, *args)` function that uses a dictionary to dispatch commands.

**Example:**
```python
def run(command, *args):
    commands = {
        'add': lambda a, b: a + b,
        'multiply': lambda a, b: a * b,
        'greet': lambda name: f"Hello, {name}"
    }
    return commands[command](*args)

run('add', 5, 3)           # Returns 8
run('greet', 'Alice')      # Returns "Hello, Alice"
```

---

### 19. Memoization Decorator
Create a `@memoize` decorator that caches function results for given arguments.

**Use case:** Speed up expensive recursive functions like Fibonacci.

---

### 20. Closure Counter
Write a function `make_counter()` that returns a closure function maintaining a counter.

**Example:**
```python
counter1 = make_counter()
print(counter1())  # 1
print(counter1())  # 2

counter2 = make_counter()
print(counter2())  # 1 (independent counter)
```

---

## Bonus Challenges

### 21. Function Composer
Create `compose(f, g)` that returns a new function h(x) = f(g(x)).

**Example:**
```python
def add_one(x):
    return x + 1

def double(x):
    return x * 2

add_then_double = compose(double, add_one)
add_then_double(5)  # Returns 12 (double(add_one(5)))
```

---

### 22. Currying Function
Implement `curry(func, *args)` that enables partial application.

**Example:**
```python
def add_three(a, b, c):
    return a + b + c

add_five_and_ten = curry(add_three, 5, 10)
result = add_five_and_ten(20)  # Returns 35
```

---

## Test Your Knowledge

After completing these exercises, you should be comfortable with:
- ✅ Defining functions with various parameter types
- ✅ Using *args and **kwargs
- ✅ Understanding scope (LEGB rule)
- ✅ Writing recursive functions
- ✅ Creating and using decorators
- ✅ Working with closures and higher-order functions
- ✅ Applying lambda functions effectively

**See `solutions.py` for complete solutions with explanations!**
