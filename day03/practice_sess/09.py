# Write a  program to find power of any number using recursion.

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent - 1)

base =2
exponent = 2
print(power(base, exponent))