# Objective:
# Use if, elif, and else with logical operators to identify number ranges.

# Ask the user to enter a number.
user_num = int(input("Enter a number: "))

# Display:
# "Number is negative." if the number is less than 0
if user_num < 0:
    print("Number is negative.")

# "Number is between 0 and 10." if between 0 and 10
elif user_num >= 0 and user_num <= 10:
    print("Number is between 0 and 10.")

# "Number is between 11 and 20." if between 11 and 20
elif user_num >= 11 and user_num <= 20:
    print("Number is between 11 and 20.")

# "Number is above 20." if greater than 20
else:
    print("Number is above 20.")

# Expected Results:

# Enter a number: -2
# Number is negative.
# -------------------------------
# Enter a number: 7
# Number is between 0 and 10.
# -------------------------------
# Enter a number: 15
# Number is between 11 and 20.
# -------------------------------
# Enter a number: 33
# Number is above 20.