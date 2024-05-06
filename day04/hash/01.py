# def fn():
#     text = "ISR"
#     total = 0
#     for ch in text:
#         print(ch)
#         total += ord(ch)
#         print(total)
# Identify the hash by applying hash function on the givenkey
# locate the hash in the hash table

def hash_fn(key_list):
    hashed_table = [None for i in range(5)]
    hash_key = None
    for key in key_list:
        unicode_sum = 0
        for ch in key:
            unicode_sum += ord(ch)
            hash_key = unicode_sum % 5
        print(key,hash_key)
        hashed_table[hash_key] = key
        print(hashed_table)
    
        # hashed_table.append(hash_code)
    # for key in key_list:
    #     hashed_table[hash_key] = key
    #     print(hashed_table)
    # return print(hashed_table)

Key_list = ["ISR", "PER", "IND", "FJI", "CAN", "SWE"]
Country_List = ["Israel", "Peru", "India", "Fiji", "Canada", "Sweden"]
hash_fn(Key_list)

def hash_value(key):
    hash_key = 0
    for i in range(0,len(key)):
        hash_key += ord(key[i])
    return (hash_key % 5)

def insert_key_val(key,val):
    index = hash_value(key)
    Country_List[index] = val
    print(Country_List)

for i in range(len(Country_List)):
    insert_key_val(Key_list[i],Country_List[i])
