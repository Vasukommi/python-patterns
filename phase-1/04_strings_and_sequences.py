# =====================================================================
# 1. Technique: Core String Manipulations
# =====================================================================

raw_input = "   FastAPI,Production,Ready   "

cleaned_input = raw_input.strip()
items = cleaned_input.split(",")

print("--- 1. String Mechanics ---")
print(f"Stripped & Split: {items}")
print(f"Replaced Path:    {cleaned_input.replace(',', '/')}\n")

# =====================================================================
# 2. Technique: Range Boundary Navigation
# =====================================================================

countdown = list(range(10, 1, -2))
print(f"Backward slice with range: {countdown}\n")