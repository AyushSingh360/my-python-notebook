# Solutions – Data Types & Operators

print("--- Solutions: Data Types & Operators ---")

# ----------------- EASY -----------------
print("\n--- Easy ---\n")

# 1. Basic Arithmetic
length = 10
width = 5
area = length * width
print(f"1. Area: {area}")

# 2. String Concatenation
first = "John"
last = "Doe"
print(f"2. Hello, {first} {last}!")

# 3. Type Checking
x = 10.5
print(f"3. Original Type: {type(x)}")
x_int = int(x)
print(f"   Converted Type: {type(x_int)}")

# 4. Modulus
num = 25
status = "Even" if num % 2 == 0 else "Odd"
print(f"4. {num} is {status}")


# ----------------- MEDIUM -----------------
print("\n--- Medium ---\n")

# 5. Fahrenheit to Celsius
f = 98.6
c = (f - 32) * 5/9
print(f"5. {f}F is {c:.1f}C")

# 6. String Slicing
text = "Python is awesome"
# "awesome" starts at index 10
target = text[10:]
print(f"6. {target.upper()}")

# 7. List Operations
colors = ['red', 'green', 'blue']
print(f"7. 'yellow' not in colors: {'yellow' not in colors}")

# 8. Dictionary Lookup
prices = {'apple': 0.5, 'banana': 0.3}
print(f"8. 'orange' in prices: {'orange' in prices}")


# ----------------- HARD -----------------
print("\n--- Hard ---\n")

# 9. Compound Interest
P = 1000
r = 0.05
n = 10
A = P * ((1 + r) ** n)
print(f"9. Compound Amount: {round(A, 2)}")

# 10. Bitwise Swap
a = 5   # 0101
b = 10  # 1010
print(f"10. Before: a={a}, b={b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"    After:  a={a}, b={b}")

# 11. Palindrome
s = "Racecar"
is_palindrome = s.lower() == s.lower()[::-1]
print(f"11. '{s}' is palindrome: {is_palindrome}")


# ----------------- EXPERT -----------------
print("\n--- Expert ---\n")

# 12. Floating Point Equality
val1 = 0.1 + 0.2
val2 = 0.3
is_equal = val1 == val2
tolerance = 1e-9
is_close = abs(val1 - val2) < tolerance
print(f"12. Strict Equality: {is_equal}")
print(f"    Close Enough: {is_close}")

# 13. Logical Short-Circuiting
# False and (1/0) -> False (Because False is encountered, 1/0 is NOT evaluated)
# True or (1/0)   -> True  (Because True is encountered, 1/0 is NOT evaluated)
print("13. Short-circuiting prevented crash!")
try:
    # This WOULD crash:
    # res = (1/0) or True
    pass
except ZeroDivisionError:
    print("Caught expected crash")

# 14. Complex Parsing
data_str = "Item:Apple,Price:0.50,Qty:10"
parsed_data = {}
for part in data_str.split(','):
    key, val = part.split(':')
    if key == 'Price':
        val = float(val)
    elif key == 'Qty':
        val = int(val)
    parsed_data[key] = val

print(f"14. Parsed: {parsed_data}")
