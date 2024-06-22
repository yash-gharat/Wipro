import json

#  Open the JSON file
with open('data.json', 'r') as file:
    #  Load JSON data
    data = json.load(file)

# Close the file
    file.close()

first_id = data['username']
print(first_id)
