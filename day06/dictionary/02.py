# A dictionaries can be used to store an unordered collection of key-value pairs. 
# The key should be unique and can be of any immutable data type. Like lists, dictionaries are mutable. 
# Let’s now understand how a dictionary is implemented in Python.
# Creating a dictionary
	
crew_details =  { "Pilot":"Kumar",
                "Co-pilot":"Raghav",
                "Head-Strewardess":"Malini",
                "Stewardess":"Mala" }
print("crew_details",crew_details)
# First element in every pair is the key and the second element is the value.


# Accessing the value using key
	
print("Accessing the value using key",crew_details["Pilot"])

	
# This will return the corresponding value for the specified key


# Iterating through the dictionary
	
for key,value in crew_details.items():
    print(key,":",value)
	
# items function gives both key and value, which can be used in a for loop.
# Dictionary in Python also have many inbuilt functions.
 
# Function
	
# Output
	
# Explanation


print(crew_details.get("Pilot"))
print(crew_details.get("new"))
	
# Kumar
	
# Returns the value for given key. If the given key is not found, returns None


crew_details.update({"Flight Attendant":"Jane", "Co-pilot":"Henry"})
print("updated dic",crew_details)
# No output, dictionary will be updated
	
# Updates the dictionary with the given key-value pairs. If a key-value pair is already existing, it will be overwritten, otherwise it will be added to the dictionary
