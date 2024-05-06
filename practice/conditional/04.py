# . Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. 
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Enter the fruit name")
color = input("Enter the fruit color").lower()

if(color == "green"):
    print(f"{fruit}: {color.upper()} - Unripe")
elif(color == "yellow"):
    print(f"{fruit}: {color.upper()} - Ripe")
elif(color == "brown"):
    print(f"{fruit}: {color.upper()} - Overripe")
else:
    print("Enter the valid color")