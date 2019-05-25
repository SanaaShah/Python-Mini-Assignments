#  1. Write a Python program which accepts the radius of a circle from the user and compute the area

from math import pi

radius = float((input('Please enter the radius of the cricle: ')))
print('Area of the circle of radius: '+str(radius) + ' is found to be: '+str(round((pi * radius**2), 2)))



