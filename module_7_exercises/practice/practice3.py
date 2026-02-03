# Write a program that functions as a simple phonebook. The program asks the user whether they want to add a new contact, search for an existing contact, or quit.
#
# If the user chooses to add a new contact, the program asks for the contact's name and phone number.
#
# If the user chooses to search, the program asks for a name and prints the corresponding phone number.
#
# If the user wants to quit, the program terminates.
#
# The program should store the data in a dictionary and allow the user to select actions multiple times until they decide to quit. The program must also handle the situation where the user tries to search for a name that does not exist.


phonebook = {}

while True:

    print("press 1 if u want add a new contact")
    print("press 2 if u want search for an existing contact")
    print("press 3 to Quit")

    user_input=int(input("Enter a selection from 1 to 3: "))

    if user_input == 1:
        contact_name = input("Enter a name: ")
        contact_number = input("Enter a number: ")
        phonebook[contact_name] = contact_number

    elif user_input == 2:
        contact_name = input("Enter a name: ")
        if contact_name in phonebook:
            print(f"corresponding number is {phonebook[contact_name]}")

    elif user_input == 3:
        break

else:
    print("invalid input")