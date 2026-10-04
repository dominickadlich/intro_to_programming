ITEM_NUMBER = 5

# Start with an empty list.
shopping_list = []

# Ask the user to enter 5 grocery items and add them (Hint: use .append()).
for i in range(ITEM_NUMBER):
    item = input(f"Enter item {i + 1}: ")
    shopping_list.append(item)

# Print the complete list.
print(f"Your list: {shopping_list}")

# Ask which item to remove.
user_remove = input("Oh shoot! We can only accept 4 items. Which item do you want to remove? ")

# Remove it from the list (Hint: use .remove()).
shopping_list.remove(user_remove)

# Print the updated list.
print(f"Updated list: {shopping_list}")