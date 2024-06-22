import json

# Python object (dictionary)
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Serialize to JSON string
json_string = json.dumps(data)

# Save to a file
with open('data.json', 'w') as file:
    json.dump(data, file)

print(json_string)  # Serialized JSON string
