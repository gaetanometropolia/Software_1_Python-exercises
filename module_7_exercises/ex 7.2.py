# Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the program either prints out New name or Existing name depending on whether the name was entered for the first time. Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure to store the names.

names = set()

while True:
    name = input("Enter a name: ")

    if name == "":
        break

    if name in names:
        print ("existing name")
    else:
        print ("new name")
        names.add(name)
print ("names entered are:")
for n in names:
    print (n)