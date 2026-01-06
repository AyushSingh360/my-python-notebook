# Solutions – Loops
# Complete solutions with detailed explanations for all exercises

# =============================================================================
# EASY LEVEL
# =============================================================================

# 1. Countdown Timer
# Uses while loop, decrementing counter until it reaches 0
print("=== Exercise 1: Countdown Timer ===")
count = 10
while count > 0:
    print(count)
    count -= 1  # Decrement to avoid infinite loop
print("Blastoff!")

# ---

# 2. Factorial Calculator
# Factorial: n! = n × (n-1) × (n-2) × ... × 1
print("\n=== Exercise 2: Factorial Calculator ===")
factorial = 1
for n in range(1, 7):  # 1, 2, 3, 4, 5, 6
    factorial *= n
print(f"6! = {factorial}")  # 720

# ---

# 3. Character Iterator
# Simple for loop over string characters
print("\n=== Exercise 3: Character Iterator ===")
for char in "loop":
    print(char)

# =============================================================================
# MEDIUM LEVEL
# =============================================================================

# 4. Fibonacci Sequence
# Each number is sum of previous two: 0, 1, 1, 2, 3, 5, 8, ...
print("\n=== Exercise 4: Fibonacci Sequence ===")
n = int(input("How many Fibonacci numbers? "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Simultaneous assignment: next value, sum
print()

# ---

# 5. Filter Even Numbers
# Accumulator pattern: build new list based on condition
print("\n=== Exercise 5: Filter Even Numbers ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:  # Modulo operator checks divisibility
        evens.append(num)
print(f"Even numbers: {evens}")

# ---

# 6. Interactive Menu System
# while True with break pattern for indefinite repetition
print("\n=== Exercise 6: Interactive Menu System ===")
while True:
    print("\n1. Start Game")
    print("2. View Scores")
    print("3. Settings")
    print("0. Exit")
    choice = input("Choice: ")
    
    if choice == "0":
        print("Goodbye!")
        break  # Exit loop
    elif choice in ["1", "2", "3"]:
        print(f"You selected option {choice}")
    else:
        print("Invalid choice, try again")

# ---

# 7. Sum of Digits
# Use modulo and integer division to extract digits
print("\n=== Exercise 7: Sum of Digits ===")
number = int(input("Enter a positive integer: "))
digit_sum = 0
temp = number  # Keep original for display
while temp > 0:
    digit = temp % 10    # Get last digit
    digit_sum += digit   # Add to sum
    temp //= 10          # Remove last digit
print(f"Sum of digits of {number}: {digit_sum}")

# ---

# 8. Multiplication Table
# Simple for loop with range
print("\n=== Exercise 8: Multiplication Table ===")
num = int(input("Enter a number (1-10): "))
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")

# =============================================================================
# HARD LEVEL
# =============================================================================

# 9. Number Guessing Game
# Uses random module, while loop, and conditional hints
print("\n=== Exercise 9: Number Guessing Game ===")
import random

target = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100...")
while True:
    guess = int(input("Your guess: "))
    attempts += 1
    
    if guess == target:
        print(f"🎉 You won in {attempts} attempts!")
        break
    elif guess < target:
        print("Higher!")
    else:
        print("Lower!")

# ---

# 10. Prime Number Generator
# Nested loops with for...else pattern
print("\n=== Exercise 10: Prime Number Generator ===")
primes = []
for num in range(2, 100):  # Check numbers from 2 to 99
    # Check if num is divisible by any number from 2 to sqrt(num)
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            break  # Not prime, exit inner loop
    else:
        # else executes only if break was never called
        primes.append(num)
print(f"Primes < 100: {primes}")
print(f"Total: {len(primes)} primes")

# ---

# 11. List Flattening
# Nested loops: outer for sublists, inner for elements
print("\n=== Exercise 11: List Flattening ===")
nested_list = [[1, 2], [3, 4], [5, 6, 7]]
flattened = []
for sublist in nested_list:
    for element in sublist:
        flattened.append(element)
print(f"Flattened: {flattened}")

# ---

# 12. Greatest Common Divisor (GCD)
# Euclidean algorithm using while loop
print("\n=== Exercise 12: GCD (Euclidean Algorithm) ===")
a, b = 48, 18
print(f"Finding GCD of {a} and {b}")
original_a, original_b = a, b

while b != 0:
    print(f"  {a} ÷ {b} = {a // b} remainder {a % b}")
    a, b = b, a % b  # Replace with remainder

print(f"GCD({original_a}, {original_b}) = {a}")

# ---

# 13. Pattern Printing (Pyramid)
# Nested loops with calculated spaces and stars
print("\n=== Exercise 13: Pyramid Pattern ===")
rows = 5
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# ---

# 14. Word Frequency Counter
# Dictionary accumulator pattern
print("\n=== Exercise 14: Word Frequency Counter ===")
sentence = "the quick brown fox jumps over the lazy dog"
word_freq = {}

for word in sentence.split():
    # If word exists, increment; otherwise, set to 1
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word frequencies:")
for word, count in word_freq.items():
    print(f"  '{word}': {count}")

# ---

# 15. Reverse String (No Built-in Reverse)
# Build new string by iterating backwards
print("\n=== Exercise 15: Reverse String ===")
text = input("Enter a string: ")
reversed_text = ""
for i in range(len(text) - 1, -1, -1):  # Start at last index, go to 0
    reversed_text += text[i]
print(f"Reversed: {reversed_text}")

# Alternative using negative indexing
reversed_alt = ""
for i in range(len(text)):
    reversed_alt += text[-(i + 1)]  # -1, -2, -3, ...
print(f"Alternative method: {reversed_alt}")

# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# 16. Find All Pairs with Target Sum
# Nested loops with early optimization
print("\n=== Exercise 16: Find Pairs with Target Sum ===")
numbers = [2, 7, 11, 15, 3]
target = 9
pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):  # Avoid duplicates
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print(f"Pairs that sum to {target}: {pairs}")

# ---

# 17. Pascal's Triangle
# Each element is sum of two elements above it
print("\n=== Exercise 17: Pascal's Triangle ===")
n = int(input("How many rows? "))

for row_num in range(n):
    # Calculate leading spaces for centering
    print(" " * (n - row_num - 1), end="")
    
    # Calculate values for this row
    value = 1
    for col in range(row_num + 1):
        print(value, end=" ")
        # Next value in row: value * (row - col) / (col + 1)
        value = value * (row_num - col) // (col + 1)
    print()  # New line after each row

# ---

# 18. Collatz Sequence
# 3n+1 problem: always reaches 1 (conjecture)
print("\n=== Exercise 18: Collatz Sequence ===")
n = int(input("Enter starting number: "))
sequence = [n]
steps = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2  # Even: divide by 2
    else:
        n = 3 * n + 1  # Odd: multiply by 3 and add 1
    sequence.append(n)
    steps += 1

print(f"Sequence: {' → '.join(map(str, sequence))}")
print(f"Reached 1 in {steps} steps")

# =============================================================================
# PERFORMANCE COMPARISON
# =============================================================================

print("\n=== Performance Tips ===")
print("List comprehension vs loop for simple transformations:")

# Traditional loop
import time
start = time.time()
squares_loop = []
for i in range(10000):
    squares_loop.append(i ** 2)
loop_time = time.time() - start

# List comprehension
start = time.time()
squares_comp = [i ** 2 for i in range(10000)]
comp_time = time.time() - start

print(f"Loop: {loop_time:.6f}s")
print(f"Comprehension: {comp_time:.6f}s")
print(f"Comprehension is {loop_time/comp_time:.2f}x faster!")

print("\n=== All Solutions Complete! ===")
