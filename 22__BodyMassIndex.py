#  22.	Write a Python program to calculate body mass index.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
print("Your body mass index is: "+ str(round(weight / (height * height), 2)))
