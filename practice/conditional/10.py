# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age.
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter the species of the pet \n").upper()
age = int(input("Enter the pets age \n"))

if(species == "DOG"):
    if(age <= 2):
        print("Puppy food")
elif(species == "CAT"):
    if(age >= 5):
        print("Senior cat food")
else:
    print("Enter the valid species")