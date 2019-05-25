#  17.	Write a Python program to convert height (in feet and inches) to centimetres.


ft = int(input("Enter the height in Feet: "))
inch = int(input("Enter the Height in Inches: "))

inch = inch + (ft * 12)
cm = round(inch * 2.54, 1)

print("Your height is :  " + str(cm)+" cm.")
