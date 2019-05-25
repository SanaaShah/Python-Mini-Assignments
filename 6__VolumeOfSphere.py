#  6. Write a Python program to get the volume of a sphere, please take the radius as input from user. V=4 / 3 πr3

from math import pi

radius = input('Please enter the radius:  ')
volume = 4 / (4 * pi * 3)
print('Volume of the sphere is found to be: '+str(round(volume, 2)))
