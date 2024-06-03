# Write a Python program to find the sum of digits of a given number. 
# E.g. Sum of number 123 will be 6
# Note: Initialize the number with various values and test your program.

#get number
#convert into (str)
#loop 
#Get first digit(str)
#Convert into (int)
#add it to sum


def sum_of_digits(number):
    sum = 0
    number_str = str(number)
    for digit_str in number_str:
        digit = int(digit_str)
        sum += digit
    return print("Sum of digits of", number, "is:",sum)

number = 123
sum_of_digits(number)

