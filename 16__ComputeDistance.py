#  16.	Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).


import math

x = int(input('Please enter 1st X co-ordinate: '))
x1 = int(input('Please enter 2nd X co-ordinate: '))
y = int(input('Please enter 1st Y co-ordinate: '))
y1 = int(input('Please enter 2nd Y co-ordinate:  '))

distance = math.sqrt(((x-y)**2)+((x1-y1)**2))

print(distance)