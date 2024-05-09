# Problem Statement
# Implement a recursive method to find the sum of the Harmonic Progression given below.  
# 1+1/2+1/3+1/4+1/5+1/6+…+1/n
# Implement the logic inside findHPSum() method. You need to find the sum based on the value of num passed to the method.
# E.g. - If the value of num is 3, you need to find the sum of 1+1/2+1/3.
# Test the functionalities using the main method of the Tester class. 
 
# Sample Input and 
#  3
#  6
# Output
#  1.8333333
# 2.44999999997

def findHPSum(n):
    if n == 1:
        return 1
    else:
        print(n)
        return((1 / n )+ findHPSum(n-1))
        
print(findHPSum(3))
print(findHPSum(6))