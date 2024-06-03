# Initialize static variable counter to 100
# breed_list: List of dog breeds required by the customer. Initialize it in the constructor
# dog_id_list: List of dog ids. Initialize it to an empty list in the constructor
# price: Total price to be paid by the customer. Initialize it to 0 in the constructor
# accessories_required: Boolean value – True indicated accessories are required and False indicated accessories are not required.                          Initialize it in the constructor
# validate_breed(): Return true if all the breeds required by the customer are available. Else return false
# validate_quantity(): Return true if one dog/breed is available for all the breeds requested by the customer. Else return false
# generate_dog_id(breed): Accept the breed of the dog for which dog id should be generated.                                                                                Auto-generate dog id starting from 101 prefixed by the first character of the breed
# get_dog_price(breed): Return the price of the dog whose breed is passed to the method
# calculate_total_price(): Calculate the total price of all the dogs required by the customer.
# Validate breed and quantity of all the dogs required by the customer
# If valid,
# For every breed in breed_list,
# Update quantity in dog_breed_dict
# Auto-generate dog id and append it to attribute, dog_id_list
# Add price to attribute, price
# If accessories are required, add 350 to attribute, price
# If price is more than 1500, provide 5% discount on price
# If any breed is not available, return -1
# If quantity is not available for any breed, return -2
# If quantity is not available for any breed, return -2
 
#Input
# breed_list = {
#     "Labrador Retriever" : 5,
#     "German Shepherd" : 12,
#     "Beagle" : 10
#     }

class dog_shop:
    counter = 100
    dog_breed_dict = {
        "Labrador Retriever": 800,
        "German Shepherd": 1230,
        "Beagle": 650
    }
    def __init__(self,breed_list,accessories_required=False) -> None:
        self.counter += 1
        # self.dog_breed_dict = breed_list
        self.breed_list = breed_list
        self.dog_id_list = []
        self.price = 0
        self.accessories_required = accessories_required

    def get_dog_id_list(self):
        return self.dog_id_list
    
    # returns the list provided by the customer
    def get_breed_list(self):
        return self.breed_list

    # returns total price to be paid by the customer
    def get_price(self):
        return self.price

    # retunrns accessories are required or not
    def get_accessories_required(self):
        return self.accessories_required

    # returns dog price based on the breed
    def get_dog_price(self,breed_name):
        return self.dog_breed_dict.get(breed_name, 0)

    # retunrs dog id based on breed
    def generate_dog_id(self,breed_name):
        self.counter += 1
        dog_id = f"{self.counter}{breed_name[0]}"
        self.dog_id_list.append(dog_id)
        return dog_id

    def validate_breed(self):
        available_breeds = self.get_breed_list().keys()
        for breed in self.dog_breed_dict:
            if breed not in available_breeds:
                return False
        return True
        
    def validate_quantity(self):
        available_breeds = self.get_breed_list()
        for breed, quantity in self.dog_breed_dict.items():
            if breed not in available_breeds or available_breeds[breed] < quantity:
                return False
        return True

    def calculate_total_price(self):
        if not self.validate_breed():
            return -1
        # if not self.validate_quantity():
        #     return -2

        for breed, quantity in self.breed_list.items():
            self.breed_list[breed] -= quantity
            for _ in range(quantity):
                self.dog_id_list.append(self.generate_dog_id(breed))
                self.price += int(self.get_dog_price(breed))
                if self.accessories_required:
                    self.price += 350

        if self.price > 1500:
            self.price *= 0.95

        return self.price


breed_list = {
    "Labrador Retriever": 5,
    "German Shepherd": 12,
    "Beagle": 10
}
# breed_list = {
#     "Retriever": 5,
#     " Shepherd": 12,
#     "Eagle": 10
# }

shop = dog_shop(breed_list, accessories_required=True)

dog_price = shop.get_dog_price("German Shepherd")
total_price = shop.calculate_total_price()
print("Dog Price:", dog_price)
print("Generate Dog ID :", shop.generate_dog_id("German Shepherd"))
print("Validate the breed :", shop.validate_breed())
print("Total Price:", total_price)