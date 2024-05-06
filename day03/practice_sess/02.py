# Write a  program to print all even or odd numbers in given range using recursion.
# fn(start,end,[even],[odd])
#check for even
#   add to even[]
#check for odd
#   add to odd[]
#Recurrsion(start != end)=> Run fn fn(start+1,end,[even],[odd])
#Repeat

def even_odd(start,end,even_list = [],odd_list = []):
    # even_list = []
    # odd_list = []

    if(start % 2 == 0):
        even_list.append(start)
    elif(start % 2 != 0):
        odd_list.append(start)
    if(start != end):
        even_odd(start+1,end,even_list,odd_list)
    return even_list,odd_list

print(even_odd(1,5))
