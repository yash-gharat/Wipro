# Given a string containing uppercase characters (A-Z), 
# compress the string using Run Length encoding. 
# Repetition of character has to be replaced by storing the length of that run.

def run_length_encoding(string):
    #init empty string to store encode val
    compressed_string = ""
    count = 1
    char = string[0]
    # print(char)

    for i in range(0,len(string)):
        if string[i] == char:
            count += 1
        else:
            compressed_string += str(count) + char
            char = string[i]
            count = 1

    # Add
    compressed_string += str(count) + char
    print(compressed_string)

string = "AAAABBBBCCCCCCCC" #4A4B8C
run_length_encoding(string)
