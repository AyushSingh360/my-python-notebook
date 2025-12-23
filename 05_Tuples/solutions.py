# Solutions – Tuples

# 1. Tuple with three types
t = (42, "answer", 3.14)
print(t[0], t[1], t[2])

# 2. Sum and product
def sum_prod(a, b):
    return (a + b, a * b)
s, p = sum_prod(4, 5)
print(s, p)  # 9 20

# 3. Last element via negative index
t = (10, 20, 30)
print(t[-1])  # 30

# 4. Detect duplicates in tuple
def has_duplicates(seq):
    return len(set(seq)) != len(seq)
lst = [1,2,3,2]
tpl = tuple(lst)
print(has_duplicates(tpl))  # True

# 5. Unpack date tuple
date = (2025, 12, 23)
year, month, day = date
print(year, month, day)

# 6. Tuple as dict key
coord_city = {}
coord_city[(40.0, -74.0)] = "NYC"
print(coord_city[(40.0, -74.0)])

# 7. zip_longest_tuple
def zip_longest_tuple(*iterables, fillvalue=None):
    max_len = max(len(it) for it in iterables)
    result = []
    for i in range(max_len):
        group = tuple(
            it[i] if i < len(it) else fillvalue
            for it in iterables
        )
        result.append(group)
    return tuple(result)
print(zip_longest_tuple([1,2], [3,4,5], fillvalue=0))

# 8. Flatten nested tuple
def flatten(tpl):
    flat = ()
    for item in tpl:
        if isinstance(item, tuple):
            flat += flatten(item)
        else:
            flat += (item,)
    return flat
nested = ((1, (2, 3)), (4, (5, (6,))))
print(flatten(nested))  # (1, 2, 3, 4, 5, 6)

# 9. Generator expression for squares (converted to tuple)
squares = tuple(x*x for x in range(10))
print(squares)

# 10. Immutable stack using tuples
class ImmutableStack:
    __slots__ = ("_data",)
    def __init__(self, data=()):
        self._data = data
    def push(self, item):
        return ImmutableStack(self._data + (item,))
    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data[-1], ImmutableStack(self._data[:-1])
    def peek(self):
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]
    def __repr__(self):
        return f"ImmutableStack{self._data}"

stack = ImmutableStack()
stack = stack.push(10).push(20)
top, stack = stack.pop()
print(top, stack)  # 20 ImmutableStack(10,)
