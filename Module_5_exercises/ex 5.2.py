# Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.

numbers = []

user_input = input(" enter a number(press enter to exit):")

while user_input != "":
    numbers.append(int(user_input))
    user_input = input(" enter another number(press enter to exit): ")

numbers.sort(reverse=True)

print ("the five gratest numbers are:")
for n in range (0 , 5):
    print (numbers [n])

