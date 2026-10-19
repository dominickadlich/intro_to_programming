# Objective:
# Use a sentinel-controlled while loop to repeat user input until they choose to stop.

# Initialize total and count set to 0.
total = 0
count = 0
user_input = 'y'

# Repeat while the user enters “y”.
while user_input == 'y':
    # Ask the user for a number, and if they want to enter another.
    total += int(input("Enter a number: "))
    count += 1
    user_input = input("Enter another number? (y or n): ")

# Calculate and display the average of all numbers entered.
avg = total / count
print(f"The average is {avg}")

# Expected Output

# Enter a number: 10
# Enter another number? (y or n): y
# Enter a number: 20
# Enter another number? (y or n): n
# The average is 15.0