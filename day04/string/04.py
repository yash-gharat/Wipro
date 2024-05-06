text = "python is a beginner friendly language"

print(text.split())
# pos = text.find("i")

# print(text[pos:])


song="JINGLE Bells jingle Bells Jingle All The Way"
song.upper()
song_words=song.split()
count=0
print(song_words)
for word in song_words:
    if(word.startswith("jingle")):
        print(word.startswith("jingle"))
        count=count+1
        print("i",count)
print(count)