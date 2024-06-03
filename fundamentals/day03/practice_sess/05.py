# Write a  program to find sum of digits of a given number using recursion.

#Get a number fn(number)
#check number > 10
#last_digit = n% 10
#remaining_digit = n // 10
#recuur = > last_digit +  fn(remaining_digit)  

def sum_of_digits(number):
    if number < 10:
        return number
    else:
        last_digit = number % 10
        remaining_digits = number // 10
        return last_digit + sum_of_digits(remaining_digits)

number = 12
print("Sum of ",number," digits:", sum_of_digits(number))
