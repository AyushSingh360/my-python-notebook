# Basic module syntax

# In main.py
import math
print(math.sqrt(16))

# Specific import
from random import randint
print(randint(1, 10))

# Alias
import datetime as dt
now = dt.datetime.now()
print(now)

# Custom module usage assuming 'mymodule.py' exists
# import mymodule
# mymodule.greet()
