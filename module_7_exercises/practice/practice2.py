# Write a program that asks the user for numbers one at a time. The program continues to ask for numbers until the user enters 0. The numbers are stored in a list. After this, the program should print the list without duplicates, meaning only the unique numbers that were entered.
#
# Hint: You can create a new set from the list, which automatically removes all duplicates. You can then convert the set back into a list if you need list functionalities.

numbers = []

while True:
    user_input = int(input("Enter a number: "))

    if user_input == 0:
        break



    else:
        numbers.append(user_input)

output = set(numbers)


print(output)

