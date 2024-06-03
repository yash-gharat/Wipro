# Write a  program to generate nth Fibonacci term using recursion.

# 0,1,1,2,3,5,8
def fibonacci(n):
    if n <= 1 :
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


print(fibonacci(5))
