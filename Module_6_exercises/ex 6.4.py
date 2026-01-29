# Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.

def sum_list (numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total

def main():
    numbers = []
    user_input = input("Enter numbers: (press enter to quit) ")
    while user_input!= "":
        numbers.append(int(user_input))
        user_input = input("Enter numbers: (press enter to quit) ")


    result = sum_list(numbers)
    print ( "sum is ", result)
main()