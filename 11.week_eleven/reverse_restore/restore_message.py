# Use the open() command to open reversed.txt in read mode.
f = open("./reversed.txt", "r")

# Use the read() command to get the text from the file.
reversed_string = f.read()

# Use string slicing again to reverse it back to the original.
restored_string = reversed_string[::-1]

f.close()

# Use the print() command to display the restored message.
print(f"Original message: {restored_string}")