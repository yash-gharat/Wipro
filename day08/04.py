# ABC DTH (Direct to Home) firm wants to calculate monthly rent for its consumers. 

# A consumer can register for one Base Package. Write a python program to implement the below given class diagram.
# Class Description:
# DirectToHomeService class:
# Initialize static variable counter to 101
# Inside constructor, auto-generate consumer_number starting from 101
# BasePackage class:
# validate_base_pack_name():
# Validate base pack name. Valid values are "Silver", "Gold" and "Platinum".
# If invalid, set attribute, base_pack_name as "Silver" and display "Base package name is incorrect, set to Silver"

# calculate_monthly_rent():
# Check if subscription period is between 1 and 24 (both inclusive). If so,
# Validate base pack name
# Identify monthly rent based on base pack. Refer table given.
# Consumers are eligible for discount of one month's rent, if subscription period is more than 12 months
# Calculate final monthly rent as per the formula given below:
# final monthly rent = ((monthly rent * subscription period) – discount amount)/subscription period
# Return the calculated final monthly rent
# If not, return -1

# Base Pack Name
# Silver
# Gold
# Platinum
	
# Monthly Rent
# 350.00
# 440.00
# 560.00

# Note: Perform case sensitive string comparison
# For testing:
# Create objects of BasePackage class
# Invoke calculate_monthly_rent() on BasePackage object
# Display the details
# has context menu

class DirectToHomeService:
    counter = 101
    
    def __init__(self):
        self.consumer_number = DirectToHomeService.counter
        DirectToHomeService.counter += 1
    
class BasePackage(DirectToHomeService):
    base_pack_names = ["Silver", "Gold", "Platinum"]
    monthly_rents = {"Silver": 350, "Gold": 440, "Platinum": 560}
    
    def __init__(self, base_pack_name, subscription_period):
        super().__init__()
        self.base_pack_name = self.validate_base_pack_name(base_pack_name)
        self.subscription_period = subscription_period
    
    def validate_base_pack_name(self, base_pack_name):
        if base_pack_name not in self.base_pack_names:
            print("Invalid Base package name")
            return "Silver"
        return base_pack_name
    
    def calculate_monthly_rent(self):
        # Check if subscription period is between 1 and 24
        if 1 <= self.subscription_period <= 24:
            monthly_rent = BasePackage.monthly_rents[self.base_pack_name]
            # Consumers are eligible for discount of one month's rent, if subscription period is more than 12 months
            if self.subscription_period > 12:
                discount_amount = monthly_rent
            else:
                discount_amount = 0
                # final monthly rent = ((monthly rent * subscription period) – discount amount)/subscription period
            final_monthly_rent = ((monthly_rent * self.subscription_period) - discount_amount) / self.subscription_period
            return final_monthly_rent
        else:
            return -1

service1 = BasePackage("Gold", 16)
service2= BasePackage("Silver", 1)
service3 = BasePackage("Platinum", 24)
service3 = BasePackage("Platinum", 64)
print(f"consumer_number : {service1.consumer_number} base_pack_name : {service1.base_pack_name} subscription_period : {service1.subscription_period} monthly_rent : {service1.calculate_monthly_rent()}")
print(f"consumer_number : {service2.consumer_number} base_pack_name : {service2.base_pack_name} subscription_period : {service2.subscription_period} monthly_rent : {service2.calculate_monthly_rent()}")
print(f"consumer_number : {service3.consumer_number} base_pack_name : {service3.base_pack_name} subscription_period : {service3.subscription_period} monthly_rent : {service3.calculate_monthly_rent()}")
