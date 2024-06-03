#Class description: 
# Constructor: Initialize both the instance variables, 
# no_of_vehicle, total_amount to 0 count_vehicle():
# Increment total number of vehicle by 1 calculate_amount(vehicle_type):
# Accept vehicle type and identify toll amount for that vehicle based on details given in the table. 

# Add it to the total_amount instance variable. collect_toll(owner_type,vehicle_type): 
# Accept owner type and vehicle type of the vehicle for which toll should be collected.
# If the owner of the vehicle is a "VIP", then toll amount need not be collected but number of vehicles should be updated. For any other type of owner, calculate the toll amount and update the number of vehicles. 

# (Hint: Invoke appropriate methods to complete the functionality) Perform case insensitive string comparison. 
# Create an object of Tollbooth class, invoke collect_toll() method for different vehicles and test your program.

class Tollbooth:
    def __init__(self):
        self.no_of_vehicle = 0
        self.total_amount = 0
    def count_vehicle(self):
        self.no_of_vehicle += 1
    
    def calculate_amount(self, vehicle_type):
        #Assuming the total values
        toll_amounts = {
            "car": 50,
            "bus": 100,
            "truck": 200,
            "bike": 20
        }
        return toll_amounts.get(vehicle_type.lower(), 0)
    
    def collect_toll(self, owner_type, vehicle_type):
        if owner_type.lower() == "vip":
            self.count_vehicle()
        else:
            toll_amount = self.calculate_amount(vehicle_type)
            self.total_amount += toll_amount
            self.count_vehicle()
    def toString(self):
        print(f"no_of_vehicle :  {self.no_of_vehicle},total_amount : {self.total_amount}")
toll_booth = Tollbooth()
toll_booth.collect_toll("Regular", "Bus")
toll_booth.collect_toll("VIP", "Car")
toll_booth.collect_toll("Regular", "Truck")

toll_booth.toString()