# Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

airport_data = {}

while True:
    print("Choose an option:")
    print("1. Enter a new airport")
    print("2. Fetch information of an existing airport")
    print("3. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        icao= input("Enter an ICAO: ")
        name=input("Enter a name")
        airport_data[icao] = name

    elif choice == 2:
        icao = input("Enter an ICAO: ")
        if icao in airport_data:
            print (f"corresponding name is {airport_data[icao]}")
        else:
            print("not found")

    elif choice == 3:
        break
else:
    print ("invalid input")




