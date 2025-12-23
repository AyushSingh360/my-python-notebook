# Examples confirming file operations

# 1. Write CSV-like data
data = ["Name,Score", "Alice,10", "Bob,20"]
with open("scores.csv", "w") as f:
    f.write("\n".join(data))

# 2. Read lines into list
with open("scores.csv", "r") as f:
    lines = f.readlines()
print(lines)

# 3. Binary write/read
with open("data.bin", "wb") as f:
    f.write(b'\x00\x01\x02')
with open("data.bin", "rb") as f:
    print(f.read())

# 4. Safe open (handle missing file)
try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
