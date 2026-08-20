# =====================================================================
# 1. Technique: Safe Lookups with .get() vs 'in'
# =====================================================================
# Reading `dict[key]` directly raises a KeyError if the key is missing.
# Use 'in' to check presence, or '.get()' to provide a fallback default.

user_scores = {"Alice": 95, "Bob": 88}

print("--- 1. Safe Lookups ---")
# Check presence explicitly
has_charlie = "Charlie" in user_scores

# Safe extraction with a fallback value (defaults to None if second arg omitted)
charlie_score = user_scores.get("Charlie", 0)

print(f"Is Charlie in dict? {has_charlie}")
print(f"Charlie's fallback score: {charlie_score}\n")


# =====================================================================
# 2. Technique: Frequency Counting Pattern (LeetCode Essential)
# =====================================================================
# Building a map of characters to their occurrence count.

text = "banana"
frequency_map = {}

print("--- 2. Frequency Counting ---")
for char in text:
    # If char is missing, .get(char, 0) returns 0. Then we add 1.
    frequency_map[char] = frequency_map.get(char, 0) + 1

print(f"Character frequencies: {frequency_map}\n")


# =====================================================================
# 3. Technique: Value Index Mapping
# =====================================================================
# Storing the array index of where an item was last seen. 
# This is the exact underpinning pattern for solving 'Two Sum'.

nums = [10, 20, 30, 40]
index_map = {}

print("--- 3. Index Mapping ---")
for index, val in enumerate(nums):
    index_map[val] = index

print(f"Value-to-Index Map: {index_map}\n")


# =====================================================================
# 4. Technique: High-Performance Dict Views
# =====================================================================
# .keys(), .values(), and .items() return dynamic memory-efficient view objects.
# They do not copy the dictionary data.

print("--- 4. Iteration Views ---")
# Unpacking key-value pairs directly in a loop
for name, score in user_scores.items():
    print(f"Key: {name} -> Value: {score}")
