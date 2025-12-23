# Solutions – Advanced

# 1. Cubes
print([x**3 for x in range(10)])

# 2. Lambda max
mx = lambda a,b: a if a>b else b
print(mx(10, 20))

# 3. KeyError
try: d={}; print(d['a'])
except KeyError: print("Missing")

# 4. Freq dict
s="abracadabra"
print({c: s.count(c) for c in set(s)})

# 5. Generator evens
def evens(n):
    for i in range(0, n+1, 2): yield i
print(list(evens(6)))

# 6. InvalidAge
class InvAge(Exception): pass
try: raise InvAge("Bad age")
except InvAge as e: print(e)

# 7. Retry
def retry(n):
    def dec(f):
        def wrap(*a, **k):
            for i in range(n):
                try: return f(*a, **k)
                except: pass
        return wrap
    return dec

# 8. Reduce fact
from functools import reduce
print(reduce(lambda x,y: x*y, range(1,6)))

# 9. Prime Gen
class Primes:
    def __iter__(self):
        self.c = 2
        return self
    def __next__(self):
        # simplified infinite prime gen logic
        while True:
            for i in range(2, int(self.c**0.5)+1):
                if self.c%i==0: break
            else:
                p = self.c; self.c+=1; return p
            self.c+=1
p = Primes()
# print(next(p))

# 10. Map/Filter
strs = ["hi", "code", "py"]
print([s.upper() for s in strs if len(s)>3])
