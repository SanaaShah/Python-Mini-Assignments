#  15.	Write a Python program to compute the future value of a specified principal amount,
#  rate of interest, and a number of years.

amount = int(input('Enter the amount:  '))
interest = float(input('Enter the Interest:  '))
years = int(input('Enter the years:  '))

future_value = amount * (pow((1 + interest / 100), years))

print(future_value)