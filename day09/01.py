import re

pattern = re.compile("python")
text = "Python is a beginer friendly language and python is high level language"  
# print(pattern)

matcher = pattern.finditer(text)

# for match in matcher:
#     print(match.start(),"---",match.end(),"---",match.group())

pattern1 = "[a-z]"
matcher1 = re.finditer(pattern1,"01cdeaghb")
for match in matcher1:
    print(match.start(),"---",match.end(),"---",match.group())

# [a-z]
# [A-Z]
# [a-zA-Z]
# [0-9]
# [a-zA-Z0-9]
# [^a-zA-Z0-9]