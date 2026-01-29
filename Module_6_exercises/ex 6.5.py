# Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.



def number_list(numbers):
    even_numbers = []
    for i in numbers:
        if  i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


def main ():
    numbers = [1,2,3,4,5,6,7,8,9]
    result = number_list(numbers)
    print ("the original list is ",   numbers)
    print ("the even numbers of the list are", result)

main()





