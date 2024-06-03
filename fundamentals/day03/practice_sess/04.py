# Write a  program to find reverse of any number using recursion.
#get a number fn(number)
#check if number < 10 =>return numbeer
# Get the last digit of the number
# Get the remaining digits
# Recurs => reverse the remaining digits
#Return join the number

def reverse_number(number):
    if number < 10:
        return number
    else:
        last_digit = number % 10
        remaining_digits = number // 10
        reversed_remaining = reverse_number(remaining_digits)
        return (str(last_digit) + str(reversed_remaining))

number = 45
print(number)
print(reverse_number(number))
