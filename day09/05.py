#  Problem Statement
# Validate the name based on the below conditions using regular expression in the checkNameValidity() method.
# The length of the name should be between 2 and 30 characters (both inclusive)
# The name can contain only alphabets and spaces
# The first character of each word of the name should be an upper case alphabet
# Each word should be separated by a space
# The name should not start or end with a space
# Special characters should not be allowed
# Return true if the name is valid, else return false.
# Sample Input and Output

import re
def fn(string):
    # pattern = "{2,30}[A-Z][a-z](" ") ^[A-Z]"
    pattern = r"^[A-Z][a-zA-Z]*(?: [A-Z][a-zA-Z]*){0,29}$"

    if re.fullmatch(pattern,string):
        return True
    else :
        return False
print(fn("Yash"))