# Exercises – Strings

"""
Completion Guide:
- Easy: Beginners (1-4)
- Medium: Intermediate (5-8)
- Hard: Advanced (9-11)
- Expert: Master (12-14)
"""

print("--- Exercises: Strings ---")

# ----------------- EASY -----------------
# 1. Basic String Methods
# Ask the user for their name (simulated as "  aLiCe  ").
# Print it stripped of whitespace and in Title Case.
# Expected: "Alice"

# 2. Substring Search
# Given the sentence "The quick brown fox jumps over the lazy dog".
# Check if the word "fox" is present using the `in` keyword.
# Expected: True

# 3. String Concatenation
# Create three variables: part1="Python", part2="is", part3="Fun".
# Join them with hyphens using the `.join()` method (hint: put them in a list first).
# Expected: "Python-is-Fun"

# 4. Counting Characters
# Count how many times the letter "e" appears in "Experience is the best teacher".
# Expected: 6


# ----------------- MEDIUM -----------------
# 5. Domain Extractor
# Given an email "user.name+tag@company.co.uk", extract the domain part ("company.co.uk").
# Do NOT use regex yet, just string methods like split or index.

# 6. Caesar Cipher (Simple)
# Create a function that shifts every letter in a string by a fixed number (e.g., 1).
# "abc" -> "bcd". Determine how to handle "z" -> "a" if you can, otherwise just simple shift.

# 7. Formatted Receipt
# Print a receipt line using f-strings.
# Item="Laptop", Price=999.99, Qty=2. Total should be calculated.
# Format: "Item: Laptop   | Qty: 2 | Total: $1,999.98" (Total with commas and 2 decimals)

# 8. Palindrome Checker
# Check if "No 'x' in Nixon" is a palindrome.
# Requirements: Ignore case, spaces, and punctuation.
# Expected: True


# ----------------- HARD -----------------
# 9. Anagram Checker
# Write a function to check if "Listen" and "Silent" are anagrams.
# (They contain the exact same characters with the same counts, case-insensitive).

# 10. Manual Split
# Write a function `my_split(text, delimiter)` that behaves like `text.split(delimiter)`
# WITHOUT using the built-in `.split()` method.
# Test with "one,two,three" and delimiter ",".

# 11. Password Validator
# Validate a password based on:
# - At least 8 chars
# - Contains at least one uppercase, one lowercase, and one digit.
# Hint: Use `any()` with string methods like `.isupper()`.


# ----------------- EXPERT -----------------
# 12. Regex Email Scraper
# Use the `re` module to extract all valid emails from a text.
# Text: "Contact support@example.com or sales@example.org for assistance."
# Expected: ['support@example.com', 'sales@example.org']

# 13. Date Normalizer
# Convert dates found in text from "MM/DD/YYYY" to "YYYY-MM-DD" using regex replacement.
# Text: "Meeting on 12/31/2023 and 01/15/2024."
# Expected: "Meeting on 2023-12-31 and 2024-01-15."

# 14. Text Justification
# Write a function that accepts a string and a width.
# It should wrap the text so no line exceeds the width, breaking at spaces.
# (Simple version of a text wrapper).
# Input: "This is a long sentence that needs wrapping.", width=10
# Output:
# This is a
# long
# sentence
# ...
