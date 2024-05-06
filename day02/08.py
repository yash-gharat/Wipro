def selection_sort(list):
    for i in range(0, len(list)):
        #min
        min = list[i]
        pos = i
        for j in range(i + 1, len(list)):
            #Compare
            if list[j] < min:
                min = list[j]
                # print(min)
                pos = j
        #Swap
        list[pos] = list[i]
        list[i] = min
    return list

list = [5, 2,5, 1, 8]
sorted_list = selection_sort(list)
print(sorted_list)
