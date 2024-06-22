# vowel are not allowed in password
# passwords are in a list

passwords = ["password1", "xyz", "123","a"]
vowels = "aeiou"

result = [
    password for password in passwords if any(char in vowels for char in password)
]

print(result)
