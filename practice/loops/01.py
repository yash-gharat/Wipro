# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count = 0
for i in range(len(numbers)):
    # print(numbers[i])
    if(numbers[i] > 0):
        count += 1
print(count) 