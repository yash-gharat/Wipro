def merge_sort(list_1,list_2):
    m=len(list_1)
    n=len(list_2)
    list_3 = []
    i=j=0
    while (i < m and j < n ):
        if list_1[i] < list_2[j]:
            list_3.append(list_1[i])
            i = i + 1
        else:
            list_3.append(list_2[j])
            j = j +  1
    while(i < m):
        list_3.append(list_1[i])
        i = i +  1
    while(j < n):
        list_3.append(list_2[j])
        j = j +  1
    return print(list_3)

list1=[2,10,18,20,23]
list2=[4,9,19,25]
merge_sort(list1,list2)
