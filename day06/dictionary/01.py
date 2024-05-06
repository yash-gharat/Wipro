sample_dic = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3"
    
}

# sample_dic[]
# print(sample_dic.get("key3"))

for key,value in sample_dic.items():
    print(key,value)

for key in sample_dic.items():
    print(key)

sample_dic["key1"] = "new_value"

print(sample_dic)