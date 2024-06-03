
# Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below 
# and returns the encrypted message.
# Words at odd position -> Reverse It
# Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change
# Note: 
# Assume that the sentence would begin with a word and there will be only a single space between the words.
# Perform case sensitive string operations wherever necessary.
# Sample Input
# the sun rises in the east
	
# Expected Output
# eht snu sesir ni eht stea
	


# --> reverse each word



def reverse(word):
    return (word[::-1])
# print(reverse("sun"))

def fn(word):
    consonants = ""
    vowels = ""
    for char in word:
        if char.lower() not in 'aeiou':
            consonants += char
        else:
            vowels += char
    return (consonants + vowels)

# print(fn("sun"))

def encrypt_sentence(string):
    words = string.split()
    print("Input",words)
    encrypted_words = []
    pos = 0
    for word in words:
        if pos % 2 != 0:
            #words are in odd pos reverse it
            encrypted_words.append(reverse(word))
            print(encrypted_words)
        else:
            #words in even Rearrange the characters so that all consonants appear before the vowels
            encrypted_words.append(fn(word))
            print(encrypted_words)
        pos += 1
        print(encrypted_words)

string = "the sun rises in the east"
encrypt_sentence(string)


# 