# Solutions – Strings

# 1. Print phrase using two variables
part1 = "Data"
part2 = "Science"
print(part1 + " " + part2)

# 2. Length of a string
s = input("Enter text: ")
print(len(s))

# 3. Uppercase conversion
word = input("Word: ")
print(word.upper())

# 4. Reverse without slicing
def rev(txt):
    out = ""
    for ch in txt:
        out = ch + out
    return out
print(rev("hello"))

# 5. Extract domain from email
email = input("Email: ")
print(email.split("@")[1])

# 6. Formatted report line
name = "Alice"
score = 92.5
print(f"Name: {name}, Score: {score}")

# 7. Caesar cipher (shift 3)
def caesar(txt, shift=3):
    res = ""
    for ch in txt:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            res += chr((ord(ch)-base+shift)%26 + base)
        else:
            res += ch
    return res
print(caesar("abc XYZ"))

# 8. Vowel count
para = input("Paragraph: ").lower()
vowels = "aeiou"
counts = {v: para.count(v) for v in vowels}
print(counts)

# 9. Identifier validation
import keyword
def is_identifier(s):
    return s.isidentifier() and not keyword.iskeyword(s)
print(is_identifier("my_var"))

# 10. Palindrome check ignoring non‑alphanum
import re

def is_palindrome(s):
    cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))
