# Write a program to perform binary search on a list of integers given below, 
# to search for an element input by the user. 
# If it is found display the element along with its position,
# otherwise display the message "Search element not found".
# 5, 7, 9, 11, 15, 20, 30, 45, 89, 97

def binary_search(list,number):
    
    low = 0
    high = len(list) - 1
    while low <= high:
        mid=(low + high) // 2
        if(number > list[mid]):
            low = mid+1
        elif(number < list[mid]):
            high = mid-1
        else:
            print("Search element found")
            return
     
    print("Search element Not found")


list = [5, 7, 9, 11, 15, 20, 30, 45, 89, 97]
num = 5

res = binary_search(list, num)