# Objective:
# Use if, elif, and else to categorize numeric scores.

# Ask the user to enter a score between 0 and 100.
user_score = int(input("Enter your score: "))

# Use the following rules:
# 90 or above → “A”
if user_score >= 90:
    grade = 'A'
# 80–89 → “B”
elif user_score >= 80:
    grade = 'B'
# 70–79 → “C”
elif user_score >= 70:
    grade = 'C'
# 60–69 → “D”
elif user_score >= 60:
    grade = 'D'
# Below 60 → “F”
else:
    grade = 'F'

print(f'Your grade is: {grade}')
# Expected Result:

# Enter your score: 87
# Your grade is: B
# ----------------------
# Enter your score: 70
# Your grade is: C