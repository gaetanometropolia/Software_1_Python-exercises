# Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters. Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.

import random

def roll_dice():
    return random.randint(1, 6)


def main():
    roll = 0
    while roll != 6:
        roll = roll_dice()
        print (roll)

main()