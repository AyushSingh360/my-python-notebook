"""
Comprehensive Guide to Data Types and Operators in Python.
This script demonstrates the core building blocks of Python programming with detailed examples.
"""

def print_section(title):
    print(f"\n{'=' * 50}")
    print(f" {title.upper()}")
    print(f"{'=' * 50}")

# ---------------------------------------------------------
# 1. NUMERIC TYPES
# ---------------------------------------------------------
print_section("1. Numeric Types")

# Integers (int)
# Integers have arbitrary precision in Python 3.
print("--- Integers ---")
a = 10
b = -5
large_num = 1_000_000_000  # Using underscores for readability
print(f"a: {a}, type: {type(a)}")
print(f"Large number: {large_num}")

# Floats (float)
# Floats are approximations of real numbers (IEEE 754 double precision).
print("\n--- Floats ---")
x = 3.14159
y = 2.5e-3  # Scientific notation: 2.5 * 10^-3 = 0.0025
print(f"x: {x}, type: {type(x)}")
print(f"y: {y}")
# Precision warning
print(f"Precision issue (0.1 + 0.2): {0.1 + 0.2}")  # Often prints 0.30000000000000004

# Complex Numbers (complex)
# Built-in support for complex numbers (real + imag part).
print("\n--- Complex Numbers ---")
c = 3 + 4j
print(f"Complex number: {c}")
print(f"Real part: {c.real}, Imaginary part: {c.imag}")
print(f"Conjugate: {c.conjugate()}")


# ---------------------------------------------------------
# 2. BOOLEANS
# ---------------------------------------------------------
print_section("2. Booleans")
# subclass of int. True == 1, False == 0.
is_python_fun = True
is_tired = False
print(f"is_python_fun: {is_python_fun}, type: {type(is_python_fun)}")
print(f"True as int: {int(True)}, False as int: {int(False)}")


# ---------------------------------------------------------
# 3. STRINGS
# ---------------------------------------------------------
print_section("3. Strings")
# Strings are immutable sequences of Unicode characters.

# Quotes
s1 = 'Single quotes'
s2 = "Double quotes"
s3 = '''Triple quotes
can span multiple
lines.'''
print(s3)

# String Operations
full_name = "Alice" + " " + "Wonderland"
print(f"Concatenation: {full_name}")
print(f"Repetition ('Hip ' * 2): {'Hip ' * 2}Hooray")

# Useful Methods
text = "  Python Programming  "
print(f"Original: '{text}'")
print(f"Stripped: '{text.strip()}'")
print(f"Lower: '{text.lower()}'")
print(f"Upper: '{text.upper()}'")
print(f"Replace: '{text.strip().replace('Python', 'Advanced Python')}'")
print(f"Split: {text.split()}")


# ---------------------------------------------------------
# 4. OPERATORS
# ---------------------------------------------------------
print_section("4. Operators")

a, b = 10, 3

# Arithmetic
print("--- Arithmetic ---")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b} (True Division)")
print(f"{a} // {b} = {a // b} (Floor Division)")
print(f"{a} % {b} = {a % b} (Modulus/Remainder)")
print(f"{a} ** {b} = {a ** b} (Exponentiation)")

# Comparison
print("\n--- Comparison ---")
print(f"{a} > {b}: {a > b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
# Chained comparison
x = 5
print(f"1 < {x} < 10: {1 < x < 10}")

# Logical
print("\n--- Logical ---")
t, f = True, False
print(f"True and False: {t and f}")
print(f"True or False: {t or f}")
print(f"not True: {not t}")
# Short-circuit evaluation
print(f"False and (1/0): {False and (1/0)}")  # Safe, because (1/0) is never evaluated

# Bitwise
print("\n--- Bitwise ---")
# 10 is 1010 in binary, 3 is 0011
print(f"{a} & {b} (AND): {a & b} (Binary: 0010 -> 2)")
print(f"{a} | {b} (OR) : {a | b} (Binary: 1011 -> 11)")
print(f"{a} ^ {b} (XOR): {a ^ b} (Binary: 1001 -> 9)")
print(f"~{a} (NOT): {~a} (-(a+1) -> -11)")
print(f"{a} << 1 (Left Shift): {a << 1} (Binary: 10100 -> 20)")

# Assignment
print("\n--- Assignment ---")
count = 5
count += 2  # Same as count = count + 2
print(f"count after += 2: {count}")

# Identity (is) vs Equality (==)
print("\n--- Identity vs Equality ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 == list2: {list1 == list2} (Values are equal)")
print(f"list1 is list2: {list1 is list2} (Memory addresses differ)")
print(f"list1 is list3: {list1 is list3} (Same object)")

# Membership
print("\n--- Membership ---")
print(f"'P' in 'Python': {'P' in 'Python'}")
print(f"10 not in list1: {10 not in list1}")


# ---------------------------------------------------------
# 5. TYPE CONVERSION
# ---------------------------------------------------------
print_section("5. Type Conversion")

# Implicit
num_int = 123
num_float = 1.23
new_num = num_int + num_float
print(f"Implicit (int + float): {new_num}, type: {type(new_num)}")

# Explicit
print(f"int(3.99): {int(3.99)} (Truncates, doesn't round)")
print(f"str(100): '{str(100)}'")
print(f"float('4.5'): {float('4.5')}")
print(f"bool(0): {bool(0)}, bool(42): {bool(42)}")
