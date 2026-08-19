# =====================================================================
# 1. Technique: Position Tracking with enumerate()
# =====================================================================

ranks = ["Alpha", "Beta", "Gamma"]

for index, code_name in enumerate(ranks, start=1):
    print(f"Rank #{index}: {code_name}")
    
# =====================================================================
# 2. Technique: Parallel Stream Binding with zip()
# =====================================================================

users = ["Alice", "Bob", "Charlie"]
ids = [1021, 1022, 1023]

for user_id, user_name in zip(ids, users):
    print(f"ID: {user_id} -> User: {user_name}")
    

# =====================================================================
# 3. Technique: High-Performance String Assembly
# =====================================================================

words_list = ["FastAPI", "Production", "Ready"]

clean_path = "/".join(words_list)
print(f"Constructed Path: {clean_path}\n")

# =====================================================================
# 4. Technique: In-Place Reverse vs Lazy Reversing
# =====================================================================

numbers = [10, 20, 30]

reversed_stream = reversed(numbers)
print(f"Iterator pointer address: {reversed_stream}")
print(f"Stream content consumed:  {list(reversed_stream)}")