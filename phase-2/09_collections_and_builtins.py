from collections import Counter, defaultdict, deque

# =====================================================================
# 1. Technique: Advanced Counting with Counter
# =====================================================================
# Counter is a dict subclass designed specifically for frequency mapping.

votes = ["yes", "no", "yes", "yes", "absent", "no"]

print("--- 1. Counter Mechanics ---")
vote_counts = Counter(votes)
print(f"Frequency Map: {vote_counts}")  # Counter({'yes': 3, 'no': 2, 'absent': 1})

# Extract top K elements using an internal heap-based algorithm (O(n log k))
print(f"Top 2 most common: {vote_counts.most_common(2)}\n")


# =====================================================================
# 2. Technique: Automatic Initialization with defaultdict
# =====================================================================
# Eliminates KeyError checks when appending items to nested structures.

# Passing 'list' means any missing key automatically instantiates a new empty list []
grouped_items = defaultdict(list)

print("--- 2. defaultdict Mechanics ---")
grouped_items["prime"].append(2)
grouped_items["prime"].append(3)
grouped_items["even"].append(4)

print(f"Grouped items: {dict(grouped_items)}\n")  # Converted to regular dict for clean print


# =====================================================================
# 3. Technique: Double-Ended Queues (deque)
# =====================================================================
# Problem: list.pop(0) takes O(n) time because it shifts elements in memory.
# Solution: deque implements a linked list layout for true O(1) shifts.

queue = deque(["task1", "task2"])

print("--- 3. Deque Mechanics ---")
queue.append("task3")      # O(1) push right
queue.appendleft("task0")  # O(1) push left
popped_left = queue.popleft() # O(1) pop left (Essential for BFS trees/graphs!)

print(f"Queue state: {queue} | Popped left: {popped_left}\n")


# =====================================================================
# 4. Technique: Global Assertions and Custom Bounds
# =====================================================================
# any() and all() use short-circuiting to check stream conditions.
# min() and max() accept 'key' functions just like sorting methods.

numbers = [4, -12, 8, 3]

print("--- 4. Built-in Utilities ---")
# Check if any element is negative
has_negative = any(x < 0 for x in numbers)
# Check if all elements are positive
all_positive = all(x > 0 for x in numbers)

print(f"Has negative? {has_negative} | All positive? {all_positive}")

# Extract maximum based on absolute distance from zero
absolute_max = max(numbers, key=lambda x: abs(x))
print(f"Max by absolute value: {absolute_max}")
