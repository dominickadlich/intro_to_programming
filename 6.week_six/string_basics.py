# Store your full name in a variable.
full_name = "Dominick Adlich"

# Print the length of your name (Hint: use len()).
print(f"Length of name: {len(full_name)}")

# Print your name in uppercase and lowercase (Hint: use .upper() and .lower()).
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")

# Replace "a" in your name with "@" (Hint: use .replace()).
modified = full_name.replace('A', '@')
print(f"Modified: {modified}")

# Check if "@" exists in the string (Hint: use in).
result = '@' in modified 

print(f"Is '@' in the string? {result}")