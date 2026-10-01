full_name = "Dominick Adlich"

print(f"Length of name: {len(full_name)}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")

modified = full_name.replace('A', '@')

print(f"Modified: {modified}")

if '@' in modified: 
    result = True
else: 
    result = False

print(f"Is @ in the string? {result}")