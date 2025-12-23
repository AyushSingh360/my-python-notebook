# Solutions – Data Types & Operators

# 1. Add two integers
x = 5
y = 8
print(x + y)  # 13

# 2. Concatenate strings
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Hello World

# 3. Divisible by 3
n = int(input("Number: "))
print(n % 3 == 0)

# 4. Swap without temp
a = 10
b = 20
a, b = b, a
print(a, b)  # 20 10

# 5. Sum of even numbers in list
nums = [1, 2, 3, 4, 5, 6]
print(sum(x for x in nums if x % 2 == 0))  # 12

# 6. Alphabet dictionary a‑e
alpha = {chr(i+96): i for i in range(1,6)}
print(alpha)  # {'a':1,'b':2,'c':3,'d':4,'e':5}

# 7. Simple string calculator
expr = input("Expr (e.g., 12*4): ")
for op in '+-*/':
    if op in expr:
        left, right = expr.split(op)
        left, right = int(left), int(right)
        if op == '+': res = left + right
        elif op == '-': res = left - right
        elif op == '*': res = left * right
        else: res = left / right
        print(res)
        break

# 8. Prime test
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(17))

# 9. Unique word count
line = input("Sentence: ")
print(len(set(line.lower().split())))

# 10. Power of two (bitwise)
def is_power_of_two(x):
    return x > 0 and (x & (x-1)) == 0
print(is_power_of_two(16))
