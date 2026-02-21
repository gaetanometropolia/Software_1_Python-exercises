# Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.

seasons = ("spring", "summer", "autumn", "winter")

month = int(input("Enter a number: "))

if month == 12 or month == 1 or month == 2:
    print(seasons[3])
elif month == 3 or month == 4 or month == 5:
    print(seasons[0])
elif month == 6 or month == 7 or month == 8:
    print(seasons[1])
elif month == 9 or month == 10 or month == 11:
    print (seasons[2])
else:
    print("no valid number")