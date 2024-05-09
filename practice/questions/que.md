Polymorphism
The process of representing one Form in multiple forms is known as Polymorphism.
Poly
morphism is derived from 2 Greek words: poly and morphs. The word "poly" means many and "morphs" means forms. So, polymorphism means many forms.
 
Real Time Polymorphism Example
 
Here we take an example of a person to understand polymorphisms Concept.
There are many ways to behaves a person in different context.
 
Suppose if Person is in class room that time a person behaves like a student in school. When the person is in the market that time a person behaves like a passenger in train or bus. When the person is at the home that time a Person Behaves Like A Child at Home. When the person is in the market that time A person behaves like a customer in a shopping mall.
 
Here one person presents in different-different behaviors
 
 
 
Polymorphism means that when one person behaves in many ways in different context.
In the same way we can say that when one method, behaves in different ways in different classes.
Polymorphism In Python
Polymorphism with Function and Objects: -
In Python we cannot specify the type explicitly. Based on provided value at runtime the type will be considered automatically. Hence Python is considered as Dynamically Typed Programming Language.
 
You can create a function that can take any object, allowing for polymorphism.
def figure(obj):     
     obj.draw()
What is the type of obj? We cannot decide at the beginning. At runtime we can pass any type. Then how we can decide the type?
 
Let’s take an example and create a function called 'figure ()' which will take an object which we will name 'obj'. Now, let’s give the function something to do that uses the 'obj' object we passed to it.
 
In this case, let’s call the methods draw () and color (), each of which is defined in the three classes 'Circle' and 'Rectangle’, ‘Square'. Now, you have to create instantiations of these classes:
 
 
class Circle:
   def draw(self):
       print('Circle Shape Draw!.')
   def color(self):
       print('Yellow Color Fill In Circle!.')
 
class Rectangle:
   def draw(self):
       print('Rectangle Shape Draw!.')
   def color(self):
       print('Green Color Fill In Rectangle!.')
  
 
 
class Square:
   def draw(self):
       print('Square Shape Draw!.')
   def color(self):
       print('Pink Color Fill In Square!.')
 
#define function for Polymorphism

def figure(obj):
   obj.draw() 
   obj.color()     
l=[Circle(),Rectangle(),Square()]
for obj in l:
   figure(obj)
   print('===========================')
 
output:
Circle Shape Draw!.
Yellow Color Fill In Circle!.
====================
Rectangle Shape Draw!.
Green Color Fill In Rectangle!.
====================
Square Shape Draw!.
Pink Color Fill In Square!.
====================
 
The problem in this approach is if obj does not contain draw() method then we will get AttributeError
 
class Circle:
   def draw(self):
       print('Circle Shape Draw!.')
  
class Rectangle:
   def paint(self):
       print('Rectangle Shape Paint!.')
  
  
class Square:
   def draw(self):
       print('Square Shape Draw!.')
class Triangle:
   def paint(self):
       print('Triangle Shape Paint!.')
 
#define function for Polymorphism
def figure(obj):
   obj.draw() 
      
l=[Circle(),Rectangle(),Square(),Triangle]
for obj in l:
   figure(obj)
   print('===========================')
output:
  
   Circle Shape Draw!.
===========================
 obj.draw()
AttributeError: 'Rectangle' object has no attribute 'draw'
 
Demo Program with hasattr() function:
 
The hasattr() method returns true if an object has the given named attribute and false if it does not.
 
The syntax of hasattr() method is:
 
hasattr(object, name)
 
The hasattr() method takes two parameters:
 
object - object whose named attribute is to be checked
name - name of the attribute to be searched.
In The given figure there are four classes Circle,Rectangle,Square,Triangle where Circle, Square classes contain draw() method and Rectangle,Triangle classes contain paint() method.
 
class Circle:
   def draw(self):
       print('Circle Shape Draw!.')
  
class Rectangle:
   def paint(self):
       print('Rectangle Shape Paint!.')
 
class Square:
   def draw(self):
       print('Square Shape Draw!.')
class Triangle:
   def paint(self):
       print('Triangle Shape Paint!.')
 
#define function for Polymorphism
def figure(obj):
   if hasattr(obj,'draw'):
       obj.draw()
   elif hasattr(obj,'paint'): 
       obj.paint()     
 
#Create a list which contain given class object     
l=[Circle(),Rectangle(),Square(),Triangle()]
for obj in l:
   figure(obj)
   print('===========================')   
 
output:
Circle Shape Draw!.
===========================
Rectangle Shape Paint!.
===========================
Square Shape Draw!.
===========================
Triangle Shape Paint!.
===========================
 
 
 
Polymorphism with Class Methods
 
 
See the above, diagram in the given diagram there are three classes. All the classes have two methods. Now we will see how to call. Here, you have to create a for loop that iterates through a tuple of objects. Next, you have to call the methods without being concerned about which class type each object is. We assume that these methods actually exist in each class.
 
 
 
 
 
 
 
class India():
   def capital(self):
       print("New Delhi")
   def language(self):
       print("Hindi and English")
 
class USA():
   def capital(self):
       print("Washington, D.C.")
   def language(self):
       print("English")
 
class Europe():
   def capital(self):
       print("Brussels")
   def language(self):
       print("French")
 
obj_ind = India()
obj_usa = USA()
obj_eur=Europe()
for country in (obj_ind, obj_usa,obj_eur):
   country.capital()
   country.language()
 
output:
New Delhi
Hindi and English
Washington, D.C.
English
Brussels
French
 
 
 
 
 
 
 
 
 
Method Overriding in Python
 
If the child class not satisfy the parent class method implementation then it is possible to override that method in the child class based on child class requirement.
 
Whatever methods parent has by default available to the child through inheritance. Sometimes child may not satisfy with parent method implementation. Then child is allowed to redefine that method based on its requirement. This process is called overriding.
 
It's an approach of re-implementing a parent classes method under the child class with the same signature.
 

The parent class method which is overridden is called overridden method.
The child class method which is overriding is called overriding method.
 
The parent class method is called-------------overridden method
The child class method is called---------------overriding method
 
When the child inherits the features from his parent, the child may be happy with those features of the parent but sometimes the child may not be happy with those features of the parent if the child is not satisfied with those features of the parent. then child Can override those features of the parent. this is nothing it is overriding.
 
In the given example, the parent has three method such as the parent has taken the decision to purchase the hero bike but may be child not be happy with this decision of the parent, may be the child wants to buy another bike, then the child Can override the parent decision
 
 
class Parent:
   def property(self):
       print('Parent has Money,Gold')
   def purchaseBike(self):
       print('parent wants to purchase Hero Bike!')
   def marry(self):
       print('parent decide marry with Black girl!')
 
class Child(Parent):
   def purchaseBike(self):
       print('Child wants to purchase R1-5 Bike!')
   def marry(self):
       print('Child decide marry with White girl!')
 
#Creating Parent class object
print('With respect to parent object!.')
p=Parent()
p.property()
p.purchaseBike()
p.marry()
#Creating Child class object
print('With respect to child object!.')
c=Child()
c.property()
c.purchaseBike()
c.marry()
 
output:
With respect to parent object!.
Parent has Money,Gold
parent wants to purchase Hero Bike!
parent decide marry with Black girl!
With respect to child object!.
Parent has Money,Gold
Child wants to purchase R1-5 Bike!
Child decide marry with White girl!
 
Real example of Java Method Overriding
Consider a scenario, Bank is a class that provides functionality to get rate of interest. But, rate of interest varies according to banks. For example, SBI, ICICI and AXIS banks could provide 8%, 7% and 9% rate of interest.
 
 
class Bank:
   def getRateOfInterest(self):
       return 0
 
 
class SBI(Bank):
   def getRateOfInterest(self):
       return 7
 
class ICICI(Bank):
   def getRateOfInterest(self):
       return 8
 
class AXIS(Bank):
   def getRateOfInterest(self):
       return 9
 
#creating an object
s= SBI();
print('SBI Rate of Interest: ',s.getRateOfInterest())
i= ICICI();
print('ICICI Rate of Interest: ',i.getRateOfInterest())
a= AXIS();
print('AXIS Rate of Interest: ',a.getRateOfInterest())
 
output:
SBI Rate of Interest:  7
ICICI Rate of Interest:  8
AXIS Rate of Interest:  9
 
 
Another Example:
class Animal:
   def eating(self):
       print('Animal Eating!.')
class Lion(Animal):
   def eating(self):
       print('Lion is eating meat!.')
 
class Cow(Animal):
   def eating(self):
       print('Cow is eating grass!.')
 
#creating an object
a=Animal()
a.eating()
l=Lion()
l.eating()
c=Cow()
c.eating()
 
output:
Animal Eating!.
Lion is eating meat!.
Cow is eating grass!.

# Python program to demonstrate
# command line arguments
 
 
import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
	print(sys.argv[i], end = " ")
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
	Sum += int(sys.argv[i])
print("\n\nResult:", Sum)