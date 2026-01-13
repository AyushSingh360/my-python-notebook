"""
Comprehensive Guide to Strings in Python.
Strings are immutable sequences of Unicode characters. This script demonstrates
creation, manipulation, formatting, and advanced operations.
"""

def print_section(title):
    print(f"\n{'=' * 50}")
    print(f" {title.upper()}")
    print(f"{'=' * 50}")

# ---------------------------------------------------------
# 1. STRING CREATION & ESCAPE SEQUENCES
# ---------------------------------------------------------
print_section("1. Creation & Escape Sequences")

s1 = 'Single quotes'
s2 = "Double quotes"
s3 = '''Triple quotes allow
multi-line strings.'''
print(s3)

# Escape Characters
print("\n--- Escape Characters ---")
print("Line 1\nLine 2 (\\n creates a new line)")
print("Col 1\tCol 2 (\\t creates a tab)")
print("She said, \"Python is awesome!\" (Escaped quotes)")

# Raw Strings (r"")
# Crucial for regex and Windows paths to ignore escape characters.
path = r"C:\Users\Name\Documents"
print(f"\nRaw String: {path}")


# ---------------------------------------------------------
# 2. SLICING & INDEXING
# ---------------------------------------------------------
print_section("2. Slicing & Indexing")

text = "Python Programming"
# Indexing (0-based)
print(f"First char: {text[0]}")
print(f"Last char:  {text[-1]}")

# Slicing [start:stop:step]
print(f"First word: '{text[:6]}'")       # 0 to 5
print(f"Last word:  '{text[7:]}'")       # 7 to end
print(f"Step by 2:  '{text[::2]}'")      # Every second char
print(f"Reverse:    '{text[::-1]}'")     # Reverse string


# ---------------------------------------------------------
# 3. STRING METHODS
# ---------------------------------------------------------
print_section("3. Common Methods")

s = "  Hello, Python World!  "

# Case Conversion
print(f"Original: '{s}'")
print(f"Strip:    '{s.strip()}' (Removes leading/trailing whitespace)")
print(f"Lower:    '{s.strip().lower()}'")
print(f"Upper:    '{s.strip().upper()}'")
print(f"Title:    '{s.strip().title()}'")

# Search & Replace
clean_s = s.strip()
print(f"\nStartswith 'Hello': {clean_s.startswith('Hello')}")
print(f"Endswith 'World!':  {clean_s.endswith('World!')}")
print(f"Find 'Python':      {clean_s.find('Python')} (Index found)")
print(f"Find 'Java':        {clean_s.find('Java')} (-1 if not found)")
print(f"Replace:            '{clean_s.replace('Python', 'Coding')}'")

# Validation
digit = "12345"
alpha = "abcDE"
print(f"\n'{digit}'.isdigit(): {digit.isdigit()}")
print(f"'{alpha}'.isalpha(): {alpha.isalpha()}")


# ---------------------------------------------------------
# 4. SPLITTING & JOINING
# ---------------------------------------------------------
print_section("4. Splitting & Joining")

# Split: String -> List
csv_line = "apple,banana,cherry,date"
fruits = csv_line.split(",")
print(f"Split results: {fruits}")

# Join: List -> String
# Syntax: separator.join(iterable)
joined = " | ".join(fruits)
print(f"Joined results: {joined}")


# ---------------------------------------------------------
# 5. STRING FORMATTING
# ---------------------------------------------------------
print_section("5. String Formatting")

name = "Alice"
score = 95.256

# 1. f-strings (Modern, Recommended)
print(f"f-string: Name={name}, Score={score}")
print(f"Rounding: Score={score:.2f}")            # 2 decimal places
print(f"Padding:  |{name:>10}|")                # Right align, width 10

# 2. .format() method (Older but still used)
print("format(): Name={}, Score={:.1f}".format(name, score))

# 3. % Operator (Legacy, C-style)
print("Percent:  Name=%s, Score=%.2f" % (name, score))


# ---------------------------------------------------------
# 6. ENCODING & DECODING
# ---------------------------------------------------------
print_section("6. Encoding (Bytes)")

# Strings are Unicode. Bytes are raw data (often for network/files).
u_str = "Café"
print(f"String: {u_str}, len: {len(u_str)}")

# Encode: String -> Bytes
b_str = u_str.encode("utf-8")
print(f"Encoded (utf-8): {b_str}, len: {len(b_str)} (Note 'é' takes 2 bytes)")

# Decode: Bytes -> String
decoded = b_str.decode("utf-8")
print(f"Decoded: {decoded}")
