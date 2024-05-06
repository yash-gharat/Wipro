# Parameterless Constructor - Try out
 # Problem Statement
# You can create a constructor without parameters. But this is rarely useful.
# Run the below code and observe the output.
# Code in Python 3
class Mobile:
  def __init__(self):
    #   print("Inside constructor")
    pass
mob1=Mobile()
mob2=Mobile()
# print(mob1,mob2)
# Parameterized Constructor - Try out

# If a constructor takes parameters then it would be called as parameterized constructor.
 
# Run the below code and observe the output.
# Code in Python 3
 
class Mobile2:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand= brand
        self.price= price
    #string representation of an object
    def __str__(self):
        return f"Mobile 1 has brand name {self.brand} and price {self.price}"

mob1=Mobile2("Apple", 2000)
print(mob1)
mob2=Mobile2("Samsung",3000)
print(mob2)
# print("Mobile 1 has brand", mob1.brand, "and price", mob1.price)
# print("Mobile 2 has brand", mob2.brand, "and price", mob2.price)
 
 
class Student:
    def __init__(self,name,age,roll_no) -> None:
        self.name = name,
        self.age = age,
        self.roll_no = roll_no
    #if u want to display the object into the string
    def __str__(self):
        return f"Name : {self.name} rollNo :{self.roll_no} and age : {self.age}"
student1= Student("John",24,1)
student2= Student("David",23,2)

print(student1)
print(student2)