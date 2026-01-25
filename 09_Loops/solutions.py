# Solutions – Loops

import random

# ==========================================
# Easy
# ==========================================

# 1. Countdown Timer
def exercise_1():
    print("--- 1. Countdown ---")
    count = 10
    while count > 0:
        print(count, end=" ")
        count -= 1
    print("Blastoff!")

# 2. Factorial Calculator
def exercise_2():
    print("--- 2. Factorial ---")
    result = 1
    for i in range(1, 7): # 1 to 6
        result *= i
    return result

# 3. Character Iterator
def exercise_3(text):
    print("--- 3. Char Iter ---")
    for char in text:
        print(char)

# ==========================================
# Medium
# ==========================================

# 4. Fibonacci Sequence
def exercise_4(n):
    fibs = []
    a, b = 0, 1
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return fibs

# 5. Filter Even Numbers
def exercise_5(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

# 6. Interactive Menu System
def exercise_6():
    print("--- 6. Menu ---")
    # Simulating 2 iterations then exit
    simulated_inputs = ["1", "3", "2"] # 1: Start, 3: Invalid, 2: Exit
    
    for choice in simulated_inputs:
        print(f"User chose: {choice}")
        if choice == "1":
            print("Starting game...")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option")

# 7. Sum of Digits
def exercise_7(number):
    total = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10
    return total

# 8. Multiplication Table
def exercise_8(num):
    print(f"--- 8. Table for {num} ---")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


# ==========================================
# Hard
# ==========================================

# 9. Number Guessing Game (Simulation)
def exercise_9():
    target = 42
    guesses = [10, 50, 42] # Simulated user input
    print("--- 9. Guessing Game ---")
    
    for guess in guesses:
        print(f"Guess: {guess}")
        if guess < target:
            print("Higher")
        elif guess > target:
            print("Lower")
        else:
            print("Correct!")
            break

# 10. Prime Number Generator
def exercise_10(limit):
    primes = []
    for num in range(2, limit):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# 11. List Flattening
def exercise_11(nested_list):
    flat = []
    for sublist in nested_list:
        for item in sublist:
            flat.append(item)
    return flat

# 12. GCD (Euclidean Algorithm)
def exercise_12(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 13. Pattern Printing
def exercise_13(rows):
    print("--- 13. Pyramid ---")
    for i in range(1, rows + 1):
        # Spaces: rows - i
        # Stars: 2*i - 1
        line = " " * (rows - i) + "*" * (2 * i - 1)
        print(line)

# 14. Word Frequency Counter
def exercise_14(sentence):
    freq = {}
    # Use simple split, real world would strip punctuation
    words = sentence.split()
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# 15. Reverse String
def exercise_15(text):
    reversed_str = ""
    # Iterate indices backwards: len-1 down to 0
    for i in range(len(text) - 1, -1, -1):
        reversed_str += text[i]
    return reversed_str


# ==========================================
# Bonus
# ==========================================

# 16. Find Pairs
def exercise_16(numbers, target):
    pairs = []
    # Nested loop
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs

# 17. Pascal's Triangle
def exercise_17(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        # Inner values are sum of two above
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

# 18. Collatz Sequence
def exercise_18(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq


# Test Execution
if __name__ == "__main__":
    exercise_1()
    print(f"Fact 6: {exercise_2()}")
    exercise_3("Loop")
    print(f"Fibs 8: {exercise_4(8)}")
    print(f"Evens: {exercise_5([1, 2, 3, 4, 5])}")
    exercise_6()
    print(f"Sum digits 12345: {exercise_7(12345)}")
    exercise_8(5)
    exercise_9()
    print(f"Primes < 20: {exercise_10(20)}")
    print(f"Flat: {exercise_11([[1, 2], [3, 4]])}")
    print(f"GCD 48, 18: {exercise_12(48, 18)}")
    exercise_13(3)
    print(f"Freq: {exercise_14('a b a c')}")
    print(f"Rev 'Python': {exercise_15('Python')}")
    print(f"Pairs sum 9: {exercise_16([2, 7, 11, 15], 9)}")
    print(f"Pascal 3: {exercise_17(3)}")
    print(f"Collatz 6: {exercise_18(6)}")
