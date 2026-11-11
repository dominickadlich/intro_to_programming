def main():
    # Use the input() command to ask the user to type a message.
    user_message = input("Enter a message: ")

    # Use string slicing ([::-1]) to reverse the message.
    reversed_message = user_message[::-1]

    # Use the open() command in write mode to create a file named reversed.txt.
    f = open("reversed.txt", "w")

    # Use the write() command to save the reversed text.
    f.write(reversed_message)

    # Use the close() command to close the file.
    f.close()

    # Use the print() command to confirm that the reversed message was saved.
    print("Reversed message saved in reversed.txt")

    # Run the program once and enter a message of your choice.
if __name__ == "__main__":
    main()