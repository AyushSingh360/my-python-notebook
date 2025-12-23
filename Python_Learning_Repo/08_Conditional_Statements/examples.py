# Examples demonstrating conditional logic

# 1. Login simulation
user = input("User: ")
password = input("Pass: ")
if user == "admin" and password == "secret":
    print("Granted")
elif user == "admin":
    print("Wrong password")
else:
    print("Unknown user")

# 2. Temperature advice
temp = float(input("Temp: "))
if temp < 0:
    print("Freezing")
elif temp < 20:
    print("Cold")
elif temp < 30:
    print("Nice")
else:
    print("Hot")

# 3. Simple calculator logic
op = input("Op (+-*/): ")
a, b = 10, 5
if op == "+": print(a + b)
elif op == "-": print(a - b)
elif op == "*": print(a * b)
elif op == "/": print(a / b)
else: print("Invalid op")
