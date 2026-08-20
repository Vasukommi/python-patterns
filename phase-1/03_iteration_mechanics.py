# =====================================================================
# 1. Technique: Position Tracking with enumerate()
# =====================================================================
# Problem: Beginners use tracking indexes manually: `i = 0` then `i += 1`.
# Solution: enumerate() returns an iterator of tuples containing (index, item).

ranks = ["Alpha", "Beta", "Gamma"]

print("--- 1. Enumerate Mechanics ---")
# You can customize the start index (e.g., start=1 instead of 0)
for index, code_name in enumerate(ranks, start=1):
    print(f"Rank #{index}: {code_name}")
print()


# =====================================================================
# 2. Technique: Parallel Stream Binding with zip()
# =====================================================================
# Problem: You need to iterate over two or more connected lists simultaneously.
# Solution: zip() pairs up elements on-demand without copying the structures.

users = ["Alice", "Bob", "Charlie"]
ids = [1021, 1022, 1023]

print("--- 2. Zip Mechanics ---")
for user_id, user_name in zip(ids, users):
    print(f"ID: {user_id} -> User: {user_name}")
print()


# =====================================================================
# 3. Technique: High-Performance String Assembly
# =====================================================================
# Problem: Loops doing `string += word` run in O(n²) because strings are immutable.
#          Python creates an entire new copy of the string on every single addition.
# Solution: Accumulate items into a list first, then combine them in O(n) using .join().

words_list = ["FastAPI", "Production", "Ready"]

print("--- 3. Clean Assembly Mechanics ---")
# The string before the dot is the connector character
clean_path = "/".join(words_list)
print(f"Constructed Path: {clean_path}\n")


# =====================================================================
# 4. Technique: In-Place Reverse vs Lazy Reversing
# =====================================================================
# Slicing with [::-1] creates a completely new list, wasting memory.
# reversed() creates a memory-efficient iterator that moves backwards.

numbers = [10, 20, 30]

print("--- 4. Reversal Mechanics ---")
# This creates a lazy pointer structure, not an allocated list copy
reversed_stream = reversed(numbers)
print(f"Iterator pointer address: {reversed_stream}")
print(f"Stream content consumed:  {list(reversed_stream)}")
