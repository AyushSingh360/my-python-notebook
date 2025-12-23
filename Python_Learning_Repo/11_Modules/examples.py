# Examples demonstrating modules

# 1. Standard library usage
import math
print("Pi:", math.pi)

# 2. Creating a dummy module usage (simulated)
# Imagine a file named 'utils.py' with:
# def add(a, b): return a + b

# import utils
# print(utils.add(5, 3))

# 3. If name == main guard
def main_logic():
    print("This runs only if executed directly.")

if __name__ == "__main__":
    main_logic()
