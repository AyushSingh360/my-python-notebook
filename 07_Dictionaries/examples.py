# Examples demonstrating dictionary usage

# 1. Counting word frequencies
text = "hello world hello python"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)

# 2. Merging dictionaries
defaults = {"host": "localhost", "port": 8080}
override = {"port": 9090, "debug": True}
# Python 3.9+ syntax
config = defaults | override
print(config)

# 3. setdefault to group items
pairs = [("aa", 1), ("b", 2), ("aa", 3)]
grouped = {}
for key, val in pairs:
    grouped.setdefault(key, []).append(val)
print(grouped)

# 4. Nested dictionaries
data = {"user": {"id": 42, "name": "Alice"}}
print(data["user"]["name"])
