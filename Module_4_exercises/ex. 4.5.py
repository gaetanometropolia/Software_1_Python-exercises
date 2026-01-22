# Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.

user = input("Enter username: ")

password = input("Enter password: ")

attempts = 0

while user != "python" or password != "rules":
    attempts = attempts + 1
    print("Wrong username or password")

    if attempts == 5:
        print ("access denied")
        break

    user = input("enter username")
    password = input("enter password")

if user == "python" and password == "rules":
    print ("welcome")




