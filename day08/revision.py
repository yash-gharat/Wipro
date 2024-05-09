# Q1 of 7outlined_flag
# What is the output of the following code snippet?
# class Parent:
#     def __init__(self,num):
#       self.__num=num
#     def get_num(self):
#       return self.__num
# class Child(Parent):
#     def __init__(self,num,val):
#       super().__init__(num)
#       self.__val=val
#     def get_val(self):
#       return self.__val
# son=Child(100,200)
# print(son.get_num())
# print(son.get_val())
 
# 100 200 x
# 200 100
# None 200

# Error: arguments cannot be passed through super() to the parent class constructor
# Q2 of 7outlined_flag
# What is the output of the following code snippet?
# class Parent:
#     def __init__(self):
#         self.num=100
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.var=200
#     def show(self):
#         print(self.num) #100
#         print(self.var) #200
# son=Child()
# son.show()
 
# None 200
# Error: A parent class instance variable cannot be accessed in a child class method
# 100 200 x
# Error: super() can invoke only parameterized constructor of a parent class


# Q3 of 7outlined_flag
# Consider the following python function for representing the customers of a retail store.5 min
# Objective of the code is to record the details of the customers.

# def customer_record(customer_type, name, discount, points_earned, membership_card_type):
#     if(customer_type=="Regular"):
#         record="Record Regular Customer:"+name+" "+(str)(discount)
#     elif(customer_type=="Privileged"):
#         record="Record Privileged Customer:"+name+" "+(str)(points_earned)
#     elif(customer_type=="Elite"):
#         record="Record Elite Customer:"+name+" "+membership_card_type
#     print(record)
# What will be the optimal class structure if this has to be re-written in Object oriented programming?
# 3 independent classes: Regular, Privileged, Elite
# 1 class: Customer
# 4 classes with inheritance: Base class: Customer; Child classes: Regular, Privileged; Grand Child of Privileged: Elite
# 4 classes with inheritance: Base class: Customer; Child classes: Regular, Privileged, Elite
# 4 classes with inheritance: Base class: Customer; Child classes: Regular, Privileged; Grand Child of Regular: Elite

# Q4 of 7outlined_flag
# What is the output of the following code snippet?
# class Parent:
#     def __init__(self):
#         self.__num=100
#     def show(self):
#         print("Parent:",self.__num)
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__var=10
#     def show(self):
#         print("Child:",self.__var)
# dad=Parent() 
# dad.show() #100
# son=Child()
# son.show() #10
# a) Child: 10
#     Child: 10
# b) Parent: 100
#     Parent: 100
# c) Error: Methods in parent and child classes cannot be same
# d) Parent: 100 x
#     Child: 10
# a
# b
# c
# d
# Q5 of 7outlined_flag
# What should be written in line 14 to get the output as mentioned below?4 min
# Parent: 100
# Child: 10
# class Parent:
#     def __init__(self):
#         self.__num=100
#     def show(self):
#         print("Parent:",self.__num)
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__var=10
#     def show(self):
#         _________________
#         print("Child:",self.__var)
# obj=Child()
# obj.show()
 
# show()
# super().show() x
# self.show()
# Parent.show()

# Q6 of 7outlined_flag
# What is the output of the below code?
# class Customer:
#     def __init__(self):
#         self.__cust_id = None
#         self.__cust_name = None
#     def get_cust_id(self):
#         print("Normal customer")
#     def get_cust_name(self):
#         return self.__cust_name
#     def set_cust_id(self, value):
#         self.__cust_id = value
#     def set_cust_name(self, value):
#         self.__cust_name = value
# class PrivilegedCustomer(Customer):
#     def __init__(self):
#         super().__init__()
#         self.__overdraft_limit = None
#     def get_overdraft_limit(self):
#         return self.__overdraft_limit
#     def set_overdraft_limit(self, value):
#         self.__overdraft_limit = value
#     def get_cust_id(self):
#         print("Privileged Customer")
# class RegularCustomer(Customer):
#     def __init__(self):
#         super().__init__()
#         self.__min_balance = None
#     def get_min_balance(self):
#         return self.__min_balance
#     def set_min_balance(self, value):
#         self.__min_balance = value
# r=RegularCustomer()
# p=PrivilegedCustomer()
# r.get_cust_id()
# p.get_cust_id()
# a) Normal Customer x
#     Privileged Customer
# b) Privileged Customer 
#     Normal Customer
# c) Error
# d) None of the above
# a
# b
# c
# d
# Q7 of 7outlined_flag
# For the given Customer class, what should be the subclasses so that the output of the code is:
#         Regular Customer
#         Normal Customer
#         Privileged Customer

# class Customer:
#     def __init__(self):
#         self.__cust_id = None
#         self.__cust_name = None
#     def get_cust_id(self):
#         print("Normal customer")
#     def get_cust_name(self):
#         return self.__cust_name
#     def set_cust_id(self, value):
#         self.__cust_id = value
#     def set_cust_name(self, value):
#         self.__cust_name = value
# Option A
# class PrivilegedCustomer(Customer):
#     def __init__(self):
#         super().__init__()
#         self.__overdraft_limit = None
#     def get_overdraft_limit(self):
#         return self.__overdraft_limit
#     def set_overdraft_limit(self, value):
#         self.__overdraft_limit = value
#     def get_cust_id(self):
#         print("Privileged Customer")
# class RegularCustomer(PrivilegedCustomer):
#     def __init__(self):
#         super().__init__()
#         self.__min_balance = None
#     def get_min_balance(self):
#         return self.__min_balance
#     def set_min_balance(self, value):
#         self.__min_balance = value
#     def get_cust_id(self):
#         print("Regular Customer")
# r=RegularCustomer()
# p=PrivilegedCustomer()
# n=Customer()
# r.get_cust_id() #RC
# p.get_cust_id()  #PC 
# n.get_cust_id()   #NC
# Option B 
# class PrivilegedCustomer(Customer):
#     def __init__(self):
#         super().__init__()
#         self.__overdraft_limit = None
#     def get_overdraft_limit(self):
#         return self.__overdraft_limit
#     def set_overdraft_limit(self, value):
#         self.__overdraft_limit = value
#     def get_cust_id(self):
#         print("Privileged Customer")
# class RegularCustomer(Customer):
#     def __init__(self):
#         super().__init__()
#         self.__min_balance = None
#     def get_min_balance(self):
#         return self.__min_balance
#     def set_min_balance(self, value):
#         self.__min_balance = value
#     def get_cust_id(self):
#         print("Regular Customer")
# r=RegularCustomer()
# p=PrivilegedCustomer()
# n=Customer()
# r.get_cust_id() #RC
# n.get_cust_id()   #NC
# p.get_cust_id()   #PC
 
# A
# B xx