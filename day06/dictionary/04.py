dict = {
    "name" : "John",
    "age" : 24,
}
print(dict.get("name"))

for key,value in dict.items():
    print(key ,":", value )
for key in dict:
    print(dict[key])
    
dict.update({"newKey" : "newValue"})
print(dict)

