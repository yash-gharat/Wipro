# Write a python program that displays a message as follows for a given number:
# If it is a multiple of three, display "Zip"
# If it is a multiple of five, display "Zap".
# If it is a multiple of both three and five, display "Zoom".
# If it does not satisfy any of the above given conditions, display "Invalid".

    # if(number % 3 ==0):
    #     return "Zip"
    # elif(number % 5 ==0):
    #     return "Zap"
    # elif(number % 3 == 0 and number %5 ==0):
    #     return "Zoom"
def zip_zap_zoom(number):
    if(number % 3 == 0 and number % 5 == 0):
        return "Zoom"
    elif(number % 3 == 0):
        return "Zip"
    elif(number % 5 == 0):
        return "Zap"
    else:
        return "Invalid"

number = 15
res = zip_zap_zoom(number)
print(res)