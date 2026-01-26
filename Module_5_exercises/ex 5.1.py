# Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

import random

dice_number = int(input("how many dice to roll? "))

total = 0

for n in range(dice_number):
    roll = random.randint(1, 6)
    total = total + roll

print("the sum of the total number rolled is: ", total )