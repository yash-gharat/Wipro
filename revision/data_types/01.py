# # #return smallest positive integer>0 from the list
# # x= None
# # print(x)

# # x=10
# # y=20
# # print("xis{} y is{}".format(y,x))

# # my =[1,2,3]
# # my.insert(1,4)
# # print(6 in my)

# # message = "hello {}"
# # name= "Alice"
# # print(message.format(name))

# # my =[1,2,3,4,5]
# # print(my[1:4])

# # test = "Python is easy"
# # print(test.find("is"))

# # dict_1 ={"a":1,"b":2}
# # for key in dict_1:
# #     print(key)

# print(range(5))



# def test_single_pair():
#     assert tuple_pair_finder((1, 2, 3, 4), 5) == [(2, 3), (1, 4)]


# def test_no_pair():
#     assert tuple_pair_finder((1, 2, 3, 4), 8) == []


# def test_multiple_pairs():
#     assert tuple_pair_finder((1, 2, 3, 2, 1), 3) == [(1, 2), (1, 2),(2,1)]


# def test_with_negative_numbers():
#     assert tuple_pair_finder((-1, -2, -3, 4), 1) == [(-3, 4)]


# def test_with_zero():
#     assert tuple_pair_finder((0, 1, 2, 3, -3), 0) == [(3, -3)]


# def test_tuple_with_repeated_numbers():
#     assert tuple_pair_finder((2, 2, 2), 4) == [(2, 2), (2, 2)]


# def test_empty_tuple():
#     assert tuple_pair_finder((), 5) == []


# def test_all_zeroes_tuple():
#     assert tuple_pair_finder((0, 0, 0, 0), 0) == [(0, 0), (0, 0), (0, 0)]

# def tuple_pair_finder(numbers, target_sum):
#     num_set = set(numbers)
#     found_pairs = set()

#     for num in numbers:
#         complement = target_sum - num
#         if complement in num_set:
#             pair = tuple(sorted([num, complement]))  # Ensure the pair is sorted
#             found_pairs.add(pair)

#     return sorted(found_pairs)  # Sort the found pairs before returning

# Test the function with the provided test cases
# print(tuple_pair_finder((1, 2, 3, 4), 5)) #== [(1, 4), (2, 3)]
# tuple_pair_finder((1, 2, 3, 4), 8) #== []
# tuple_pair_finder((1, 2, 3, 2, 1), 3) #== [(1, 2)]
# tuple_pair_finder((-1, -2, -3, 4), 1) #== [(-3, 4)]
# tuple_pair_finder((0, 1, 2, 3, -3), 0) #== [(-3, 3)]
# tuple_pair_finder((2, 2, 2), 4) #== [(2, 2)]
# print(tuple_pair_finder((), 5)) #== []
# print(tuple_pair_finder((0, 0, 0, 0), 0)) #== [(0, 0), (0, 0), (0, 0)]

# print("All test cases passed successfully!")

def tuple_pair_finder(numbers, target_sum):
    numbers = sorted(numbers)
    left = 0
    right = len(numbers) - 1
    found_pairs = []

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target_sum:
            # Special case: if both numbers are zeros, return all possible pairs of zeros
            if numbers[left] == numbers[right] == 0:
                found_pairs.extend([(0, 0)] * (right - left + 1))
                break
            found_pairs.append((numbers[left], numbers[right]))
            left += 1
            right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1


    return sorted(found_pairs)  # Sort the found pairs before returning

# Test the function with the provided test cases
print(tuple_pair_finder((1, 2, 3, 4), 5)) #== [(1, 4), (2, 3)]
print(tuple_pair_finder((1, 2, 3, 4), 8)) #== []
print(tuple_pair_finder((1, 2, 3, 2, 1), 3)) #== [(1, 2)]
print(tuple_pair_finder((-1, -2, -3, 4), 1)) #== [(-3, 4)]
print(tuple_pair_finder((0, 1, 2, 3, -3), 0)) #== [(-3, 3)]
print(tuple_pair_finder((2, 2, 2), 4)) #== [(2, 2)]
print(tuple_pair_finder((), 5)) #== []
print(tuple_pair_finder((0, 0, 0, 0), 0)) #== [(0, 0), (0, 0), (0, 0)]
