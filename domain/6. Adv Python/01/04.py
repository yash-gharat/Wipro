import json
# import day03.data.json as data
data = {
    "id": 1,
    "username": "yash123",
    "email": "yash@example.com",
    "password" : "123456"
}

# Create a new dictionary with only the username
filtered_data = data.get("username")


# Write the filtered dictionary to a JSON file
with open("data.json", "w") as json_file:
    json.dump(filtered_data, json_file)
print(filtered_data)
