# =====================================================================
# 1. Technique: Advanced Scope Isolation (LEGB)
# =====================================================================

global_counter = 100

def outer_function():
    outer_value = "Initial Outer State"
    
    def inner_function():
        nonlocal outer_value
        outer_value = "Modified Outer state"
        
        global global_counter
        global_counter += 1
    inner_function()
    return outer_value

print(f"Modified outer variable: {outer_function()}\n")
print(f"Global counter modified: {global_counter}\n")

# =====================================================================
# 2. Technique: Short-Circuit Evaluation
# =====================================================================

# If first condition is False, Python stops executing immediately.
# This safeguards against "NoneType object has no attribute..." crashes.

node = None

if node and node.val == 10:  # PEP 8 Standard: if node is not None and node.val == 10:
    print("Found!")
else:
    print("Safely skipped crash due to short-circuiting.\n")
    
# =====================================================================
# 3. Technique: Ternary Operators (Conditional Expressions)
# =====================================================================

score = 65

status = "pass" if score >= 50 else "fail"
print(status)