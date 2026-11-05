# Objective:
# Use a for loop to iterate through a dictionary and apply conditional logic to find B grades.

# Use the following dictionary:
scores = { 'Bob': 95, 'Ella': 98, 'Lauren': 78, 'Jon': 83, 'Alex': 65, 'Nina': 87, 'Mia': 92, 'Tom': 81, 'Liam': 76, 'Sara': 88, 'Noah': 90, 'Olivia': 84, 'Emma': 73, 'Ava': 67 }

b_count = 0
# Use a for loop to print each student’s name and grade.
for name in scores:
    print(f"{name} has a grade of {scores[name]}")
    # Count how many students earned a B grade (score between 80 and 89 inclusive).
    if 80 <= scores[name] < 90:
        b_count += 1

# Display the number of B grades at the end.
print(f"The number of B's is {b_count}")

# Expected Result:
# Bob has a grade of 95
# Ella has a grade of 98
# Lauren has a grade of 78
# Jon has a grade of 83
# Alex has a grade of 65
# Nina has a grade of 87
# Mia has a grade of 92
# Tom has a grade of 81
# Liam has a grade of 76
# Sara has a grade of 88
# Noah has a grade of 90
# Olivia has a grade of 84
# Emma has a grade of 73
# Ava has a grade of 67
# The number of B's is 5