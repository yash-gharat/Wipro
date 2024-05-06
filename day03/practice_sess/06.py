# Write a  program to find factorial of any number using recursion

def factorial(number):
    if number <= 1 :
        return 1
    else:
        return (factorial(number-1) * number)


print(factorial(10))