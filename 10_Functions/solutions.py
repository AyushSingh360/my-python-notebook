# Solutions – Functions

import math
import time
from functools import wraps

# 1. is_even
def is_even(n): return n % 2 == 0
print(is_even(4))

# 2. area_circle
def area_circle(r): return math.pi * r * r
print(area_circle(3))

# 3. say_hello
def say_hello(): print("Hello!")
say_hello()

# 4. max_of_three
def max_of_three(a, b, c): return max(a, b, c)
print(max_of_three(1, 9, 5))

# 5. count_vowels
def count_vowels(s): return sum(1 for c in s.lower() if c in "aeiou")
print(count_vowels("Hello"))

# 6. apply_twice
def apply_twice(f, x): return f(f(x))
print(apply_twice(lambda x: x+1, 5))

# 7. Recursive flatten
def flatten(lst):
    flat = []
    for i in lst:
        if isinstance(i, list): flat.extend(flatten(i))
        else: flat.append(i)
    return flat
print(flatten([1, [2, [3]], 4]))

# 8. timer decorator
def timer(f):
    @wraps(f)
    def wrapper(*args, **kw):
        t0 = time.time()
        res = f(*args, **kw)
        print(f"{f.__name__} took {time.time()-t0:.4f}s")
        return res
    return wrapper

@timer
def heavy(): time.sleep(0.1)
heavy()

# 9. Group by first letter
def group_by_first_letter(words):
    d = {}
    for w in words:
        key = w[0].lower()
        d.setdefault(key, []).append(w)
    return d
print(group_by_first_letter(["Apple", "Banana", "apricot"]))

# 10. Command dispatcher
cmds = {"add": lambda a,b: a+b, "sub": lambda a,b: a-b}
def run(cmd, *args):
    return cmds[cmd](*args) if cmd in cmds else "Unknown"
print(run("add", 2, 3))
