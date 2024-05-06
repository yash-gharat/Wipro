text = "python is a beginner friendly language"

# 3.Print Even Length Words in a String
for word in text.split():
    if len(word) % 2 == 0:
        print(len(word),word)