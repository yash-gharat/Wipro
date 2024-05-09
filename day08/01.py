# from abc import ABCMeta
# class Shape(metaclass=ABCMeta):
#     def aera(self):
#         pass
 
# class Rectangle(Shape):
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def aera(self):
#         return self.length*self.breadth
 
# class Square(Shape):
#     def __init__(self,side):
#         self.side=side
#     def aera(self):
#         return self.side*self.side
   
 
# s1=Rectangle(10,20)
# res=s1.aera();
# print('Rectangle Aera= ',res)
# s2=Square(10)
# res=s2.aera()
# print('Sqaure Aera= ',res)

from abc import ABCMeta,abstractmethod
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def aera(self):
        pass
 
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def aera(self):
        return self.length*self.breadth
 
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def aera(self):
        return self.side*self.side
   
 
s1=Rectangle(10,20)
res=s1.aera();
print('Rectangle Aera= ',res)
s2=Square(10)
res=s2.aera()
print('Sqaure Aera= ',res)