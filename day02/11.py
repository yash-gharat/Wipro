# Write a program to input and sort the weight of ten people. 
# Sort and display them in descending order using the selection sort technique.
# 95.7,59.6, 91.0,84.9,76.2,65.3,95.4

def selection_sort_weights(list):
    for i in range(0, len(list)):
        #assume max
        max = list[i]
        pos = i
        for j in range(i + 1, len(list)):
            #Compare
            if list[j] > max:
                max = list[j]
                pos = j
        #Swap
        list[pos] = list[i]
        list[i] = max
    return print("sORTED_WEIGHTS :",list)

list = [95.7,59.6, 91.0,84.9,76.2,65.3,95.4]
selection_sort_weights(list)

