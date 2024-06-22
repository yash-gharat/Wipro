students = [
    {"name": "Yash", "phone": "123456789"},
    {"name": "Aarav", "phone": "987654321"},
    {"name": "Ishita", "phone": "555555555"},
    {"name": "Raj", "phone": "444444444"},
    {"name": "Nina", "phone": "333333333"}
]


new_list = list(map(lambda name : name["name"],students))
print(new_list)