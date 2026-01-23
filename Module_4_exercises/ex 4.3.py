# Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.

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





