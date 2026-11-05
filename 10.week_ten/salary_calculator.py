# Function 1: calculate_tax(salary)
def calculate_tax(salary):
    # This function receives the employee’s salary as a parameter.
    # It decides the tax rate based on the salary amount:
    # If the salary is $3,000 or less, tax = 10% of salary.
    if salary <= 3_000:
        tax = salary * 0.10
    # If the salary is greater than $3,000, tax = 15% of salary.
    else:
        tax = salary * 0.15
    # It should return the amount of tax that will be deducted.
    return tax

# Function 2: calculate_net_salary(salary)
def calculate_net_salary(salary):
    # This function calls calculate_tax(salary) to find the tax amount.
    tax_amount = calculate_tax(salary)
    # Then it subtracts the tax from the salary to find the net salary.
    net_salary = salary - tax_amount
    # It prints the tax amount inside the function.
    print(f"Tax deducted: ${tax_amount:.2f}")
    # Finally, it returns the net salary value.
    return net_salary

# In the main program:
def main():
    # Ask the user to enter their gross salary.
    salary = float(input("Enter your gross salary: "))
    # Call the calculate_net_salary() function and pass the salary to it.
    net = calculate_net_salary(salary)
    # Print the net salary after the function returns the result.
    print(f"Net salary: ${net:.2f}")

if __name__ == "__main__":
    main()

# Expected Result:

# Enter your gross salary: 4000
# Tax deducted: $600.0
# Net salary: $3400.0