# Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.

import random

digit_three_1 = random.randint (0,9)
digit_three_2 = random.randint (0,9)
digit_three_3 = random.randint (0,9)

print (digit_three_1, digit_three_2, digit_three_3)

digit_four_1 = random.randint (1,6)
digit_four_2 = random.randint (1,6)
digit_four_3 = random.randint (1,6)
digit_four_4 = random.randint (1,6)

print (digit_four_1, digit_four_2, digit_four_3, digit_four_4)
