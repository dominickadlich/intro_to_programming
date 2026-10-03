# Start with scores = [0, 0, 0, 0, 0].
scores = [0, 0, 0, 0, 0]

# Change the first element to 4.
scores[0] = 4

# Change the element at index 3 to 5.
scores[3] = 5

# Decrease the last element by 1.
scores[-1] -= 1

print(scores)

# Print the length of the list (Hint: use len()).
print(f'Length: {len(scores)}')

# Create another list with the first 5 letters of the alphabet.
abcde = ['A', 'B', 'C', 'D', 'E']

# Append "F" to the list (Hint: use .append()).
abcde.append('F')

# Print the updated list.
print(abcde)

# Expected Result:
# [4, 0, 0, 5, -1]
# Length: 5
# ['A', 'B', 'C', 'D', 'E', 'F']