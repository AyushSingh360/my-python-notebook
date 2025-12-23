# Solutions – File Handling

# 1, 2, 3 Basic I/O
with open("hello.txt", "w") as f: f.write("Hello World\n")
with open("hello.txt", "r") as f: print(f.read())
with open("hello.txt", "a") as f: f.write("Goodbye\n")

# 4, 5 CSV salary
data="id,name,salary\n1,A,1000\n2,B,2000\n3,C,3000"
with open("employees.csv", "w") as f: f.write(data)
total=0; count=0
with open("employees.csv", "r") as f:
    next(f) # skip header
    for line in f:
        p = line.strip().split(",")
        total+=int(p[2]); count+=1
print(total/count)

# 6. Read head
def read_head(p, n=5):
    with open(p) as f:
        return [f.readline().strip() for _ in range(n)]
print(read_head("employees.csv", 2))

# 7. SafeOpen
class SafeOpen:
    def __init__(self, p, m): self.p, self.m = p, m
    def __enter__(self): 
        print(f"Opening {self.p}"); self.f=open(self.p, self.m); return self.f
    def __exit__(self, *a): 
        print("Closing"); self.f.close()
with SafeOpen("hello.txt", "r") as f: pass

# 8. Binary Copy
def copy_bin(src, dst):
    with open(src, "rb") as s, open(dst, "wb") as d:
        while True:
            b = s.read(1024)
            if not b: break
            d.write(b)
# copy_bin("bin1", "bin2")

# 9. Rotate log
import os
def log(msg, i=0):
    fn = f"log_{i}.txt"
    if os.path.exists(fn) and os.path.getsize(fn)>1024:
        log(msg, i+1)
    else:
        with open(fn, "a") as f: f.write(msg)
log("test")

# 10. Freq
def freq(p):
    c={}
    with open(p) as f:
        for l in f:
            for w in l.split():
                c[w]=c.get(w,0)+1
    return c
# print(freq("hello.txt"))
