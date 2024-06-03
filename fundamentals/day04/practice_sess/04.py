# Write a function, check_palindrome() to check whether the given string is a palindrome or not. 
# The function should return true if it is a palindrome else it should return false.
# Note: Initialize the string with various values and test your program. 
# Assume that all the letters in the given string are all of the same case. Example: MAN, civic, WOW etc.

#eg WOW = WOW on reverse

def check_palindrome(string):
    if(string == string[::-1]):
        print(string ,"is a palindrome")
    else: 
        print(string ,"is a not palindrome")
check_palindrome("WOW")
check_palindrome("MAN")
check_palindrome("CIVIC")