# Solutions – OOP

# 1. Car
class Car:
    def __init__(self, mk, md, yr): self.mk, self.md, self.yr = mk, md, yr
    def desc(self): return f"{self.yr} {self.mk} {self.md}"
print(Car("Toyota", "Camry", 2022).desc())

# 2. Circle
class Circle:
    pi = 3.14
    def area(self, r): return self.pi * r * r
print(Circle().area(5))

# 3. ID
print(id(object()), id(object()))

# 4. Animal
class Animal:
    def speak(self): pass
class Dog(Animal):
    def speak(self): return "Woof"
print(Dog().speak())

# 5. Stack
class Stack:
    def __init__(self): self.s = []
    def push(self, x): self.s.append(x)
    def pop(self): return self.s.pop() if self.s else None
    def peek(self): return self.s[-1] if self.s else None
s = Stack(); s.push(1); print(s.pop())

# 6. Student
class Student:
    def __init__(self): self.__g = 0
    def set(self, g): 
        if 0<=g<=100: self.__g = g
    def get(self): return self.__g
st = Student(); st.set(90); print(st.get())

# 7. ABC
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def speed(self): pass
class Bike(Vehicle):
    def speed(self): return 30
print(Bike().speed())

# 8. Poly Area
class Rect:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
def total_area(shapes): return sum(s.area() for s in shapes)
print(total_area([Rect(2,3), Rect(5,5)]))

# 9. Multiple Inh
class Fly: 
    def fly(self): return "Fly"
class Swim:
    def swim(self): return "Swim"
class Duck(Fly, Swim): pass
print(Duck().fly())

# 10. Singleton
class Singleton(type):
    _inst = {}
    def __call__(cls, *args, **kw):
        if cls not in cls._inst:
            cls._inst[cls] = super().__call__(*args, **kw)
        return cls._inst[cls]
class Log(metaclass=Singleton): pass
print(Log() is Log())
