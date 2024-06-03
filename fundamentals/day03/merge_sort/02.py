def merge_sort(list):
    # list1=[2,10,18,20,23]
    print("Unsorted list",list)
    #mid = 2
    mid = len(list) // 2
    #Dividing the list into 2 parts
    #[2,10]
    left_half = list[:mid]
    #[18,20,23]
    right_half = list[mid:]   
    length_of_left_list = len(left_half) 
    length_of_right_list = len(right_half) 
    merged = []
    i = j = 0
    while i < length_of_left_list and j < length_of_right_list:
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i = i + 1
        else:
            merged.append(right_half[j])
            j = j + 1
    while i < length_of_left_list:
        merged.append(left_half[i])
        i += 1
    while j < length_of_right_list:
        merged.append(right_half[j])
        j += 1
    print("Sorted list",merged)

list1=[2,21,10,21,18,23]
merge_sort(list1)

# def merge(A,l,mid,h):
#     B=[]
#     i=l
#     j=mid+1
#     k=l
#     while(i<=mid and j<=h):
#         if A[i]<A[j]:
#             B.append(A[i])
#             i=i+1
#         else:
#             B.append(A[j])
#             j=j+1
#     while i<=mid:
#         B.append(A[i])
#         i=i+1
#     while(j<=h):
#         B.append(B[j])
#         j=j+1
#     return B
