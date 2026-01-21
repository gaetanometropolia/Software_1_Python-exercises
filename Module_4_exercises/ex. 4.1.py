# Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

numbers = 1

while numbers <= 1000:
    if numbers % 3 == 0:
        print (numbers)
    numbers = numbers + 1
