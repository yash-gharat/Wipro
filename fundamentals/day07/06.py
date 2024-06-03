# Problem Statement
# An apparel shop wants to manage the items which it sells. 
# Write a python program to implement the class diagram given below.
# Class Description:
# Apparel class:
# Initialize static variable counter to 100
# In the constructor, auto-generate item_id starting from 101 prefixed by "C" for cotton apparels and "S" for silk apparels. Example – C101, S102, S103, C104 etc.
# calculate_price(): Add 5% service tax on the price of the apparel and update attribute, price with the new value
# Cotton class:
# While invoking parent constructor from child constructor, pass "Cotton" as item_type
# calculate_price(): Update attribute, price of Apparel class based on rules given below
# Add service tax on price by invoking appropriate method of Apparel class
# Apply discount on price
# Add 5% VAT on final price
# Silk class:
# While invoking parent constructor from child constructor, pass "Silk" as item_type
# calculate_price(): Update attribute, price of Apparel class based on rules given below
# Add service tax on price by invoking appropriate method of Apparel class
# Identify points earned based on rules given below:
# Silk apparels with price more than Rs. 10000, earn 10 points and anything less than or equal to that earn 3 points
# Initialize attribute, points with the identified points
# Add 10% VAT on price
# Note: Perform case sensitive string comparison  

# string = "yash"
# print(string[0])

class Apparel():
    counter = 100
    
    def __init__(self,price):
        self.price = price
        
    def calculate_price(self):
        self.price *= 0.05

class Cotton(Apparel):
    def __init__(self, price):
        super().__init__(price)
        self.item_type = "Cotton"
        self.item_id = self.item_type[0] + str(self.counter)

    def calculate_price(self):
        super().calculate_price()
        self.price -= self.price * 0.02
        self.price *= 1.05

class Silk(Apparel):
    def __init__(self, price):
        super().__init__(price)
        self.item_type = "Silk"
        self.item_id = self.item_type[0] + str(self.counter)
        
    def calculate_price(self):
        super().calculate_price()
        if self.price > 10000:
            self.points = 10
        else:
            self.points = 3
        self.price *= 1.1  

cotton_apparel = Cotton(200)
cotton_apparel.calculate_price()
print("Cotton Item ID:", cotton_apparel.item_id)
print("Cotton Price:", cotton_apparel.price)
