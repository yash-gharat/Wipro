text = "python is a beginner friendly language"

# 1.Find the Length of a String
length = len(text)
print("Length of a String {0}".format(length))


# 2.Avoid Spaces in String Length

length_without_spaces = len(text.replace(" ", ""))
print("Length of the string without spaces:", length_without_spaces)

# 3.Print Even Length Words in a String
for word in text.split():
    if len(word) % 2 == 0:
        print(len(word),word)
        
# 4.Print First Half of the String in Uppercase and the Next Half in Lowercase

mid = len(text) // 2
first_half = text[:mid].upper()
second_half = text[mid:].lower()
print("First half in uppercase & Second half in lowercase:", first_half + second_half)

# 5.Capitalize the Alternative Characters of the String

capitalize_char = ''
for i, char in enumerate(text):
    if i % 2 == 0:
        capitalize_char += char.upper()
    else:
        capitalize_char += char.lower()
print("Capitalize the Alternative Characters of the String",capitalize_char)



# 6.First and Last Characters of Each Word in a String

word_list = text.split()
first_last_characters = []

for word in word_list:
    first_last_char = (word[0], word[-1])
    first_last_characters.append(first_last_char)

print("First and last characters of each word in the string:", first_last_characters )




# 7.Count the Number of Digits, Alphabets, and Other Characters in a String

digit_count = alpha_count = other_count = 0

for char in text:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        alpha_count += 1
    else:
        other_count += 1

print("Number of digits:{0}, Number of alphabets:{1}, Number of other characters:{2}".format(digit_count,alpha_count,other_count))

# 8.Check if a String Starts With the Alphabet and Has Digits

starts_with_alpha = text[0].isalpha()
has_digits = text.isdigit()
print("Starts with alphabet:", starts_with_alpha,"Has digits:", has_digits)

# 9.Count the Number of Vowels in a String
vowels = 'aeiouAEIOU'
vowel_count = 0
for vowel in vowels:
    vowel_count += text.count(vowel)

print("Number of vowels:", vowel_count)


# 10.Remove All Duplicate Words From a Given String
words = text.split()
#creating a array to store unique values
unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)
result = ' '.join(unique_words)
print("Remove All Duplicate Words From a Given String",result)

# 11.Print the Character with Maximum Frequency in a String

char_frequency = []
for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# Find the character with the maximum frequency
max_frequency_char = max(char_frequency, key=char_frequency.get)
print("Character with maximum frequency:", max_frequency_char)

# 12.Print the Frequency of Each Character in String

char_frequency = []
for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Frequency of Each Character in String:", char_frequency)

# 13.Remove ith Character From the String
i = 4 
memoved_text = text[:i] + text[i+1:]
print("after removing ith character:", memoved_text)

# 14.Split and Join a String
split_text = text.split()
joined_text = '+'.join(split_text)
print("Split text:", split_text)
print("Joined text:", joined_text)


# 15.Replace Commas with Whitespace Character in a Given String

replaced_text = text.replace(',', ' ')
print("String with commas replaced by whitespace:", replaced_text)