
# Write a python function to add 'ing' at the end of a given string and return the new string. 
# If the given string already ends with 'ing' then add 'ly'.
# If the length of the given string is less than 3, leave it unchanged.
 
# Sample Input
# sleep
# amazing
# is
	
# Expected Output
# sleeping
# amazingly
# is



def add_string(str1):

  #start writing your code here
  if len(str1) < 3:
      return str1
  elif str1.endswith("ing"):
      return (str1+"ly")
  else:
      return(str1 +"ing")      
 
str1="sleep"
# str1="amazing"
# str1="is"

print(add_string(str1))



