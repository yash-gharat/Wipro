# # Creating class
# # $class is a logical structure for the objects
# class Mobile:
#     pass

# # Creating objects
# Mobile()

# # Rrefernce variable

# mob1 =Mobile()
# mob2 =Mobile()
# # Address of ref var using id

# mob1.price = 20000
# mob1.name = "Samsung"


# print(mob1.name)
# print(mob2)


class Mobile:
    # __init__ speacial function(also know as constructor) automatically invoked when the class is called
    # self is the refrening/pointing for the cureent object
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

mob1 = Mobile(price=2000,brand="Apple")
mob2 = Mobile(price=2000,brand="Samsung")

print(mob1)
print(mob2)