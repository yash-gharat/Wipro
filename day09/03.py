import re
s1 = "bob has a birthday on Feb 25th"
s2 = "sara has a birthday on Feb 25th"
s3 = "12eup 586iu"
s4 = "0turt"

pattern_one= re.compile("\w+\d")
pattern_two= re.compile("\d")
x = pattern_one.search(s1) 
y = pattern_two.search(s2) 
print(x)
print(y)