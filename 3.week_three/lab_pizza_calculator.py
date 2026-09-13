# Warn user not to enter 0 for calculation
print("Warning: Do not enter 0 for the number of people!")

# Obtain number of pizza slices
num_slices = int(input("How many slices of pizza are available? "))

# Obtain number of guests
num_guests = int(input("How many people are eating? "))

# Calculate number of slices per person
slices_per_guest =  num_slices / num_guests

# Print result for user
print("Number of slices per person:", slices_per_guest)