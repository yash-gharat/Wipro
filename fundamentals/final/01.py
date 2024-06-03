# Problem Statement
# Implement a recursive method to generate the nth Fibonacci number.
# The Fibonacci series consists of the first two numbers as 0 and 1 and the subsequent numbers are the sum of the previous two numbers.
# Implement the logic inside findFibonacci() method.
# Fibonacci numbers – 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, … 
# Test the functionalities using the main method of the Tester class.                    
# Sample Input and
# 1
# 5
# Output
# 0
# 3

def findFibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return  findFibonacci(n-1) + findFibonacci(n-2)

print(findFibonacci(1))
print(findFibonacci(5))
