# List Comprehensions
squares = [x**2 for x in range(10)]
print(squares)


# Creating an Iterator:
def multiple(num):
    return num * num


my_list = [1, 2, 3]
my_iter = iter(my_list)


# print(next(my_iter))  # Output: 1
# print(next(my_iter))  # Output: 2
# print(next(my_iter))  # Output: 3

print(multiple(next(my_iter)))  # Output: 1
print(multiple(next(my_iter)))  # Output: 4
print(multiple(next(my_iter)))  # Output: 9

# Creating a Generator
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# Creating and Using Decorators:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.


# Understanding Lambda Functions
# lambda arguments: expression

# Lambda function to add 10 to the input
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

from functools import reduce

numbers = [1, 2, 3, 4]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # Output: 10

numbers = [1, 2, 3, 4]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

