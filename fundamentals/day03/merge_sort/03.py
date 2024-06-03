# # Slicing
# A = [1,2,3,4,5,6,7]
# B = A[5:]
# print(B) #B = [6,7]

def m1(n):
    if(n==0):
        return
    print("hello",n-1)
    m1(n-1)

def factorial(n):
    if(n<=1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(12))


def func(n):
    if n == 0:
        return 1
    result = func(n - 1)
    # print(result)
    return result * n

# print(func(12))
