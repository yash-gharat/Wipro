# merge_Sort using recursion
def merge_sort(list):
    sorted_list = []
    if len(list) > 1:
        mid = len(list) // 2
        left_half = list[:mid]
        print("first",left_half)
        right_half = list[mid:]
        print("second",right_half)
        # lenght of left list
        m = len(left_half)
        # lenght of right list
        n = len(left_half)
        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = 0

        while i < m and j < n:
            if left_half[i] < right_half[j]:
                sorted_list.append(left_half[i])
                i += 1
            else:
                sorted_list.append(right_half[j])
                j += 1
        # Check if any elements are left
        while i < m:
            sorted_list.append(left_half[i])
            i += 1


        while j < n:
            sorted_list.append(right_half[j])
            j += 1

    return sorted_list

# list1 = [2, 21, 10, 21, 18, 23]
# print("Unsorted list:", list1)
# sorted_list = merge_sort(list1)
# print("Sorted list:", sorted_list)

def fun(number):
    if(number<2):
        return 1
    elif(number/2==2):
        return fun(number-1)
    else:
        return (number-1)*fun(number-1)
# print(fun(7))

def fun(number):
    if(number <=  0):
        return 
    x= number - 1
    fun(x)
    print(x)
    x = x-1
    fun(x)
    
print(fun(4))
    