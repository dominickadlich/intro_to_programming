# Objective:
# Practice using nested loops to display a right-angled triangle made of asterisks (*).

# Write a program that:
# Asks the user to enter the number of rows for the triangle.
rows = int(input("Enter the number of rows: "))

# Uses nested for loops to print the right-angled triangle.
# The first loop should control the number of rows
for i in range(1, rows + 1):
    # the inner loop should control how many stars appear in each row.
    for _ in range(i):
        print("*", end="")
    print()

# Run the program and verify the output matches the example.

# Expected Output Example:

# Enter the number of rows: 5
# *
# **
# ***
# ****
# *****