# Problem Statement
# Mary is a kindergarten teacher. 
# She has given a task to the children after teaching them a list of words. 
# The task is to find the unknown words (other than the words they already know) from the given text. 
# Write a python function which accepts the text and the known list of words and returns the set of unknown words found.
# Return -1 if there are no unknown words.

# Sample Input
# Expected Output

# Text: "the sun rises in the east"
# Vocabulary: ["sun","in","east","doctor","day"]
# {'rises', 'the'}


#Convert the statement into the words
#Compare each word in []
#if word is not in the list add it into unknown_word[]
#If there are unknown words, return the unknown_word[]. Otherwise, return -1.

def find_unknown_words(text,know_words):
    #converting string into array
    words = text.split()
    unknown_words = []
    for word in words:
        if(word not in know_words):
            #add the word into unknown_word[]
            unknown_words.append(word)
    if unknown_words:

        return print(unknown_words)
    else:
        return -1

    #compare each word in words

text = "the sun rises in the east"
know_words = ["sun","in","east","doctor","day"]
find_unknown_words(text , know_words)