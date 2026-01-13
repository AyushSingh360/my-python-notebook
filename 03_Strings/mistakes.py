# Common Mistakes – Strings

"""
This file demonstrates common errors beginners make with strings.
Each section shows the WRONG way, explains WHY it's wrong, and shows the RIGHT way.
"""

def print_mistake(title):
    print(f"\n❌ Mistake: {title}")

def print_fix(title):
    print(f"✅ Fix: {title}")

# ---------------------------------------------------------
# 1. String Immutability
# ---------------------------------------------------------
print_mistake("Trying to modify a string in place")
s = "Hello"
try:
    # s[0] = "M" 
    print("Code: s[0] = 'M'")
    print("Error: TypeError: 'str' object does not support item assignment")
except TypeError as e:
    print(e)

print_fix("Create a new string")
s = "M" + s[1:]
print(f"New string: {s}")


# ---------------------------------------------------------
# 2. Join Syntax Confusion
# ---------------------------------------------------------
print_mistake("Calling .join() on the list instead of the separator")
words = ["Python", "is", "cool"]
try:
    # result = words.join(" ")
    print("Code: words.join(' ')")
    print("Error: AttributeError: 'list' object has no attribute 'join'")
except AttributeError as e:
    print(e)

print_fix("Call .join() on the string separator")
result = " ".join(words)
print(f"Result: '{result}'")


# ---------------------------------------------------------
# 3. Strip Misunderstanding
# ---------------------------------------------------------
print_mistake("Thinking strip() removes words, not characters")
text = "banana shake"
# User wants to remove "banana"
clean = text.strip("banana")
print(f"Original: '{text}'")
print(f"Code: text.strip('banana') -> Result: '{clean}'")
print("Explanation: strip() removes characters from the ENDS, not substring.")

print_fix("Use replace() or slicing")
real_clean = text.replace("banana", "").strip()
print(f"Result: '{real_clean}'")


# ---------------------------------------------------------
# 4. f-string Common Errors
# ---------------------------------------------------------
print_mistake("Forgetting the 'f' prefix")
name = "Alice"
# User forgets 'f'
msg = "Hello {name}"
print(f"Code: \"Hello {{name}}\" -> Result: '{msg}'")

print_fix("Add 'f' before the quote")
msg = f"Hello {name}"
print(f"Result: '{msg}'")


# ---------------------------------------------------------
# 5. Comparing Strings with Numbers
# ---------------------------------------------------------
print_mistake("Comparing string digit with integer")
age_input = "25"
age_limit = 25
print(f"Code: '25' == 25 -> Result: {age_input == age_limit}")

print_fix("Convert types before comparison")
print(f"Code: int('25') == 25 -> Result: {int(age_input) == age_limit}")
