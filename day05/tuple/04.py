# Write a python function which accepts a sentence
# and finds the number of letters and digits in the sentence.
# It should return a list in which the first value should be letter count 
# and second value should be digit count.
# Ignore the spaces or any other special character in the sentence.

# Sample Input
# Infosys 123
# ABCEFG

# Expected Output
# [7,3]
# [6,0]


def count_digits_letters(sentence):
    #start writing your code here
    result_list = []
    letter_count = 0
    digit_count = 0
    
    for word in sentence:
        if word.isalpha():
            letter_count += 1
        elif word.isdigit():
            digit_count +=1    
        result_list = [letter_count, digit_count]     
    
    return result_list


# sentence="Infosys Mysore 570027"
# sentence="ABCEFG"
sentence="Infosys 123"
print(count_digits_letters(sentence))
 
 