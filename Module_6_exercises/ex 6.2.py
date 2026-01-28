# Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice, which is asked from the user at the beginning.

import random

def roll_dice(sides):
    return random.randint(1, sides)


def main():
    sides = int(input("Enter number of sides: "))
    roll = 0
    while roll != sides:
        roll = roll_dice(sides)
        print (roll)

main()