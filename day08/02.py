# Q1 of 6outlined_flag
# What is the output of the following code snippet?
# from abc import ABCMeta, abstractmethod
# class Parent(metaclass=ABCMeta):
#     def __init__(self):
#         # print(self)
#         self.num=100
#     @abstractmethod
#     def show(self):
#         pass
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__var=10
#     def show(self):
#         print(self.num)
#         print(self.__var)
# obj=Parent()
# obj.show()
# a) 100
#     10
# b) 10
#     100
# c) Error: abstract method should always have a valid statement other than pass
# d) Error: abstract class cannot be instantiated
# a
# b
# c
# d x