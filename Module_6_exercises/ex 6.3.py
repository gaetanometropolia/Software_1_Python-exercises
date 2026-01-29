# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters. The conversion must be done by using the function. Conversions continue until the user inputs a negative value.


def conversion():
    if gallons >0:
        liters = gallons * 3.785
        print (f"{gallons} gallons are {liters} liters ")
    return

while True:
    gallons = float(input("enter how many gallons "))
    if gallons <0:
        print (f"{gallons} gallons is negative")
        break
    else:
        conversion()



