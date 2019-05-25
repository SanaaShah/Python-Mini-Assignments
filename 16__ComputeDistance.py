#  16.	Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).


import math
x = [4, 0]
y = [6, 6]
distance = math.sqrt(((x[0]-y[0])**2)+((x[1]-y[1])**2))

print(distance)