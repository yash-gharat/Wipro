## Day 03
```
Merge sort
Recursion
```
Merge Sort
```
The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, and then building the array back together the correct way so that it is sorted.
```
Divide 
Compare 1element of list1 with 1element of the list2
if A[i] < B[j] smaller push the code into another list
```
def merge(list):
    sorted_list=[]
    l=0
    h=len(list)-1
    mid=(l+h)//2
    i=l
    j=mid+1
    while(i<=mid and j<=h):
        if A[i]<A[j]:
            sorted_list.append(list[i])
            i=i+1
        else:
            sorted_list.append(list[j])
            j=j+1
    while i<=mid:
        sorted_list.append(list[i])
        i=i+1
    while(j<=h):
        sorted_list.append(list[j])
        j=j+1
    return sorted_list
```
Recurrsion - function calling itself
```
def factorial(n):
    if(n<=1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(12))
```
What is the output of the following code snippet?
def fun(number):
    if(number<2):
        return 1
    elif(number/2==2):
        return fun(number-1)
    else:
        return (number-1)*fun(number-1)
print(fun(7))

# Write a  program to find power of any number using recursion.
# Write a  program to print all natural numbers between 1 to n using recursion.
# Write a  program to print all even or odd numbers in given range using recursion.
# Write a  program to find sum of all natural numbers between 1 to n using recursion.
# Write a  program to find reverse of any number using recursion.
# Write a  program to find sum of digits of a given number using recursion.
# Write a  program to find factorial of any number using recursion
# Write a  program to generate nth Fibonacci term using recursion.
# Write a  program to find GCD (HCF) of two numbers using recursion.

