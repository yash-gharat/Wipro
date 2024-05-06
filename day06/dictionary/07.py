# Write a python program that accepts a text and displays a string which contains the word with the largest frequency
# in the text and the frequency itself separated by a space.

# Rules:
# The word should have the largest frequency.

# In case multiple words have the same frequency, then choose the word that has the maximum length.
# Assumptions:
# The text has no special characters other than space.
# The text would begin with a word and there will be only a single space between the words.
# Perform case insensitive string comparisons wherever necessary.
 
# Sample Input
# "Work like you do not need money love like you have never been hurt and dance like no one is watching"
# "Courage is not the absence of fear but rather the judgement that something else is more important than fear"
	
# Expected Output
# like 3
# fear 2

##list
#Count frequency of each words
#Find the maximum frequency among all words
# Get word with the maximum frequency
# if there are more max freq words return the longest one


def fn(text):
    words = text.split()
    word_count = {}
    most_frequent_word = []
    for word in words:
        word_count[word] = text.count(word)
        # print(word_count)
	# find words with max freq
    max_freqency = max(word_count.values())
    for word, freq in word_count.items():
        if freq == max_freqency:
            most_frequent_word.append(word)
            
    # find longest word  from most frequent words
    test = {}
    for i in most_frequent_word:
        length = len(i)
        test.update({i : length})
    maxVal = max(test.keys())
    # print(maxVal)
    return maxVal, max_freqency

text = "Work like you do not need money love like you have never been hurt and dance like no one is watching"

print(fn(text))
	