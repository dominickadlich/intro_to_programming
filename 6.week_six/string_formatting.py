# Ask the user to enter a product name.
product_name = input("Enter product: ")

# Ask the user to enter a quantity (Hint: cast with int(input())).
qty = int(input("Enter quantity: "))

# Ask the user to enter a price per unit (Hint: cast with float(input())).
price = float(input("Enter price per unit: "))

# Calculate the total and display the result with 2 decimal places (Hint: use f"{value:.2f}").
total = qty * price
print(f"{qty} {product_name} cost ${total:.2f}")

# Expected Result:
# Enter product: apples
# Enter quantity: 5
# Enter price per unit: 1.5
# 5 apples cost $7.50