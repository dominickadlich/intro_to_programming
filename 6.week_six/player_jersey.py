# Create a dictionary with 3 soccer players and their jersey numbers. {'Messi': 10, 'Ronaldo': 7, 'Neymar': 11}
jersey_numbers = {
    'Messi': 10,
    'Ronaldo': 7,
    'Neymar': 11
}

# Print Messi’s jersey number (Hint: use dict[key]).
print(f"Messi's jersey: {jersey_numbers['Messi']}")

# Add a new player to the dictionary. {'Mbappe': 9}
jersey_numbers['Mbappe'] = 9

# Update Ronaldo’s jersey number. (Make it 77)
jersey_numbers.update({'Ronaldo': 77})

# Print the updated dictionary.
print(jersey_numbers)