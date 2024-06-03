# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.


num = 5
fact = 1
while num>0:
    fact *= num
    num -= 1
    print(num,fact)