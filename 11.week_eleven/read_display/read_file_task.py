# Use the open() command to open the text file in read mode.
f = open("chapter9_message.txt", "r")

# Use the read() command to read the entire contents into a variable.
contents = f.read()

# Use the close() command to close the file.
f.close()

# Use the print() command to display the title File Contents: and then the text from the file.
print(f"File Contents:\n{contents}")