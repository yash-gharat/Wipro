# Day 02

## DataTypes

- Normal variable can hold single value
- List - [10,20,30,40,50]

- Function - block to execute particular task

```
# syntax
def function_name():
    statement1
    statement2

```

- Example

```
def add(a,b):
print("result = ",a+b)

# calling a function
add(1,3) //output : result =  4
```

# Algorithms

### 1. Searching Algorithm

**Searching algorithms are used to find a specific target element within a collection of data.**

1.  **Linear Search Algorithm -
    Linear search is a simple searching algorithm that checks every element in a list or array until the desired element is found or the end of the list is reached.**

```
function linear_search(array, target):
    for each item in the array:
        if item equals target:
            return index of item
    return -1  //target not found
```

Q1. Guessing game

```
def linear_search(list, target):
    flag = False
    for i in range(len(list)):
        if list[i] == target:
            flag = True
            return print("Element found in the list.")
    return print("Element not found in the list.")

my_list = [1, 2, 3, 4, 5]
num = 56
linear_search(my_list, num)
num = 5
linear_search(my_list, num)

#Output:-
Element not found in the list.
Element found in the list.
```

2.  **Binary Search Algorithm - Binary search is a searching algorithm that finds the position of a target value within a sorted array. It compares the target value to the middle element of the array and continues the process recursively on the sub-array containing the target value until the position is found or the sub-array becomes empty.**

```
def binary_search(arr, target):
    left = 0
    right = length of arr - 1

    while left <= right:
        mid = (left + right) / 2

        if arr[mid] equals target:
            return mid // target found at index mid
        else if arr[mid] < target:
            left = mid + 1 // search in the right half
        else:
            right = mid - 1 // search in the left half

    return -1 // target not found

```

**Q1.
Using the binary search strategy of having numbers in sorted order, if you have to find 25 from a list containing numbers from 1 to 50 arranged in ascending order,how many guesses do you have to make?<br>
0 <br>
1 :white_check_mark: <br>
25<br>
50**

**Q2.
Using the binary search strategy of having numbers in sorted order, if you have to find 50 from a list containing numbers from 1 to 50 arranged in ascending order, how many guesses do you have to make?<br>
6 :white_check_mark: <br>
8<br>
4<br>
2**

**Q3.
Do you think the number of guesses to be made is equal to the position of the number to be guessed?<br>
Yes<br>
No** :white_check_mark:

### 2. Sorting Algorithms

**Sorting data in ascending or descending order.**

1. **Selection Sort Algorithm - Selection sort divides the input list into two parts: a sorted sublist and an unsorted sublist. It repeatedly selects the smallest (or largest) element from the unsorted sublist and moves it to the end of the sorted sublist.**

2. **Bubble Sort: This algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process repeats until the list is sorted.**



    -Selection sort - arranging items into accessinding or decending order
    Q. nums = [5,8,9,10,7,1]

    find
    compare
    swap

Q1 of 1outlined_flag
You have just learnt the selection sort algorithm to sort a list of elements in ascending order.
Options

- What changes should be made in the algorithm to sort the elements in descending order?
- Find the smallest element and swap it with the element at the first position in the list
- Find the largest element and swap it with the element at the first position in the list check
- Use the same algorithm, sort the elements in ascending order, finally reverse the elements in the list
- Find the largest element and swap it with the element at the last position in the list

QWrite a python program that displays a message as follows for a given number:
If it is a multiple of three, display "Zip"
If it is a multiple of five, display "Zap".
If it is a multiple of both three and five, display "Zoom".
If it does not satisfy any of the above given conditions, display "Invalid".

QWrite a program to perform binary search on a list of integers given below, to search for an element input by the user. If it is found display the element along with its position, otherwise display the message "Search element not found".
5, 7, 9, 11, 15, 20, 30, 45, 89, 97

Write a program to input and sort the weight of ten people. Sort and display them in descending order using the selection sort technique.

## Bubble sort

incase of bubble sort
compare adjecent element and swap
Question

- Consider the list of numbers given below:
  num_list = [ 67,34,8,22,23]
  How many passes bubble sort algorithm will go through to sort the numbers in the above list in ascending order?
  1
  3
  4
  7

```
67,34,8,22,23
34,67,8,22,23
34,8,67,22,23
34,8,22,67,23
34,8,22,23,67,
8,34,22,23,67,
8,22,34,23,67,
8,22,23,34,67,
```

Size = size - 1
for i in range(0,len(list))
for j in range(0,leng(list)-i-1)
if list[j]>list[i+1]
temp = list[j]
list[j] = list[j+1]
list[j+1] = temp

[89,43,99,55,87,67]
[43,89,99,55,87,67]

[43,89,99,55,87,67]
[43,89,55,99,87,67]
[43,89,55,87,99,67]
[43,89,55,87,67,99]

[43,89,55,87,67,99]
[43,55,89,87,67,99]
[43,55,87,89,67,99]
[43,55,87,67,89,99]

[43,55,87,67,89,99]
[43,55,67,87,89,99]

Now take a step-by-step look at what’s happening with the array as the algorithm progresses:
The code starts by comparing the first element, 8, with its adjacent element, 2. Since 8 > 2, the values are swapped, resulting in the following order: [2, 8, 6, 4, 5].
The algorithm then compares the second element, 8, with its adjacent element, 6. Since 8 > 6, the values are swapped, resulting in the following order: [2, 6, 8, 4, 5].
Next, the algorithm compares the third element, 8, with its adjacent element, 4. Since 8 > 4, it swaps the values as well, resulting in the following order: [2, 6, 4, 8, 5].
Finally, the algorithm compares the fourth element, 8, with its adjacent element, 5, and swaps them as well, resulting in [2, 6, 4, 5, 8]. At this point, the algorithm completed the first pass through the list (i = 0). Notice how the value 8 bubbled up from its initial location to its correct position at the end of the list.
The second pass (i = 1) takes into account that the last element of the list is already positioned and focuses on the remaining four elements, [2, 6, 4, 5]. At the end of this pass, the value 6 finds its correct position. The third pass through the list positions the value 5, and so on until the list is sorted.

# Linear Search Alorithm

# Binary Search Alorithm

