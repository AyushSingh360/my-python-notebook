# Solutions – Strings

import re

print("--- Solutions: Strings ---")

# ----------------- EASY -----------------
print("\n--- Easy ---\n")

# 1. Basic String Methods
name = "  aLiCe  "
clean_name = name.strip().title()
print(f"1. Name: '{clean_name}'")

# 2. Substring Search
sentence = "The quick brown fox jumps over the lazy dog"
has_fox = "fox" in sentence
print(f"2. Contains 'fox': {has_fox}")

# 3. String Concatenation
part1 = "Python"
part2 = "is"
part3 = "Fun"
parts = [part1, part2, part3]
joined = "-".join(parts)
print(f"3. Joined: {joined}")

# 4. Counting Characters
text = "Experience is the best teacher"
count_e = text.count("e")
print(f"4. Count of 'e': {count_e}")


# ----------------- MEDIUM -----------------
print("\n--- Medium ---\n")

# 5. Domain Extractor
email = "user.name+tag@company.co.uk"
# Split by '@', take the second part (index 1)
domain = email.split("@")[1]
print(f"5. Domain: {domain}")

# 6. Caesar Cipher (Simple)
def caesar_cipher_simple(text, shift=1):
    result = ""
    for char in text:
        # Simple shift, doesn't wrap z->a for simplicity in Medium task
        # Correct approach uses ord() and chr() with modulo
        new_ord = ord(char) + shift
        result += chr(new_ord)
    return result
# Better implementation handling wrapping:
def caesar_cipher_better(text, shift=1):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            # (char_code - base + shift) % 26 + base
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

print(f"6. Cipher ('abc', 1): {caesar_cipher_better('abc', 1)}")

# 7. Formatted Receipt
item = "Laptop"
price = 999.99
qty = 2
total = price * qty
# :>10 aligns right, width 10. :,.2f adds commas and 2 decimals.
receipt = f"Item: {item:<10} | Qty: {qty} | Total: ${total:,.2f}"
print(f"7. {receipt}")

# 8. Palindrome Checker
s = "No 'x' in Nixon"
# Remove special chars and lowercase
cleaned = ''.join(c for c in s if c.isalnum()).lower()
is_pal = cleaned == cleaned[::-1]
print(f"8. '{s}' is palindrome: {is_pal}")


# ----------------- HARD -----------------
print("\n--- Hard ---\n")

# 9. Anagram Checker
w1 = "Listen"
w2 = "Silent"
# Sort characters and compare
is_anagram = sorted(w1.lower()) == sorted(w2.lower())
print(f"9. '{w1}' & '{w2}' Anagram: {is_anagram}")

# 10. Manual Split
def my_split(text, delimiter):
    result = []
    current_word = ""
    for char in text:
        if char == delimiter:
            result.append(current_word)
            current_word = ""
        else:
            current_word += char
    result.append(current_word) # Add last word
    return result

test_str = "one,two,three"
print(f"10. Manual Split: {my_split(test_str, ',')}")

# 11. Password Validator
pwd = "Password1"
is_valid = (
    len(pwd) >= 8 and
    any(c.isupper() for c in pwd) and
    any(c.islower() for c in pwd) and
    any(c.isdigit() for c in pwd)
)
print(f"11. Password '{pwd}' valid: {is_valid}")


# ----------------- EXPERT -----------------
print("\n--- Expert ---\n")

# 12. Regex Email Scraper
text_emails = "Contact support@example.com or sales@example.org for assistance."
# Pattern: \S matches non-whitespace
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text_emails)
print(f"12. Emails found: {emails}")

# 13. Date Normalizer (MM/DD/YYYY -> YYYY-MM-DD)
text_dates = "Meeting on 12/31/2023 and 01/15/2024."
# Capture groups: (\d{2})/(\d{2})/(\d{4}) -> Group 1, 2, 3
normalized = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', text_dates)
print(f"13. Original: {text_dates}")
print(f"    Fixed:    {normalized}")

# 14. Text Justification (Simple Wrap)
def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_len = 0
    
    for word in words:
        # Check if adding word exceeds width (len(word) + spaces)
        if current_len + len(word) + len(current_line) > width:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_len = len(word)
        else:
            current_line.append(word)
            current_len += len(word)
    lines.append(" ".join(current_line)) # Last line
    return "\n".join(lines)

long_text = "This is a long sentence that needs wrapping to fit."
print(f"14. Wrapped (width=10):\n{justify_text(long_text, 10)}")
