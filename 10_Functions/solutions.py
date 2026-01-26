# Solutions – Functions
import math

# ==========================================
# Easy
# ==========================================

# 1. Even Checker
def exercise_1(n):
    return n % 2 == 0

# 2. Circle Area
def exercise_2(radius):
    return math.pi * (radius ** 2)

# 3. Simple Greeting
def exercise_3():
    print("Hello, World!")

# 4. Name Greeting
def exercise_4(name):
    return f"Hello, {name}!"

# 5. Temp Converter
def exercise_5(celsius):
    return celsius * 9/5 + 32


# ==========================================
# Medium
# ==========================================

# 6. Max of Three
def exercise_6(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# 7. Vowel Counter
def exercise_7(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

# 8. List Reverser
def exercise_8(lst):
    new_lst = []
    for i in range(len(lst) - 1, -1, -1):
        new_lst.append(lst[i])
    return new_lst

# 9. Default Parameters
def exercise_9(base, exponent=2):
    return base ** exponent

# 10. Apply Twice
def exercise_10(func, arg):
    return func(func(arg))

# 11. Sum All (*args)
def exercise_11(*args):
    return sum(args)

# 12. Keyword Printer (**kwargs)
def exercise_12(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


# ==========================================
# Hard
# ==========================================

# 13. Recursive Factorial
def exercise_13(n):
    if n <= 1:
        return 1
    return n * exercise_13(n - 1)

# 14. Recursive Flatten
def exercise_14(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(exercise_14(item))
        else:
            flat.append(item)
    return flat

# 15. Recursive Fibonacci
def exercise_15(n):
    if n <= 0: return 0
    if n == 1: return 1
    return exercise_15(n-1) + exercise_15(n-2)

# 17. Group by First Letter
def exercise_17(words):
    groups = {}
    for word in words:
        letter = word[0].lower()
        if letter not in groups:
            groups[letter] = []
        groups[letter].append(word)
    return groups

# 18. Command Dispatcher
def exercise_18(command, *args):
    cmds = {
        'add': lambda a, b: a + b,
        'multiply': lambda a, b: a * b,
        'greet': lambda name: f"Hello, {name}"
    }
    if command in cmds:
        return cmds[command](*args)
    return "Unknown command"


# ==========================================
# Bonus
# ==========================================

# 21. Composer
def exercise_21(f, g):
    def h(x):
        return f(g(x))
    return h

# 22. Currying
def exercise_22(func, *fixed_args):
    def wrapper(*remaining_args):
        return func(*(fixed_args + remaining_args))
    return wrapper


# Test Execution
if __name__ == "__main__":
    print(f"Even 4? {exercise_1(4)}")
    print(f"Area 5: {exercise_2(5)}")
    exercise_3()
    print(exercise_4("Alice"))
    print(f"20C to F: {exercise_5(20)}")
    print(f"Max 10,20,5: {exercise_6(10,20,5)}")
    print(f"Vowels 'hello': {exercise_7('hello')}")
    print(f"Rev [1,2]: {exercise_8([1,2])}")
    print(f"Pow 2^3: {exercise_9(2,3)}")
    print(f"Apply x+1 twice to 5: {exercise_10(lambda x: x+1, 5)}")
    print(f"Sum 1,2,3: {exercise_11(1,2,3)}")
    exercise_12(a=1, b=2)
    print(f"Fact 5: {exercise_13(5)}")
    print(f"Flat [1,[2]]: {exercise_14([1,[2]])}")
    print(f"Fib 6: {exercise_15(6)}")
    print(f"Group: {exercise_17(['apple', 'banana'])}")
    print(f"Dispatch Add: {exercise_18('add', 5, 3)}")
    
    add_one = lambda x: x+1
    double = lambda x: x*2
    composed = exercise_21(double, add_one)
    print(f"Compose (5+1)*2: {composed(5)}")
    
    def add3(a,b,c): return a+b+c
    curried = exercise_22(add3, 1, 2)
    print(f"Curry 1+2+3: {curried(3)}")
