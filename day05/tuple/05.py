# Write a python function which accepts a list of numbers and returns true,
# if 1, 2, 3 appears in sequence in the list.
# Otherwise, it should return false.
 
# Sample Input
# [1, 1, 2, 3, 1]
# [1, 1, 2, 4, 3]
	
# Expected Output
# True
# False

def check_sequence(list):
    for i in range(0,len(list)):
        if list[i] == 1 and list[i + 1] == 2 and list[i + 2] == 3:
            return True
    return False




print(check_sequence([1, 1, 2, 3, 1]))
print(check_sequence([1, 1, 2, 4, 3]))


	