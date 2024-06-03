# Data Types

- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dictionary : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)
- Set : set('abc'), {'a', 'b', 'c'}
- Boolean : True, False
- None : None

# Conditional statements
- if-else
- if-elif-else

## Questions

<details>
<summary>1. Age Group Categorization
</summary>
Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

```
def check_age(age):
    if(age <= 13):
        return "Child"
    elif (13<=age <=19):
        return "Teenager"
    elif 20 <=age <= 59:
        return "Adult"
    elif age >= 60:
        return "Senior"
```

</details>

<details>
<summary>2. Movie Ticket Pricing
</summary>
Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

```
def movie_ticket_price(age,day):
    adult_ticket_price = 12
    child_ticket_price = 8
    
    if(day.lower() == "wednesday"):
        if(age >= 18):
            adult_ticket_price -= 2
            return adult_ticket_price
        else:
            child_ticket_price -= 2
            return adult_ticket_price
    else :
        return (f"adult : {adult_ticket_price} \n child : {child_ticket_price}")
    
```
</details>

<details>
<summary>3. Grade Calculator
</summary>
Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

```
def assign_grade(grade):
    if 90<= grade <= 100:
        return "A"
    elif 80<= grade <= 89:
        return "B"
    elif 70<= grade <= 79:
        return "C"
    elif 60<= grade <= 69:
        return "D"
    elif grade < 60:
        return "F"
```
</details>

<details>
<summary>4. Fruit Ripeness Checker
</summary>
Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

</details>

<details>
<summary>5. Weather Activity Suggestion
</summary>
Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

</details>

<details>
<summary>6. Transportation Mode Selection
</summary>
Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

</details>


<details>
<summary>7. Coffee Customization
</summary>
Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

```
order = input("Enter your order \n").lower()
extra_shot = bool(int(input("Extra shot of expresso 0 or 1 \n")) )

print(extra_shot)

if(extra_shot == True ):
    print(f"{order} coffee with extra shot ")
else:
    print(f"{order} coffee without extra shot ")
    
```
</details>


<details>
<summary>8. Password Strength Checker
</summary>
Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

</details>


<details>
<summary>9. Leap Year Checker
</summary>
Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

```
def check_leap_year(year):
    if((year % 4 == 0)and(year % 100 != 0) or year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a leap year"
print(check_leap_year(2005))
```
</details>


<details>
<summary>10. Pet Food Recommendation
</summary>
Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

```
species = input("Enter the species of the pet \n").upper()
age = int(input("Enter the pets age \n"))

if(species == "DOG"):
    if(age <= 2):
        print("Puppy food")
elif(species == "CAT"):
    if(age >= 5):
        print("Senior cat food")
else:
    print("Enter the valid species")
```

</details>


# Loops
- for loop
- while loop

## Questions

# Loops in Python

<details>
<summary>
1. Counting Positive Numbers
</summary>
Problem: Given a list of numbers, count how many are positive.

```python
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
```
```python
def positive_numd(list):
    positve_list = []
    for i in range(len(list)):
        print(list[i])
        if list[i] > 0:
            positve_list.append(list[i])
    return positve_list
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
print(positive_numd(numbers))

```

</details>


<details>
<summary>
2. Sum of Even Numbers
</summary>
Problem: Calculate the sum of even numbers up to a given number n.

</details>


<details>
<summary>
3. Multiplication Table Printer
</summary>
Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

</details>


<details>
<summary>
4. Reverse a String
</summary>
Problem: Reverse a string using a loop.

```
def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("yash"))
```
</details>


<details>
<summary>
5. Find the First Non-Repeated Character
</summary>
Problem: Given a string, find the first non-repeated character.

```
number = 5
fact = 1
while number > 0:
    fact *= number
    number -=1
print(fact)
```
</details>


<details>
<summary>
6. Factorial Calculator
</summary>
Problem: Compute the factorial of a number using a while loop.

```
number = 5
fact = 1
while number > 0:
    fact *= number
    number -=1
print(fact)
```

</details>


<details>
<summary>
7. Validate Input
</summary>
Problem: Keep asking the user for input until they enter a number between 1 and 10.

```
while True:
    number = int(input("Enter : "))
    if 1<= number <=10:
        print("ThankYou")
    else:
        print("Try again")
```
</details>


<details>
<summary>
8. Prime Number Checker
</summary>
Problem: Check if a number is prime.

```
number = 28

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
print(is_prime)
```

</details>


<details>
<summary>
9. List Uniqueness Checker
</summary>
Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

```python
items = ["apple", "banana", "orange", "apple", "mango"]

def check_duplicate(list):
    unique_items = set()
    for item in range(len(list)):
        print(list[item])
        if item in unique_items:
            break
        else:
            unique_items.add(list[item])
    return unique_items


items = ["apple", "banana", "orange", "apple", "mango"]
print(check_duplicate(items))

```
</details>


<details>
<summary>
10. Exponential Backoff
</summary>
Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

```python

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1

```
</details>

# Data structure and algorithm

1. Linear search algorithm

```python
def linear_search(list,target):
    for i in range(0,len(list)): 
        if(list[i] == target):
            return "Target found"
    return "Target Not found"

my_list = [4, 2, 7, 1, 9, 5]
target_element = 76
print(linear_search(my_list, target_element))
```
2. Binary search algorithm(neads sorted array)

```python
def binary_search(list,target):
    high = len(list) - 1
    low = 0
    
    while low <= high:
        mid = (high + low)//2
        if list[mid] == target:
            return mid
        elif target > list[mid]:
            low = mid + 1
        elif target < list[mid]:
            high = mid - 1
    return -1

my_list = [1, 3, 5, 7, 9, 11, 13]
target_element = 76
print(binary_search(my_list, target_element))
```

3. Selection sort algorithm

```python
def selection_sort(list):
    n = len(list)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if list[j] < list[min_index]:
                min_index = j
        # Swap the smallest element with the first element of the unsorted portion
        list[i], list[min_index] = list[min_index], list[i]
    return list

my_list = [64, 25, 12, 22, 11]
print("Original list:", my_list)
selection_sort(my_list)
print("Sorted list:", my_list)
```
4. Merge sort algorithm

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call to merge_sort for each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
my_list = [64, 25, 12, 22, 11]
print("Original list:", my_list)
merge_sort(my_list)
print("Sorted list:", my_list)
```
5. Bubble sort algorithm

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize if the array is already sorted
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

my_list = [64, 25, 12, 22, 11]
print("Original list:", my_list)
bubble_sort(my_list)
print("Sorted list:", my_list)

```
6.Stack(LILO)
7.Queue(FIFO)
8.Linked list
9.Graph (google_maps)
10. Tree(herarical)

# OOPS

1. Classes
2. Objects

