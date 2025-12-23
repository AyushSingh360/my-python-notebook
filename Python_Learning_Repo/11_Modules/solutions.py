# Solutions – Modules

# 1. Constants
# constants.py: PI = 3.14
# main.py:
# from constants import PI
# print(PI)

# 2. Greetings
# greetings.py: def morning(n): return f"Hi {n}"
# main.py:
# import greetings
# print(greetings.morning("Alice"))

# 3. Random
import random
print(random.randint(1, 100))

# 4. Package 'calc'
# calc/__init__.py (empty)
# calc/add.py: def add(a,b): return a+b
# main.py: from calc.add import add

# 5. Counter class
# counter.py: class Counter: ...
# main.py: from counter import Counter

# 6. __main__
# if __name__ == "__main__": print("Direct exec")

# 7. Lazy load
def heavy():
    import json
    return json.dumps({"a":1})
print(heavy())

# 8. Plugin loader (simplified)
import importlib, os
# for f in os.listdir("plugins"): 
#     if f.endswith(".py"): importlib.import_module(f"plugins.{f[:-3]}")

# 9. Relative
# from . import sibling

# 10. Timing
import time
t0 = time.time(); import json; print(time.time()-t0)
