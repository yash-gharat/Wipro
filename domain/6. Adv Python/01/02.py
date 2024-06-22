my_list = [12,13,65,44,15,26,87,58,79]
is_even = lambda x : x % 2 == 0
is_odd = lambda x : x % 2 != 0

even_list = list(filter(is_even,my_list))
print("Even list: " ,even_list)
odd_list = list(filter(is_odd,my_list))
print("Odd list: " , odd_list)