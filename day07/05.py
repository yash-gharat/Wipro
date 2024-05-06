# Q1 of 2outlined_flag
# What will be the output of the code given below?
# class A:
#     def m1(self):
#         return 20
# class B(A):
#     def m1(self):
#         return 30
#     def m2(self):
#         return 40
# class C(B):
#     def m2(self):
#         return 20
# obj1=A()
# obj2=B()
# obj3=C()
# print(obj1.m1() + obj3.m1()+ obj3.m2())
 # 20 +30  +20
# Error: Method m1 should be overridden in class C.
# 80
# 70 x
# 90
# Q2 of 2outlined_flag
# What will be the output of the code given below?
# class A:
#     def m1(self):
#         return 20
# class B(A):
#     def m1(self):
#         val=super().m1()+30 #20 + 30
#         return val 
# class C(B):
#     def m1(self):
#         val=self.m1()+20 #Error 
#         return val
# obj=C()
# print(obj.m1())
 
# 70
# 20
# RunTimeError: Maximum recursion depth exceeded


# super() when u wan to access praent class method from child class use super()
class C1:
    def __init__(self):
        print("C1 constructor!!")
 
class C2(C1):
    def __init__(self):
        super().__init__()
        print("C2 constructor!!")
 
c2=C2()