# Objective:
# Use string length, in, and logical operators to check password strength.

# Ask the user to enter a password.
password = input('Enter a password: ')

length = len(password)

# Classify the password:
# If the password has fewer than 6 characters → print "Weak password".
if length < 6:
    print('Weak password')

# If the password has 6–10 characters → print "Moderate password".
elif length <= 10:
    print('Moderate password')

# If the password has more than 10 characters and includes either @ or ! → print "Strong password".
elif '!' in password or '@' in password:
    print('Strong password')

# If the password has more than 10 characters but no @ or ! → print "Strong password (without special symbol)".
else:
    print('Strong password (without special symbol)')


# Expected Results:
# Enter a password: cat1
# Weak password
# --------------------------------------
# Enter a password: Tiger22
# Moderate password
# --------------------------------------
# Enter a password: supersecurepass
# Strong password (without special symbol)
# --------------------------------------
# Enter a password: supersecurepass!
# Strong password