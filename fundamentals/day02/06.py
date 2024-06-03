def binary_search(lst, num):
    flag = False
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if num > lst[mid]:
            low = mid + 1
        elif num < lst[mid]:
            high = mid - 1
        else:
            flag = True
            break

    return flag

my_list = [1, 2, 3, 4, 5]
num = 5

res = binary_search(my_list, num)
if res:
    print("Element found")
else:
    print("Element not found")
