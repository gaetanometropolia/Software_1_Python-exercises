# Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

inches = float(input("Enter inches: "))

while inches >= 0:
    cm = inches * 2.4
    print (f"{inches} inches = {cm} cm ")
    inches = float(input("Enter inches (negative value to stop): "))
print ("program ended")