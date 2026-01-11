# Solutions – File Handling

import os
import csv
import json
from pathlib import Path

# =============================================================================
# EASY LEVEL
# =============================================================================

# 1. Basic Write
print("=== 1. Basic Write ===")
filename = "my_info.txt"
with open(filename, "w") as f:
    f.write("Alice\n")
    f.write("25\n")
print(f"Created {filename}")

# 2. Basic Read
print("\n=== 2. Basic Read ===")
with open(filename, "r") as f:
    for line in f:
        print(line.strip())

# 3. Append Mode
print("\n=== 3. Append Mode ===")
with open(filename, "a") as f:
    f.write("I love Python!\n")

with open(filename, "r") as f:
    print("Updated content:", f.read())

# 4. Line Counting
print("\n=== 4. Line Counting ===")
poem_file = "poem.txt"
poem_content = """Rose is red,
Violet is blue,
Python is sweet,
And so are you.
Coding is fun!"""
with open(poem_file, "w") as f:
    f.write(poem_content)

count = 0
with open(poem_file, "r") as f:
    for line in f:
        count += 1
print(f"Lines in poem: {count}")

# 5. List to File
print("\n=== 5. List to File ===")
colors = ["Red", "Green", "Blue"]
with open("colors.txt", "w") as f:
    # Adding newline to each color
    f.writelines(c + "\n" for c in colors)
print("Colors saved.")

# =============================================================================
# MEDIUM LEVEL
# =============================================================================

# 6. Copy File
print("\n=== 6. Copy File ===")
def copy_file(src, dst):
    with open(src, "r") as f_src:
        content = f_src.read()
    with open(dst, "w") as f_dst:
        f_dst.write(content)
    print(f"Copied {src} to {dst}")

copy_file("poem.txt", "poem_copy.txt")

# 7. File Statistics
print("\n=== 7. File Stats ===")
def file_stats(fname):
    with open(fname, "r") as f:
        content = f.read()
        lines = content.split('\n') # Or splitlines()
        words = content.split()
    print(f"Chars: {len(content)}")
    print(f"Words: {len(words)}")
    print(f"Lines: {len(lines)}")

file_stats("poem.txt")

# 8. Find and Replace
print("\n=== 8. Find and Replace ===")
with open("bad_review.txt", "w") as f:
    f.write("This is a bad movie. Really bad.")

with open("bad_review.txt", "r") as f:
    text = f.read()

new_text = text.replace("bad", "good")

with open("good_review.txt", "w") as f:
    f.write(new_text)
print("Review fixed!")

# 9. Safe Open
print("\n=== 9. Safe Open ===")
def read_safe(fname):
    try:
        with open(fname, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: {fname} not found.")

read_safe("ghost_file.txt")

# 10. CSV Writer
print("\n=== 10. CSV Writer ===")
with open("students.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Grade"])
    writer.writerow(["John", "A"])
    writer.writerow(["Doe", "B"])
    writer.writerow(["Smith", "A"])
print("CSV written.")

# 11. Log Parser
print("\n=== 11. Log Parser ===")
# Create dummy log
with open("server.log", "w") as f:
    f.write("INFO: Started\nERROR: DB Fail\nINFO: Running\nERROR: Timeout\n")

print("Errors found:")
with open("server.log", "r") as f:
    for line in f:
        if line.startswith("ERROR"):
            print(line.strip())

# =============================================================================
# HARD LEVEL
# =============================================================================

# 12. Binary Copy
print("\n=== 12. Binary Copy ===")
# Generate a dummy binary file
with open("test.bin", "wb") as f:
    f.write(b'\x00\xFF\xAA\xBB')

# Copy it
with open("test.bin", "rb") as source:
    data = source.read()
    with open("test_copy.bin", "wb") as dest:
        dest.write(data)
print("Binary data copied.")

# 13. JSON Config
print("\n=== 13. JSON Config ===")
settings = {"volume": 80, "difficulty": "hard", "dark_mode": True}

with open("settings.json", "w") as f:
    json.dump(settings, f, indent=4)

with open("settings.json", "r") as f:
    loaded_settings = json.load(f)
    print(f"Loaded Volume: {loaded_settings['volume']}")

# 14. File Walker
print("\n=== 14. File Walker ===")
# Limit output to just a few
count = 0
for root, dirs, files in os.walk("."):
    for file in files:
        if count < 3:
            # print(os.path.join(root, file))
            count += 1
print("(File walking demo suppressed to keep output clean)")

# 15. Large File Chunk Reader
print("\n=== 15. Chunk Reader ===")
def read_in_chunks(file_obj, chunk_size=10): # Small chunk for demo
    while True:
        data = file_obj.read(chunk_size)
        if not data:
            break
        yield data

with open("poem.txt", "r") as f:
    for i, chunk in enumerate(read_in_chunks(f, chunk_size=10)):
        print(f"Chunk {i}: {repr(chunk)}")

# 16. Context Manager Class
print("\n=== 16. Custom Context Manager ===")
class LogWriter:
    def __init__(self, fname):
        self.fname = fname
        
    def __enter__(self):
        self.file = open(self.fname, 'w')
        self.file.write("--- Start Logging ---\n")
        return self.file
    
    def __exit__(self, exc_type, exc_val, tb):
        self.file.write("--- End Logging ---\n")
        self.file.close()

with LogWriter("session.log") as log:
    log.write("User logged in.\n")
    log.write("Action performed.\n")
print("Session log created.")

# 17. Multi-File Search
print("\n=== 17. Multi-File Search ===")
def search_files(word, files):
    for fname in files:
        if not os.path.exists(fname): continue
        with open(fname, "r") as f:
            for line_no, line in enumerate(f, 1):
                if word in line:
                    print(f"Found '{word}' in {fname}:{line_no}")

search_files("Python", ["my_info.txt", "poem.txt", "colors.txt"])

# 18. Seek Reverse
print("\n=== 18. Read Last chars ===")
with open("poem.txt", "br") as f: # Binary mode needed for seeking from end in some OS
    f.seek(-10, 2) # 2 means SEEK_END
    last_10 = f.read()
    print(f"Last 10 bytes: {last_10}")

# =============================================================================
# BONUS
# =============================================================================

# 19. CSV to JSON
print("\n=== 19. CSV to JSON ===")
csv_data = []
if os.path.exists("students.csv"):
    with open("students.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_data.append(row)
    
    with open("students.json", "w") as f:
        json.dump(csv_data, f, indent=4)
    print("Converted CSV to JSON.")

# 20. Atomic Write (Concept)
print("\n=== 20. Atomic Write ===")
def write_atomic(fname, content):
    temp_name = fname + ".tmp"
    with open(temp_name, "w") as f:
        f.write(content)
    # This replace operation is atomic on POSIX
    os.replace(temp_name, fname)
    print(f"Atomically wrote to {fname}")

write_atomic("atomic.txt", "Important Data")

# 21. Directory Cleaner
print("\n=== 21. Directory Cleaner ===")
# Danger zone! Code commented out for safety in demo script.
# for file in os.listdir("."):
#     if file.endswith(".tmp"):
#         os.remove(file)
print("Cleaner function ready (commented out for safety).")
