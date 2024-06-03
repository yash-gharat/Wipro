#even odd
#if number %2 ==0 then even
def isEven(number):
    if(number %2 == 0):
        return True
    else:
        return False

# res = isEven(1)
num = int(input("Enter a number: "))
if isEven(num):
    print(num, "is even.")
else:
    print(num, "is odd.")