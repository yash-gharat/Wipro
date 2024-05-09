# Day - 08

1. Abstraction - hiding the internal working from the user

- defined method - method that has a body
```
def m1():
    print("HELLO")
```
- undefined method
```
def m2():
    pass
```

concreted class - has defined method

Abstract class - has altleast one  undefined method

Abstract method:
====================
|-A method without body is called as abstract method
 
|-To mark our undefined method as abstract method we have needs to annotate our undefined method by @abstractmethod annottation
 
 
@abstractmethod
def payBiil(self,amount):
     pass
 
 Abstract class
================
|-The class which contains atleast one abstract method that class is called as a   Abstract class.
 
 
|-To mark our class as abstrac class we needs to mark ABCMeta
 
from abc import ABCMeta
class Product(metaclass=ABCMeta):
       @abstractmethod
	def payBiil(self,amount):
    		 pass
 
Summary:
=======
-Abstract classes should not be instantiated.
-An abstract class may contain 0 or many abstract methods.
-Usually the parent class is an abstract class.
-Abstract classes are meant to be inherited.
-If a class has an abstract method, then the class cannot be instantiated.
-The child class must implement/override all the abstract methods of the parent   class. Else the child class cannot be instantiated.

Abstract Class - Introduction
Let us assume that we have a Product class , all items being sold in our online app and extend this Product class.
In an online shopping app, we only have specific types of products. We don’t have something called a Product itself. In that sense, an object of Product class would not represent a real world object, because a Product is just an abstract concept. While shopping, we purchase types of products, not a product itself. Thus the best practice is not to create object of the parent class
 
Preventing instantiation
Since we are the creator of the Product class, we know it is abstract in nature and we won’t create an instance for it. But how can another programmer know about it? How can we ensure that some other developer does not end up creating an object of such an abstract class?
We can programmatically declare a class as an abstract class. An abstract class should not be instantiated.
Note: In python, you will not get an error if you try to instantiate it. However, in languages like Java, C++, C# you will get an error if you try to instantiate an abstract class
What is the use of abstract?
If an abstract class should never be instantiated, then what is the use of such a class? The only way we can use an abstract class is to make other classes inherit from the abstract class. An abstract class is meant to be sub classed.
 
Abstract Method - A Scenario
Let us extend the concept of abstract further. All products must have a return_policy() method which will display the number of days within which the products have to be returned    
class Product:
    def return_policy(self):
        pass
class Mobile(Product):
    pass
class Shoe(Product):
    pass
 
Problem Statement
Now each type of product will have its own return_policy(), so we will override the return_policy() in each of the child classes.
class Mobile(Product):
   def return_policy(self):
       print("All mobiles must be returned within 10 days of purchase")
 
class Shoe(Product):
   def return_policy(self):
       print("All shoes must be returned within 7 days of purchase")
                                 
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

```
Try out - Exception Handling - The Scenario
 
Problem Statement
Go through the below code, execute and observe the result, which calculates the airport expenditure.
#calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
  total=0
  for expenditure in list_of_expenditure:
       total+=expenditure
  print(total)
list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)
 
Problem Statement
We got an error in the below code, one way to take care of such error situation is to use selection constructs.
The error was due to addition of a string (“400”) to an integer. If we add a condition to check whether the expenditure is of type int, that would solve this error. But that can cause further issues.
 
#calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
  total=0
  for expenditure in list_of_expenditure:
       total+=expenditure
  print(total)
list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)
 
 
Try out - Exception Handling using 'try' & 'except'

Problem Statement
 
In python we can create a try and except block of code.
If any error occurs in the try block of code, it will jump to except block of code.
Once the except block is executed, the code continues to execute other statements outside except block.
Code in Python 3
#calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
   total=0
   try:
       for expenditure in list_of_expenditure:
          total+=expenditure
       print(total)
   except:
      print("Some error occured")
  print("Returning back from function.")
 
list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)
 
Exception Handling - Different Types
 
Python has many kinds of errors predefined as part of the language. Here are some of the common types.
Built-in Exception
	
When it will be raised
	
Example


ZeroDivisionError
	
When a value is divided by zero
	
num_list=[]
total=10
avg=total/len(num_list)


TypeError
	
When we try to do an operation with incompatible data types
	
total=10
total+="20"


NameError
	
When we try to access a variable which is not defined
	
avg=total/10 where total is not defined


IndexError
	
When we try to access an index value which is out of range
	
num_list=[1,2,3,4]
value=num_list[4]


ValueError
	
When we use a valid data type for an argument of a built-in function but passes an invalid value for it
	
#string is a valid data type for int() but the value “A” is invalid, as "A" can't be converted into int.
value="A"
num=int(value)
 
Python also allows us to handle different errors that can occur separately. That means you can have a different action or message for every unique error that occurs.
Here is the same expenditure calculation code with additional average expenditure calculation
 
 
def calculate_expenditure(list_of_expenditure):
   total=0
   try:
       for expenditure in list_of_expenditure:
           total+=expenditure
       print("Total:",total)
       avg=total/num_values
       print("Average:",avg)
   except ZeroDivisionError:
       print("Divide by Zero error")
   except TypeError:
       print("Wrong data type")
   except:
       print("Some error occured")
list_of_values=[100,200,300,"400",500]
num_values=0
calculate_expenditure(list_of_values)
 
 
 
Try out - Customized Error Messages
 
Problem Statement
Fix the below code to get customized error messages. You can use various except blocks.
Code in Python 3
def calculate_expenditure(list_of_expenditure):
  total=0
  try:
       for expenditure in list_of_expenditure:
           total+=expenditure
       print("Total:",total)
       avg=total/num_values
       print("Average:",avg)
  except:
       print("Some error occured")
  except ZeroDivisionError:
       print("Divide by Zero error")
  except TypeError:
       print("Wrong data type")
  
list_of_values=[100,200,300,"400",500]
num_values=0
calculate_expenditure(list_of_values)
 
 
Try out - Multiple Try Blocks
 
Problem Statement
If an error occurs inside a function and if the error is not caught inside it, then the error is transferred to the function call where we have another opportunity to catch it.
 
Execute the below code and observe the results.
Code in Python 3
def calculate_sum(list_of_expenditure):
  total=0
  try:
       for expenditure in list_of_expenditure:
           total+=expenditure
       print("Total:",total)
       avg=total/no_values
       print("Average:",avg)
  except ZeroDivisionError:
       print("Divide by Zero error")
  except TypeError:
       print("Wrong data type")
 
try:
  list_of_values=[100,200,300,400,500]
  num_values=len(list_of_values)
  calculate_sum(list_of_values)
except NameError:
  print("Name error occured")
except:
  print("Some error occured")
 
Try out - Finally Block
 
Problem Statement
Sometimes in programming we need to execute some code irrespective of whether the primary program logic itself succeeds or fails to do its job. In Python we can achieve this using a finally block.
A finally block of statement is an optional part of the try-except statements. A code written inside the finally block will ALWAYS be executed.
Execute the below code and observe the results.
Code in Python 3
balance=1000
amount="300Rs"
def take_card():
  print("Take the card out of ATM")
try:
  if balance>=int(amount):
       print("Withdraw")
  else:
       print("Invalid amount")
 
except TypeError:
  print("Type Error Occurred")
except ValueError:
  print("Value Error Occurred")
except:
  print("Some error Occurred")
finally:
  take_card()
 
 
Quiz - Exception Handling
 
 
 
Q2 of
Go through the below code and predict the output:
num1=100
num2=0
try:
   result=num1/num2
   print(result)
except ZeroDivisionError:
   print("Zero Division Error Occurred")
 
 
Q3 of 4outlined_flag
What will be the output of the code given below?
def division(value_1,value_2):
   try:
       return int(value_1)/value_2
   except TypeError:
       print("Type error")
   except ValueError:
       print("Value error")
   finally:
       print("Finally")
   print("Done")
division('A',10)
a. Value error
    Finally
    Done
b. Type error
    Finally
    Done
c. Type error
    Finally
d. Value error
    Finally
 
Q4 of 4outlined_flag
What will be the output of the below code?
def find_sum(value_1,value_2):
   try:
       print(value_1+value_3)
   except NameError:
       print("Function name error")
   finally:
       print("Sum finally")
try:
   find_sum(12,13)
except NameError:
   print("Invocation name error")
finally:
   print("Invocation finally")
a. Function name error
    Sum finally
b. Function name error
    Sum finally
    Invocation finally
c. Function name error
    Sum finally
    Invocation name error
    Invocation finally
d. Sum finally
    Invocation name error
    Invocation finally
 
 
Exercise on Exception Handling - Level 1
 
Problem Statement
 
The python function, find_average() given below, is written to accept a list of marks and return the average marks. On execution, the program is resulting in an error.
1: Add code to handle the exception occurring in the code.
2: Make the necessary correction in the program to remove the error.
3: Make the following changes in the code, execute, observe the results. Add code to handle the errors occurring in each case.
Case – 1: Initialize m_list as ["1",2,3,4]
Case – 2: Initialize m_list as given below
mark1="A"
mark1=int("A")
m_list=[mark1,2,3,4]
Case – 3: Initialize m_list as []
Case – 4: Make the following change in the for loop statement
for i in range(0, len(mark_list)+1):
 
 
 
has context menu
```