# Solutions – Conditional Statements

# 1. Even/Odd
n = int(input("N: "))
print("Even" if n % 2 == 0 else "Odd")

# 2. Age
age = int(input("Age: "))
print("Minor" if age < 18 else "Adult")

# 3. Vowel
ch = input("Char: ").lower()
print("Vowel" if ch in "aeiou" else "Consonant")

# 4. Grading
score = float(input("Score: "))
if score >= 90: g = "A"
elif score >= 80: g = "B"
elif score >= 70: g = "C"
elif score >= 60: g = "D"
else: g = "F"
print(g)

# 5. Traffic light
c = input("Light: ").lower()
if c == "red": print("Stop")
elif c == "yellow": print("Caution")
elif c == "green": print("Go")
else: print("Invalid")

# 6. Flags
admin = True
active = True
perm = True
if admin and active and perm: print("Access granted")

# 7. Loan
age = 25; income = 30000; credit = 700
if age < 21: print("Too young")
elif income < 20000: print("Low income")
elif credit < 600: print("Bad credit")
else: print("Approved")

# 8. Categorize
x = int(input("Num: "))
sign = "pos" if x > 0 else "neg" if x < 0 else "zero"
abs_x = abs(x)
size = "small" if abs_x < 10 else "med" if abs_x <= 100 else "large"
print(f"{sign}, {size}")

# 9. Command parser
cmd = input("Cmd: ").split()
op = cmd[0] if cmd else ""
arg = cmd[1] if len(cmd)>1 else None
if op == "add" and arg: print(f"Adding {arg}")
elif op == "list": print("Listing")
else: print("Unknown or invalid")

# 10. RPS
import random
u = input("Choice: ")
c = random.choice(["rock", "paper", "scissors"])
if u == c: print("Draw")
elif (u=="rock" and c=="scissors") or (u=="paper" and c=="rock") or (u=="scissors" and c=="paper"):
    print("Win")
else:
    print("Lose")
