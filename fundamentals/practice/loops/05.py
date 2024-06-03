# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

string = "yyasshhh"

for char in string:
    # print(char)
    if string.count(char) == 1:
        print(char)
