# Obtain weekly hours from user
hours_per_week = int(input("Enter the number of hours you work per week: "))

# Obtain hourly wage from user 
hourly_wage = int(input("Enter your hourly wage: "))

# Calculate weekly income based on user input
weekly_income = hours_per_week * hourly_wage

# Display weekly income given user input
print("Your weekly income is $", weekly_income, sep='')