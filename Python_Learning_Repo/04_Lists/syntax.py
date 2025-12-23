# Basic list syntax examples
my_list = []                # empty list
my_list.append(1)           # [1]
my_list.extend([2,3])        # [1,2,3]
my_list.insert(0, 0)        # [0,1,2,3]
print(my_list)
# Access and slice
print(my_list[0])          # first element
print(my_list[1:3])        # slice
# List comprehension
squares = [x*x for x in range(5)]
print(squares)
