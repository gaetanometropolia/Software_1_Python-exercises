# Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.

cities_list = []


for n in range(5):
    user_input = input("enter the name of city: ")
    cities_list.append(user_input)

for i in cities_list:
    print(i)