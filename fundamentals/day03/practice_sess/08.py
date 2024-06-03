# Write a  program to find GCD (HCF) of two numbers using recursion.

def gcd_recursive(a, b):
    # print(a,b)
    if b == 0:
        return a
    else:
        # print("text %", a%b)
        return gcd_recursive(b, a % b)

num1 = 20
num2 = 28
print(gcd_recursive(num1,num2))