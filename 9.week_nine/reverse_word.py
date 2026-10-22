# Objective:
# Use the reversed() function and a for loop to process a string in reverse.

# Ask the user to enter a word.
user_word = input("Enter a word: ")

reversed_word = ""
# Use a for loop with reversed() to display the word backward (on one line).
for char in reversed(user_word):
    reversed_word += char

print(f"Reversed word: {reversed_word}")

# Do not use slicing ([::-1]).

# Expected Result:

# Enter a word: Python
# Reversed word: nohtyP