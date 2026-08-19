import copy

# =====================================================================
# 1. Technique: References vs Objects (The "is" vs "==" Distinction)
# =====================================================================

list_a = [1,2,3]
list_b = [1,2,3]

list_c = list_a

print("--- 1. Reference Check ---")
print(f"Structural Equality (list_a == list_b): {list_a == list_b}")  # True: values match
print(f"Identity Equality   (list_a is list_b): {list_a is list_b}")  # False: separate memory boxes
print(f"Shared Reference    (list_a is list_c): {list_a is list_c}")  # True: same exact box
print(f"Memory Addresses: a={id(list_a)}, c={id(list_c)}\n")

# =====================================================================
# 2. Technique: Shallow Copy vs Deep Copy
# =====================================================================

original = [[1, 2], [3, 4]]

shallow_cloned = original.copy() # Alternative: original[:] or list(original)

deep_cloned = copy.deepcopy(original)

original[0][0] = 99 

print("--- 2. Copy Behavior Check ---")
print(f"Original list:       {original}")
print(f"Shallow copy legacy: {shallow_cloned}")  # Affected! Sub-list references were shared.
print(f"Deep copy isolated:  {deep_cloned}\n")    # Clean! Deepcopy fully unlinked memory.

# =====================================================================
# 3. Technique: The Mutable Default Argument Trap
# =====================================================================

def append_to_payload(item, payload = []):
    payload.append(item)
    return payload

print("--- 3. Default Argument Bug ---")
first_call = append_to_payload("user_id")
second_call = append_to_payload("session_token")

print(f"First call output:  {first_call}")
print(f"Second call output: {second_call}")  # Polluted! The hidden default list persists.