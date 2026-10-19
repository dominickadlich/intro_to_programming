# Objective:
# Use a while loop to validate input and trap the user until a valid value is entered.

user_age = int(input("Enter your age: "))

# If the age is negative, print “Invalid age.” and ask again.
while user_age < 0:
    print("Invalid age.")
    # Ask the user to enter their age.
    user_age = int(input("Enter your age: "))

# When a valid age (≥ 0) is entered, display “Valid age entered.”
print("Valid age entered.")

# Expected Result:

# Enter your age: -3
# Invalid age.
# Enter your age: -1
# Invalid age.
# Enter your age: 21
# Valid age entered.
