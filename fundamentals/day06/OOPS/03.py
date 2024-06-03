# Assignment:30 mins
# WeCare insurance company wants to calculate premium of vehicles.
# Vehicles are of two types – "Two Wheeler" and "Four Wheeler". Each vehicle is identified by vehicle id, type, cost and premium amount.
# Premium amount is 2% of the vehicle cost for two wheelers and 6% of the vehicle cost for four wheelers. 
# Calculate the premium amount and display the vehicle details.
# Identify the class name and attributes to represent vehicles. Drag and drop the chosen class name, attributes and methods into the appropriate section of the box shown below.
 
 
# premium_percentage
# premium_amount
# calculate_premium()
# FourWheeler
# TwoWheeler
# vehicle_id
# vehicle_type
# display_vehicle_details()
# __init__()
# vehicle_cost
# Vehicle
# calculate_vehicle_cost()

# class -  Vehicle
# attributes - vehicle_id,vehicle_type,vehicle_cost
# methods - __init__(),calculate_premium(),display_vehicle_details(),calculate_vehicle_cost()

class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_cost):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.vehicle_cost = vehicle_cost
        self.premium_amount = None
        self.premium_percentage = None
    
    def calculate_premium(self):
        if self.vehicle_type == "Two Wheeler":
            self.premium_percentage = 0.02
        elif self.vehicle_type == "Four Wheeler":
            self.premium_percentage = 0.06
        else:
            print("Invalid vehicle type")
        self.premium_amount = self.vehicle_cost * self.premium_percentage

    def calculate_vehicle_cost(self):
        
        pass
    
    def display_vehicle_details(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Vehicle Type:", self.vehicle_type)
        print("Vehicle Cost:", self.vehicle_cost)
        print("Premium Amount:", self.premium_amount)


bike = Vehicle(1,"Two Wheeler",50000)
bike.calculate_premium()
car = Vehicle(1,"Four Wheeler",200000)
car.calculate_premium()

bike.display_vehicle_details()
car.display_vehicle_details()