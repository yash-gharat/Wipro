# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather 
# (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input("Enter the current weather").upper()
if(weather == "SUNNY"):
    print("Go for a walk")
elif(weather == "RAINY"):
    print("Read a book")
elif(weather == "SNOWY"):
    print("Build a snowman")
else:
    print("Enter a valid weather")

