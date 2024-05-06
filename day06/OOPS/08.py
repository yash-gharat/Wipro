#Recap

class Student:
    def __init__(self,id,name,grade):
        self.id = id
        self.name = name
        self.grade = grade

student1 = Student(1,"John","A")
student2 = Student(2,"David","C")

# print(f"Id : {student1.id} Name : {student1.name} Grade : {student1.grade} " )
# print(f"Id : {student2.id} Name : {student2.name} Grade : {student2.grade} " )


# What is the output of the below code snippet?
# class Example:
#     def __init__(self,num):
#         self.num=num
#     def set_num(self,num):
#         self.num=num
#     def get_num(self):
#         return self.num
# obj=Example(10)
# print(obj.get_num()) 
# obj.set_num(15)
# print(obj.get_num())
# a. 10
#     10
# b. 10
#     15
# c. Error: constructor cannot accept a value
# a
# b x
# c

# What is the output of the following code snippet?
# class Customer:
#     def __init__(self):
#         cust_id = 100
# c1=Customer()
# print(c1.cust_id)
 
# 100
# Error x
# None

# [09:18 am] Ashutosh  (Unverified)
# What is the output of the following code snippet?
# class Customer:
#     def __init__(self):
#         self.id = 100
# c1=Customer()
# print(c1.id)
 
# 100 x
# Error 
# None

# What is the output of the following code snippet?
# class Customer:
#     def __init__(self,id1):
#         self.id = id1
# c1=Customer(200)
# print(c1.id)
 
# 200 x
# Error
# None