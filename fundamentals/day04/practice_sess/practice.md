# Practice Session
Q1 of 3outlined_flag
```
Consider the following list of pan card numbers:
pancard_list=["AABGT6715H", "UFFAC4352T", "IFSBD9163K", "JOOEC1225H","RWXAFE187B"]

What is the output of the below two print statements?

print(pancard_list[3][6], end=" ")

print(pancard_list[4][3:])

A. 9 OEC1225H

B. 2 AFE187B

C. 9163K O
 
D. 225H A

sol -
JOOEC1225H
2
RWXAFE187B
AFE187B
2 , AFE187B
```
 
 
 
Q2 of 3
```
What is the output of the code given below?
 
message="welcome to Mysore"         #
word=message[-7:]               #  Mysore
if(word=="mysore"):
    print("got it")
else:
    message=message[3:14]
    print(message)              #come to Mysore

 
A. come to Myso
B. come to Mys
C. lcome to Mys
D. lcome to Myso



 ```
 
Q3 of 3
 
What is the output of the below code?
 
```
song="JINGLE Bells jingle Bells Jingle All The Way"
song.upper()
song_words=song.split()
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)

 
A.0
B.3
C.2
D.1

JINGLE Bells jingle Bells Jingle All The Way
[JINGLE Bells jingle Bells Jingle All The Way]

1
```
<hr>

# Set 2

```
1.Find the Length of a String

2.Avoid Spaces in String Length

3.Print Even Length Words in a String

4.Print First Half of the String in Uppercase and the Next Half in Lowercase

5.Capitalize the Alternative Characters of the String

6.First and Last Characters of Each Word in a String

7.Count the Number of Digits, Alphabets, and Other Characters in a String

8.Check if a String Starts With the Alphabet and Has Digits

9.Count the Number of Vowels in a String

10.Remove All Duplicate Words From a Given String

11.Print the Character with Maximum Frequency in a String

12.Print the Frequency of Each Character in String

13.Remove ith Character From the String

14.Split and Join a String

15.Replace Commas with Whitespace Character in a Given String
```

```
Write a python program which displays the count of the names that matches a given pattern from a list of names provided.
Consider the pattern characters to be:
1. "_ at" where "_" can be one occurrence of any character
2. "%at%" where "%" can have zero or any number of occurrences of a character
 
Sample Input

[Hat, Cat, Rabbit, Matter]
	
Expected Output

_at -> 2
%at% -> 3

```
```
[02:58 pm] Ashutosh  (Unverified)
Write a function, check_palindrome() to check whether the given string is a palindrome or not. The function should return true if it is a palindrome else it should return false.
Note: Initialize the string with various values and test your program. Assume that all the letters in the given string are all of the same case. Example: MAN, civic, WOW etc.
[02:58 pm] Ashutosh  (Unverified)
Problem Statement
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program
 
	


Sample Input
AAAABBBBCCCCCCCC
	
AABCCA


Expected Output
4A4B8C
	
2A1B2C1A
 
```
 