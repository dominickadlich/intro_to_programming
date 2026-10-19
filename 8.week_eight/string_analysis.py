# Objective:
# Iterate through a string and analyze characters using a for loop.

# Instructions:

# Ask the user to enter a sentence.
user_sentence = input("Enter a sentence: ")
count = 0

for i in user_sentence:
    # Print each character on a new line.
    print(i)
    if i.isupper():
        count += 1
        
# After the loop, display how many uppercase letters the sentence contains.
print(f"Number of uppercase letters: {count}")

# Expected Result:

# Enter a sentence: Johnson County Community College
# J
# o
# h
# n
# ...
# e
# Number of uppercase letters: 4