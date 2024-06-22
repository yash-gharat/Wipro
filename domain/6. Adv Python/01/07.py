import json

# Deserialize from JSON string
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_string)

print(data)  # Python dictionary

# Load from a file
with open('data.json', 'r') as file:
    data = json.load(file)

print(data)  # Python dictionary
