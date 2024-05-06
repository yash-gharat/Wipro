
menu = {
    "Raisin Toast": 2.50,
    "French Toast": 2.80,
    "Mushroom Roast": 3.00,
    "Pancake": 4.00,
    "Pancake with Ice Cream": 7.50,
    "Chef's Speciality": 10.00
}
print("BREAD BASKET")
print("Lookinf for healthy breakfast, this is the place for you !!")
print("-" * 35)

for item, price in menu.items():
    print("{0} ${1}".format(item, price))
    # print("{:<25} ${:<10.2f}".format(item, price))
print("-" * 35)