# =====================================================================
# 1. Technique: In-Place sort() vs Out-of-Place sorted()
# =====================================================================
# Python uses Timsort (O(n log n) time, stable, O(n) space worst-case).

unordered = [5, 2, 9, 1]

print("--- 1. Basic Sorting ---")
# sorted() returns a new list; original is unchanged
fresh_sorted = sorted(unordered) 

# .sort() mutates the list directly in-place (saves memory allocations)
unordered.sort() 
print(f"Original mutated in-place: {unordered}\n")


# =====================================================================
# 2. Technique: Custom Sorting Keys with Lambda
# =====================================================================
# The 'key' function transforms elements before comparing them.
# Perfect for objects, dictionaries, or tuples.

students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 95},
    {"name": "Charlie", "grade": 88}
]

print("--- 2. Single Key Sorting ---")
# Sort primary by grade ascending
students.sort(key=lambda s: s["grade"])
print(f"Sorted by grade: {students}\n")


# =====================================================================
# 3. Technique: Advanced Multi-Condition Tuple Sorting
# =====================================================================
# Python compares tuples element-by-element: (A1, B1) < (A2, B2).
# Trick: To reverse a numeric sorting condition, put a minus sign (-) in front of it.

# Goal: Sort coordinates by X ascending, but if X is a tie, sort by Y descending!
points = [(4, 5), (1, 2), (4, 9), (1, 5)]

print("--- 3. Multi-Condition Sorting ---")
# Tie-breaker logic: p[0] is X (normal ascending), -p[1] flips Y to descending
points.sort(key=lambda p: (p[0], -p[1]))

print(f"X ascending, Y descending: {points}")
