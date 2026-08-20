# =====================================================================
# 1. Technique: Advanced Slicing & Memory Allocations
# =====================================================================
# Slicing creates a brand new shallow copy list, taking O(k) time/space.
# [::-1] is common for reversing, but it uses O(n) memory.

nums = [10, 20, 30, 40, 50]

print("--- 1. Slicing Mechanics ---")
# Step slicing [start:stop:step]
even_indices = nums[0:5:2]  # [10, 30, 50]
reversed_copy = nums[::-1]   # [50, 40, 30, 20, 10] (allocates new memory)

print(f"Reversed copy: {reversed_copy}")

# In-place reversal via .reverse() uses O(1) extra space (essential for space constraints!)
nums.reverse() 
print(f"In-place reversed original: {nums}\n")


# =====================================================================
# 2. Technique: Starred Unpacking (*rest)
# =====================================================================
# Cleanly separating head, body, or tail sections without manually slicing.

stream_data = [100, 200, 300, 400, 500]

print("--- 2. Starred Unpacking ---")
first, *middle, last = stream_data

print(f"First element (head): {first}")
print(f"Middle chunk (body):   {middle}")  # Always collected into a list
print(f"Last element (tail):   {last}\n")


# =====================================================================
# 3. Technique: Common Element Modifiers (The Cost of Positioning)
# =====================================================================
# Array inserts/deletions at the start require shifting ALL items.

arr = [2, 3, 4]

print("--- 3. List Operation Cost ---")
arr.append(5)         # O(1) amortized - very fast at the end
arr.insert(0, 1)      # O(n) linear time - slow! Everything must shift right.
removed_item = arr.pop(0)  # O(n) linear time - slow! Everything shifts left.

print(f"Final list: {arr} | Popped item: {removed_item}")
