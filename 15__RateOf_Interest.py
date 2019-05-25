#  15.	Write a Python program to compute the future value of a specified principal amount,
#  rate of interest, and a number of years.

amount = int(input('Enter the amount:  '))
interest = int(input('Enter the Interest:  '))
years = int(input('Enter the years:  '))

futureValue  = amount*((1+(0.01*interest)) ** years)

print(futureValue)