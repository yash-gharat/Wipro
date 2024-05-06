# def linear_search(lst, num):
#     flag = False
#     for i in range(0, len(lst)):
#         if lst[i] == num:
#             flag = True
#             break
#     return flag
def linear_search(list, target):
    flag = False
    for i in range(len(list)):
        if list[i] == target:
            flag = True
            return print("Element found in the list.")       
    return print("Element not found in the list.")  

my_list = [1, 2, 3, 4, 5]
num = 56

# res = linear_search(my_list, num)
linear_search(my_list, num)
num = 5
linear_search(my_list,num)
# if res == True:
#     print("Element Found")
# else:
#     print("Element Not Found")
