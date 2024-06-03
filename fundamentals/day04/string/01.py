text = "161sdvvdaf"
text2 = "ooo"
#length of the string
print(len(text))

# Concetating
new = text+ text2
print(text)
print(text2)
print(new)

#looping

list = []
for i in range(len(text)):
    list.append(text[i].upper())
print(list)

list = []
for i in text:
    print(i.upper(), end=' ')

num = "01213"
word = "hello"
print(word.count("l"))
print(word.replace("e","E"))
print(word.find("a"))
print(word.endswith("o"))
print(word.startswith("H"))
print(word.isdigit())
print(word.upper())
print(word.lower())
print(word.split("e"))