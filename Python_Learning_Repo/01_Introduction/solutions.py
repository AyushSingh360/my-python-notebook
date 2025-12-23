# Solutions – Introduction

# 1. Print a phrase
print("Python is fun!")

# 2. Age variable
age = 25
print(age)

# 3. Sum of two numbers
a = int(input("First: "))
b = int(input("Second: "))
print("Sum:", a + b)

# 4. Miles to kilometers
miles = float(input("Miles: "))
km = miles * 1.60934
print(f"{miles} miles = {km:.2f} km")

# 5. Even or odd
num = int(input("Number: "))
print("Even" if num % 2 == 0 else "Odd")

# 6. Mad‑libs
noun = input("Noun: ")
verb = input("Verb: ")
adj = input("Adjective: ")
print(f"The {adj} {noun} likes to {verb}.")

# 7. Mini‑menu
while True:
    print("\nMenu:\n1) Greet\n2) Add\n3) Exit")
    choice = input("Choice: ")
    if choice == "1":
        print("Hello!")
    elif choice == "2":
        x = int(input("x: "))
        y = int(input("y: "))
        print("Sum:", x + y)
    elif choice == "3":
        break
    else:
        print("Invalid")

# 8. Factorial
n = int(input("n: "))
fact = 1
for i in range(2, n + 1):
    fact *= i
print(f"{n}! = {fact}")

# 9. Guess the number
import random
target = random.randint(1, 100)
while True:
    guess = int(input("Guess: "))
    if guess == target:
        print("Correct!")
        break
    elif guess < target:
        print("Higher")
    else:
        print("Lower")

# 10. Vowel counter
text = input("Enter text: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print("Vowels:", count)
