# Inheritance - Introduction
 
# Types of phones
# Let us say that the online shopping app wants to sell different types of phones:
# Feature phones and Smartphones
# Class diagram
# The below are the class diagrams for both the classes:
# Common attributes & behaviors
# We can see that both the class have a lot in common. This is because they both are ultimately phones and each is just a special type of phone.
# In our example, FeaturePhone is inheriting the Phone and SmartPhone is inheriting the Phone class (SmartPhone "is-A" phone, FeaturePhone "is-A" phone). So Phone is the parent class and FeaturePhone and SmartPhone are derived classes.

# What are the advantages of inheritance?
# There are three main advantages of inheritance:
# We can keep common properties in a single place. Thus any changes needs to be made need not be repeated.
# Inheritance encourages code reuse thus saving us time.
# If we want to add a new type of phone later on, we can simply inherit the Phone class instead of writing it from scratch.
# Inheritance - Independent Classes - Try out
 
# Problem Statement
# Let us look at inheritance in code. For now we will create the Phone class with necessary attributes and methods. We will create FeaturePhone and SmartPhone classes without any attributes or methods now. We will create them later.
 
class Phone:
   def __init__(self, price, brand, camera):
       self.price = price
       self.brand = brand
       self.camera = camera
 
   def buy(self):
       print ("Buying a phone")
 
   def return_phone(self):
       print ("Returning a phone")
 
class FeaturePhone:
   pass
 
class SmartPhone:
   pass
 
Phone(10000,"Apple","13px").buy()
 
 
 
# Inheritance - Connecting Classes - Try out
# Problem Statement
# To create an inheritance relationship between the classes, mention the name of the parent class in brackets as shown:
 
class Phone:
   def __init__(self, price, brand, camera):
       self.price = price
       self.brand = brand
       self.camera = camera
 
   def buy(self):
       print ("Buying a phone")
 
   def return_phone(self):
       print ("Returning a phone")
 
class FeaturePhone(Phone):
   pass
 
class SmartPhone(Phone):
   pass
 
featurephone= FeaturePhone(10000,"Apple","13px")
featurephone.buy()
 
 
# What gets inherited?
 
# Inheriting Constructor - Try out 1
# Since the SmartPhone class is inheriting the Phone class, the SmartPhone class inherits the constructor of the Phone class.
 
# class Phone:
#    def __init__(self, price, brand, camera):
#        print ("Inside phone constructor")
#        self.price = price
#        self.brand = brand
#        self.camera = camera
 
#    def buy(self):
#        print ("Buying a phone")
 
#    def return_phone(self):
#        print ("Returning a phone")
 
# class FeaturePhone(Phone):
#    pass
 
# class SmartPhone(Phone):
#    pass
 
# s=SmartPhone(20000, "Apple", 13)
 
 
 
# Problem Statement
# Consider the below code. Since the SmartPhone class has its own constructor, the Phone class constructor is not inherited. Hence the attributes in the Phone class are also not inherited.
 
class Phone:
   def __init__(self, price, brand, camera):
       print ("Inside phone constructor")
       self.__price = price
       self.brand = brand
       self.camera = camera
 
   def buy(self):
       print ("Buying a phone")
 
   def return_phone(self):
       print ("Returning a phone")
 
class FeaturePhone(Phone):
   pass
 
class SmartPhone(Phone):
   def __init__(self, os, ram):
       self.os = os
       self.ram = ram
       print ("Inside SmartPhone constructor")
 
   def buy(self):
       print ("Buying a SmartPhone")
 
s=SmartPhone("Android", 2)
 
print(s.os)
print(s.brand)
 
 
# Problem Statement
# A child class cannot directly access the private attributes of the parent class.
# class Phone:
#    def __init__(self, price, brand, camera):
#        print ("Inside phone constructor")
#        self.__price = price
#        self.brand = brand
#        self.camera = camera
 
#    def buy(self):
#        print ("Buying a phone")
 
#    def return_phone(self):
#        print ("Returning a phone")
 
# class FeaturePhone(Phone):
#    pass
 
# class SmartPhone(Phone):
#    def check(self):
#        print(self.__price)
 
# s=SmartPhone(20000, "Apple", 13)
# s.check()
 
 
 
# Inheriting Methods - Try out
# Problem Statement
# Apart from attributes, the child class inherits the methods of the parent class as shown:
# class Phone:
#    def __init__(self, price, brand, camera):
#        print ("Inside phone constructor")
#        self.__price = price
#        self.brand = brand
#        self.camera = camera
 
#    def buy(self):
#        print ("Buying a phone")
 
#    def return_phone(self):
#        print ("Returning a phone")
 
# class FeaturePhone(Phone):
#    pass
 
# class SmartPhone(Phone):
#    pass
 
# s=SmartPhone(20000, "Apple", 13)
 
# s.buy()
 
 
 
# Method Overriding - Try out
 
# Problem Statement
# Sometimes a child may not want to use what it has inherited from the parent. The same holds true for OOP as well. If the child class does not want to use a method inherited from the parent class then it may create its own method with the same name.
# When the child has a method with the same name as that of the parent, it is said to override the parent’s method. This is called as Method Overriding. Method overriding is also called as Polymorphism.
 
# class Parent:
#    def purchaseBike(self):
#        print("Parent wants to purchase Hero Bike")
#    def marry(self):
#        print("Parent decided marry for our child with ABC")
#    def property(self):
#        print("Car+Gold+Money")
 
# class Child(Parent):
#    def purchaseBike(self):
#        print("Child wants to purchase R1-5 Bike")
#    def marry(self):
#        print("Child decided marry with PQR")
 
# c=Child()
# c.property()
# c.purchaseBike()
 
 
# class Sim:
#    def network(self):
#        print("default network!!")
# class Jio(Sim):
#    def network(self):
#        print("jio networl")
 
# class BSNL(Sim):
#    def network(self):
#        print("BSNL network")
 
# class Idea(Sim):
#    def network(self):
#        print("Idea network")
 
# s1=Jio()
# s1.network()
# s2=BSNL()
# s2.network()
# s3=Idea()
# s3.network()
 
# class Phone:
#    def __init__(self, price, brand, camera):
#        print ("Inside phone constructor")
#        self.__price = price
#        self.brand = brand
#        self.camera = camera
 
#    def buy(self):
#        print ("Buying a phone")
 
#    def return_phone(self):
#        print ("Returning a phone")
 
# class FeaturePhone(Phone):
#    pass
 
# class SmartPhone(Phone):
#    def buy(self):
#        print ("Buying a smartphone")
 
# s=SmartPhone(20000, "Apple", 13)
 
# s.buy()
# Single Level Inheritance - Single parent and single child

# Multilevel Inheritance - C1(GrandPArent) - C2(Parent) - C3(Child)

#Multiple Inheritance - child having multiple parent

# Hirarichel Inheritance - Serveral class derived from common class