# Solutions – Loops

# 1. Countdown
i = 10
while i > 0:
    print(i)
    i -= 1

# 2. Factorial
f = 1
for n in range(1, 7): f *= n
print(f)

# 3. Char iteration
for c in "loop": print(c)

# 4. Fibonacci
n = int(input("n: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b
print()

# 5. Filter evens
nums = [1, 2, 3, 4]
evens = []
for x in nums:
    if x % 2 == 0: evens.append(x)
print(evens)

# 6. Menu
while True:
    c = input("Choice (0=exit): ")
    if c == "0": break
    print("You chose", c)

# 7. Guess number
import random
tgt = random.randint(1,100)
while True:
    g = int(input("Guess: "))
    if g == tgt:
        print("Win")
        break
    print("Lower" if g > tgt else "Higher")

# 8. Primes
primes = []
for n in range(2, 100):
    for d in range(2, int(n**0.5)+1):
        if n%d == 0: break
    else:
        primes.append(n)
print(primes)

# 9. Flatten
mat = [[1,2],[3,4]]
flat = []
for r in mat:
    for v in r:
        flat.append(v)
print(flat)

# 10. GCD
a, b = 48, 18
while b:
    a, b = b, a%b
print(a)
