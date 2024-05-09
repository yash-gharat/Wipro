# 4. Function Returning Multiple Values
# Problem: 
# Create a function that returns both the area and circumference of a circle 
# given its radius.
import math
def circle(radius):
    area = math.pi * (radius ** 2)
    circumferencce = 2 * math.pi * radius
    return(area,circumferencce)
print(circle(2))
