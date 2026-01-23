# Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.

# ask user to enter input
# Variables to store: user input, smallest_number, largest number, empty string, user_input_int

# WHILE Loop (until the user input is an empty string, string_var = ', ==
# Convert input to an int -> user_input_int = int(user_input)
# Check (if) user input < smallest_number
# smallest_number = user input!
# elif user input > Largest_number


# largest_number = user input!
# ask input
# Print the variables smallest and Largest numbers!

user_input = input("Enter a number:  ")

if user_input == "":
    print("No numbers entered.")

else:
    user_input_int = int(user_input)
    smallest_number = user_input_int
    largest_number = user_input_int
    user_input = input("Enter a number: (press enter to exit) ")

    while user_input != "":
        user_input_int = int(user_input)
        if user_input_int > largest_number:
            largest_number = user_input_int
        elif user_input_int < smallest_number:
            smallest_number = user_input_int

        user_input = input("Enter a number: (press enter to exit)")

    print ("smallest_number" ,  smallest_number )
    print ("largest_number" ,  largest_number )





