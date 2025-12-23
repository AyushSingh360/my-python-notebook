# Basic dictionary syntax examples
person = {"name": "Bob", "age": 28}
print(person["name"])
# Adding / updating
person["city"] = "London"
person["age"] = 29
# Deleting
del person["city"]
# Using get
print(person.get("salary", 0))
# Dictionary comprehension
squares = {x: x*x for x in range(5)}
print(squares)
