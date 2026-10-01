shopping_list = []

ITEM_NUMBER = 5

for i in range(ITEM_NUMBER):
    item = input(f"Enter item {i + 1}: ")
    shopping_list.append(item)

print(f"Your list: {shopping_list}")

user_remove = input("Oh shoot! We can only accept 4 items. Which item do you want to remove? ")

shopping_list.remove(user_remove)

print(f"Updated list: {shopping_list}")