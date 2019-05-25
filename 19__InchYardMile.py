#  19.	Write a Python program to convert the distance (in feet) to inches, yards, and miles. \
#       1 feet = 12 inches, 3 feet = 1 yard, 5280 feet = 1 mile

ft = int(input("Enter the distance in feet: "))
inches = ft * 12
yards = ft / 3
miles = ft / 5280

print("The distance in inches is: " + str(inches))
print("The distance in yards is:  " + str(yards))
print("The distance in miles is:  " + str(miles))

