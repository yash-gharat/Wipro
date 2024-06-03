# Write a  program to find sum of all natural numbers between 1 to n using recursion.

#fn(n)
# Check if(n==1) =>return 1
# else  fn(n-1)  + n


def add_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + add_natural_numbers(n - 1)

n = 10
result = add_natural_numbers(n)
print("Sum of natural numbers from 1 to", n, "is:", result)

