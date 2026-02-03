# Write a program that asks the user for three different fruits and their amounts in kilograms. Store the fruits and their amounts in a dictionary where the fruit's name is the key and the amount is the value. The program should print the dictionary.


fruit_store = {}

#faster way

# for i in range(3):
#     fruit = input("Enter a fruit: ")
#     amount = int(input("Enter an amount: "))
#     fruit_store[fruit] = amount
# print(fruit_store)

fruit1 = input("Enter a fruit name: ")
amount1 = int(input("Enter a fruit amount: "))
fruit_store[fruit1] = amount1

fruit2 = input("Enter another fruit name: ")
amount2 = int(input("Enter another fruit amount: "))
fruit_store[fruit2] = amount2

fruit3 = input("Enter another fruit name: ")
amount3 = int(input("Enter another fruit amount: "))
fruit_store[fruit3] = amount3

print (fruit_store)
print("end")
