# Problem Statement
# Write a Python program to generate the next 15 leap years starting from a given year. 
# Populate the leap years into a list and display the list. 

# Check if year is leap year then return true
def is_leap_year(year):
    if (year%4 == 0 and year % 100 != 0) or (year%400 == 0):
        return True
    else:
        return False

# loop it till the list is less than 15
def leap_years(start_year):
    leap_years_list = []
    year = start_year
    while len(leap_years_list) < 15:
        #if its true append to the leap year list 
        if is_leap_year(year):
            leap_years_list.append(year)
        year += 1
    return leap_years_list

print(leap_years(2000))
