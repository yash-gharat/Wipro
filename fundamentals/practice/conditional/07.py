# 7. Coffee Customization
# Problem: Customize a coffee order: 
# "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order = input("Enter your order \n").lower()
extra_shot = bool(int(input("Extra shot of expresso 0 or 1 \n")) )

print(extra_shot)

if(extra_shot == True ):
    print(f"{order} coffee with extra shot ")
else:
    print(f"{order} coffee without extra shot ")
    