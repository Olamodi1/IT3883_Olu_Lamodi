# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Olu Lamodi
# Assignment Number: Assignment 1
# Due Date: 01/24/2026
# Purpose: This program implements a text-based menu system that allows users to
#          append data to an input buffer, clear the buffer, display the buffer
#          contents, or exit the program. The buffer maintains user input across
#          multiple append operations until cleared.
# Resources: No external resources used - all code written independently.

def display_menu():
    # Print out the menu options for the user
    print("\n" + "=" * 50)
    print("TEXT-BASED MENU PROGRAM")
    print("=" * 50)
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")
    print("=" * 50)


def append_to_buffer(current_buffer):
    # Ask user to type in some text
    user_input = input("Enter text to append to the buffer: ")
    # Add the new text to what's already in the buffer
    updated_buffer = current_buffer + user_input
    print("Data successfully appended to buffer!")
    return updated_buffer


def clear_buffer():
    # Clear out everything in the buffer by making it empty
    print("Input buffer has been cleared!")
    return ""


def display_buffer(current_buffer):
    # Show what's currently stored in the buffer
    print("\n" + "-" * 50)
    print("CURRENT BUFFER CONTENTS:")
    print("-" * 50)
    # Check if there's anything in the buffer
    if current_buffer:
        print(current_buffer)
    else:
        # If buffer is empty, let the user know
        print("[Buffer is empty]")
    print("-" * 50)


def main():
    # Start with an empty buffer
    input_buffer = ""

    # Keep looping until user chooses to exit
    while True:
        # Show the menu
        display_menu()

        # Get the user's choice
        choice = input("\nEnter your choice (1-4): ")

        # Check which option the user picked
        if choice == "1":
            # User wants to add text to buffer
            input_buffer = append_to_buffer(input_buffer)

        elif choice == "2":
            # User wants to clear the buffer
            input_buffer = clear_buffer()

        elif choice == "3":
            # User wants to see what's in the buffer
            display_buffer(input_buffer)

        elif choice == "4":
            # User wants to exit the program
            print("\nThank you for using the program. Goodbye!")
            break

        else:
            # User entered something other than 1-4
            print("\nInvalid choice! Please enter a number between 1 and 4.")


# This runs the main function when the program starts
if __name__ == "__main__":
    main()