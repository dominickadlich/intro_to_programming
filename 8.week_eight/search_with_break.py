# Objective:
# Use break to stop early when a match is found and else to handle “not found”.

# Define a list: fruits = ["apple", "banana", "cherry", "mango"].
fruits = ["apple", "banana", "cherry", "mango"]

# Ask the user for a fruit to search for.
user_fruit = input("Search for: ")

# Loop through the list:
for fruit in fruits:
    if user_fruit in fruits:
        # If you find the fruit, print Found: <fruit> and break.
        print(f"Found {user_fruit}")
        break
# If the loop finishes without finding it, use else to print Not found.
else:
    print("Not found")


# Expected Result (found case):

# Search for: banana
# Found: banana
# Expected Result (not found case):

# Search for: kiwi
# Not found