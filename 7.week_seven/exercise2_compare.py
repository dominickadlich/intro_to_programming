# Objective:
# Use relational operators (>, <, ==) to compare values.

# Ask the user to input two numbers.
num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))

# Compare them and print whether the first number is greater, smaller, or equal to the second.
if num_one > num_two:
    print(f"{num_one} is greater than {num_two}")
elif num_one < num_two:
    print(f"{num_one} is smaller than {num_two}")
elif num_one == num_two:
    print("The two numbers you entered are equals")

# Expected Result:

# Enter first number: 5
# Enter second number: 8
# 5 is smaller than 8
# --------------------------
# Enter first number: 14
# Enter second number: 11
# 14 is greater than 11
# --------------------------
# Enter first number: 10
# Enter second number: 10
# The two numbers you entered are equals