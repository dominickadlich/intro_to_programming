# Use the open() command in write mode to create a file named notes.txt.
f = open("notes.txt", "w")

# Use the write() command three times to write three sentences (each on a new line).
f.write("File handling is an essential Python topic.\n")
f.write("Always open a file before writing.\n")
f.write("Always close it when finished.\n")

# Use the close() command to close the file.
f.close()

# Reopen the same file using open() in append mode.
f = open("notes.txt", "a")

# Use the write() command twice to add two new sentences at the end.
f.write("Append mode adds new content at the end.\n")
f.write("Existing data is never lost when appending.\n")

# Use the close() command again to close the file.
f.close()

print("Program finished. File 'notes.txt' created and updated.")