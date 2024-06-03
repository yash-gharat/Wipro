# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". 
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

# string = "yash"
# print(len(string))

password = str(input("Enter the password you what to check \n"))
length = len(password)


if(length < 6):
    print("Password is weak")
elif(length >= 6 and length <= 10):
    print("Password is medium")
elif(length > 10):
    print("Password is strong")
