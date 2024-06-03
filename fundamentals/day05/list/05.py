# Assignment on List - Level 2 
# Problem Statement
# Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers. 
# Note: Assume that all the numbers are two digit numbers.
# Sample Input
# 23,34,55
# Expected Output
# 553423

def create_largest_number(number_list):
    number_list.sort(reverse=True)
    # number_list.reverse()
    print(number_list)
    test = ""
    for i in range(len(number_list)):
        # print(number_list[i])
        string = str(number_list[i])
        test += string
        # print(test)
    print(test)    
    #remove pass and write your logic here
 
number_list=[23,45,67,21]
create_largest_number(number_list)


# def create_largest_number(number_list):
#     number_list.sort(reverse=True)  
#     largest_number = ''.join(str(num) for num in number_list)
#     return largest_number
 
# number_list = [23, 45, 67,21]
# number_lise_2 = [23,34,55]
# # largest_number = create_largest_number(number_list)
# largest_number = create_largest_number(number_lise_2)
# print(largest_number)