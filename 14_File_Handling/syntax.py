# Basic File I/O Syntax

# Writing
with open("test.txt", "w") as f:
    f.write("Hello\nWorld")

# Reading
with open("test.txt", "r") as f:
    content = f.read()
    print(content)

# Appending
with open("test.txt", "a") as f:
    f.write("\nAppended")

# Line by line
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())
