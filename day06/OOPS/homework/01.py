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

class DogShop:
    counter = 100
    dog_breed_dict = {
         "Labrador Retriever": 800,
            "German Shepherd": 1230,
            "Beagle": 650
    }

    def __init__(self, breed_list, accessories_required=False):
        self.breed_list = breed_list
        self.dog_id_list = []
        self.price = 0
        self.accessories_required = accessories_required

    def validate_breed(self):
        # Assuming dog_breed_dict is a global dictionary containing available dog breeds and their quantities
        available_breeds = set(self.dog_breed_dict.keys())
        return all(breed in available_breeds for breed in self.breed_list)

    def validate_quantity(self):
        # Assuming dog_breed_dict is a global dictionary containing available dog breeds and their quantities
        return all(self.dog_breed_dict[breed] > 0 for breed in self.breed_list)

    def generate_dog_id(self, breed):
        self.counter += 1
        return f"{breed[0]}{self.counter}"

    def get_dog_price(self, breed):
        # Assuming dog_prices is a global dictionary containing prices for each dog breed
        return dog_prices.get(breed, 0)

    def calculate_total_price(self):
        total_price = sum(self.get_dog_price(breed) for breed in self.breed_list)
        if self.accessories_required:
            total_price += 350
        if total_price > 1500:
            total_price *= 0.95  # 5% discount
        return total_price

    def sell_dogs(self):
        if not self.validate_breed():
            return -1  # Breed not available
        if not self.validate_quantity():
            return -2  # Quantity not available

        for breed in self.breed_list:
            if self.dog_breed_dict[breed] > 0:
                self.dog_id_list.append(self.generate_dog_id(breed))
                self.price += self.get_dog_price(breed)
                if self.accessories_required:
                    self.price += 350
                self.dog_breed_dict[breed] -= 1

        if self.price > 1500:
            self.price *= 0.95  # 5% discount

        return self.price

# Example usage:
dog_shop = DogShop(["Labrador", "Poodle"], accessories_required=True)
price = dog_shop.sell_dogs()
print("Total price:", price)
print("Dog IDs:", dog_shop.dog_id_list)
