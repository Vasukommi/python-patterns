# =====================================================================
# 1. Technique: Core String Manipulations
# =====================================================================
# Strings are immutable; every method returns a completely NEW string.

raw_input = "   FastAPI,Production,Ready   "

# Clean up whitespace and break the string apart into an array
cleaned_input = raw_input.strip()
items = cleaned_input.split(",")

print("--- 1. String Mechanics ---")
print(f"Stripped & Split: {items}")
print(f"Replaced Path:    {cleaned_input.replace(',', '/')}\n")


# =====================================================================
# 2. Technique: Range Boundary Navigation
# =====================================================================
# range(start, stop, step) -> 'stop' is exclusive (not included!)

print("--- 2. Range Mechanics ---")
# Count down backwards from 10 to 2
countdown = list(range(10, 1, -2))
print(f"Backward slice with range: {countdown}\n")


# =====================================================================
# 3. Technique: Optional/Removed Concept Note
# =====================================================================
# As discussed, 'string.ascii_letters' is omitted from core priority. 
# It is just a static string helper: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("--- 3. Audit Note ---")
print("Phase 1 is now 100% complete. Ready for Phase 2 tomorrow!")
