# Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
#
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.
# Example output:
#
# Enter talents:
# 3
#
# Enter pounds:
# 9
#
# Enter lots:
# 13.5
#
# The weight in modern units:
# 29 kilograms and 545.95 grams.


#asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti).
talents_string = input("enter the mass in talents:")
pounds_string = input("enter the mass in pounds:")
lots_string = input("enter the mass in lots:")

#calculate kilograms and grams from the mass input
talent_conversion_grams = float(talents_string) * 20 * 32 * 13.3
pound_conversion_grams = float(pounds_string) * 32 * 13.3
lots_conversion_grams = float(lots_string) * 13.3

sum_kilograms = (talent_conversion_grams + pound_conversion_grams + lots_conversion_grams) // 1000
sum_grams = (talent_conversion_grams + pound_conversion_grams + lots_conversion_grams) % 1000

#output the result to the user
print ("the weight in modern units")
print (f"{sum_kilograms}kilograms and {sum_grams:.2f} grams")

#end