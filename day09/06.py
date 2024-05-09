# roblem Statement
# Validate the password based on the below conditions using regular expression in the checkPasswordValidity() method.
# The length of the password should be between 8 and 20 characters (both inclusive)
# The password must contain minimum one lower case alphabet, one upper case alphabet, one digit and one special character
# The password can contain only the following special characters.
#      [ !, @, #, $, %, &, *, _]
# Return true if the password is valid, else return false.
# Test the functionalities using the main method of the Tester class.
import re
def checkPasswordValidity(password):
    # pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%&*_])[A-Za-z\d!@#$%&*_]{8,20}$"
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%&*_])[A-Za-z\d!@#$%&*_]{8,20}"
    
    if re.fullmatch(pattern,password):
        return True
    else:
        return False
print(checkPasswordValidity("P@SSWorD1"))