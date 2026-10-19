# Objective:
# Use a for loop with a negative step to count down.

# Ask the user to enter a starting number.
user_num = int(input("Enter a number: "))

# Use a for loop to count down from that number to 1.
for i in range(user_num, 0, -1):
    print(i)
    
print("Blast off!")

# Print “Blast off!” after the loop.

# Expected Result:

# Enter a number: 5
# 5
# 4
# 3
# 2
# 1
# Blast off!