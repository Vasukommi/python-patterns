# =====================================================================
# 1. Technique: De-duplication and Fast Membership (O(1))
# =====================================================================
# Checking `if item in list` takes O(n) linear time because it scans sequentially.
# Checking `if item in set` takes O(1) constant time due to hashing.

raw_ids = [4, 1, 2, 2, 3, 4, 1]

print("--- 1. Set Foundations ---")
# Instantiating a set filters out all duplicate entries instantly
unique_ids = set(raw_ids)
print(f"De-duplicated set: {unique_ids}")

# O(1) membership validation
print(f"Is ID 3 present? {3 in unique_ids}\n")


# =====================================================================
# 2. Technique: Set Mathematics & Bitwise Operators
# =====================================================================
# These operations are highly optimized in C under the Python engine.

group_a = {1, 2, 3}
group_b = {3, 4, 5}

print("--- 2. Set Mathematics ---")

# Intersection (&): Items present in BOTH sets
intersection_set = group_a & group_b  # Alternative: group_a.intersection(group_b)
print(f"Intersection (&): {intersection_set}")  # {3}

# Union (|): All distinct items combined from both sets
union_set = group_a | group_b         # Alternative: group_a.union(group_b)
print(f"Union (|):        {union_set}")         # {1, 2, 3, 4, 5}

# Difference (-): Items in group_a that DO NOT exist in group_b
difference_set = group_a - group_b    # Alternative: group_a.difference(group_b)
print(f"Difference (-):   {difference_set}")    # {1, 2}

# Symmetric Difference (^): Items in either set, but NOT in both
sym_diff_set = group_a ^ group_b      # Alternative: group_a.symmetric_difference(group_b)
print(f"Symmetric Diff (^): {sym_diff_set}")  # {1, 2, 4, 5}
