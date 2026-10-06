# Objective:
# Use multiple if-elif-else branches and logical comparisons to determine ticket prices.

# Ask the user to enter their age.
age = int(input("Enter your age: "))

# Age < 5 → Free
if age < 5:
    ticket_price = 0

# Age 5–12 → $5
elif age <= 12:
    ticket_price = 5

# Age 13–59 → $10
elif age <= 59:
    ticket_price = 10

# Age 60 and above → $7
else:
    ticket_price = 7

# Display the appropriate price message.
print(f"Your ticket price is ${ticket_price}.")

# Expected Result:

# Enter your age: 65
# Your ticket price is $7.
# -----------------------------
# Enter your age: 40
# Your ticket price is $10.