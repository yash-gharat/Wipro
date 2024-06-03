# Let’s compare selection sort and bubble sort algorithms in this exercise.
# Combine the selection sort and bubble sort programs as per the template code provided below and display the number of passes for each of them.
# Invoke both the functions (selection_sort() and bubble_sort()) using the following two lists and observe the results.

# Case 1: [8,2,19,34,23, 67, 91]

# Case 2: [91,8,19,23,34,67,2]
# Code in Python 3


# #lex_auth_0127667385791856643328

def swap(num_list, first_index, second_index):
    num_list[first_index], num_list[second_index] = num_list[second_index], num_list[first_index]

def find_next_min(num_list,start_index):
    min_index = start_index
    for i in range(0,len(num_list)):
        if num_list[i] < num_list[min_index]:
            min_index = i
    return min_index

def selection_sort(num_list):
    total_passes = 0
    for i in range(0,len(num_list)):
        min_index = find_next_min(num_list, i)
    swap(num_list, i, min_index)
        # total_passes += 1
    total_passes = total_passes + 1
    return print("Total Selection sort passes",total_passes)

def bubble_sort(num_list):
    total_passes = 0
    len(num_list)
    for i in range(0,len(num_list)):
        swapped = False
        for j in range(0, len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                swap(num_list, j, j+1)
                swapped = True
        # total_passes += 1
        total_passes = total_passes + 1
        if not swapped:
            break
    return print("Total Bubble sort passes",total_passes) 
    
my_list = [8,2,19,34,23, 8,67, 91]
selection_sort(my_list)
bubble_sort(my_list)