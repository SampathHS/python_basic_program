
import math

radius = eval(input("Enter a positive value to find the area:"))

try:
    if radius < 0:
        raise ValueError
    else:
        areaOfCircle = math.pi * radius ** 2
        print("The area of a circle is:=",areaOfCircle)
except ValueError: 
    print(ValueError)
    print("For finding the area of a circle\nRadius cannot be a Negative value...")


