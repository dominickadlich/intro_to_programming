# Objective:
# Use logical operators (and) to combine two conditions.

# Ask the user for their income and years of employment.
income = int(input("Enter your income: "))
years_of_employment = int(input("Enter your years of employment: "))

# If the income is greater than 40,000 and the years of employment are 2 or more, display "You qualify for a loan!".
if income > 40_000 and years_of_employment >= 2:
    print("You qualify for a loan!")

# Otherwise, display "You do not qualify for a loan."
else:
    print("You do not qualify for a loan.")


# Enter your income: 45000
# Enter your years of employment: 3
# You qualify for a loan!
# --------------------------------------
# Enter your income: 39000
# Enter your years of employment: 10
# You do not qualify for a loan.
# --------------------------------------
# Enter your income: 50000
# Enter your years of employment: 1
# You do not qualify for a loan.    