# Quantifier - identifies how many times a char should occur

# a - exactly one a
# a* - 0 or more times
# a+ - one or more times
# a? - 0 or one time
# a{n} -exactly n time
# a{n,} -exactly at least 1 n time
# a{n,m} element from n to m time
# . any char
# ^ starts with
# $ ends with

import re
text = "The rain in spain"
#findall() function returns a list contaonong all matcher

x = re.findall('ai',text)
y = re.search('ai',text)
z = re.fullmatch('ai',text)
print(x)
print(y)
print(z)
print(text[y.start():y.end()])
# print(text[z.start():z.end()])
