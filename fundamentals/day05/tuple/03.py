# Given a list of numbers, write a python function which returns true 
# if one of the first 4 elements in the list is 9. Otherwise it should return false.
# The length of the list can be less than 4 also.
 
# Sample Input
# [1, 2, 9, 3, 4]
# [1, 2, 9]
# [1, 2,3,4]
	
# Expected Output
# True
# True
# False


	
# Code in Python 
def find_nine(nums):
    #Remove pass and write your code here
    return 9 in nums[:4]

# nums=[1,9,4,5,6]
nums=[1,4,5,6,8,7,9]
print(find_nine(nums))
